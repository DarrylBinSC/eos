# EOS Registers: One Item per File, Browser Editing, Read-First Briefings

Date: 2026-10-15. Decision owner: Darryl Benson. Built by Claude the same day.

## Why

The EOS knowledge base (`Products/`, `01`, `06`, `Reference/`) was serving its primary use case well: document creation, analysis and executive updates. The dynamic registers (`03` Radar and Backlog, `04`, `05`) were not staying current, because updating them meant opening large markdown files and dictating changes to Claude. Darryl's diagnosis, 2026-10-15: the files were becoming a dumping ground rather than working documents, and the fix is visibility and a cheap update path, not another structural redesign.

This is consistent with the 2026-08-19 finding that register overgrowth is a disposal-throughput problem, not a structure problem. Nothing in the four-register model, the attribution test, the tiers, or the caps changes. The storage shape changes so that disposal costs seconds instead of minutes.

## Decisions (Darryl, 2026-10-15)

| Decision | Choice |
|---|---|
| Storage | Option B: one item per file with front matter; `03` Radar/Backlog, `04` and `05` become generated views. Option A (parse and rewrite the existing tables in place) rejected for parser fragility and no per-item notes. Option C (artifact with its own database) rejected: breaks files as source of truth, no LAN access |
| Archive items | Migrated as items with `status: closed / dropped / aged_out` so the disposed-item check becomes a query |
| Creating items from the browser | Yes. New items land as `T#` with `needs_triage: true` and `register: triage`; Claude classifies them at the next brief. This replaces `log:` for anything thought of between meetings |
| Access control | Open on the home network for now; password deferred (`EOS_PASSWORD` in `Tools/eos-server.command` turns it on) |
| Git | Initialized in the EOS folder by the launcher on first run; every change commits |
| Host | Darryl's Mac, always on with the screen off; server bound to the LAN |

## What changed in the folder

| Path | Status | Notes |
|---|---|---|
| `Registers/action/*.md` | New, source of truth | Register A, Other-Owned, Closed, Aged Out, Dropped, and `T#` triage items. 253 files |
| `Registers/watch/*.md` | New, source of truth | Active, Passive, Retired. IDs `W001`–`W097` assigned at migration (none existed) |
| `Registers/decision/*.md` | New, source of truth | Radar and Backlog. IDs `D001`–`D095` assigned at migration (none existed) |
| `05_Commitments.md` | Generated | Tables only, plus the standing rules. Session prose that used to accumulate between tables is in the archive and in git history |
| `04_Executive_Watch_List.md` | Generated | Same |
| `03_Decision_Log.md` | Part generated | Only the Decision Radar and Decision Backlog sections are generated. Decisions Made, Entry Format, and Decisions Being Avoided or Stalled remain hand-maintained |
| `Archive/2026-10-15_pre_registers/` | New, frozen | Byte-for-byte copies of the three files before migration |
| `Tools/eos_registers.py` | New | Front matter read/write, item loading, generators |
| `Tools/migrate_2026-10-15.py` | New, one-time | Refuses to run twice. Report: `Deliverables/EOS_Meta/2026-10-15_Registers_Migration_Report.md` |
| `Tools/eos_server.py` | New | Web app and API; watches `Registers/` for outside edits and regenerates and commits them |
| `Tools/eos-server.command` | New | Launcher. First run initializes git |
| `.git/` | New | Created by the launcher on the Mac |

## Item schema

Flat front matter (no nesting, no YAML library required), then a markdown body for notes and dated updates.

Common: `id`, `kind` (action / watch / decision), `title`, `status`, `owner`, `product`, `next_action`, `source`, `created`, `last_touched`, `closed_date`, `closed_by`, `disposition_note`, `needs_triage`, `tags`, `legacy_section` (where the row came from at migration).

Action: `register` (A / other / triage), `type` (Delegated / Awaited), `counterparty`, `due` (ISO), `due_note` (gate text), `trigger`, `critical` (bool), `critical_reason`, `basis`.

Watch: `tier` (active / passive / retired), `severity`, `trend`, `evidence_basis`.

Decision: `tier` (radar / backlog), `status` (free text, as before), `forum`, `forum_date`.

`status` values for actions and watch: `open`, `closed`, `dropped`, `aged_out`. A watch item set to tier `retired` is closed. A decision marked RESOLVED in its old heading migrated as `status: closed` with the date.

Body conventions: migrated Register A items carry `## Next step` with the full original text; Other-Owned and watch items carry the original Note cell; decisions carry their original bullets minus the ones lifted into front matter (Status, Owner, Forum, Next action, Source). Notes added in the app append as `YYYY-MM-DD (Darryl, web): ...`.

## Migration findings worth acting on

- **A29 and C62 had no value in their Due / Gate column** (the source rows were one cell short). Both are now undated items in the registers. A29 is Register A and the dating rule says it must carry a date or be dropped.
- **C-i3-3 appeared twice** with different content; the second is `C-i3-3b`. The i3 items use a non-standard ID pattern (`C-i3-1..3`); left as is.
- **A1, A3, A9, A14 were reused**: each ID has a dropped item from July/August and a different live item today. The old ones are `A1-old` etc. New IDs are now allocated by scanning all files, so this cannot recur.
- **B8** was struck through in the live Other-Owned table and also recorded in Archive, Closed. The archive row is the record.
- Watch Active holds 27 against the cap of 20 and Radar 35 against 20. The migration did not change that; the app makes it visible on every open.

## Process changes (recorded in CLAUDE.md the same day)

1. Claude edits item files, never the generated tables. `03` Decisions Made and Avoided/Stalled are still hand-edited.
2. **Read first.** Every daily or weekly brief starts by reading what Darryl changed since the last brief: `git log --since=<last brief date> -- Registers` and the diff, plus every item with `needs_triage: true`. Those are reconciled before any new evidence is processed. The brief names what it found.
3. The end-of-day check reads the same two things and asks only about items that are not already dispositioned in the registers.
4. The web app is the notes channel. A note Darryl adds to an item is evidence from Darryl (outranks Copilot), the same as `log:` in chat.
5. The server watches `Registers/` and regenerates and commits anything changed outside the app, so Claude's session edits and any text-editor edits get the same treatment. If the server is not running, the next start catches up.

## Observable artifacts that prove this is running (per the 2026-08-25 rule)

- `git log` in the EOS folder shows `web:` commits on days Darryl used the app and `edit outside the web app:` commits on days Claude filed.
- Briefings carry a "Changes since last brief" line naming commits and triage items processed.
- `05_Commitments.md` carries a `GENERATED` banner with a timestamp that moves.

If any of those stops moving for a week, check whether the server is running before concluding anything about engagement.

## Deferred

- Password on the LAN (`EOS_PASSWORD`).
- Per-product views and filters beyond search; build after two weeks of using the triage view.
- A cap sweep on Watch Active and Radar; a disposal exercise for Darryl, not a migration task.
- Impact Ledger (`09`) stays as it is.
