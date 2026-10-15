# Product Elevator Pitches and Soft Metrics — FY27 Portfolio

**Date:** 2026-08-26
**Products:** entroCIM, Wesco Asset Management, Ascent Navigator, Connected Device Assurance
**Audience:** Internal. CSS leadership portfolio review
**Status:** FINAL, 2026-08-26. Agreed with Darryl in session and released for circulation. Source content for the slide deck of the same name
**Companion:** `2026-08-26_Soft_Metrics_Backing_Document.md` (metric owners, source systems, open confirmations)

## 1. Purpose

One page per product carrying two things: an elevator pitch that explains what the product is, what it does and how it creates value, and a small set of soft metrics that can be measured and reported every month.

This is internal content. It is not an external sales pitch, and it is not a substitute for the FY27 AOP submission. Its job is to let a Wesco leader who does not work on these products understand each one in under a minute, and then see whether it is moving.

## 2. The standard applied to all four

**Elevator pitch.** Roughly 150 words, three moves:

1. What it is. One sentence naming the category and who it serves.
2. What it does. Two or three sentences of plain capability language.
3. What it gives Wesco. Revenue, cost avoidance, differentiation or portfolio enablement, with the line between current and future capability drawn explicitly.

No external sales framing, no absolutes, no em dashes. Planned capability is stated as planned.

**Soft metrics.** Four per product, for comparability across the set. Each carries a name, a one-sentence definition including the unit, a source system, and a baseline status. Two rules govern selection:

- **Non-financial.** Revenue, margin and cost avoidance are carried in the AOP submission and the P&Ls. These metrics measure whether the product is working, not what it earned.
- **No metric that depends on permission we do not hold.** Nothing requiring a customer to agree to share results. This follows the rule set on 2026-08-17: adding a metric later puts you ahead; committing now and failing to report it is a credibility problem in the first reporting cycle.

**Cadence.** Monthly internally. The entroCIM and CDA AOP submissions commit to a quarterly cadence and that commitment is unchanged. The monthly set is a faster tempo on the same measurement, not a second promise.

**Start point.** Report what is measurable now. Metrics that require capability which does not exist yet are named with the date they begin rather than shown as zero.

## 3. entroCIM

### Elevator pitch

entroCIM is Wesco's operational technology and facility intelligence platform. It connects OT and IoT systems and devices across a customer's sites and turns their telemetry into alarming, fault detection, analytics, dashboards and reporting that operations teams act on daily. It has been in market over ten years with an established installed base, and runs on customer infrastructure or as a Wesco-hosted instance in Azure.

In the portfolio, entroCIM provides operational intelligence where WAM provides asset lifecycle and commercial intelligence, and it is the platform beneath Wesco's Intelligent Facility Services. Planned integrations will share asset and work order data with WAM and device telemetry with Ascent Navigator; Connected Device Assurance draws on the same platform and engineering team.

For Wesco it is an owned platform carrying software revenue and pull-through on the devices we sell, keeping control of the customer's operational data rather than renting it. The priority now is commercial conversion of the installed base, not product proving.

### Soft metrics

| # | Metric | Definition and unit | Maps to submitted KPI | Reportable now |
|---|---|---|---|---|
| 1 | Platform availability | Monthly uptime of Wesco-hosted instances against the committed Managed Services service level. Percent. | KPI 2, unchanged | Yes |
| 2 | Licensed point utilization | Percentage of licensed points in active service, with covered proportion stated. Target 80% or above. Percent. | KPI 1, cadence only | Yes |
| 3 | Net licensed point movement | Points added within existing customers less points lost, in the month. Renewal rate reported on a rolling twelve months rather than monthly. Count plus percent. | KPI 4, split by tempo | Yes |
| 4 | Containerized deployment coverage | Percentage of active instances running the containerized deployment model, against the mandatory direction set 2026-08-12. Percent. | New | Yes |

**Notes.**

- Renewal rate is not a monthly number. With a handful of renewals in a month it swings and reads as noise, so KPI 4 is split into a monthly count that moves and a rolling rate that means something.
- Submitted KPI 3, functional adoption depth, is deliberately absent from the monthly set because the instrumentation to measure it does not exist. It remains in the quarterly AOP commitment and joins the monthly set when it becomes measurable.
- Metric 4 opens at or near zero. Containerization testing began around 2026-08-17. The alternative held in reserve, if a near-zero metric is unwanted in a leadership review, is connected-site coverage: the percentage of licensed sites with a live data connection to Wesco.

## 4. Wesco Asset Management

### Elevator pitch

