# FRB BP43 Smart Building Bid: Review of Turner's Answers to Wesco's Six Questions

Reviewer: Claude, for Darryl Benson
Date: 2026-10-20
Source: Turner Construction (Dayana Sayritupac, Procurement Agent, NJ Business Unit) reply of 2026-10-20 09:14 to Sarah Monteleone's six questions of 2026-10-16, forwarded by Sarah to Leanne Gordon and Valli Poornakumar (cc Chad Steger, Darryl Benson, Syed Zaidi). Original email saved as `Evidence/Email_FRB_BP43_Turner_Bid_Answers_2026-10-20.pdf`.
Deadline: Wesco's response is due 2026-10-21 (Sarah, confirming `Registers/watch/W026.md`).
Register home: `W026` (FRBNY Smart Building bid). This file is reference material only.

## Bottom line

Turner answered all six questions and the bid remains open to Wesco. Two of the six answers remove obstacles (perpetual licensing, BIM modeling under B37). Three add scope Wesco had assumed was the Owner's or outside its offer: restroom gateways under Add Alternate H1, four construction-phase laptops plus a temporary access portal under C51, and COBie ingestion with 3D model navigation under C1.1. The gateway point Darryl asked about is confirmed, with one correction on attribution and scope, below.

## The gateway statement

Darryl's note was that Sarah stated Wesco needs to supply gateways. The record is slightly different and the difference matters for pricing:

- Sarah asked Turner on 2026-10-16: "Please clarify who will be providing the gateways" (C44/H1, UC5.2 Optimized Building Cleaning).
- Turner answered on 2026-10-20: C44 is struck from the base scope ("marked N in Bid Supplement 01"). Under Add Alternate H1, "the Smart Building subcontractor is still requested to include furnishing and installing the gateways and associated connections required for the Restroom Management System. The smart toilet accessories and plumbing fixtures themselves are to be furnished and installed by others." Turner asks that "the gateway and associated integration costs are included in your H1 alternate pricing, separately from the base bid."

So: the gateway obligation is Turner's answer, not Sarah's statement; it sits in Add Alternate H1 only, not the base bid; and it is furnish and install, not supply alone. Installation of field gateways and their connections to fixtures is a construction-trade task, not an entroCIM integration task. The 08-19 Section 3.1 review already flagged that the Smart Restroom outputs depend on a third-party restroom platform, not entroCIM; the H1 price now has to carry hardware, installation labor, and that platform's integration, or H1 has to be qualified.

## The six answers, assessed

