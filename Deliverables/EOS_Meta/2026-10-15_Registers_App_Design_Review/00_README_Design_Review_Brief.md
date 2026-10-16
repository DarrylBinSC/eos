# Design Review Brief: EOS Registers Web App

Prepared 2026-10-15 for a usability and visual design review in Claude Design. Everything needed is in this folder; no access to the live system or the original conversation is required.

## Context

Darryl Benson runs an Executive Operating System (EOS): a folder of markdown files that Claude maintains as his chief-of-staff record. Three registers matter here:

- **Actions**: Register A (his own commitments, capped at 15), Other-Owned (delegated or awaited, about 140 items, some tagged Critical), and new items awaiting triage.
- **Watch list**: risks in tiers Active (capped at 20), Passive, Retired, with severity and trend.
- **Decisions**: Decision Radar (routed to a forum with a date, capped at 20) and Decision Backlog.

Until today these lived as tables inside large markdown files, which Darryl rarely opened, so statuses went stale. As of 2026-10-15 each item is its own file, and this web app is how Darryl views and updates them from any device on his home network. Claude reads his changes first at every morning brief. The app is a working surface, not a dashboard: its job is to make a 30-second update cost 30 seconds.

The app was built in a few hours as a single Python file serving one HTML page. It works. It has had no design pass. That is what this review is for.

## The user

One user: a senior technology director, 58, technically fluent, works from home. Uses the app on a MacBook (Safari or Chrome, desktop width) and on an iPhone, often between meetings or on a Sunday evening. He does not want to learn an interface; he wants to see what is due, change a status, type a note, and leave. Reading happens on the Mac; quick updates happen on the phone.

## Task

Review the app for usability and visual design and propose improvements. Produce the deliverables listed under Output Format. Do not rebuild the backend; the review is about the page.

## Goal

The triage view should let the user clear his open items in under five minutes from a phone. Opening an item should put the two things he actually uses (status and the notes box) within one thumb reach. The page should look considered, calm, and executive, in light and dark mode, without becoming a "product."

## Constraints

- Single self-contained HTML page: inline CSS and vanilla JavaScript, no build step, no frameworks, no external fonts or CDNs (the Mac may be offline from the internet while serving the LAN). System font stack is fine.
- Must render in Safari (macOS and iOS) and Chrome. Phone width 390 px is the primary mobile target; 1280 px and wider for desktop.
- Keep the data model and API exactly as they are. The page talks to `GET /api/items`, `PATCH /api/items/{id}` with `{patch:{...}, note:"..."}`, `POST /api/items` with `{title, note}`, and `GET /api/log`. Field names in the demo's embedded JSON are the real ones.
- Keep the information architecture: the seven views (Triage, Mine, Other-owned, Watch, Decisions, Needs triage, Disposed), search, Add, and Changes. Reorganizing within them is welcome; adding features beyond them is out of scope for this pass.
- Register caps are domain rules, not UI preferences: Register A 15, Watch Active 20, Radar 20. Showing the counts against caps is required; how is open.
- Status choices per kind are fixed: actions open / closed / dropped; watch items active / passive / retired; decisions radar / backlog.
- Light and dark mode via `prefers-color-scheme`. No theme toggle needed.
- No login screen (deliberately open on the home network for now).
- US English.

## Source material (this folder)

| File | What it is |
|---|---|
| `eos_registers_demo.html` | The live page, verbatim, with the server calls replaced by embedded anonymized sample data so it runs from a file. Open it in a browser; edits work locally. This is the artifact to redesign |
| `01_desktop_triage.png` | Default view, 1280 px, light |
| `02_desktop_item_drawer.png` | Item panel open (A58), desktop |
| `03_desktop_watch_view.png` | Watch list view |
| `04_desktop_add_item.png` | Add-item form |
| `05_phone_triage.png` | Default view at 390 px |
| `06_phone_item_drawer.png` | Item panel at 390 px. Note where the notes box is |
| `07_desktop_dark.png` | Default view, dark mode |

