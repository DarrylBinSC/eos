# AI-Assisted Part Taxonomy and ADM Attribute Derivation Requirements Document

## 1. Purpose, Scope, and How to Read This Document

### 1.1 Purpose

This document defines requirements for an AI-assisted capability that analyzes Wesco internal product taxonomy data and derives structured attributes required by Asset Data Manager (ADM).

The capability is intended to:

- increase the completeness and usefulness of ADM asset records;
- reduce manual data-enrichment effort; and
- accelerate onboarding of customer asset data.

The pilot population consists of 100,000 deduplicated unique part records and is targeted for completion within one month.

The resulting data will be consumed by ADM and potentially by Strev. The expected consumption model is primarily Wesco employees using the enriched data on behalf of customers.

### 1.2 Requirement conventions

Mandatory requirements use **shall**.

Desirable requirements use **should**.

Each requirement is assigned one of the following priorities:

| Priority | Meaning |
|---|---|
| Must | Required for acceptance of the applicable phase unless explicitly identified as dependent on an open item |
| Should | Desired and expected where practical, but not required for pilot acceptance |
| Could | Optional enhancement |
| Not this phase | Explicitly excluded from the current phase |

Requirement IDs use the format `REQ-<AREA>-<nnn>`.

Areas are:

| Code | Area |
|---|---|
| DAT | Data |
| FUN | Functional |
| MOD | Data model and conformance |
| EVD | Evidence, confidence, and trust |
| PRC | Process and workflow |
| QUA | Quality assurance and verification |
| REV | Human review and decision rights |
| NFR | Non-functional |
| INT | Interface and integration |
| GOV | Governance and change control |

Each requirement includes an acceptance criterion and verification method so the delivered capability can be objectively accepted or rejected.

---

## 2. Business Context and Objectives

ADM requires structured product information that is not consistently available in existing data.

The missing information limits ADM's ability to:

- identify hardware, software, and service products;
- identify software and license information;
- identify warranty information;
- support renewal-related activities;
- give Wesco employees a more complete view of customer assets; and
- support downstream managed services.

The current state reduces the business value ADM can provide because required attributes are missing and must otherwise be enriched manually.

The capability is intended to derive this information rapidly from existing Wesco internal product taxonomy data while maintaining sufficient evidence, control, repeatability, and auditability for the derived results to be trusted.

ADM is the primary consuming application.

Akansh Gangil, ADM Product Owner, is the owner of the consuming product and the acceptance authority for delivered output.

---

## 3. Definitions and Controlled Vocabulary

| Term | Definition |
|---|---|
| ADM | Asset Data Manager, the primary consumer of the derived data. |
| Internal product taxonomy | Wesco's internal taxonomy and related product data used as the source domain for this phase. |
| Unique part | A distinct Wesco part number. It is the unit of analysis for this capability. |
| Part-level fact | An attribute that belongs to the unique part and can be inherited by every occurrence of that part. |
| Transaction-level fact | A fact that applies to a particular customer, order, asset, or transaction rather than to the underlying part. |
| Hardware | A valid part classification within the ADM target model. |
| Software | For this phase, a software classification represents a software license rather than a service interaction. |
| Service | A product or offering involving an ongoing or performed interaction with the customer. |
| Extended warranty | Time-bound warranty coverage. |
| Support service | A service tied to interaction or service delivery involving the customer. |
| License term | A license-related term derivable from the taxonomy when supported by available evidence. |
| Warranty term | A warranty-related term derivable from the taxonomy when supported by available evidence. |
| Entitlement | Applicability to the pilot data is not yet established. `[OPEN: determine whether entitlement exists in the target data or target ADM model for this phase]` |
| Coverage | The proportion of eligible parts for which the capability produces a supported value for a derivation. |
| Accuracy | The proportion of evaluated derived values that agree with validated ground truth. |
| Vendor tier | A grouping of vendors based on part count per vendor. `[OPEN: define vendor-tier boundaries]` |
| Sourced fact | A value supported directly by part-specific source evidence. |
| Derived inference | A value produced by a validated rule or analytical method rather than read directly from part-specific source evidence. |
| Review flag | An explicit indicator that a record requires human review or business decision. |
| Unresolvable | A terminal processing state for a part that cannot be resolved from available evidence under the approved method. |
| Blank | Absence of a populated value. Blank does not mean `N/A`, `unknown`, zero, or a substitute value. |
| Controlled vocabulary | The approved ADM value set against which a derived value must conform before delivery. |

Controlled value lists currently identified as relevant are:

- Hardware, Software, and Service classification;
- warranty terms; and
- license terms.

`[OPEN: confirm the approval/sign-off status and exact allowed values of each controlled value list]`

---

## 4. In Scope and Out of Scope

### 4.1 In scope

The current phase includes:

- analysis of the Wesco internal product taxonomy;
- a pilot population of 100,000 deduplicated unique part numbers;
- classification of parts as Hardware, Software, or Service;
- derivation of warranty terms when discoverable from the taxonomy;
- derivation of license terms when discoverable from the taxonomy;
- use of vendor or brand reference data where applicable;
- use of SKU decoding rules where applicable;
- reuse of prior validated output where applicable;
- evidence capture;
- quality assurance;
- human review;
- export of resulting data in a file that ADM can import; and
- definition of a pilot exit gate.

The capability is intended to support an ongoing process after the pilot rather than only a one-time backfill.

### 4.2 Out of scope

The current phase excludes:

- transaction dates;
- pricing;
- quantities;
- contract data;
- attributes outside the ADM target attribute set; and
- transaction-level derivation of warranty start dates or comparable instance-specific dates.

Entitlement processing is not included unless its applicability is established during the pilot.

---

## 5. Assumptions, Constraints, and Dependencies

### 5.1 Assumptions register