Wesco Asset Management is the CSS platform that gives Wesco and its customers a governed view of the assets, licenses, warranties and entitlements in a customer's install base. It ingests data from Wesco systems, suppliers and customers, normalizes and enriches it through ADM and the Managed Services team, and delivers it two ways: to customers through Strev inside a Managed Services engagement, and to Sales Operations as dated renewal, warranty and refresh notifications.

It also carries complex builds, the configured multi-component systems Wesco assembles and serializes, into the customer install base record. Complex builds are a key growth area, and WAM keeps them visible and serviceable after delivery.

Intelligent Asset Management Services is the customer-facing service; WAM is the platform behind it, with ADM as the data foundation and Strev as the experience layer.

For Wesco it converts install-base data we already hold into renewal and refresh demand. The platform is production-ready and selling today; scale depends on supplier data participation and data quality.

### Soft metrics

| # | Metric | Definition and unit | Source | Reportable now |
|---|---|---|---|---|
| 1 | Renewal signal yield | Expiration and renewal notifications issued to Sales Operations in the month, and the percentage acted upon within 30 days. Count and percent. | ADM notification analytics reporting | Yes. Shipped in the 2026-08-17 production release |
| 2 | Managed record completeness | Percentage of asset and license records under management carrying the complete core attribute set. Percent. | ADM | Yes, once the core attribute set is defined |
| 3 | Supplier and purchase-history coverage | Percentage of in-scope suppliers whose purchase history is ingested, beyond configured supplier id. Percent. | ADM against the in-scope supplier list | Yes, once the in-scope list is fixed |
| 4 | Automated ingestion rate | Percentage of records entering ADM through an automated feed rather than manual entry or flagging. Percent. | ADM audit trail | Confirmation required |

**Notes.**

- Metric 1 answers the hardest question WAM faces, which is what the license capability has produced, without leaning on the 2026 attainment figure that comes from the supply chain motion rather than the license capability (framing correction, Darryl, 2026-08-05).
- Metric 2 requires the core attribute set to be named. Proposed: manufacturer part number, product type, license or warranty term, expiration date. P360 governance declined product type as a global attribute and it is collected by workaround, so this metric will make that governance gap visible in the number.
- Metric 1 reports both assigned and converted counts rather than choosing one definition of "acted upon" and defending it.

## 5. Ascent Navigator

### Elevator pitch

Ascent Navigator is the operations platform that runs Ascent's data center and critical facilities managed services business. It is the system of record for assets, work orders, maintenance programs, vendor and contract management, budgeting and forecasting, operated daily by Ascent's 24x7 operations center and dispatch teams.

Navigator 2.0, in build through 2027, replaces IBM Maximo, moves the platform to cloud hosting with an on-premises option, and adds multi-tenant deployment so new customer sites can be added without a further Maximo implementation.

For Wesco the case is direct. Navigator 2.0 removes an IBM Maximo renewal falling due in March or April 2027, avoiding approximately $3.98M inside the investment year, and puts the platform roadmap under our control rather than a vendor's. Without it, Ascent faces a forced migration to the Maximo Application Suite on a points-based license costed at roughly ten times the current subscription.

Integration with entroCIM, WAM and Connected Device Assurance follows as the redesign lands.

### Soft metrics

| # | Metric | Definition and unit | Source | Reportable now |
|---|---|---|---|---|
| 1 | Maximo dependency remaining | Number of the six core operational functions still running on Maximo rather than Navigator 2.0. Count, counting down to zero against the 2027 renewal. | Navigator 2.0 release record | Yes |
| 2 | Planned maintenance completion | Percentage of scheduled maintenance tasks completed within their scheduled window in the month. Percent. | Navigator / Maximo work management | Confirmation required |
| 3 | Asset record completeness | Percentage of managed facility assets carrying a complete record: identity, location, maintenance program assignment, and contract or warranty linkage. Percent. | Navigator asset register | Confirmation required |
| 4 | Facility coverage | Number of customer facilities operated on the platform, and how many of those run on the multi-tenant deployment rather than a dedicated instance. Two counts. | Ascent operations | Yes |

**Notes.**

- The set covers operate, record, scale and exit, with no overlap.
- Metric 1 is the only metric across the four products tied to a dated external forcing function, and it counts down rather than up, so lateness is visible early rather than at the renewal.
- Alternative to metric 3 if throughput is preferred to record quality: work orders created and closed per month, with the percentage inside target resolution time.

### What changed from DJ Vaughn's draft (email, 2026-08-25)

The opening paragraph survives nearly intact; it was the strongest content in the draft. Changes made:

