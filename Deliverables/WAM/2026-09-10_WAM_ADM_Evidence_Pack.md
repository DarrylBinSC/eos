# WAM and ADM: Evidence Pack

**Produced:** 2026-09-09. **Rebuilt:** 2026-09-10 around three use cases, then revised the same day after a slide-by-slide review. Per `Deliverables/WAM/2026-09-10_Sean_Deck_Revision_Decisions.md`.
**Audience:** Sean McCloskey, one to one with Darryl. No third reader, and no orientation content.
**Companion deck:** `Deliverables/WAM/2026-09-10_WAM_ADM_Sean_Deck.pptx`, six pages.
**Relationship between the two.** The deck leads with velocity, defect burden and control, because that is the case Sean needs in order to spend political capital. This pack holds the fuller picture, including the constraint analysis that cuts the other way. Both are true and Darryl should have both in the room.

**What the meeting is for.** To update Sean at executive level, discuss the product from the users' point of view, tie those users back to work still to be completed, and reach a judgement together on how likely each use case is to create value for Wesco. That judgement informs one decision: does Digital Products take over the development resources currently supplied by the Platforms team in India.

**The two concerns behind the question, and they are not the same question.** Sean raised the resource question out of concern that Wesco is not getting good results from the India Platforms team. Separately, he is not certain ADM is recoverable, given what has been spent and what is still required. The first is about a team and is testable against delivery evidence. The second is about the program and turns on whether the use cases below convert. An answer that satisfies one can read as an evasion of the other, so both are answered here and neither is merged into the other.

**Darryl's own position on the first concern, stated 2026-09-10 and Confirmed.** He agrees results have not been good. The motivation for taking the development team on is partly political and partly grounded in more than a year of slow delivery, quality questioned by his own team, and a working view that skills, control and motivation are all part of the problem. The deck therefore defends no one. What it has to do is give Sean something defensible upward.

**Darryl's own position is held in a separate file**, `2026-09-10_WAM_ADM_Darryl_Position.md`, and is not part of this pack.

**Where each question is answered.**

| Question | Where |
|---|---|
| Who uses this and what do they get | Part 2 |
| How does the data reach them | Part 3 |
| Where does each use case actually stand | Part 4 |
| What is blocking each one, and who holds it | Part 4.2 and Part 3.4 |
| Is the value there | Part 5, and the working page in the deck |
| Do we take the development resources | Part 6 |
| What we still do not know | Part 7 |

**Evidence tiers used throughout.** Confirmed means a document, transcript, query result, ticket or system export supports it. Stated means a person asserted it and no independent artifact corroborates it. Inferred means it follows from evidence but was not asserted. Assumed means it is a working assumption and is labelled as such. Nothing here is presented as fact on an Assumed basis.

---

## Part 1. Evidence summary

Three use cases carry the product: license and warranty management for Sales Operations, asset lifecycle tracking for Managed Services, and complex builds for the warehouse, field service and the customer install-base record. Only one of the three reaches a user today; the license half of use case A has been in production since 2026-08-17, sending 60-day expiration signals with analytics to the owning sales representative, and its coverage has never been measured. The warranty half has no data anywhere: a path was named for the first time on 2026-09-10, adding warranty data to P360 with Supplier Relations and the supplier feeds populating it, and P360 governance declined a comparable global-attribute request on 2026-08-10. Asset lifecycle tracking is partially served, with purchase and order data flowing from EUDM and an enrichment service live for one internal program, while the asset upload work was deferred in September to make room for it. Complex builds have no data path at all: the write from VAS into the enterprise data layer does not exist, the final data model is open between Daniel Totino and Akansh Gangil, and the warehouse capture instruction is five weeks old and unproven at volume. Twelve blockers stand across the three use cases; three are ours, two are development work gated on decisions held elsewhere, and seven are not development work in any organization. On Sean's first concern the record splits, and both halves are real: four major data capabilities were re-estimated in August to land between October 2026 and February 2027, 29 defects were confirmed still open on review with a historical backlog parked without disposition, and a seven-area data-quality stabilization plan has been running since the July go-live; against that, the team has shipped against every requirement it could scope and finish alone, including an enrichment service scoped and refined in two days against a live business need, and has moved nothing that required another organization's data or decision. On Sean's second concern, forward development cost is known at $150,480 of FY27 expense after capitalization, the Strev half of forward cost has no number anywhere in the plan, and current WAM revenue is earned through supply chain programs rather than through the license capability, so 2026 attainment is not evidence that any of the three use cases is converting.

---

## Part 2. The three use cases, and the enabler beneath them

Redefined by Darryl on 2026-09-10. The prior set of eleven, derived from the seven value propositions in the record, mixed development-team tasks in with use cases. What follows is the corrected set. Value to Wesco is shown as reaching it through Sales Operations and Amy Aguirre's Managed Services; the customer is the reason those two can sell it, not a third recipient.

### A. License and warranty management

Internal sales triggers and lifecycle reporting.

| Field | Content |
|---|---|
| User | Sales Operations, at Senior Director level through Debbie Hunter, with Natalie Marquardt embedded in the work |
| Trigger | A license, warranty or support term entering the notification window, or an account review |
| What they do | Receive a dated expiration signal for a customer instead of researching accounts one at a time; see the license term, the end date and the assigned end user in one place; report lifecycle position across the install base |
| Data required | License order records, license term, warranty term, a trustworthy end date, end-user assignment, customer identity resolved to a single ERP record |
| What changes for Wesco | Renewal work starts from a governed signal rather than from manual digging, and renewal revenue becomes attributable |
| Value reaches Wesco through | Sales Operations |

The two halves of A are at very different stages and the pack keeps them separate throughout, because merging them would state warranty capability that does not exist.

### B. Asset lifecycle tracking

Purchase history, current orders, status. Lifecycle here does not mean end of life or refresh signalling; that reading was corrected by Darryl on 2026-09-10.

| Field | Content |
|---|---|
| User | Managed Services delivery, in Amy Aguirre's organization, with ADM and the Managed Services enrichment team |
| Trigger | A new engagement, an install-base refresh, or a program request |
| What they do | Look up what a customer has bought, by supplier and by part; see current orders and their status against an engagement; stand up a customer install base without rebuilding it by hand |
| Data required | Complete purchase history by customer and supplier, order records and status, supplier attribute data, product classification, customer-supplied records where they exist |
| What changes for Wesco | Onboarding becomes repeatable rather than bespoke, which is what lets the service scale past hand-built engagements |
| Value reaches Wesco through | Managed Services |

The enrichment service delivered for Violet Moyer's Microsoft AV requirement sits inside B as delivered work. It accepts sales order, Wesco part number and manufacturer part number and returns shipping fields and transaction price with not-found statuses; average-price logic was deferred. That the driver is the Microsoft AV requirement is Darryl-reported as of 2026-09-09 and should be confirmed with Akansh Gangil and Violet Moyer before it is used outside Darryl's own hands.