| # | Topic | Turner's answer | Assessment | What to do by 10-21 |
|---|---|---|---|---|
| 1 | Software licensing (perpetual vs subscription) | Enter 0 for Perpetual License and separately identify the initial startup/licensing cost; enter 0 for Annual Support (perpetual model) if not applicable; enter the 2-year subscription total following Substantial Completion with the annual cost shown separately and inclusions stated. Base bid must include all licensing costs; Deduct Alternate H3 is the credit if FRBNY procures and renews software directly. | Favorable. Turner accepted the exception and gave a clean fill-in rule. The H3 deduct is the one to watch: it signals FRBNY may take entroCIM licensing direct, which moves licensing revenue out of Turner's contract and into a direct FRBNY relationship. That is a different contracting path (FRB procurement, possibly a Wesco direct agreement) and should be priced identically to the base-bid licensing so there is no duplication and no discount by accident. | Leanne/Valli fill in per the rule. Confirm the H3 deduct equals exactly the licensing and support fees in the base. State what the annual fee includes (maintenance, support, upgrades) in the Owner's terms. Use "entroCIM licensing" throughout. |
| 2 | BIM modeling exception | B37 struck; BIM modeling and LOD 400/500 deliverables are out of BP #43. C1.1 remains: incorporate COBie asset information provided by other trades into the unified user interface, including 3D model navigation for asset and space visualization (25 00 00, 2.03 items G and H). H5 (post-occupancy BIM model updates) is an Add Alternate, subject to FRBNY's decision. | Half resolved. The modeling exception is accommodated. C1.1 is a product-capability question, not a scope question: can entroCIM ingest COBie and present 3D model navigation of assets and spaces? Wesco's own deviation row 2.03 D ("3D functionality depends on the supplied BIM/COBie model... material model remediation excluded") is still shown as "Pending Turner / Owner review." H5 is work Wesco does not do. | Ron Snyder or David Blondel confirm, before submission, what entroCIM does today for COBie ingestion and 3D navigation, so the response commits only to shipped capability. Keep the 2.03 D deviation in the response. For H5, state not offered, or price through a BIM partner if one exists; do not leave it blank. |
| 3 | Page 5, UBE percentages | Best efforts only, not contractual. Provide a percentage where applicable, otherwise 0. | Low risk. | Enter 0 unless Wesco has a lower-tier diverse supplier on this bid to claim. |
| 4 | C51, temporary access portal and laptops | FRB provides laptops only for vendor remote access post-Substantial Completion (C58, RFI 0344 #5). Under C51 the MSI still provides the temporary access portal and four onsite laptops during construction. | Contradicts what Wesco took away from the September descope meeting. Four laptops are a small cost; the portal with view and adjust access to all connected systems during construction is an early, construction-phase entroCIM deployment with its own commissioning effort and a security posture (adjust rights during construction) that needs to be priced and bounded. Note what Turner did not say: nothing in the answer confirms FRB provides the servers. Wesco's question bundled servers and laptops; the answer addresses laptops only. The server pricing thread (`C57`, Dell budgetary server pricing for FRB Cash Services) is still open. | Price C51 in the base: four laptops, portal configuration, and a stated number of construction-phase user profiles. Ask Turner in the submission cover note to confirm server provision explicitly rather than inferring it from silence. |
| 5 | C44/H1, restroom gateways | See "The gateway statement" above. | Scope Wesco did not plan for, in an alternate FRBNY may or may not take. | Price H1 as furnish and install with a named installing party (Wesco delivery team, a subcontractor, or the plumbing trade under a Wesco purchase order), or qualify H1 as gateway furnish only with installation by others. Chad Steger's call on whether the delivery team installs. |
| 6 | H2, work order management | C52 struck from the base; UC5.3 priced separately under Add Alternate H2 per Appendix B page 23, with IBM TRIRIGA as the client-provided platform. | Turner did not answer whether entroCIM's email default is acceptable, so assume it is not for H2 and price a TRIRIGA integration. The 08-19 open question still stands: is the TRIRIGA work order path a productized connector or a project-configured integration? That determines both the price and the wording. | David Blondel or Ron Snyder answer the connector-versus-configuration question before H2 is priced. Word H2 as one-way work order creation unless bidirectional is confirmed. |

## Risks

- **Scope creep into hardware and construction work (H1, C51).** Both are priced as alternates or base items that Wesco's offer did not contemplate. The exposure is margin and delivery accountability, not the win itself. Medium severity because H1 is an alternate FRBNY may not elect.
- **Capability commitment under C1.1 (COBie, 3D navigation).** Writing this as included without engineering confirmation is the kind of statement the 08-19 review warned against ("can" versus "will"). High if committed unverified; low if confirmed or deviated.
- **H3 deduct path.** If FRBNY elects H3, licensing moves to a direct FRBNY procurement. Confirm Wesco can contract that way with FRBNY before relying on it, and that the base-bid price does not assume Turner's contract terms.
- **Timing.** One business day to submission. The two engineering confirmations (C1.1, H2) are the gating items; everything else is a pricing exercise.

## What this does not settle

- Who the Wesco bid owner is. Sarah Monteleone is running the question-and-answer exchange and the response is with Leanne Gordon and Valli Poornakumar for pricing; no one is named as owner of the submission. `W026` keeps "no named owner" until stated.
- Whether FRB provides servers (silence in Turner's answer, see item 4).
- Whether the restroom gateways are Wesco-sourced hardware (a distribution sale) or a third-party restroom platform's gateways. Turner's answer does not specify the gateway type.

## Decisions that are Darryl's

None of the six answers requires Darryl's decision for the submission to go in. Two are worth his word before it does, because they commit his team's delivery capacity:

1. Whether the delivery team installs the H1 gateways, or Wesco prices install by others. Chad Steger can recommend; Darryl confirms.
2. Whether to commit to C1.1 3D model navigation on a confirmed shipped capability, or carry the 2.03 D deviation as the answer. Ron Snyder confirms capability; Darryl decides the commitment.

## Addendum, 2026-10-20 09:55 (Darryl)

- **Gateway type:** nothing in Turner's reply, Sarah's questions, Bid Supplement 01 excerpts, or the EOS record (08-19 RFP reviews, Products, registers) names the gateway type or the restroom fixture vendor. C44/H1 wording ("gateways and associated connections to toilet accessories / plumbing fixtures") reads as the fixture vendor's own sensor gateways (inference, not evidence). The smart restroom platform in Wesco's Layer 1 architecture was never named. Ask Turner to name the fixture/accessory vendor and gateway specification; price H1 as an allowance or conditional on that answer.
- **C1.1 position, stated by Darryl:** entroCIM does not support COBie ingestion or 3D model navigation; it can produce a static image of a 3D space. The 3D piece is the sticking point. The response must be a deviation (strengthen 2.03 D) with the alternatives entroCIM does provide, and optionally a partner 3D viewer priced as an alternate. Not a committed capability.

## COBie research note, 2026-10-20 10:05

Primary source: NIBS, NBIMS-US V3 COBie standard (https://www.nibs.org/cobie). COBie is a data format and process standard: a non-graphic subset of BIM, 19 relational tables, delivered as SpreadsheetML, JSON or IFC. No 3D geometry (Coordinate table holds simple orientation only). No API; file exchange only; custom fields not permitted (Attribute table instead). For entroCIM, COBie ingestion is a mapping import into the Haystack model by configuration or a loader through the documented API, a priceable service rather than a product gap. The 3D model navigation requirement (2.03 H) is separate from COBie and is the real exception. Effort to be confirmed by Ron Snyder.

## H1 install position, 2026-10-20 10:00 (Darryl direct)

The entroCIM delivery team does not install field hardware. H1 gateway installation is priced through the TS group (Matt Powers) or a third party; Sarah Monteleone obtains that price. Darryl's call 1 above is closed.

## Correction, 2026-10-20 10:05 (Darryl direct)

COBie ingestion is not a configuration service: it would require a connector built specifically for COBie by Ron Snyder's team. The response carries a placeholder price for that development. The bid is Sarah Monteleone's responsibility; Darryl's role is advisory and supporting, and messages to the group are written that way.
