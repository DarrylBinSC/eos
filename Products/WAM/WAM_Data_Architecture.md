> Imported 2026-07-14 from Darryl_Work_Context_Library_v1. EOS is master: update this file here; portable bundles are regenerated from EOS on demand.

# WAM — Data Architecture and Dependencies

**Version:** 1.0  
**Last updated:** 2026-07-14  
**Last known operating context:** 2026-07  
**Sensitivity:** Internal / Confidential

## 0B. UPDATE 2026-09-11 — Strev system-of-record proposal, open against the confirmed architecture

Source: Darryl, direct, 2026-09-11. Confirmed, not transcribed. Recorded here because it bears directly on section 0A.

Strev is being considered for use at Wesco's complex-build sites as a system of record. If adopted, metadata would flow back from Strev into ADM, and from ADM into EUDM. The GPO is separately reviewing the Strev tool in the warehouse.

**This does not supersede 0A and it is not a decision.** It is an open proposal that would reverse part of what 0A confirms: that DDP and EUDM are the single source of truth for asset data and the only route into ADM, with flow running one way. Do not redraw the target-state diagram on this basis until the question is settled.

Open, and each one changes the design:

- Which system is authoritative when Strev and EUDM disagree on a serial number or a parent-child relationship.
- Whether a write-back interface is inside the existing Strev SOW or is new scope.
- How the return path is governed under the Strev QA and release governance obligations.
- Whether it changes the 2027 Strev priorities, where bulk parent-child asset mapping assumes Wesco produces the hierarchy data first.

**The direction that matters is capture, not consumption.** If the warehouse and complex-build teams adopt Strev, they capture into it. Strev then holds asset data that has to reach ADM and EUDM, which is why the return paths exist at all. Framing this as Strev serving another consumer understates it and hides the governance question.

**A consequence for the component definitions.** `WAM.md` describes Strev as the customer-facing experience layer. If it becomes the warehouse system of record it is also a capture system, and that definition needs revising. Not changed yet, because the adoption is under review.

Decision-log entry: `03_Decision_Log.md`, 2026-09-11. Carried on the Sean deck as gate G7, now marked at two points on the diagram: the return paths out of Strev, and the warehouse capture path into it.

## 0A. UPDATE 2026-08-19 — Complex-Build Flow, Confirmed by Darryl

Source: Darryl, direct confirmation during diagram review 2026-08-19. Supersedes the corresponding items in §0 below; §0 retained for the decision trail.

**Confirmed architecture facts:**

- **Scope note: the work is the target state.** Current state is pre-DDP, is not defined, and is largely incapable of this flow (Darryl, 2026-08-19). Do not diagram or narrate a current state for this topic.
- **DDP/EUDM is the single source of truth for asset data and the only route into ADM.** WMX and VAS deliver into DDP; ADM takes nothing directly from either. This supersedes the 2026-07-14 candidate path of VAS delivering the serialized parent-child structure straight to ADM. ACT is the single exception, and only as a contingency.
- **WMX is not a DDP application** (Darryl, 2026-08-19). WMX and VAS are grouped in the diagram under the functional label Complex Builds, not as a platform grouping. Which systems do count as DDP applications is not yet recorded.
- **VAS and CPQ are already integrated in both directions.** VAS supplies the finished-goods parent-child template at sales-order time; CPQ supplies order and configuration context back. Integration detail sits with the dev team; flow definition sits with GPO.
- **The complex-build capture mechanism is a WMX-triggered workflow.** WMX triggers the complex-build workflow in VAS, and VAS returns the attributes WMX is able to hold. This supersedes the 2026-07-14 description of serials being pulled back from WMX into VAS. Trigger ownership is likely WMX but is not confirmed.
- **VAS writes the complete parent-child structure, serial, MAC and attributes, to DDP.** This is new build.
- **P360 provides serialization setup to WMX.** New in scope since 2026-07-14.
- **ACT is a contingency path into ADM, not a live path.** It is not integrated today and sits outside the DDP application set. Shown dotted and labelled CONTINGENCY.

