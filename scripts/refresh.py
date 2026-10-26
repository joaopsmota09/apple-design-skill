#!/usr/bin/env python3
"""Refresh the local cache of Apple's design guidance and report what changed.

Reads Apple's public HIG JSON (the same data the website renders), converts each page to Markdown under
cache/hig/, writes cache/rules/ (the bold rule headlines only, quick to scan), cache/MANIFEST.json and
cache/CHANGES.md. Also saves the text and links of /design/ and /design/resources/.

    python3 scripts/refresh.py              # polite crawl; unchanged pages are skipped via ETag
    python3 scripts/refresh.py --force      # re-download everything
    python3 scripts/refresh.py --only color,materials
    python3 scripts/refresh.py --status     # show cache age and recently updated pages, no network

Be polite: one request per --delay seconds (default 0.6). The cache is for personal use. It holds Apple's
copyrighted text, so do not redistribute it; the skill's own references/ files are original summaries.
Standard library only.
"""
import argparse
import hashlib
import html.parser
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache"
BASE = "https://developer.apple.com"
UA = "apple-design-skill/1.0 (personal-use cache; polite crawler)"
INDEX = "/tutorials/data/index/design--human-interface-guidelines"
HIG_JSON = "/tutorials/data/design/human-interface-guidelines/{slug}.json"
# Apple articles outside the HIG that matter for current design language (documentation JSON, same format).
EXTRA = {
    "doc-liquid-glass": "/tutorials/data/documentation/technologyoverviews/liquid-glass.json",
    "doc-adopting-liquid-glass": "/tutorials/data/documentation/technologyoverviews/adopting-liquid-glass.json",
}
HTML_PAGES = {"design-home": "/design/", "design-resources": "/design/resources/"}


def get(path, etag=None, retries=3):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": UA, **({"If-None-Match": etag} if etag else {})})
    for i in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, r.read(), r.headers.get("ETag")
        except urllib.error.HTTPError as e:
            if e.code == 304:
                return 304, b"", etag
            if e.code in (429, 503):
                time.sleep(5 * (i + 1))
                continue
            return e.code, b"", None
        except (urllib.error.URLError, TimeoutError):
            time.sleep(2 * (i + 1))
    return 0, b"", None


# ---------------- DocC JSON -> Markdown ----------------
UNHANDLED = {}  # block type -> pages where the converter found content it does not know how to render
CURRENT_PAGE = [""]
KNOWN_SKIP = {"image", "video", "thematicBreak", "dictionaryExample", "endpointExample"}

def title_of(ident, refs):
    r = refs.get(ident) or {}
    return r.get("title") or ident.rsplit("/", 1)[-1].replace("-", " ")


def inline(nodes, refs):
    out = []
    for n in nodes or []:
        t = n.get("type")
        if t == "text":
            out.append(n.get("text", ""))
        elif t == "codeVoice":
            out.append("`" + n.get("code", "") + "`")
        elif t == "strong":
            out.append("**" + inline(n.get("inlineContent"), refs).strip() + "**")
        elif t == "emphasis":
            out.append("*" + inline(n.get("inlineContent"), refs).strip() + "*")
        elif t == "reference":
            out.append(n.get("overridingTitle") or title_of(n.get("identifier", ""), refs))
        elif t == "link":
            out.append(f"[{n.get('title') or n.get('destination')}]({n.get('destination')})")
        elif t == "image":
            alt = (refs.get(n.get("identifier")) or {}).get("alt")
            out.append(f"[image: {alt}]" if alt else "")
        elif "inlineContent" in n:
            out.append(inline(n["inlineContent"], refs))
    return "".join(out)


