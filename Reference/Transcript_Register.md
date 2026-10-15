# Transcript Register

> **Purpose: make Copilot's access claims falsifiable.** Created 2026-09-14 after two weekly runs on the same day disagreed about which transcripts existed and which could be retrieved (`10_Pilot_Feedback_Log.md`, 2026-09-14).
>
> **Updated 2026-09-14 with Darryl's Teams verification**, taken from `Transcript_Register.docx` in this folder. That pass changed what this register can and cannot prove. Read "What the verification established" before using the rules below; two of the three original rules had to be corrected.

## What the verification established

Darryl recorded the Teams state for all 33 forums, then corrected one entry and changed the setting on the forums he controls. Both corrections are folded in below. The net position is narrower than the first merge suggested, and one rule that was withdrawn has been partly restored.

**Correction 1: `Weekly Sync` was recorded OFF in error. It is ON.** That removes the only observed case of a transcript existing for a series set to OFF, and with it the reason the quote-rejection rule was withdrawn.

**Correction 2: the states recorded for forums Darryl controls are post-change, set 2026-09-14, not the state during the 09-07 to 09-14 reporting window.** This resolves the `Wesco / SkyFoundry` conflict. The series is ON now; it was not ON on 2026-09-09, which is why the re-run correctly reported `isMeetingTranscribed:false` for that occurrence.

**Consequence for the 09-14 package: run 1's two Wesco/SkyFoundry action items are confirmed manufactured.** No transcript existed for that meeting during the window, so the Explicit-confidence quotes had no source. Both stay at Inferred in `Evidence/M365_Evidence_Weekly_2026-09-14_ACCEPTED.md`. This is settled and does not need revisiting.

**`WAM Data Challenges` is also resolved.** Confirmed 2026-09-14: it was switched on that day, so it was off during the window. The recording-with-no-transcript artifact is explained and there is no defect to chase.

**What remains genuinely unresolved: one row.**

| Forum | Teams state | Copilot evidence | Open question |
|---|---|---|---|
| `2026 Deployment — Daily Scrum` | ON (as-found, Chad Steger's series, not Darryl's to change) | Retrieved 0–286 of 286, but not transcribed 09-08, 09-09, 09-10 | ON at series level with three occurrences still missing. Most likely depends on who starts the occurrence. One question for Chad. |

## Rules, restored and qualified

| Situation | Rule |
|---|---|
| Coverage Gap on an ON forum | **Failed run. Re-run it.** Unchanged, and now the strongest trigger in the register. |
| Coverage Gap on an OFF forum | **Almost certainly a correct "Not transcribed at source" entry.** An operating signal, not a retrieval failure. |
| A quote attributed to an OFF forum | **Treat as a manufactured source and reject the row.** Restored after the `Weekly Sync` correction, with one qualification: transcription can still be started by hand inside a meeting whose series is OFF, so this is a strong presumption rather than proof. Confirm against the occurrence before acting on anything consequential. |

**The check that does not depend on this register at all, and the one to lean on:** does the row's source appear in that run's own Retrieval and Source-Status Statement as a transcript actually retrieved? A row quoting a meeting the same package never reports retrieving is manufactured whatever the register says. That is acceptance-gate check 1 and it is self-contained.

**How the remaining uncertainty gets settled: by the next package, not by more inspection.** Every forum now ON should produce a retrievable transcript in the 2026-09-21 weekly. Any that does not is a live defect with a named owner. That run is the verification, and it costs nothing extra.

## How to read the evidence column

| Value | Meaning |
|---|---|
| **Transcript retrieved** | A package retrieved the transcript to its stated total. |
| **Not transcribed** | A package reported `isMeetingTranscribed:false` for that occurrence. |
| **Varies by occurrence** | Both of the above observed for the same series. |
| **Truncated, continuation failed** | Transcript exists; retrieval did not complete. A retrieval problem, not a transcription problem. |
| **No evidence** | The forum has not appeared in any package with a transcript status. |

Teams state values as recorded: **ON**, **OFF**, **MIXED**, **NA**. NA currently carries two different meanings, "not applicable to this forum" and "not mine to inspect," and should be split at the next review.

## Core product, delivery, and governance

