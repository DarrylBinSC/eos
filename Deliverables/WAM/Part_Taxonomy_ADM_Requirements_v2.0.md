# AI-Assisted Part Taxonomy and ADM Attribute Derivation: Requirements

Version 2.0
Date: 2026-08-13
Supersedes: version 1.0, retained unchanged as `Part_Taxonomy_ADM_Requirements_v1.0_ChatGPT_original.md`

## 1. Purpose, scope, and how to read this document

### 1.1 Purpose

This document defines requirements for an AI-assisted capability that analyzes Wesco internal product taxonomy data and derives structured attributes required by Asset Data Manager (ADM).

The capability is intended to increase the completeness of ADM part records, reduce manual data enrichment effort, and accelerate onboarding of customer asset data.

The pilot population is 100,000 deduplicated unique part records, targeted for completion within one month. Delivered data is consumed by ADM and possibly by Strev. The expected consumption model is Wesco employees using the enriched data on behalf of customers, which makes the output indirectly customer facing and sets the accuracy bar accordingly.

### 1.2 What changed from version 1.0, and why

Version 1.0 was well formed as a set of requirements and not usable as build guidance. Version 2.0 makes seven changes.

The feasibility arithmetic is now stated in Appendix D rather than deferred. Population, duration, review capacity and expected flag rate did not reconcile in version 1.0, and the gap was recorded as an open item to be measured during the pilot. It is now resolved by position rather than by deferral.

Section 3 no longer restates category definitions in its own words. The Software and Service boundary is quoted from the rule already in force, because the version 1.0 wording inverted the classification of the most commonly misclassified item type in this data.

Priority now discriminates. Version 1.0 marked 78 of 79 requirements Must. Must now means required for acceptance of this pilot phase, and the distribution is reported below.

The dependency register now contains dependencies. Version 1.0 filed eighteen unanswered questions as dependencies, six of which duplicated open items and most of which the delivery team can resolve itself. Those are now tasks in section 18.

Four requirements were added: the method constraint the timeline implies, precedence between evidence classes, the disposition of pre-existing classified work, and a calibration run that produces the targets version 1.0 left open.

REQ-DAT-006 was corrected. As written in version 1.0 it required confirming manufacturer identity from part-specific evidence, which assumes a per-part external lookup that the throughput target forbids.

Section 18 is new. It states what can start immediately, what is genuinely blocked, and what waits until after the exit gate.

### 1.3 Requirement conventions

Mandatory requirements use shall. Desirable requirements use should.

| Priority | Meaning |
|---|---|
| Must | Required for acceptance of this pilot phase |
| Should | Expected where practical; absence does not block pilot acceptance |
| Could | Optional enhancement |
| Not this phase | Correct, and deliberately excluded from this phase |

Requirement identifiers use the format REQ-AREA-nnn, where AREA is DAT, FUN, MOD, EVD, PRC, QUA, REV, NFR, INT or GOV. Each requirement carries an acceptance criterion and a verification method of Test, Demonstration, Inspection or Analysis.

Priority distribution across the 93 requirements in this version:

| Priority | Count | Share |
|---|---|---|
| Must | 61 | 66% |
| Should | 28 | 30% |
| Not this phase | 4 | 4% |
| Could | 0 | 0% |

Version 1.0 was 78 Must of 79, or 99%. This version is 66%, which is an improvement and is still above the guidance of about half. That is reported as a finding rather than presented as a target met.

The reason it stays high is that a data quality pilot is mostly about whether anyone should believe the output, so the controls that make the output believable are not optional in the way a feature is optional. The honest route to a lower figure is to narrow what the pilot attempts rather than to weaken the controls on what it retains. Specifically, dropping license duration from this phase and delivering classification and warranty duration alone would move roughly eight requirements out of scope and reduce both the review and the validation surface. That decision belongs to the product owner and is not taken here.

---

## 2. Business context and objectives

This section contains no requirements.

ADM requires structured product information that existing data does not consistently carry. The absence limits ADM's ability to identify hardware, software and service products, to identify software and license information, to identify warranty information, to support renewal activity, to give Wesco employees a complete view of customer assets, and to support downstream managed services. Today that information is either missing or enriched manually.

The capability derives this information from existing Wesco internal product taxonomy data while retaining enough evidence, control, repeatability and auditability for the results to be trusted by a consumer who did not produce them.

ADM is the primary consuming application. Akansh Gangil, ADM Product Owner, is the owner of the consuming product and the acceptance authority for delivered output.

Because the output reaches customers indirectly, through Wesco employees acting on their behalf, a wrong value carries more cost than a missing one. That position is the origin of the blank-over-guess rule throughout this document and of the capacity position in Appendix D.

---

## 3. Definitions and controlled vocabulary

### 3.1 Category definitions, quoted from the rule in force

The following boundary was settled by team decision during the supplier part classification program and is quoted rather than restated. It is not reopened by this document.

Hardware. Physical products, including mounts, brackets, enclosures, cables and accessories.

Software. Anything delivering software functionality or access to a software platform. This includes SaaS, cloud platforms, cloud storage and recording subscriptions, software licenses including those labeled "Service License," and software support or update plans.

Service. Genuine non-software labor or fees only: installation, configuration or programming fees, training, on-site visits, advance replacement and RMA handling.

Extended Warranty. A SKU whose sole purpose is to extend or upgrade hardware warranty coverage.

Tie-breakers, applied in order.

1. If the deliverable is access to software, a platform or the cloud, it is Software, even when the vendor brands it a service and sells it with a term.
2. Service applies only when no software is delivered. A one-time programming fee is Service. Ongoing cloud video storage is Software.
3. A hardware-plus-service bundle is classified by primary purpose, with the bundle noted in the description.
4. Genuine ambiguity is flagged for review, not resolved by preference.

The first tie-breaker exists because vendors routinely market software, cloud platforms and licenses as services with a term attached. It is the single most common classification error in this data.

Permitted classification values are Hardware, Software, Service and Extended Warranty. Extended Warranty is retained in the permitted set even though it did not occur once in 5,436 previously classified parts. Its presence costs nothing; its absence would force those SKUs into a category that misdescribes them.

`[OPEN-001: confirm that the four-value set above is the classification vocabulary ADM expects, and its sign-off status]`

### 3.2 Other terms