**Open, as of 2026-08-19:**

- Which parent attributes WMX can ingest, including WMX 5.7 attribute support. **Note the tension with §0 below**, which records no WMX complex-build attribute capability and no roadmap until 2028. Either that statement refers to full parent-child support rather than parent attributes, or it is out of date. Resolve with Steve Leslie or Sid; the answer changes how much VAS has to carry.
- Owner of the complex-build workflow trigger.
- Mandatory serial and MAC enforcement.
- P360 and WMX configuration ownership.
- Non-DDP site handling.

Current diagrams: `Deliverables/WAM/2026-08-19_Complex_Build_Asset_Flow_v4.md`.

## 0. UPDATE 2026-07-14 — Asset-Tracking Flow Facts (VAS Roadmap meeting transcript; source: Akansh Gangil + Govardhan Shetty)

**Confirmed current-state mechanics:**
- Order chain: **VAS finished-goods template → pulled by CPQ at sales-order time → OMS → WMX.**
- **WMX captures serial numbers at shipment against the order** for simple products, and propagates them to DDP. MAC address capture: unconfirmed. Serial-to-VAS association does not happen today.
- **WMX cannot store complex-build / finished-goods attributes (MAC, serials with parent-child): no capability, no roadmap until 2028**, and even then quarters-to-years to build parent-child support.
- **ACT (Asset Capture Tool): a couple of warehouses + JPMC projects only; not scaling; not the go-to product in the DDP world** (per background sales discussions). Duplicating VAS's parent-child relationship in ACT makes little architectural sense (Akansh).
- **VAS holds finished-goods parent-child/BOM templates** (part number, manufacturer part number, manufacturer name — fully synced with DDP including price/cost).

**Govardhan's proposed mechanism (the candidate future state):** pull serial numbers back from WMX under the part number of the shipped order, map them onto the VAS parent-child template (FG number → components), and deliver the complete serialized parent-child structure downstream — VAS extends to hold serial/MAC per transaction rather than a separate capture tool.

**Open per decision log:** WMX serial/MAC capability details for complex builds (Steve Leslie/Sid), GPO roadmap buy-in, user validation (Troy Doyle). Transcript portion 7:31–26:06 not captured; mechanism above is evidenced, remaining detail may exist in that gap.

## 1. Executive Orientation

WAM's ability to scale depends on more than application development. It requires an operating model and architecture for obtaining, classifying, governing, enriching, ingesting, and maintaining asset, license, warranty, supplier, and lifecycle data.

The key executive problem is ownership across multiple systems and teams.

## 2. Data Domains

Relevant data domains include product master, customer, order history, asset, serial number, software license, license term, warranty term, entitlement, supplier part number, product description, renewal date, contract metadata, complex builds, nested BOMs, and customer-provided or non-Wesco data.

## 3. Major Systems and Capabilities

| System or Team | Role in the Model | Known Issue or Question |
|---|---|---|
| DDP / EUDM | Governed enterprise product, customer, order, and related data foundation | Connection is live; broader attribute coverage and operational use continue |
| MDM / Data Governance | Product classification, descriptions, terms, and product-master logic | Structures for software, licenses, warranties, and related attributes need definition |
| ADM | Internal normalization, enrichment, research, and data preparation | Scope and interfaces with Strev and enterprise platforms require clarity |
| Strev | WAM partner/customer-facing platform | Integration, environment, and vendor-support dependencies have existed |
| WMX | Potential serial-number or asset-record source | Feasibility and target role require validation |
| WACT / ACT | **Evaluated and not pursued (Darryl, direct, 2026-09-14).** Was: potential interim source for complex builds and nested BOMs | **The sufficiency test has now been run and WACT failed it: the tool is not mature and holds little data.** This closes the open question in this row rather than leaving it open. Do not re-propose WACT as a complex-build source without new evidence that the tool and its data have materially changed |
| VAS | Potential future source or evolution for complex asset capture | Roadmap and timing require validation |
| IDP | Document, PDF, or email extraction and ingestion automation | Could accelerate ingestion if priorities and integration align |
| Supplier Relations / Vendors | Source of license, warranty, part, and lifecycle data | Data availability, cadence, and standardization are major constraints |
| Sales Operations | Commercial and supplier-data coordination | Manual outreach and attribution have been necessary |
| Customer data | Non-Wesco assets, contracts, spreadsheets, documents | Requires controlled ingestion and quality process |

