# EOS Registers: direction 1a (Ledger)

## Two-minute summary
The page worked but treated every item the same: 17 identical cards with a date somewhere on the right. 1a sorts by urgency instead. Triage is split into bands: **Needs triage, Overdue, Due this week, Later, No date, Watch**. The bands answer "what is actually due" before you read a single date. The next action sits directly under each title in body ink, because it is the most useful line on the page. Every row has a one-tap status control, so you never hit the iOS wheel picker. Opening an item shows status, the note box and Save first. The other 13 fields wait under "Details". On a laptop the panel docks on the right, so you can work down the list without opening and closing a drawer.

There is one color rule: **red means late or Critical, amber means waiting for your triage**. Everything else is neutral. Dark mode was rebuilt by hand, not inverted.

## Walk-throughs (before → after)
- **(a) Close an overdue item and add a two-line note, phone:** 6 taps + 2 scrolls (open, status select, wheel, Done, scroll to note, type, scroll, Save) → 4 taps, 0 scrolls (open, Closed, note, Save).
- **(a) Same task, desktop:** 5 clicks + 1 scroll → 4 clicks, 0 scrolls.
- **(b) Critical items past their gate:** scan every row for red date + Critical chip, several scrolls at 100+ rows → open Triage; the Overdue band is at the top with CRITICAL marked in red. Typing "critical" in search narrows the bands (search now matches the Critical flag).
- **(c) Capture a new item:** 3 taps (Add, focus title, Add) → 2 taps (Add, title is focused; Add or Return).

## Prioritized changes
1. Status and note first in the panel; fields collapsed under Details. *Markup + JS.*
2. Segmented status on rows and in the panel, replacing `<select>`. *Markup + JS.*
3. Triage bands, with Watch collapsed to its top 3 by severity. *JS (`groups()`).*
4. Next action promoted to its own line; owner/type moved to a quiet meta line. *Markup + CSS.*
5. Semantic color system and a hand-tuned dark palette. *CSS only.*
6. Cap meters in a fixed strip on every view; a bar turns red over cap. *Markup + CSS.*
7. History rendered as a dated timeline, newest first, instead of a `<pre>`. *JS (`history()`).*
8. Saves confirmed in the panel ("Saved 9:41 · Closed · committed"); a session count on Changes; the Changes panel lists this session's edits. Rows you change stay in place, struck through, until you switch views. *JS.*
9. Docked panel at ≥1100 px, overlay below, full screen at ≤820 px; 44 px targets and 16 px inputs on phone (no iOS zoom). *CSS.*

## Change list (eos_registers_demo.html)
- `<style>`: fully replaced. Tokens in `:root` plus a dark block; header/tabs/caps; `.group/.row/.seg`; panel; phone `@media (max-width:820px)`.
- `<header>`: chips → `<nav id="views">` tabs with counts (rendered in `render()`); added a phone-only `#searchBtn`; `#meta` is now the caps strip.
- `filtered()`: same filters and sort, now via `inView()`. Membership checks `BASE[id]` (the item before this session's edits). Search also matches Critical, severity and type.
- New `groups()`, `rowHtml()`, `seg()`, `dueInfo()`, `context()`, `who()`; `tags()` rewritten.
- `render()`: draws tabs, caps strip, Changes badge and grouped list.
- `patch()`: same local write; also records `BASE`, `SESSION`, `SAVED` and refreshes an open panel. **API swap goes here.**
- `openDrawer()`: rebuilt (head, status, note form, history, Details form). Keeps typed note and scroll position on refresh.
- New `layout()/showDrawer()/closeDrawer()`, `history()`; Escape and scrim close the panel.
- `#newBtn`, `#logBtn` handlers: same behavior, restyled; Changes adds a "This session" list.
- Unchanged: `SAMPLE`, `load()`, field names, status vocabularies, API shape.

Fully implemented: triage list, item panel, Add and Changes. Other views reuse the same row in a single group.

## Contrast (WCAG AA, 4.5:1)
All pairs pass in both modes. The lowest is light-mode inactive status labels at 4.97; muted grey was darkened to `#5f666e` to get there. Dark mode: body 13.7, overdue and Critical red 7.1, needs-triage pill 9.7. The full table is in `EOS 1a Final Screens.dc.html`.

## Safari / iOS audit (code review, not tested on a device)
Fixed in this pass:
- `-webkit-appearance:none` on the search box and textarea, so iOS keeps the rounded style.
- `cursor:pointer` on the scrim, because iOS won't fire taps on a plain div without it.
- The page behind is locked while an item is open full screen (`body.locked`), and `overscroll-behavior:contain` stops scroll from leaking out of the panel.
- Tap highlight removed on rows, tabs and buttons.

Already safe:
- 16 px inputs on phone, so iOS doesn't zoom.
- `viewport-fit=cover` + `env(safe-area-inset-*)` for the notch and home bar.
- The Add title is focused inside the tap, so the iOS keyboard opens.
- No `100vh`.

Degrades gracefully:
- `text-wrap:pretty` is ignored before Safari 26; titles wrap normally.
- `<summary>` as flex needs Safari 16+; older versions show Details as a plain line.

Still to do: open on Darryl's iPhone and Mac Safari; check that the note box stays visible above the keyboard.

## Review-only URL options
`?theme=light|dark` forces a color scheme; `?open=A61` opens an item. They are used by the annotated screens and are marked in the last lines of the script. Delete them before deploying if you like; nothing else depends on them.