- The ten Strategic Outcomes were dropped. None can be reported in any month. The three carrying real content (scale, standardization, reduced legacy dependence) were folded into the capability and value sentences.
- The $3.98M cost avoidance and the March or April 2027 renewal date were added. The draft omits them, and they are the strongest internal value point Navigator has.
- Navigator 2.0 is marked as in build rather than described in the present tense. Two of the draft's bullets read as though the commercialization foundation already exists.
- "Reduces dependence on legacy platforms" was replaced with the specific and checkable fact: removal of the on-premises Maximo dependency ahead of the 2027 renewal.

Darryl to take the first draft of the deck to DJ for input.

## 6. Connected Device Assurance

### Elevator pitch

Connected Device Assurance is a managed service that takes ownership of the connected devices on a customer's sites after they are installed. A small Wesco-managed appliance on the network automatically discovers every camera, access control and network device, maintains a verified inventory, and assesses each for firmware currency, known vulnerabilities and support status, continuously rather than by sampling.

Firmware and configuration changes are planned, customer-approved, executed remotely and validated, with evidence recorded for every action, giving the customer a defensible cyber position rather than an assessment that ages. Work needing hands on a device escalates to field service with a complete work package.

Wesco Managed Services owns and delivers it, drawing on entroCIM's platform, tools and engineering expertise, and it is designed in support of Navigator's 2027 redesign, where work orders and field escalations land.

For Wesco it converts an installed base we already supply into recurring service revenue and qualified hardware refresh demand, and it is the lead-in service for the CSS digital portfolio: the secure connection and verified inventory it establishes are what the other services need. 2027 is a development and validation year; first revenue follows the pilot.

### Soft metrics: FY27 readiness

CDA is the only product of the four with no current reporting line, because the investment is not yet approved and the work has not started. First report for all four metrics is 2Q27, monthly thereafter. This is a statement of fact rather than a gap.

| # | Metric | Definition and unit | First report | Lifecycle |
|---|---|---|---|---|
| 1 | Device family qualification | Number of device families with confirmed firmware access, update mechanism and managed-service rights, against the FY27 target set. Count. | 2Q27 | Permanent |
| 2 | Launch dependency closure | Number of named launch dependencies closed out of the total: partner sensor agreement, connectivity and credential architecture, liability and service level language, pricing and margin model, Sales sponsorship. Count out of a fixed denominator. | 2Q27 | Retires at pilot start |
| 3 | Service capability demonstrated | Number of the four service functions, identify, monitor, manage and execute, demonstrated end to end on a qualified device family. Count, zero to four. | 2Q27 | Retires after pilot completion |
| 4 | Pilot commitment, then account expansion | Named pilot customers committed, and contracted device count against the 250 to 1,000 camera pilot basis. Two counts. | 2Q27 | Permanent |

**Notes.**

- The set answers four different questions and does not overlap: can we technically do it, are we allowed to do it, have we built it, and does anyone want it.
- Metric 1 is permanent by decision (Darryl, 2026-08-26). Its meaning matures rather than expiring: today it asks whether we can launch; at maturity it measures how much of the addressable estate the service can manage, which is the supply-side ceiling on every expansion conversation.
- Metric 4 is the earliest true signal. A service with no named pilot customer by mid 2027 has a problem no development milestone will reveal.
- Metric 3 runs in parallel with the service KPIs through the pilot window. Capability demonstrated is a build measure; the service KPIs are a performance measure. During a pilot both are wanted.

### The five submitted service KPIs (target state, from first pilot connection)

Held here for traceability, unchanged from the FY27 AOP submission:

1. Device coverage depth
2. Automated discovery yield
3. Advisory correlation coverage
4. Remote change success rate
5. Service evidence completeness

## 6a. Reportability matrix (deck slide 6)

Every metric in one grid, so the four products can be compared on when a number first exists, who produces it, and what the product is worth. Functions are named rather than individuals; proposed individual owners stay in the backing document.

