# WAM Value Proposition Feasibility Review: Cowork Master Prompt

**Created:** 2026-09-09
**Purpose:** run an evidence-based feasibility assessment of the WAM value propositions against ADM's actual ability to obtain the underlying data, ahead of the first WAM program update to Sean McCloskey.
**Position in the sequence:** this is the evidence work that makes slides 1 through 5 of `Deliverables/WAM/2026-09-02_Sean_Deck_Brief.md` defensible. Run this before the working session with David Blondel and Akansh Gangil, and before the deck is drafted.
**Written to be picked up cold.** Assume no memory of prior sessions.

---

## 1. Context

WAM is sold on a set of value propositions drafted on 2026-07-16 and extended on 2026-08-26. Those propositions promise the customer and the business visibility and action across assets, serial numbers and metadata, licenses, warranties, entitlements and renewals. Every one of them depends on ADM being able to acquire, normalize and maintain the underlying data.

The propositions have never been tested against what ADM can actually get. That test is the subject of this session.

Sean McCloskey is a VP. This is the first WAM program update he has received, and he re-shares upward to Dirk and Engel, where WAM benefits underreporting has already left a negative impression (`06_Stakeholder_Map.md`). What he asked for, reported verbally on 2026-09-01 and not transcribed, was usable license data in the system and how serial numbers and other metadata are provided for the business. The feasibility question is therefore the update, not background to it.

**The governing judgment to test, not to assume:** WAM's limiting factors sit outside the development team. They are enterprise data, master data, supplier participation, and process ownership across WMX, VAS, GPO, MDM, DDP and EUDM. Five constraint holders are named in the record and four of them are outside Darryl's organization. If the analysis supports that conclusion it becomes the spine of the update; if the evidence does not support it, say so.

**A framing correction that must survive into this work.** Current WAM revenue is earned through supply chain programs, not through the license capability, corroborated independently by the FY27 gross margin of 15.2%, which is a distribution margin rather than a software margin. Do not use 2026 attainment ($16.7M year to date, 87% attainment through June) as evidence that any license or asset value proposition is converting.

---

## 2. Task

Produce a feasibility assessment that decomposes each WAM value proposition into the data it requires, identifies the authoritative source for that data, states what exists today with an evidence tier, names who holds the constraint, and returns a feasibility verdict.

Then produce a revised value proposition set in which every claim is scoped to what the data can currently support, with the aspirational portion moved into a clearly separated forward statement.

Then produce the gap list and the working session agenda needed to close what the record cannot answer.

---

## 3. Goal

Sean must leave the review able to answer three questions without Darryl in the room:

1. Which parts of the WAM value proposition are real today, and on what evidence.
2. Which parts are gated, what specifically gates them, and who holds each gate.
3. What decision or support only he can provide.

The output is not a status report. Shipped features, sprint completion, release milestones and ticket counts do not clear the threshold in `Reference/Sean_Update_Standard.md`, because delivery competence is assumed and reporting it implies it was in doubt.

---

## 4. Source Material

Read in this order. The Executive Operating System is the master record; where a source conflicts with it, say so rather than silently choosing.

**Canonical product context**
- `Products/WAM/WAM.md` (value propositions are in the sections "What It Is / Value Proposition" and "Value Propositions (drafted 2026-07-16, Cowork session)"; weekly evidence sections carry the current state)
- `Products/WAM/WAM_Data_Architecture.md` (data domains, systems table, the 2026-08-19 confirmed complex-build architecture, failure modes in section 10)
- `Products/WAM/Part_Classification.md`
- `Products/WAM/WAM_Roadmap.md`
- `Products/WAM/Strev_2027_Priorities.md`

**The Sean thread**
- `Deliverables/WAM/2026-09-01_Sean_WAM_Program_Update_Prep.md` (two-track structure, constraint holders, the three defects, the information requests already sent)
- `Deliverables/WAM/2026-09-02_Sean_Deck_Brief.md` (the nine-slide storyline this work feeds)
- `Reference/Sean_Update_Standard.md` (scope and threshold; apply the filter before drafting, not after)

