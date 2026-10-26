# Platforms, inputs and system experiences

Original summary. Full text: `cache/hig/<slug>.md`. Flag dates are Apple's own.

## Platform characteristics  (`designing-for-*`)
| Platform | Display and distance | Inputs | Interaction style | Design for |
| --- | --- | --- | --- | --- |
| **iOS** (`designing-for-ios`) | medium screen, hand-held, 1 to 2 ft | touch, virtual keyboard, voice, sensors | minutes to an hour; many apps open | few on-screen controls, secondary actions one step away, reachable middle/bottom controls, swipe-back and row swipes, widgets, quick actions, Spotlight, Shortcuts |
| **iPadOS** (`designing-for-ipados`) | large, hand-held or on a stand, about 3 ft | touch, Pencil, keyboard, trackpad, voice | multitasking, multiple windows | elevate content, minimize modals, input mode drives density, adapt to orientation, multitasking, Dark Mode, Dynamic Type and to running on Mac |
| **macOS** (`designing-for-macos`) | large, possibly several displays, 1 to 3 ft, stationary | keyboard, pointing device, game controls, Siri | minutes to hours, many apps open | more content in fewer nested levels with less modality, resizable/hideable windows and full screen, the menu bar for all commands, high-precision input, keyboard shortcuts, personalization (toolbars, windows, colors, fonts) |
| **tvOS** (`designing-for-tvos`) | very large, 8 ft or more | Siri Remote, game controller, voice, other devices | long, immersive, lean-back | focus system, edge-to-edge artwork, legible from across the room, shared sign-in and profile switching |
| **visionOS** (`designing-for-visionos`) | infinite 3D canvas, passthrough | eyes plus hand gestures (indirect or direct), voice | Shared Space, Full Space, immersion levels | prefer windows for UI tasks, minimum immersion needed per moment, comfort first (content in the field of view, no overwhelming motion, support indirect gestures), SharePlay |
| **watchOS** (`designing-for-watchos`) | tiny, glance | Digital Crown, tap/swipe, Action button | under a minute, complications and notifications are used more than the app | glanceable single-screen tasks, shallow hierarchy, Crown navigation, complications and notifications |
| **iPhone Duo** (`designing-for-iphone-duo`, NEW 2026-09-09) | two displays plus hinge | iPhone inputs | folds, poses | see below |

### iPhone Duo (new page)
- Still designed as iPhone; build to **resize** with size classes, margins and safe-area insets (compact width for the outer display,
  regular for the inner), never fixed widths or display-specific logic.
- Keep functionality and state identical between displays and poses; the inner display may add one level of hierarchy (a split view).
- System toolbars, tab bars and navigation controls move to the **side** (vertical axis) on the outer display and in inner landscape
  to save vertical space; standard components do this for free.
- **Reserved regions**: outer camera (expands into the Dynamic Island for Live Activities), inner camera (only when active), the
  folding region. Alerts, context menus and sheets avoid the fold automatically; custom views use the ReservedRegion API.
  Prefer an even column count in grids, small adjustments instead of re-arranging when the device folds. Arrangement views come in split and overlay types.

## Inputs  (`pointing-devices`, `keyboards`, `gestures`, `focus-and-selection`)
- **Pointer and trackpad:** behave consistently, never redefine system-wide trackpad gestures, let the pointer reveal auto-hiding
  controls, keep modifier-key behavior consistent, pad hit regions, use system pointer effects and contiguous hit regions on bars.
- **Keyboard:** support Full Keyboard Access and standard shortcuts (do not repurpose Command-C/V/Z, Command-comma for settings,
  Esc cancels, Tab and Shift-Tab move focus, Control-Tab moves between groups). Every command should be reachable by keyboard.
- **Gestures:** offer more than one way to do everything, follow standard meanings (iOS undo: three-finger swipe left or shake),
  respond immediately, show when a gesture is unavailable, add custom gestures only for frequent specialized tasks and teach them,
  never conflict with system gestures.
- **Focus:** use system focus effects; do not move focus without user action; focus ring for text/search fields, highlight in lists
  and collections; Tab moves in reading order through focus groups. (Web: visible `:focus-visible` rings and logical tab order.)

## System experiences  (verify current numbers in the cache before specifying)
- **Widgets** (`widgets`, 2026-10-13: Apple HomeView guidance, watchOS spec updates): system small/medium/large/extra-large families
  and accessory circular/corner/inline/rectangular; full-color, accented and vibrant appearances; glanceable, no scrolling.
- **Live Activities** (`live-activities`, 2026-10-13: limited-width layouts, supported platforms): for tasks with a clear start and end,
  under 8 hours; compact, minimal, expanded, Lock Screen and StandBy layouts; Mac menu bar and Watch Smart Stack too; no ads, no sensitive data.
- **Snippets** (`snippets`, NEW 2026-06-08): lightweight quick-interaction cards; legible contrast on the system background in light and dark,
  concise, descriptive primary-button label on confirmations, purpose communicated visually, not only by dialogue.
- **Notifications** (`notifications`, `managing-notifications`): concise, no duplicates, no tasks, errors use alerts not notifications,
  no sensitive content, sentence case, no app name or icon, useful non-destructive actions that do more than open the app.
- **Controls** (`controls`): actions that help without launching the app; descriptive symbol, tint, redact when locked, require auth
  for security actions. **App Shortcuts** (`app-shortcuts` 2026-06-08): app schemas preferred for common functionality; short memorable phrases;
  "Shortcuts" always plural, title case.
- **Generative AI** (`generative-ai`, 2026-06-08: letting people refine results, feedback during generation, model choice):
  keep people in control, disclose where AI is used and its limits, ask permission for personal data, prefer on-device models
  for privacy and offline use, minimize hallucination risk, confirm before irreversible actions, work well when AI is off or unavailable.
- **Siri** (`siri`, 2026-06-08 Siri AI): clear, short, device-independent, audible-and-visual responses; no advertising; omit the app name.
- Other technologies pages: `apple-pay`, `wallet` (iOS 27), `apple-in-app-purchase` (2026-09-17), `sign-in-with-apple`, `healthkit`, `carplay`,
  `maps`, `icloud`, `shareplay`, `machine-learning`, `augmented-reality`, `voiceover`.

## Games  (`designing-for-games`)
- Playable right after install (initial download ideally under 30 minutes, rest in the background), great defaults from device
  info, teach through play, defer permission requests, support every platform's input.