| Product | Metric | Reportable from | Produced by | Why it matters to Wesco |
|---|---|---|---|---|
| entroCIM | Platform availability | Now, monthly | entroCIM Delivery | An owned platform carrying software revenue and pull-through on the devices we sell, keeping control of the customer's operational data rather than renting it. The priority now is commercial conversion of the installed base |
| entroCIM | Licensed point utilization | Now, monthly. Covered proportion stated each report | entroCIM Product with Commercial | |
| entroCIM | Net licensed point movement | Now, monthly. Renewal rate rolling 12 months | Commercial and Sales Operations | |
| entroCIM | Containerized deployment coverage | Now, monthly. Opens near zero; testing began Aug 2026 | Deployment and Delivery | |
| WAM | Renewal signal yield | Now, monthly. Analytics shipped 2026-08-17 | ADM with Sales Operations | Install-base data we already hold, converted into renewal and refresh demand, and the data foundation Intelligent Asset Management Services runs on. Production-ready and selling today; scale depends on supplier data participation |
| WAM | Managed record completeness | Blocked: core attribute set not yet defined | ADM with WAM Product | |
| WAM | Supplier and purchase-history coverage | Blocked: in-scope supplier list not yet fixed | Supplier Data with ADM | |
| WAM | Automated ingestion rate | Confirm: does the ADM audit trail split automated from manual | ADM | |
| Navigator | Maximo dependency remaining | Now, monthly | Ascent Product Development | Removes an IBM Maximo renewal falling due in March or April 2027, avoiding approximately $3.98M inside the investment year, and puts the roadmap for a mission-critical operations platform under our control rather than a vendor's |
| Navigator | Planned maintenance completion | Confirmation required from Ascent | Ascent Operations | |
| Navigator | Asset record completeness | Confirmation required from Ascent | Ascent Operations | |
| Navigator | Facility coverage | Now, monthly | Ascent Operations | |
| CDA | Device family qualification | 2Q27, monthly. Permanent measure | CDA Product with Supplier Relations | Converts an installed base we already supply into recurring service revenue and qualified hardware refresh demand, and it is the lead-in service for the CSS digital portfolio. 2027 is a development and validation year |
| CDA | Launch dependency closure | 2Q27, monthly. Retires at pilot start | Managed Services Business Lead | |
| CDA | Service capability demonstrated | 2Q27, monthly. Retires after pilot | CDA Engineering | |
| CDA | Pilot commitment | 2Q27, monthly. Becomes account expansion | Commercial with Managed Services | |

## 6b. Slide format (agreed 2026-08-26)

Each product page runs left to right rather than in columns, after the two-box version read as disjointed:

- **Left half:** the elevator pitch in one continuous light box, dark text at 11.5 to 12 point. The box is tinted rather than dark, because the slide background is light and reversed text was hard to read.
- **Right half:** the four soft metrics as stacked full-width rows, each with its number, name and definition on one line of sight.
- **Footnote under the metric column**, where a product needs one. Used on Navigator (the metrics are produced inside Ascent) and CDA (the service KPIs begin at first pilot connection).
- **No value band.** What the product is worth to Wesco is the closing paragraph of the pitch, and appears again condensed in the matrix.

Pitch length was cut 10 to 16 percent per product: entroCIM 184 to 158 words, WAM 185 to 160, Navigator 178 to 160, CDA 233 to 196. Cuts were redundancy and hedging, not content. Nothing material was removed; "asset lifecycle and commercial intelligence" was explicitly retained on entroCIM because the commercial half is what distinguishes WAM from a configuration database.

## 6c. Pitch format: hybrid prose and bullets (agreed 2026-08-26)

Each pitch runs prose, bullets, prose. The rule governing the split:

- **Bullets carry only genuinely parallel facts.** entroCIM's four platform attributes; WAM's two delivery paths, which complete the sentence above them; Navigator's six core operational functions, which are also the denominator of its first metric; CDA's three service actions, all verb-parallel.
- **Anything with a because in it stays in prose.** Portfolio positioning, the cyber-posture consequence, the Maximo exposure. Bullets let a writer skip the connective tissue, and those points are the connective tissue.
- **The closing paragraph is prose on every page.** The value argument has to reason rather than list.

Navigator gained something from this beyond readability: naming the six core operational functions on the page makes its first metric legible, since that metric counts how many of them still run on Maximo.

## 6d. Definitions (deck slide 7)

Nine terms, as cards. The selection test: define a term only where taking it differently would change how a metric or a value statement reads. Everything else is left out, because a glossary of terms the audience already knows reads as talking down.