**Asset, serial and complex-build evidence**
- `Deliverables/WAM/2026-08-19_Complex_Build_Asset_Flow_v4.md`
- `Deliverables/WAM/2026-07-14_Asset_Tracking_Data_Flow.md`
- `Deliverables/WAM/Part_Taxonomy_ADM_Requirements_v2.0.md`
- `Deliverables/WAM/Part_Taxonomy_UseCase_Brief_and_Data_Model.md`

**Live registers, for current status rather than history**
- `03_Decision_Log.md`, `04_Executive_Watch_List.md`, `05_Commitments.md`, `09_Impact_Ledger.md`
- Latest weekly briefing in `Briefings/`

**Standards**
- `Reference/Benefits_Realization_Standards.md` (realized versus planned discipline is mandatory)
- `Reference/Communication_Preferences.md` (voice; no em dashes; title names the page, headline says the thing)
- `Reference/Mermaid_Standards.md` if any diagram is produced

---

## 5. Value Propositions Under Test

Test all seven. Do not reword them before testing them; the point is to find out which ones survive contact with the data.

**Customer-facing**
1. One place to see everything you own: hardware, software licenses, warranties, and lifecycle status across the install base.
2. No more surprise expirations: proactive alerts on renewals, warranty and support expirations.
3. Faster, cleaner onboarding: asset and license data normalized and structured, cutting manual reconciliation the customer absorbs today.

**Internal commercial**
4. Governed triggers, not manual digging: renewal, warranty and refresh signals pushed to Sales and Sales Ops from the data.
5. Install-base intelligence for account conversations: visibility into what a customer already owns.
6. Already producing pipeline, not just promised: the first sales-notification release, 60-day expiration alerts, live since July.

**Added 2026-08-26, and absent from every prior value statement**
7. Complex builds stay visible and serviceable: WAM carries the configured multi-component systems Wesco assembles and serializes into the customer install base record.

---

## 6. Required Analysis

### 6.1 Decompose each proposition into its data dependencies

For every proposition, identify the specific data required, not the data domain in general. "Asset data" is not an answer; "serial number captured at shipment, associated to the parent finished good, with MAC address and asset tag, landed in DDP and readable by ADM" is.

Cover these five capture domains explicitly, because they are what Sean asked about:

- **Assets and install base records:** what constitutes an asset record, what ADM can ingest today, and from where.
- **Serial numbers:** simple products versus complex builds, capture point, propagation path, and enforcement.
- **Metadata and attribute capture:** MAC address, asset tag, parent and child relationship, room or location, product class, warranty term, license term, clean description.
- **Licenses:** identification of license and software part numbers in master data, license term, description quality, activation, and end-user assignment.
- **Sales renewals:** the notification trigger, its data preconditions, attribution logic, and the difference between a signal fired and a renewal earned.

### 6.2 Fill the row for each dependency

| Column | What it holds |
|---|---|
| Value proposition | Which of the seven, by number |
| Data required | The specific field or structure, not the domain |
| Authoritative source | The system or team of record. DDP/EUDM is the single source of truth for asset data and the only route into ADM; ACT is a contingency path only |
| State today | What actually exists, stated as a fact with a date |
| Evidence tier | Confirmed (transcript, document, or direct statement), Stated (reported, not verified), Inferred, or Assumed. Never present an assumption as a fact |
| Gate | What specifically prevents completeness |
| Gate holder | Named person and organization |
| Feasibility verdict | Supportable now, Conditional, or Not supportable (see 6.4) |
| What would change the verdict | The specific evidence, decision, or commitment required |

### 6.3 Capture the enrichment capability built for the Microsoft AV requirement

This is the newest capability in the record and it belongs in the assessment. Reported by Darryl, and the surrounding detail is to be confirmed with Akansh Gangil before it is presented.

