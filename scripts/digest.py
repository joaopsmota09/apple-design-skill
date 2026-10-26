#!/usr/bin/env python3
"""Skim cached HIG pages: headings, the bold rule sentences (with their first explanatory sentence), lines that
carry numbers (points, percentages, ratios, durations) and small tables. Much shorter than reading a whole page.

    python3 scripts/digest.py sidebars tab-bars        # one or more slugs
    python3 scripts/digest.py --max 40 sidebars               # cap each page at 40 printed lines
    python3 scripts/digest.py --skip tvOS,watchOS,visionOS buttons   # drop platform sections you do not need
    python3 scripts/digest.py --full buttons           # whole page text, images and link lists removed
    python3 scripts/digest.py --find "scroll edge"     # which pages mention a phrase (with the matching line)
    python3 scripts/digest.py --list                   # all cached slugs by group
Run scripts/refresh.py first if the cache is empty.
"""
import json
import re
import sys
from pathlib import Path

CACHE = Path(__file__).resolve().parent.parent / "cache"
NUM = re.compile(r"\b\d+(\.\d+)?\s?(pt|points?|px|pixels?|%|:1|ms|seconds?|fps|dp|hz)\b|\b\d+\s?x\s?\d+\b", re.I)
STOP = ("## Resources", "### Resources", "## Related", "## Videos", "## Developer documentation", "## Change log", "### Change log")


def body(slug):
    f = CACHE / "hig" / f"{slug}.md"
    if not f.exists():
        sys.exit(f"no cached page '{slug}'. Try --list, or run scripts/refresh.py")
    out = []
    for line in f.read_text().splitlines():
        if line.startswith(STOP):
            break
        if line.strip() and not line.startswith("[image:") and not line.startswith("Source:"):
            out.append(line)
    return out


def first_sentence(text):
    m = re.search(r"(?<=[.!?])\s+(?=[A-Z])", text)
    return text[:m.start()] if m else text


LIMIT = [0]


def digest(slug, skip=()):
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        _digest(slug, skip)
    out = buf.getvalue().splitlines()
    if LIMIT[0] and len(out) > LIMIT[0]:
        out = out[:LIMIT[0]] + [f"  ... (+{len(out) - LIMIT[0]} more lines; use --full {slug})"]
    print("\n".join(out))


def _digest(slug, skip=()):
    lines = body(slug)
    print(f"=== {slug}")
    in_table = 0
    skip_level = None
    for line in lines:
        m = re.match(r"(#+) (.*)", line)
        if m and skip:
            level = len(m.group(1))
            if skip_level is not None and level <= skip_level:
                skip_level = None
            if skip_level is None and level >= 3 and any(k.lower() in m.group(2).lower() for k in skip):
                skip_level = level
        if skip_level is not None:
            continue
        if line.startswith("# "):
            print(line)
        elif line.startswith(("Platforms:", "Apple flagged", "Group:")):
            print(line)
        elif line.startswith("#"):
            print("\n" + line)
            in_table = 0
        elif line.startswith("|"):
            in_table += 1
            if in_table <= 14:
                print(re.sub(r"\[image:[^\]]*\]", "", line)[:200])
        elif line.startswith("**"):
            m = re.match(r"\*\*(.+?)\*\*\s*(.*)", line)
            if m:
                rest = first_sentence(m.group(2))
                print(f"- {m.group(1)}" + (f" {rest[:240]}" if rest and len(m.group(1)) < 90 else ""))
        elif line.startswith(("- ", "> ")) and NUM.search(line):
            print(line[:260])
        elif NUM.search(line) and not line.startswith("*"):
            print("  ~ " + first_sentence(line)[:240] if len(line) > 260 else "  ~ " + line[:260])
        else:
            in_table = 0


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "--list":
        m = json.loads((CACHE / "MANIFEST.json").read_text())["pages"]
        groups = {}
        for s, p in m.items():
            groups.setdefault(p["group"], []).append(s)
        for g, v in sorted(groups.items()):
            print(f"[{g}] " + ", ".join(sorted(v)))
    elif a[0] == "--find":
        q = " ".join(a[1:]).lower()
        for f in sorted((CACHE / "hig").glob("*.md")):
            for line in f.read_text().splitlines():
                if q in line.lower() and not line.startswith(("[image:", "Source:")):
                    print(f"{f.stem}: {line[:220]}")
                    break
    elif a[0] == "--full":
        for s in a[1:]:
            print(f"=== {s}\n" + "\n".join(l[:900] for l in body(s)))
    else:
        skip = ()
        while a and a[0] in ("--skip", "--max"):
            if a[0] == "--skip":
                skip = tuple(a[1].split(","))
            else:
                LIMIT[0] = int(a[1])
            a = a[2:]
        for s in a:
            digest(s, skip)


if __name__ == "__main__":
    main()
