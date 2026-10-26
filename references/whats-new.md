# What changed recently (from Apple's own update flags)

Snapshot taken 2026-10-26 from `cache/MANIFEST.json`. Re-derive anytime with `python3 scripts/refresh.py --status`, which lists every page
Apple flagged in the last 180 days. Older skills and training data predate most of this, so check here before relying on memory.

## Design language: Liquid Glass (WWDC 2025 onward)
- 2025-09: `materials` and `motion` updated. 2025-12: `color`, `buttons`, `toolbars` updated for Liquid Glass. 2026-06: `app-icons` refined.
- The shift: controls and navigation sit in a translucent **functional layer** above flat content; scroll edge effects replace solid bar
  backgrounds; color on glass is sparse and applied to a primary control's background; concentric rounded shapes follow the hardware.
  Details: `foundations-visual.md`, `cache/hig/doc-liquid-glass.md`, `cache/hig/doc-adopting-liquid-glass.md`.

## June 2026 batch (iOS 27 / macOS 27 generation; Apple's design kits are now "iOS and iPadOS 27" and "macOS 27")
- **design-principles reintroduced** (purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, delight).
- **sidebars**: new guidance on sidebar icon colors (accent by default, fixed color only with meaning) and the adaptable sidebar style.
- **tab-bars**: terminology and art updated. **search-fields / searching**: terminology and search as a tab in iOS.
- **scroll-views**: scroll edge effects guidance. **menus**: menu item icons (all items in a group or none).
- **snippets**: new component page. **app-shortcuts**: adopt app schemas. **siri**: revised for Siri AI.
- **generative-ai**: refine results and feedback during generation, model-type choice. **wallet**: iOS 27 and the Pass Designer app. **apple-pay**: refreshed.

## September 2026
- **layout** updated to current best practices. **branding**: brand color guidance refined.
- **designing-for-iphone-duo**: new page for a two-display, hinged iPhone (poses, reserved regions, side-mounted toolbars and tab bars).
- **apple-in-app-purchase** rebranded and refined (2026-09-17). **shareplay** reorganized.

## October 2026
- **widgets** (2026-10-13): Apple HomeView guidance, watchOS specs. **live-activities** (2026-10-13): limited-width layouts, platform list, specs.

## Earlier but still relevant
- 2026-03-24 **sheets**: button placement. 2025-12-16 **typography**: emphasized weights per text style; **writing**: language patterns, possessives.
- 2025-07 **sf-symbols**: Draw animations and gradient rendering (SF Symbols 7). 2025-06 **accessibility**: Assistive Access, Switch Control,
  Accessibility Nutrition Labels; **windows**, **split-views**, **the-menu-bar** (iPadOS menu bar), **multitasking** for resizable iPad windows;
  **going-full-screen**; **icons** table of standard action symbols.

## How to stay current
1. `python3 scripts/refresh.py` (polite, ETag-aware, about 3 minutes cold, seconds when nothing changed).
2. Read `cache/CHANGES.md` for what changed since the last run and `--status` for Apple's own flags.
3. If a page matters to the task, `python3 scripts/digest.py <slug>` or open `cache/hig/<slug>.md`.