### C. Complex builds

Work instruction, parent-child and metadata tracking, including serial number and MAC address.

| Field | Content |
|---|---|
| User | Warehouse and field service, and the customer through the install-base record |
| Trigger | Fulfillment of a configured multi-component system, then any later service event |
| What they do | Capture serial number, MAC address and asset tag against the parent-child structure as part of standard work; identify a delivered system and every component in it at any later service event |
| Data required | Parent-child structure from the VAS finished-goods template, serial number and MAC address per component, asset tag, room or location, order and configuration context |
| What changes for Wesco | Configured systems stay identifiable and serviceable after delivery, in a growth area where they currently go dark at the warehouse door |
| Value reaches Wesco through | Managed Services |

**New as of 2026-09-11, and it is not settled.** Strev is being considered for use at the complex-build sites as a system of record, which would mean metadata flowing back from Strev into ADM and from ADM into EUDM. The GPO is separately reviewing the Strev tool in the warehouse. This would reverse part of the architecture Darryl confirmed on 2026-08-19, where DDP and EUDM are the single source of truth and the only route into ADM and the flow runs one way. It is carried as gate G7 and as an open decision rather than as a design, because the authority question, the SOW scope question and the governance question are all unanswered. Settling the complex-build data model without settling this first means settling it twice.

### D. API integration to Strev

The enabler. It has no direct user of its own and is not treated as a peer of A, B and C. It is the ADM to Strev connection on the data-path diagram, and it is how all three use cases reach a customer-facing surface. Decided 2026-09-10 that it needs no further visibility in the deck.

Two things the record says about it that matter to the other three. Strev delivers under SOW, with SOW 3 active, declared on the FY27 AOP as third-party solution, dependency and outsourced resource, which makes it a delivery dependency carrying schedule and quality risk rather than only a licensed component. And bulk parent-child asset mapping, the leading 2027 Strev enhancement request, consumes the parent-child hierarchy data that use case C has to produce first. The dependency runs Wesco to Strev, not the other way.

### What is deliberately not a use case

Support for the supply chain programs that earn current WAM revenue is a real motion and it is not one of the three. It is carried in Part 5, because it is the reason a value discussion cannot rest on 2026 attainment. Entitlement event handling is dropped: no data model exists, and it is not one of the three.

---

## Part 3. The data plan

### 3.0 Architectural facts that constrain every answer

Confirmed by Darryl, 2026-08-19. DDP and EUDM are the single source of truth for asset data and the only route into ADM. WMX and VAS deliver into DDP; ADM takes nothing directly from either. ACT is a contingency path, not integrated today. The complex-build capture mechanism is a WMX-triggered workflow into VAS, and VAS writes the complete parent-child structure, serial, MAC and attributes to DDP, which is new build. P360 provides serialization setup to WMX. Current state for the complex-build flow is pre-DDP, undefined and largely incapable of the flow, so what follows describes a target path and where it is gated, not a working path with faults.

### 3.1 Which dependency chain each use case runs on

Each use case is traced to the dependencies it needs and, through 3.2a, to a named Wesco system of record for each. Nothing below ends at a domain.

| Use case | Dependencies it requires | Systems of record at the end of the chain |
|---|---|---|
| A, license | D1, D2, D3, D4, D5, D6, D7, D8, D9 | EUDM, MDM, IAP, Core ERP, NetSuite, Anixter mainframe |
| A, warranty | D17, D18, and a P360 attribute that does not exist yet | P360, MDM, supplier feeds |
| B | D1, D8, D9, D16, D18, D19, D20 | EUDM, Core ERP, NetSuite, P360, supplier feeds, customer documents through IDP |
| C | D10, D11, D12, D13, D14, D15 | WMX, VAS, P360, EUDM |
| D, the enabler | Everything A, B and C produce, plus Strev tenant configuration | ADM to Strev over the API, under SOW |

### 3.2 Data dependencies

Twenty-one dependencies, keyed D1 to D21. The twelve-column specification does not render as one readable table, so it is split into 3.2a (what is required and what exists) and 3.2b (the gate, its holder, and the plan). The keys join the two.

#### 3.2a What is required, and what exists today