| Forum | Cadence | Owner | Who can switch it on | Copilot evidence to date | Teams state | Verified on | Priority |
|---|---|---|---|---|---|---|---|
| WAM Product Leadership Sync | Weekly | David Blondel | David Blondel | Not transcribed (08-25 diagnostic). Transcription ON imposed 2026-09-01 under the agenda standard; no occurrence evidenced since | **MIXED** | | Confirm the 09-01 change took effect |
| ADM connect with Natalie | Weekly | Akansh Gangil | Akansh Gangil | No evidence | ON | | High — where WAM data-foundation defects surface |
| WAM Product discussion | Weekly | Akansh Gangil | Akansh Gangil | No evidence | ON | | Medium |
| WAM Data Challenges (Problem Definition) | Weekly | **Darryl Benson** | **Darryl** | Recording artifact only, 0 usable transcript lines (09-14 re-run) | ON (set 2026-09-14) | 2026-09-14 | Resolved. Was off during the window, which explains the recording-only artifact. Expect a transcript at the next session |
| DDP Entrance Call | Weekly (Mon) | Anna Baker | Anna Baker | Transcript exists; truncated, continuation failed (08-25, 0–435 of 574) | NA | | Low — mostly out of scope, but a transcript demonstrably exists, so NA is not accurate here |
| WAM Product Backlog Refinement | Bi-weekly | Sakshi Mathur | Sakshi Mathur | Transcript retrieved 0–699 of 699 (09-14 re-run) | ON | | Confirmed working |
| WAM India Dev Team weekly | Weekly | TBC | TBC | No evidence | OFF | | Medium |
| WAM Sprint Review | Bi-weekly | Sakshi Mathur | Sakshi Mathur | No evidence | ON | | Low |
| Daily Stand Up (entroCIM) | Daily | Ron Snyder | Ron Snyder | Transcript retrieved 0–355 of 355 (09-14 re-run) | ON | | Confirmed working |
| 2026 Deployment — Daily Scrum | Daily | Chad Steger | Chad Steger | Varies by occurrence. Retrieved 0–286 of 286; not transcribed 09-08, 09-09 (re-run), 09-09, 09-10 (run 1) | ON (as-found) | 2026-09-14 | **The one unresolved conflict. Ask Chad how occurrences are started** |
| entroCIM Backlog Deep Dive | Bi-weekly | David Blondel | David Blondel | Transcript retrieved 0–815 of 815 (09-14 re-run). Run 1 wrongly reported this one as truncated | ON | | Confirmed working |
| entroCIM Leadership Collaboration | Weekly | Ron Snyder | Ron Snyder | Not transcribed (08-25 diagnostic). Transcription ON imposed 2026-09-01 under the agenda standard; only a channel message evidenced since | NA | | **The 09-01 agenda-standard commitment remains unverified** |
| Quest Migration Weekly Check-In | Weekly | Chad Steger | Chad Steger | Not transcribed (08-25 diagnostic; 09-14 run 1; 09-14 re-run, 09-08). Consistently off across three weeks | NA | | High — one request to Chad; migration governance is running blind |
| Showcase recurring | Bi-weekly | David Blondel | David Blondel | No evidence | ON | | Low |
| Deployment Team Knowledge Share | Periodic | TBC | TBC | No evidence | ON | | Low |
| DCOE & entroCIM Weekly | Weekly | Balachandar Murali | Balachandar Murali | No evidence | OFF | | Low |
| CSS Platforms All Hands | Periodic | Leadership | Darryl / leadership | No evidence. Decision-rich forum | ON | | High — ON but never evidenced; expect a transcript at the next session |
| Digital Products Portfolio Review | Periodic | Sean McCloskey / Chris Gazdic | Meeting owner | No evidence | NA | | Medium |
| Dell Service Management Process | TBC | Syed Jamshed Zaidi / Chad Steger | Meeting owner | No evidence | NA | | Medium — customer-facing |
| Dell Program Delivery Alignment | New | TBC | Meeting owner | No evidence | NA | | Medium — customer-facing |
| Wesco Asset Manager Backlog Deep Dive | Bi-weekly | TBC | Meeting owner | No evidence | ON | | Medium |
| EntroCIM Project Closeout Process Review | Unconfirmed | TBC | Meeting owner | No evidence | NA | | Low |

## 1:1 and leadership alignment

