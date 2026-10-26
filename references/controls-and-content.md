# Controls, menus, lists and content

Original summary. Full text: `cache/hig/<slug>.md`. Dates are Apple's "last updated" flags (older flag = stable guidance).

## Buttons  (`buttons`, 2025-12-16 Liquid Glass)
- Give buttons room to be distinguished; always include a **press state** for custom buttons.
- Prominent style for the single most likely action; distinguish the preferred choice by **style, not size**.
- Do not tint labels to a color similar to the content behind translucent bars; prefer monochrome then.
- Label by purpose: a familiar symbol, a few words, or both. Primary role goes to the button people most likely choose
  (it answers Return); **never give the primary role to a destructive action**, even if likely.
- iOS: a button can show an activity indicator for slow actions. macOS: ellipsis when the button opens another window or
  view; square buttons and help buttons live in the view, not the window frame (one help button per window, lower corner);
  image buttons keep about 10 px padding.

## Toggles, checkboxes, radio buttons, segmented controls, pickers  (`toggles`, `segmented-controls`, `pickers`)
- **Toggle** = two opposing values. State difference must be obvious (fill, shape, check or dot).
- iOS switch: only inside a list row, default green unless the accent is wanted; outside a list use a button that toggles.
- macOS: switch for emphasized settings, checkbox for hierarchies of settings (states on, off, mixed), radio buttons for a few
  mutually exclusive options (not too many), a single on/off setting prefers a checkbox. None of these in the window frame.
- **Segmented control:** closely related choices; one kind of content (all text or all icons), equal widths, few segments,
  noun labels, do not mix selection and action segments. On macOS use a tab view for main-area view switching.
- **Picker:** medium-to-long ordered lists, shown in context; fewer minute values in date pickers; a short list may be a
  pull-down button instead. iOS compact date picker when space is tight.

## Text fields, labels, text views, sliders, steppers  (`text-fields`, `labels`, `text-views`, `sliders`, `steppers`)
- Text field: small input, placeholder as a hint (not a replacement for a label), secure field for secrets, size matches expected
  text, logical tab order, validate sensibly, number formatters, correct keyboard type (iOS/tvOS/visionOS), clear button
  at the trailing end, minimal typing on tvOS and watchOS.
- Labels: for non-editable text; system label colors for importance (label, secondary, tertiary, quaternary); make useful values
  (errors, IP addresses, serial numbers) selectable.
- Sliders: minimum on the leading side, maximum on the trailing side; add a text field or stepper for precise values; tick marks
  and live feedback on macOS; not for audio volume on iOS (use a volume view). Steppers: make the controlled value obvious,
  pair with a text field for large ranges; macOS Shift-click for bigger steps.

## Menus and menu bar  (`menus` 2026-06-08, `the-menu-bar`, `context-menus`, `pull-down-buttons`, `pop-up-buttons`)
- Item labels: verb for actions, title-style capitalization, no articles, ellipsis when more input is needed, dim unavailable items
  (but in **context menus hide** unavailable items). Icons sparingly and uniformly: all items in a group or none (rule refined 2026-06).
- Order by importance and logical group; keep menus short; one level of submenu at most (prefer a submenu to indenting).
  Toggled items: a changing label ("Show Map" / "Hide Map"), a checkmark for attributes, an item that clears several at once.
- **Mac menu bar:** keep the standard menus and order, always show the same items (dim when unavailable), standard shortcuts
  for standard items, short one-word menu titles; app menu starts with About, then Settings, then Services, Hide, Quit.
  Every toolbar action must be reachable here.
- Context menu: the few most relevant actions, available elsewhere in the main interface too, destructive items last and
  marked; shortcuts are shown in the main menus, not in context menus; do not offer both a context menu and an edit menu on the same iOS item.
- Pull-down button: commands related to the button's action, at least three items, never hide a view's primary actions in one.
  Pop-up button: a flat list of mutually exclusive options with a sensible default and a label that predicts the choices.

## Lists, tables, disclosure  (`lists-and-tables`, `disclosure-controls`, `outline-views`, `collections`)
- Lists and tables are best for text: succinct row text, preserved readability when clipped, noun column headings in title style,
  selection feedback, edit and reorder where it helps. macOS: sortable and resizable columns, optional alternating rows,
  outline views for hierarchy (disclosure triangles with descriptive labels such as "Advanced Options").
- Disclosure: most-used controls on top, details hidden until relevant; at most one disclosure button per view.

## Alerts, status and progress  (`alerts`, `progress-indicators`, `gauges`, `action-sheets`)
- **Alerts:** sparingly; only for important, actionable situations; not at launch; not for common undoable actions. Direct, neutral
  title that states the situation; informative text only if useful; buttons 1 to 2 words that name the result (avoid bare "OK" unless
  purely informational); likely choice trailing (or on top in a stack); destructive style only for actions people did not
  deliberately choose, always with a Cancel; Esc and Command-period cancel.
- **Progress:** determinate when possible and accurate; keep it moving; switch indeterminate to determinate when known; do not
  swap spinner and bar; consistent location; allow Cancel and warn if cancelling loses progress; macOS prefers a spinner for
  background work, unlabelled.

## Charts and data  (`charts`, `charting-data`)
- Chart only to highlight what matters; keep it simple and let detail be opt-in; prefer common types (bar, line, point) and
  combine marks only for clarity; teach unusual charts.
- Axes: choose fixed vs dynamic range by meaning; **bar charts start at zero**; familiar tick sequences (0, 5, 10); few grid lines.
- Add descriptive title, subtitle and annotations that state the takeaway; give a summary for assistive tech; never rely on
  color alone and separate adjacent colored areas; make interaction optional, keyboard- and Switch-Control-friendly, with
  large hit targets; highlight important changes; align chart edges with neighboring content; keep colors and layout
  consistent across charts of the same data.