| ID | Data required | Wesco system of record | Path into ADM | State today | Evidence tier | Completeness |
|---|---|---|---|---|---|---|
| D1 | License order records by vendor part number and supplier ID | DDP / EUDM | DDP/EUDM to ADM, live since 2026-07-03 | Delivered and in use | Confirmed | No figure exists |
| D2 | Identification of which part numbers are software or license items | MDM, plus Anixter mainframe product-class grouping | MDM to DDP to ADM | Manual flagging in ADM. A source rule was supplied 2026-08-27 by Jen Turnage (`dbo_IA_TPRODUCT_GROUPING_BY_PROD_CLASS` where `PROD_GROUPING = SOFTWARE`), not yet validated against known examples | Stated | No figure exists |
| D3 | License term, meaning duration, per license part number | MDM, with supplier input | MDM to DDP to ADM | Active and flagged red on the July backlog slide, dependency named as MDM and DDP. Not delivered | Confirmed | No figure exists |
| D4 | Clean, standardized product description | MDM | MDM to DDP to ADM | Same red item as D3 | Confirmed | No figure exists |
| D5 | End-user assignment on a license record | IAP, plus ADM UI editing | IAP to ADM | Delivered 2026-05-14 for records lacking end-user data. Default assignment, bulk edit and clear, and uppercase handling confirmed in production 09-09. Notification assignment logic restricted to ERP 12004 records to avoid duplicate-customer-ID ambiguity | Confirmed, except the 09-09 production confirmation which is Stated (AI meeting notes, no transcript) | Roughly 13,000 to 13,500 legacy records still need disposition after the pending-activation fix |
| D6 | License activation state | ADM, dependent on sales order dates | Internal to ADM | Activation failures traced to null and missing sales order dates (bug 7827). Reported resolved 09-09 | Stated. The resolution rests on AI meeting notes, not a transcript | No figure exists |
| D7 | Expiration date and the notification trigger | Derived from D1 and D3, with supplier end dates for Milestone and ExacQ | Internal to ADM, out to Sales | 60-day expiration notifications shipped to production 2026-08-17 with analytics reporting | Confirmed | No figure exists for the share of records carrying a trustworthy end date |
| D8 | Full-length manufacturer part number | DDP / EUDM | DDP/EUDM to ADM | Truncated at 15 characters in EUDM Bronze and Silver. A source query now exists to trace the full value; the values themselves are unchanged. Defect W1 | Confirmed | Not measured. Orders are missed outright where matching fails |
| D9 | Presence of all sales orders in the EUDM table | Core ERP and NetSuite into EUDM | EUDM to ADM | Core ERP orders missing under INC5456198 (W3). Sample orders absent outright and requiring NetSuite hydration (W2) | Confirmed | Not measured |
| D10 | Serial number, simple products | WMX | WMX to DDP to ADM | Captured at shipment against the order and propagated to DDP | Confirmed | No figure exists |
| D11 | Serial number with parent-child association, complex builds | VAS | VAS to DDP to ADM | Does not happen today. Serial-to-VAS association is new build. Warehouse standard work has instructed capture inside VAS since 2026-08-27 | Confirmed | Not measured, and the instruction is five weeks old and unproven at volume |
| D12 | MAC address | WMX, and VAS for complex builds | WMX or VAS to DDP to ADM | WMX capture unconfirmed. WMX 5.7 expected to add MAC address and asset tag fields. Inside VAS, covered by the 08-27 standard work instruction | Stated | No figure exists |
| D13 | Asset tag | Same as D12 | Same as D12 | Same as D12 | Stated | No figure exists |
| D14 | Parent-child hierarchy structure for configured systems | VAS finished-goods template | VAS to DDP to ADM, then ADM to Strev | The template exists and is synced with DDP for part, manufacturer part and manufacturer name. Delivering it serialized to DDP is new build | Confirmed | Not applicable until the path exists |
| D15 | Room or location per component | Not established | Not established | Named as an open item in the complex-build data model. No source system identified | Inferred from the open-items list | None |
| D16 | Product type or product class as a governed attribute | P360, with MDM | P360 to DDP to ADM | P360 governance declined to add product type as a global attribute. Akansh Gangil's team collects it outside P360 by workaround | Confirmed | No figure exists |
| D17 | Warranty term | MDM, with supplier input | MDM to DDP to ADM | Work in flight this year and not represented on the roadmap deck. Automated warranty end date calculation is a 2027 Strev item, which computes a date from a rule rather than sourcing a term | Stated | No figure exists |
| D18 | Supplier attribute and purchase-history coverage | Supplier feeds, via Supplier Relations and Sales Operations | Supplier to MDM or direct to ADM | Roughly 5,000 missing records inserted and Exact data 90 to 95 percent present as of 2026-08-25. HID ingestion intermittent, root cause unresolved | Confirmed for the insertion and the Exact figure | 90 to 95 percent for Exact only. No figure for the supplier set as a whole |
| D19 | Customer-supplied and non-Wesco asset records | Customer documents, spreadsheets, email | IDP to ADM | IDP-to-ADM proof of concept and integration architecture received WAB approval 2026-09-02. Ankit Chadha would not commit engineering resources | Confirmed, verbatim transcript | None. No production path |
| D20 | Shipping fields and transaction price against an order line | DDP / EUDM | ADM enrichment service | MVP scoped 09-01, refined 09-03. Returns not-found statuses. Average-price logic deferred | Confirmed | No not-found rate has been measured |
| D21 | Entitlement events and the rights they change | Not established | Not established | Concept defined in `WAM_Data_Architecture.md` section 8. Implementation and data model require validation | Confirmed as a definition, Assumed as anything more | None |

#### 3.2b The gate, who holds it, and the plan to close it

| ID | Gate | Gate holder | Inside Digital Products | Plan to close, owner, sequence | Cost of delay |
|---|---|---|---|---|---|
| D1 | No completeness measure has been requested | Akansh Gangil | Yes | Request a figure. No plan exists today | Every rating downstream stays Conditional |
| D2 | The Jen Turnage rule is unvalidated, and MDM has not completed license identification | MDM, with Jen Turnage on taxonomy | No | Validate the rule against known examples, then decide whether it substitutes for the MDM item. No owner or date | A license and B all rest on knowing which items are licenses |
| D3 | MDM and DDP have not defined license-term structures | MDM. Inder Gambhir and Gandhi Subramanian are named in the record | No | None in evidence. Red since the July slide | A license cannot be trusted without a term |
| D4 | Same as D3 | MDM | No | None in evidence | Degrades every customer-facing view |
| D5 | Legacy record disposition needs a reliable post-fix export | Akansh Gangil | Yes | Export after the pending-activation fix, then dispose. September release | A attribution errors on legacy records |
| D6 | Root cause is upstream in D9 | Akansh Gangil, with the EUDM team | Partly | Confirm the 09-09 resolution against a transcript or a query, not meeting notes | A fires on records that cannot activate |
| D7 | End-date trustworthiness depends on D3 and on supplier end dates | MDM and suppliers | No | Milestone and ExacQ end dates loaded. No plan for the rest | A wrong date is worse than no alert |
| D8 | The truncation is upstream in EUDM. No named fix owner since late August | EUDM and DDP team. Daniel Totino and the EUDM team per the 09-01 prep, tier Stated | No | Akansh Gangil's escalation has not produced an owner. Darryl escalates further if it stays silent. Register A29, B53 | Orders are missed outright, which caps D1, D18, D20 and every use case above them |
| D9 | Pipeline breaks from Core ERP and NetSuite into EUDM | EUDM and DDP team, with BI_Wesco_Integration_Support_L2 | No | INC5456198 open. NetSuite hydration path not designed | The install base is incomplete by an unmeasured amount |
| D10 | Whether capture is mandatory or optional is not established | John Barlolotti as GPO for WMX, delegated from Steve Leslie; Sid Sarna as solution architect | No | Open item on the 08-19 architecture. No owner | A license and C rest on capture actually happening |
| D11 | The final data model is open, and the VAS to DDP write is unbuilt | Daniel Totino with Akansh Gangil on the model; build ownership not established | Partly | 09-01 decision set WMX for standard collection and VAS governance for project-specific requests. Data model still open. Register A1 marked potentially closed, unconfirmed | C does not exist until this lands |
| D12 | WMX 5.7 attribute support is unconfirmed, and conflicts with the standing no-capability-until-2028 record | John Barlolotti and Sid Sarna | No | Resolve the conflict with GPO. Named as open since 08-19 | Decides how much VAS has to carry, and therefore the size of the build |
| D13 | Same as D12 | Same as D12 | No | Same as D12 | Same as D12 |
| D14 | The serialized write to DDP is new build with no funded plan | Build ownership not established | Partly | Required before Strev bulk parent-child mapping can consume anything | The one genuine dependency running Wesco to Strev |
| D15 | No source system identified | Open | Unknown | Name a source, or drop the field from C | C service outcomes need location |
| D16 | P360 governance refused the attribute | P360 governance | No | Workaround continues outside P360. The governance question is unresolved | Classification stays local and unauditable |
| D17 | Warranty term structures are undefined in MDM | MDM, with Supplier Relations | No | GPO and MDM work is defined but not delivered | A warranty claims are unsupported |
| D18 | Supplier participation and cadence | Jarod Booth's organization via David Blondel, and Natalie Marquardt in practice, who is flagged as a single point of dependency | No | Continues through Sales Operations outreach. No coverage target | Caps B directly |
| D19 | Approved architecture, no engineering capacity | Ankit Chadha | No | One to two week capacity investigation from 09-02. Check in around 09-16 | B keeps absorbing manual document handling |
| D20 | Not-found rate is unmeasured, and it is a function of D8 and D9 | Akansh Gangil | Yes | Measure it during the MVP. Not currently planned | The one delivered internal service has no quality figure |
| D21 | No data model, no source mapping | Open. Product decision, not a data decision | Yes | Define the model, or drop entitlement from the value language | entitlement handling cannot be scoped, priced or sold |