| Term | Definition |
|---|---|
| ADM | Asset Data Manager, the primary consumer of the derived data |
| Internal product taxonomy | Wesco's internal taxonomy and related product data, the source domain for this phase |
| Unique part | A distinct Wesco part number. The unit of analysis for this capability |
| Part-level fact | An attribute belonging to the unique part and inherited by every occurrence of it |
| Transaction-level fact | A fact applying to a particular customer, order, asset or transaction rather than to the part |
| Sourced fact | A value supported directly by evidence naming the specific part |
| Derived inference | A value produced by a rule or analytical method rather than read from part-specific evidence |
| Vendor tier | A grouping of vendors by part count per vendor. Boundaries set by the calibration run, REQ-QUA-012 |
| Review flag | An explicit indicator that a record requires human review or a business decision |
| Unresolvable | A terminal state for a part that cannot be resolved from available evidence under the approved method |
| Blank | Absence of a value. Not "N/A", not "unknown", not zero |
| Calibration run | The bounded first stage of the pilot that measures throughput, accuracy and review effort, and from which the targets in section 16 are set |

### 3.3 Controlled value lists

| ADM attribute | Values | Status |
|---|---|---|
| Warranty Duration | 1, 2, 3, 5, 10 Years; 18 Months; Lifetime | Fixed enum as captured 2026-07-06. Confirm currency |
| License Duration | 1 Month, 6 Months, 1, 2, 3, 5, 7, 10 Years, Perpetual | Fixed enum as captured 2026-07-06. Confirm currency |
| Supplier Warranty Effective | Date of Manufacture, Installation, Factory Shipment, Sale or Invoice, End-Customer Delivery | A trigger event, not a date. Not this phase |
| Delivery Format | Eight values per DDPTRK-6346 | Pending sign-off. Not this phase |
| Software Type | Ten values per DDPTRK-6346 | Pending sign-off. Not this phase |
| License Model | Nine values per DDPTRK-6346 | Pending sign-off. Not this phase |

Three lists are unsigned. This phase does not populate attributes governed by an unsigned list, which removes the rework exposure rather than accepting it. `[OPEN-002: confirm current sign-off status of all six lists]`

---

## 4. In scope and out of scope

In scope this phase: analysis of the Wesco internal product taxonomy; a pilot population of 100,000 deduplicated unique part numbers; classification into the four values in section 3.1; derivation of warranty duration where discoverable; derivation of license duration where discoverable; use of vendor and brand reference data; use of SKU decoding rules; reuse of prior validated output where overlap is established; evidence and provenance capture; quality assurance; human review as defined in Appendix D; file export importable by ADM; and a documented pilot exit gate.

The capability is intended to become an ongoing process after the pilot rather than a one-time backfill.

Out of scope this phase: per-part external research in the processing loop, per REQ-FUN-009; the three ADM attributes governed by unsigned value lists; Supplier Warranty Effective; transaction dates; warranty and license start dates at part level; pricing; quantities; contract data; entitlement processing; downstream defect measurement, which has no measurement path until a consumer is live; and production designation of a system of record.

---

## 5. Assumptions, constraints and dependencies

### 5.1 Assumptions

| ID | Assumption | Impact if false |
|---|---|---|
| ASM-001 | The pilot extract contains 100,000 records representing 100,000 unique part numbers | If rows exceed unique parts, the map-back requirements activate and the population profile changes |
| ASM-002 | The population is deduplicated before processing begins | If false, REQ-PRC-001 becomes load-bearing rather than dormant, and effort estimates change |
| ASM-003 | ADM consumes delivered results through file import | If an API or staging table is required, section 14 is rewritten |
| ASM-004 | The AI Data team operates the pilot process | If operated by a single person, single-operator dependency becomes an active risk |
| ASM-005 | Prior validated classifications, brand reference data and SKU decoders may be reused where applicability is established | If overlap is nil, the pilot loses its cheapest coverage and the schedule tightens |
| ASM-006 | Strev may consume the data downstream; ADM is the defined consumer for the pilot | If Strev is a pilot consumer, it carries its own interface requirements, currently unwritten |
| ASM-007 | Ten source fields are available per record, sufficient to support classification without an external lookup | This is the load-bearing assumption of the entire pilot. If the fields do not carry categorical signal, the method fails and the timeline is irrelevant |

ASM-007 is the assumption most worth testing first and is the subject of the first task in section 18.

### 5.2 Constraints

| ID | Constraint |
|---|---|
| CON-001 | The pilot population is 100,000 unique parts |
| CON-002 | The pilot target duration is one month |
| CON-003 | Human review capacity is approximately 4 hours per week, allocated per Appendix D |
| CON-004 | A wrong derived value is more harmful than a blank value |
| CON-005 | Warranty and license durations are populated only where discoverable from taxonomy evidence or a validated rule |
| CON-006 | The pilot is not a production deployment and has an exit gate |
| CON-007 | The AI Data team selects the AI platform, subject to Wesco data handling constraints |
| CON-008 | The throughput target precludes a per-part external lookup in the processing loop. See Appendix D |

### 5.3 Dependencies

A dependency has a named owner outside the delivery team and a status. Questions the delivery team can answer itself are tasks and appear in section 18, not here.

| ID | Dependency | Owner | Status |
|---|---|---|---|
| DEP-001 | Sign-off of the Delivery Format, Software Type and License Model value lists | ADM data governance track | Pending. Mitigated this phase by excluding the attributes they govern |
| DEP-002 | Wesco data lake restructuring, which creates room for these attributes | `[OPEN-003: owner]` | In progress |
| DEP-003 | ADM consumption and field mapping specification | Akansh Gangil | `[OPEN-004: status]` |
| DEP-004 | Mechanism by which delivered output reaches ADM and P360 | Akansh Gangil | Not decided. Pilot assumes file import per ASM-003 |
| DEP-005 | Confirmation of the classification vocabulary and its sign-off status | ADM data governance track | Open, see OPEN-001 |

---

## 6. Data requirements

