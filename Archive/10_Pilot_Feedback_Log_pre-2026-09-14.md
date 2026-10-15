# Pilot Feedback Log

> Added 2026-07-16 per external review of the EOS. Tracked the 30-day operating pilot, review scheduled for 2026-08-12.
>
> **Closed 2026-08-06, six days early.** Darryl's own value assessment (`EOS_Value_and_Purpose_Review_2026-08-06.md`) answered the questions this file was tracking toward — is the dashboard read, which sections earn their place, does the system change decisions — with a sharper diagnosis than volume/noise alone. No second review needed on the same question at 08-12. This file is retained as the historical record of the pilot; new value/usage questions are tracked in the review doc going forward.

## How to Read This File

Each dated entry captures: time cost, what the system caught that Darryl would have missed, decisions/commitments/risks it helped move, and where it was wrong, silent, or noise. At 2026-08-12, patterns here (not architectural preference) decide what stays, changes, or goes.

## Time Cost

| Date | Evidence intake (min) | Review/correction (min) | Notes |
|---|---|---|---|
| 2026-07-16 | — | — | Pilot instituted mid-day; baseline starts next full cycle |
| 2026-07-24 | — | — | Session also added a new recurring briefing section (Key Product Due Dates) at Darryl's request — first cycle carrying it |
| 2026-07-27 | — | — | First true **weekly** evidence package processed (7-day lookback vs. prior daily 24-hour pulls); briefing carried the Weekly Analytics Block for the first time (Section 16, per `Reference/EOS_Analytics_Standard.md`) |
| 2026-08-03 | — | — | Second full weekly cycle; first cycle where the Dashboard snapshot gap (07-28–07-31, no daily capture) became visible in the trend series — flagged in the dashboard footer rather than silently interpolated |

## Value Signals

| Date | Item surfaced Darryl would've missed | Decision improved/accelerated | Commitment recovered | Risk caught early |
|---|---|---|---|---|
| 2026-07-21 | A direct Darryl-run status sweep across all 26 open commitments (via uploaded spreadsheet) closed 9 items and merged 1 pair in a single pass — far more throughput than the evidence-driven cycle alone produces | Confirmed the WMX follow-up (Wed 07-22) and the newly-set Brian Miller JCI meeting (also Wed 07-22) collide on the calendar — caught before either was missed | Strev invoice payment, Dell Limerick resolution, CSM pilot access, CODA talking points, Shorenstein response (all recovered/confirmed same session) | Strev vendor-relationship strain flagged as a pattern worth a standing check, not just a one-off invoice fix |
| 2026-07-24 | TCCC/Coca-Cola Airwall offline for a second day, with no confirmed ticket or customer engagement — not visible from living-doc review alone | JCI markup date sharpened from "next week" to a specific 2026-07-31, converting a soft commitment into a trackable one | None this cycle | TCCC outage caught on day 2 rather than surfacing only when it became a third/fourth consecutive silent day, matching the pattern the entroCIM-release silence taught earlier in the pilot |
| 2026-07-27 | QPM 3.4.3's "significantly behind" status and the Dell/Wesco support-process gap (with its own new forum) — neither visible from living-doc review, both material to a customer go-live and a recurring escalation pattern | Dell Service Management Process forum use case sharpened by naming the two concrete process misses (Limerick, Non-DC) to bring to today's first session | None this cycle | The TCCC/Coca-Cola silence itself became the catch — the weekly package's total absence of any TCCC reference, four cycles running, was flagged as a risk in its own right rather than read as resolution |
| 2026-08-03 | An unowned Freshdesk support-mailbox failure (support.ec@wesco.com, 2 days of tickets) — not visible from living-doc review, sits underneath every customer support response the team sends | FY27 AOP sharpened from a soft planning-cycle thread to a mandatory, dated, dual-product deliverable (A19, due 08-21) | None this cycle | TCCC's hardware-installation question (C12) confirmed open a second consecutive week despite being named the likely-dispositive fact in the 07-28 session — worth forcing this week rather than reissuing a third time |