### 3.3 The sequenced path

Read as a critical path rather than as a backlog. Items in the same tier can proceed in parallel; a later tier cannot complete before the tier above it.

**Tier 0, prerequisite to everything and currently unowned.** D8, the truncated manufacturer part number, and D9, the missing sales orders. Every downstream data set is capped by these two, and neither has a named fix owner. Nothing in tiers 1 through 4 can be measured honestly until they are closed or bounded, because a completeness figure taken over an incomplete source measures the wrong denominator.

**Tier 1, measurement.** Completeness figures for D1, D3, D5, D10, D12, D13, D18 and the not-found rate for D20. This tier is entirely inside Digital Products, requires no other organization's commitment, and is the single cheapest thing on this list. It is also the tier that converts every Conditional rating in Part 4 into a defensible one.

**Tier 2, master data.** D2, D3, D4, D16 and D17. All held by MDM and P360 governance. These are the gates behind the license and warranty use cases, and none of them is a development task.

**Tier 3, complex builds.** D11, D12, D13, D14 and D15, in that order, gated on the final data model between Daniel Totino and Akansh Gangil and on the WMX 5.7 answer from GPO. D14 is the prerequisite for the Strev bulk parent-child mapping investment, so a 2027 Strev item is downstream of a Wesco decision that has not been made.

**Tier 4, breadth.** D18 supplier coverage and D19 customer-supplied data. Both run at the pace of another organization, Supplier Relations in the first case and Ankit Chadha's engineering capacity in the second.

**What Digital Products can execute alone:** the whole of Tier 1, the D5 legacy disposition, the D20 measurement, the D21 entitlement model definition, and its half of the D11 data model. That is measurement, definition and disposition. It is not the capability itself.

**What requires a commitment from another organization:** D2, D3, D4, D8, D9, D10, D12, D13, D16, D17, D18 and D19. Twelve of twenty-one dependencies, and they include every one that gates a customer-facing use case.

This split is the answer to point 4 and it falls out of the analysis rather than being asserted at the top of it.

### 3.4 The three completeness defects, mapped to what they undermine

| Ref | Defect | Age | Owner | Use cases undermined | Effect |
|---|---|---|---|---|---|
| W1 | Manufacturer part numbers truncated at 15 characters in EUDM Bronze and Silver, while ADM holds full values, so exact matching fails | Root cause named 2026-08-25, symptom tracked since 2026-07-28 | None. Akansh Gangil's escalation has produced no owner; Register A29's trigger has not fired | A license, B | Orders are missed outright, so the install base and the notification set are both short by an unmeasured amount |
| W2 | Sample orders absent from EUDM outright, requiring hydration from NetSuite | Confirmed 2026-09-01 | None named | A license, B | A whole order class is invisible to ADM |
| W3 | Core ERP sales orders present in the ERP but missing from the EUDM table, INC5456198 | Raised 2026-07-27 | Akansh Gangil, Vishal Balasubramanian, Revanth Jampana named in evidence; BI_Wesco_Integration_Support_L2 asked to verify upstream cause. No fix owner | A license, B, and probably A warranty through D6 | Legitimate orders never reach the data lake, so this is a pipeline failure rather than a release defect |

A defect open four weeks with no owner is evidence about the operating model, not about the defect. All three sit in the same place, upstream of ADM and outside Digital Products, and the escalation route available to Darryl has been used and has not produced an owner.

### 3.5 Conflicts in the record, flagged rather than resolved

These are stated as conflicts because resolving them by choosing a side would put an assertion into a pack whose credibility depends on not doing that.

**WMX complex-build attribute capability.** Section 0 of `WAM_Data_Architecture.md` records no capability and no roadmap until 2028, while later evidence expects WMX 5.7 to add MAC address and asset tag fields. Either the earlier statement refers to full parent-child support rather than parent attributes, or it is out of date. The answer decides how much VAS has to carry and therefore the size of the D11 and D14 build. Resolve with John Barlolotti or Sid Sarna.

**The complex-build architecture is not settled.** The 2026-09-01 decision, WMX for standard serial collection and VAS governance for project-specific and ad hoc requests, refines rather than reverses the 08-31 position. The final data model, meaning the serial-number anchor, the parent and room relationship, the required attributes, and the VAS to WMX handoff, remains open between Daniel Totino and Akansh Gangil. Register A1 is marked potentially closed and has not been confirmed with Akansh Gangil.

**The DDP and EUDM sync automation.** The 08-05 Backlog Deep Dive deck marks the automated three-times-daily sync as Q2 complete, while the 07-16 and 07-20 record states the feed is manually triggered daily and instructs explicitly that the automation not be presented as production-grade. Both cannot be current. This claim has already appeared in outbound material.

**IDP and ADM: approved but unstaffed.** The proof of concept and integration architecture received WAB approval, and production resourcing stalled the same week when Ankit Chadha would not commit engineering resources, citing competing high-volume work and an October Oracle deadline. Approved but unstaffed is the accurate description, and it is a different problem from unapproved.

**Strev as a system of record against the confirmed architecture.** Section 0A of `WAM_Data_Architecture.md`, confirmed by Darryl on 2026-08-19, records DDP and EUDM as the single source of truth for asset data and the only route into ADM. The 2026-09-11 proposal to use Strev as the system of record at complex-build sites introduces return paths the confirmed architecture does not contemplate, and puts a vendor platform upstream of the enterprise data layer for a class of asset data. Flagged, not resolved. Recorded at `WAM_Data_Architecture.md` section 0B and `03_Decision_Log.md`, 2026-09-11.

**The software and license identification rule.** Jen Turnage's product-class grouping criterion is a durable data-source fact and has not been validated against known examples. Do not treat it as final, and do not treat it as closing the red MDM item without that validation.

**Coverage language.** The phrase "beyond Core and Anixter part numbers" is under a standing instruction not to be used in outbound material until resolved with Akansh Gangil, on the basis that it rests on a probable misunderstanding and sits close to two adjacent concepts. The safe formulation is that license data now syncs from multiple source systems into a single view.

---

## Part 4. Where each use case stands, and what is blocking it

### 4.1 Progress, by stage

Four stages rather than a percentage. A percentage needs a baseline and none of these has one, so quoting one would be manufactured precision.