What the record holds: a WAM data-enrichment MVP was scoped and prioritized ahead of the asset-upload epic, by Akansh Gangil with Violet Moyer's agreement, decided 2026-09-01 and confirmed in the 2026-09-03 backlog refinement. It accepts sales order, Wesco part number and manufacturer part number, and returns shipping fields and transaction price with not-found statuses. Average-price logic was deferred until requirements are clearer. The asset-upload epic was deprioritized to make room for it, with supplier ID work continuing in parallel.

What the record does not hold, and what this session must capture: that the driver for this capability is Violet Moyer's Microsoft AV data-gathering requirement. Treat that as Darryl-reported, to be confirmed with Akansh Gangil and Violet Moyer.

Then answer these, since they are what makes the capability matter to the assessment rather than a feature note:

- Which value proposition does the enrichment MVP actually advance, and does it advance the customer-facing propositions or only an internal program need.
- Whether it is a Microsoft AV program-specific capability or a general ADM enrichment service that a specific program funded first. This distinction decides whether it is evidence of a repeatable capability or of a one-off.
- Whether the deprioritized asset-upload epic was on the critical path for propositions 1, 3 or 7, and what the deferral costs those propositions in time.
- What data the Microsoft AV program requires beyond shipping fields and transaction price, and whether ADM can obtain it.
- Whether this is evidence for or against the governing judgment in section 1. A capability delivered inside two weeks against a business requirement is evidence the development team is not the constraint.

### 6.4 Apply the verdict rubric consistently

- **Supportable now.** The data exists at sufficient completeness, from a named source, and ADM can consume it today. State the completeness figure or state that no figure exists, in which case the verdict cannot be Supportable now.
- **Conditional.** The path exists but is gated by a named dependency with a named holder. State the gate and the holder.
- **Not supportable.** No source, no path, or a defect that removes confidence in the data. State which.

A verdict of Supportable now without a completeness number is not permitted. If the number is missing, the verdict is Conditional and the missing number goes on the gap list.

### 6.5 Carry the three completeness defects into the analysis rather than a footnote

Truncated manufacturer part numbers with no named fix owner since late August; sample orders absent from EUDM requiring NetSuite hydration; Core ERP sales orders missing from the EUDM table under INC5456198. Carried as W1, W2 and W3 on the WAM Product Leadership Sync register.

For each, state which value propositions it undermines and by how much. These are the concrete evidence for the cross-functional support Darryl needs, so they belong in front of Sean rather than being found later. Do not present them as an admission of delivery failure.

### 6.6 Verify the constraint holder table

The prep file names five constraint holders, four outside Darryl's organization: John Barlolotti as GPO for WMX with Sid Sarna as solution architect; Daniel Totino and the EUDM team; MDM with Inder Gambhir and Gandhi Subramanian; Jarod Booth's organization for supplier attribute data via David Blondel; and Natalie Marquardt for supplier data collection in practice, flagged as a single point of dependency.

Confirm each against the current registers, correct anything stale, and map each holder to the specific value propositions their gate blocks. A constraint holder who blocks nothing on the list should be removed; a gate with no named holder is itself the finding.

### 6.7 Reconcile the known conflicts rather than choosing silently

- WMX complex-build attribute capability: `WAM_Data_Architecture.md` section 0 records no capability and no roadmap until 2028, while later evidence expects WMX 5.7 to add MAC address and asset tag fields. Either the earlier statement refers to full parent-child support or it is out of date. Flag it; do not resolve it by assertion.
- The 2026-09-01 decision (WMX for standard serial collection, VAS governance for project-specific and ad hoc requests) refines rather than reverses the 08-31 position. The final data model, meaning the serial-number anchor, the parent and room relationship, required attributes and the VAS to WMX handoff, remains open between Daniel Totino and Akansh Gangil. Do not present the architecture as settled.
- The automated three-times-daily DDP/EUDM sync is marked Q2 complete on the 08-05 deck, while the 07-16 and 07-20 record states the feed is manually triggered daily. Unresolved. Do not present that automation as production-grade without confirmation from Akansh Gangil.
- The IDP/ADM integration architecture received WAB approval, and production resourcing stalled the same week when Ankit Chadha would not commit engineering resources. Approved but unstaffed is the accurate description.

---

## 7. Output Format