| ID | Requirement | Priority | Acceptance criterion | Verification |
|---|---|---|---|---|
| REQ-DAT-001 | The solution shall use the unique part number as the unit of analysis. | Must | Each pilot record is processed and reported against one unique part identifier. | Test |
| REQ-DAT-002 | The solution shall preserve each source part number as supplied and shall not alter its meaning through numeric or format coercion. | Must | Structured alphanumeric, purely numeric and custom part-number forms round-trip without semantic alteration. | Test |
| REQ-DAT-003 | The solution shall produce a completeness profile for every source field before derivation begins. | Must | A completeness rate exists for each source field, reported before any derivation is run. | Inspection |
| REQ-DAT-004 | The solution shall report the vendor concentration of the population, stating the share of parts held by the top ten vendors and the count of vendors with fewer than five parts. | Must | Both figures are reported before vendor tier boundaries are set. | Inspection |
| REQ-DAT-005 | The solution shall normalize vendor strings to a canonical representation before vendor-based grouping. | Must | Equivalent vendor strings map to a documented canonical value before grouping. | Test |
| REQ-DAT-006 | The solution shall treat the source vendor field as unverified input. | Must | No derivation is represented as verified solely because a vendor value is present in the source record. | Test |
| REQ-DAT-007 | The solution shall confirm manufacturer identity against a validated reference entry or decoder rule before manufacturer identity is used to select a derivation rule, and shall mark the record vendor-unconfirmed where no such confirmation exists. | Must | In the quality sample, every record whose derivation rule was selected on vendor identity carries either a confirmation reference or a vendor-unconfirmed marker. | Test |
| REQ-DAT-008 | The solution shall quarantine junk and non-product records before attribute derivation begins. | Should | Quarantined records are absent from the derivation population and are separately identifiable. | Test |
| REQ-DAT-009 | The solution shall validate an input layout against an explicit field mapping before processing. | Should | Processing does not begin until input fields are mapped to the expected schema. | Demonstration |
| REQ-DAT-010 | The solution shall not infer header position or field meaning from an arbitrary source layout without explicit validation. | Should | A deliberately altered input layout is rejected or routed for mapping rather than silently processed. | Test |
| REQ-DAT-011 | The solution shall report the overlap between the pilot population and previously classified parts. | Must | An overlap count is reported before the disposition decision in REQ-FUN-010 is taken. | Inspection |

REQ-DAT-007 replaces the version 1.0 requirement to confirm manufacturer identity from part-specific evidence, which assumed an external lookup that CON-008 excludes. The control is preserved by making the unconfirmed state explicit and carrying it on the record rather than by requiring research the method does not permit.

---

## 7. Functional requirements: derivation and classification

| ID | Requirement | Priority | Acceptance criterion | Verification |
|---|---|---|---|---|
| REQ-FUN-001 | The solution shall derive a part classification from the permitted value set in section 3.1 when the available evidence supports one. | Must | Every populated classification is one of the four permitted values and carries recorded evidence. | Test |
| REQ-FUN-002 | The solution shall apply the tie-breakers in section 3.1 in the stated order when classifying a part. | Must | Test cases covering a cloud storage subscription, a programming fee, a software support plan and a hardware-plus-service bundle are classified per section 3.1. | Test |
| REQ-FUN-003 | The solution shall derive a warranty duration only where supported by taxonomy evidence or a validated rule. | Must | No populated warranty duration lacks supporting evidence or a validated rule identifier. | Test |
| REQ-FUN-004 | The solution shall derive a license duration only where supported by taxonomy evidence or a validated rule. | Should | No populated license duration lacks supporting evidence or a validated rule identifier. | Test |
| REQ-FUN-005 | The solution shall state and report a separate coverage target and accuracy target for each derivation, by vendor tier. | Must | Classification, warranty duration and license duration each carry separate coverage and accuracy targets for every vendor tier. Values are set by the calibration run per REQ-QUA-012. | Inspection |
| REQ-FUN-006 | The solution shall report measured coverage separately from measured accuracy, with no blended figure presented as the quality of a derivation. | Must | Results carry separate coverage and accuracy fields by tier. | Inspection |
| REQ-FUN-007 | The solution shall reuse a previously validated part-level result when the same unique part recurs and the result remains valid under current rule and model versions. | Should | A previously validated part is not re-derived where its result remains valid. | Test |
| REQ-FUN-008 | The solution shall permit a defined classification value to have zero observed instances without assigning records to it. | Should | A population containing no instances of a permitted value reports zero rather than forcing assignments. | Test |
| REQ-FUN-009 | The solution shall derive attributes from the internal taxonomy, validated rules and reference data only, and shall not perform a per-part external lookup within the processing loop. | Must | No processing stage issues a per-part external request. Any lookup is a separate, out-of-band activity that does not gate throughput. | Demonstration |
| REQ-FUN-010 | The solution shall record a single disposition for previously classified parts as seed data, as ground truth, or as neither, and shall not use the same records for both purposes. | Must | The disposition is recorded before the calibration run, and no record appears in both the seed pool and the ground truth set. | Inspection |
| REQ-FUN-011 | The solution shall apply the evidence class precedence in section 9 when two methods produce different values for the same attribute on the same part. | Must | In a constructed conflict set, the higher precedence class prevails and the superseded value is retained in the record history. | Test |

REQ-FUN-009 makes explicit the method constraint the one-month timeline already imposes. Appendix D shows the arithmetic. Taxonomy parsing is positioned as a coverage accelerator that pre-fills attributes and reduces the parts needing a later lookup, not as a replacement for research.

---

## 8. Data model and conformance requirements

| ID | Requirement | Priority | Acceptance criterion | Verification |
|---|---|---|---|---|
| REQ-MOD-001 | The solution shall populate a controlled attribute only with a value from the applicable approved ADM value list. | Must | Zero delivered controlled attributes contain an off-list value. | Test |
| REQ-MOD-002 | The solution shall leave an attribute blank where available evidence does not support a value. | Must | Test records with insufficient evidence carry a blank target value. | Test |
| REQ-MOD-003 | The solution shall leave a controlled attribute blank where an observed value cannot be mapped to the controlled vocabulary, and shall not substitute the nearest allowed value. | Must | Non-conforming values are not coerced. | Test |
| REQ-MOD-004 | The solution shall flag every source value that cannot be mapped to the controlled vocabulary, recording the original observed value. | Must | Every unmapped value appears in the non-conformance report with its original form. | Test |
| REQ-MOD-005 | The solution shall represent blank as an empty value rather than "N/A", "unknown" or zero. | Must | Unresolved attributes contain no placeholder. | Test |
| REQ-MOD-006 | The solution shall model warranty and licensing attributes as global part attributes rather than as fields conditional on category. | Must | A hardware part carries applicable warranty and licensing attributes without violating the schema. | Test |
| REQ-MOD-007 | The solution shall store part-level facts separately from transaction-level facts. | Should | Part-level output contains no transaction-specific date, price, quantity or contract value. | Inspection |
| REQ-MOD-008 | The solution shall not derive a warranty or license start date as a property of the unique part. | Must | No unique-part output contains a start date as an intrinsic attribute. | Test |
| REQ-MOD-009 | The solution shall not populate an ADM attribute governed by a value list that is not signed off. | Must | Delivered output contains no value for Delivery Format, Software Type, License Model or Supplier Warranty Effective. | Test |