| Use case | Defined | Data available | Built | In use by the user | Evidence |
|---|---|---|---|---|---|
| A, license | Complete | Partial | Complete | Partial | Expiration notifications, analytics reporting, export, audit trail, UI license editing, end-user assignment and bulk edit are in production, and Sales Operations receives the notifications. Shipped 2026-08-17, confirmed by Akansh Gangil. Coverage has never been measured |
| A, warranty | Partial | Not started | Not started | Not started | A path was named on 2026-09-10: add warranty data to P360, populated by Supplier Relations and the supplier feeds. Nothing is built, and no term structure exists in master data |
| B | Complete | Partial | Partial | Partial | Purchase and order data flow from EUDM since 2026-07-03. Exact supplier data is 90 to 95 percent present as of 2026-08-25. The enrichment service is live for one internal program. The asset upload epic was deprioritized 2026-09-01 |
| C | Complete | Not started | Not started | Not started | Architecture confirmed 2026-08-19, tool boundary decided 2026-09-01, warehouse capture instructed inside VAS since 2026-08-27. No serial-to-parent data reaches ADM today |

The single most useful line in this table: A, license is the only row with anything in the fourth column, and it sits at Partial because nobody has counted. That is not a delivery problem.

### 4.2 What is blocking each use case

Stated as the business problem with the holder named. Thirteen blockers as of 2026-09-11. Three are ours.

**Note on the deck.** The deck carries a shorter list per use case, at Darryl's direction for an executive conversation. This is the full list and it is the one to work from.

**The two principal hurdles, in Darryl's own framing, 2026-09-10.** P360 attributes with their data population, and proper EUDM sync with ADM, where sync means the completeness defects and the sync-automation question together as one hurdle. Everything else on this list is secondary to those two.

**A, license and warranty management**

| Blocker | Holder | Inside Digital Products |
|---|---|---|
| License terms and clean descriptions are not defined in enterprise master data | MDM, open and flagged red since July | No |
| Some orders never reach the enterprise data lake, and some arrive with the manufacturer part number cut short, so ADM misses them | EUDM and DDP team. No fix owner named for four weeks | No |
| Warranty data has no home. It needs a P360 attribute, then supplier population | P360 governance and Supplier Relations | No |
| We have never measured how complete the license data is | Ours | Yes |

**B, asset lifecycle tracking**

| Blocker | Holder | Inside Digital Products |
|---|---|---|
| Supplier purchase and attribute coverage is partial and moves at the pace of supplier participation | Supplier Relations and Sales Operations, with Natalie Marquardt flagged as a single point of dependency | No |
| The same missing and truncated orders cap what can be shown | EUDM and DDP team. No fix owner named | No |
| Customer-supplied documents have no automated route in. The architecture received WAB approval, no engineering capacity was committed, and staff availability is still not known as of 2026-09-11 | Ankit Chadha | No |
| Asset upload work was deferred in September to make room for the enrichment service | Ours | Yes |

**C, complex builds**

| Blocker | Holder | Inside Digital Products |
|---|---|---|
| The write from VAS into the enterprise data layer does not exist. It is new build with no named owner | Build owner not named | Partly |
| The final data model is open: serial anchor, parent and room relationship, required attributes, the VAS to WMX handoff | Daniel Totino with Akansh Gangil | Partly |
| Whether capture is mandatory, and which attributes WMX can hold, are unresolved | GPO: John Barlolotti, with Sid Sarna as solution architect | No |
| Strev is under review as the warehouse system of record, which would change the data model before it closes | GPO | No |
| The warehouse capture instruction is five weeks old and unproven at volume | Ours | Yes |

### 4.3 The same twelve, sorted by what a development team can do about them

This is the evidence that makes the resource question answerable, and it falls out of 4.2 rather than being asserted.

| Category | Count | Items |
|---|---|---|
| A development team can close these now | 3 | Measure how complete the license data is. Restart the asset upload work deferred in September. Measure whether warehouse capture is holding at volume |
| Development work, gated on a decision held elsewhere | 2 | Build the write from VAS into the enterprise data layer, gated on the final data model and on funding. Complex-build attribute support, gated on the WMX roadmap answer |
| Not development work in any organization | 7 | License terms and clean descriptions in master data. A warranty attribute in P360. Supplier participation and coverage. Orders that never reach the enterprise data lake. Manufacturer part numbers cut short upstream. The mandatory-capture decision on WMX. Document-route engineering capacity, which sits in another team |

**This analysis is deliberately not in the deck.** Darryl's judgement, 2026-09-10: it does not serve a high-level discussion with a leader who gets straight to the point. It is retained here because it is the answer if Sean asks what a transfer actually changes, and that question should not be met without one.

The three in the first row are unblocked and undone. That is the honest counterweight to any reading of this pack as a defence of the current arrangement, and it belongs to Darryl rather than to the development team.

---

## Part 5. Is the value there

This part is the evidence behind Sean's recoverability concern. It separates what is realized from what is planned, states where the money is actually earned today, and asks what the enterprise loses if ADM stops.

### 5.1 Realized, against the standard

Applying `Reference/Benefits_Realization_Standards.md`, a benefit is realized only with an owner, a baseline, a measure, a target and an evidence source. Measured against that, the register is short.

| Item | Owner | Baseline | Measure | Target | Evidence | Status |
|---|---|---|---|---|---|---|
| DDP and EUDM connection, 2026-07-03 | Akansh Gangil | None | None | None | Go-live | Realized capability milestone. Not a realized benefit |
| Notification suite in production, 2026-08-17, with analytics reporting | Akansh Gangil | None | Notifications sent is available through the analytics addition | None set | Release confirmed by Akansh Gangil | Realized capability. The first governed renewal signal reaching Sales Operations. No outcome measured |
| Supplier data: roughly 5,000 records inserted, Exact 90 to 95 percent | Natalie Marquardt with Akansh Gangil | Implied | Coverage percentage for one supplier | None set | Verbatim transcript, 08-25 | Partial. Realized on the insertion only, and it sits alongside W1, which causes orders to be missed regardless of supplier completeness |
| Enrichment MVP for the Microsoft AV requirement | Akansh Gangil | None | Not-found rate available but unmeasured | None | Backlog refinement 09-03 | Realized capability. Outcome not measured |
| 2026 attainment, 16.7M year to date, 87 percent through June | Finance | 19M objective | Revenue | 19M | Actuals deck | Realized revenue, and it is earned by the supply chain motion, not by the license capability. It is not evidence that any use case above is converting |

Everything else in the WAM benefits language is planned. The four monthly soft metrics agreed 2026-08-26, renewal signal yield, managed record completeness, supplier and purchase-history coverage, and automated ingestion rate, are the right measures and three of them carry open definitional or verification dependencies. None has a first reported value.

### 5.2 The gap between what was funded and what earns the money

This is the open strategic question from 2026-08-05 and no decision has been taken on it. The license capability is what was requested and what the roadmap is built around. The revenue is earned through supply chain programs, which none of the three use cases describes and which draws only lightly on the license data path. The FY27 gross margin of 15.2 percent corroborates this independently: it is a distribution margin, and a license and software business would not produce it.

