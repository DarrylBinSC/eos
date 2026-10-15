# AI Part Taxonomy Pilot: Decisions Required Before Build Starts

Prepared for: Akansh Gangil, product owner, ADM and DDP
Date: 2026-08-13
Subject: guidance needed by the DEV and AI teams before work begins on the AI-assisted part taxonomy and ADM attribute derivation pilot

## Why this brief exists

A requirements document for the capability has been drafted. It contains 79 requirements, 78 of which are marked Must, and 28 open items. It is sound as an acceptance checklist and it is not usable as build guidance, because it states what must be true at the end without stating what is built first, what is measured, and what waits.

Eight decisions are needed. Four of them must be made before the team writes code. The other four must be made before the pilot exit gate. None of them require new analysis; they require someone to choose.

Two numbers in the current requirement set do not reconcile with each other, and that is the most urgent item here. It is covered in Decision 2.

## Part A: decide before the team writes code

### Decision 1. Confirm the source data and whether this is a new population

Situation. The requirements assume a pilot population of 100,000 deduplicated unique part numbers drawn from the Wesco internal product taxonomy, with ten fields available per record. Neither the identity of those ten fields nor the completeness of each has been established, and it is not confirmed whether this population overlaps the roughly 20,364 supplier parts already being worked in the existing classification program. The entire feasibility case rests on this. If one of the ten fields is a product description, the work is largely a text classification problem with a high expected yield. If the ten fields are all codes and identifiers, it is a decoder problem with a much lower yield and a much larger residual.

Recommendation. Before any requirement is finalized, have the AI Data team profile the actual pilot extract and report seven numbers: the ten field names, the completeness rate of each, the count of distinct vendors, the share of parts held by the top ten vendors, the count of vendors with fewer than five parts, the share of part numbers that are purely numeric, and the overlap with parts already classified. This is a half day of work, not a dependency on another team.

If not decided. Fifteen of the 28 open items cannot be closed, including every coverage and accuracy target, and the pilot will be sized on an assumption.

### Decision 2. Confirm what the review capacity is for

Situation. Stated human review capacity is approximately 4 hours per week. A one-month pilot is therefore about 16 hours, or 960 minutes, against a population of 100,000 parts.

| Minutes spent per flagged record | Records reviewable in the pilot | Implied maximum flag rate |
|---|---|---|
| 0.5 | 1,920 | 1.9% |
| 1.0 | 960 | 1.0% |
| 2.0 | 480 | 0.5% |

Flag rates measured in the existing supplier classification work were 8.0%, 18.7%, 19.7% and 32.9% across four completed populations. The requirement set as written therefore demands a flag rate ten to thirty times lower than anything the work has produced to date, and it defers the problem to pilot measurement rather than resolving it.

Recommendation. State that the 4 hours per week is a measurement budget rather than a queue-clearing budget. It funds validation of the ground truth sample and adjudication of disagreements found by quality assurance. Records that are flagged are delivered blank and counted; they are not cleared during the pilot. This is consistent with the existing constraint that a wrong value is more harmful than a blank one, it requires no additional resource, and it makes the one-month pilot achievable.

If not decided. The flagging threshold will be lowered in week two to keep the queue manageable, which converts the primary quality control into a formality. This exact failure is already named in the risk register as RSK-011.

### Decision 3. Confirm the method constraint the timeline implies

Situation. The existing classification program produced roughly 5,400 classified parts over about six weeks using per-part external research. The pilot targets 100,000 parts in one month, which is approximately 4,500 per business day. That rate is achievable only if no per-part external lookup sits in the processing loop.

Recommendation. State explicitly that the pilot derives attributes from the internal taxonomy and from validated rules and reference data only, and that per-part external research is out of scope this phase. Position taxonomy parsing as a coverage accelerator that pre-fills attributes and reduces the number of parts needing a lookup later, not as a replacement for research.

If not decided. The team will design a method that includes lookups, and the timeline will fail for a reason nobody wrote down.

### Decision 4. Fix the Software and Service boundary before analysis starts

Situation. The draft defines Software as a software license rather than a service interaction, and Service as an offering involving an ongoing or performed interaction with the customer. Under those definitions a cloud video storage subscription classifies as Service. The existing program operates under a team-confirmed rule that classifies it as Software. The two are in direct conflict, and this is the most common classification error in this data because vendors routinely market software, cloud platforms and licenses as services with a term attached.

Recommendation. Adopt the rule already in force in the governing specification for the existing program, including its ordered tie-breakers, rather than restating the boundary from scratch. Confirm it once in writing and treat it as signed off before any derivation runs. Confirm at the same time whether Extended Warranty is a permitted classification value, since the draft defines it but does not include it in the permitted value set.

If not decided. Two runs of the same data will disagree, and the disagreement will be attributed to the model rather than to the definition.

## Part B: decide before the pilot exit gate

