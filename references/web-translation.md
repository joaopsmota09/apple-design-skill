# Translating Apple design to the web and desktop browsers

The HIG targets Apple's platforms and has no web chapter. On the web, copy the *intent* (hierarchy, clarity, deference to
content, adaptivity, accessibility, native-feeling behavior), not Apple's assets. This file is original guidance; values marked
"verify" are not stated in the cached HIG and should be checked against Apple's current UI kit (`cache/design-resources.md`).

## Hard limits (legal and practical)
- **Fonts:** Apple says to reach the system fonts through system APIs and **not to embed them**. On the web that means the system
  font stack only: `font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", system-ui, "Helvetica Neue", sans-serif;`
  (resolves to SF on Apple devices, to the OS font elsewhere). Never ship SF or New York font files with a site.
- **SF Symbols** carries terms and conditions (Apple's page warns about prohibited uses). Do not copy symbols into a web app; use your
  own simple stroked SVG icons or an openly licensed set, drawn at a weight matching the text.
- **Apple Design Resources** (UI kits, templates) are for designing apps for Apple platforms. Do not lift Apple artwork, logos, product
  images or trademarks (also: no Apple trademarks in names). Do not make a site look like it is made or endorsed by Apple.

## Structure and layout
- **Size classes -> breakpoints.** Compact below ~900 px: single column, bottom tab bar (4 to 5 items, 49 px tall plus safe area).
  Regular at 900 px and up: left **sidebar** (about 240 to 260 px, verify) with the same destinations, content in a multi-column grid
  that uses the full width. Same functions at every size; only the amount shown changes.
- **Toolbar:** a sticky top bar with a concise title (under ~15 characters), few actions, extra actions in a More menu.
  Large title in content on narrow screens, collapsing into the bar on scroll.
- **Content width:** text columns stay readable (about 60 to 75 characters); dashboards may span the window, never leave a dead
  right half: let `grid-template-columns: repeat(auto-fit, minmax(~340px, 1fr))` use the space.
- **Grouped lists:** the iOS inset-grouped list is the workhorse: rounded container, 44 px rows, label left and value right, hairline
  separators inset from the leading edge. Prefer rows over tables for small data; use real tables for multi-column comparison.
- **Spacing:** multiples of 4 and 8 px; 16 px page margins on phones, 20 to 40 px on desktop. Group by space and separators, not boxes inside boxes.
- **Safe areas:** `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">` and
  `padding: env(safe-area-inset-*)` on fixed bars.
- **Corner radii:** make nested shapes concentric (inner radius = outer radius minus the padding between them). Typical: cards 12 to 20 px,
  controls 8 to 12 px or capsule, grouped-list cells 10 to 12 px.

## Size of things (CSS px at 1x)
- **Targets:** touch/coarse pointer 44x44 default (28 minimum); desktop pointer 28x28 default (20 minimum). Use
  `@media (pointer: coarse)` to enlarge. Space between controls counts as much as size.
- **Type:** dense desktop tools 13 to 15 px body (macOS body is 13 pt, minimum 10); touch UIs 17 px (minimum 11). Use `rem`
  so the browser's text-size setting works (the web's Dynamic Type); `line-height` about 1.3 to 1.4; weights 400, 500, 600, 700 only;
  `font-variant-numeric: tabular-nums` for any column of numbers; small positive tracking on large titles.
  iOS default style ladder (px): Large Title 34/41, Title 1 28/34, Title 2 22/28, Title 3 20/25, Headline 17/22 semibold, Body 17/22,
  Callout 16/21, Subhead 15/20, Footnote 13/18, Caption 12/16 and 11/13. macOS ladder: 26, 22, 17, 15, 13 bold, 13, 12, 11, 10.

