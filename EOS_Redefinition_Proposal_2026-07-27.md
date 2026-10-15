# EOS Redefinition Proposal

**Date:** 2026-07-27
**Status:** PROPOSAL. Nothing in the operating files has been changed. Adoption requires Darryl's approval.
**Scope:** Registers (05), decision log (03), watch list (04), briefing format, dashboard.
**Out of scope:** New product workstream (Device Lifecycle Assurance / AOP 2027 concept). Untouched by this proposal.
**Supersedes:** Portions of the 30-day pilot rules dated 2026-07-16. See §7.

---

## 1. Problem Statement

The EOS is capturing the right material and losing it to volume and mis-attribution. Darryl's stated symptoms, 2026-07-27: commitments are misinterpreted and possibly overstated; focus is diluted rather than sharpened; it is unclear what is next. Product tracking and general awareness are working and are not the problem.

Measured state of the files as of this date:

| Measure | Value |
|---|---|
| Open items in `05_Commitments.md` | 62 |
| Open items filed under "Commitments Darryl Made" | 39 |
| Of those, items whose actual owner is someone else | 6 |
| Of those, items generated from a single meeting (WAM Data Challenges, 07-23) | 7 |
| Of those, standing role responsibilities that can never close | 4 |
| Of those, carrying no date ("Not specified" / "Not dated") | 30 |
| Closed rows still sitting inline in active tables (05) | 25 |
| "Decisions Approaching" entries in 03 | 34 |
| Watch rows in 04 | 48, of which 9 are resolved or downgraded and still in the Active table |
| Watch rows carrying no severity, trend, or evidence basis | 2 |
| Briefing size, 2026-07-13 to 2026-07-27 | 7.9 KB to 25.5 KB |
| Briefing sections Darryl reads by design (per `00_README`) | 4 of 16 |

Every register is growing monotonically. None has a working archive. `05` lists "Completed / Closed: *(none yet)*" while carrying 25 closed rows inline; `04` lists "Retired Items: *(none yet)*" while carrying 9.

## 2. Root Causes

Three causes, only one of which is volume.

**2.1 The intake has no attribution test.** Nothing in `CLAUDE.md` or `02_Copilot_Intake_Prompts.md` defines when a meeting-derived action becomes Darryl's commitment. Copilot extracts action items from sessions Darryl attended, and they land in his column by default. The 07-27 briefing itself notes that several Copilot attributions are labeled "Inferred" by Copilot; they were carried into `03` with a caveat rather than held back. The seven items generated from the single 07-23 WAM Data Challenges session are the clearest instance: group actions from a forum recorded as Darryl's personal commitments.

**2.2 The schema encodes the ambiguity.** The `05` table header is `Commitment | Expected By | Due | Status | Risk if Slipped | Source`. "Expected By" holds a counterparty, not a date, and there is no Owner column. So these two rows are structurally identical and mean opposite things:

- `Analyze AI project ideas for CSS-synergy | Sean McCloskey` (Darryl owes Sean)
- `Brian Miller to send final markup to JCI | Brian Miller` (Brian owes Darryl)

A nested table headed "Commitment owed to Darryl" sits inside the "Commitments Darryl Made" section, placing four JCI/Ascent items owned by Jeff McCorvey and Mike Reed in Darryl's list.

**2.3 No single home per fact.** QPM 3.4.3 appears six times in the 07-27 briefing: executive summary, priority 1, Key Product Due Dates, risk table, watch-list delta, and decision radar. AOP appears three times. Duplication is the main driver of the threefold briefing growth, and it also means a status change has to be applied in several places or the record diverges.

**Consequence.** 30 undated items in a flat list produce no ordering, so the register cannot answer "what is next." The briefing's commitment section surfaced 8 of 62 items using an unstated selection rule, so the selection reads as arbitrary. Both effects match the reported symptom precisely.

## 3. Decisions Taken (Darryl, 2026-07-27)

