# Executive Operating System — Operating Manual

*One-page reference: how the system works, what you provide, what you get, how to use it. Agreed 2026-07-13.*

## The Model

**Copilot collects what happened. You add what Copilot can't see. Claude determines what it means and what to do. The files remember everything.**

Your total time cost: ~5 minutes to feed it, ~5 minutes to read the output.

## The Daily Loop (each working morning)

| Step | Who    | What                                                                                                                         | Time    |
| ---- | ------ | ---------------------------------------------------------------------------------------------------------------------------- | ------- |
| 1    | You    | Run the **Daily Prompt** from `02_Copilot_Intake_Prompts.md` in Copilot; paste output into a session in this folder          | 2 min   |
| 2    | You    | Answer "anything happen outside the record?" — or skip if nothing                                                            | 1–2 min |
| 3    | Claude | Process field notes → reconcile evidence against living documents → write briefing to `Briefings/` → update living documents → drop a copy in `Pandoc/inbox/` and copy the resulting .docx from `Pandoc/output/` to `Briefings/` | —       |
| 4    | You    | Read the briefing (reading pattern below)                                                                                    | 5 min   |
| 5    | You    | Answer 3–5 yes/no closure checks                                                                                             | 1 min   |

Between sessions, say "log: ..." in any chat whenever something closes verbally or a signal appears, **or open the EOS web app from any device on the home network (added 2026-10-15)**: change a status, date or next action, add a note, or add a new item. Claude reads those changes first at the next brief.

## The Registers App (added 2026-10-15)

Start it by double-clicking `Tools/eos-server.command` (leave the Terminal window open, like the Pandoc watcher). It prints the address for other devices (`http://<mac-ip>:8765`). The Focus view (renamed from Triage 2026-10-19) shows your Register A items, Critical other-owned items, Active watch items and the Decision Radar, oldest due first; the other chips show each register in full and the disposed items. Click a row for the full record and the notes box; the status dropdown on the row is the fast path. **+ Add** creates an item flagged for Claude to classify. **Changes** shows the git history. **?** opens the user guide (`Reference/Registers_App_User_Guide.md`): every element, Radar vs Backlog, statuses and tiers, how to change dates and names, best practices. Every save writes the item file under `Registers/`, regenerates 03/04/05, and commits. The register files `03` (Radar and Backlog sections), `04` and `05` are now generated views: read them, do not edit them; edit in the app or ask Claude.

*Pandoc pipeline update (2026-10-05):* template v3 and a filter (`Pandoc/filters/eos.lua`) now set the title, footer, table widths and callout boxes. How it works is in `Pandoc/README.md`. **After any change to `pandoc-watch.command`, restart the watcher** (close its Terminal window, double-click the file).