## 4. DDP/EUDM Benefits

The enterprise-data connection is intended to enable governed product classification and taxonomy, historical order data, consistent product and customer context, reduced manual movement and cleanup, repeatable ingestion, better install-base visibility, and a stronger foundation for automation and AI.

### Critical clarification

DDP/EUDM is a foundation, not the complete solution.

Remaining work includes attribute definitions, stewardship, source coverage, vendor-data acquisition, quality rules, exception management, customer-data ingestion, and complex-build sourcing.

## 5. Product Classification

Known requirements include:

- Separate hardware, software, licenses, warranties, and services
- Standardize descriptions
- Identify license type and duration
- Identify warranty term
- Support lifecycle and renewal logic
- Handle ambiguous or incomplete product records
- Create a controlled human-review path

The Data Governance intake included concepts such as product classification flag, software license-term visibility, hardware warranty-term visibility, and standardized product descriptions.

## 6. Historical and Supplier Data

Open design questions include:

- How far back to retrieve data
- Default versus user-controlled filters
- Configured part numbers versus broad retrieval
- How to incorporate customer-provided records
- How to resolve supplier-specific formats
- How to maintain data after initial ingestion
- How to distinguish renewal, new sale, and attribution

## 7. ACT / WACT Integration Lesson

The team discussed an ADM-to-ACT integration for serial-number or production data.

The key lesson was:

> Validate that ACT contains the production data required to solve the business problem before investing in a substantial integration.

A rough estimate of approximately three months was discussed, while the long-term role of ACT remained uncertain due to platform limitations and possible future systems such as WOS or WMX.

Do not treat an integration estimate as approval to build.

**Closed 2026-09-14 (Darryl, direct, Confirmed, not transcribed).** The validation the lesson called for was performed and WACT did not pass it: **the tool is not mature and does not hold much data.** WACT is therefore eliminated as an option. **Nothing else about the capture path is settled** (Darryl, direct, 2026-09-14): the 2026-09-01 WMX/VAS boundary is a stated position reclassified to Approaching, and the system of record is open pending the 2026-09-11 Strev review (`03`, gate G7, owner GPO). Eliminating an option narrows the evaluation; it does not conclude it, and this file should not be read as recording a chosen path.

**The lesson held, and it is worth recording that it held.** This is the first case in the record where a "prove sufficiency before integrating" caution was actually executed and produced a negative answer that stopped work. The three-month integration was not built. Cite this when the same pattern recurs on WMX, VAS, or any future asset source: the row above still reads "Feasibility and target role require validation" for WMX, and that test has not been run.

## 8. Entitlement Concept

An entitlement event is an occurrence that creates, changes, renews, transfers, consumes, suspends, or terminates a customer's right to use a software capability or receive a related service.

Examples include license purchase, activation, renewal, upgrade, seat changes, transfer, expiration, cancellation, and support or maintenance changes.

The exact WAM implementation and data model require validation.

## 9. Decision Framework

For each data dependency, identify the business outcome, authoritative source, data owner, steward, ingestion method, quality standard, exception process, interim solution, target architecture, delivery date, and cost of delay.

## 10. Failure Modes

- Building integrations before validating source-data fitness
- Treating all data problems as application-development work
- Allowing problem-definition workshops to continue without decisions
- Creating local workarounds without a retirement plan
- Assuming supplier data will arrive in a standard form
- Confusing a technical connection with a governed operating model
- Overstating AI readiness when foundational data is weak