| ID | Assumption |
|---|---|
| ASM-001 | The pilot population presented for analysis contains 100,000 records representing 100,000 unique part numbers. |
| ASM-002 | The pilot population has already been deduplicated before processing begins. |
| ASM-003 | ADM will consume the delivered results through file import. |
| ASM-004 | The AI Data team will operate the pilot process. |
| ASM-005 | Previously validated classifications, vendor or brand reference data, and SKU decoding rules may be reused when their applicability can be established. |
| ASM-006 | Data may potentially be consumed downstream by Strev, although ADM is the defined consumer for the pilot. |

### 5.2 Constraints register

| ID | Constraint |
|---|---|
| CON-001 | The pilot population is 100,000 unique parts. |
| CON-002 | The pilot target duration is one month. |
| CON-003 | Human review capacity is approximately 4 hours per week during the pilot. |
| CON-004 | A wrong derived value is considered more harmful than leaving a value blank. |
| CON-005 | Warranty and license terms are populated only when discoverable from the available taxonomy evidence. |
| CON-006 | The pilot is not a production deployment and must have an exit gate. |
| CON-007 | The AI Data team may select the AI platform or analytical tooling, subject to applicable Wesco data-handling constraints once defined. |

### 5.3 Dependencies register

| ID | Dependency |
|---|---|
| DEP-001 | `[OPEN: identify the 10 available source fields]` |
| DEP-002 | `[OPEN: determine completeness rate for each source field]` |
| DEP-003 | `[OPEN: determine distinct vendor count]` |
| DEP-004 | `[OPEN: determine percentage of parts associated with the top 10 vendors]` |
| DEP-005 | `[OPEN: determine number of vendors having fewer than five parts]` |
| DEP-006 | `[OPEN: define vendor-tier boundaries]` |
| DEP-007 | `[OPEN: confirm ADM controlled vocabulary values and sign-off status]` |
| DEP-008 | `[OPEN: define required accuracy target for each derivation and vendor tier]` |
| DEP-009 | `[OPEN: define acceptable downstream defect threshold]` |
| DEP-010 | `[OPEN: define independent-QA disagreement threshold]` |
| DEP-011 | `[OPEN: define the working-data location]` |
| DEP-012 | `[OPEN: designate the system of record]` |
| DEP-013 | `[OPEN: document sanctioned AI platform and data-handling constraints]` |
| DEP-014 | `[OPEN: define retention requirements]` |
| DEP-015 | `[OPEN: define access-control roles]` |
| DEP-016 | `[OPEN: define cost target or cost constraint]` |
| DEP-017 | `[OPEN: define rule-validation threshold and approving role]` |
| DEP-018 | `[OPEN: define pilot exit-gate approval authority if different from ADM output acceptance authority]` |

---

## 6. Data Requirements

| ID | Requirement | Priority | Acceptance criterion | Verification method |
|---|---|---|---|---|
| REQ-DAT-001 | The solution shall use the unique part number as the unit of analysis. | Must | Each pilot record is processed and reported against one unique part identifier. | Test |
| REQ-DAT-002 | The solution shall preserve each source part number as supplied and shall not change its meaning through numeric or format coercion. | Must | Structured alphanumeric, numeric, and custom part-number forms round-trip through the process without semantic alteration. | Test |
| REQ-DAT-003 | The solution shall produce a completeness profile for every available source field before derivation begins. | Must | A completeness result exists for each of the `[OPEN: 10 source fields]`. | Inspection |
| REQ-DAT-004 | The solution shall normalize vendor strings to a canonical vendor or brand representation before vendor-based grouping is performed. | Must | Equivalent vendor strings used in the pilot are mapped to a documented canonical representation before vendor grouping. | Test |
| REQ-DAT-005 | The solution shall treat the source vendor field as unverified input. | Must | No vendor-dependent derivation is represented as verified solely because a vendor value exists in the source record. | Test |
| REQ-DAT-006 | The solution shall confirm manufacturer identity from part-specific evidence or a validated rule before manufacturer identity is used to select a derivation rule. | Must | In the quality sample, zero records use an unconfirmed manufacturer identity to select a derivation rule. | Test |
| REQ-DAT-007 | The solution shall quarantine records identified as junk or non-product data before attribute derivation begins. | Must | Records designated as junk or non-product data are absent from the active derivation population and are identifiable in a quarantine population. | Test |
| REQ-DAT-008 | The solution shall validate an input layout against an explicit field mapping before processing that population. | Must | Processing does not begin for an input population until the input fields have been mapped to the expected schema. | Demonstration |
| REQ-DAT-009 | The solution shall not infer header position or field meaning from an arbitrary source layout without explicit validation. | Must | A deliberately altered input layout is rejected or routed for mapping rather than silently processed using an inferred schema. | Test |

---

## 7. Functional Requirements: Derivation and Classification

| ID | Requirement | Priority | Acceptance criterion | Verification method |
|---|---|---|---|---|
| REQ-FUN-001 | The solution shall derive a part classification of Hardware, Software, or Service when the available evidence supports one of those values. | Must | Every populated part classification is one of the approved values and is supported by recorded evidence. | Test |
| REQ-FUN-002 | The solution shall apply the defined Software and Service boundary when classifying a part. | Must | Test cases representing a software license and a customer-interaction service are classified according to the definitions in Section 3. | Test |
| REQ-FUN-003 | The solution shall derive a warranty term only when that warranty term is discoverable from the available taxonomy evidence. | Must | No populated warranty term lacks supporting taxonomy evidence or a validated derivation rule. | Test |
| REQ-FUN-004 | The solution shall derive a license term only when that license term is discoverable from the available taxonomy evidence. | Must | No populated license term lacks supporting taxonomy evidence or a validated derivation rule. | Test |
| REQ-FUN-005 | The solution shall state a separate coverage target and accuracy target for each derivation by vendor tier. | Must | Part classification, warranty-term derivation, and license-term derivation each have separate coverage and accuracy targets for every defined vendor tier. Targets remain `[OPEN: values]` until approved. | Inspection |
| REQ-FUN-006 | The solution shall report measured coverage separately from measured accuracy. | Must | Results contain separate coverage and measured-accuracy fields and do not present one blended figure as the quality measure for a derivation. | Inspection |
| REQ-FUN-007 | The solution shall reuse previously validated part-level results when the same unique part is encountered again. | Must | A previously validated part is not unnecessarily re-derived when the existing result remains valid under the current rule and model versions. | Test |
| REQ-FUN-008 | The solution shall permit an approved classification or vocabulary value to have zero observed instances in a population. | Must | A test population containing no examples of an approved value reports zero observations without assigning records to that value merely to populate the category. | Test |

