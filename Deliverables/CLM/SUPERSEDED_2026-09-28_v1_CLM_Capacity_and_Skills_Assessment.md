---
title: "Contract Lifecycle Management: Capacity and Skills Assessment"
subtitle: "Input to the FY27 AOP decision"
date: "2026-09-28"
author: "Darryl Benson"
---

# Summary

CLM can be built by a CSS Platforms team, and the reported $1.2M covers the labor for Release 1 at our current delivery mix. Money isn't the constraint. The constraints are three things the AOP decision has to settle: the funding has to move with the work, the team needs skills it does not have today, and CLM needs its own product owner and delivery lead rather than being added to leaders who already carry entroCIM, WAM and CDA.

If CLM is absorbed into existing capacity without those terms, it will be staffed from entroCIM and CDA by default, and all three will slip.

Recommended terms for the decision:

1. The $1.2M transfers to Digital Products with the build, or a chargeback is agreed before work starts.
2. Authority to staff a dedicated CLM team of about 16 FTE, weighted to India delivery, with a small core seeded from the existing organization.
3. Nanda's organization provides the business product owner and the Oracle, Dynamics and FileNet integration SMEs, since it owns those systems.
4. A six-week discovery gate before the eight-month build clock starts: a written account of why the iCertis effort failed, a build-versus-configure comparison, a sized Release 1 backlog, and SOX scoping with Internal Audit.

# What is being asked of the team

The scope defines about 24 epics across one shared platform and two journeys (buy-side for Procurement and Sourcing, sell-side for Sales), released in three stages. The eight-month MVP is Release 1:

- Shared foundation: intake, contract workspace, authoring with Word editing and in-system preview, approvals, security and audit
- One buy-side and one sell-side journey
- E-signature orchestration (Nitro / DocuSign)
- Handoff of executed contracts to the existing repository (FileNet)
- CLM record search

Release 2 adds clause-level workflow, Oracle Procurement and Dynamics/CPQ/billing integration, contract families, Outlook, mobile and reporting. Release 3 adds Contract Intelligence, obligations, the Inventory Planning handoff and analytics.

Two features of this scope drive the skill mix more than its size does. It integrates with systems our team has never worked in (Oracle Cloud Procurement, Microsoft Dynamics, FileNet, DocuSign), and its users include a broad, occasional-use Sales population, so the usability standard is higher than for an expert tool.

# Current capacity

The FY27 plan carries 71 people across five reporting teams. The Digital Products organization accounts for 34 of them, allocated almost entirely to entroCIM (20.0 FTE) and CDA (7.0 FTE).

| Available today in the FY27 plan | FTE | Note |
|---|---|---|
| Digital Products allocated FTE vs. headcount | 4.5 unallocated | Mostly fractional; not a ready team |
| Development architect (India), unallocated | 1.0 | Candidate CLM solution architect |
| Scrum master (India), half unallocated | 0.5 | Candidate CLM delivery support |
| Resources moving out of entroCIM development | about 9 (estimate) | Final count not yet confirmed; most appear to be the CDA pod already |

There is no spare team. Anything beyond about two people comes either from new staffing or from taking capacity off entroCIM or CDA. entroCIM has just reset its 2027 roadmap to a reduced cadence, and CDA is a funded FY27 product, so neither has capacity to give up without a decision that says so.

Leadership is the tighter constraint. The same product owner covers entroCIM, WAM and CDA, and the same development director covers entroCIM and CDA. CLM should not be the fourth product on either.

# Skills: what we have and what CLM needs

| Skill area | CLM need | Current team |
|---|---|---|
| Web application development (front and back end) | Core of the build | Strong. CDA and entroCIM pods, India delivery model |
| Architecture, QA, UX | Core | Present; UX depth matters more here because of occasional Sales users |
| Contract, legal and procurement process knowledge (P2P, O2C) | Requirements, workflow design, acceptance | Not present. Must come from Nanda's organization, Legal, Procurement and Sales Operations |
| Oracle Cloud Procurement and Dynamics integration | Epics 14 and 19 | Not present. Owned by Corporate Applications |
| FileNet repository integration | Epic 21, Release 1 | Not present |
| Word-based document authoring and redlining | Epic 3, Release 1 | Not present. Specialized, and the largest single technical risk in Release 1 |
| E-signature API integration | Epic 6, Release 1 | Not present in the development team |
| Enterprise identity, role and attribute-based access, legal privilege separation | Epic 9 | Partial |
| SOX-compliant delivery (change control, test evidence, access certification) | Epic 24, if CLM is in SOX scope | Partial. Adjacent experience from customer cyber-control work; not ITGC-grade |

The gaps are in domain and in enterprise integration, not in core engineering. That is why the integration SMEs should come from the organization that owns those systems, and why the business product owner should sit with Nanda.