Write to `Deliverables/WAM/2026-09-XX_WAM_Value_Proposition_Feasibility_Assessment.md`, dated the day it is produced. Markdown. Five parts.

**Part 1. Position statement, at most six sentences.** Where the value proposition set actually stands and what is wrong with it. A position, not a summary of the analysis. This is the sentence Sean repeats upward, so it has to be defensible without the rest of the document.

**Part 2. The feasibility matrix.** One table, the columns from 6.2, ordered by value proposition number. Wide tables must remain readable; split by capture domain if a single table becomes unreadable on one page.

**Part 3. Revised value proposition set.** Each of the seven rewritten so the claim matches the evidence, with the aspirational portion moved to a separate "and next" line. Show the original and the revised version side by side, with a one-line note on what changed and why. Where a proposition cannot honestly be made at all today, say so and recommend it be withdrawn from external use until its gate clears. Preserve the durable framing corrections already made: enrichment is performed by ADM and the Managed Services team, not by ADM alone; do not name MDM or VAS in outward-facing pitch language; complex builds belong in the value statement.

**Part 4. Gap list.** What the record cannot answer, who owns the answer, what it blocks, and by when it is needed. Merge with the outstanding requests in section 5 of the prep file rather than duplicating them, and mark which are already sent and awaited.

**Part 5. Working session agenda for David Blondel and Akansh Gangil.** Built from the gaps, in decision order, with a stated objective per item and the artifact each item must produce. This is the session that closes the assessment.

Then, separately, state which slides of the nine-slide storyline in the deck brief this assessment changes, and how. Slides 1 through 5 are the expected targets. Do not rewrite the deck in this session.

---

## 8. Constraints

- Voice per `Reference/Communication_Preferences.md`. Direct, neutral, precise. No em dashes. Minimal bold. Complete sentences.
- Realized versus planned stays visibly separate throughout. No benefit stated as realized without a baseline, a measure and evidence.
- Do not imply a capability exists today when it is planned or under development.
- Separate confirmed facts, reported information, assumptions, inferences and hypotheses. Label every assumption as an assumption.
- Do not manufacture precision. If a completeness number does not exist, say it does not exist; do not estimate one.
- Do not describe cross-functional dependencies as WAM team delivery failure.
- Do not reopen settled decisions without new evidence.
- No feature lists, sprint status, release milestones or ticket counts.
- Where the analysis contradicts something in the Executive Operating System, name the file, quote the conflicting line, and recommend the update. Do not silently overwrite the record.

---

## 9. Validation Criteria

The assessment is finished when all of the following are true.

1. Every one of the seven value propositions carries a verdict, and no verdict of Supportable now stands without a completeness figure.
2. Every Conditional verdict names a gate and a gate holder. No gate is left unowned without that absence being called out as a finding.
3. Every factual claim carries an evidence tier, and no Stated or Inferred item is written as though it were Confirmed.
4. The Microsoft AV enrichment capability is captured, its driver identified as Darryl-reported and pending confirmation, and its effect on the value proposition set assessed rather than merely noted.
5. The three completeness defects are mapped to the propositions they undermine.
6. The four conflicts in section 6.7 are flagged rather than resolved by assertion.
7. The revised propositions could be read aloud to a customer or to Dirk without a later correction.
8. The gap list has an owner and a date on every line.
9. Nothing in the document would fail the threshold test in `Reference/Sean_Update_Standard.md`: could a competent director have written this from their calendar. If yes, it goes back.
10. No em dashes.

---

## 10. Open Items for Darryl, Ask Before Finalizing

1. Is the review with Sean alone or a wider audience, and has a date been set. A pack re-shared to Dirk or Engel is built differently from a one-to-one.
2. Confirm the Microsoft AV driver behind the enrichment MVP with Akansh Gangil, and whether Violet Moyer's requirement is program-specific or general.
3. Whether the asset-upload epic deferral is acceptable given what it costs propositions 1, 3 and 7.
4. Whether any proposition should be withdrawn from external use pending its gate, which is a commercial decision rather than an analytical one.