Two consequences follow and both are live. A funding case for the license capability cannot rest on 2026 attainment, because the attainment comes from a different motion. And Sales Operations expectations were set at Senior Director level with Debbie Hunter on the license notification capability, which may not be where the revenue sits.

### 5.3 What the enterprise loses if ADM stops

This is a different question from what WAM gains if it continues, and it is the one a kill decision actually turns on. The record supports the following, and no more.

Internal consumers who would lose a capability: Sales Operations loses the 60-day expiration notification and its analytics, which is the only governed renewal signal they receive and which they have watched since 2026-07-16; Violet Moyer's Microsoft AV program loses the enrichment service delivered against a live requirement; Managed Services loses the normalization and enrichment path that customer onboarding runs on today.

Customer-facing commitments in flight: Strev is live in customer engagements, and the supply chain programs that earn the current revenue run through it. Whether those programs depend on ADM specifically or on Strev with manual loading is not established in the record, and it is the single most consequential unknown for a stop decision. It is on the gap list.

What would not be lost: the license capability's promised benefits are largely unrealized, so stopping would forfeit planned value rather than realized value. That cuts both ways in a decision and is stated here without a conclusion attached.

### 5.4 Scale against run rate

The FY27 plan carries 19.00 FTE, all India, zero North America, at $752,400 gross DEV labor and $150,480 of expense after capitalization. Against a gross margin of $4.9M to $5.8M, the development expense line is small and is not what makes or breaks the P&L. The honest reading is that the run rate is not the problem; the question is whether spending it improves anything, and the answer depends on gates that money does not open, because twelve of twenty-one dependencies require another organization's commitment rather than more engineering.

Stated as an assumption to be tested rather than as a finding: if the twelve external gates stay shut, additional development capacity produces additional unusable capability. Nothing in the record contradicts this, and nothing independently confirms it either.

---

## Part 6. The development resource question

### 6.1 What is now established, and what is not

Three things closed on 2026-09-10, all Confirmed, Darryl direct, not transcribed.

The development resources are not part of Darryl's organization. They are supplied by the Platforms team in India. The 09-09 pack could not establish this from the record and carried it as its first gap to close.

Sean raised the question out of concern that Wesco is not getting good results from that team. This matters because it names the concern as delivery performance rather than as an organizational plan or a resourcing change, and delivery performance is testable against evidence.

Sean separately doubts ADM is recoverable, given what has been spent and what is still required. This is a sunk-cost and forward-cost question about the program, and it is the larger of the two.

Still not established, and each one changes the answer: whether the India Platforms team is Merwan Mereby's specifically; who sets the backlog today; the funding line; and the codebase diligence, meaning age, architecture, test coverage, documentation, build and release tooling, environment ownership, and the open defect backlog including the seven-area data-quality stabilization plan and the 29 open bugs confirmed on review 2026-07-30.

An FY27 Product and Platform scope split is separately being worked with Rajesh, and the FY27 WAM scope field could not be finalised until it is agreed. Whether the resource question is the same question in a different form, or independent of it, is not established.

### 6.2 The nearest precedent runs the other way

On 2026-08-26, Register A9 closed on the answer that the CMP tool stays with the India Platforms team under Merwan Mereby and is not coming to Product. Same team, opposite direction, decided two weeks ago, with Sean as the counterpart on that thread. Stated as context, not as an argument. The two are not equivalent: CMP is a tool whose business owner was moving elsewhere, ADM is a platform with a live delivery program and external commitments.

### 6.3 Answering Sean's first concern on evidence

The claim to test is that Wesco is not getting good results from the India Platforms team. Darryl agrees with it. The record supports it on velocity and defect burden, and cuts against it on scope of control. Both readings are set out below, because Sean will find the second one whether or not it is offered.

**What supports the concern.** Four major data capabilities were re-estimated on 2026-08-06 to land between 2026-10-08 and 2027-02-03, well past the year they were committed in. Twenty-nine defects were confirmed still open on review at 2026-07-30, some earlier items having been found resolved or not actual defects. A historical ADM bug backlog was parked without a prioritization decision, noted 2026-07-24. A seven-area data-quality stabilization plan has run since the July go-live and has not closed. Read together, delivery is responsive on small self-contained work and slow on anything needing sustained capacity.

**What the record does not support.** A skills claim. The only skills evidence is the ADB-skilled data engineer replacing Vishal. Everything else above is data quality and upstream completeness rather than code quality. Darryl's decision, 2026-09-10: argue velocity, defect burden and control on the page, and leave skills to the conversation.

**What cuts the other way.**

What the team shipped this year, all Confirmed: license order data from EUDM by vendor part number and supplier ID, live 2026-07-03; export, audit trail and UI license editing; end-user project name from IAP; automated 60-day expiration notifications to the owning sales representative, in production 2026-08-17 with notification analytics and a product-upload fix beyond original scope; default end-user assignment, bulk end-user edit and clear, uppercase end-user handling and part-number upload, in production by 2026-09-09, though that last set rests on AI meeting notes rather than a transcript and is Stated. An enrichment service was scoped on 2026-09-01 against a live business requirement and refined by 2026-09-03.

What has not moved: nothing that the team could act on alone. Every stalled item in Part 4.2 needs data, a decision or capacity from another organization. Seven of the twelve blockers are not development work in any organization, and two more are gated on decisions held outside Digital Products.

The finding that cuts the other way, and it should be said first rather than under questioning: three blockers are unblocked, undone, and ours. No completeness figure has been requested for any domain. That is a product and prioritization gap at Darryl's level, not a delivery gap at the team's.

Set against that, the concentration on Akansh Gangil is real, documented and reconfirmed on 2026-09-09 across requirements, EUDM data quality, the enrichment MVP, complex-build modeling and Strev planning. It is unaddressed under every option including doing nothing.

### 6.4 What a transfer would inherit

| Item | What the record establishes | Evidence tier |
|---|---|---|
| Team and cost | 19.00 FTE, all India, zero North America, $752,400 gross DEV labor, $601,920 capitalized, $150,480 expense | Confirmed, FY27 P&L draft |
| Rate exposure | The India rate basis differs between the P&L at $22 and the AOP rate card at $24, a $71,440 variance on the form. Resources NA is zero, so any North America assignment is unbudgeted at a 4.3x differential | Confirmed, and open with Finance |
| Capitalization treatment | Labelled 65 percent, computes 80 percent, a $112,860 swing. A transfer changes who capitalizes what | Confirmed, and open with Finance |
| Codebase and technical debt | Not in the record. Required diligence: age, architecture, test coverage, documentation, build and release tooling, environment ownership, and the open defect backlog including the seven-area data-quality stabilization plan and the 29 open bugs confirmed on review 2026-07-30 | Absent. Named as a gap |
| Vendor position | Strev from Revnue Corp delivers under SOW, with SOW 3 active, declared on the FY27 AOP as third-party solution, dependency and outsourced resource. No Strev line is visible in the FY27 WAM P&L, so the spend is either inside COGS without separate identification or not in the plan. The QA integration and release governance obligations transfer with it | Confirmed on the declaration, Inferred on where the spend sits |
| Dependency set | Twelve of twenty-one data dependencies gated outside Digital Products, across five constraint holders, four of them outside Darryl's organization | Confirmed by Part 3 |
| Live commitments | Sales Operations expectations set at Senior Director level with Debbie Hunter; the Microsoft AV enrichment requirement; customer engagements running on Strev; the September release scope covering default end-user assignment, bulk end-user edit and clear, cancelled-order handling and the pending-activation fix | Confirmed |
| Knowledge concentration | Akansh Gangil is the named single point of dependency across requirements, EUDM data quality, the enrichment MVP, complex-build modeling and Strev planning, reconfirmed 2026-09-09. Natalie Marquardt is separately flagged as a single point of dependency for supplier data collection | Confirmed |