# Team required

A planning estimate built from the scope document, not from a sized backlog. The discovery gate replaces it with a sized plan. Costs use the FY27 plan's own rates: $22/hour India, $94/hour North America, 1,880 hours a year.

| Role | Lean: sell-side first | Recommended: both journeys, shared foundation | Full parallel: two product teams |
|---|---|---|---|
| Product owner (NA) | 1 | 1 | 2 |
| Business analyst (NA, India) | 1 | 2 | 2 |
| Solution architect | 1 | 1 | 1 |
| Integration lead | 1 | 1 | 1 |
| Back-end developers | 3 | 4 | 6 |
| Front-end developers | 1 | 2 | 3 |
| UX designer | 0.5 | 1 | 1 |
| QA / SDET | 1.5 | 2 | 3 |
| DevOps / platform | 0.5 | 1 | 1 |
| Scrum master | 0.5 | 0.5 | 1 |
| Security / identity | 0 | 0.5 | 0.5 |
| **Total FTE** | **11** | **16** | **21.5** |
| of which North America | 2 | 2 | 3 |

| Labor cost | Lean | Recommended | Full parallel |
|---|---|---|---|
| Annual run rate | $726K | $932K | $1.30M |
| Eight-month MVP | $484K | $622K | $866K |

At the recommended level, the eight-month build uses about half of the $1.2M and a full year uses about 78%. That leaves room for non-labor costs (hosting, e-signature volume, tooling) that no source has sized yet. The full-parallel option, which the scope document recommends because buy-side and sell-side behave like two products, reaches the $1.2M in a year with no allowance for non-labor costs.

After Release 3, CLM needs a standing team for configuration (templates, approval matrices, routing rules), integration support, and user support for a large Sales population. On the pattern used in our other plans, assume about half the build team is retained. That is a recurring cost the business case should carry.

# Why a discovery gate before the build

An iCertis effort was attempted before this and did not succeed. No record says why. If it failed on process ownership, adoption or data rather than on the tool, a custom build carries the same causes forward and adds the cost of building and maintaining the software ourselves.

Much of what the scope describes is the core of mature commercial CLM products, and the architecture choice (custom build, low-code on our existing Microsoft platform, or configuring a commercial product) changes the team we need more than any other decision. Six weeks with the core four (product owner, architect, business analyst, integration lead) costs about $60K. It produces four things:

1. The iCertis post-mortem, from Controllership and Nanda's team
2. A build-versus-configure comparison against the Release 1 scope
3. A sized Release 1 backlog, which replaces the estimate above
4. SOX scoping with Internal Audit, which decides whether change control and test evidence are ITGC-grade from day one

If the gate confirms the custom build, the core four become the leadership of the build team and nothing is lost.

# Risks

- Funding does not move with the work. The build then lands on existing entroCIM and CDA capacity by default.
- Hiring lead time. The eight-month clock should start when the team is in place, not when the decision is made.
- Word-based authoring and redlining (Epic 3) is in Release 1 and is the most specialized engineering in the scope.
- Integration partners are outside our organization. Oracle, Dynamics, FileNet and the Contract Intelligence service all have their own owners and roadmaps.
- Sales adoption. The scope itself notes that success with trained Sourcing users does not prove usability for Sales.

# Decisions needed at the AOP meetings

| Decision | Recommended answer |
|---|---|
| Does CLM build move to Digital Products? | Yes, with the terms below attached |
| Does the $1.2M move with it? | Yes, or a chargeback agreed before work starts |
| Staffing authority | About 16 FTE, India-weighted; core seeded from the existing organization |
| Nanda's role | Business product owner and source of integration SMEs |
| Product Executive seat | Darryl Benson |
| Start condition | Six-week discovery gate, then the eight-month Release 1 build |

Takeaway: we can build CLM, provided the funding, the staffing authority and a dedicated product owner come with the assignment.

---

Notes for Darryl (remove before sharing):

- Team sizes are my planning estimate from the scope document and the epic map, not a sized backlog. The rates are derived from the FY27 staffing plan and reproduce its totals exactly (for example, WAM 19 India FTE at $785,840).
- The unallocated architect is Chethan GR and the half-time scrum master is Sakshi Mathur, both in the FY27 staffing plan. Neither has been asked.
- "About 9 resources moving out of entroCIM" is still the unconfirmed estimate from the 2026-09-16 roadmap discussion. Comparing the 2026 and FY27 plans suggests most of them are the CDA developers, which is why I have not counted them as available.
- The discovery gate cost assumes two NA and two India roles for six weeks.
- I have not used Nanda's or Merwan's staffing because nothing in the record describes it. If Nanda has people or contractors on CLM today, that changes the Current capacity section.
- The Product Executive recommendation is yours to confirm. The body names you; delete that row if you would rather Sean raise it.