def blocks(items, refs, depth=0):
    out = []
    for b in items or []:
        t = b.get("type")
        if t == "heading":
            out.append("\n" + "#" * (b.get("level", 2) + 1) + " " + b.get("text", "") + "\n")
        elif t == "paragraph":
            s = inline(b.get("inlineContent"), refs).strip()
            if s:
                out.append(s + "\n")
        elif t in ("unorderedList", "orderedList"):
            for i, it in enumerate(b.get("items", []), 1):
                body = " ".join(x.strip() for x in blocks(it.get("content"), refs, depth + 1) if x.strip())
                out.append("  " * depth + (f"{i}. " if t == "orderedList" else "- ") + body)
            out.append("")
        elif t == "aside":
            body = " ".join(x.strip() for x in blocks(b.get("content"), refs) if x.strip())
            out.append(f"> **{b.get('name') or b.get('style', 'Note').title()}** {body}\n")
        elif t == "table":
            rows = b.get("rows", [])
            if rows:
                cells = [[" ".join(x.strip() for x in blocks(c, refs) if x.strip()).replace("|", "/") for c in r] for r in rows]
                out.append("| " + " | ".join(cells[0]) + " |")
                out.append("|" + "---|" * len(cells[0]))
                out += ["| " + " | ".join(r) + " |" for r in cells[1:]]
                out.append("")
        elif t == "codeListing":
            out.append("```\n" + "\n".join(b.get("code", [])) + "\n```\n")
        elif t == "row":
            for col in b.get("columns", []):
                out += blocks(col.get("content"), refs, depth)
        elif t == "tabNavigator":
            for tab in b.get("tabs", []):
                out += blocks(tab.get("content"), refs, depth)
        elif t == "small":
            s = inline(b.get("inlineContent"), refs).strip()
            if s:
                out.append("*" + s + "*\n")
        elif t == "links":
            out += [f"- {title_of(i, refs)}" for i in b.get("items", [])] + [""]
        elif "content" in b:
            out += blocks(b["content"], refs, depth)
        elif t not in KNOWN_SKIP:
            UNHANDLED.setdefault(t, set()).add(CURRENT_PAGE[0])
    return out


def rule_headlines(items, refs):
    """Apple writes its guidance as paragraphs that open with a bold sentence; collect those, grouped by heading."""
    out, current = [], ""
    def visit(items):
        nonlocal current
        for b in items or []:
            t = b.get("type")
            if t == "heading":
                current = b.get("text", "")
                out.append(f"\n## {current}")
            elif t == "paragraph" and b.get("inlineContent") and b["inlineContent"][0].get("type") == "strong":
                out.append("- " + inline(b["inlineContent"][:1], refs).strip("* "))
            elif t in ("unorderedList", "orderedList"):
                for it in b.get("items", []):
                    visit(it.get("content"))
            elif "content" in b:
                visit(b["content"])
            elif t == "tabNavigator":
                for tab in b.get("tabs", []):
                    visit(tab.get("content"))
            elif t == "row":
                for col in b.get("columns", []):
                    visit(col.get("content"))
    visit(items)
    return "\n".join(out).strip()


def convert(doc, slug, group):
    refs = doc.get("references", {})
    meta = doc.get("metadata", {})
    custom = meta.get("customMetadata", {})
    content = []
    for sec in doc.get("primaryContentSections", []):
        content += sec.get("content", [])
    body = "\n".join(blocks(content, refs))
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    abstract = inline(doc.get("abstract"), refs).strip()
    head = [f"# {meta.get('title', slug)}", "",
            f"Source: {BASE}/design/human-interface-guidelines/{slug}" if not slug.startswith("doc-") else f"Source: {BASE}/documentation/technologyoverviews/{slug[4:]}",
            f"Group: {group}", f"Platforms: {custom.get('supported-platforms', 'n/a')}"]
    if custom.get("alert-date"):
        head.append(f"Apple flagged update: {custom['alert-date']} - {custom.get('alert-text', '')}")
    head += ["", abstract, "", body]
    return "\n".join(head) + "\n", rule_headlines(content, refs), custom


def index_pages():
    status, raw, _ = get(INDEX)
    if status != 200:
        sys.exit(f"could not fetch the HIG index (HTTP {status})")
    langs = json.loads(raw)["interfaceLanguages"]
    tree = langs.get("swift") or next(iter(langs.values()))
    pages = []
    def walk(nodes, trail):
        for n in nodes:
            path = n.get("path", "")
            if n.get("type") in ("article",) and path.startswith("/design/human-interface-guidelines/"):
                pages.append((path.rsplit("/", 1)[-1], " > ".join(trail), n.get("title")))
            walk(n.get("children") or [], trail + ([n["title"]] if n.get("title") and n.get("type") == "collection" else []))
    walk(tree, [])
    return pages


# ---------------- plain HTML pages ----------------
class Text(html.parser.HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "head", "nav", "footer"}

    def __init__(self):
        super().__init__()
        self.out, self.skip, self.href = [], 0, None

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        if tag == "a":
            self.href = dict(attrs).get("href")
        if tag in ("h1", "h2", "h3", "li", "p", "br", "div", "section"):
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        if tag == "a":
            self.href = None

    def handle_data(self, data):
        if self.skip:
            return
        s = " ".join(data.split())
        if s:
            self.out.append(s + (f" <{self.href}>" if self.href and self.href.startswith(("http", "/")) else "") + " ")


