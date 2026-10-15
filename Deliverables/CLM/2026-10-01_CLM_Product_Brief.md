---
title: "Contract Lifecycle Management: Product Brief"
date: "2026-10-01"
author: "Prepared for Darryl Benson"
---

> **Status 2026-10-01:** CLM was not adopted in the FY27 AOP and will not be built in 2027. This document is retained as reference if CLM returns in a later cycle.


# Bottom line

CLM is a custom enterprise workflow application that runs a contract from request to signature and then through renewal or termination, for both buying (suppliers) and selling (customers). It deliberately does not store the final documents (FileNet does) and does not do AI analysis (Merwan Mereby's Contract Intelligence service does). Nanda's scope is well bounded and better written than most first-draft scopes. What it lacks is the operating data that sizes the work (contract volumes, user counts, today's process) and any account of why the earlier iCertis effort failed.

Chris' notes are a Copilot summary of a single call, not Nanda's words. Four points in them need care: the $1.2M is a request in an AOP, not funding; "24 epics" counts one epic that appears only in the visual; the 8-month MVP has no stated basis; and the ownership line ("product under Nanda, Product Ownership under Sean") predates Sean's 9/28 statement to you and is ambiguous on decision rights.

Three questions decide whether this product succeeds, and none is answered in the material:

1. **Why did iCertis fail?** iCertis was a Gartner Magic Quadrant Leader for CLM in 2023 and 2024, so a weak tool is the least likely cause. If the cause was ownership, adoption, integration or data, a custom build inherits it.
2. **Who owns the content?** CLM runs on templates, a clause library, approval matrices and delegation-of-authority rules. Legal and Finance own that content, and no Legal or Controllership owner is named.
3. **How do the contracts already in force get into CLM?** Legacy migration is excluded from scope, yet renewals, amendments and obligations (Epics 7, 8, 15, 20) only work for contracts CLM knows about.

The rest of this brief explains the product, decodes Chris' notes line by line, gives an independent read of the scope, and lays out an investigation plan you can run yourself. The team, cost and AOP terms are in the 2026-09-28 Capacity and Skills Assessment and are not repeated here.

# What CLM is

Contract lifecycle management is an established software category. A CLM system replaces the mix of email, shared drives, Word attachments and side approvals that most companies use to get a contract written, reviewed, approved and signed, and it then tracks what was agreed so renewals and obligations are not missed.

Nanda's design rests on one sentence, which is worth memorizing because it settles most scope arguments:

> *"CLM manages the process. The repository preserves the document. Contract Intelligence interprets the content. Operational systems act on validated commitments."*

| Layer | Owns | Does not own |
|---|---|---|
| CLM (the product) | Requests, workspaces, authoring workflow, negotiation, approvals, signature orchestration, lifecycle status, amendments, renewals, obligations, operational reporting | Final document storage; AI analysis |
| Existing repository (FileNet) | Executed and legacy documents, signature evidence, retention, legal holds | Request and approval workflow |
| Contract Intelligence (Merwan Mereby) | Extraction, summaries, clause analysis, semantic search, risk scoring | Human approvals, workflow status |
| Operational systems (Oracle, Dynamics, Inventory Planning) | Acting on the agreed terms (POs, orders, billing, stock) | Contract workflow |

The practical consequence: CLM is a workflow and control product with integrations, not a document management product and not an AI product.

## One platform, two journeys

| | Buy-side | Sell-side |
|---|---|---|
| Purpose | Acquire goods and services on compliant terms | Sell on acceptable commercial and legal terms |
| Starts from | Sourcing event, purchase need, SOW, renewal | Opportunity, customer request, quote, renewal |
| Users | Sourcing, Category Management, Procurement | Sales, account management, Sales Operations |
| Core system | Oracle Cloud Sourcing and Procurement, supplier master | Microsoft Dynamics, customer master, CPQ, order and billing |
| Risk lens | Spend, supplier risk, security, payment | Revenue, margin, credit, warranty, delivery commitments |

The scope makes one point that matters for design: trained Sourcing users and occasional Sales users are different populations. A workflow that works for Procurement specialists can still fail with a broad Sales force.

## How a contract moves through it

The visual (`CLM_Process_Module_Flow.jpg`) shows five phases. A sell-side example makes them concrete.

1. **Intake and initiation.** A CSS account manager has a data-center customer that sends its own master agreement. She opens a guided request in CLM, links the Dynamics opportunity, and CLM checks whether a customer agreement already exists (Epics 1 and 16).
2. **Author and collaborate.** Legal is assigned. The customer's paper is uploaded and Legal redlines it in Word with tracked changes. Work happens in three zones: privileged Legal discussion, the internal deal team (where Sales sees plain-language status and can comment but cannot accept legal deviations), and the external zone where a clean version goes to the customer (Epics 3, 4, 17).
3. **Review and approval.** Sections route in parallel: Credit reviews payment terms, Tax reviews tax language, Pricing reviews discounts and margin. If the customer wants stock held, Inventory Planning confirms feasibility. Approval levels follow the delegation-of-authority matrix, and a change to a primary term after approval forces re-approval (Epics 5 and 18, plus the Inventory Planning handoff).
4. **Execute.** The approved version is locked and sent for e-signature through Nitro or DocuSign. The executed document and signature evidence transfer to FileNet, and CLM keeps the FileNet ID (Epics 6 and 21).
5. **Post-execution.** CLM links the contract to the Dynamics quote, order and billing records, tracks commitments, and alerts the owner before the renewal notice date (Epics 8, 19, 20).

Underneath both journeys sit the shared platform services (workspace, document experience, clause workflow, security, audit, configuration, search, notifications, reporting), the integrations, and a SOX and internal-controls layer.

# Reading Chris' notes

Chris met Nanda on 9/25 and sent Sean a Copilot summary the same afternoon; he forwarded it to you on 9/28 as FYI with no ask. Copilot meeting summaries paraphrase and can misattribute, so treat every figure and role statement as reported until Nanda confirms it.

| Chris' note says | What it means | Check against the sources | Ask |
|---|---|---|---|
| CLM as a new digital product, managing contracts "through execution and centralized repository management" | Run as a product with an owner and roadmap, not a one-time project | The phrase "repository management" overstates CLM's role. Nanda's scope says CLM hands documents to FileNet and creates no second store | None; use Nanda's boundary when you describe it |
| Standardized workflow spanning review, approvals, execution, repository | Today's process is fragmented, likely email, shared drives and side approvals | No current-state description or baseline exists in any source | What does a sales contract go through today, and how many are there per year? |
| Legal, IP, VMO, Category Management, Real Estate and Sales across three SBUs; sales contracts are the priority because of "direct accounting impact" | Enterprise-wide, across EES, CSS and UBS. "Accounting impact" points to revenue recognition: payment terms, bill-and-hold, customer-owned product, rebates and pricing commitments change when and how revenue is booked. That is why Controllership started this and why Epic 19 names Bill & Hold and Customer-Owned Product | VMO is presumably the Vendor Management Office and IP the intellectual-property legal function; confirm. Real Estate and IP do not fit either journey and are not scoped | What accounting problem triggered this: audit findings, restatements, or close-cycle effort? |
| "Managed as a product under Nanda, with Product Ownership under Sean, but no dedicated headcount exists today" | As of 9/25, Nanda's organization held the product and Sean's organization was expected to own delivery, with no people assigned | Superseded in part by Sean's 9/28 statement that he would give build and development to your team. Neither statement says who decides scope, priority and acceptance | Who holds which decision rights, and who is Product Executive on the Digital Product List? |
| "Approximately 24 epics," "8-month MVP" | The size Nanda has in mind | The scope document defines Epics 1 to 23. Epic 24 (Reporting; SOX and internal controls) appears only in the visual. The 8 months appears in no document, and nothing says whether the MVP equals Release 1 | What is the 8 months based on, and what team does it assume? |
| "Dedicated cross-functional delivery structure and collaboration channel" needed | Nanda recognizes there is no delivery organization. This is the gap that lands on your team | Consistent with all sources | What does Nanda's organization contribute: product owner, analysts, integration SMEs? |
| Dependencies: FileNet (Epic 21), Merwan's Contract Intelligence (Epic 22), Nitro/DocuSign (Epic 6) | The three integrations discussed on the call | Incomplete. The scope also depends on Oracle Procurement (14), Dynamics, CPQ and billing (19), identity and SSO (9), enterprise analytics and Inventory Planning. Two e-signature tools are named with no choice made | Is Wesco keeping both Nitro and DocuSign? |
| "$1.2M is included in AOP" | A number has been placed in an AOP | Under your funding rule this is a request until it clears approval and exists as a UiPath project. Whose AOP, which fiscal year, and whether it covers labor, licenses or both are unstated. For scale, the 9/28 assessment puts Release 1 labor at about $540K to $620K and the annual run rate at about $810K to $930K | Whose AOP line is it, and does it move with the work? |
| Originated in Controllership; follows an "unsuccessful iCertis initiative," creating "a need for a more achievable approach" | Nanda's thesis is that a scoped custom build is more achievable than the commercial platform was | No source records why iCertis failed, when, or what it cost. "More achievable" is an untested premise | See the iCertis questions below |
| Recommended direction: governed product, defined ownership, dedicated capacity, prioritized MVP, stakeholder governance | Reads as Copilot's synthesis of the conversation rather than a decision | Consistent with your 9/28 assessment | None |

What the notes do not mention is as useful as what they do: no Legal owner, no contract or user volumes, no SOX scoping, no start date, and no comparison with licensing a platform.

# Scope at a glance

The epics read best as three layers of one application rather than 24 separate builds. This is the architecture view from the 9/28 assessment, summarized here so the scope is readable on its own.

| Layer | Epics | What it is |
|---|---|---|
| Core application | 1 Intake, 2 Workspace, 3 Authoring, 4 Collaboration, 5 Review and approval, 7 Contract family, 8 Post-execution, 9 Security and audit, 10 Configuration, 24 Reporting and controls | Built once; most of the engineering. Epic 3 (Word editing and preview) and Epic 5 (clause-level parallel review) are the hardest parts |
| Integration adapters | 6 E-signature, 14 Oracle Procurement, 19 Dynamics, CPQ, billing, 21 FileNet, 22 Contract Intelligence, 23 Data synchronization, plus identity, analytics, Inventory Planning | One per external system; schedules partly set by the owning teams |
| Journeys (use models) | Buy: 11, 12, 13, 15. Sell: 16, 17, 18, 20 | Should be configuration of the core: contract types, forms, templates, routing rules |

**Proposed releases (Nanda's scope):**

| Release | Content |
|---|---|
| 1 | Shared foundation; one buy-side and one sell-side journey; authoring, preview, workflow, approvals, signature, FileNet integration, CLM search, audit |
| 2 | Broader Sourcing, Category and Sales participation; clause-level workflow; Oracle and Dynamics integrations; contract families; Outlook, mobile, reporting |
| 3 | Contract Intelligence; validated obligations; Inventory Planning handoff; advanced renewal and termination; cross-platform analytics |

**Inconsistencies across the three sources to resolve with Nanda:**

- Epic 24 exists only in the visual. The SOX and controls layer shown there has no counterpart in the scope document.
- The visual labels Clause and Section Workflow as Epic 4; the document puts clause routing in Epic 5.
- Chris' notes make sell-side the priority; the scope puts one journey of each side in Release 1.
- Clause-level workflow is described as a core requirement, but the release plan defers it to Release 2.

# Independent read of the scope

## What it does well

- **Boundaries.** It refuses a second document store and refuses to duplicate AI services. That discipline is the single best protection against scope creep.
- **Shared core, two journeys.** The right structure, and it leaves room for Real Estate, IP or other contract areas as configuration later.
- **Measures.** Adoption, cycle-time, control and data-quality measures are defined, and AI extraction accuracy is correctly assigned to Contract Intelligence rather than CLM.
- **Grounded requirements.** It was built from an earlier business-area requirements matrix covering Legal, Sourcing, Sales, Inventory, Pricing and Accounting, so the detail reflects what users asked for.

## What is missing or understated

| Gap | Why it matters |
|---|---|
| No volumes: contracts per year by type and side, users by role, external counterparties | Drives architecture, performance, licensing comparison, support model and team size. A 2,000-contract business and a 40,000-contract business need different products |
| No current-state baseline | Without one, none of the success measures can show improvement later |
| Contracts already in force | Legacy migration is excluded, but renewals, amendments and obligations need live contracts in CLM. Creating those records probably depends on Contract Intelligence extracting metadata from FileNet, which would pull Epic 22 forward from Release 3 |
| Content ownership | Templates, clause library, fallback positions, approval matrices and delegation of authority are Legal and Finance content. Without a named owner, "standard-template usage" cannot rise and routing rules cannot be configured |
| Word editing approach | In-browser Word editing with tracked changes is the hardest technical requirement. Embedding Word for the web directly in a custom application runs through Microsoft's partner program (WOPI); the common enterprise alternative keeps working drafts in SharePoint or OneDrive and opens them in Word for the web. This choice shapes the whole document service and should be settled early by your architect |
| External counterparty access | The external negotiation zone means customers and suppliers touch the system, which brings external identity, security review and information-protection questions. Release 1 may be simpler if external exchange stays by email with CLM tracking versions |
| SOX scope | Controllership's involvement makes it plausible CLM becomes a SOX-relevant system. That changes change management, test evidence, access certification and release cadence for the life of the product |
| Non-functional targets | Availability, recovery time, retention and audit-evidence periods are listed as topics without numbers |
| Global use | Three SBUs and multiple countries imply legal-entity controls, possible language needs and e-signature validity across jurisdictions |

# Build versus license: context for your own view

This brief does not reopen the recommendation in the 9/28 assessment (a discovery gate that compares building the core with licensing it). It gives you the market context to hold that conversation.

**The market is mature.** The vendors named Leaders in Gartner's 2025 Magic Quadrant for Contract Life Cycle Management, per their own announcements, are Agiloft, Docusign, Ironclad, Malbek and Sirion. Icertis was a Leader in 2023 and 2024. Nanda's feature list (clause-level parallel review, Word redlining, negotiation zones, e-signature orchestration, contract families, obligations, approval matrices) is the standard core of these products.

**First implementations fail often, and rarely because of features.** MGI Research's 2025 CLM Buyer's Guide, as cited by Elevate, reports that over 40% of organizations replace their first CLM system within three years. The causes most often cited are poor adoption and integration: the CLM sits outside the systems people already work in, so users go back to email. Treat these as industry signals, not Wesco evidence. They do sharpen the iCertis question.

**Wesco may already own part of the answer.** Three possibilities are worth checking before anyone commits to building every layer:

- **Oracle Procurement Contracts.** Oracle Fusion Cloud includes a procurement contracts module with a clause library, templates, policy-driven approval rules, a Word add-in for authoring and deviation detection, and deliverables tracking. If Wesco licenses it, much of the buy-side journey may already exist in the system Procurement uses. That would let the custom build focus on the sell-side, which is the stated priority and where Dynamics integration is the main need. This is a hypothesis to test, not a conclusion.
- **DocuSign.** If Wesco's DocuSign agreement is an enterprise one, its CLM product is an add-on conversation, and it is a current Gartner Leader.
- **iCertis.** Whether the license is still active, and what configuration, templates and clause content were built in it. Content built for iCertis (templates, clause library, approval matrices) is reusable whatever platform follows.

# Investigation plan

The aim is to have your own evidence-based view before the role split and funding are settled, and to arrive at the first working session with Nanda already knowing the right questions. Ordered by value.

## Conversations

| Who | Why them | What to learn |
|---|---|---|
| **Nanda Kumar Rajagopal** | Scope author, business-side owner | iCertis history (when, cost, what was configured, why it stopped); contract and user volumes; today's process; basis for the 8 months; whose AOP holds the $1.2M; which role he expects to keep; Legal and Controllership sponsors by name; Nitro or DocuSign; Corporate Applications platform and hosting standards |
| **Chris Gazdic** | Held the call; runs Product Operations | What was said beyond the summary; how he reads Akash's and Nanda's expectations; how CLM would appear on the Digital Product List |
| **Brandon (Senior Counsel)** | Your existing contact in Legal | Legal's experience with iCertis; who owns templates and the clause library; how privileged review works today; whether Legal sees CLM as its tool or as Finance's |
| **Controllership lead** (name to get from Nanda) | Originating sponsor | The accounting problem behind this; which contract terms drive revenue recognition; SOX expectations |
| **Debbie Hunter or Natalie Marquardt** (Sales Operations) | Sell-side is the priority, and you already work with them on WAM | How a sales contract is requested and tracked today; how Dynamics is used for opportunities and quotes; who the occasional-use requestors are |
| **Merwan Mereby** | Owns Contract Intelligence | What the service does in production today versus planned; its interfaces; whether it can extract metadata from FileNet to create records for contracts in force; roadmap and support model |
| **FileNet, Oracle Procurement and Dynamics application owners** (likely in Nanda's organization) | Integration dependencies | APIs, metadata model, test environments; whether Oracle Procurement Contracts is licensed or in use |
| **Internal Audit** | SOX scoping | Whether CLM would be in scope and what that requires from day one |
| **Ron Snyder** | Your development leadership | Architecture view on the Word editing approach and on a configuration-driven core; readiness for a measured Claude Code pilot |

## Documents to request

- The iCertis project closure, post-mortem or steering-committee record, and the license agreement
- `CLS Tool Requirements by business area.docx`, the earlier requirements matrix Nanda built the scope from
- Contract volumes for the last 12 months by type, side and SBU
- Current contract templates, the clause library if one exists, and the delegation-of-authority matrix
- FileNet contract metadata schema and retention rules
- Contract Intelligence overview and interface documentation
- The AOP line item detail behind the $1.2M

## First-hand observation

- **Walk one sales contract end to end** with Sales Operations and Legal, from customer request to filed signed copy. This is the fastest way to understand the real problem and the users.
- **Look at the FileNet repository** as a user would, to see what metadata exists today.
- **If the iCertis tenant still exists, get read access** and see what was built.
- **Consider one vendor demonstration** of a current Leader platform. It calibrates what "standard" looks like and gives the build-versus-license comparison a reference point. It commits nothing.

# Glossary

| Term | Meaning |
|---|---|
| Company paper / counterparty paper | Contract drafted on Wesco's template versus on the customer's or supplier's template. Counterparty paper needs more Legal review |
| Redline | Tracked changes showing proposed edits during negotiation |
| Clause library | Approved standard clauses and permitted fallback positions that templates draw on |
| Playbook | Legal's guidance on which deviations are acceptable and who may approve them |
| MSA, SOW, amendment, addendum | Master agreement setting general terms; statement of work for a specific engagement; formal change; supplementary terms. Epic 7 manages the parent-child "contract family" among them |
| Obligations | Commitments in an executed contract (SLAs, minimum purchases, stock levels, notice periods) that someone must perform and evidence |
| Delegation of authority (DoA) | Who may approve what, at which value or risk level |
| Segregation of duties (SoD) | Controls preventing one person from both requesting and approving, for example |
| RBAC / ABAC | Access by role, or by attributes such as business unit, region, customer or contract side |
| Bill & Hold | Customer is invoiced but takes delivery later; revenue recognition depends on specific contract terms |
| Customer-Owned Product | Inventory Wesco holds that belongs to the customer; affects inventory and revenue accounting |
| CPQ | Configure, price, quote: the sales pricing and quoting system |
| FileNet | IBM enterprise content management platform; Wesco's contract repository as reported |
| IPE | Information produced by the entity: reports used as audit evidence, which must be shown to be complete and accurate |
| ITGC | IT general controls: access, change management and operations controls auditors test on SOX-relevant systems |
| SOC report / CUEC | Third-party assurance report on a vendor's controls; complementary user entity controls Wesco must operate in return |
| WOPI | Microsoft's protocol for embedding Word for the web in another application |

# Source files

| File | Location | Weight |
|---|---|---|
| Enterprise CLM Scope (Nanda) | `Products/CLM/Enterprise_CLM_Scope_Augmented_with_Prior_Requirements.docx` | Authored scope; "an evolving doc" |
| CLM High Level Process Flow (Nanda) | `Products/CLM/CLM_Process_Module_Flow.jpg` | Companion visual; only source for Epic 24 and the SOX layer |
| Email chain with Chris' Copilot notes | `Products/CLM/Email_Fw_CLM Doc.pdf` | Copilot summary of one call; figures and roles reported, not confirmed |
| CLM product file | `Products/CLM/CLM.md` | EOS front door; epic map and risks |
| Capacity and Skills Assessment v2 | `Deliverables/CLM/2026-09-28_CLM_Capacity_and_Skills_Assessment.md` | Team, cost and AOP terms |

**External sources**

- Gartner 2025 Magic Quadrant Leaders, per vendor announcements: [Docusign](https://www.docusign.com/blog/docusign-clm-named-a-leader-in-gartner-magic-quadrant-for-contract-lifecycle-management), [Agiloft](https://www.prnewswire.com/news-releases/agiloft-named-a-leader-in-the-2025-gartner-magic-quadrant-for-contract-life-cycle-management-302615410.html), [Ironclad](https://www.prnewswire.com/news-releases/ironclad-named-a-leader-in-the-2025-gartner-magic-quadrant-for-contract-life-cycle-management-for-third-consecutive-year-302615851.html), [Sirion](https://www.businesswire.com/news/home/20251114626620/en/Sirion-Named-a-Leader-in-2025-Gartner-Magic-Quadrant-for-Contract-Lifecycle-Management-for-Fourth-Consecutive-Year), [Malbek](https://www.malbek.io/blog/gartner-mq-ceo-insights)
- Icertis as a Leader in 2023 and 2024: [Icertis, 2024](https://www.icertis.com/company/news/icertis-named-a-leader-in-2024-gartner-magic-quadrant-for-contract-life-cycle-management/), [Icertis, 2023](https://www.icertis.com/company/news/icertis-named-a-leader-in-2023-gartner-magic-quadrant-for-contract-life-cycle-management/)
- First-CLM replacement rate and failure causes: [Elevate, citing MGI Research 2025 CLM Buyer's Guide](https://elevate.law/expertise/clm-implementation-challenges-why-40-of-enterprise-deployments-fail/); [Bind, CLM market report](https://bindlegal.com/resources/guides/clm-market-report-gartner-forrester/)
- Oracle Procurement Contracts capabilities: [Oracle datasheet](https://www.oracle.com/assets/procurement-contracts-cloud-ds-3013238.pdf)
- Word for the web integration: [Microsoft Cloud Storage Partner Program](https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/online/apply-for-cspp-program)
