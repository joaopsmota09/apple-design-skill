# Review checklist and scoring

Use when asked to review, audit or "make it feel native". Score each row 1 or 0, add the bonus points, report the total out of 10
and list the specific changes needed to reach 10. (Structure inspired by wondelai/ios-hig-design's scoring, MIT; the rows and
thresholds below are rewritten against the current HIG.)

| # | Question | Evidence to check | Fix if no |
| --- | --- | --- | --- |
| 1 | Does the layout respect safe areas and adapt by available width (size classes), keeping the same functions at every size? | resize from phone to widest window; no fixed widths; no dead areas | switch to adaptive grid, sidebar at wide widths, tab bar at narrow |
| 2 | Are touch/click targets at least 44x44 (touch) or 28x28 (desktop pointer), with room between them? | measure | enlarge hit areas, add spacing |
| 3 | Does it work in light and dark, with Increase Contrast and Reduce Transparency, without an in-app toggle? | toggle each | semantic color roles, contrast variants, opaque fallback |
| 4 | Does text use a defined type scale, respect text-size changes and never truncate key content at the largest size? | 200% zoom / largest Dynamic Type | rem sizes, stack or wrap, drop columns |
| 5 | Can a screen reader and a keyboard-only user finish every task (names, roles, states, focus order, visible focus)? | VoiceOver / keyboard pass | labels, landmarks, focus-visible, shortcuts |
| 6 | Are navigation patterns standard for the platform (tab bar or sidebar, toolbar, sheets, menus; no hamburger as primary nav)? | structure review | use the standard pattern |

**Bonus (up to 4):** +1 semantic colors and text styles everywhere (no hard-coded values) · +1 system or native controls instead of custom
re-implementations · +1 standard gestures, shortcuts and sensible feedback (haptics on devices that have them) · +1 correct icons: a coherent icon
set matched to text weight (SF Symbols on Apple platforms), correct app-icon shape and layering.

**Bands:** 9 to 10 native-feeling, accessible, adaptive · 5 to 6 works but hard-codes values or leaks other platforms' idioms · 3 or below
fails safe areas, target sizes or screen-reader use.

## Liquid Glass era checks (add when the design targets the current Apple look)
- Glass only on the functional layer; none in content. Custom glass used sparingly. No stacked glass.
- No solid bar backgrounds behind scrolling content; a scroll edge effect or soft edge instead. Bars stay monochrome over colorful content.
- Color on glass is limited to a primary action or status, applied to the background rather than the label.
- Nested shapes are concentric. Full-bleed content extends under sidebars and toolbars.
- Motion is brief and optional; Reduce Motion honored.

## Common mistakes
Overriding standard gestures or shortcuts · custom window or bar chrome · color-only status · cramped controls · hard-coded font sizes ·
alerts for non-actionable news · launch-time permission prompts · modals inside modals · hiding the tab bar or sidebar by default · branding in the
launch screen · app-specific appearance toggle · custom backgrounds under toolbars.
