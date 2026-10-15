# Soft Metrics Backing Document — FY27 Portfolio

**Date:** 2026-08-26
**Companion to:** `2026-08-26_Product_Pitches_and_Soft_Metrics.md` and the slide deck of that name
**Status:** Owners below are **proposed, not confirmed**. Every name is an inference from role, not a commitment anyone has given

## Why this document exists

Names are deliberately kept off the slides (Darryl, 2026-08-26). The slides carry the metric; this document carries who produces the number, from which system, and what still has to be true for the number to exist. A metric with no named producer is a metric that will not be reported in month two.

## How to use it

Each metric below has a production step, which is the actual monthly action someone takes. When owners are confirmed, replace "Proposed" with the agreed name and date. Where a confirmation is outstanding, the metric is reportable only in principle.

---

## entroCIM

| # | Metric | Source system | Proposed owner | Monthly production step | Status |
|---|---|---|---|---|---|
| 1 | Platform availability | Wesco-hosted instance monitoring | Ron Snyder (delivery and release) | Pull monthly uptime per hosted instance, compare against the committed Managed Services service level, report aggregate and any instance below level | Measurable now |
| 2 | Licensed point utilization | License records plus platform telemetry | Product with commercial input (David Blondel, Nathan Kehr) | Points licensed against points in active service, stated with the covered proportion of the estate | Measurable now. Coverage proportion must be stated each month, not assumed |
| 3 | Net licensed point movement | License and renewal records | Commercial and Sales Operations (Nathan Kehr, Tom Boss) | Points added within existing customers less points lost in the month; renewal rate recalculated on a rolling twelve months | Measurable now |
| 4 | Containerized deployment coverage | Deployment record | Deployment and delivery (Chad Steger, Ron Snyder) | Count active instances on the containerized model against total active instances | Measurable now. Opens at or near zero; testing began around 2026-08-17 |

**Coverage caveat that must travel with metrics 1 and 2.** Wesco-hosted deployments are fully measurable. Customer-hosted deployments are measurable only where connectivity allows. The covered proportion is stated at each report rather than implied, which is the same discipline used in the AOP submission.

---

## Wesco Asset Management

| # | Metric | Source system | Proposed owner | Monthly production step | Status |
|---|---|---|---|---|---|
| 1 | Renewal signal yield | ADM notification analytics reporting | Akansh Gangil (ADM), with Sales Operations for the action side | Notifications issued in the month; of those, count assigned and count converted to a quoted opportunity within 30 days | Measurable now. Notification analytics shipped in the 2026-08-17 production release |
| 2 | Managed record completeness | ADM | Akansh Gangil with product (David Blondel) | Records under management carrying all four core attributes, as a percentage of records under management | **Blocked on definition.** Core attribute set must be named first |
| 3 | Supplier and purchase-history coverage | ADM against the in-scope supplier list | Supplier data with ADM (Natalie Marquardt, Akansh Gangil) | In-scope suppliers with purchase history ingested, over total in-scope suppliers | **Blocked on denominator.** The in-scope supplier list must be fixed and dated, or the percentage moves for the wrong reasons |
| 4 | Automated ingestion rate | ADM audit trail | Akansh Gangil | Records created by automated feed over total records created in the month | **Confirmation required.** Assumes the audit trail distinguishes automated from manual creation. Not verified |

**Definitional decisions still open.**

1. **Core attribute set for metric 2.** Proposed: manufacturer part number, product type, license or warranty term, expiration date. Note that P360 governance declined product type as a global attribute (2026-08-10) and it is being collected outside P360 by workaround. Including it means the metric will show the governance gap rather than hide it, which is the intent.
2. **"Acted upon" for metric 1.** Assigned is safe to report and weak in meaning. Converted to a quoted opportunity is meaningful and depends on Sales Operations discipline outside product control. Both counts are reported and the ratio left to speak, rather than choosing one and defending it.
3. **Fallback for metric 4** if the audit trail cannot separate automated from manual: customer onboarding cycle time, median days from customer data receipt to normalized data live in Strev. Monthly volume may be too low to read, which is why it is the fallback and not the first choice.

---

## Ascent Navigator

