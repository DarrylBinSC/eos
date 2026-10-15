# Contract Lifecycle Management (CLM)
As of: 2026-10-01 (status update; body as of 2026-09-28). Area created this date from three source files Darryl added to `Products/CLM/`. This file is the front door for the product; the source files hold the detail and are not duplicated here.

**Source files and how much weight each carries.**

| File | What it is | Evidence quality |
|---|---|---|
| `Email_Fw_CLM Doc.pdf` | Chain: Nanda to Merwan Mereby (2026-09-01), Nanda to Chris Gazdic (2026-09-25), Chris to Sean McCloskey with Copilot notes from Chris's call with Nanda (2026-09-25), Chris to Darryl "FYI" (2026-09-28) | The business-need summary is **Copilot-generated meeting notes**, not Nanda's own words. Treat figures ($1.2M, 24 epics, 8 months) and attributions as reported, pending confirmation |
| `Enterprise_CLM_Scope_Augmented_with_Prior_Requirements.docx` | Nanda's product scope. Nanda calls it "an evolving doc." Built on an earlier business-area matrix, `CLS Tool Requirements by business area.docx` (not in the folder) | Authored scope. Defines Epics 1 to 23; Epic 24 is not defined in it |
| `CLM_Process_Module_Flow.jpg` | One-page visual: five lifecycle phases, buy-side and sell-side swimlanes, shared platform, integrations, and a SOX and internal controls layer | Companion to the scope doc. The only source that shows Epic 24 and the SOX layer |

**Intended for Darryl and his team, pending Sean's decision (Darryl direct, 2026-09-28).** Sean McCloskey told Darryl in conversation today that he would give CLM to Darryl and his team to build and develop. Sean makes the final decision in the corporate AOP meetings the week of 2026-09-28 with Akash and Nanda. The product comes from Akash; Nanda reports to Akash and sits at the same level as Sean. None of the three source files reflects this; they predate it. Record: `03` Decision Radar, 2026-09-28. Capacity and skills input: `Deliverables/CLM/2026-09-28_CLM_Capacity_and_Skills_Assessment.md` (v2; v1 kept as SUPERSEDED_). Learning brief and investigation plan: `Deliverables/CLM/2026-10-01_CLM_Product_Brief.md` (2026-10-01). It adds three open questions not elsewhere in this file: how contracts already in force get CLM records given legacy migration is out of scope (likely a Contract Intelligence dependency that pulls Epic 22 forward); who owns templates, clause library and delegation-of-authority content (no Legal owner named); and whether Wesco already licenses Oracle Procurement Contracts, which could cover much of the buy-side journey (hypothesis, unverified).

## What It Is / Value Proposition

A custom-built enterprise application that governs contracts from request through execution and post-execution lifecycle, with one shared platform and two differentiated journeys: **buy-side** (Procurement, Sourcing, Category Management) and **sell-side** (Sales, account management, Sales Operations).

The governing principle, in Nanda's words: *"CLM manages the process. The repository preserves the document. Contract Intelligence interprets the content. Operational systems act on validated commitments."* CLM therefore owns request, authoring, collaboration, negotiation, approval, signature orchestration, amendment, renewal, termination, obligations and operational reporting. It explicitly does not own document storage (the existing repository, reported as FileNet), AI extraction or semantic search (Contract Intelligence, reported as Merwan Mereby's solution), or inventory calculations (planning systems).

Business need as reported: replace fragmented contract processes with a governed, standardized workflow across Legal, IP, VMO, Category Management, Real Estate and Sales, across three SBUs. **Sales contracts are the stated priority because of their direct accounting impact.** The effort originated in Controllership.

## Current State

> **2026-10-01: not adopted in the FY27 AOP; CLM will not be built in 2027** (Darryl, direct; original source not stated). Everything below describes the product as scoped and the pre-decision position. Unknown: deferred to FY28 or dropped; whether Nanda's organization pursues it another way; whether the intent to place it with Darryl's team carries forward. The CDA staffing option tied to CLM no longer applies. Record: `03` Decisions Made, 2026-10-01.

Pre-delivery. Scope is drafted and evolving; no delivery organization exists.

