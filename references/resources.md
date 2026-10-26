# Apple Design Resources and tools

Live list (with download links) is cached in `cache/design-resources.md` (from https://developer.apple.com/design/resources/) and the
overview in `cache/design-home.md` (https://developer.apple.com/design/). Re-run `scripts/refresh.py` for current versions.

## What exists (as of the 2026-10-26 snapshot)
- **UI kits (Figma and Sketch):** iOS and iPadOS 27, macOS 27, watchOS 26, visionOS 26, tvOS 18 (Sketch). Plus app-icon templates
  (Figma, Sketch, Photoshop and Illustrator) for iOS/iPadOS/watchOS 27, and product-specific kits (Apple Pay, App Clips, Live Activities,
  iMessage apps and stickers, widgets and more).
- **SF Symbols app** (7,000+ symbols, nine weights, three scales), the **San Francisco and New York fonts** (for design mockups; do
  not embed in apps or sites, use the system font APIs), **Icon Composer** (layered app icons, in Xcode and downloadable),
  **Parallax Previewer / Exporter** (tvOS layered images), Dynamic Type size tables per platform, color guides.
- **Terms:** the kits and fonts are for designing apps for Apple platforms; SF Symbols has its own terms and prohibitions. Read the
  license on the download page before using any asset, and never ship Apple artwork or trademarks in your product.

## Using resources in a workflow
- Starting a native app: begin from the platform's UI kit and Dynamic Type table, build with system components (SwiftUI, UIKit, AppKit),
  preview in Xcode and Device Hub at smallest and largest sizes.
- Web or cross-platform: use the kit only as a *reference* for spacing, radii and hierarchy; implement with your own assets
  (see `web-translation.md`).
