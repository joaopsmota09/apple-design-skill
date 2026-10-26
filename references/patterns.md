# Interaction patterns

Original summary. Full text: `cache/hig/<slug>.md`.

## Feedback, status, errors  (`feedback`)
- Offer feedback in more than one channel (visual, text, haptic, sound) so it is accessible. Prefer status shown next to the
  thing it describes over interruptions. Alerts only for critical, ideally actionable information.
- Warn before unexpected, irreversible data loss. Confirm significant completed actions (a payment). When a command cannot run,
  say why and what to do.

## Loading and launching  (`loading` 2025-06-09, `launching` 2024-06-10)
- Show something immediately; let people keep working while content loads; give them something to look at during long waits;
  show progress with a system indicator; download large assets in the background.
- Launch instantly. A launch screen is not branding or onboarding: nearly identical to the first screen, no text, no ads.
  Restore the previous state on restart so people continue where they left off.

## Onboarding and help  (`onboarding` 2024-06-10, `offering-help`)
- Teach by doing, not by slides. Prefer context-specific tips to one long flow; keep any required flow brief; make tutorials
  optional and do not repeat them. Postpone non-essential setup and offer good defaults. Ask for permissions only when needed,
  and do not ask for ratings or purchases before people have experienced the app. Leave licence text to the store.
- Tips: short, actionable, for simple features, with targeting rules; popover tip to keep flow, inline tip to keep surrounding
  content visible; do not explain standard components.

## Settings  (`settings` 2024-06-10)
- Best defaults for most people; as few settings as possible; infrequent, general options only in the settings area; task-specific
  options where the task happens; respect system-wide settings (do not duplicate them); do not ask for what the system can detect.
  Open Settings with Command-comma on Mac.

## Entering data  (`entering-data`)
- Take data from the system when possible; offer choices instead of typing; allow drag and drop and paste; label or hint every
  field; secure entry for secrets and never prefill a password; validate as people type; make required fields obvious.

## Undo and redo, drag and drop  (`undo-and-redo`, `drag-and-drop`)
- Undo: predictable and visible, as many levels as possible, batch revert, in the Edit menu with standard shortcuts; do not
  redefine the iOS undo gestures (three-finger swipe, shake).
- Drag and drop: support it widely and always offer an alternative; show a drag image after about 3 pt of movement; show whether
  a destination accepts the drop and give feedback on failure; define move vs copy; support multi-item, auto-scroll and undo.

## Windows, full screen, multitasking  (`going-full-screen` 2025-06-09, `multitasking` 2025-06-09)
- Use the system's full-screen mode, never resize the window yourself, keep essential controls reachable, let people choose when
  to enter and leave, restore state, optionally hide toolbars for content. In iOS/iPadOS consider deferring system gestures.
- Multitasking: pause attention-demanding work when people switch away, finish user-started tasks in the background, handle
  audio interruptions smoothly, use notifications sparingly.

## Notifications, accounts, sharing, files
- **Notifications** (`managing-notifications`): urgency must be honest. Interruption levels: Passive and Active do not break
  through Focus; Time Sensitive breaks through Focus; Critical also overrides the ring/silent switch. Never use Time Sensitive for marketing;
  get explicit permission for promotional notifications and provide in-app notification settings.
- **Accounts** (`managing-accounts`): explain the benefit, delay sign-in as long as possible, prefer Sign in with Apple or passkeys, name
  the authentication method precisely ("Sign In with Face ID"), do not call it "passcode", provide in-app account deletion
  (or a direct link), allow scheduling it and say when it completes.
- **Sharing** (`collaboration-and-sharing`): Share button in the toolbar, short permission phrases ("Only invited people can edit"), show the
  Collaboration button as soon as collaboration starts.
- **Files** (`file-management`): menus and shortcuts to create/open; work is always preserved; hide extensions by default; Quick Look previews.

## Charts and data  -> see `controls-and-content.md`.