The dependency line is the one that carries the most weight. If it holds, a development transfer moves the team and does not move the gates, which means it answers a question about where engineering reports rather than the question of whether the use cases become feasible. Part 3 supports it: twelve of twenty-one dependencies, and every dependency gating a customer-facing use case, require a commitment from an organization that no transfer would touch.

The knowledge concentration line is the second. Any transfer plan that does not address the concentration on Akansh Gangil is incomplete regardless of which way the decision goes, and so is any decision to leave things as they are.

### 6.5 Answering Sean's second concern on evidence

The claim to test is that ADM may not be recoverable, given spend to date and what is still required.

What is known about forward cost: FY27 development is 19.00 FTE, all India, zero North America, $752,400 gross, capitalized to $150,480 of expense, against a gross margin of $4.9M to $5.8M. The development expense line is not what makes or breaks the P&L.

What is not known, and it is half the question: no Strev line is visible in the FY27 WAM P&L, so Strev SOW spend is either inside COGS without separate identification or not in the plan at all. The 2027 Strev priorities document carries no cost, effort, sequence or date. Sean's concern rests on the amount required going forward, and half of that figure does not exist anywhere. That gap is ours to close, and it is the single most useful thing to bring back to him.

Two open Finance items would be quoted back against any figure: the capitalization line is labelled 65 percent and computes 80 percent, a $112,860 swing, and the India rate basis differs between the P&L at $22 and the AOP rate card at $24. Resources NA is zero, so any North America assignment is unbudgeted at a 4.3x differential.

On the return side: the license capability's promised benefits are largely unrealized, and current WAM revenue is earned through supply chain programs rather than through it, corroborated by the FY27 gross margin of 15.2 percent, which is a distribution margin rather than a software margin. Stopping would forfeit planned value rather than realized value. That cuts both ways in a decision and is stated without a conclusion attached.

What the enterprise would lose if ADM stopped, and this is the question a recoverability judgement actually turns on: Sales Operations loses the only governed renewal signal it receives, set at Senior Director level with Debbie Hunter and watched since 2026-07-16; Violet Moyer's Microsoft AV program loses the enrichment service delivered against a live requirement; Managed Services loses the normalization and enrichment path that onboarding runs on. Whether the supply chain programs that earn the current revenue depend on ADM specifically, or on Strev with manual loading, is not established in the record and is on the gap list. It is answerable in a week and no recoverability judgement is safe without it.

### 6.6 The decision, with the verdict open

Two options, assessed on identical criteria. Neither is pre-selected.

| Criterion | Take the resources | Do not |
|---|---|---|
| What changes | Priority and pace on the three unblocked items, and on the two gated builds once their gates open | Effort goes to the gate holders instead of to an internal move |
| What does not change | The seven blockers that are not development work in any organization | The same seven |
| Cost exposure | Unknown, and it is the largest single unknown here. If any part of the work moves to North America it is unbudgeted at a 4.3x differential against a zero NA line. If it stays in India the labor cost is broadly unchanged and the change is managerial | None |
| Continuity risk | The September release scope, the Violet Moyer commitment, and the Strev QA and release governance obligations all run through a transition | None |
| Knowledge concentration | Unaddressed, or worse during transition | Unaddressed |
| What has to be true | That delivery pace, and not master data and process ownership, is what limits the outcome | That the gate holders respond to executive weight, which has been tried at Darryl's level and has not produced an owner |
| Reversibility | Poor. Moving a development team twice inside a year costs more than moving it once, and the second move lands during whatever the first disrupted | Not applicable |

| Field | Entry |
|---|---|
| Decision | Does Digital Products take over development resources from the Platforms team in India |
| Verdict | |
| Owner | |
| Date | |
| Conditions attached | |
| Next review | |

A third path exists and is not an ownership option, so it is not in the table: seek named owners and dated commitments for the master data items and the missing and truncated orders from the organizations that hold them. That is the decision that moves the seven, and it is what Darryl needs Sean's weight for.

---

## Part 7. Gap list

Four gaps the 09-09 pack carried are now closed. What remains is below, with the sent status recorded, because an unanswered request is evidence in its own right.

### 7.1 Closed on 2026-09-10

| Was | Answer |
|---|---|
| What prompted the resource question | Sean's concern that Wesco is not getting good results from the India Platforms team, plus a separate doubt that ADM is recoverable |
| Who is in the meeting | Sean and Darryl, one to one |
| The current development arrangement | Resources are supplied by the Platforms team in India and are not part of Darryl's organization. Partially closed; reporting line, backlog authority and funding line remain open |
| Whether "ditch ADM" is the live question | The evaluation Sean wants is narrower: does Digital Products take over the development resources |

### 7.2 Blocks the decision, not the meeting

