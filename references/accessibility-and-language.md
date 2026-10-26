# Accessibility, inclusion, writing, right-to-left, privacy

Original summary. Full text: `cache/hig/<slug>.md`.

## Accessibility  (`accessibility`, 2025-06-09: Assistive Access, Switch Control, Accessibility Nutrition Labels added)
**Vision**
- Support larger text (system text styles); default / minimum sizes iOS+iPadOS 17 / 11 pt, macOS 13 / 10, tvOS 29 / 23,
  visionOS 17 / 12, watchOS 16 / 12. Thin custom weights need larger sizes.
- **Contrast minimums:** text up to 17 pt at any weight 4.5:1; 18 pt text 3:1; bold text 3:1. Prefer system colors, which carry
  Increase Contrast variants.
- Information must never depend on color alone. Describe every control and piece of content for VoiceOver.

**Hearing:** pair audio cues with haptics and visual cues; give text alternatives for dialogue and key audio info.

**Mobility**
- **Control sizes (default / minimum):** iOS+iPadOS 44x44 / 28x28 pt · macOS 28x28 / 20x20 · tvOS 66x66 / 56x56 ·
  visionOS 60x60 / 28x28 · watchOS 44x44 / 28x28. Spacing between controls matters as much as size.
- Prefer simple gestures and always offer an alternative to a gesture. Support Voice Control, Full Keyboard Access, Pointer
  Control, Switch Control, AssistiveTouch, Siri and Shortcuts. Everything must be operable with the keyboard alone on Mac.

**Cognitive:** simple, consistent interactions; avoid auto-dismissing UI on timers; no autoplay without controls; honor
Reduce Motion; avoid fast blinking or flashing; let people opt out of flashing video; optimize for Assistive Access.

**Do before shipping:** test at the largest text size, with VoiceOver on, with Increase Contrast, Reduce Transparency and
Reduce Motion, with keyboard only, and with color filters or grayscale.

## Inclusion  (`inclusion`)
- Welcoming language: address people as "you", define or avoid jargon, use plain language instead of idioms, think hard before
  using humor (it does not translate). Avoid stereotypes and gendered assumptions; offer inclusive options for gender and
  names. People-first language about disability; show a range of people and settings.

## Writing  (`writing`, 2025-12-16)
- Decide the app's voice, then adapt tone to the situation. Be clear, action-oriented (active voice, verb labels), consistent
  (one label per step of a flow, one capitalization style), and sparing with possessives ("my", "your").
- Every screen has one purpose. Empty states give a clear next step and a welcome. Error messages help people avoid and
  fix errors in plain words. Settings labels are practical. Text fields show hints.
- Alerts and menus use title-style capitalization for menu items and buttons; sentence style for alert body text.

## Right to left  (`right-to-left`)
- Mirror layout, alignment of lists, progress controls (sliders, progress bars) and navigation order (back points right).
- Do not reverse the digits inside a number; do reverse counting and progress direction. Do not flip photos, logos, universal signs or
  real-world object icons; flip icons that indicate text direction or forward and backward motion.
- Align a paragraph (3+ lines) to its own language; keep one alignment per list. Balance Latin and Arabic or Hebrew sizes.

## Privacy and permissions  (`privacy`)
- Ask only for data a feature actually needs, and only when the person shows interest in that feature, not at launch
  (unless the app cannot work without it). Explain why in an active, specific purpose string ("The app records during the
  night to detect snoring" beats "Microphone access is needed").
- A pre-alert screen may have a single button that opens the system prompt and nothing else. Never place a custom screen
  before a tracking request that could mislead. Prefer on-device processing and system privacy protections. Be transparent.
