# Navigation, windows and presentation

Original summary. Full text: `cache/hig/<slug>.md`. Dates are Apple's own "last updated" flags.

## Choosing the top-level structure
- **Tab bar** = navigate between peer sections of the app (never a place for actions). **Sidebar** = navigate areas or
  top-level collections when there is room for it (iPad, Mac, large windows). **Split view** = list plus detail
  (two or three panes). Many apps use the adaptable style that shows a tab bar when narrow and a sidebar when wide
  (`sidebars`, `tab-bars`, both updated 2026-06-08 for iOS 27).
- Layout rule behind it: change *how much* is visible with available space, never *what the app can do*.
- Desktop web translation: a left sidebar for 4 to 7 sections at wide widths, a bottom tab bar below ~900 px. See `web-translation.md`.

## Tab bars  (`tab-bars`, 2026-06-08)
- Navigation only. Keep it visible while moving through the app; do not hide or disable a tab when its content is empty.
- As few tabs as the hierarchy needs; avoid overflow tabs. Always label tabs; SF Symbols for the icons.
- Badge (red oval with a number or "!") only for information that needs attention. Do not give labels a color similar to
  bright content behind a translucent bar; prefer the monochrome look then.
- iPadOS: prefer a tab bar first, let people customize it. visionOS: vertical bar with symbol plus text label; a sidebar inside a tab is fine.

## Sidebars  (`sidebars`, 2026-06-08 icon-color and adaptable-style update)
- At most **two levels** of hierarchy; if deeper, use a split view with a content list in the middle. Short group titles.
- Let people hide it (macOS: a button and View-menu commands; iPadOS: edge swipe) but do not hide it by default.
- Let people customize contents where it makes sense; use disclosure controls for large hierarchies; familiar SF Symbols.
- Sidebar icons use the accent color by default and follow the user's macOS accent choice; fixed colors only when the
  color carries meaning (for example Mail's yellow VIP star).
- Let rich content extend beneath the sidebar (it floats in the Liquid Glass layer). macOS row height and glyph size follow
  the small, medium or large sidebar-size setting. Never put critical actions at the bottom of a sidebar. Consider
  auto-collapsing when the window narrows.

## Toolbars  (`toolbars`, 2025-12-16)
- Few items, grouped by function and frequency; keep navigation and critical actions (Done, Close, Save) in distinct
  groups; keep text-label actions apart from icon actions so they do not read as one control.
- Put extra actions in a More menu. Prefer system symbols without borders; use the prominent style for the key action
  (Done, Submit). Minimize custom bar backgrounds and tint.
- Titles: useful, concise (under about 15 characters), never the app name. Use the standard Back and Close buttons.
- iOS: large title that collapses on scroll. macOS: **every toolbar item must also exist as a menu-bar command**
  (toolbars can be customized or hidden). iPadOS: toolbar and tab bar may share the top row.

## Split views and windows  (`split-views` 2025-06-09, `windows` 2025-06-09)
- Keep the current selection visibly highlighted in every pane on the path to the detail view; allow drag and drop between panes.
- macOS: sensible min/max pane sizes, let people hide panes with several ways to bring them back (button, menu command,
  shortcut), use the thin 1 pt divider. iPhone: only in regular width. iPadOS: design for narrow, compact and mid widths.
- Windows (Mac, iPad, visionOS): adapt fluidly, do not build custom window chrome, say "window" in copy, open new windows
  only when it helps multitasking or context, keep custom windows in system appearances so the foreground window is
  obvious, do not park critical controls on a bottom bar.

## Panels, sheets, popovers  (`panels`, `sheets` 2026-03-24, `popovers`)
- **Panel (macOS):** quick adjustments or an inspector that follows the selection; titled, floats, hides with the app,
  not listed in the Window menu, no minimize button. Use standard panels over HUDs; keep HUDs small with little color.
- **Sheet:** one at a time; simple, short tasks. If you show Done, pair it with Cancel (or Back); button placement was
  updated 2026-03. Prefer a non-modal view for supplementary content, a panel when people repeatedly enter input and
  watch the result. iOS: medium detent, grabber on resizable sheets, swipe down to dismiss; iPad: page or form style;
  macOS: modest default size, parent window stays usable. visionOS: center in the field of view, not from the bottom edge.
- **Popover:** a little information or a few related actions; arrow points at its source; only one at a time; nothing over
  it except an alert; save work if it can be dismissed by clicking outside; never for warnings; not in compact widths.
  macOS may let people detach one into a panel.

## Scroll views  (`scroll-views`, 2026-06-08 scroll edge effects)
- Support the default gestures and keyboard scrolling; make scrollability obvious; never nest same-direction scrolls.
- **Scroll edge effect:** only when scrolling content sits behind floating controls; keep the automatic style, one per
  view (in split panes keep them the same height). It replaces solid bar backgrounds. Not decorative.
- Page-by-page scrolling plus a page control where it fits; sensible zoom limits.

## Search  (`search-fields`, `searching` both 2026-06-08)
- Placeholder text states the scope; search as people type; show recents or suggestions; most relevant results first;
  default to a broad scope then narrow with a scope bar or tokens (pair tokens with suggestions).
- iOS: search can be a tab, sit in a bottom toolbar (preferred when there is room), or be an inline field above the list.
  iPadOS/macOS: trailing side of the toolbar, or top of the sidebar to filter navigation; focus the field immediately in
  a dedicated search area; keep placement sensible as windows resize.

## Modality  (`modality`)
- Use only with a clear benefit; keep tasks short; no app-within-an-app; offer an obvious dismiss; confirm before losing
  data; make the task identifiable; one modal at a time. Full-screen modal for immersive or multistep editing.

## Other structure pages worth opening when relevant
`going-full-screen`, `multitasking`, `launching`, `onboarding`, `settings`, `tab-views`, `column-views`, `outline-views`,
`lists-and-tables`, `collections`, `disclosure-controls`, `path-controls`, `token-fields`, `boxes`, `labels`, `lockups`.
