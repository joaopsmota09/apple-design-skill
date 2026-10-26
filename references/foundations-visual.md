# Visual foundations: color, Dark Mode, type, materials, motion, layout, icons, branding

Original summary of Apple's guidance. Exact wording and the full tables live in `cache/hig/<slug>.md`
(run `scripts/refresh.py` first if the cache is empty). Each section lists its source slug and the date Apple last
flagged it as updated.

## Color  (`color`, 2025-12-16 Liquid Glass update)
- **Semantic first.** Use the system's role-based colors (background levels, label levels, separator, link, fill)
  instead of fixed values. Roles adapt to light, dark and Increase Contrast on their own. Never reuse a role for
  another job (no separator color as text, no secondary label as a background).
- **Background levels:** primary = the whole view, secondary = grouped content inside it, tertiary = groups inside
  those. Use the *grouped* set for grouped tables, the plain set otherwise.
- **Label levels:** label, secondary, tertiary, quaternary, plus placeholder, separator (translucent) and opaque separator, link.
- **Custom color** needs a light variant, a dark variant and an Increase Contrast variant of each.
- **One meaning per color.** If the brand color marks something tappable, do not also use it for static text.
- **Never color alone.** Pair status color with a word, shape or glyph (color blindness, glare, culture).
- **Light conditions:** colors look darker and muted in sun, brighter and more saturated in the dark. Test both.
- **System palette defaults** (documented for design reference only; Apple warns the live values drift between
  releases, so take them from the platform API, not from hard-coded constants). Light / dark RGB:
  red 255,56,60 / 255,66,69 · orange 255,141,40 / 255,146,48 · yellow 255,204,0 / 255,214,0 ·
  green 52,199,89 / 48,209,88 · mint 0,200,179 / 0,218,195 · teal 0,195,208 / 0,210,224 ·
  cyan 0,192,232 / 60,211,254 · **blue 0,136,255 / 0,145,255** · indigo 97,85,245 / 109,124,255 ·
  purple 203,48,224 / 219,52,242 · pink 255,45,85 / 255,55,95 · brown 172,127,94 / 183,138,102.
  Grays (iOS/iPadOS), light / dark: gray 142,142,147 both · gray2 174,174,178 / 99,99,102 · gray3 199,199,204 / 72,72,74 ·
  gray4 209,209,214 / 58,58,60 · gray5 229,229,234 / 44,44,46 · gray6 242,242,247 / 28,28,30.
  Increase-Contrast variants are in `cache/hig/color.md`.
- **Liquid Glass color:** glass has no color of its own; it takes the content behind it. Tint sparingly, only for
  emphasis (a primary action, a status). Tint the *background* of a primary control rather than its symbol or text.
  Do not tint many controls. If the content layer is colorful, keep toolbars and tab bars monochrome. Keep the
  resting state of scrolling content legible under controls.
- **macOS accent:** the user's system accent color (or multicolor) overrides the app accent in buttons, selection and
  sidebar icons. A sidebar icon with a fixed color keeps it because the color carries meaning.
- **Wide color:** use Display P3 (16 bit PNG) where it helps; give sRGB fallbacks if two P3 colors look the same on sRGB.

## Dark Mode  (`dark-mode`)
- No in-app appearance switch. Follow the system, including Auto changing while the app is open.
- Test Dark with Increase Contrast and Reduce Transparency on, separately and together.
- Contrast: never below **4.5:1**; aim for **7:1** for small text.
- iOS/iPadOS use **base** (dimmer) and **elevated** (brighter) backgrounds so a layer above another reads as closer.
  Prefer system backgrounds so popovers, sheets and multitasking get this automatically.
- Soften pure-white image backgrounds so they do not glow. Use separate light/dark icon art only when needed.
- macOS "desktop tinting" (graphite accent): neutral custom components with their own background should allow some
  transparency so they pick up the window tint; colored states should stay opaque.
- Only exception for a permanent dark UI: immersive media viewing.

## Typography  (`typography`, 2025-12-16 emphasized weights added)
- **Default / minimum sizes (pt):** iOS+iPadOS 17 / 11 · macOS 13 / 10 · tvOS 29 / 23 · visionOS 17 / 12 · watchOS 16 / 12.
- Avoid Ultralight, Thin and Light; prefer Regular, Medium, Semibold, Bold. Build hierarchy with weight, size and color.
- **System fonts:** SF Pro (SF Compact on watchOS, SF Mono for code, rounded variants) and New York (serif). Use the
  platform font API; do not embed or ship Apple's system fonts. Variable fonts handle optical sizing and tracking.
- **Text styles** (size / leading, regular unless noted):
  - iOS Large (default) Dynamic Type: Large Title 34/41 · Title 1 28/34 · Title 2 22/28 · Title 3 20/25 ·
    Headline 17/22 semibold · Body 17/22 · Callout 16/21 · Subhead 15/20 · Footnote 13/18 · Caption 1 12/16 · Caption 2 11/13.
    Other sizes (xSmall to AX5) are in `cache/hig/typography.md`.
  - macOS (no Dynamic Type): Large Title 26/32 · Title 1 22/26 · Title 2 17/22 · Title 3 15/20 · Headline 13/16 bold ·
    Body 13/16 · Callout 12/15 · Subheadline 11/14 · Footnote 10/13 · Caption 1 10/13 · Caption 2 10/13 medium.
  - tvOS: Title 1 76 · Title 2 57 · Title 3 48 · Headline 38 · Subtitle 38 · Callout 31 · Body 29 · Caption 25 / 23.