---

## 8. Data Model and Conformance Requirements

| ID | Requirement | Priority | Acceptance criterion | Verification method |
|---|---|---|---|---|
| REQ-MOD-001 | The solution shall map populated controlled attributes only to values contained in the applicable approved ADM controlled value list. | Must | Zero delivered controlled attributes contain a value outside the applicable approved list. | Test |
| REQ-MOD-002 | The solution shall leave an attribute blank when the available evidence does not support a value. | Must | Test records with insufficient evidence contain a blank target value. | Test |
| REQ-MOD-003 | The solution shall leave a controlled attribute blank when an observed value cannot be mapped to the applicable controlled vocabulary. | Must | Non-conforming values are not coerced to the nearest approved value. | Test |
| REQ-MOD-004 | The solution shall flag every source value that cannot be mapped to the applicable controlled vocabulary. | Must | Each unmapped observed value is represented in the non-conformance output with the original observed value. | Test |
| REQ-MOD-005 | The solution shall represent blank as an empty value rather than `N/A`, `unknown`, or zero. | Must | Test records with unresolved attributes contain no placeholder value in the target field. | Test |
| REQ-MOD-006 | The solution shall model warranty and licensing attributes as global part attributes rather than as fields conditional on the part's category. | Must | A hardware part can carry applicable warranty or licensing attributes without violating the output schema. | Test |
| REQ-MOD-007 | The solution shall store part-level facts separately from transaction-level facts. | Must | Part-level output contains no transaction-specific date, price, quantity, or contract value. | Inspection |
| REQ-MOD-008 | The solution shall not derive a warranty start date as a property of the unique part. | Must | No unique-part output includes a warranty start date derived as an intrinsic part attribute. | Test |

---

## 9. Evidence, Confidence, and Trust Requirements

| ID | Requirement | Priority | Acceptance criterion | Verification method |
|---|---|---|---|---|
| REQ-EVD-001 | The solution shall distinguish sourced facts from derived inferences for every populated derived attribute. | Must | Every populated result identifies whether its evidence class is sourced fact or derived inference. | Test |
| REQ-EVD-002 | The solution shall record evidence provenance for every populated derived attribute. | Must | Each populated derived attribute has a source identifier or rule identifier sufficient to identify the evidence used. | Inspection |
| REQ-EVD-003 | The solution shall record a confidence value or confidence band for every derived inference. | Must | No derived inference lacks a recorded confidence value or confidence band. | Test |
| REQ-EVD-004 | The solution shall record the applicable review flag for every processed unique part. | Must | Every processed part contains an explicit review state rather than requiring review status to be inferred. | Inspection |
| REQ-EVD-005 | The solution shall record the rule, prompt, or model version responsible for each derived inference. | Must | Each derived inference can be traced to the version that produced it. | Inspection |
| REQ-EVD-006 | The solution shall record the processing timestamp associated with each derived inference. | Must | Every derived inference contains a processing timestamp. | Inspection |
| REQ-EVD-007 | The solution shall require part-specific evidence or a validated derivation rule before treating a value as supported. | Must | Evidence naming only a general product family, vendor homepage, or non-part-specific source does not by itself satisfy the support criterion. | Test |

---

## 10. Process and Workflow Requirements

| ID | Requirement | Priority | Acceptance criterion | Verification method |
|---|---|---|---|---|
| REQ-PRC-001 | The solution shall derive a part-level fact once for a unique part and make that result reusable by subsequent occurrences of that part. | Must | Repeated occurrences of the same part inherit the validated part-level result rather than creating independent conflicting facts. | Test |
| REQ-PRC-002 | The solution shall record processing state explicitly in the data. | Must | The current processing state of every part can be determined by reading recorded state fields without reconstructing state from external history. | Inspection |
| REQ-PRC-003 | The solution shall permit each processing stage to be rerun without duplicating completed work. | Must | Re-executing a completed stage produces no duplicate derived records. | Test |
| REQ-PRC-004 | The solution shall permit each processing stage to be rerun without corrupting previously validated results. | Must | Re-executing a completed stage preserves previously validated results unless a controlled version change explicitly requires reprocessing. | Test |
| REQ-PRC-005 | The solution shall process work in bounded units that are checkpointed before the next unit begins. | Must | An interrupted processing run retains the most recently completed checkpoint rather than losing all work since run start. | Demonstration |
| REQ-PRC-006 | The solution shall verify persistence after writing a checkpoint or committed result. | Must | A simulated persistence failure is detected rather than reported as a successful save. | Demonstration |
| REQ-PRC-007 | The solution shall treat Unresolvable as a terminal analytical state. | Must | A part marked Unresolvable does not automatically re-enter the analysis queue without a new business decision or material evidence change. | Test |
| REQ-PRC-008 | The solution shall route Unresolvable parts to a recorded business-decision path. | Must | Every Unresolvable part has a recorded disposition or decision status outside the normal derivation queue. | Inspection |
| REQ-PRC-009 | The solution shall produce immutable, versioned delivered output for each delivery event. | Must | A delivered output version can be retrieved and compared with a later version without the earlier version having been overwritten. | Demonstration |

---

## 11. Quality Assurance and Verification Requirements

