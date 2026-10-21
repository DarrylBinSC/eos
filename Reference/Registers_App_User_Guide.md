# EOS Registers: User Guide

What each element means, what to do with it, and what Claude does with what you enter. Also opens from the Help button in the app.

## What you are looking at

Every row is one item file under `Registers/`. There are three kinds:

- **Actions** (IDs A, B, C, T): things someone has to do.
- **Watch items** (W): risks being tracked.
- **Decisions** (D): questions that need a decision.

Everything you change in the app is written to that item's file, the summary files `03`, `04` and `05` are regenerated, and the change is committed to git. Claude reads your changes first at the next morning brief, before any Copilot evidence, and treats them as your word.

## The views

| Tab | Shows |
|---|---|
| **Pulse** | What your team-governed forums are carrying, in a rolling 14-day window: what needs your call, your pinned account, how many forums you heard from, account health, live issues, your weekly governance, knowledge risks, and the people carrying the most. See Pulse, below |
| **Copilot** (header button, added 2026-10-19; also on the Pulse tab) | Every Copilot prompt in one place. A Today list says what to run: the Weekly prompt on Mondays, the Daily prompt Tuesday to Friday (ticked once that day's package is saved in Evidence), then Pulse Prompt 1 (Delivery track) and/or Prompt 2 (Development track) only when needed. Each card has a named Copy button, and the confirmation says which prompt you copied. The Daily and Weekly text is read live from `02_Copilot_Intake_Prompts.md`, so editing that file updates the app |
| **Briefs** (added 2026-10-19) | Every daily and weekly brief, newest first, grouped This week / Last week / Earlier. A dot on the tab means today's brief is in. The brief opens formatted, with the Risk and Decision Required boxes; every item ID in it (A61, W021, C72) opens that item so you can close, re-date or note it without leaving the brief. The Word version is one tap away. Charts show in the Word version only |
| **Focus** (renamed from Triage 2026-10-19) | What needs your attention: your own actions, Critical other-owned actions, Active risks, and Radar decisions, in bands by urgency (needs triage, overdue, due this week, later, no date, watch) |
| **Mine** | Register A: actions only you can move. Ceiling 15 |
| **Other-owned** | Actions you delegated (Delegated) or are waiting on from someone else (Awaited) |
| **Watch** | All open risks, Active and Passive |
| **Decisions** | Radar and Backlog |
| **Needs triage** | Items you added that Claude has not classified yet |
| **Disposed** | Closed, dropped, aged out, retired. The record; nothing here needs action |

**Sorting (added 2026-10-16).** Every list has a Sort control above it that states the order in use. Watch, Decisions and Needs triage default to ID order (W001, W002 ... W010, numeric, not alphabetical); Mine and Other-owned default to due date, with undated items last; Disposed defaults to most recently disposed; Triage and Pulse default to their attention order, which the bar spells out. Choose another order or reverse it; the app remembers your choice per tab on that device. Ties always fall back to ID.

The strip under the tabs shows each capped register against its ceiling. Red means over cap. The caps are rules of the system, not of the app: Register A 15, Watch Active 20, Decision Radar 20.

## Actions

**Register A (Mine)** holds an item only if you said you would do it, confirmed it, or it is direct follow-through on a decision you own with no other executor. If someone else is named anywhere, it is Other-owned. Every Register A item carries a **due date or a trigger**.

**Other-owned** items have an **Owner**, a **Type** (Delegated: your organization executes; Awaited: owed to you), and may be **Critical**. Critical means: if this went quiet and never came back, something would happen that you would have paid to prevent (a customer sees it, money or contract is exposed, or it gates something on a date). Importance alone is not Critical. Non-Critical items age out automatically after 14 days with no evidence; Critical items stay until you close them.

**Status**, one tap on the row or in the panel:

- **Open**: live.
- **Closed**: done. The close date is recorded automatically.
- **Dropped**: deliberately not doing it. Permanent do-not-re-add; if it resurfaces, Claude tells you it was dropped before.

**Trigger** is the alternative to a due date: an event that makes the action live ("once the entitlement document arrives"). Use it only when a date is impossible. A trigger that has not fired in 14 days gets asked about and must be re-dated, converted, or dropped.

## Watch items

Each has a **Tier**:

- **Active**: needs attention or a decision now. Ceiling 20.
- **Passive**: logged for completeness, no action; escalates on a direct signal.
- **Retired**: closed, with the reason in the history.

**Severity** (High, Medium, Low) and **Trend** (↑ worsening, → stable, ↓ improving, New). **Evidence basis** says how the risk is grounded: Direct (a concrete event), Single-source, Repetition (recurring mention), or Inferred (a pattern Claude drew). Mention-frequency is never treated as severity.

Moving an item from Active to Passive is the normal way to get back under the cap; it is reversible in one tap.

## Decisions: Radar and Backlog

Both hold open decisions. The difference is routing.

- **Radar**: the decision has a named forum and a live date for being taken (a specific meeting, a review, an AOP gate). This is the list the weekly brief works from. Ceiling 20. A Radar item whose forum date has passed with no decision and no new date fails the test and belongs in Backlog.
- **Backlog**: raised, real, but not yet routed to a forum or date. Reviewed monthly or on demand. Moving an item to Radar means naming where and when it will be decided; set **Forum** and **Forum date** in Details when you do.

Decisions do not have open/closed status in the app. When one is made, tell Claude (a note is enough); Claude records it in `03` Decisions Made and closes the item.

## The item panel

Opens when you click a row. Top to bottom:

1. **Status** segment: one tap saves.
2. **Note box**: what happened, what you decided, what Claude should know. Dated, appended to the item, committed. Lists work: type `1. ` or `- ` and press Return.
3. **History**: everything on the item, newest first. Your notes and Claude's updates are dated entries; the original record sits beneath.
4. **Details** (click to expand): every field, including title, owner, dates, product, basis. Save with "Save details".

## Changing dates, names and other fields

Open the item, expand **Details**, edit, click **Save details**. Dates are `YYYY-MM-DD`. For actions the date field is **Due**; for decisions it is **Forum date** (and **Forum**). Titles, owners and counterparties are plain text fields. A corrected title is as much your word as a note; Claude reads the change at the next brief and carries it into any other file that repeats the fact.

If a correction is bigger than a field (the item is really about something else, or two items are one), write a note saying so and Claude restructures it.

## Adding items

**Add** takes a title and an optional note. The item lands as `T#` with the "needs triage" flag. At the next brief Claude classifies it: your own action, delegated, awaited, a risk, or a decision, with the right ID, and clears the flag. Use it for anything you think of between meetings; it replaces typing `log:` in chat. If you already know which register it belongs in, say so in the note.

## Changes

Lists what you changed this session and the recent git commits. Every save is a commit, so the folder's history is the audit trail.

## Best practices

- Clear the Focus view, top band first, when you have five minutes. Overdue first, then due this week.
- Status on the row, note in the panel. Do not write "closed" in a note; tap Closed.
- One line of next action per open item is the most useful text on the page. If the next action shown is stale, fix it in Details.
- Keep dropping things. Register A comes down only by disposal; Watch Active and Radar come down by moving items to Passive and Backlog. Caps in red are a disposal prompt, not a failure.
- Dates everywhere. An undated action is invisible to the overdue band and to the end-of-day check.
- Say the uncertain thing in the note. "Potentially done, confirm with Ron" is better than silence; Claude will ask the right question.

## What Claude does with it

- **Morning brief**: reads your changes and notes since the last brief, classifies new `T#` items, carries corrections into the other files, then processes the evidence package. The brief names what it found.
- **End-of-day check (16:30, weekdays)**: asks about items due today or overdue, triggers that have not fired, and anything you added that needs classifying. Skips anything you already dispositioned in the app that day.
- **Weekly brief**: closure checks on the oldest open items, Radar review, register health.

## When something looks wrong

- An item shows old text after you saved: reload the page; the server regenerates within seconds.
- Items Claude filed during a session do not appear: wait up to 30 seconds, or switch away from the tab and back. Since 2026-10-20 the page checks for file changes every 30 seconds and whenever the tab regains focus, and re-reads the files when they have changed (you will see "Updated from the files"). It never refreshes while you have an item open or are typing, so finish or close what you are doing and it catches up on the next check.
- The page will not load from your phone: the server is not running on the Mac. Double-click `Tools/eos-server.command`.
- A name or fact is wrong in several places: fix the item and add a note; Claude propagates it. You do not need to find every copy.

## Pulse (added 2026-10-16)

**Layout (updated 2026-10-16).** The top row is Today: **Needs your call** (each with a one-line reason: you were asked, it crosses a team boundary, it has been stuck ten business days, and so on), your **pinned account** (its 7-day trend, its load, and a line of the team-raised load day by day; see How load and trend are calculated, below), and **Evidence**, which says how many of the 13 forums you heard from in the window. In the evidence strip and in governance, a filled mark means an issue was raised, an outline means the forum met and nothing was raised, and hatching (or a dash) means no evidence: the forum may have been quiet or may simply not have been covered. Treat "not heard" as a gap, not as good news; the governance agenda opens by naming those forums so you can ask. **Issue rows.** Each live issue shows its badges (severity, customer-visible, "Stuck · raised since", New for anything first raised in the last seven days, Escalated), the owner (or "No owner named" in red), the account, forum and last raised date, and the next action. The buttons follow the issue's state: Escalate and Leave with team; Left with team plus Escalate if you change your mind; or Open Watch for one already escalated. Tick "Include quiet and resolved" to see the rest. When a filter is on, the "Showing" chip stays at the top as you scroll. **On phone**, tapping an issue opens a preview sheet with the next action, owner, people named, forum, dates and links; Escalate, Add a note and "Full detail and history" are at the bottom. **Open agenda** opens the governance meeting view: a not-heard banner, numbered sections (stuck, needs a decision, new this week, gone quiet, who backs up whom) and a side rail with the track's counts, forums and escalations. Use Present full screen to put it on a shared screen, or Copy as text to paste it into the meeting chat or notes. **People** shows the top eight (Show all for everyone); Owns and Involved are Pulse counts, Delegated is from your registers, and a dot means none. **Knowledge** entries show coverage, exposure, holder and backup, and the mitigation; quiet entries are listed in one line at the bottom. **Pinning:** use Pin on any row of the account table to make that account the one in the Today row; only one account is pinned at a time. **Phone:** the page runs calls, pinned account, evidence, live issues (first four, then Show all), governance (summary, Open agenda, Forums), then accounts, knowledge and people as summary rows you can open.

The Pulse is how you keep a finger on the organization without tracking work that belongs to someone else. Issues raised in team-governed forums (the Deployment Daily Scrum, the entroCIM Daily Stand Up, backlog refinement, sprint reviews and the rest) run on each team's own governance: a project process or a sprint cycle. They live here, not in the registers.

**Nothing in the Pulse needs closing.** An issue stays live while the forum keeps raising it. When it has not been raised for 14 days it goes **quiet**: either it was resolved or nobody is talking about it, and the governance agenda asks the team which. You can mark an issue Resolved if you know it is.

### How load and trend are calculated

Changed 2026-10-19 from a score out of 100, which bottomed out at 0 for Dell once the team-forum backlog was captured and could no longer show change.

**Load** is the weight of everything open about an account. Each item adds points:

| What is open | Points |
|---|---|
| Live issue, High, customer can see it | 8 |
| Live issue, High, internal only | 6 |
| Live issue, Medium | 3 |
| Live issue, Low | 1 |
| Stuck: still raised 10 or more business days after it first came up | +4 on top |
| Needs your call (an open call on an issue or a knowledge risk) | +3 on top |
| Quiet issue: not raised in 14 days, not confirmed resolved | 1 |
| Item about the account on your own registers (Watch Active, Register A, Critical other-owned) | 5 |

Worked example, Dell on 2026-10-19: 9 High customer-visible issues (72) + 7 Medium (21) + 2 stuck (8) + 2 quiet (2) + 7 open calls (21) = 124 team-raised points, plus 1 register item (5) = load 129.

**Trend** is the headline: how much the team-raised load moved in the last 7 days. Each issue counts from the day a meeting raised it, not the day the evidence reached Claude, so a late Copilot run does not show up as a sudden jump. **Worsening** or **Improving** means a move of at least 5 points and at least 15% of last week's load; anything smaller is **Steady**. Your register items count in the load but not in the trend, because they have no dated history.

**Baseline.** Forum-by-forum capture began with the meetings of 2026-10-13. Until 2026-10-20 an account shows **Baseline** with its load and the daily line instead of a trend, because comparing against the week before capture began would show capture starting, not the account changing.

**Reading it.** The number is operational friction from the evidence, not customer sentiment, and it only counts what the forums were heard saying: check "Heard from n of 13 forums" before reading a flat line as calm. The weights are Claude's first cut, so tell Claude when the trend does not match your read of an account.

**Needs your call.** An issue lands here when it meets one of four tests: you were **asked** (named for a decision, resource or escalation); it **crossed a boundary** the forum cannot settle (contract, money, a customer executive, what to tell the customer, a team outside the forum); it is **stuck** (still being raised 10 or more business days after it first came up); or there is a **gap** (no owner, or the customer is unaware of a material problem). Severity alone is not a test: a High issue with an owner is the governance working.

- **Escalate** creates an Active Watch item linked to the issue. The team still owns the work; the Watch item tracks your part.
- **Leave with team** records that you looked and decided it is theirs. It stays in the Pulse and can still be escalated later.

**Account table** (formerly tiles). One tile per account on the roster (`Registers/pulse/_accounts.json`: Dell, Wesco Warehouse, Ford, Federal Reserve, Coca-Cola, BAE, Stanford, Louvre Abu Dhabi, UWM) that has a live Pulse issue or an open item on your registers. Accounts with neither are listed underneath as "no signals." Dell is pinned first; the rest run Worsening first, then Steady, then Improving, and by load within each. Internal and partner accounts are labelled.

**Following a tile or a name to the items.** Tap an account tile or a person and the Pulse filters to them: their Pulse issues come straight after the tiles, followed by **On your registers**, the register items behind the numbers (for an account, the "on your registers" count in its tile; for a person, their Delegated count). Each row says which register it lives in; tap it to open it, or use its status buttons as you would on that tab. When an account or person has nothing in the Pulse at all, only that register list shows. Clear returns to the full Pulse.

**Knowledge concentration.** Where one person holds knowledge a customer, a release or a migration depends on. Each entry names the knowledge area, who holds it, the backup (if any), coverage (no backup, backup unknown, partly covered, covered), what is exposed, and any mitigation under way. It is a different risk from load: the fix is a backup, documentation or cross-training, not a lighter workload. Entries stay live for 45 days after the last evidence, because silence does not remove a single point of failure. One becomes a call for you when no backup is confirmed and a customer or release depends on it, or when the holder's absence or departure is near or has passed without a confirmed handover. Filter by a person to see the areas they hold, and each track's weekly agenda ends with "who backs up whom, and by when."

**Forums.** Each card shows live, new this week, stuck and quiet counts. **Governance agenda** produces a ready agenda for your weekly governance meeting with that team: stuck items first, then decisions, new, still open, gone quiet, and anything escalated. Copy it into the invite or Loop. Forums marked with an asterisk have a classification you have not confirmed yet.

**People.** Where named people concentrate. **Owns** counts live Pulse issues they own; **Involved** counts live issues where the evidence names them (a statement, a commitment or a stated role) but someone else owns it; **Delegated** counts their open delegated or awaited register items. Attending a meeting does not make someone involved. Tap a name: their issues appear in two groups, the ones they own and the ones they are named on, with the owner shown on every row. This is the view behind the knowledge-concentration watch (W066).

**Where it comes from.** Claude infers Pulse issues from transcripts and evidence at each brief, adds a dated sighting to an existing issue when the forum raises it again, and proposes calls. Your escalations and notes are your word and are read first at the next brief. The header strip always shows Dell health and the number of open calls, on every tab.

## Products tab (added 2026-10-21)

One card per product you have marked live. Each card shows how fresh the product file is, how many entries were added in the window (7, 14 or 30 days; the choice is remembered on this device), the open register items by kind, and the newest entries with the item IDs they cite. Tap an ID to open the item. "Open register items" lists everything open that touches the product. A live product with nothing new still shows, and says so.

Hide (bottom of a card) removes the product from the tab; the footer lists hidden products and Change lets you show one again. Both write to `Products/_products.json` and commit. Nothing is deleted.