## Failure Signals

| Date | Weak/incorrect inference | Missing evidence instance | Section consistently skipped | File updated but unused | Duplicate info across files |
|---|---|---|---|---|---|
| 2026-07-21 | Shorenstein/Sarah Monteleone response was carried as "open, overdue" across the 07-20 and 07-21 morning briefings; Darryl confirmed it was actually resolved 2026-07-17. Two consecutive Copilot evidence packages missed a closed item rather than surfacing it — an evidence-recency gap, not a wrong inference, but it produced a false overdue read for 4 days | Same instance: entroCIM Jul 20 release outcome still absent from evidence as of 07-21 (2nd consecutive day) | None flagged yet | None flagged yet | None flagged yet |
| 2026-07-22 | — | — | entroCIM Jul 20 release outcome — now a 3rd consecutive day absent; 07-22 evidence offered a plausible cause (DCOE compliance hold) rather than continuing as pure silence, worth testing directly rather than waiting for a 4th cycle | None flagged yet | None flagged yet |
| 2026-07-28 | **Material misread from a Copilot summary.** The evidence package rendered the TCCC/AOC item as "Coca-Cola engineering requested disabling remaining entroCIM connectivity due to observed network improvements," which Claude filed as a customer-perception risk and a probable Contradiction against the 07-27 closed Airwall item. The actual email thread (supplied by Darryl) showed something different: a two-stage escalation running 07-22 to 07-27, a documented year-old history of overloaded network segments worked with ALC, and several connectors already disabled pending hardware upgrades. Root cause is a controller capacity limit with a direct FRB Distech precedent. **The summary was not wrong in its facts; it was too thin to support the conclusion drawn from it.** Lesson: for customer escalations, the Copilot row is a pointer to a thread, not a substitute for it — request the source thread before writing a position into 03/04 | Same instance: the evidence package carried none of the thread's prior history (ALC engagement, disabled connectors, pending hardware), all of which was sitting in Scott Dunn's own reply | None flagged | None flagged | The 07-28 briefing and the first 03/04 entries both framed this as a reopen/perception issue. Corrected same day in 03, 04, and 06 |

## Meeting Load Changes

| Date | Meeting delegated / eliminated / improved | Trigger |
|---|---|---|
| | | |

## Daily System Feedback Rollup

*(Pulled from briefing section 14 — useful insight / weak inference / missing evidence / section not useful / record needing correction. One line per briefing.)*

| Date | Useful insight | Weak inference | Missing evidence | Section not useful | Record needing correction |
|---|---|---|---|---|---|
| 2026-07-21 | Surfaced a real capacity collision (Dell Limerick landing on the same two names as BAE/FRBNY) not visible from living-doc review alone | None beyond standard unconfirmed-name caution (Strev "operational" claim flagged, not treated as fact) | entroCIM Jul 20 release outcome — second consecutive day absent | None flagged | None this cycle |
| 2026-07-22 | Evidence offered a plausible cause (DCOE compliance hold) for the entroCIM release silence, turning a pure evidence gap into a testable hypothesis | None identified beyond standard unconfirmed-name caution | entroCIM Jul 20 release outcome (3rd consecutive day); Quest Migration Weekly Check-In produced no transcript ("migration completion" is inferred, not confirmed) | None flagged | None this cycle |
| 2026-07-24 | Evidence surfaced a live, unconfirmed customer outage (TCCC) and a concrete JCI date (07-31) sharpening prior "next week" language | None significant beyond standard unconfirmed-role caution (Maggie Becker, Kiranmai) | NexusCon and QPM 3.4.3/Charlotte dates remain unevidenced; several 07-23 meetings were recap-only, not transcribed | None flagged | None this cycle |
| 2026-07-27 | QPM 3.4.3 escalation and the new Dell service-management forum both caught early; the TCCC silence itself flagged as the sharpest single item this cycle | "Anna Baker" QPM 3.4.3 attribution flagged as probable-not-confirmed given a role-domain mismatch with her tracked DDP/MDM scope | TCCC/Coca-Cola Airwall — total absence across the full 7-day weekly package, 4th consecutive cycle; QPM 3.4.3 report-out call date; NexusCon dates | None flagged | None this cycle |
| 2026-07-28 | The session's value came from the working exchange rather than the briefing: Claude's challenge to the Airwall-report approach (wrong vantage point, and volume evidence against a concurrency failure) was adopted, and the "was the scoped hardware ever installed" question was pulled out of Scott Dunn's own email as the likely dispositive test | Initial read of the TCCC item as a customer-perception/reopen risk, drawn from a Copilot summary rather than the source thread — see Failure Signals | The Copilot package omitted the thread's prior ALC history entirely; also carried no TCCC dates beyond the current exchange | None flagged | 03/04/06 TCCC entries rewritten same day once the thread and Darryl's technical context arrived |
| | | | | | |