---

## 9. Evidence, confidence and trust requirements

Evidence classes and their precedence, highest first. A lower class shall not overwrite a value set by a higher class.

| Rank | Evidence class | Maximum confidence | May complete a record automatically |
|---|---|---|---|
| 1 | Direct authoritative source naming the exact part | High | Yes |
| 2 | Validated rule or decoder with a measured accuracy above threshold | Set by the measured rate | Yes, after validation per REQ-QUA-002 |
| 3 | Vendor or class default from a documented brand policy | Medium | Policy decision, see OPEN-007 |
| 4 | Unvalidated taxonomy inference | Low | No |
| 5 | Not determined | Blank and flagged | Not applicable |

| ID | Requirement | Priority | Acceptance criterion | Verification |
|---|---|---|---|---|
| REQ-EVD-001 | The solution shall record the evidence class for every populated derived attribute, using the classes above. | Must | Every populated result carries one of the five evidence classes. | Test |
| REQ-EVD-002 | The solution shall record a source identifier or rule identifier for every populated derived attribute. | Must | Each populated attribute carries an identifier sufficient to locate the evidence used. | Inspection |
| REQ-EVD-003 | The solution shall record a confidence value or band for every derived inference. | Must | No derived inference lacks a confidence value. | Test |
| REQ-EVD-004 | The solution shall record an explicit review flag on every processed unique part. | Must | Review state is present on every part rather than inferred. | Inspection |
| REQ-EVD-005 | The solution shall record the rule, prompt or model version responsible for each derived inference. | Should | Each inference traces to the version that produced it. | Inspection |
| REQ-EVD-006 | The solution shall record a processing timestamp on each derived inference. | Should | Every inference carries a timestamp. | Inspection |
| REQ-EVD-007 | The solution shall not treat evidence naming only a product family, a brand homepage or a non-part-specific source as sufficient support for a value. | Must | Records supported only by general evidence remain flagged and are not auto-completed. | Test |
| REQ-EVD-008 | The solution shall not permit an unvalidated taxonomy inference to set the review flag to No. | Must | Zero records carry evidence class 4 with review flag No. | Test |

---

## 10. Process and workflow requirements

| ID | Requirement | Priority | Acceptance criterion | Verification |
|---|---|---|---|---|
| REQ-PRC-001 | The solution shall derive a part-level fact once per unique part and make the result inheritable by subsequent occurrences. | Should | Repeated occurrences inherit the validated result rather than producing independent conflicting facts. | Test |
| REQ-PRC-002 | The solution shall record processing state explicitly in the data. | Must | The state of every part is determinable by reading recorded fields, without reconstructing history externally. | Inspection |
| REQ-PRC-003 | The solution shall permit each processing stage to be re-run without duplicating completed work. | Should | Re-executing a completed stage produces no duplicate derived records. | Test |
| REQ-PRC-004 | The solution shall permit each processing stage to be re-run without corrupting previously validated results. | Should | Re-execution preserves validated results unless a controlled version change requires reprocessing. | Test |
| REQ-PRC-005 | The solution shall process work in bounded units checkpointed before the next unit begins. | Must | An interrupted run retains the most recent completed checkpoint rather than losing work since run start. | Demonstration |
| REQ-PRC-006 | The solution shall verify persistence after writing a checkpoint or committed result. | Must | A simulated persistence failure is detected rather than reported as a successful save. | Demonstration |
| REQ-PRC-007 | The solution shall treat Unresolvable as a terminal analytical state. | Should | A part marked Unresolvable does not re-enter the analysis queue without a business decision or material new evidence. | Test |
| REQ-PRC-008 | The solution shall route Unresolvable parts to a recorded business-decision path. | Should | Every Unresolvable part carries a disposition status outside the derivation queue. | Inspection |
| REQ-PRC-009 | The solution shall produce immutable, versioned output for each delivery event. | Should | A delivered version remains retrievable and comparable after a later version is issued. | Demonstration |

REQ-PRC-001 is dormant if ASM-002 holds and the population is genuinely pre-deduplicated, which is why it is Should rather than Must this phase. It becomes load-bearing the moment that assumption is false, so it is written now rather than added later. Confirming ASM-002 is part of the profiling task in section 18.1.

---

## 11. Quality assurance and verification requirements

| ID | Requirement | Priority | Acceptance criterion | Verification |
|---|---|---|---|---|
| REQ-QUA-001 | The solution shall measure the accuracy of a derivation rule against human-validated ground truth not used to build or tune that rule. | Must | The validation sample is documented as independent of the rule-development sample. | Inspection |
| REQ-QUA-002 | The solution shall prevent automatic completion by a derivation rule until the rule achieves the accuracy threshold set by the calibration run and is approved by `[OPEN-005: approving role]`. | Must | A rule below threshold or lacking approval cannot auto-complete records. | Test |
| REQ-QUA-003 | The quality process shall include at least one validation method capable of disagreeing with the primary derivation, differing from it by input signal, method, model or operator. | Must | The independent method reads the source record rather than the primary result, and the difference in frame is documented. | Demonstration |
| REQ-QUA-004 | The independent method shall report a disagreement rate by attribute and vendor tier rather than substituting a second authoritative answer. | Must | Quality results report disagreement rates, and disagreements are adjudicated individually. | Inspection |
| REQ-QUA-005 | The solution shall withhold automatic completion for an attribute where independent disagreement exceeds the threshold set by the calibration run. | Must | A test population exceeding the threshold does not pass automatic completion for that attribute. | Test |
| REQ-QUA-006 | The solution shall run deterministic conformance checks in code against every delivered record. | Must | Every delivered record has passed the defined checks. | Test |
| REQ-QUA-007 | The solution shall block delivery when a deterministic conformance check fails. | Must | A deliberately non-conforming record prevents the affected delivery from passing. | Demonstration |
| REQ-QUA-008 | The solution shall validate structural integrity of the write and export path separately from content validation. | Should | A structural corruption test is detected even where the attribute values themselves are valid. | Test |
| REQ-QUA-009 | Quality sampling shall be stratified by vendor tier, attribute, confidence band and derivation method. | Must | The sample report shows representation across all four dimensions. | Inspection |
| REQ-QUA-010 | Quality sampling shall oversample long-tail vendors and the low-confidence band relative to their population share. | Should | Sampling intensity for those segments exceeds their unadjusted population share. | Analysis |
| REQ-QUA-011 | The solution shall measure the downstream defect rate found after delivery. | Not this phase | No consumer is live during the pilot, so no measurement path exists. Establish at production exit. | Analysis |
| REQ-QUA-012 | The pilot shall begin with a calibration run on a bounded sample that measures throughput per working day, accuracy by vendor tier and attribute, and actual review minutes per flagged record, and from which the targets in REQ-FUN-005, REQ-QUA-002 and REQ-QUA-005 are set. | Must | The calibration report states all three measured figures, and the targets are recorded and approved before the full population is processed. | Analysis |