| ID | Requirement | Priority | Acceptance criterion | Verification method |
|---|---|---|---|---|
| REQ-QUA-001 | The solution shall measure the accuracy of a derivation rule against human-validated ground truth not used to build or tune that rule. | Must | The validation sample is documented as independent from the rule-development sample. | Inspection |
| REQ-QUA-002 | The solution shall prevent automatic completion by a derivation rule until the rule achieves `[OPEN: accuracy threshold]` and is approved by `[OPEN: approving role]`. | Must | A rule below the approved threshold or lacking approval cannot automatically complete records. | Test |
| REQ-QUA-003 | The quality process shall include at least one validation method capable of disagreeing with the primary derivation method. | Must | The quality method uses a materially different input signal, method, or frame from the primary derivation. | Demonstration |
| REQ-QUA-004 | The independent quality method shall report disagreement rate rather than substituting its answer as a second authoritative classification. | Must | Quality results report disagreement by attribute and vendor tier. | Inspection |
| REQ-QUA-005 | The solution shall withhold automatic completion for an attribute when independent disagreement exceeds `[OPEN: disagreement threshold]`. | Must | A test population exceeding the threshold does not pass automatic completion for that attribute. | Test |
| REQ-QUA-006 | The solution shall run deterministic conformance checks against every delivered record. | Must | Every delivered record has passed the defined deterministic conformance checks. | Test |
| REQ-QUA-007 | The solution shall block delivery when a deterministic conformance check fails. | Must | A deliberately malformed or non-conforming test record prevents the affected delivery from receiving a passing verdict. | Demonstration |
| REQ-QUA-008 | The solution shall perform structural-integrity validation of the write and export path separately from content validation. | Must | A structural corruption test is detected even when the semantic attribute values themselves are valid. | Test |
| REQ-QUA-009 | Quality sampling shall be stratified by vendor tier, attribute, confidence band, and derivation method. | Must | The quality sample report identifies representation across all four dimensions. | Inspection |
| REQ-QUA-010 | Quality sampling shall oversample long-tail vendors and low-confidence results relative to their population share. | Must | The sample design demonstrates higher sampling intensity for the long tail and low-confidence band than their unadjusted population share. | Analysis |
| REQ-QUA-011 | The solution shall measure downstream defect rate against `[OPEN: acceptable downstream defect threshold]`. | Must | The downstream defect report states the measured rate and compares it with the approved threshold. | Analysis |

---

## 12. Human Review and Decision Rights Requirements

| ID | Requirement | Priority | Acceptance criterion | Verification method |
|---|---|---|---|---|
| REQ-REV-001 | The process shall prefer a blank, flagged result over a derived value that does not meet the approved evidence or confidence standard. | Must | Records below the approved standard remain blank and flagged rather than being populated with a plausible value. | Test |
| REQ-REV-002 | The pilot review workload shall not exceed 4 hours per week without reporting a capacity breach. | Must | Weekly review effort at or below 4 hours is within capacity; any excess is explicitly recorded as a breach. | Analysis |
| REQ-REV-003 | The permitted review flag rate shall be derived from measured review effort and the 4-hour weekly review capacity. | Must | The pilot reports the observed review effort and the resulting sustainable flag rate rather than adopting an unsupported flag-rate target. | Analysis |
| REQ-REV-004 | The process shall not lower a review threshold solely to keep the review queue within capacity. | Must | A capacity breach results in an explicit reported exception rather than an undocumented reduction in the flagging standard. | Inspection |
| REQ-REV-005 | A human review decision that establishes a generally applicable interpretation shall be incorporated into rules or reference data. | Must | A repeated future case subject to the same general decision is handled by the updated rule or reference data rather than requiring the identical manual decision again. | Demonstration |
| REQ-REV-006 | Akansh Gangil, as ADM Product Owner, shall provide acceptance of the delivered ADM output for the pilot. | Must | Pilot output has a recorded acceptance or rejection decision from the ADM Product Owner. | Inspection |

---

## 13. Non-Functional Requirements

| ID | Requirement | Priority | Acceptance criterion | Verification method |
|---|---|---|---|---|
| REQ-NFR-001 | The pilot solution shall process the 100,000-part pilot population within one month. | Must | The complete pilot processing period does not exceed one month. | Analysis |
| REQ-NFR-002 | The solution shall support repeated processing of new part populations after the initial pilot. | Must | A subsequent population can be processed without rebuilding the processing method from the beginning. | Demonstration |
| REQ-NFR-003 | The AI Data team shall document the selected AI or analytical platform and applicable data-handling constraints before pilot data is submitted to that platform. | Must | The selected platform and applicable constraints are recorded before processing begins. | Inspection |
| REQ-NFR-004 | Pilot working data shall reside in `[OPEN: approved working-data location]`. | Must | Inspection confirms that working data is stored only in the approved location. | Inspection |
| REQ-NFR-005 | Access to pilot working data and derived output shall be restricted to `[OPEN: approved roles or access groups]`. | Must | Access-control configuration corresponds to the approved role list. | Inspection |
| REQ-NFR-006 | Pilot data and evidence shall be retained for `[OPEN: retention period]`. | Must | Records remain retrievable for the approved retention period. | Inspection |
| REQ-NFR-007 | The process shall provide an auditable history sufficient to trace a delivered value to its source or rule, processing version, confidence, review state, and processing time. | Must | A sampled delivered value can be traced through the recorded evidence and processing history. | Demonstration |
| REQ-NFR-008 | Pilot operating cost shall be measured against `[OPEN: pilot cost target or cost constraint]`. | Should | Actual pilot operating cost is reported against the approved target when a target has been established. | Analysis |

---

## 14. Interface and Integration Requirements

| ID | Requirement | Priority | Acceptance criterion | Verification method |
|---|---|---|---|---|
| REQ-INT-001 | The solution shall export derived pilot results in a file that ADM can import. | Must | ADM successfully imports the pilot output file without manual reconstruction of the derived data. | Demonstration |
| REQ-INT-002 | The exported result shall conform to the applicable ADM global attribute structure on P360. | Must | Exported fields map to the approved ADM global attribute structure without category-specific nesting of global attributes. | Test |
| REQ-INT-003 | The delivery process shall preserve the unique part identifier used to associate the enriched result with the corresponding ADM part. | Must | Every imported result can be reconciled to the unique part that produced it. | Test |
| REQ-INT-004 | The system of record shall be designated before the pilot exits to production use. | Must | `[OPEN: system of record]` is formally identified before a production exit decision is approved. | Inspection |

---

## 15. Governance and Change Control Requirements