| # | Decision | Choice |
|---|---|---|
| D1 | Attribution standard for Darryl's personal action register | **Strict**: Darryl's own words in evidence, or his confirmation |
| D2 | Briefing structure | **Short daily, full weekly** |
| D3 | Ordering of the personal action register | **By date; undated items forced to a decision** |

## 4. The Framework

### 4.1 Four registers replacing two sections

`05_Commitments.md` is replaced by four clearly delineated registers. The delineation is the point: today one list mixes four different kinds of obligation, which is what makes the count feel overstated.

| Register | Contains | Test | Appears in briefing |
|---|---|---|---|
| **A. My Actions** | Darryl personally takes the next step | If Darryl does nothing, this does not move | Yes, capped and rule-selected |
| **B. Accountable, Delegated** | Darryl's org owns it; named executor; Darryl engages at a gate | Darryl is answerable for the outcome but not the next step | Gate dates only, in Key Product Due Dates |
| **C. Awaiting Others** | Owed to Darryl by anyone, internal or external | Darryl's action is chasing, not doing | Only when aging past threshold or blocking a dated item |
| **D. Standing Responsibilities** | Recurring role duties that never close | Has no completion state | No. Moves to `07_Operating_Cadence.md` or `01` |

Register D leaves the commitment system entirely. Items such as "Leadership oversight of WAM data challenges," "Participate in WAM executive product review process," and "Keep Sean aware of ADM defects (Ongoing)" are role definition, not commitments. Counting them permanently inflates the register and dilutes items that can actually be closed.

Estimated Register A size after re-sort: **10 to 14 items**, from the current 39.

### 4.2 Attribution test (D1, strict)

An item enters **Register A** only if one of the following holds:

1. Evidence shows Darryl stating he will do it (email, chat, transcript, in his own words), or
2. Darryl confirms it in a field note or session, or
3. It is a direct follow-through on a decision Darryl owns and no other executor is named.

An item does **not** enter Register A if:

- It was raised in a meeting Darryl attended without Darryl accepting it. It goes to B or C with the named owner, or is not tracked.
- Copilot labels the attribution "Inferred." Inferred attributions are surfaced once in the briefing as a confirmation question, never written into Register A first.
- Another owner is named anywhere in the evidence.

**Failure mode this accepts:** occasionally an item Darryl did intend to own will be parked in B or C until he confirms it. Mitigation: unconfirmed-attribution items are surfaced in the closure-check block as "Is this yours?" rather than silently dropped. This is the deliberate trade for a register Darryl can trust at face value.

### 4.3 Schema

Register A columns:

`Action | Owner (always Darryl) | Counterparty | Next Step | Due | Basis | Status | Source`

- **Counterparty** replaces "Expected By." It is a person, never a date.
- **Next Step** is the concrete physical action, not the objective.
- **Basis** records how it became Darryl's: `Stated` / `Confirmed` / `Decision follow-through`. This makes attribution auditable, which is the check that was missing.

Registers B and C carry an explicit **Owner** column naming the actual executor.

### 4.4 Dating rule (D3)

Every Register A item carries one of:

- a **date**, or
- a **review trigger** (a named event that makes it actionable, e.g. "after JCI markup ships 07-31"), or
- it is **dropped**.

No item stays undated. Register A sorts by date, with triggered items in a separate short block beneath. This is the mechanism that answers "what is next" without interpretation.

### 4.5 Briefing focus rule

The daily briefing surfaces at most **seven** Register A items, selected by a rule written into `CLAUDE.md` rather than by judgment each morning:

1. Due within 14 days, or
2. On the critical path of a Key Product Due Dates milestone, or
3. Aging past 21 days with no status movement.

Everything else lives in the file and is not surfaced. The rule is stated in the briefing so the selection is inspectable and challengeable.

### 4.6 Briefing structure (D2)

**Daily (target: one page, sections 1 to 5):**

1. Evidence coverage line (one line, pilot rule retained)
2. Executive Summary, max 5 bullets
3. Top 3 Leadership Priorities
4. Risks requiring action today
5. My Actions (rule-selected, max 7)