REQ-QUA-012 replaces fifteen open items in version 1.0 with one dated activity. Targets that nobody currently has are produced by measurement rather than negotiated in advance or left open.

---

## 12. Human review and decision rights requirements

| ID | Requirement | Priority | Acceptance criterion | Verification |
|---|---|---|---|---|
| REQ-REV-001 | The process shall prefer a blank, flagged result over a derived value not meeting the approved evidence or confidence standard. | Must | Records below standard remain blank and flagged rather than populated with a plausible value. | Test |
| REQ-REV-002 | Review capacity shall be allocated to ground truth validation and disagreement adjudication, and shall not be allocated to clearing the flagged queue. | Must | The review log shows time spent on ground truth and adjudication. Flagged records not adjudicated are delivered blank and counted. | Inspection |
| REQ-REV-003 | The solution shall report the flagged record count as a measured output of the phase rather than as a backlog. | Must | The delivery report states flagged count by attribute and tier, with no implied obligation to have cleared it. | Inspection |
| REQ-REV-004 | The process shall not lower a review or flagging threshold in order to keep the queue within capacity. | Must | A capacity pressure event produces a reported exception rather than an undocumented threshold change. | Inspection |
| REQ-REV-005 | A human review decision establishing a generally applicable interpretation shall be written back into the rules or reference data. | Should | A recurring case subject to the same general decision is handled by the updated rule rather than by a repeat manual decision. | Demonstration |
| REQ-REV-006 | Akansh Gangil, as ADM Product Owner, shall record acceptance or rejection of the delivered pilot output. | Must | A recorded acceptance decision exists. | Inspection |
| REQ-REV-007 | The solution shall record the definitional owner for each category boundary and vocabulary, and shall route a boundary dispute to that owner rather than resolving it in analysis. | Should | Each boundary in section 3 carries a named owner, and disputes appear in that owner's queue. | Inspection |

Version 1.0 required the review workload not to exceed 4 hours per week and left the permitted flag rate to be derived from measurement. Appendix D shows why that could not hold. REQ-REV-002 and REQ-REV-003 replace it with a position: capacity funds measurement, and flagged records are an output, not a debt.

---

## 13. Non-functional requirements

| ID | Requirement | Priority | Acceptance criterion | Verification |
|---|---|---|---|---|
| REQ-NFR-001 | The solution shall sustain the throughput rate established by the calibration run for the remainder of the pilot population. | Should | Measured rate over the full run does not fall below the calibration rate by more than a stated tolerance. | Analysis |
| REQ-NFR-002 | The pilot shall report elapsed time to process the full population against the one-month target, and shall report a variance rather than absorbing it. | Must | Elapsed time is reported against target with any variance explained. | Analysis |
| REQ-NFR-003 | The AI Data team shall document the selected AI or analytical platform and applicable data-handling constraints before pilot data is submitted to it. | Must | Platform and constraints are recorded before processing begins. | Inspection |
| REQ-NFR-004 | Pilot working data shall reside in `[OPEN-008: approved working-data location]`. | Must | Working data is stored only in the approved location. | Inspection |
| REQ-NFR-005 | Access to pilot working data and output shall be restricted to `[OPEN-009: approved roles]`, separating who may submit, who may see work in progress, who may see delivered output and who may change the rules. | Must | Access configuration matches the approved role list across the four populations. | Inspection |
| REQ-NFR-006 | The process shall provide an auditable history sufficient to trace a delivered value to its source or rule, version, confidence, review state and processing time. | Must | A sampled delivered value traces end to end. | Demonstration |
| REQ-NFR-007 | The solution shall support processing of subsequent populations without rebuilding the method. | Should | A second population is processed using the same pipeline. | Demonstration |
| REQ-NFR-008 | Pilot operating cost shall be measured and reported per thousand records on observed consumption. | Should | Cost per thousand records is reported from observed figures. | Analysis |
| REQ-NFR-009 | Pilot data and evidence shall be retained for a defined period. | Not this phase | Establish before production exit. | Inspection |
| REQ-NFR-010 | The solution shall define availability and recovery expectations for the working store. | Not this phase | Establish before production exit. | Inspection |

Version 1.0 stated that the solution shall process 100,000 parts within one month. That is a schedule commitment written as a requirement, and it was unsupported by any demonstrated rate. REQ-NFR-001 and REQ-NFR-002 replace it with a rate established by measurement and a variance that is reported rather than absorbed.

---

## 14. Interface and integration requirements

| ID | Requirement | Priority | Acceptance criterion | Verification |
|---|---|---|---|---|
| REQ-INT-001 | The solution shall export derived results in a file ADM can import. | Must | ADM imports the output without manual reconstruction of the derived data. | Demonstration |
| REQ-INT-002 | The exported result shall conform to the applicable ADM global attribute structure on P360, without category-specific nesting of global attributes. | Must | Exported fields map to the approved global structure. | Test |
| REQ-INT-003 | The delivery shall preserve the unique part identifier associating each result with the corresponding ADM part. | Must | Every imported result reconciles to the unique part that produced it. | Test |
| REQ-INT-004 | The solution shall provide a reconciliation report proving that what was delivered is what was received. | Should | Delivered and received record counts and checksums match. | Test |
| REQ-INT-005 | The solution shall define error and rejection handling at the ADM boundary. | Should | Rejected records are reported with a reason rather than silently dropped. | Demonstration |
| REQ-INT-006 | A system of record shall be designated for the delivered attributes. | Not this phase | Required before production exit, not before pilot exit. | Inspection |