### Decision 5. Lock the target attribute set and the vocabulary status

Situation. The pilot claims part classification, warranty term and license term. The ADM global attribute set on Anixter P360 and DDP P360 per DDPTRK-6346 also includes Supplier Warranty Effective, Delivery Format, Software Type and License Model, and three of those value lists were pending sign-off as captured on 2026-07-06. Building against an unsigned enumeration creates rework the schedule has not accounted for.

Recommendation. Confirm the current sign-off status of each list through the supplier attribute and data governance track, state which attributes the pilot populates and which it explicitly does not, and record the rework exposure for each list still pending. Deliver the pilot against the two fixed enumerations, Warranty Duration and License Duration, and treat the three pending lists as out of scope until signed.

If not decided. The pilot will deliver values against a list that changes, and the rework will be discovered at import.

### Decision 6. Decide which evidence class wins in a conflict

Situation. The capability produces two different kinds of value: a fact read from a part-specific source, and an inference derived from a naming pattern or taxonomy rule. The draft requires them to be distinguishable but never states which one wins when they disagree on the same part. The team will hit this on day one.

Recommendation. Sourced fact takes precedence over derived inference. A taxonomy inference may not set the review flag to No until the pattern has a measured accuracy rate against a validation sample it was not built on. Name the role that approves that promotion.

If not decided. Precedence will be set implicitly by whichever process runs last.

### Decision 7. Decide the status of existing classified work

Situation. The existing program has classified roughly 5,436 unique parts across four populations and maintains a reference library of 69 brands with warranty policies and SKU decoders. The draft requires reuse of previously validated results but never establishes that this body of work exists, who owns it, or whether it seeds the pilot. It is the cheapest coverage available.

Recommendation. Establish the overlap between the pilot population and the existing classified set, then decide whether the existing results are treated as validated seed data, as ground truth for accuracy measurement, or as neither. They cannot be both seed and ground truth for the same parts.

If not decided. Work already paid for will be re-derived, and the reference library will diverge from the pilot.

### Decision 8. Define what pass looks like, and who signs it

Situation. Fifteen of the 28 open items are coverage or accuracy targets. The draft names the ADM product owner as the acceptance authority for delivered output but leaves the exit gate approval authority open, and those are not necessarily the same person, and leaves the consequence of a failing verdict undefined. A quality process with no defined consequence for failure is a reporting exercise.

Recommendation. Do not set numerical accuracy targets before profiling. Instead, make the first two weeks of the pilot a calibration run on a bounded sample: measure throughput, measured accuracy by vendor tier, and actual review minutes per flagged record, then set the targets from observed figures and hold the exit gate against them. Confirm now who approves the exit gate and what happens on a Fail verdict.

If not decided. Targets will be argued after delivery rather than agreed before it.

## What the team can start immediately

None of the eight decisions block the following, and all of it is on the critical path.

Profile the pilot extract and report the seven numbers in Decision 1. Build the output schema and the provenance fields, which are already fully specified in the draft and are not contentious. Build the deterministic conformance checks, which run in code and depend only on the field list. Build the quarantine and vendor normalization steps. Stand up the state model so processing state lives in the data and stages are safe to re-run.

## What is genuinely blocked on someone else

Four items are real external dependencies and should be tracked as such, with an owner and a date. The current dependency register in the draft does not contain them; it contains eighteen unanswered questions instead, six of which duplicate entries in the open items register.

The sign-off status of the Delivery Format, Software Type and License Model value lists. The Wesco data lake restructuring. The ADM consumption and field mapping specification. The mechanism by which delivered output reaches ADM and P360, whether by API, file export or staging table, which is not decided.

## How to use the requirements document

Keep it. The requirement writing is sound and several requirements encode failures this program has already paid for, specifically the treatment of the vendor field as unverified input, the prohibition on coercing a value to the nearest allowed enumeration, the separation of part-level facts from transaction-level dates, the requirement that quality assurance be capable of disagreeing with the analysis, and the requirement that a save be verified rather than assumed.

Use it at the exit gate, not at kickoff. Re-prioritize it so that Must means required for pilot acceptance; at present 78 of 79 requirements are Must, which gives the team no basis for a tradeoff under a one-month deadline. Move the open items that the team can answer itself out of the dependency register and into the task list, where they belong.

## Basis and confidence

Figures on the existing program, including the 5,436 classified parts, the four measured flag rates and the 69-brand reference library, were computed from the working files on 2026-08-13 and are facts. The pilot parameters, including the 100,000-part population, the one-month duration, the 4 hours per week review capacity, file import as the delivery mechanism, and the AI Data team as operator, are as recorded in the requirements draft and should be confirmed. The ADM attribute list and value lists are taken from the DDPTRK-6346 mapping as captured on 2026-07-06 and require re-confirmation. Whether the pilot population overlaps the existing supplier classification work is not established and is the gating unknown.