| # | Metric | Source system | Proposed owner | Monthly production step | Status |
|---|---|---|---|---|---|
| 1 | Maximo dependency remaining | Navigator 2.0 release record | Ascent product development (DJ Vaughn) | Count how many of the six core operational functions still run on Maximo | Measurable now |
| 2 | Planned maintenance completion | Navigator / Maximo work management | Ascent operations | Scheduled maintenance tasks completed inside their window over tasks scheduled in the month | **Confirmation required** |
| 3 | Asset record completeness | Navigator asset register | Ascent operations | Managed assets with identity, location, maintenance program assignment and contract or warranty linkage, over total managed assets | **Confirmation required** |
| 4 | Facility coverage | Ascent operations | Ascent operations | Facilities operated on the platform; of those, how many on multi-tenant rather than a dedicated instance | Measurable now |

**The six core operational functions** for metric 1, per the FY27 AOP submission: asset visibility, asset financials, contract and vendor management, MRO work order and ticketing, business financials, document management.

**Reporting-line risk, and it is the material one on this product.** Every Navigator metric is produced inside Ascent's operation. Darryl is Product Executive but does not control the reporting line, so a monthly cadence depends on DJ Vaughn or Lisa Orton committing to supply the numbers. This should be landed as an explicit ask rather than assumed, because a metric that arrives late once tends to arrive late permanently.

---

## Connected Device Assurance

No metric is measurable before 2Q27. The investment is not approved and the work has not started. Owners below apply from the point work begins.

| # | Metric | Source | Proposed owner | Monthly production step | First report |
|---|---|---|---|---|---|
| 1 | Device family qualification | Manufacturer qualification record | CDA product with Supplier Relations | Count device families with confirmed firmware access, update mechanism and managed-service rights | 2Q27 |
| 2 | Launch dependency closure | Dependency register | Brad Stevens (business lead) with CDA product | Count dependencies closed against the fixed denominator of five | 2Q27 |
| 3 | Service capability demonstrated | Development and test record | CDA engineering | Count how many of identify, monitor, manage and execute run end to end on a qualified device family | 2Q27 |
| 4 | Pilot commitment, then account expansion | Commercial pipeline | Commercial with Managed Services | Named pilot customers committed; contracted device count against the 250 to 1,000 camera pilot basis | 2Q27 |

**The five launch dependencies** forming the denominator of metric 2: partner sensor agreement; connectivity and credential architecture; liability and service level language; pricing and margin model; Sales sponsorship with a named pilot customer. If the denominator changes, say so in the report rather than silently re-basing the percentage.

**Transition rule.** At first pilot connection the five submitted AOP service KPIs begin. Metric 2 retires at pilot start, metric 3 after pilot completion, metrics 1 and 4 continue permanently.

---

## Consolidated open items

| # | Item | Product | Needed from | Blocking? |
|---|---|---|---|---|
| 1 | Confirm named metric owners | All | Darryl | Yes, for monthly operation |
| 2 | Define the core attribute set | WAM | Product and ADM | Yes, for metric 2 |
| 3 | Fix and date the in-scope supplier list | WAM | Supplier data and ADM | Yes, for metric 3 |
| 4 | Confirm ADM audit trail separates automated from manual creation | WAM | ADM | Yes, for metric 4 |
| 5 | Commitment to supply four metrics monthly | Navigator | Ascent (DJ Vaughn, Lisa Orton) | Yes, for the whole product |
| 6 | Confirm Navigator work management can report planned maintenance completion and asset record completeness | Navigator | Ascent | Yes, for metrics 2 and 3 |

## Change record

| Date | Change |
|---|---|
| 2026-08-26 | Created alongside the pitches and metrics document. All owners proposed, none confirmed |
| 2026-10-13 | First WAM data point, from Sales Operations' October ADM scorecard (Natalie Marquardt). Metric 1: 1,337 notification line items to 238 reps (North America, Darryl's working assumption 2026-10-13); acted-upon-within-30-days rate not reported. Sales figure in the deck ($697K) is North America only, August and September. Metric 3: dated roster of 35 suppliers live, 4 targeted Q4 2026, which largely addresses open item 3. Owners still unconfirmed. Detail in `Products/WAM/WAM.md`, 2026-10-13 |