| ID | Requirement | Priority | Acceptance criterion | Verification method |
|---|---|---|---|---|
| REQ-GOV-001 | Rules, prompts, and models used to derive pilot results shall be versioned. | Must | Every active rule, prompt, and model has a retrievable version identifier. | Inspection |
| REQ-GOV-002 | A material change to a rule, prompt, or model shall trigger re-validation of affected results produced under the prior version. | Must | Change records identify the affected prior population and its re-validation disposition. | Inspection |
| REQ-GOV-003 | A regression set shall be executed before a changed rule, prompt, or model is adopted. | Must | No controlled change is adopted without a recorded regression result. | Test |
| REQ-GOV-004 | Recurring controlled-vocabulary non-conformance shall be escalated for a business decision on vocabulary extension. | Must | Repeated unmapped source values appear in a governance review queue rather than being silently coerced. | Inspection |
| REQ-GOV-005 | The quality process shall support a failing verdict. | Must | The pilot quality decision can explicitly result in Fail rather than requiring every run to pass. | Demonstration |
| REQ-GOV-006 | A failing verdict shall have a documented consequence before pilot exit. | Must | `[OPEN: consequence of a failing verdict]` is recorded before the exit-gate decision. | Inspection |
| REQ-GOV-007 | Quality follow-up actions shall have an owner and due date. | Must | Every unresolved follow-up accepted at a quality gate has both an identified owner and due date. | Inspection |
| REQ-GOV-008 | The pilot shall have a documented exit-gate decision before being treated as a production capability. | Must | The pilot has a recorded Pass, Pass with follow-ups, or Fail decision before production use. | Inspection |
| REQ-GOV-009 | The pilot exit-gate decision shall be approved by `[OPEN: pilot exit-gate approval authority]`. | Must | The exit-gate record contains the required approval. | Inspection |

---

## 16. Acceptance Criteria and Phase Exit Conditions

### 16.1 Acceptance approach

Pilot acceptance is based on objective evidence from the requirements in Sections 6 through 15.

The available verdicts are:

| Verdict | Meaning |
|---|---|
| Pass | Required pilot criteria are satisfied and no unresolved condition prevents exit. |
| Pass with follow-ups | Required pilot criteria permit exit, with identified follow-up work recorded with an owner and due date. |
| Fail | One or more required conditions prevent pilot exit. |

### 16.2 Pilot exit conditions

The pilot exit gate requires the following conditions:

| Exit condition | Supporting requirements | Current state |
|---|---|---|
| 100,000 unique parts can be processed within one month | REQ-NFR-001 | Defined |
| ADM can import the delivered output file | REQ-INT-001 | Defined |
| Hardware, Software, and Service classification is measured against approved coverage and accuracy targets | REQ-FUN-001, REQ-FUN-005, REQ-FUN-006 | `[OPEN: targets and vendor tiers]` |
| Warranty-term derivation is measured against approved coverage and accuracy targets | REQ-FUN-003, REQ-FUN-005 | `[OPEN: targets and vendor tiers]` |
| License-term derivation is measured against approved coverage and accuracy targets | REQ-FUN-004, REQ-FUN-005 | `[OPEN: targets and vendor tiers]` |
| Independent QA disagreement remains within the approved threshold | REQ-QUA-003 through REQ-QUA-005 | `[OPEN: disagreement threshold]` |
| Deterministic content and structural checks pass | REQ-QUA-006 through REQ-QUA-008 | Defined |
| Human review workload is compatible with 4 hours per week | REQ-REV-002, REQ-REV-003 | Threshold methodology defined; sustainable record rate to be measured |
| Downstream defect rate is within the approved tolerance | REQ-QUA-011 | `[OPEN: defect threshold]` |
| ADM Product Owner accepts the delivered output | REQ-REV-006 | Defined |
| Required working-data, security, access, and retention decisions are documented | REQ-NFR-003 through REQ-NFR-006 | Open dependencies |
| System of record is designated before production exit | REQ-INT-004 | `[OPEN]` |
| Pilot has a recorded exit-gate verdict | REQ-GOV-008, REQ-GOV-009 | Approval authority open |

---

## 17. Risk Register

| Risk ID | Risk | Consequence | Mitigating requirements |
|---|---|---|---|
| RSK-001 | Incorrect vendor value is treated as authoritative | Incorrect derivation rule is applied at scale | REQ-DAT-004, REQ-DAT-005, REQ-DAT-006 |
| RSK-002 | Vendor naming variations fragment one vendor into multiple groups | Reduced rule reuse and unreliable vendor-level reporting | REQ-DAT-004 |
| RSK-003 | Weak evidence is accepted for a derived value | Incorrect values appear credible and require remediation | REQ-EVD-002, REQ-EVD-007 |
| RSK-004 | Software licenses are misclassified as services | ADM classification and downstream use are incorrect | REQ-FUN-001, REQ-FUN-002 |
| RSK-005 | Unverifiable values are filled with plausible answers | Incorrect data is delivered instead of an explicit data gap | REQ-MOD-002, REQ-REV-001 |
| RSK-006 | Real source values fall outside the ADM vocabulary | Values are silently distorted to fit an enum | REQ-MOD-003, REQ-MOD-004, REQ-GOV-004 |
| RSK-007 | Quality checking is correlated with the derivation method | QA confirms the original method rather than testing it | REQ-QUA-003, REQ-QUA-004, REQ-QUA-005 |
| RSK-008 | Structural corruption occurs during export or write | Valid content becomes mechanically corrupted without detection | REQ-QUA-008 |
| RSK-009 | A save reports success but data is not persisted | Completed work is lost | REQ-PRC-005, REQ-PRC-006 |
| RSK-010 | Long-running work is committed only at completion | A failure near the end loses significant completed work | REQ-PRC-005 |
| RSK-011 | Review backlog exceeds available capacity | Review controls are weakened to maintain throughput | REQ-REV-002, REQ-REV-003, REQ-REV-004 |
| RSK-012 | Process state is inferred instead of explicitly stored | Progress and remaining work cannot be reliably determined | REQ-PRC-002 |
| RSK-013 | Re-running processing duplicates or corrupts prior results | Ongoing operations become unreliable | REQ-PRC-003, REQ-PRC-004 |
| RSK-014 | Previously classified parts are repeatedly re-derived | Unit cost and effort remain unnecessarily high | REQ-FUN-007, REQ-PRC-001 |
| RSK-015 | Long-tail vendors are underrepresented in validation | Reported accuracy overstates actual performance on difficult parts | REQ-QUA-009, REQ-QUA-010 |
| RSK-016 | Junk or non-product records consume analysis effort | Pilot effort is spent on data that cannot create ADM value | REQ-DAT-007 |
| RSK-017 | Custom or non-resolvable parts remain indefinitely in the queue | Processing effort is repeatedly spent without additional information | REQ-PRC-007, REQ-PRC-008 |
| RSK-018 | A controlled category with zero examples is incorrectly forced into the output | Classification results are distorted | REQ-FUN-008 |
| RSK-019 | Source-layout variation is parsed incorrectly | Records can be silently mapped to incorrect fields | REQ-DAT-008, REQ-DAT-009 |
| RSK-020 | A rule change causes regression in previously valid classifications | New releases silently reduce quality | REQ-GOV-001, REQ-GOV-002, REQ-GOV-003 |
| RSK-021 | Pilot results are treated as production-ready without a formal gate | Unresolved quality or operating gaps enter production | REQ-GOV-008, REQ-GOV-009 |
| RSK-022 | Customer, order, or asset dates are represented as intrinsic part facts | ADM contains semantically incorrect part-level information | REQ-MOD-007, REQ-MOD-008 |