---

## 15. Governance and change control requirements

| ID | Requirement | Priority | Acceptance criterion | Verification |
|---|---|---|---|---|
| REQ-GOV-001 | Rules, prompts and models used to derive pilot results shall be versioned. | Must | Every active rule, prompt and model carries a retrievable version identifier. | Inspection |
| REQ-GOV-002 | A material change to a rule, prompt or model shall trigger re-validation of results produced under the prior version. | Should | Change records identify the affected population and its re-validation disposition. | Inspection |
| REQ-GOV-003 | A regression set shall be executed before a changed rule, prompt or model is adopted. | Should | No change is adopted without a recorded regression result. | Test |
| REQ-GOV-004 | Recurring controlled-vocabulary non-conformance shall be escalated for a business decision on vocabulary extension. | Should | Repeated unmapped values appear in a governance queue rather than being coerced or flagged indefinitely. | Inspection |
| REQ-GOV-005 | The quality process shall support a failing verdict. | Must | The pilot quality decision can return Fail. | Demonstration |
| REQ-GOV-006 | A failing verdict shall carry a documented consequence, recorded before the exit-gate decision. | Must | `[OPEN-006: consequence of a Fail verdict]` is recorded before the gate. | Inspection |
| REQ-GOV-007 | Quality follow-up actions shall carry an owner and a due date. | Must | Every accepted follow-up has both. | Inspection |
| REQ-GOV-008 | The pilot shall have a documented exit-gate decision of Pass, Pass with follow-ups, or Fail before being treated as a production capability. | Must | A recorded verdict exists. | Inspection |
| REQ-GOV-009 | The pilot exit-gate decision shall be approved by `[OPEN-010: exit-gate approval authority]`. | Must | The exit-gate record carries the required approval. | Inspection |
| REQ-GOV-010 | Model and prompt changes shall pass through the same change control as a code change. | Should | Prompt changes appear in the change log with a version and a regression result. | Inspection |

---

## 16. Acceptance criteria and phase exit conditions

Verdicts: Pass means deliver and exit. Pass with follow-ups means deliver and exit, with follow-ups tracked as work carrying an owner and a date; this is the expected common outcome. Fail means do not deliver, with the consequence recorded per REQ-GOV-006.

| Exit condition | Supporting requirements | Current state |
|---|---|---|
| Source profile completed and ASM-007 tested | REQ-DAT-003, REQ-DAT-004, REQ-DAT-011 | Not started. Gating |
| Calibration run completed and targets set | REQ-QUA-012 | Not started |
| Classification measured against calibration-set coverage and accuracy targets by tier | REQ-FUN-001, 002, 005, 006 | Targets set by calibration |
| Warranty duration measured against calibration-set targets by tier | REQ-FUN-003, 005 | Targets set by calibration |
| License duration measured against calibration-set targets by tier | REQ-FUN-004, 005 | Targets set by calibration |
| Independent disagreement within the calibration-set threshold | REQ-QUA-003, 004, 005 | Threshold set by calibration |
| Deterministic content and structural checks pass on every delivered record | REQ-QUA-006, 007, 008 | Defined |
| Review capacity spent on measurement, with flagged count reported as an output | REQ-REV-002, 003 | Defined |
| Throughput sustained at the calibration rate, with variance reported | REQ-NFR-001, 002 | Defined |
| ADM imports the delivered file and reconciles | REQ-INT-001, 003 | Defined |
| No attribute delivered against an unsigned value list | REQ-MOD-009 | Defined |
| ADM Product Owner records acceptance | REQ-REV-006 | Defined |
| Working data location, access roles and platform recorded | REQ-NFR-003, 004, 005 | Open items 8 and 9 |
| Exit-gate verdict recorded and approved | REQ-GOV-008, 009 | Open item 10 |

Downstream defect rate, retention, availability and system of record are production exit conditions, not pilot exit conditions.

---

## 17. Risk register

| ID | Risk | Consequence | Mitigating requirements |
|---|---|---|---|
| RSK-001 | Incorrect vendor value treated as authoritative | Wrong derivation rule applied at scale | REQ-DAT-005, 006, 007 |
| RSK-002 | Vendor naming variation fragments one vendor into several groups | Reduced rule reuse, unreliable tier reporting | REQ-DAT-005 |
| RSK-003 | Weak evidence accepted for a derived value | Wrong values read as credible; remediation pass | REQ-EVD-002, 007, 008 |
| RSK-004 | Software licenses and cloud subscriptions misclassified as Service | ADM classification and downstream use incorrect | Section 3.1 quoted definitions and tie-breakers; REQ-FUN-002 tests them |
| RSK-005 | Unverifiable values filled with plausible answers | Wrong data delivered instead of a visible gap | REQ-MOD-002, REQ-REV-001 |
| RSK-006 | Real values fall outside the ADM vocabulary | Values silently distorted to fit an enum | REQ-MOD-003, 004, REQ-GOV-004 |
| RSK-007 | Quality checking correlated with the derivation method | QA confirms rather than tests | REQ-QUA-003, 004, 005 |
| RSK-008 | Structural corruption during export or write | Valid content mechanically corrupted undetected | REQ-QUA-008 |
| RSK-009 | A save reports success but data is not persisted | Completed work lost | REQ-PRC-005, 006 |
| RSK-010 | Long-running work committed only at completion | Failure near the end loses significant work | REQ-PRC-005 |
| RSK-011 | Flagged volume treated as a backlog to clear | Flagging threshold weakened under pressure | REQ-REV-002, 003, 004 |
| RSK-012 | Process state inferred rather than stored | Progress and remaining work not reliably determinable | REQ-PRC-002 |
| RSK-013 | Re-running processing duplicates or corrupts results | Ongoing operation unreliable | REQ-PRC-003, 004 |
| RSK-014 | Previously classified parts re-derived | Unit cost stays flat; cheapest coverage wasted | REQ-DAT-011, REQ-FUN-007, 010 |
| RSK-015 | Long-tail vendors underrepresented in validation | Reported accuracy overstates real performance | REQ-QUA-009, 010 |
| RSK-016 | Junk records consume analysis effort | Effort spent on data that cannot create value | REQ-DAT-008 |
| RSK-017 | Unresolvable parts circulate in the queue | Repeated effort with no new information | REQ-PRC-007, 008 |
| RSK-018 | Source-layout variation parsed incorrectly | Records silently mapped to wrong fields | REQ-DAT-009, 010 |
| RSK-019 | A rule change regresses previously valid results | Releases silently reduce quality | REQ-GOV-001, 002, 003 |
| RSK-020 | Pilot results treated as production-ready without a gate | Unresolved gaps enter production | REQ-GOV-008, 009 |
| RSK-021 | Transaction facts represented as intrinsic part facts | ADM carries semantically wrong part data | REQ-MOD-007, 008 |
| RSK-022 | ASM-007 false: the ten source fields carry insufficient categorical signal | The method does not work and the timeline is irrelevant | REQ-DAT-003, REQ-QUA-012. Tested first, per section 18 |
| RSK-023 | Attributes built against a value list that changes before delivery | Rework discovered at import | REQ-MOD-009, DEP-001 |
| RSK-024 | Taxonomy inference and sourced fact conflict resolved by run order | Inconsistent values with no decision trail | REQ-FUN-011, section 9 precedence |