**Weekly (full format):** the daily five plus Key Product Due Dates, People Requiring Engagement, Meeting Preparation, Blind Spots, Delegation Opportunities, Chief of Staff Advice, Objectives, Watch List delta, Decision Radar, Communication Opportunities, Analytics block, System Feedback.

Sections 6 through 16 are planning and delegation material. They are useful weekly and are noise daily, which is why the operating manual already instructs reading only 1 through 4.

### 4.7 Single home per fact

| Fact type | Canonical home | Everywhere else |
|---|---|---|
| Decision | `03_Decision_Log.md` | Referenced by title only |
| Risk | `04_Executive_Watch_List.md` | Referenced by title only |
| Action | Register A/B/C | Referenced by title only |
| Date | Generated from 03 and Registers, not maintained separately | Key Product Due Dates table is a view, not a source |

Where an item legitimately spans types (QPM 3.4.3 is a risk, a decision, and a date), it is written once in its canonical home and referenced by title elsewhere. This removes the six-appearance duplication without losing any of the six viewpoints.

### 4.8 Archive discipline (applies to 03, 04, and the registers)

Closed, resolved, or retired items move out of active tables at the moment of closure, into the file's Closed/Retired section. Nothing is deleted; the decision trail is preserved. Expected immediate effect: `05` shrinks by roughly 40 percent, `04` by 9 rows, `03` by 3 entries.

### 4.9 Decision log and watch list corrections

Both files need the same delineation treatment as the registers, for the same reason.

**`03` — "Decisions Approaching" holds 34 entries.** A radar with 34 items is a backlog, not a radar. Proposal: split into *Decisions Approaching* (has a named forum and a target date, appears on the radar) and *Decision Backlog* (real but unforumed and undated, reviewed monthly, not surfaced weekly). Per `07_Operating_Cadence.md`, every radar item must have a routing forum; items that cannot be routed are backlog by definition.

**`04` — 48 rows, 9 resolved, 2 empty.** Proposal: retire the 9, delete or populate the 2 carrying no severity, trend, or evidence basis ("WAM benefits realization," "Technical debt / architecture risk" hold no information today). Repair the table fragmentation, where several rows including JCI, WMX Cloud, and WAM/ADM data integrity sit outside the main table. Introduce an explicit **Passive** tier for items logged for completeness that require no attention, so that active-risk count means something.

## 5. What Is Not Changing

- Product tracking and portfolio awareness. Darryl assessed these as working.
- The Copilot intake prompts, other than adding the attribution test.
- The field-notes mechanism and the field-notes-outrank-evidence trust rule.
- The evidence-basis discipline (Direct / Single-source / Repetition / Inferred) in `04`.
- The absence-is-not-non-occurrence rule.
- The Pandoc pipeline.
- The new product workstream.

## 6. Implementation Plan — ACCELERATED (Darryl, 2026-07-27)

Original plan ran Monday to Friday. Compressed at Darryl's direction on 2026-07-27.

| Step | Owner | Status | Output |
|---|---|---|---|
| 1. Framework approved; §8 questions resolved | Darryl | **Done 07-27** | Approved framework |
| 2. Re-sort all 62 open items into Registers A/B/C/D | Claude | **Done 07-27** | `EOS_Register_Sort_2026-07-27.md` |
| 3. Review proposed Register A: confirm, reject, or reassign each item; set dates and triggers | Darryl | **Gate — pending** | Confirmed Register A |
| 4. Restructure `05` into four registers; archive closed rows in `03`, `04`, `05` | Claude | On approval of step 3 | Restructured registers |
| 5. Split `03` into radar and backlog; clean and repair `04` | Claude | Same session as step 4 | Corrected decision log and watch list |
| 6. Update `CLAUDE.md`, `00_README_Operating_Manual.md`, `02_Copilot_Intake_Prompts.md` with the attribution test, focus rule, and daily/weekly split | Claude | Same session as step 4 | Updated operating rules |
| 7. Run the next briefing under the new daily format | Both | Next briefing | Validated format |
| 8. Two-week check-in on Q1 cadence and Register A size | Both | 2026-08-10 | Keep/adjust decision |
| 9. Dashboard redesign | Both | At or after 2026-08-12 | Deferred, see §8.1 |