def html_to_text(raw):
    p = Text()
    p.feed(raw.decode("utf-8", "replace"))
    return re.sub(r"\n\s*\n+", "\n\n", "".join(p.out)).strip()


# ---------------- main ----------------
def load_manifest():
    f = CACHE / "MANIFEST.json"
    return json.loads(f.read_text()) if f.exists() else {"pages": {}, "refreshed": None}


def status():
    m = load_manifest()
    if not m["refreshed"]:
        print("No cache yet. Run: python3 scripts/refresh.py")
        return
    age = datetime.now(timezone.utc) - datetime.fromisoformat(m["refreshed"])
    print(f"Cache refreshed {m['refreshed']} ({age.days} days ago), {len(m['pages'])} pages.")
    cutoff = (datetime.now(timezone.utc) - timedelta(days=180)).date().isoformat()
    recent = sorted(((p["alertDate"], s, p["alertText"]) for s, p in m["pages"].items() if p.get("alertDate", "") >= cutoff), reverse=True)
    print(f"Pages Apple flagged as updated in the last 180 days ({len(recent)}):")
    for d, s, t in recent:
        print(f"  {d}  {s}: {t}")
    if age.days > 30:
        print("The cache is older than 30 days: consider re-running refresh.py.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", help="comma-separated page slugs")
    ap.add_argument("--delay", type=float, default=0.6)
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    if a.status:
        return status()
    for d in ("hig", "rules"):
        (CACHE / d).mkdir(parents=True, exist_ok=True)
    old = load_manifest()
    new = {"pages": {}, "refreshed": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    pages = index_pages()
    only = set(a.only.split(",")) if a.only else None
    todo = [(s, g, t, HIG_JSON.format(slug=s)) for s, g, t in pages] + [(s, "Technology overviews", s, p) for s, p in EXTRA.items()]
    added, changed, removed, failed = [], [], [], []
    for n, (slug, group, title, path) in enumerate(todo, 1):
        prev = old["pages"].get(slug, {})
        if only and slug not in only:
            if prev:
                new["pages"][slug] = prev
            continue
        status_code, raw, etag = get(path, None if a.force else prev.get("etag"))
        time.sleep(a.delay)
        if status_code == 304 and prev:
            new["pages"][slug] = prev
            continue
        if status_code != 200:
            failed.append((slug, status_code))
            if prev:
                new["pages"][slug] = prev
            continue
        CURRENT_PAGE[0] = slug
        md, rules, custom = convert(json.loads(raw), slug, group)
        digest = hashlib.sha256(md.encode()).hexdigest()[:16]
        (CACHE / "hig" / f"{slug}.md").write_text(md)
        (CACHE / "rules" / f"{slug}.md").write_text(f"# {title}: rule headlines\n\n{rules}\n")
        new["pages"][slug] = dict(title=title, group=group, etag=etag, hash=digest, alertDate=custom.get("alert-date", ""),
                                  alertText=custom.get("alert-text", ""), fetched=new["refreshed"])
        (added if not prev else changed if prev.get("hash") != digest else []).append(slug)
        if n % 25 == 0:
            print(f"  {n}/{len(todo)} pages", flush=True)
    removed = [s for s in old["pages"] if s not in new["pages"]]
    for name, path in HTML_PAGES.items():
        code, raw, _ = get(path)
        time.sleep(a.delay)
        if code == 200:
            (CACHE / f"{name}.md").write_text(f"# {name}\n\nSource: {BASE}{path}\n\n{html_to_text(raw)}\n")
        else:
            failed.append((name, code))
    (CACHE / "MANIFEST.json").write_text(json.dumps(new, indent=1))
    if UNHANDLED:
        print("WARNING: block types the converter does not render (content may be missing):")
        for t, pgs in UNHANDLED.items():
            print(f"  {t}: {sorted(pgs)[:6]}{' ...' if len(pgs) > 6 else ''}")
    lines = [f"# Changes at {new['refreshed']}", "", f"Added {len(added)}, changed {len(changed)}, removed {len(removed)}, failed {len(failed)}.", ""]
    for label, items in (("Added", added), ("Changed", changed), ("Removed", removed)):
        if items:
            lines += [f"## {label}"] + [f"- {s}" for s in items] + [""]
    if failed:
        lines += ["## Failed"] + [f"- {s}: HTTP {c}" for s, c in failed]
    (CACHE / "CHANGES.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:3]))
    status()


if __name__ == "__main__":
    main()