*Pandoc pipeline note (2026-07-24):* the watcher renders ` ```mermaid ` blocks into diagrams in the .docx via `mermaid-filter` (installed and verified working 2026-07-24). If the filter is ever missing, files still convert and diagrams appear as code blocks.

## The Pulse (added 2026-10-16)

The **Pulse** tab in the web app is your view of the organization: what the team-governed forums (Deployment Daily Scrum, entroCIM Daily Stand Up, the WAM and entroCIM backlog and sprint forums, and the rest) are carrying in a rolling 14-day window. Those issues belong to each team's own governance; you do not track or close them. You see account health (Dell pinned, also shown in the header on every tab), the issues that need your call with one-tap **Escalate** or **Leave with team**, each forum's live and stuck issues with a ready **Governance agenda** for your weekly meeting with that team, and the people carrying the most. Claude fills it from the evidence at each brief. The daily brief carries one Pulse line; the weekly adds the trend. Rules: `CLAUDE.md`, Operational Pulse.

## The Weekly Loop (Friday close or Monday open)

Run the **Weekly Prompt** instead of (or after) the daily. Claude produces `Briefings/YYYY-MM-DD_Weekly.md`: what advanced vs. stalled, decisions made vs. avoided, risk trends, time-below-role-level review, next week's engagement plan and calendar pressure.

## What You Provide

1. **Copilot evidence packages** — daily (24h) and weekly (7d). Prompts are locked with an output contract for repeatability. Re-run the baseline (30d) only after long absences or major reorgs.
2. **Signals, in chat** — the things no system records: hallway decisions, verbal closures, gut signals. Say `log: ...` in any session. Your word outranks Copilot evidence. Use `claude: ...` for requests — process changes, things to remember, drafts, prep, or challenges; these are acted on first. *(`08_Field_Notes.md` was retired 2026-08-19 after sitting empty for 26 days. The file was the friction; chat is not.)*
3. **Closure answers** — one word each, at the end of briefings and to the 16:30 end-of-day check. **This is the highest-leverage minute you spend on the system.** Every register closure in its history has come from you answering, and when the check stopped running for twelve days in August, closures went to zero.
4. **Occasional corrections** — when a characterization in the living documents is wrong, say so; the files are only as good as their last correction.

## What Claude Produces

1. **The briefing — restructured 2026-07-27.** *Daily* is five sections and about one page: evidence coverage, executive summary, top 3 priorities, risks needing action today, and your actions (max 7). *Weekly* adds the planning material: product due dates, delegated and awaiting-others registers, people, meeting prep, blind spots, delegation, Chief of Staff advice, objectives, watch-list delta, decision radar, communication opportunities, analytics, and closure checks. Built to answer one question: *where can you create the greatest leadership impact today?* Priorities capped at three, ranked by business value.
2. **Maintained living documents** — decision log split into Radar and Backlog (03), watch list with Active/Passive/Retired tiers and evidence-basis discipline (04), **four action registers** (05), stakeholder map (06), cadence map (07). These compound; nothing gets re-explained.

   **The four registers (05), added 2026-07-27.** *A — My Actions*: only where you take the next step; every item dated or triggered; max 7 surface daily. *B — Accountable, Delegated*: your org owns it, named executor, you engage at a gate. *C — Awaiting Others*: owed to you, chased on cadence. *D — Standing Responsibilities*: role duties with no completion state, filed in 07 and never counted as commitments. B and C surface weekly.

   **Attribution test.** An item becomes yours only on your words, your confirmation, or as follow-through on a decision you own with no other executor named. Actions raised in meetings you attended do not qualify automatically. If something you meant to own gets parked, it comes back as a one-line question at the weekly closure check.
3. **On demand:** meeting prep for any forum, decision memos, drafts in your voice (exec updates, escalations, recognition notes), pre-read reviews, an `Action_Register.xlsx` shareable view of open items, product deep-dives in `Products/`, **forum registers** (added 09-01 — rolling agenda registers for the WAM Product Leadership Sync and entroCIM Leadership Collaboration in `Deliverables/Portfolio_Admin/`, published ahead of each session and reconciled weekly against `05` and `03` per `Reference/Meeting_Agenda_Standard.md`; say "reconcile the WAM register" or "publish the entroCIM register for Monday"), and a **Sean update** (say "Sean update" — sendable Teams/email draft per `Reference/Sean_Update_Standard.md`, built from the Impact Ledger, decision log, watch list, and commitments).
4. **Analytics (added 07-14):** weekly briefings carry a trend block (decision velocity, commitment aging, watch-list trends, recurring themes, time-at-role, wins captured) per `Reference/EOS_Analytics_Standard.md`. Wins live in `09_Impact_Ledger.md`. Pick the session model per `Reference/EOS_Model_Selection_Standard.md`.
5. **Dashboard — retired 2026-08-06.** Confirmed unused; no longer regenerated. Files left in `Dashboard/` in case the mechanism is repurposed later toward portfolio/product health rather than register health; see `EOS_Value_and_Purpose_Review_2026-08-06.md`.
6. **`Products/` — the front door, elevated 08-06.** Durable knowledge on WAM, entroCIM, JCI, and the CSS Device Lifecycle Assurance ideation program, among others. Start here before evidence reconciliation when the question is "what do I already know about X," not "what happened since yesterday."
7. **`Deliverables/` — the actual force-multiplier output.** Organized in subfolders by initiative (08-06). This, not the daily brief, is where most ad hoc value gets built: briefs, decks, reconciliations, memos.

## Creating Deliverables (PowerPoint, memos, diagrams, documents)

Any content that should leverage your product background gets built in a Cowork session with the EOS folder selected. Claude draws on `Products/`, `Reference/` (including `Communication_Preferences.md` — voice, slide standards, benefit-note format, Mermaid rules), and the living documents, and creates the file (.pptx, .docx, .md) directly in the folder. Just ask: "build the Sean pre-read deck" or "draft the WAM benefits one-pager." Facts used get checked against current evidence; anything new that emerges gets filed per the session-end rule.

## Best Way to Use the Output

- **Read the whole daily briefing** — it is now five sections and about a page, which is what you were already reading. The planning material moved to the weekly, where it is actually useful. If the daily creeps past a page again, say so; that is the system drifting back.
- **Same-day flags come to you in chat**, not buried in the file. If Claude says something needs a reply today, that's the triage.
- **Before any decision-carrying forum**, ask "prep me for X" — Claude pulls the open decisions, commitments, and stakeholder context routed to that forum.
- **Push back.** Challenge severity ratings, evidence basis, characterizations. Corrections make the system smarter; the evidence-basis audit is a standing feature because you asked for it once.
- **Delegation sections are meant to be acted on** — if the same delegation opportunity appears three briefings running, that's the system telling you something.

## Trust Rules

- Field notes (you) > Copilot evidence > inference.
- Every watch-list item carries an evidence basis: Direct / Single-source / Repetition / Inferred. Mention-frequency is never treated as severity.
- Claude states what is known, what is uncertain, and what can still be decided anyway.

## Current Operating Rules (as of 2026-08-19)

- **Register caps.** Watch List Active 20, Decision Radar 20, Register A 15. Forced ranking. When something new goes on, something comes off. `03` and `04` are cut on their own entry test and the overflow is annotated, never deleted. Register A is different: it comes down only by your disposal decisions, so when it runs over 15 you get a single sweep of the most overdue items to close, drop, delegate, or re-date.
- **End-of-day check, weekdays 16:30.** Max six one-line yes/no questions, only what is due, overdue, or stalled. Silent when nothing qualifies. It asks; it never closes anything itself.
- **Sean update, fortnightly.** Produced with the first weekly briefing of each fortnight whether or not you ask, drafted from the Impact Ledger delta and dropped in `Deliverables/Exec_Briefs/`. You edit or discard. Producing it is not sending it.
- **Aging rule checkpoint 2026-09-02.** Count what the 14-day Other-Owned roll-off actually cleared. If it is fewer than ten, the clock goes retroactive and the Critical tags get re-audited.
- **The pilot is closed.** Its evidence-discipline rules are permanent; its measurement and feedback sections are gone.