## Color tokens (names mirror Apple's roles)
- Define roles, not hexes, in `:root`, and redefine under `@media (prefers-color-scheme: dark)`: `--bg`, `--bg-2`, `--bg-3` (levels),
  `--label`, `--label-2`, `--label-3`, `--label-4`, `--separator`, `--fill`, `--tint`, plus status `--red --orange --green`.
  Add `color-scheme: light dark` and honor `prefers-contrast: more` with stronger separators and label colors.
- **Tints (current system palette, light / dark):** blue 0,136,255 / 0,145,255 · green 52,199,89 / 48,209,88 · red 255,56,60 / 255,66,69 ·
  orange 255,141,40 / 255,146,48 · yellow 255,204,0 / 255,214,0 · indigo 97,85,245 / 109,124,255 (from `cache/hig/color.md`).
- **Neutrals (approximate, verify in the UI kit):** light page background #F2F2F7 with white #FFFFFF cells; dark page #000000 with
  cells #1C1C1E and a third level #2C2C2E. Labels: light #000 then rgba(60,60,67, .6 / .3 / .18); dark #FFF then rgba(235,235,245, .6 / .3 / .18).
  Separator light rgba(60,60,67,.29), dark rgba(84,84,88,.6).
- One accent color, used for interactive things and selection only. Status color always comes with text or a glyph. Contrast: 4.5:1
  text up to 17 px, 3:1 for 18 px and bold, 3:1 for UI components. No in-app light/dark toggle: follow the system.

## Materials (the web version of Liquid Glass)
- Only the **functional layer** (sticky toolbar, sidebar, tab bar, popovers, sheets) gets a translucent material:
  `background: color-mix(in srgb, var(--bg) 80%, transparent); backdrop-filter: saturate(180%) blur(20px);` with a hairline border.
  The content layer stays flat. Do not stack glass on glass or fake refraction.
- Provide a solid fallback: `@supports not (backdrop-filter: blur(1px))`, and for users who reduce transparency or raise contrast
  (`prefers-contrast: more`, `prefers-reduced-transparency` where supported) use an opaque bar.
- Replace a solid bar behind scrolling content with a soft edge (a gradient fade or the hairline that appears on scroll), not a heavy shadow.

## Interaction
- Use native elements first (`button`, `input`, `select`, `details`, `dialog`, the Popover API): they carry keyboard, focus and
  assistive behavior for free. Every custom control needs role, name, state and keyboard operation.
- States: hover only for fine pointers (`@media (hover: hover)`), a visible pressed state, `:focus-visible` ring (2 px accent, offset 2 px),
  disabled states that still explain themselves. Primary action answers Enter; Esc closes dialogs and popovers.
- Keyboard: tab order follows reading order, shortcuts for frequent actions (a command palette on Cmd/Ctrl+K), never override browser shortcuts.
- Motion: 150 to 300 ms ease-out, only for meaning (selection, reveal, state change), nothing on frequent actions, and
  `@media (prefers-reduced-motion: reduce)` removes it. Never let animation block input.
- Destructive actions: red, confirmed, and preferably undoable (an undo toast beats a confirm dialog for common deletes).
- Feedback: inline status near the thing, skeleton or content immediately, determinate progress when known, errors that say what to do.

## Dashboards and data (HIG charts guidance applied)
- Numbers: tabular figures, units in labels, signed deltas with + and - plus color. Put the key figure first, large; supporting detail lower.
- Charts: bar charts start at zero; few gridlines; annotate the takeaway in words; give the chart a text summary (`role="img"` and
  `aria-label`); never encode meaning in color alone; keep interaction optional and keyboard-reachable; keep colors consistent across charts of the same data.
- Empty states say what will appear and when. Live data shows a clear "updated" time and a visible failure state.
- Show how much is at risk or at stake before the controls that change it.

## Checks before shipping
Light and dark; 200% text zoom; narrow (about 390 px) and wide (1440 px or more) with no dead areas; keyboard only; screen reader
landmarks (`header`, `nav`, `main`) and labels; reduced motion; high contrast; coarse pointer targets; print/no-JS failure message.