---

# Appendix A: ADM Global Attribute Conformance Matrix

| ADM attribute | Scope this phase | Unit | Derivation basis | Controlled vocabulary status | Blank policy | Notes |
|---|---|---|---|---|---|---|
| Part classification | In scope | Unique part | Internal product taxonomy and validated supporting rules/reference data | Hardware, Software, Service identified; `[OPEN: confirm sign-off status]` | Blank and flag when unsupported | Software and Service boundary defined in Section 3 |
| Warranty term | In scope when discoverable | Unique part | Internal product taxonomy | `[OPEN: exact values and sign-off status]` | Blank and flag when unsupported | No warranty start date at part level |
| License term | In scope when discoverable | Unique part | Internal product taxonomy | `[OPEN: exact values and sign-off status]` | Blank and flag when unsupported | Global attribute, not conditional on Software classification |
| Warranty start date | Not this phase as a part-level attribute | Transaction or asset instance | Not applicable to unique-part derivation | Not applicable | Not populated | Belongs to the instance or transaction layer |
| Transaction dates | Not this phase | Transaction | Not applicable | Not applicable | Not populated | Explicitly out of scope |
| Price | Not this phase | Transaction | Not applicable | Not applicable | Not populated | Explicitly out of scope |
| Quantity | Not this phase | Transaction | Not applicable | Not applicable | Not populated | Explicitly out of scope |
| Contract data | Not this phase | Transaction or contract | Not applicable | Not applicable | Not populated | Explicitly out of scope |
| Entitlement | `[OPEN: determine applicability]` | `[OPEN]` | `[OPEN]` | `[OPEN]` | Not populated unless brought into scope | Applicability not established |

---

# Appendix B: Requirement Traceability Matrix

