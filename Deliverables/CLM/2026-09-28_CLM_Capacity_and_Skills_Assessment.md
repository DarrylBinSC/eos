---
title: "Contract Lifecycle Management: Capacity and Skills Assessment"
date: "2026-09-28 (v2)"
author: "Darryl Benson"
---

> **Status 2026-10-01:** CLM was not adopted in the FY27 AOP and will not be built in 2027. This document is retained as reference if CLM returns in a later cycle.


# Summary

CLM can be built by a CSS Platforms team, and the reported $1.2M covers the labor for Release 1. Money isn't the constraint. What the AOP decision has to settle is where the team comes from, whether the funding moves with the work, and who owns the product.

The option now under discussion answers the first question well. Moving CDA to the entroCIM team frees the CDA development pod (about 5.75 FTE of developers, UX and QA, already staffed) to form the core of a CLM team of about 13. That removes most of the hiring lead time. It only works if CDA's FY27 scope is reset to validation and pilot on existing entroCIM capabilities, since the entroCIM team has already reset its 2027 roadmap to a reduced cadence.

Two further points shape the estimate:

- The 24 epics are not 24 modules to build. They resolve into a core application, a set of integration adapters, and journeys (buy-side, sell-side) that should be configuration of the core. Designed that way, the build effort sits in the core and the adapters, and adding Real Estate, IP or other contract areas later is configuration work.
- AI-assisted development (Claude Code, which Ron's team already has) can shorten the build. Published evidence ranges from a slowdown to about a quarter more work completed, so we should measure the gain on CLM itself during discovery rather than assume it in the plan.

Recommended terms for the decision:

1. Build moves to Digital Products, with the $1.2M transferred or a chargeback agreed before work starts.
2. CDA moves to the entroCIM team, with CDA's FY27 scope reset to validation and pilot, and the CDA pod's cost moving to the CLM line.
3. A CLM team of about 13: the CDA pod plus about 1.5 FTE already unallocated, plus authority for about 6 new FTE, mostly India.
4. Nanda's organization provides the business product owner and the Oracle, Dynamics and FileNet integration SMEs.
5. A six-week discovery gate before the eight-month build: iCertis post-mortem, build-versus-configure comparison, a sized Release 1 backlog, SOX scoping, and a measured Claude Code pilot on a thin slice of the core.

# What is being asked of the team

The scope defines about 24 epics, one shared platform and two journeys (buy-side for Procurement and Sourcing, sell-side for Sales), released in three stages. Release 1 is the eight-month MVP: intake, contract workspace, Word-based authoring and preview, approvals, security and audit, one buy-side and one sell-side journey, e-signature (Nitro / DocuSign), handoff to the existing repository (FileNet), and CLM search.

Release 2 adds clause-level workflow, Oracle Procurement and Dynamics/CPQ/billing integration, contract families, Outlook, mobile and reporting. Release 3 adds Contract Intelligence, obligations, the Inventory Planning handoff and analytics.

# Architecture: core application versus use models

Read as architecture, the epics fall into three layers.

| Layer | What it is | Epics | Build character |
|---|---|---|---|
| Core application | Contract record and domain model; workflow and task engine; approval and policy engine (routing matrices, delegation of authority, segregation of duties); document service (templates, Word co-authoring, versions, redlines, preview); access control and collaboration zones; audit and evidence; configuration; search, notifications and reporting | 1, 2, 3, 4, 5, 7, 8, 9, 10, 24 | Built once. Where most of the engineering is |
| Integration adapters | Connections to systems CLM does not own | 6 e-signature, 14 Oracle Procurement and supplier master, 19 Dynamics, CPQ, order and billing, 21 FileNet, 22 Contract Intelligence, 23 data synchronization, identity, analytics, Inventory Planning handoff | Built per system. Depends on other teams for access and test environments |
| Use models | Buy-side and sell-side journeys: contract types, intake forms, templates, routing and approval rules, participants | 11, 12, 13, 15 (buy); 16, 17, 18, 20 (sell) | Should be configuration of the core, with limited journey-specific logic |

This changes the plan in four ways.

- Effort. The epic count overstates the build in one respect (eight of the epics should be mostly configuration) and understates it in another (Word co-authoring in Epic 3 and clause-level parallel review in Epic 5 are the hardest engineering in the scope). Sizing should follow the layers, not the epic count.
- Release 1. The scope puts one journey from each side in Release 1. Framed this way, Release 1 is the core, the three adapters it needs (e-signature, repository, identity) and one use model, sell-side first because it is the stated priority. The second use model then becomes the test of the architecture: if buy-side needs substantial new code rather than configuration, the core was built wrong.
- Scope growth. Real Estate and IP are named in the business need and fit neither journey. In a configuration-first core they are new use models, not new development projects.
- Build versus buy. The core is what commercial CLM products sell. The adapters and the use-model configuration are needed whichever way we go. So the real comparison is building the core versus licensing it, and the discovery gate should frame it that way.

# Current capacity and the CDA option

The FY27 plan carries 71 people across five reporting teams. The Digital Products organization accounts for 34 of them, allocated almost entirely to entroCIM (20.0 FTE) and CDA (7.0 FTE). About 1.5 FTE is unallocated (a development architect and half a scrum master).

The CDA pod:

| CDA role today | FTE on CDA | Fit for CLM |
|---|---|---|
| Back-end architect | 1.0 | Solution architect for the core |
| Back-end developers | 2.0 | Core and adapters |
| Front-end developers (one senior) | 2.0 | Intake, workspace, Sales-facing experience |
| Front-end architect (shared with entroCIM) | 0.5 | Stays with entroCIM in this option |
| UX analyst (shared with entroCIM) | 0.5 | Moves; CLM needs a full UX role |
| QA developer (shared with entroCIM) | 0.25 | Moves |
| Support engineer, product owner (shared) | 0.75 | Stay with CDA/entroCIM |

About 5.75 FTE transfers. The developers' skills are general web engineering and carry over. Their platform-specific experience (SkySpark and entroCIM components) does not, and none of them has CLM, contract-process or Oracle/Dynamics experience.

The case for moving CDA to the entroCIM team is architectural as much as organizational. CDA already runs on SkySpark and many of the entroCIM components, so the entroCIM team maintains most of what CDA depends on. The condition is scope. CDA does not yet have a named business sponsor, and its business case already staffs production only after pilot economics are proven. A validation-and-pilot scope on existing entroCIM capabilities is a reasonable FY27 target for the entroCIM team. The full FY27 CDA build plan is not, on a team that has just reset to two major releases a year.

Two things need to be explicit in the decision so that nothing is funded twice or not at all:

- The CDA pod's cost (about $323K a year in the FY27 plan) moves to the CLM line.
- CDA's FY27 AOP line is re-stated for the reduced scope.

# Skills: what we have and what CLM needs

| Skill area | CLM need | Source |
|---|---|---|
| Web application development, architecture, UX, QA | Core of the build | CDA pod and unallocated architect |
| Contract, legal and procurement process knowledge (P2P, O2C) | Requirements, workflow and rule design, acceptance | Nanda's organization, Legal, Procurement, Sales Operations |
| Oracle Cloud Procurement and Dynamics integration | Epics 14 and 19 | Corporate Applications SMEs |
| FileNet repository integration | Epic 21, Release 1 | Corporate Applications SMEs |
| Word-based document authoring and redlining | Epic 3, Release 1 | Gap. The most specialized engineering in Release 1; candidate for early proof in discovery |
| E-signature API integration | Epic 6, Release 1 | Gap; well-documented APIs, a good fit for AI-assisted development |
| Identity, role and attribute-based access, legal privilege separation | Epic 9 | Partial |
| SOX-compliant delivery (change control, test evidence, access certification) | Epic 24, if CLM is in SOX scope | Partial; Internal Audit to scope |

# Team required

Planning estimates built from the scope and the architecture above, not from a sized backlog. Costs use the FY27 plan's own rates: $22/hour India, $94/hour North America, 1,880 hours a year.

| Role | Baseline (no AI assumption) | CDA pod core, AI-assisted hypothesis |
|---|---|---|
| Product owner (NA) | 1 | 1 |
| Business analysts (1 NA, 1 India) | 2 | 2 |
| Solution architect | 1 | 1 (CDA pod) |
| Integration lead | 1 | 1 (unallocated architect) |
| Back-end developers | 4 | 2 (CDA pod) |
| Front-end developers | 2 | 2 (CDA pod) |
| UX designer | 1 | 1 (0.5 CDA pod, 0.5 new) |
| QA / SDET | 2 | 1.5 (0.25 CDA pod) |
| DevOps / platform | 1 | 0.5 |
| Scrum master | 0.5 | 0.5 (unallocated) |
| Security / identity | 0.5 | 0.5 |
| Total FTE | 16 | 13 |
| of which already in the organization | about 1.5 | about 7.25 |
| of which new | about 14.5 | about 5.75 |

| Labor cost | Baseline | CDA pod core, AI-assisted |
|---|---|---|
| Annual run rate | $932K | $808K |
| Eight-month Release 1 | $622K | $539K |

The difference between the two columns is three FTE: two back-end developers, half a QA role and half a DevOps role. That is the part of the plan that depends on the AI-assisted gain being real. The rest of the reduction in new hiring comes from the CDA pod, not from AI.

After Release 3, CLM needs a standing team for configuration, integration support and user support. On the pattern used in our other plans, assume about half the build team is retained.

# Validating the estimate with Claude Code

Nanda expects the product owners and developers to use Claude Code to shorten development, and all of Ron's team already has access. The expectation is reasonable, but the size of the gain is not known, and Sean has asked for AI benefits to be measured rather than claimed.

What the published evidence says:

| Study | Setting | Result |
|---|---|---|
| Cui, Demirer et al., three field experiments (Microsoft, Accenture, a Fortune 100 firm), Management Science 2025 | About 4,900 developers in their normal work, AI code assistant | About 26% more tasks completed; larger gains for less experienced developers |
| METR randomized trial, July 2025 | Experienced developers on their own mature codebases, early-2025 AI tools | 19% slower, while the developers believed they were about 20% faster |

Both studies predate current agentic tools like Claude Code, and neither studied a greenfield enterprise build. The honest reading is that the gain depends on the work and the team, and that developers' own estimates are not reliable evidence of it.

Where the gain should show up on CLM: scaffolding the core, building adapters against documented APIs (DocuSign, Oracle REST, Dynamics), generating tests (which also produces SOX test evidence), documentation, and turning business rules and approval matrices into configuration. Product owners and analysts can use it to turn requirements into stories and acceptance criteria.

Where it will not: decisions that belong to Legal, Controllership and Sales; access to Oracle, Dynamics and FileNet test environments owned by other teams; security review; SOX evidence review; user acceptance; and Sales adoption. These are on the critical path and set the floor on the schedule.

Proposed method, inside the discovery gate:

1. The CDA pod builds a thin vertical slice of the core with Claude Code over two to three weeks: intake, workspace, one approval route, an e-signature call and a repository handoff (stubbed where environments are not available).
2. Measure against the sized backlog: throughput per sprint, defects found in QA, rework, and cycle time from story to done. These are the measures Sean named.
3. Set the Release 1 team size from the measured result, between the two columns above.

This also tests the architecture and gives the build-versus-buy comparison a data point: if the core slice comes together quickly and cleanly, building the core becomes more credible.

For the AOP, ask for staffing authority at the 13-FTE level with a stated contingency to 16 if the pilot does not show the gain. Do not ask for 13 as though the gain were proven.

# Why a discovery gate before the build

An iCertis effort was attempted before this and did not succeed, and no record says why. If it failed on process ownership, adoption or data rather than on the tool, a custom build carries the same causes forward.

Six weeks with the core four (product owner, architect, business analyst, integration lead), plus the CDA pod on the Claude Code pilot, produces:

1. The iCertis post-mortem, from Controllership and Nanda's team
2. A build-versus-license comparison for the core
3. A sized Release 1 backlog, organized by core, adapters and use models
4. SOX scoping with Internal Audit
5. A measured AI-assisted productivity figure for this team on this work

If the gate confirms the custom build, the same people carry straight into Release 1, and the pilot code becomes the start of the core.

# Risks

- Funding does not move with the work, and CLM is built on existing capacity by default.
- CDA momentum. The sponsor and commercial conversations for CDA are active now; a reduced FY27 scope needs to be explained to them, not discovered by them.
- entroCIM absorbs CDA on top of a roadmap that has just been reduced. The rationalization has to name what comes out.
- Word-based authoring and redlining (Epic 3) is the hardest engineering in Release 1.
- Integration partners are outside our organization and set part of the schedule.
- Sales adoption. Success with trained Sourcing users does not prove usability for Sales.

# Decisions needed at the AOP meetings

| Decision | Recommended answer |
|---|---|
| Does CLM build move to Digital Products? | Yes, with the terms below attached |
| Does the $1.2M move with it? | Yes, or a chargeback agreed before work starts |
| CDA | Moves to the entroCIM team; FY27 scope reset to validation and pilot; CDA pod cost moves to CLM |
| Staffing authority | About 6 new FTE on top of the CDA pod and unallocated staff (13 total), contingency to 16 pending the AI pilot |
| Nanda's role | Business product owner and source of integration SMEs |
| Product Executive seat | Darryl Benson |
| Start condition | Six-week discovery gate, then the eight-month Release 1 build |

Takeaway: moving the CDA pod gives CLM a ready team core. The build can start as soon as the funding moves, the CDA scope is reset, and the discovery gate confirms the approach.

---

Notes for Darryl (remove before sharing):

- v2 replaces v1 from earlier today. It adds the CDA option, the core/adapter/use-model architecture, and the Claude Code validation method. v1 is kept as SUPERSEDED_ in the same folder.
- CDA pod names: Narendra Singh (back-end architect), Abhishek Savanur and Sai Kiran Vadluri (back-end), Shubham Kumar Singh and Nisha More (front-end), with Harsha E (UX) and Shreyans Saklecha (QA) shared with entroCIM. The unallocated architect is Chethan GR and the half-time scrum master is Sakshi Mathur. None of them has been asked.
- Rates are derived from the FY27 staffing plan and reproduce its totals exactly. The CDA pod's $323K is the FY27 plan figure. CDA's submitted AOP build figure was $246,787; the two are different bases, so check which one the AOP conversation uses.
- The AI-assisted column is a hypothesis. It removes three FTE from the baseline and nothing more, so it can be checked against the pilot directly.
- Keeping Priyatosh Patra (front-end architect) with entroCIM is my assumption, since he is split 50/50. If he moves with the pod, entroCIM loses its front-end architect.
- This version names the CDA scope reset in a document Sean may see. If you want to raise it with him verbally first, move the CDA rows to a spoken point.