The sample data uses placeholder names and titles; the real app carries customer and colleague names, which is why the design should assume dense, specific, sometimes long titles (60 to 120 characters is normal).

## How the page works today

- **Header**: title, seven view chips, search, Add, Changes.
- **Meta line**: counts shown against caps (Register A 15/15, Watch Active 26/20, and so on).
- **List**: one card per item. Columns at desktop: ID, title with tags and a one-line next action, owner, due date (red when past), status dropdown. On phone the card stacks.
- **Triage view** sorts: items needing triage first, then actions (Mine before Other-Owned, Critical first within Other-Owned), then watch, then decisions; within each, earliest due first.
- **Item panel** (drawer from the right, full width on phone): ID and file path, every editable field as a labeled input or select, then a notes textarea, Save, and a read-only "Notes and history" block showing the item's body. Saving writes the file, regenerates the markdown views, commits to git.
- **Add**: title plus optional note; lands as a `T#` item flagged "needs triage" for Claude to classify.
- **Changes**: the last 40 git commits, one line each.

## Known concerns (from the builder, not yet validated with the user)

1. On the phone the item panel is a wall of fourteen fields; the notes box and Save are below the fold. The two most-used controls should come first.
2. The triage view can show 100+ rows (the registers are over cap). It needs a stronger sense of "what is actually due" versus "what is merely open." Grouping, a due-this-week band, or progressive disclosure are all candidates.
3. The one-line "next action" under each title is the most useful text on the page and is visually indistinguishable from owner and tag chrome.
4. Status change on the row is a native `<select>`; on iOS this is a wheel picker, which is slow for a one-tap action.
5. Tag chips (Mine, Delegated, Critical, needs triage, severity) use five colors with no system behind them.
6. Dark mode was derived mechanically from the light palette; nobody has looked at it closely.
7. The "Notes and history" block is a monospace-ish `<pre>` of raw markdown. It is the item's whole history and deserves better than that.
8. Nothing tells the user a save succeeded beyond a small toast; nothing shows what changed in this session.

## Required analysis

1. A usability walk-through of three tasks on the phone and on desktop: (a) mark an overdue item closed and add a two-line note; (b) find everything Critical that is past its gate; (c) capture a new item between meetings in under 15 seconds. Note every step, tap, and scroll; name the friction.
2. A visual audit: hierarchy, type scale, spacing rhythm, color system (including dark mode and the semantic colors for overdue, Critical, needs triage, severity), and density. Say what the page is currently communicating and what it should.
3. A prioritized list of changes, each with the problem it solves and its cost (CSS-only, markup change, or JavaScript change).
4. Redesigned screens for the triage list and the item panel at 390 px and 1280 px, light and dark.

## Output format

1. **A one-page summary** of findings and the recommended direction, written for Darryl to read in two minutes.
2. **Designs**: the triage view and the item panel at both widths, light and dark. Annotate what changed and why.
3. **An updated `eos_registers_demo.html`** implementing the recommended design, so it can be dropped into the real app with the embedded sample data swapped back for the API calls. Keep the `SAMPLE` constant and the function names `load`, `render`, `openDrawer`, `patch` so the swap is mechanical. If a full implementation is too much for one pass, implement the triage list and item panel and leave the rest as is, and say so.
4. **A change list** mapping each design change to the lines or blocks of the HTML it touches.

## Validation criteria

- Each of the three walk-through tasks completes in fewer taps and less scrolling than in the current page; state the before and after counts.
- The notes box and the status control are visible without scrolling when an item is opened at 390 px.
- Counts against caps remain visible on every view.
- The page remains a single file with no external resources and renders in Safari on iOS.
- Dark mode passes a contrast check for body text and for the overdue, Critical, and needs-triage markers.
- Long titles (120 characters) and long next-action lines do not break the layout at 390 px.
- Nothing in the redesign requires a change to the API or the data model.