- **Ownership: build and development intended for Darryl and his team** (Sean, verbal, 2026-09-28, relayed by Darryl); **final decision at the corporate AOP meetings this week.** This supersedes the delivery gap in the 2026-09-25 Copilot notes, which said CLM "would be managed as a product under Nanda, with Product Ownership under Sean" and that no delivery headcount existed. **Still undefined:** what role Nanda keeps (requirements owner, business-side product manager, or handoff only), and whether Darryl is formally the Product Executive on the Digital Product List. Nothing written exists yet.
- **Sponsor chain:** Akash (Nanda's manager; Sean and Nanda are peers). Controllership is the originating business need.
- **Headcount: none dedicated today.** The work lands on Darryl's existing organization unless the funding moves with it.
- **Staffing option under discussion (Darryl, 2026-09-28):** move CDA to the entroCIM team with roadmap rationalization, and use the CDA development pod as all or part of the CLM team. About 5.75 FTE would transfer (back-end architect, two back-end and two front-end developers, shared UX and QA). Condition: CDA's FY27 scope reset to validation and pilot on existing entroCIM capabilities. Worked through in the v2 assessment.
- **AI-assisted development (Nanda's expectation, relayed by Darryl 2026-09-28):** Nanda sees product ownership and the development team using Claude Code to shorten development; all of Ron Snyder's team has access. Darryl's direction: use it to validate the resource, effort and timing estimates. Method proposed: a measured Claude Code pilot on a thin slice of the core during discovery (throughput, defects, rework, cycle time, per Sean's 09-16 measurement standard). Planning range: 16 FTE baseline, 13 FTE with the CDA pod core and an AI-assisted hypothesis.
- **Timing:** Sean is in corporate AOP meetings the week of 2026-09-28, which is where the funding question is live.
- **Scope:** approximately 24 epics; 8-month MVP envisioned. The scope doc recommends three releases:

| Release | Focus |
|---|---|
| 1 | Shared foundation; one buy-side and one sell-side journey; authoring, preview, workflow, approvals, signature, repository integration, CLM search, audit |
| 2 | Broader Sourcing, Category and Sales participation; clause-level workflow; Procurement and commercial integrations; contract families; Outlook, mobile, reporting |
| 3 | Contract Intelligence integration; validated obligations; Inventory Planning handoff; advanced renewal and termination; cross-platform analytics |

Whether the 8-month MVP equals Release 1 is not stated.

- **Not on the August 2026 Digital Product List** (`Reference/Digital_Product_List.md`), in either Invest or Run. Consistent with a product still being formed; do not infer anything further from the absence.

### Epic map

Assembled from all three sources. Named systems come from the email; the scope doc keeps them generic.

| # | Epic | Side | Named system or note |
|---|---|---|---|
| 1 | Request and intake | Shared | Guided forms; existing-contract check |
| 2 | Contract workspace | Shared | Visual also maps Search and Views, Notifications and Tasks here |
| 3 | Authoring and document experience | Shared | Word editing with tracked changes; preview without download; watermarks |
| 4 | Collaboration and negotiation | Shared | Three zones: Internal Legal, internal deal team, external. Visual labels Clause and Section Workflow as Epic 4; the doc places clause routing in Epic 5 |
| 5 | Review and approval | Shared | Clause-level and parallel review; segregation of duties; dependent-term warnings |
| 6 | E-signature orchestration | Shared | **Nitro / DocuSign** |
| 7 | Contract family | Shared | MSA, SOW, amendments, supersession |
| 8 | Post-execution lifecycle | Shared | Renewal, termination, obligations |
| 9 | Security, identity and audit | Shared | SSO, RBAC and ABAC, legal privilege separation |
| 10 | Configuration and administration | Shared | Types, workflows, approval matrices, effective-dated rules |
| 11 to 15 | Sourcing initiation; supplier commercial workflow; specialist reviews; procurement integration; supplier lifecycle | Buy | Epic 14: **Oracle Cloud Sourcing and Procurement**, supplier master |
| 16 to 20 | Sales initiation; Sales participation; commercial approvals; commercial integration; customer lifecycle | Sell | Epic 19: **Microsoft Dynamics**, customer master, CPQ and pricing, order and billing, Bill & Hold, Customer-Owned Product |
| 21 | Repository integration | Integration | **FileNet** |
| 22 | Contract Intelligence integration | Integration | **Merwan Mereby's Contract Intelligence Solution**; workflow must continue if it is unavailable |
| 23 | Data synchronization | Integration | Common identifiers; master data |
| 24 | Reporting; SOX and internal controls | Shared | **Visual only; not defined in the scope doc.** SOX scoping, complete-population controls, SoD, delegation of authority, interface controls, key reports and IPE, ITGCs, third-party (SOC) controls |

### Architecture reading of the epics (Darryl and Claude, 2026-09-28)

Darryl's read, confirmed on analysis: the epics are modules, use cases and process flows of one core CLM application, not 24 things to build. Three layers:

| Layer | Epics | Character |
|---|---|---|
| Core application (domain model, workflow and task engine, approval and policy engine, document service, access and zones, audit, configuration, search/notify/report) | 1, 2, 3, 4, 5, 7, 8, 9, 10, 24 | Built once; most of the engineering. Epic 3 (Word co-authoring) and Epic 5 (clause-level parallel review) are the hardest parts |
| Integration adapters | 6, 14, 19, 21, 22, 23, plus identity, analytics, Inventory Planning handoff | Built per system; schedule partly set by other teams |
| Use models (journeys) | Buy 11, 12, 13, 15; Sell 16, 17, 18, 20 | Should be configuration of the core. Real Estate and IP would be further use models |

Consequences: size by layer, not epic count; Release 1 = core + e-signature, repository and identity adapters + one use model (sell-side first); the second use model tests whether the core is truly configuration-driven; the build-versus-buy question is really "build the core or license it," since adapters and configuration are needed either way.

A sell-side **Inventory Planning commitment handoff** (storm stock, quantities, days of supply, dates) is carried as a workflow and data handoff, not as an inventory engine. It sits in Release 3.

## Commercial Position

Internal enterprise capability. No external revenue model, no customer, and no commercialization path is proposed in any source. Value is control, cycle time, and data quality, not revenue.

**Funding (reported):** "$1.2M is included in AOP to support the initiative." Under the funding-governance rule in `01`, that is state (1), **a number requested in an AOP**, until it is shown to have cleared approval and to exist as a UiPath project. Which organization's AOP carries the line is not stated. **Now that the build sits with Darryl's team, this is the first thing to settle:** if the $1.2M sits in Nanda's or Akash's AOP and the work sits in Darryl's organization, the build is unfunded on Darryl's side until the line is transferred or a chargeback is agreed.

## Key Dependencies

- **Existing contract repository (FileNet), Epic 21.** Authoritative storage, signature evidence, retention and legal holds. CLM deliberately creates no second document store.
- **Contract Intelligence (Merwan Mereby), Epic 22.** Extraction, summarization, clause analysis, semantic search, risk scoring. Separately governed. Merwan leads the India Platforms team (`03`, 2026-08-26 CMP decision), the same team whose ADM delivery performance Sean has questioned (`06`, Sean McCloskey, 09-10). Deferred to Release 3, which limits early exposure.
- **E-signature (Nitro / DocuSign), Epic 6.** Two tools are named; whether both stay or one is chosen is not stated.
- **Oracle Cloud Sourcing and Procurement, supplier master (Epic 14); Microsoft Dynamics, customer master, CPQ, order and billing (Epic 19).** Each is an integration with its own owning team.
- **Authoritative employee identity and SSO (Epic 9).**
- **Enterprise analytics platform** for governed CLM data (Epic 24 / reporting).
- **Business process owners across Legal, IP, VMO, Category Management, Real Estate, Sales, Finance, Tax, Pricing and Inventory Planning.** None is named.
- **Internal Audit / SOX program**, if CLM is scoped as a SOX-relevant system (see Risks).

## Managed Services Angle

No external managed service. The internal operating model is the equivalent question and it is unaddressed: who administers templates, approval matrices, routing rules and effective-dated configuration (Epic 10) after go-live, who supports a broad occasional-use Sales population, and who owns integration monitoring and failed-transfer reconciliation (Epics 21 and 23). Configurable CLM platforms carry a standing administration load that does not shrink after launch; the delivery plan needs a funded run team, not only a build team.

## Benefits Realization

Planned, not realized. The scope doc defines a strong measurement set in three groups: adoption (for example, eligible contracts initiated through CLM, template usage, digital signature usage); process performance (request-to-assignment, approval cycle time, end-to-end cycle time, internal versus counterparty wait, renewal timeliness); and control, data and integration (approval evidence completeness, repository linkage, master-data match rate, duplicate-document incidents). It correctly assigns AI extraction accuracy to Contract Intelligence rather than CLM.

What is missing is a baseline. None of the measures has a current-state value, so no benefit can be demonstrated later without capturing one before Release 1.

## Key People

- **Nanda Kumar Rajagopal**, VP, Corporate Applications, IT & Digital (Pittsburgh). Author of the scope and the earlier requirements matrix. Reported as the manager of CLM as a product.
- **Sean McCloskey.** Reported as holding Product Ownership. Received Chris's Copilot notes on 2026-09-25.
- **Chris Gazdic**, Senior Director, Product Operations. Held the call with Nanda and routed the material to Sean and to Darryl.
- **Merwan Mereby.** Owner of the Contract Intelligence Solution (reported). Received the scope and visual from Nanda on 2026-09-01.
- **Controllership.** Originating sponsor organization; no individual named.
- **Akash (presumed Akash Khurana; confirm).** Sponsor; Nanda reports to him. Darryl stated the reporting line; the identification with the Akash Khurana in `06` is an inference from the name and seat.
- **Darryl Benson and team.** Intended to build and develop CLM (Sean, 2026-09-28), pending Sean's decision at the AOP meetings.

## Major Risks and Open Decisions

Current status lives in the living documents; this file does not duplicate register state. Pending decision recorded in `03` Decision Radar, 2026-09-28.

- **Open: funding follows the work?** Where the $1.2M sits, and whether it transfers to Darryl's organization. Sean's AOP meetings this week are the forum.
- **Open: division of ownership with Nanda.** Who owns requirements, prioritization and acceptance, and who holds the Product Executive seat on the portfolio list.
- **Risk: capacity.** CLM becomes a fifth Invest-scale product, and the first outside CSS, on a team that already carries entroCIM, WAM, Navigator and CDA, with no dedicated headcount named.
- **Open, and the most important question in the material: why custom-build after an unsuccessful iCertis effort?** The scope doc's feature set (clause-level parallel review, Word-based redlining, negotiation zones, e-signature orchestration, contract families, obligations, approval matrices) is the core of mature commercial CLM platforms. No source records why iCertis failed. If the cause was process ownership, data, adoption or scope rather than the tool, a custom build carries the same causes forward and adds build and maintenance risk. A written iCertis post-mortem and a build-versus-configure comparison are needed before build commitment.
- **Risk: Release 1 is large for the capacity described.** Two journeys, Word-based authoring, signature, repository integration and audit, with no dedicated headcount and an 8-month MVP target. The scope doc itself warns that success with trained Sourcing users does not prove usability for a broad Sales population.
- **Tension: sequencing.** The email makes sell-side the priority (accounting impact); the scope doc puts one journey of each side in Release 1. These need reconciling before a plan is built.
- **Gap: SOX and controls scope is undefined in writing.** The visual shows a full SOX and internal-controls layer (Epic 24) with no counterpart in the scope doc. Given the Controllership origin, CLM may become an in-scope SOX system, which would change change-management, testing, access-certification and release cadence for the life of the product. Internal Audit belongs in scoping, not at go-live.
- **Gap: named stakeholders the model does not cover.** Real Estate and IP are named in the business need but do not fit the buy-side / sell-side journeys cleanly. Either they need a journey or they are out of MVP scope; the material says neither.
- **Dependency risk: Contract Intelligence and FileNet are separately governed.** CLM's design depends on both services existing and being stable. Their roadmaps, owners and service levels are not stated.

## History and Lessons

- Origin in Controllership. An earlier iCertis CLM initiative was unsuccessful (date and cause not recorded).
- An earlier requirements matrix, `CLS Tool Requirements by business area.docx`, covered Legal, Sourcing, Sales, Inventory, Pricing and Accounting. The current scope was augmented from it, adding fine-grained clause workflow, document controls, productivity features and the Inventory Planning handoff.
- 2026-09-01: Nanda sent the scope and visual to Merwan Mereby as an evolving document.
- 2026-09-25: Chris Gazdic met Nanda, sent Copilot notes to Sean.
- 2026-09-28: Chris forwarded the chain to Darryl, FYI. Darryl added the product to the EOS the same day. Sean told Darryl the same day that he would give CLM to Darryl and his team to build and develop, with the final decision to be made at the corporate AOP meetings that week with Akash and Nanda.
