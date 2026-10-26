# Notice and attributions

- **Apple content.** The guidelines text cached by `scripts/refresh.py` under `cache/` is Apple's copyrighted material, fetched from
  developer.apple.com for personal use. It is git-ignored and must not be redistributed. Apple, SF Symbols, San Francisco, Liquid Glass and
  related names are Apple trademarks. This skill is not affiliated with or endorsed by Apple.
- **Original work.** Everything in `references/` is an original summary and organization written for this skill, with source page slugs
  and Apple's update dates so each point can be checked against the cache. `scripts/` and `SKILL.md` are original.
- **Structural inspiration (MIT licensed).** The "ask targeting questions first, then load only the relevant references" workflow follows
  ebuntario/apple-hig (https://github.com/ebuntario/apple-hig). The 6-row diagnostic with bonus points and score bands in
  `references/review-checklist.md` follows wondelai/ios-hig-design (https://github.com/wondelai/skills); the rows themselves are rewritten
  against the current HIG. No text was copied from either project.
- **Crawling.** `refresh.py` reads only public, non-disallowed paths (`/tutorials/data/...`, `/design/`), identifies itself, waits 0.6 s between
  requests and uses ETags so unchanged pages are not downloaded again.