RSK-004 in version 1.0 pointed its mitigation at a requirement to apply the section 3 definitions, where those definitions were the defect. The mitigation now rests on the quoted rule itself, with REQ-FUN-002 as the test.

---

## 18. Sequencing

### 18.1 Start immediately, dependent on none of the open decisions

Profile the pilot extract and report: the ten field names, completeness per field, distinct vendor count, top-ten vendor share, count of vendors with fewer than five parts, share of purely numeric part numbers, and overlap with previously classified parts. This tests ASM-007 and closes open items that version 1.0 filed as external dependencies. Estimated half a day. Owner: AI Data team.

Build the output schema and provenance fields, per sections 8 and 9. Uncontentious and fully specified.

Build the deterministic conformance checks, per REQ-QUA-006 through 008. Code only; depends on the field list, not on any target.

Build intake, layout validation, quarantine and vendor normalization, per section 6.

Stand up the state model so processing state lives in the data and stages are re-runnable, per REQ-PRC-002 through 006.

Run the calibration run, per REQ-QUA-012, as soon as the profile is available.

### 18.2 Blocked, on whom

DEP-001 through DEP-005 in section 5.3. Each carries an owner and a status. Nothing else is externally blocked.

### 18.3 Waits until after the exit gate

Downstream defect measurement, retention, availability and recovery, system of record designation, the three attributes governed by unsigned value lists, Supplier Warranty Effective, entitlement, and full change-control machinery for prompts and models.

---

## Appendix A: ADM attribute conformance matrix

| ADM attribute | Scope this phase | Unit | Derivation basis | Vocabulary status | Blank policy |
|---|---|---|---|---|---|
| Part classification | In scope | Unique part | Internal taxonomy, validated rules, reference data | Four values per section 3.1; sign-off open, OPEN-001 | Blank and flag when unsupported |
| Warranty Duration | In scope where discoverable | Unique part | Internal taxonomy, validated rules | Fixed enum, confirm currency | Blank and flag when unsupported |
| License Duration | In scope where discoverable | Unique part | Internal taxonomy, validated rules | Fixed enum, confirm currency | Blank and flag when unsupported |
| Supplier Warranty Effective | Not this phase | Unique part | A trigger event, not a date | Fixed enum | Not populated |
| Delivery Format | Not this phase | Unique part | Not attempted | Pending sign-off | Not populated |
| Software Type | Not this phase | Unique part | Not attempted | Pending sign-off | Not populated |
| License Model | Not this phase | Unique part | Not attempted | Pending sign-off | Not populated |
| Warranty or license start date | Not this phase, and not a part attribute | Transaction or asset instance | Computed downstream from the effective trigger plus the order or install date | Not applicable | Not populated |
| Transaction dates, price, quantity, contract data | Not this phase | Transaction | Not applicable | Not applicable | Not populated |
| Entitlement | Not this phase | Undetermined | Applicability not established | Undetermined | Not populated |

---

## Appendix B: Requirement traceability

Acceptance criteria and verification methods are stated once, in the section tables, and are not restated here. This matrix carries identifier, objective and status only.

| Area | Objective served | Requirements | Status |
|---|---|---|---|
| DAT | Establish a trustworthy input contract and an accurate population profile | REQ-DAT-001 to 011 | 003, 004, 011 pending the profile task in 18.1; remainder defined |
| FUN | Derive the in-scope attributes at measurable coverage and accuracy | REQ-FUN-001 to 011 | 005 pending calibration; remainder defined |
| MOD | Deliver output ADM can consume without distortion | REQ-MOD-001 to 009 | 001 pending OPEN-001; remainder defined |
| EVD | Make the basis of every value inspectable and rank-ordered | REQ-EVD-001 to 008 | Defined |
| PRC | Make the process repeatable, resumable and safe to re-run | REQ-PRC-001 to 009 | Defined |
| QUA | Make the output believable by a consumer who did not produce it | REQ-QUA-001 to 012 | 002, 005 pending calibration; 011 not this phase; remainder defined |
| REV | Keep human judgment where it belongs and within capacity | REQ-REV-001 to 007 | 002 pending OPEN-005; remainder defined |
| NFR | Establish throughput, cost, access and auditability on observed figures | REQ-NFR-001 to 010 | 004, 005 pending OPEN-008 and 009; 009, 010 not this phase |
| INT | Deliver to ADM and prove what arrived | REQ-INT-001 to 006 | 006 not this phase; remainder defined |
| GOV | Make a rule change traceable to the records it affects | REQ-GOV-001 to 010 | 006, 009 pending OPEN-006 and 010; remainder defined |

---

## Appendix C: Open items

Ten open items, reduced from twenty-eight in version 1.0. Eighteen were closed by being reclassified: fifteen coverage and accuracy targets are now produced by the calibration run, REQ-QUA-012; and the source profiling questions became tasks in section 18.1 rather than dependencies.