| Forum | Cadence | Owner | Who can switch it on | Copilot evidence to date | Teams state | Verified on | Priority |
|---|---|---|---|---|---|---|---|
| Darryl / Nate Weekly 1:1 | Weekly | Nathan Kehr | Nathan Kehr | No evidence | OFF | | Medium |
| Darryl – Ron 1:1 | Weekly | **Darryl** | **Darryl** | Not transcribed, 09-08 (09-14 re-run) | OFF | | **High — Darryl-owned, consistent with evidence, one setting away** |
| Darryl – Chad 1:1 | Weekly | **Darryl** | **Darryl** | No evidence | OFF | | **High — Darryl-owned** |
| Weekly Sync (Amy Aguirre) | Weekly | **Darryl** | **Darryl** | Transcript retrieved 0–308 of 308 (09-14 re-run). Run 1 wrongly reported this one as truncated | ON | 2026-09-14 | Confirmed working. Recorded OFF in error on the first pass and corrected same day |
| Digital Products / Agile Staff Meeting | Weekly | Chris Gazdic | Chris Gazdic | Transcript retrieved 0–497 of 497 (09-14 re-run) | ON | | Confirmed working |
| Product Team – Platform Team connect | Weekly | Keyur Patel | Keyur Patel | No evidence | NA | | Low |

## Commercial, finance, customer, external

| Forum | Cadence | Owner | Who can switch it on | Copilot evidence to date | Teams state | Verified on | Priority |
|---|---|---|---|---|---|---|---|
| entroCIM Sales Ops/Finance Sync | Twice-monthly | Tom Boss | Tom Boss | No evidence | NA | | Medium |
| WAM / External BIR: 2517699 Actuals | Monthly | John Erickson | John Erickson | No evidence | NA | | Medium |
| Wesco / SkyFoundry | Monthly | **Darryl** | **Darryl** | Not transcribed, 09-09 (09-14 re-run). Run 1 reported it as a truncated transcript and quoted two action items from it; no transcript existed | ON (set 2026-09-14) | 2026-09-14 | Resolved. Was OFF during the window, switched on 09-14. Expect a transcript at the next session |
| BAE/Wesco Weekly | Weekly | Kevin Cochran | Kevin Cochran | No evidence | OFF | | Medium — external customer, and OFF means no durable record |
| Smart Buildings Issues Log Catch-Up | Bi-weekly | Raj Ramroop | Raj Ramroop | No evidence | OFF | | Low |

## Ad hoc and customer meetings seen in evidence

Not recurring forums, so not series-configurable, but recorded because they carried material content.

| Meeting | Date seen | Copilot evidence | Note |
|---|---|---|---|
| FRBNY CSC: Smart Building Descope | 2026-09-08 | Not transcribed | The FRB thread is carried in the accepted 09-14 package from run 1 only. With no transcript, recovery depends entirely on email and chat |
| PASS-06 Server Migration Cutover | 2026-08 | Not transcribed (08-25 diagnostic) | Darryl's own organisation |
| Differentiation exercise | 2026-08 | Truncated, 0–583 of 952, continuation failed | Transcript exists |
| Claude Code Model Upgrades - VAS, Assortment, QPM | 2026-09 | Out of scope | Optional-attendee forum |

## Action queue, after correction

1. **`2026 Deployment — Daily Scrum`** — the only unresolved conflict. ON at series level, three occurrences with no transcript, and Chad Steger's to explain. Pair it with `Quest Migration Weekly Check-In`, which is still off, in one conversation.
2. **`entroCIM Leadership Collaboration` and `WAM Product Leadership Sync`** — recorded NA and MIXED. The 2026-09-01 agenda standard specified transcription on for both, and neither has produced a transcript since. Worth confirming with Ron Snyder and David Blondel that the change took effect.
3. **The two 1:1s are a judgment call, not an oversight.** `Darryl – Ron 1:1` and `Darryl – Chad 1:1` remain OFF. A 1:1 is where personal and sensitive material surfaces, and the 09-14 package already shows a named individual's health situation reaching a standing team file from a chat. Transcribing 1:1s puts that class of content into a durable, searchable artifact. Leaving them OFF is defensible; if they stay OFF, the register should say so deliberately rather than carry them as an open action.
4. **`BAE/Wesco Weekly`** — OFF on an external customer cadence. A deliberate decision is worth making rather than defaulting.
5. **Split NA** into "not applicable" and "cannot inspect" at the next review.
6. **Verify by running, not by checking.** The 2026-09-21 weekly is the test: every forum now ON should return a transcript. Any that does not becomes a named defect.

## Source and sync

Darryl's verification was recorded in `Transcript_Register.docx` in this folder and merged here on 2026-09-14, then corrected the same day: `Weekly Sync` was recorded OFF in error and is ON, and the states for forums Darryl controls are post-change rather than as-found. This markdown file is canonical; the Word file is the fill-in surface. Pre-verification copy of this file is archived outside the folder. When the Word file is updated again, hand it over and it will be merged the same way rather than maintained in parallel.