| Term | Definition |
|---|---|
| Licensed points | A point is a single monitored data value in a building or OT system: a temperature reading, a status, a setpoint. entroCIM is licensed by the number of points a customer connects, so a point is both the unit of sale and the unit of use |
| Entitlements | The rights a customer holds under a purchase or contract, separate from the hardware itself: software licenses, support coverage, warranty terms, and usage or feature rights. They expire and renew on their own schedules, which is why they are tracked apart from the asset |
| Install base | The equipment and software a customer already has in service, whether Wesco supplied it or not. Wesco's install base is the subset Wesco sold, and it is where renewal, refresh and service demand comes from |
| Complex builds | Configured multi-component systems Wesco assembles and serializes before shipment, rather than single items picked from stock. The parent and each child component carry their own serial and MAC data, which has to reach the customer's asset record intact |
| Product pull-through | Hardware and product sales generated by a platform or a service rather than sold directly. A service that identifies an out-of-support camera creates a replacement sale, and that sale is pull-through |
| Firmware currency | How far a device's installed firmware is behind what the manufacturer has released. Out-of-date firmware is the most common route to a known device vulnerability, which is why it is measured rather than assumed |
| Multi-tenant | One deployment of a platform serving several customers at once, with their data kept separate. The alternative is a dedicated instance per customer, which makes every new customer a new implementation and a new license |
| Containerized deployment | Packaging an application with everything it needs to run, so it installs the same way on any host. It is what makes version control, security updates and repeatable installation possible at scale, and it is a prerequisite for delivering a platform as a managed service |
| Points-based license | A licensing model priced on counted units of capacity rather than on named users or a flat subscription. IBM's Maximo Application Suite uses one, which is why the modelled renewal is roughly ten times Ascent's current cost. Unrelated to entroCIM's licensed points, which are monitored data values |

**Deliberately excluded.** OT, IoT, telemetry, MRO, AOP and P&L: the audience either knows these or asks without embarrassment. **ADM and Strev excluded on Darryl's call (2026-08-26)**, since the deck circulates outside CSS and the entry would have exposed internal plumbing to no benefit. The risk that decision accepts is the one worth naming: a reader outside CSS may conflate Intelligent Asset Management Services with Wesco Asset Management, which is the distinction the WAM page exists to draw. The page carries it in prose; the glossary no longer reinforces it.

## 7. Relationship to the FY27 AOP submission

The AOP workbooks submitted 2026-08-21 are unchanged by this work. Specifically:

- **entroCIM and CDA** carry Value KPI blocks with a quarterly cadence. Those stand. The monthly sets above are the same measurement run faster, internally.
- **Navigator and WAM** have deliberately blank Value KPI blocks, because both submitted on the Financial Benefits path and the template instructs one of three. That decision is not reversed. The metrics above exist for internal portfolio management, not for the form.

If any of this content is later written back into a workbook, that is a separate decision requiring its own change-log entry.

## 8. Open confirmations

| Item | Product | Needed from |
|---|---|---|
| Core attribute set definition for managed record completeness | WAM | Product and ADM |
| Whether the ADM audit trail distinguishes automated from manual record creation | WAM | ADM |
| In-scope supplier list fixed for coverage denominator | WAM | Supplier data and ADM |
| Monthly production of all four metrics, and who supplies them | Navigator | Ascent |
| Named metric owners per product | All | Darryl |

## 9. Change record

| Date | Change |
|---|---|
| 2026-08-26 | Created. All four pitches and metric sets agreed in session. Cadence, start point, Navigator handling and metric-owner placement decided by Darryl at the outset |
| 2026-08-26 (final, rev A) | Definitions added as slide 7: nine terms as cards, selected by whether misreading them changes how a metric or a value claim reads. ADM and Strev excluded on Darryl's call. Deck is now seven slides |
| 2026-08-26 (final) | Deck approved by Darryl for circulation. `2026-08-26_Product_Pitches_and_Soft_Metrics.pptx` is the released artifact. The two format drafts in the same folder (`_Layout_Drafts_entroCIM`, `_Hybrid_Pitch_Drafts`) are retained as decision artifacts, not superseded versions; they record why the format is what it is |
| 2026-08-26 (rev 4) | Pitches converted to hybrid prose and bullets across all four products, under the rule in §6c: bullets for parallel facts only, prose for anything carrying a because, closing paragraph always prose. Format drafts retained as `2026-08-26_Hybrid_Pitch_Drafts.pptx` |
| 2026-08-26 (rev 3) | Layout changed to pitch-left, metrics-right after review: the two-column pitch read as disjointed, and the dark box was hard to read against a light slide. Pitch box now light with dark text at 11.5 to 12 point. All four pitches shortened 10 to 16 percent. Value band removed; value now closes the pitch and repeats condensed in the matrix. Layout drafts retained as `2026-08-26_Layout_Drafts_entroCIM.pptx` |
| 2026-08-26 (rev 2) | Deck restructured on Darryl's review. The two product boxes merged into one continuous elevator-pitch block, because separate boxes with different titles did not read as a pitch. Per-metric status text and the green "For Wesco" band removed from the product pages and consolidated into a new reportability matrix (slide 6) carrying reportable-from, produced-by and why-it-matters. Content added while checking for lost detail: the Intelligent Asset Management Services / WAM / ADM / Strev disambiguation on WAM, the forced-migration risk on Navigator, and the CDA service-KPI transition line, which had been a slide footnote |