| ID | Question | Owner | Related |
|---|---|---|---|
| OPEN-001 | Is the four-value classification set in section 3.1 what ADM expects, and is it signed off | ADM data governance | REQ-FUN-001, REQ-MOD-001 |
| OPEN-002 | Current sign-off status of all six ADM value lists | ADM data governance | REQ-MOD-009, DEP-001 |
| OPEN-003 | Owner of the data lake restructuring dependency | Product owner | DEP-002 |
| OPEN-004 | Status of the ADM consumption and field mapping specification | Akansh Gangil | DEP-003 |
| OPEN-005 | Which role approves a derivation rule for automatic completion | Product owner | REQ-QUA-002 |
| OPEN-006 | Defined consequence when the quality verdict is Fail | Product owner | REQ-GOV-006 |
| OPEN-007 | May a vendor or class default auto-complete a record, or does it always flag | Product owner | Section 9, class 3 |
| OPEN-008 | Where pilot working data resides | AI Data team | REQ-NFR-004 |
| OPEN-009 | Which roles may access working data and output, across the four access populations | AI Data team | REQ-NFR-005 |
| OPEN-010 | Who approves the pilot exit gate, if different from the output acceptance authority | Product owner | REQ-GOV-009 |

---

## Appendix D: Feasibility reconciliation

### D.1 Review capacity against population

Stated capacity is approximately 4 hours per week. Across a one-month pilot that is roughly 16 hours, or 960 minutes.

| Minutes per flagged record | Records reviewable in the pilot | Implied maximum flag rate against 100,000 parts |
|---|---|---|
| 0.5 | 1,920 | 1.9% |
| 1.0 | 960 | 1.0% |
| 2.0 | 480 | 0.5% |

Measured flag rates across four completed populations of comparable work were 8.0%, 18.7%, 19.7% and 32.9%, computed 2026-08-13. Manual research on this data took roughly three to five minutes per part, which makes one to two minutes a reasonable working range for adjudicating a flagged record.

The plan does not close if review capacity is intended to clear the flagged queue. The gap is a factor of roughly ten to thirty.

Position taken, per REQ-REV-002 and REQ-REV-003. Review capacity is a measurement budget. It funds validation of the ground truth sample and adjudication of disagreements surfaced by the independent quality method. Both scale with the sample rather than with the population and fit inside 16 hours. Records that are flagged and not adjudicated are delivered blank and counted, which is consistent with CON-004. The flagged count is a reported output of the pilot, not a backlog it failed to clear.

Rejected alternatives, recorded so they are not revisited without new information. Lowering the flagging threshold to fit capacity converts the primary quality control into a formality and is the failure mode named at RSK-011. Adding review capacity sufficient to clear the queue would require roughly 160 to 500 hours over the pilot, which is not a marginal ask. Reducing the population to fit a queue-clearing model would put the pilot at roughly 5,000 to 10,000 parts, which remains available if the position above is rejected.

### D.2 Throughput against demonstrated rate

The target is 100,000 unique parts in one month, roughly 4,500 per working day.

The demonstrated rate for comparable classification work with a per-part external lookup in the processing loop was approximately 5,400 unique parts over about six weeks, or roughly 180 per working day. The target is about twenty-five times that rate.

That ratio is not achievable by effort. It is achievable only by removing the external lookup from the processing loop, which is what CON-008 and REQ-FUN-009 now state. The consequence is accepted deliberately: taxonomy parsing carries lower evidence strength than part-specific sourcing, which is why the evidence class precedence in section 9 exists and why an unvalidated taxonomy inference may not clear its own review flag under REQ-EVD-008.

The residual uncertainty is that no rate has been demonstrated for the taxonomy parsing method on this data. REQ-QUA-012 establishes it on a bounded sample before the full population is committed, and REQ-NFR-002 requires the variance against the one-month target to be reported rather than absorbed.

### D.3 Summary position

The plan closes on the following basis. Review capacity funds measurement rather than queue clearing. The processing loop performs no per-part external lookup. Coverage and accuracy targets are set by a calibration run rather than asserted in advance. The one-month figure is treated as a target with a reported variance rather than as a commitment, because no rate for this method has yet been demonstrated.

If any of those four is rejected, the plan does not close and the population or the duration has to move.

---

## Validation findings

Checked against the twelve criteria in the drafting prompt and the additional criteria added in prompt version 1.1. Two failures are reported rather than corrected.

The Must share is 66%, above the guidance of about half. Stated in section 1.3 with the reasoning and the recommended route to reduce it, which is dropping license duration from this phase rather than weakening controls. An earlier draft of this document stated a distribution that did not match the priorities actually assigned to the requirement tables; the figures above were recounted from the tables and are correct. That error is worth noting because it is the same class of failure this version corrects in version 1.0: a number stated in the front matter that nobody reconciled against the body.

Vendor tier boundaries are still undefined, so the requirements that state targets by tier cannot yet be fully specified. This is deliberate: the boundaries follow from the vendor concentration profile, which is the first task in section 18.1, and inventing them now would be exactly the fabrication the prompt prohibits.

The three requirements with the highest remaining uncertainty. REQ-FUN-009, because no throughput has been demonstrated for taxonomy parsing on this data and the method constraint is derived from arithmetic rather than from a trial; the calibration run resolves it. REQ-DAT-007, because it weakens the manufacturer confirmation control to fit the no-lookup constraint, and whether a reference-entry confirmation is strong enough is not established; measuring vendor-attribution error in the ground truth sample resolves it. REQ-FUN-010, because the disposition of previously classified parts cannot be decided until the overlap is measured.

Answers that remain inconsistent. ASM-001 and ASM-002 assert a pre-deduplicated population of unique parts, which sits oddly with the known condition that source rows materially outnumber unique parts in this data; if the assumption is wrong, REQ-PRC-001 becomes load-bearing and the population figure changes. ADM is named as the consumer while the system of record is undesignated; these are compatible for a pilot and must be reconciled before production exit.

Known conditions not fully converted into requirements. The extent to which real values will fall outside the ADM vocabulary cannot be estimated until the source profile exists, so REQ-MOD-003 and REQ-GOV-004 handle the condition without sizing it. The long-tail yield condition is addressed by stratified sampling but its operational cost cannot be quantified until vendor concentration is profiled.

Whether the plan closes. It closes only on the four conditions in Appendix D.3. It does not close on the version 1.0 basis.