| # | Gap | Owner of the answer | What it blocks | Sent |
|---|---|---|---|---|
| G1 | The Strev half of forward cost. No Strev line is visible in the FY27 WAM P&L, and the 2027 priorities document carries no cost, effort, sequence or date | Akansh Gangil, with Sunny Sharma's organization | Sean's recoverability concern rests on the amount required going forward, and half of it does not exist | Drafted, not sent |
| G2 | Completeness figures: license master data, serial, MAC and asset tag coverage split simple against complex, and the not-found rate on the enrichment service | Akansh Gangil | Every Partial in Part 4.1, and the value judgement in the meeting | Not sent. Entirely inside Digital Products |
| G3 | Current owner and expected fix date for the missing and truncated orders, or a statement that none exists | Akansh Gangil, escalating to the EUDM and DDP team | The largest single constraint on A and B | Escalation sent by Akansh Gangil; no owner produced. Register A29 trigger has not fired |
| G4 | Whether P360 governance will accept a warranty attribute, given it declined product type as a global attribute on 2026-08-10 and the team works around it | Darryl, with P360 governance | The warranty half of A has no other path |  Not raised |
| G5 | Whether the supply chain programs that earn current revenue depend on ADM specifically, or on Strev with manual loading | Amy Aguirre or Senthil Govindaswamy, with Akansh Gangil | No recoverability judgement is safe without it, and it is answerable in a week | Not sent |
| G6 | Codebase diligence: age, architecture, test coverage, documentation, build and release tooling, environment ownership, open defect backlog | Whoever owns ADM development today | Taking the resources cannot be costed without it | Not sent |
| G7 | Whether the India Platforms team is Merwan Mereby's specifically, who sets the backlog, and the funding line | Sean McCloskey or Akansh Gangil | The remaining half of the arrangement question | Not sent |
| G8 | Resolution of the WMX 5.7 attribute conflict against the standing no-capability-until-2028 record | John Barlolotti or Sid Sarna | The size of the complex-build build | Not sent |
| G9 | Confirmation that the 2026-09-01 Daniel Totino decision closes Register A1, or that architecture work continues under it | Akansh Gangil | Whether C's path can be described as settled | On this week's closure check |
| G10 | Whether the DDP and EUDM sync is automated three times daily or manually triggered | Akansh Gangil | An outbound claim already in use | Open since 2026-08-05, unresolved |
| G11 | Validation of the Jen Turnage product-class grouping rule against known examples | Akansh Gangil, with Jen Turnage | Whether the red MDM license-identification item has a workaround | Not sent |
| G12 | Confirmation that the Microsoft AV requirement is the enrichment driver, and whether it is program-specific or a general service | Akansh Gangil and Violet Moyer | Whether that capability is an asset or a bespoke obligation | Not sent |

### 7.3 What could not be independently established

Named explicitly, because a short list of single-source claims is more credible than a pack that hides them.

Nearly every fact about ADM's data position arrives through Akansh Gangil, who is simultaneously the delivery owner, the requirements owner and the named single point of dependency. The following rest on a single interested source with no corroborating artifact: the 2026-09-09 production confirmations, including that new-order license activation is resolved and that personalized views, bulk selection and edit, uppercase end-user handling and part-number upload are in production, all from AI meeting notes rather than a verbatim transcript; the claim that Exact supplier data is 90 to 95 percent present, which is from a transcript but is self-reported with no independent query; that the 2026-08-27 VAS standard work instruction is being followed at volume, which has never been measured; that WMX captures MAC address, recorded as unconfirmed since 2026-07-14 and never confirmed; and that the enrichment driver is the Microsoft AV requirement, which is Darryl-reported.

Claims that do carry independent artifacts, and which are the spine of this pack: the FY27 P&L and the AOP change log; INC5456198 and the EUDM defect thread; the Jen Turnage product-class grouping table; the Strev SOW declaration on the FY27 AOP form; the WAB approval and the Ankit Chadha resourcing refusal, both from a verbatim transcript; the Register A9 CMP decision; and the seven-area stabilization plan with the 29 open bugs confirmed on review.

---

## Part 8. Working session agenda, David Blondel and Akansh Gangil

Sixty minutes, in decision order. This session exists to close the gaps in 7.2 that Digital Products can close. The gaps that belong to Sean are not on it, and neither is the resource question, because it concerns the scope of one of the attendees and putting it in the room would change what they say about everything else.

| # | Item | Objective | Artifact it must produce | Minutes |
|---|---|---|---|---|
| 1 | Measurement | Agree what can be counted this week without new development | Committed figures for license master data completeness, serial, MAC and asset tag coverage split simple against complex, and the enrichment not-found rate, each with a date. This is G2 | 15 |
| 2 | Forward cost | Establish where Strev SOW spend sits in the FY27 plan and what sizing is obtainable | The P&L line or its absence, and a date by which Sunny Sharma's organization returns sizing by investment area. This is G1 | 15 |
| 3 | The missing and truncated orders | Establish whether an owner exists, or confirm that none does | A named owner and date, or a written statement that none exists, suitable to put in front of Sean. This is G3 | 10 |
| 4 | Warranty into P360 | Decide how the warranty attribute request is made, given the August refusal on product type | A named approach and owner. This is G4 | 10 |
| 5 | Complex builds | Confirm whether the 2026-09-01 decision closes Register A1 and what remains open in the data model | A one-page statement of the settled architecture and the open items, with owners. This is G9 | 10 |

---

## Part 9. Darryl's own position

Held in a separate file so it cannot travel with the pack: `Deliverables/WAM/2026-09-10_WAM_ADM_Darryl_Position.md`. It carries the recommendation Darryl would give if asked directly, what he needs from Sean, and the questions he expects with his answers to them.

---

## Revision history

**2026-09-11, fourth pass.** Bulleted groups rebuilt as single editable text frames so the deck can be edited without shapes drifting. Concern 2 reframed as determining ADM viability. Gate G7 added for the Strev system-of-record proposal, with both return paths drawn as under consideration. Page 5 simplified from a form into a conversation structure, and page 6 reduced to the why-now evidence.

**2026-09-10, revised after slide-by-slide review.** The deck went from eight pages to six and now leads with the two concerns and the decision. The page sorting blockers by what a development team could close was deleted from the deck and retained here. The argument on the page changed from the constraint analysis to velocity, defect burden and control, on Darryl's direction and with his own reasoning recorded. Gates G1 to G6 restored to the data path. Full record: `Deliverables/WAM/2026-09-10_Sean_Deck_Revision_Decisions.md`, Revision 3, and `03_Decision_Log.md`, 2026-09-10.

**2026-09-10, rebuilt.** Restructured around three use cases plus one enabler, replacing the eleven-use-case set derived from the value propositions. The gates page in the companion deck was removed and its content redistributed into the use case it blocks. The four-option ownership frame was replaced by the single development-resource question. Full record of what changed and why: `Deliverables/WAM/2026-09-10_Sean_Deck_Revision_Decisions.md`. Decision-log entry: `03_Decision_Log.md`, 2026-09-10.

**2026-09-09, first version.** Built from the v3 Cowork master prompt against Sean's five-point message. Its audience correction, its dependency analysis in Part 3, and its constraint finding are carried forward unchanged.

## Record corrections made across these sessions

Original statements preserved throughout.

- `Deliverables/WAM/2026-09-01_Sean_WAM_Program_Update_Prep.md`: dated correction note appended on the audience position and on scope.
- `Deliverables/WAM/2026-09-02_Sean_Deck_Brief.md`: dated correction note appended on the audience position and the storyline.
- `06_Stakeholder_Map.md`: entries added under Sean McCloskey on the corrected audience position, the widened request, his two concerns, the one-to-one meeting, and the development resource arrangement.
- `03_Decision_Log.md`: 2026-09-10 entry covering the use case redefinition, the narrowed evaluation, and the new facts.
- `Briefings/`: checked. No briefing carries the superseded first-update framing.
- `Pandoc/processed/2026-09-02_Sean_Deck_Brief-20260902-110019.md` carries the same uncorrected sentence as the deck brief. It is a generated export rather than a source of record and was left as it stands.