| ID | Objective | Priority | Acceptance criterion | Verification | Status |
|---|---|---|---|---|---|
| REQ-DAT-001 | Analyze at unique-part grain | Must | One processing record per unique part | Test | Defined |
| REQ-DAT-002 | Preserve part-number semantics | Must | Mixed part-number formats survive unchanged | Test | Defined |
| REQ-DAT-003 | Establish source completeness | Must | Completeness reported for every source field | Inspection | Open dependency |
| REQ-DAT-004 | Normalize vendor identity | Must | Equivalent vendor names map canonically | Test | Defined |
| REQ-DAT-005 | Prevent trust in raw vendor field | Must | Vendor presence alone never constitutes verification | Test | Defined |
| REQ-DAT-006 | Confirm manufacturer before vendor rules | Must | No vendor rule uses unconfirmed manufacturer | Test | Defined |
| REQ-DAT-007 | Remove junk from analysis queue | Must | Quarantined records excluded from derivation | Test | Defined |
| REQ-DAT-008 | Validate source mapping | Must | Explicit mapping exists before processing | Demonstration | Defined |
| REQ-DAT-009 | Prevent silent layout inference | Must | Altered layouts are rejected or remapped | Test | Defined |
| REQ-FUN-001 | Classify product type | Must | Populated values are Hardware, Software, or Service | Test | Defined |
| REQ-FUN-002 | Apply category boundaries | Must | Boundary test cases conform to definitions | Test | Defined |
| REQ-FUN-003 | Derive supported warranty term | Must | Every value has supporting evidence | Test | Defined |
| REQ-FUN-004 | Derive supported license term | Must | Every value has supporting evidence | Test | Defined |
| REQ-FUN-005 | Establish coverage and accuracy targets | Must | Separate targets by derivation and vendor tier | Inspection | Open dependency |
| REQ-FUN-006 | Separate coverage from accuracy reporting | Must | No blended quality figure | Inspection | Defined |
| REQ-FUN-007 | Reuse validated prior results | Must | Valid prior results are reused | Test | Defined |
| REQ-FUN-008 | Permit zero-instance categories | Must | Zero remains zero without forced assignment | Test | Defined |
| REQ-MOD-001 | Enforce controlled values | Must | No non-approved populated values | Test | Open dependency |
| REQ-MOD-002 | Leave unsupported values blank | Must | Insufficient evidence produces blank | Test | Defined |
| REQ-MOD-003 | Prevent vocabulary coercion | Must | Unmapped source value remains unmapped | Test | Defined |
| REQ-MOD-004 | Capture vocabulary non-conformance | Must | Every unmapped value is reported | Test | Defined |
| REQ-MOD-005 | Standardize blank representation | Must | No placeholder value represents blank | Test | Defined |
| REQ-MOD-006 | Preserve global ADM attributes | Must | Global fields are not nested by category | Test | Defined |
| REQ-MOD-007 | Separate part and transaction facts | Must | No excluded transaction facts in part output | Inspection | Defined |
| REQ-MOD-008 | Keep warranty start date off unique part | Must | No intrinsic warranty start date produced | Test | Defined |
| REQ-EVD-001 | Distinguish evidence classes | Must | Evidence class exists for populated results | Test | Defined |
| REQ-EVD-002 | Capture provenance | Must | Source or rule identifier exists | Inspection | Defined |
| REQ-EVD-003 | Capture confidence | Must | Confidence exists for every inference | Test | Defined |
| REQ-EVD-004 | Record review state | Must | Explicit review state exists | Inspection | Defined |
| REQ-EVD-005 | Record production version | Must | Result traces to rule, prompt, or model version | Inspection | Defined |
| REQ-EVD-006 | Record processing time | Must | Timestamp exists | Inspection | Defined |
| REQ-EVD-007 | Require part-specific support | Must | Weak general evidence does not qualify | Test | Defined |
| REQ-PRC-001 | Reuse part-level facts | Must | Duplicate occurrences inherit validated result | Test | Defined |
| REQ-PRC-002 | Make process state explicit | Must | State readable directly from data | Inspection | Defined |
| REQ-PRC-003 | Make rerun duplicate-safe | Must | No duplicates after rerun | Test | Defined |
| REQ-PRC-004 | Make rerun corruption-safe | Must | Valid results survive rerun | Test | Defined |
| REQ-PRC-005 | Checkpoint bounded work | Must | Interrupted work retains completed checkpoint | Demonstration | Defined |
| REQ-PRC-006 | Verify persistence | Must | Failed persistence is detected | Demonstration | Defined |
| REQ-PRC-007 | Terminate unresolvable analysis | Must | Unresolvable does not loop automatically | Test | Defined |
| REQ-PRC-008 | Route unresolvable to business decision | Must | Disposition path exists | Inspection | Defined |
| REQ-PRC-009 | Preserve delivered versions | Must | Prior delivery remains retrievable | Demonstration | Defined |
| REQ-QUA-001 | Validate against independent ground truth | Must | Validation sample excluded from development | Inspection | Defined |
| REQ-QUA-002 | Gate auto-completion | Must | Unapproved or below-threshold rules cannot auto-complete | Test | Open dependency |
| REQ-QUA-003 | Use disagreeing QA frame | Must | QA method materially differs from primary method | Demonstration | Defined |
| REQ-QUA-004 | Measure disagreement | Must | Disagreement reported by attribute and tier | Inspection | Defined |
| REQ-QUA-005 | Act on excess disagreement | Must | Excess disagreement blocks auto-completion | Test | Open dependency |
| REQ-QUA-006 | Run deterministic checks | Must | Every record passes checks | Test | Defined |
| REQ-QUA-007 | Block failed delivery | Must | Failed conformance prevents pass | Demonstration | Defined |
| REQ-QUA-008 | Check structural integrity separately | Must | Mechanical corruption is independently detected | Test | Defined |
| REQ-QUA-009 | Stratify sampling | Must | Sample covers required dimensions | Inspection | Open dependency |
| REQ-QUA-010 | Oversample difficult segments | Must | Long tail and low confidence sampled more heavily | Analysis | Defined |
| REQ-QUA-011 | Measure downstream defects | Must | Measured rate compared with approved threshold | Analysis | Open dependency |
| REQ-REV-001 | Prefer blank to wrong | Must | Unsupported values remain blank and flagged | Test | Defined |
| REQ-REV-002 | Respect review capacity | Must | Capacity breach reported above 4 hours/week | Analysis | Defined |
| REQ-REV-003 | Derive sustainable flag rate | Must | Flag rate tied to measured review effort | Analysis | Open until pilot measurement |
| REQ-REV-004 | Prevent capacity-driven quality reduction | Must | Threshold is not silently lowered | Inspection | Defined |
| REQ-REV-005 | Reuse general human decisions | Must | General decisions become rules/reference data | Demonstration | Defined |
| REQ-REV-006 | Obtain ADM acceptance | Must | ADM Product Owner records acceptance decision | Inspection | Defined |
| REQ-NFR-001 | Meet pilot throughput | Must | 100,000 parts within one month | Analysis | Defined |
| REQ-NFR-002 | Support ongoing use | Must | Subsequent population can be processed | Demonstration | Defined |
| REQ-NFR-003 | Establish sanctioned tool handling | Must | Tool and constraints documented before use | Inspection | Open dependency |
| REQ-NFR-004 | Use approved storage | Must | Working data stored in approved location | Inspection | Open dependency |
| REQ-NFR-005 | Restrict access | Must | Access matches approved roles | Inspection | Open dependency |
| REQ-NFR-006 | Apply retention policy | Must | Data retained for approved duration | Inspection | Open dependency |
| REQ-NFR-007 | Maintain auditability | Must | Sample result traces end to end | Demonstration | Defined |
| REQ-NFR-008 | Measure cost | Should | Cost compared with target | Analysis | Open dependency |
| REQ-INT-001 | Deliver importable ADM file | Must | ADM successfully imports output | Demonstration | Defined |
| REQ-INT-002 | Conform to ADM structure | Must | Output maps to global ADM schema | Test | Open dependency |
| REQ-INT-003 | Preserve reconciliation identifier | Must | Each result matches unique part | Test | Defined |
| REQ-INT-004 | Designate system of record | Must | System identified before production exit | Inspection | Open dependency |
| REQ-GOV-001 | Version analytical assets | Must | Version identifier exists | Inspection | Defined |
| REQ-GOV-002 | Revalidate after changes | Must | Affected prior results receive disposition | Inspection | Defined |
| REQ-GOV-003 | Run regression before adoption | Must | Regression result recorded | Test | Defined |
| REQ-GOV-004 | Govern vocabulary gaps | Must | Recurring gaps reach governance queue | Inspection | Defined |
| REQ-GOV-005 | Permit Fail verdict | Must | Quality process can return Fail | Demonstration | Defined |
| REQ-GOV-006 | Define consequence of failure | Must | Consequence documented | Inspection | Open dependency |
| REQ-GOV-007 | Govern follow-up work | Must | Owner and due date assigned | Inspection | Defined |
| REQ-GOV-008 | Require pilot exit gate | Must | Exit verdict recorded before production | Inspection | Defined |
| REQ-GOV-009 | Require exit approval | Must | Required approver records decision | Inspection | Open dependency |

