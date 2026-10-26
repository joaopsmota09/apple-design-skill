# apple-design: a Claude Code skill for Apple design, always current

Design, build and review interfaces that follow Apple's **current** Human Interface Guidelines (including Liquid Glass) for iOS, iPadOS,
macOS, watchOS, tvOS, visionOS and iPhone Duo, in SwiftUI, UIKit and AppKit, and for **web or desktop-browser apps that should feel
Apple-native**.

What makes it different from a static skill: it fetches Apple's live guidelines from developer.apple.com into a local cache and tells
you what Apple changed recently, so answers come from the current text instead of from memory.

## Install
```bash
git clone https://github.com/joaopsmota09/apple-design-skill ~/.claude/skills/apple-design
python3 ~/.claude/skills/apple-design/scripts/refresh.py      # builds the local cache (about 3 minutes, public pages only)
```
Start a new Claude Code session. The skill triggers on requests about Apple design, HIG, Liquid Glass, SF Symbols, native-feeling UI, and design reviews.
Update later with `git pull` and `python3 scripts/refresh.py`. Requires Python 3.8+ (standard library only).

## What is inside
| Path | What |
| --- | --- |
| `SKILL.md` | The router: freshness check, targeting questions, which reference to load, non-negotiable design rules, output rules |
| `references/foundations-visual.md` | Color (current system palette), Dark Mode, type scales, Liquid Glass and materials, motion, layout, icons, branding |
| `references/navigation-and-structure.md` | Tab bars, sidebars, toolbars, split views, windows, sheets, popovers, scroll edge effects, search |
| `references/controls-and-content.md` | Buttons, toggles, menus, lists, alerts, progress, charts |
| `references/accessibility-and-language.md` | Control sizes, contrast minimums, writing, inclusion, right-to-left, privacy |
| `references/patterns.md` | Onboarding, settings, feedback, undo, drag and drop, notifications, accounts |
| `references/platforms-inputs-system.md` | Platform characteristics, inputs, widgets, Live Activities, AI, Siri, iPhone Duo |
| `references/web-translation.md` | How to get an Apple-native feel on the web and desktop browsers, with the licensing limits |
| `references/review-checklist.md` | Scored review (out of 10) plus Liquid Glass era checks |
| `references/whats-new.md` | Dated changes in Apple's guidance (2025 to 2026) |
| `scripts/refresh.py` | Polite crawler for the public HIG JSON, ETag-aware, writes Markdown cache and a change report |
| `scripts/digest.py` | Skims cached pages: rules, numbers, small tables; search across all pages |

## How it stays current
`refresh.py` reads the same public JSON that developer.apple.com renders (the HIG index plus every page, Apple's Liquid Glass articles,
and the `/design/` and `/design/resources/` pages), waits 0.6 s between requests, identifies itself and skips unchanged pages. Every page
carries an Apple "last updated" flag; `python3 scripts/refresh.py --status` lists pages flagged in the last 180 days.

## Legal
- The cache contains Apple's copyrighted text and is **git-ignored**: it stays on your machine. Do not redistribute it.
- Everything tracked here is original summary, tooling and guidance. Apple and its product and technology names are Apple's trademarks;
  this project is not affiliated with Apple. Apple's fonts and SF Symbols have their own licenses (see `references/web-translation.md`).
- Released under the MIT License (original work only). See `LICENSE` and `NOTICE.md`.