## Closure Confirmations (new rule, 2026-07-16)

Items moved from `Potentially closed — confirmation required` to final closure, with the confirming source.

| Date | Item | Confirmed by | Source |
|---|---|---|---|
| 2026-07-16 | Zscaler / WAM access resolution (05, commitments) | Darryl (explicit, chat) | Retroactive confirmation under new closure-discipline rule |
| 2026-07-21 | Strev invoice INV-2606-00014 (ACH payment made 07-20) | Darryl (explicit, via Natalie Marquardt) | Commitment status update, 07-21 |
| 2026-07-21 | Shorenstein Nashville Moore Building response (actually closed 07-17) | Darryl (explicit) | Commitment status update, 07-21 |
| 2026-07-21 | JCI blocker re-engagement (Gutierrez/McCorvey) | Darryl (explicit) | Commitment status update, 07-21 |
| 2026-07-21 | Invite Sunny Sharma to WAM meeting (deleted, no longer necessary) | Darryl (explicit) | Commitment status update, 07-21 |
| 2026-07-21 | DDP Entrance Call attendance (folded into standing cadence) | Darryl (explicit) | Commitment status update, 07-21 |
| 2026-07-21 | FRB SASTEC support follow-through (transferred to ops team) | Darryl (explicit) | Commitment status update, 07-21 |
| 2026-07-21 | Digital Products Portfolio Review duplicate-invite cleanup (not Darryl's to track) | Darryl (explicit) | Chat, 07-21 |
| 2026-07-21 (marked provisional) | Dell Limerick alarming issue | Darryl (explicit, quoting ticket) — provisional, monitoring continues | Commitment status update, 07-21 |
| 2026-07-21 | Technical CSM pilot hosted-environment access tickets | Darryl (explicit) | Commitment status update, 07-21 |
| 2026-07-21 | CODA talking points for Natalia Shtern | Darryl (explicit) | Commitment status update, 07-21 |

## First Run of the Revised Intake — 2026-07-27 PM

The revised Copilot prompts and the four-register model were used together for the first time on the 24-hour package of 2026-07-27.

**Attribution result:** 5 action items extracted, **0 attributed to Darryl as owner**. One item (Coda renewal signature confirmation) came back as *Implied* naming both Nathan Kehr and Darryl, and was raised as a confirmation question rather than written into Register A. Owners Copilot named instead: Revanth Jampana (Explicit), BI_Wesco_Integration_Support_L2 (Implied), Sarah Monteleone (Explicit), one "Owner unclear." Under the previous prompt wording ("Commitments I Made"), several of these would very likely have arrived as Darryl's. **Register A unchanged at 10 after a full evidence cycle.**

**Closure-signal result:** the new section returned two closure signals on first use (PaaS-02 SAML validation ticket closed by Babu Papanna; SSO user-group propagation partial). Neither was previously visible to the intake. This is the section added to address the four-day Shorenstein false-overdue.

**Disposed-item filter, first use:** 4 matches against the 33-item disposal list. Classified 1 Contradiction (entroCIM release — deployment evidence postdating an "approved and complete" closure), 1 Echo (PaaS-02 SSO — confirmatory, suppressed and reported), 1 Resemblance (EUDM sales-order gap resembling the retired supplier-data row but distinct), 1 clean (TCCC, no contradicting evidence). **The Contradiction case earned its place immediately:** the record had conflated "approved" with "deployed," and a blanket filter would have hidden that.

**Failure signal:** no meeting transcripts were retrievable at all this cycle. Today's Dell Service Management Process session (Register A10) and the DDP Backlog Entrance Call produced no evidence whatsoever, so A10's outcome cannot be confirmed. Recurring pattern — transcript availability is now the single largest evidence gap in the system, noted on 07-24 and 07-27 as well.

**Value signal:** the package surfaced a probable root-cause link between the new EUDM sales-order gap (INC5456198) and bug 7827, which is currently carried as a defect inside the Aug 3 MVP1 gate. If confirmed, a release defect is actually a data-pipeline failure with a different owner, 7 days before go-live. Not visible from living-document review.

## Mid-Pilot Intervention — 2026-07-27

**Darryl accelerated the structural half of the review.** Record this when reading the 08-12 data: behaviour before and after 2026-07-27 is not comparable, because the system changed underneath the measurement.

**Trigger (Darryl, 07-27):** commitments were being misinterpreted and overstated, diluting focus rather than sharpening it, with less clarity on what was next. Product tracking and general awareness assessed as working.

**Diagnosis (measured, not inferred):**

| Finding | Value |
|---|---|
| Items filed as Darryl's commitments | 39, of which 10 were actually his |
| Items whose owner was someone else | 6 (a table headed "Commitment owed to Darryl" was nested inside "Commitments Darryl Made") |
| Items generated by one 07-23 meeting | 7 (18% of apparent load) |
| Standing role duties with no completion state | 4 |
| Undated items | 30 of 39 |
| Closed rows still inline in active tables | 25 in `05`, 9 in `04`, 3 in `03` |
| Briefing growth 07-13 to 07-27 | 7.9 KB to 25.5 KB, while `00_README` instructed reading 4 of 16 sections |
| Duplicate appearances of QPM 3.4.3 in one briefing | 6 |

**Root causes:** no attribution test at intake; schema encoded the ambiguity ("Expected By" held a counterparty, no Owner column); no single home per fact.

**Changes made:** four-register model; strict attribution test; 14-day aging threshold; daily/weekly briefing split; closure checks weekly; `04` Active/Passive/Retired tiers (48 rows to 27 active); `03` split into a 24-item Radar and a 6-item Backlog; Register D moved to `07`. Snapshots in `Archive/`.

**Result:** Register A at 10, all dated or triggered. Register B 12, Register C 10. 13 items dropped by Darryl, 9 closed.

**What this does to the 08-12 verdict:** the structural questions (what is tracked, how it is attributed, how it is communicated) are now answered and should not be re-litigated. The remaining questions are value questions: is the dashboard read, which briefing sections earn their place, does the system change decisions, and does the smaller register hold or drift back up.

### Failure signal captured by this intervention

The system had been patching its own attribution problem in prose rather than structurally. The 07-22 entry on the AI-analysis commitment carried the note "same underlying deliverable, don't double-count" — an acknowledgment that duplication existed, written as a caveat instead of fixed in the schema. Worth watching for this pattern generally: a caveat repeated across cycles is a design defect, not a disclosure.

## 2026-08-12 Review Checklist

- [ ] Time cost trend across the pilot (intake + review)
- [ ] Count of items surfaced Darryl would've missed
- [ ] Count of decisions improved/accelerated, commitments recovered, risks caught early
- [ ] Count and pattern of weak inferences and missing-evidence instances
- [ ] Briefing sections flagged "not useful" 3+ times → propose cut
- [ ] Files touched but never referenced in a session → propose archive
- [ ] Duplicate information found across files → propose canonical source
- [ ] Dashboard tiles that ever just restated a briefing line
- [ ] Net verdict per component: keep / modify / merge / cut