---

# Appendix C: Open Items Register

| Open item | Question / decision required | Related requirements |
|---|---|---|
| OPEN-001 | What are the 10 source fields available on each pilot record? | REQ-DAT-003 |
| OPEN-002 | What is the completeness rate of each source field? | REQ-DAT-003 |
| OPEN-003 | How many distinct vendors occur in the pilot? | REQ-FUN-005, REQ-QUA-009 |
| OPEN-004 | What percentage of parts is associated with the top 10 vendors? | REQ-FUN-005, REQ-QUA-009, REQ-QUA-010 |
| OPEN-005 | How many vendors have fewer than five parts? | REQ-FUN-005, REQ-QUA-009, REQ-QUA-010 |
| OPEN-006 | What vendor-tier boundaries will be used? | REQ-FUN-005, REQ-QUA-004, REQ-QUA-009 |
| OPEN-007 | What is the sign-off status and exact value set for the Hardware, Software, and Service classification? | REQ-MOD-001, REQ-INT-002 |
| OPEN-008 | What is the sign-off status and exact value set for warranty terms? | REQ-MOD-001, REQ-INT-002 |
| OPEN-009 | What is the sign-off status and exact value set for license terms? | REQ-MOD-001, REQ-INT-002 |
| OPEN-010 | What is the required accuracy target for part classification by vendor tier? | REQ-FUN-005, REQ-QUA-002 |
| OPEN-011 | What is the required accuracy target for warranty-term derivation by vendor tier? | REQ-FUN-005, REQ-QUA-002 |
| OPEN-012 | What is the required accuracy target for license-term derivation by vendor tier? | REQ-FUN-005, REQ-QUA-002 |
| OPEN-013 | What is the required coverage target for part classification by vendor tier? | REQ-FUN-005 |
| OPEN-014 | What is the required coverage target for warranty-term derivation by vendor tier? | REQ-FUN-005 |
| OPEN-015 | What is the required coverage target for license-term derivation by vendor tier? | REQ-FUN-005 |
| OPEN-016 | What independent-QA disagreement threshold is acceptable? | REQ-QUA-005 |
| OPEN-017 | What downstream defect rate is acceptable for the pilot? | REQ-QUA-011 |
| OPEN-018 | What rule-validation accuracy threshold is required before automatic completion? | REQ-QUA-002 |
| OPEN-019 | Which role approves a derivation rule for automatic completion? | REQ-QUA-002 |
| OPEN-020 | Where will pilot working data reside? | REQ-NFR-004 |
| OPEN-021 | What is the authoritative system of record? | REQ-INT-004 |
| OPEN-022 | Which AI or analytical platforms are sanctioned and what data-handling restrictions apply? | REQ-NFR-003 |
| OPEN-023 | Which roles or access groups may access the working data and output? | REQ-NFR-005 |
| OPEN-024 | What retention period applies to pilot data, evidence, and output? | REQ-NFR-006 |
| OPEN-025 | Is there a pilot cost target or cost constraint? | REQ-NFR-008 |
| OPEN-026 | What is the defined consequence when the quality verdict is Fail? | REQ-GOV-006 |
| OPEN-027 | Who approves the pilot exit gate if that authority differs from ADM output acceptance? | REQ-GOV-009 |
| OPEN-028 | Is entitlement represented in the source or target model and, if so, is it in scope? | Appendix A |

---

# Draft Validation Findings

The draft cannot yet fully satisfy the requirement for numerical coverage and accuracy targets because those targets have not been established.

The draft cannot yet fully satisfy the independent-QA threshold requirement because the acceptable disagreement rate has not been established.

The draft cannot yet establish a numerical maximum review-flag rate. The available capacity is 4 hours per week, but the number of records that can be reviewed within that capacity depends on actual review effort observed during the pilot.

The controlled vocabulary structure is known at the attribute level, but the exact approved values and sign-off status for warranty terms and license terms have not been provided.

## Three Requirements With the Highest Remaining Uncertainty

**REQ-FUN-005** is uncertain because the vendor tiers, coverage targets, and accuracy targets have not yet been defined. Profiling the pilot population and establishing the business quality thresholds will resolve it.

**REQ-QUA-002** is uncertain because neither the minimum validated accuracy required for automatic completion nor the approving role has been established. Defining the risk tolerance for each attribute and the associated decision authority will resolve it.

**REQ-REV-003** is uncertain because review capacity is known in hours but not yet in sustainable records per week. Measuring actual review time during an initial pilot sample will allow the permitted flag rate to be calculated.

## Potentially Inconsistent Answers

No unresolved direct inconsistency remains in the interview answers.

The initial answer limited classification to Software or Hardware, but subsequent clarification explicitly added Service as a valid classification. The document therefore uses Hardware, Software, and Service.

The stated consuming system is ADM, while the system of record remains open. These answers are not inherently inconsistent because a consuming application does not necessarily have to be the authoritative system of record, but the distinction must be resolved before production exit.

## Known Conditions Not Fully Resolved Into Requirements

The known condition that long-tail vendor populations materially reduce yield has been addressed through stratified quality sampling and oversampling, but the operational impact cannot be quantified until vendor concentration is profiled.

The known condition that review backlog can exceed available capacity has been converted into review-capacity requirements, but the permitted numerical flag rate cannot be established until actual review effort per flagged record is measured.

The known condition that real values can fall outside the target vocabulary has been converted into non-conformance and governance requirements, but the expected extent of that condition cannot be assessed until the exact ADM value lists and their approval status are available.