**Step 3 is the only gate and the only material time cost to Darryl.** Steps 4 through 6 run in a single session immediately on his approval. Everything else is Claude-side.

## 7. Relationship to the 30-Day Pilot

The pilot rule dated 2026-07-16 prohibits deletion, merging, and archival before the 2026-08-12 review. This proposal requires archival and restructuring, so **adoption constitutes Darryl's explicit approval to lift that constraint for the scope defined here.** Nothing is deleted; closed content moves to archive sections within the same files.

The 2026-08-12 review is **not** superseded. The split is deliberate:

- **Now (structural):** what is tracked, how it is attributed, how it is delineated, how it is communicated. Diagnosable from the current files; needs no further pilot data.
- **2026-08-12 (value):** which components earn their place. Is the dashboard read. Which briefing sections are never used. Does the system change decisions. This needs the remaining two weeks of measurement in `10_Pilot_Feedback_Log.md`.

`10_Pilot_Feedback_Log.md` should record this restructure as a mid-pilot intervention, so the 08-12 verdict distinguishes pre- and post-change behaviour.

## 8. Resolved Questions (Darryl, 2026-07-27)

| # | Question | Decision |
|---|---|---|
| Q1 | Register B and C visibility | **Weekly**, piloted. Check in after two weeks (target 2026-08-10) to confirm the cadence still works |
| Q2 | Aging threshold for resurfacing a stalled item | **14 days**, not 21. Applies to the §4.5 focus rule |
| Q3 | Dashboard | Daily snapshot retained for now. **The dashboard itself is not considered correct** and requires redesign after the EOS restructure. See §8.1 |
| Q4 | `03` decision-backlog review cadence | **Monthly**, plus on-demand, plus automatic surfacing when a backlog item is mentioned in a meeting captured in evidence |
| Q5 | Closure checks | **Weekly**, not daily |

### 8.1 Dashboard — deferred redesign

Darryl's assessment, 2026-07-27: the dashboard is too much, carries ill-defined items, and presents too much to focus on to function as a dashboard. This is the same volume-and-definition failure diagnosed in §2, expressed visually.

Treatment: snapshot capture continues so trend history is not broken, but the dashboard is **not** redesigned as part of this week's work. It is a dependent workstream. The registers and watch list must be redefined first, because the dashboard's indicators are derived from them; redesigning the view before fixing the underlying definitions would reproduce the same problem in a new layout.

Sequence: complete §6, run two weeks under the new structure, then redesign the dashboard against definitions that have proven stable. Target: at or shortly after the 2026-08-12 review. Open question for that redesign, recorded now so it is not lost: whether a dashboard is the right instrument at all, or whether the daily briefing's section 5 already does the job.

### 8.2 Amendments arising

- §4.5 focus rule, criterion 3: aging threshold changes from 21 days to **14 days**.
- §9 success criteria: the "re-audit if Register A drifts above 20" trigger stands, measured at the 2026-08-10 two-week check-in.
- Closure checks move from the daily briefing to the weekly briefing. The daily retains same-day chat flags, which are a different mechanism.
- Registers B and C are surfaced in the **weekly** briefing only, in condensed form.

## 9. Success Criteria

The restructure has worked if, within two weeks:

- Register A stays under 15 items without suppressing real obligations.
- Darryl can name the next action without reading past the daily briefing's section 5.
- No item appears in more than one canonical register.
- Zero items enter Register A on inferred attribution.
- Daily briefing returns to roughly one page.

If Register A drifts back above 20, the attribution test is being applied loosely and should be re-audited rather than the register expanded.