- **Dynamic Type** (not on macOS): layouts must survive every size. Stack horizontal items vertically, let rows grow,
  reduce columns, keep the primary item on top, grow meaningful icons with text, and avoid truncating (test the
  largest accessibility size). Do not grow secondary chrome such as tab titles.
- Custom fonts must be legible at the minimum sizes and must honor Bold Text and Dynamic Type.
- In mockups only: adjust tracking by point size; a running app does it automatically.

## Materials and Liquid Glass  (`materials`, `doc-liquid-glass`, `doc-adopting-liquid-glass`)
- **Two layers.** Liquid Glass is the *functional* layer for controls and navigation (tab bars, sidebars, toolbars,
  sheets) that floats above content. Standard materials (blur, vibrancy) structure the *content* layer.
- **Never put Liquid Glass in the content layer.** Exception: transient interactive controls such as slider knobs and toggles.
- Use custom glass effects sparingly, only on the most important controls.
- **Regular** glass blurs and adjusts luminosity for legibility: use it for text-heavy surfaces (alerts, sidebars, popovers).
  **Clear** glass is highly translucent: only over rich media backgrounds; add a ~35% dark dimming layer if the media is bright.
- Instead of a solid or semi-opaque bar behind controls, use a **scroll edge effect** so controls lift above content.
  Extend full-bleed backgrounds under sidebars, toolbars and tab bars (a *background extension effect* mirrors and blurs
  the image so it appears to continue under a sidebar).
- Standard materials: choose by meaning, not by the color you see. Thicker = more contrast for fine text, thinner =
  more context. iOS has ultra-thin, thin, regular, thick; put vibrant colors (label levels, fills, separators) on top.
- macOS: materials have designated purposes; choose a blending mode (behind window or within window) and test vibrancy.
- visionOS windows use the fixed *glass* material: prefer translucency to opaque fills, keep color sparse on glass.

## Motion  (`motion`, 2025-09-09 Liquid Glass update)
- Purposeful only; never the only carrier of information (back it with haptics, sound, text). Make it optional.
- Feedback motion follows the gesture and is brief and precise. A view revealed by sliding down is dismissed upward, not sideways.
- Avoid animating frequent UI interactions; never make people wait for an animation; let them cancel it.
- Liquid Glass motion is stronger for touch and subtler for a trackpad. Honor Reduce Motion.
- visionOS: avoid peripheral motion, sustained ~0.2 Hz oscillation, rotating a whole world; prefer fades to relocate an object.

## Layout  (`layout`, 2026-09-09 update)
- Hierarchy: important content top and leading; align and indent to show relationships; group with space, shapes or
  separators; disclose progressively; differentiate controls from content (glass + scroll edge effect).
- **Adapt by size class, not device or orientation.** Keep functionality the same as space changes; only the amount shown
  changes (for example tab bar to sidebar, or reveal overflow actions on larger windows).
- Respect safe areas and layout guides (readable width limits). Support text-size changes. Test smallest and largest layouts.
- macOS: never put controls or key information at the bottom edge of a window (windows get dragged off-screen), and avoid
  the camera housing at the top edge. tvOS: inset 60 pt top/bottom, 80 pt sides. visionOS: support resizing, keep control
  centers at least 60 pt apart, supplemental content goes in an adjacent window, not an ornament. watchOS: at most 3 glyph
  buttons or 2 text buttons side by side.

## SF Symbols and icons  (`sf-symbols`, `icons`)
- Use SF Symbols for interface icons; match their weight to adjacent text; pick a rendering mode that stays legible in
  every context (monochrome, hierarchical, palette, multicolor). Variable color shows *change*, not depth.
- Animate symbols rarely and with purpose (appear, bounce, pulse, replace, draw on/off in SF Symbols 7).
- Custom symbols: follow the template, keep optical weight and detail consistent, supply an accessibility label, vector
  (SVG/PDF) only, no replicas of Apple hardware.
- Standard action glyphs are listed in `cache/hig/icons.md` (cut, copy, delete = trash, share = square.and.arrow.up, ...).

## App icons  (`app-icons`, 2026-06-08 Liquid Glass refinement)
- Layered artwork (vector layers, clear edges, varied opacity) for system lighting; do not bake in highlights, shadows or blur.
- Keep primary content centered; the system masks the shape. 1024x1024 px for iOS/iPadOS/macOS (appearances: default, dark,
  clear, tinted), 800x480 tvOS, 1024 visionOS (circular mask), 1088 watchOS. Same recognizable design on every platform.
- No text unless essential, prefer illustration to photos, base the dark icon on the light one, no UI replicas.

## Images and branding  (`images`, `branding`, 2026-09-09 brand color update)
- Scale factors: iOS @2x and @3x; iPadOS, watchOS @2x; macOS, tvOS @1x and @2x. Photos JPEG/HEIC, flat art SVG/PDF, include color profiles.
- Branding defers to content: judicious accent color, familiar components, no logo everywhere, no launch-screen branding,
  never put Apple trademarks in app names or imagery.
