# WAM / ADM Feasibility and Ownership Evidence Pack

**Produced:** 2026-09-09
**Built from:** `Deliverables/WAM/2026-09-09_WAM_ADM_Feasibility_Evidence_Pack_Cowork_Prompt.md` (v3)
**Audience:** Sean McCloskey, to present and discuss in his own meeting.
**Companion graphics:** `Deliverables/WAM/2026-09-09_WAM_ADM_Feasibility_Deck.pptx`

**How to read this pack.** Parts 1 through 8 are evidence. They carry no recommendation and no verdict, because Sean asked to run the decision in the room. Darryl's own position is held in a separate file, `2026-09-09_WAM_ADM_Darryl_Position.md`, and is not part of this pack.

**Where each of the five questions is answered.**

| Question | Where |
|---|---|
| 1. What are the use cases | Part 2, eleven use cases in a fixed structure |
| 2. What is the plan for getting the data from Wesco systems | Part 3, twenty-one dependencies, the sequenced path, the defects and the conflicts |
| 3. Is WAM and ADM feasible, and does it provide value | Part 4 use case by use case, Part 5 in aggregate |
| 4. What would Digital Products be signing up for, and should ADM continue | Part 6, four options on common criteria, verdict left open |
| 5. Independent evidence and a graphical view with a go or no-go placeholder | Part 7.3 on what could and could not be independently established, and the companion deck, whose last page is the decision page |

**Evidence tiers used throughout.** Confirmed means a document, transcript, query result, ticket or system export supports it. Stated means a person asserted it and no independent artifact corroborates it. Inferred means it follows from evidence but was not asserted. Assumed means it is a working assumption and is labelled as such. Nothing in this pack is presented as fact on an Assumed basis.

---

## Part 1. Evidence summary

ADM delivers license order data from DDP and EUDM into a single view, and since 2026-08-17 a governed 60-day expiration notification reaches the owning sales representative in production; those two are the only WAM capabilities in the record with evidence of use rather than evidence of build. No completeness figure exists for any of the five data domains Sean named, which is why every use case below that would otherwise rate Supportable now rates Conditional instead. Three data-completeness defects sit upstream of ADM inside DDP and EUDM, the oldest open since late August with no named fix owner, and all three degrade the same set of use cases rather than separate ones. Serial number capture works for simple products from WMX into DDP, while for complex builds the parent-to-child association does not happen today; the capture point was made explicit inside VAS on 2026-08-27 and the final data model is still open between Daniel Totino and Akansh Gangil. Of the gates standing between the current state and the use cases, the large majority are held outside Digital Products: the WMX roadmap, the EUDM and DDP data model, MDM master data, supplier participation, and IDP engineering capacity. Current WAM revenue is earned through supply chain programs rather than through the license capability, corroborated independently by the FY27 gross margin of 15.2 percent, which is a distribution margin. The record does not establish who owns ADM development today, what Merwan Mereby's team builds, or what prompted the transfer question, so the ownership assessment is built on what would be inherited rather than on a comparison of two known arrangements. The nearest precedent runs the other way: on 2026-08-26 the CMP tool was ruled to stay with the India Platforms team under Merwan Mereby rather than move to Product, with Sean as the counterpart on that decision.

---

## Part 2. Use cases

Sean asked for use cases rather than value propositions. A value proposition is a claim made to a buyer; a use case is a named actor performing a named task on named data to produce a named outcome. Only the second can be tested for feasibility. The eleven below are derived from the seven propositions in the record plus four motions the propositions do not cover.

### UC1. See the whole install base in one place

| Field | Content |
|---|---|
| Actor | Customer asset or facilities manager |
| Trigger | Periodic review, audit, budget cycle, or an incident |
| Task | Open the Strev portal and view every owned item with its lifecycle state |
| Data required | Asset record with serial number, manufacturer part number, product class, warranty term, license term, end-user assignment, parent-child relationship for configured systems |
| Outcome | The customer stops maintaining a parallel spreadsheet and can answer an ownership question without asking Wesco |
| Value type | Customer retention, and enablement of UC2, UC3 and UC9 |
| Beneficiary | Customer |
| Source proposition | Customer-facing 1 |

### UC2. Act before something expires

| Field | Content |
|---|---|
| Actor | Customer asset manager |
| Trigger | A license, warranty or support term approaching its end date |
| Task | Receive a dated alert and act on it before lapse |
| Data required | License term and warranty term per record, a trustworthy end date, an end-user or contact to notify |
| Outcome | Lapses stop happening unnoticed |
| Value type | Risk reduction for the customer, renewal revenue for Wesco |
| Beneficiary | Customer, and commercial |
| Source proposition | Customer-facing 2 |

### UC3. Onboard a customer's data without manual reconciliation

| Field | Content |
|---|---|
| Actor | Managed Services delivery, with ADM and the Managed Services enrichment team |
| Trigger | A new customer engagement or an install-base refresh |
| Task | Ingest customer, supplier and Wesco records, normalize them, and load a usable install base |
| Data required | Wesco order and asset history, supplier attribute data, customer-supplied spreadsheets and documents, a classification and description standard |
| Outcome | Onboarding becomes repeatable rather than bespoke |
| Value type | Cost avoidance, and scalability of the service |
| Beneficiary | Managed Services, and customer |
| Source proposition | Customer-facing 3 |

### UC4. Push a governed renewal signal to the owning sales representative

| Field | Content |
|---|---|
| Actor | Sales representative and Sales Operations |
| Trigger | An expiration date entering the notification window |
| Task | Receive a dated, attributed notification and open a renewal conversation |
| Data required | License order record, license term, expiration date, current owning representative, customer identity resolved to a single ERP record |
| Outcome | Renewal work starts from a signal rather than from account-by-account research |
| Value type | Revenue |
| Beneficiary | Commercial |
| Source proposition | Internal commercial 1, and its delivered slice is internal commercial 3 |

### UC5. Bring install-base facts into an account conversation

| Field | Content |
|---|---|
| Actor | Sales representative |
| Trigger | Account planning, a quarterly business review, or a refresh conversation |
| Task | Look up what a customer already owns before proposing what to sell |
| Data required | Complete purchase history by customer and supplier, product classification, lifecycle state, non-Wesco holdings where the customer supplies them |
| Outcome | Cross-sell and refresh conversations rest on data rather than recollection |
| Value type | Revenue |
| Beneficiary | Commercial |
| Source proposition | Internal commercial 2 |

### UC6. Not a distinct use case

Internal commercial proposition 3, "already producing pipeline, not just promised," describes the first delivered slice of UC4 rather than a separate task performed by a separate actor. It is recorded here as a finding rather than rated: it is evidence for UC4's feasibility, and presenting it as a seventh proposition double counts one capability. This is the only proposition in the set that does not decompose into a testable use case.

### UC7. Keep a complex build visible and serviceable after delivery

| Field | Content |
|---|---|
| Actor | Customer, Managed Services delivery, and Wesco field service |
| Trigger | Delivery of a configured multi-component system, then any later service event |
| Task | Identify the delivered system, its components, and each component's serial number, MAC address and location |
| Data required | Parent-child structure from the VAS finished-goods template, serial number and MAC address per component, asset tag, room or location, order and configuration context |
| Outcome | A configured system remains identifiable in the customer install base after it leaves the warehouse |
| Value type | Customer retention, service enablement, and access to a stated company growth area |
| Beneficiary | Customer, Managed Services |
| Source proposition | Added 2026-08-26, absent from every prior value statement |

### UC8. Enrich an order line on request

| Field | Content |
|---|---|
| Actor | An internal program team, first instance Violet Moyer's Microsoft AV requirement |
| Trigger | A program needs shipping and price detail against order lines it holds |
| Task | Submit sales order, Wesco part number and manufacturer part number, and receive enriched fields |
| Data required | Sales order presence in EUDM, full manufacturer part number, shipping fields, transaction price |
| Outcome | A program team stops assembling the same data by hand |
| Value type | Cost avoidance, and enablement of further internal consumption |
| Beneficiary | Internal operations |
| Source proposition | New. Not derived from any proposition |

### UC9. Stand up an install base for a new Managed Services engagement

| Field | Content |
|---|---|
| Actor | Managed Services delivery |
| Trigger | A signed engagement |
| Task | Configure a Strev tenant and load the customer's install base |
| Data required | Everything in UC1, plus tenant configuration, custom fields, views and business rules |
| Outcome | Time to first usable customer view falls, and the deployment model becomes repeatable |
| Value type | Cost avoidance, margin, scalability |
| Beneficiary | Managed Services |
| Source proposition | New. This is the motion the Strev tenant cloning investment is aimed at |

### UC10. Support a supply chain program

| Field | Content |
|---|---|
| Actor | Supply chain program team, with Managed Services |
| Trigger | An active program with a customer |
| Task | Ingest, hold and report program asset data through Strev, largely by file upload today |
| Data required | Program-specific asset and order data, much of it customer or program supplied rather than drawn from the license path |
| Outcome | The program runs, and this is where current WAM revenue is earned |
| Value type | Revenue |
| Beneficiary | Commercial, Managed Services |
| Source proposition | New. Absent from every value proposition, and it is the motion that earns the money |

### UC11. Handle an entitlement event

| Field | Content |
|---|---|
| Actor | ADM operations, Sales Operations, customer |
| Trigger | A purchase, activation, renewal, upgrade, seat change, transfer, expiration, cancellation or support change |
| Task | Record the event and update the customer's rights accordingly |
| Data required | An entitlement data model, event definitions, the source system for each event type |
| Outcome | Rights held by a customer stay accurate through their lifecycle |
| Value type | Enablement of UC1, UC2 and UC4; risk reduction |
| Beneficiary | Customer, commercial, operations |
| Source proposition | New. Defined conceptually in section 8 of `WAM_Data_Architecture.md`, implementation not validated |

### 2.1 The enrichment capability, read as evidence

The enrichment MVP was scoped and prioritized ahead of the asset-upload epic by Akansh Gangil with Violet Moyer's agreement, decided 2026-09-01 and confirmed in the 2026-09-03 backlog refinement (Confirmed, verbatim transcript). It accepts sales order, Wesco part number and manufacturer part number and returns shipping fields and transaction price with not-found statuses; average-price logic was deferred until requirements are clearer. That the driver is Violet Moyer's Microsoft AV data-gathering requirement is Darryl-reported as of 2026-09-09 and is not otherwise in the record; confirm with Akansh Gangil and Violet Moyer before this pack is used outside Darryl's own hands.

Four things follow, and they are what make this more than a feature note.

It serves UC8, an internal program need, not a customer-facing outcome. Whether it is a Microsoft AV specific build or a general ADM enrichment service that one program funded first is not established in the record, and it is the question that decides whether this is evidence of a repeatable capability or of a bespoke obligation. That distinction carries directly into what a transfer would inherit.

The cost of the deferral is not quantified anywhere. The asset-upload epic serves UC1, UC3 and UC7, so the deprioritization moved capacity from three use cases to one; supplier ID work continued in parallel. Neither the time cost nor the sequence cost is stated, and no one has been asked for it.

What the Microsoft AV program needs beyond shipping fields and transaction price is not in the record, and neither is whether ADM can obtain it. The deferred average-price logic is the one named gap.

Read as evidence on the ownership question, a capability scoped on 09-01 and refined against a live business requirement by 09-03 says something about the current development arrangement's responsiveness. It is presented here as evidence, not as an argument in either direction, because a two-day turn on a scoped MVP and a four-week-old unowned defect are both true at once and they point different ways.

---

## Part 3. The data plan

### 3.0 Architectural facts that constrain every answer

Confirmed by Darryl, 2026-08-19. DDP and EUDM are the single source of truth for asset data and the only route into ADM. WMX and VAS deliver into DDP; ADM takes nothing directly from either. ACT is a contingency path, not integrated today. The complex-build capture mechanism is a WMX-triggered workflow into VAS, and VAS writes the complete parent-child structure, serial, MAC and attributes to DDP, which is new build. P360 provides serialization setup to WMX. Current state for the complex-build flow is pre-DDP, undefined and largely incapable of the flow, so what follows describes a target path and where it is gated, not a working path with faults.

### 3.1 Which dependency chain each use case runs on

Every use case is traced to the specific dependencies it needs and, through 3.2a, to a named Wesco system of record for each. Nothing below ends at a domain; each chain ends at a system.

| Use case | Dependencies it requires | Systems of record at the end of the chain |
|---|---|---|
| UC1 | D1, D2, D3, D4, D8, D9, D10, D11, D12, D13, D14, D16, D17, D18 | DDP and EUDM, WMX, VAS, MDM, P360, Core ERP, NetSuite, supplier feeds |
| UC2 | D1, D3, D5, D7, D17, D18 | DDP and EUDM, MDM, IAP, supplier feeds |
| UC3 | D2, D4, D16, D18, D19 | MDM, P360, supplier feeds, customer documents through IDP |
| UC4 | D1, D3, D5, D6, D7, D8, D9 | DDP and EUDM, MDM, IAP, Core ERP, NetSuite |
| UC5 | D1, D8, D9, D16, D18, D19 | DDP and EUDM, Core ERP, NetSuite, P360, supplier feeds, customer documents |
| UC7 | D10, D11, D12, D13, D14, D15 | WMX, VAS, P360, DDP and EUDM |
| UC8 | D1, D8, D9, D20 | DDP and EUDM, Core ERP, NetSuite |
| UC9 | everything in UC1, plus Strev tenant configuration | as UC1, plus Strev |
| UC10 | D1, D18, plus program and customer supplied data | DDP and EUDM, supplier feeds, customer and program data |
| UC11 | D21, and then D1, D3, D5 once a model exists | not established. This is the finding |

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
| D2 | The Jen Turnage rule is unvalidated, and MDM has not completed license identification | MDM, with Jen Turnage on taxonomy | No | Validate the rule against known examples, then decide whether it substitutes for the MDM item. No owner or date | UC1, UC2, UC4 and UC5 all rest on knowing which items are licenses |
| D3 | MDM and DDP have not defined license-term structures | MDM. Inder Gambhir and Gandhi Subramanian are named in the record | No | None in evidence. Red since the July slide | UC2 and UC4 cannot be trusted without a term |
| D4 | Same as D3 | MDM | No | None in evidence | Degrades every customer-facing view |
| D5 | Legacy record disposition needs a reliable post-fix export | Akansh Gangil | Yes | Export after the pending-activation fix, then dispose. September release | UC4 attribution errors on legacy records |
| D6 | Root cause is upstream in D9 | Akansh Gangil, with the EUDM team | Partly | Confirm the 09-09 resolution against a transcript or a query, not meeting notes | UC4 fires on records that cannot activate |
| D7 | End-date trustworthiness depends on D3 and on supplier end dates | MDM and suppliers | No | Milestone and ExacQ end dates loaded. No plan for the rest | A wrong date is worse than no alert |
| D8 | The truncation is upstream in EUDM. No named fix owner since late August | EUDM and DDP team. Daniel Totino and the EUDM team per the 09-01 prep, tier Stated | No | Akansh Gangil's escalation has not produced an owner. Darryl escalates further if it stays silent. Register A29, B53 | Orders are missed outright, which caps D1, D18, D20 and every use case above them |
| D9 | Pipeline breaks from Core ERP and NetSuite into EUDM | EUDM and DDP team, with BI_Wesco_Integration_Support_L2 | No | INC5456198 open. NetSuite hydration path not designed | The install base is incomplete by an unmeasured amount |
| D10 | Whether capture is mandatory or optional is not established | John Barlolotti as GPO for WMX, delegated from Steve Leslie; Sid Sarna as solution architect | No | Open item on the 08-19 architecture. No owner | UC1 and UC7 rest on capture actually happening |
| D11 | The final data model is open, and the VAS to DDP write is unbuilt | Daniel Totino with Akansh Gangil on the model; build ownership not established | Partly | 09-01 decision set WMX for standard collection and VAS governance for project-specific requests. Data model still open. Register A1 marked potentially closed, unconfirmed | UC7 does not exist until this lands |
| D12 | WMX 5.7 attribute support is unconfirmed, and conflicts with the standing no-capability-until-2028 record | John Barlolotti and Sid Sarna | No | Resolve the conflict with GPO. Named as open since 08-19 | Decides how much VAS has to carry, and therefore the size of the build |
| D13 | Same as D12 | Same as D12 | No | Same as D12 | Same as D12 |
| D14 | The serialized write to DDP is new build with no funded plan | Build ownership not established | Partly | Required before Strev bulk parent-child mapping can consume anything | The one genuine dependency running Wesco to Strev |
| D15 | No source system identified | Open | Unknown | Name a source, or drop the field from UC7 | UC7 service outcomes need location |
| D16 | P360 governance refused the attribute | P360 governance | No | Workaround continues outside P360. The governance question is unresolved | Classification stays local and unauditable |
| D17 | Warranty term structures are undefined in MDM | MDM, with Supplier Relations | No | GPO and MDM work is defined but not delivered | UC1 and UC2 warranty claims are unsupported |
| D18 | Supplier participation and cadence | Jarod Booth's organization via David Blondel, and Natalie Marquardt in practice, who is flagged as a single point of dependency | No | Continues through Sales Operations outreach. No coverage target | Caps UC5 directly |
| D19 | Approved architecture, no engineering capacity | Ankit Chadha | No | One to two week capacity investigation from 09-02. Check in around 09-16 | UC3 and UC5 keep absorbing manual document handling |
| D20 | Not-found rate is unmeasured, and it is a function of D8 and D9 | Akansh Gangil | Yes | Measure it during the MVP. Not currently planned | The one delivered internal service has no quality figure |
| D21 | No data model, no source mapping | Open. Product decision, not a data decision | Yes | Define the model, or drop entitlement from the value language | UC11 cannot be scoped, priced or sold |

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
| W1 | Manufacturer part numbers truncated at 15 characters in EUDM Bronze and Silver, while ADM holds full values, so exact matching fails | Root cause named 2026-08-25, symptom tracked since 2026-07-28 | None. Akansh Gangil's escalation has produced no owner; Register A29's trigger has not fired | UC1, UC4, UC5, UC8 | Orders are missed outright, so the install base and the notification set are both short by an unmeasured amount |
| W2 | Sample orders absent from EUDM outright, requiring hydration from NetSuite | Confirmed 2026-09-01 | None named | UC1, UC5, UC8 | A whole order class is invisible to ADM |
| W3 | Core ERP sales orders present in the ERP but missing from the EUDM table, INC5456198 | Raised 2026-07-27 | Akansh Gangil, Vishal Balasubramanian, Revanth Jampana named in evidence; BI_Wesco_Integration_Support_L2 asked to verify upstream cause. No fix owner | UC1, UC4, UC5, UC8, and probably UC2 through D6 | Legitimate orders never reach the data lake, so this is a pipeline failure rather than a release defect |

A defect open four weeks with no owner is evidence about the operating model, not about the defect. All three sit in the same place, upstream of ADM and outside Digital Products, and the escalation route available to Darryl has been used and has not produced an owner.

### 3.5 Conflicts in the record, flagged rather than resolved

These are stated as conflicts because resolving them by choosing a side would put an assertion into a pack whose credibility depends on not doing that.

**WMX complex-build attribute capability.** Section 0 of `WAM_Data_Architecture.md` records no capability and no roadmap until 2028, while later evidence expects WMX 5.7 to add MAC address and asset tag fields. Either the earlier statement refers to full parent-child support rather than parent attributes, or it is out of date. The answer decides how much VAS has to carry and therefore the size of the D11 and D14 build. Resolve with John Barlolotti or Sid Sarna.

**The complex-build architecture is not settled.** The 2026-09-01 decision, WMX for standard serial collection and VAS governance for project-specific and ad hoc requests, refines rather than reverses the 08-31 position. The final data model, meaning the serial-number anchor, the parent and room relationship, the required attributes, and the VAS to WMX handoff, remains open between Daniel Totino and Akansh Gangil. Register A1 is marked potentially closed and has not been confirmed with Akansh Gangil.

**The DDP and EUDM sync automation.** The 08-05 Backlog Deep Dive deck marks the automated three-times-daily sync as Q2 complete, while the 07-16 and 07-20 record states the feed is manually triggered daily and instructs explicitly that the automation not be presented as production-grade. Both cannot be current. This claim has already appeared in outbound material.

**IDP and ADM: approved but unstaffed.** The proof of concept and integration architecture received WAB approval, and production resourcing stalled the same week when Ankit Chadha would not commit engineering resources, citing competing high-volume work and an October Oracle deadline. Approved but unstaffed is the accurate description, and it is a different problem from unapproved.

**The software and license identification rule.** Jen Turnage's product-class grouping criterion is a durable data-source fact and has not been validated against known examples. Do not treat it as final, and do not treat it as closing the red MDM item without that validation.

**Coverage language.** The phrase "beyond Core and Anixter part numbers" is under a standing instruction not to be used in outbound material until resolved with Akansh Gangil, on the basis that it rests on a probable misunderstanding and sits close to two adjacent concepts. The safe formulation is that license data now syncs from multiple source systems into a single view.

---

## Part 4. Feasibility ratings

### 4.1 The rubric is a proposal

Sean said the rating system is to be discussed. What follows is a straw man, shown working so the scale can be judged against real cases. The evidence in Part 3 and the ratings here are deliberately kept in separate columns, so changing the scale does not require redoing the analysis.

| Dimension | Scale | Rule |
|---|---|---|
| Data feasibility | Supportable now, Conditional, Not supportable | Supportable now is not permitted without a completeness figure. Where the figure is missing the rating is Conditional and the missing number goes on the gap list |
| Business value | High, Moderate, Low, stated against the use case's value type | Realized and planned stay separate. Value is what it is worth if delivered |
| Effort and dependency | Inside Digital Products, Mixed, Outside Digital Products | Judged on where the gates sit, not on where the code is written |
| Confidence | Strong, Moderate, Weak | The strength of the evidence behind the other three ratings, not confidence in success |

The completeness rule is what stops this pack from repeating the benefits underreporting problem in the opposite direction, by overstating rather than understating. Its immediate consequence is visible below: no use case rates Supportable now, including two that are running in production today. That is the rule working, not a judgment that nothing works.

### 4.2 The ratings

| UC | Data feasibility | Gate and gate holder | Business value | Effort and dependency | Confidence |
|---|---|---|---|---|---|
| UC1 Whole install base in one place | Conditional | D2, D3, D8, D9, D11, D17. MDM, EUDM and DDP team, GPO | High, customer retention | Outside Digital Products | Moderate |
| UC2 Act before something expires | Conditional | D3 license term, red since July. MDM | High, risk and renewal revenue | Outside Digital Products | Moderate |
| UC3 Onboard without manual reconciliation | Conditional | D18 supplier coverage, D19 IDP capacity. Supplier Relations, Ankit Chadha | High, cost avoidance and scalability | Outside Digital Products | Moderate |
| UC4 Governed renewal signal to the rep | Conditional | Delivered and in production; no completeness figure for D1, D3 or D7. Akansh Gangil holds the measurement | High, revenue | Mixed | Strong on delivery, Weak on coverage |
| UC5 Install-base facts in an account conversation | Conditional | D18, D8, D9. Supplier Relations, EUDM and DDP team | Moderate to High, revenue | Outside Digital Products | Moderate |
| UC6 | Not rated. See Part 2, UC6 | | | | |
| UC7 Complex build visible and serviceable | Not supportable today | D11, D12, D13, D14, D15. Daniel Totino, GPO, and an unnamed build owner | High, retention and a stated growth area | Outside Digital Products | Strong on the gap, Weak on the path |
| UC8 Enrich an order line on request | Conditional | D8 and D9 set the not-found rate, and it is unmeasured | Moderate, cost avoidance | Mixed | Strong on delivery, Weak on quality |
| UC9 Stand up an install base for an engagement | Conditional | Everything in UC1, plus tenant tooling that is a 2027 Strev item | High, margin and scalability | Outside Digital Products | Weak |
| UC10 Support a supply chain program | Conditional | Runs today largely by file upload into Strev. No completeness figure, and the license path is not what serves it | High, revenue, and it is the revenue that exists | Mixed | Moderate |
| UC11 Handle an entitlement event | Not supportable | D21. No data model and no source mapping. The gate holder is product, which is inside Digital Products | Moderate, enablement | Inside Digital Products | Strong on the absence |

Two Conditional ratings, UC4 and UC8, describe capabilities that are live in production. The rating is about measured coverage, not about whether the software runs. Saying so plainly is what keeps the rest of the pack credible.

Every Conditional rating above names a gate and a gate holder except one. UC11's gate is held inside Digital Products and has no assigned person, which is a finding rather than a blank: the entitlement model is the one item on this list that Darryl's own organization could close and has not.

---

## Part 5. Does WAM and ADM provide value to the organization

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

This is the open strategic question from 2026-08-05 and no decision has been taken on it. The license capability is what was requested and what the roadmap is built around. The revenue is earned through supply chain programs, UC10, which the value propositions do not describe and which draws only lightly on the license data path. The FY27 gross margin of 15.2 percent corroborates this independently: it is a distribution margin, and a license and software business would not produce it.

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

## Part 6. The ownership question

### 6.1 The current arrangement is not established, and that blocks the assessment

The record does not establish who owns ADM development today, how any India platform team relates to Akansh Gangil's scope, or what the reporting and funding lines are. This is the first gap to close and the assessment cannot be completed without it. What the record actually holds:

Merwan Mereby appears in the WAM FY27 AOP submission's stakeholder field as "Platform" (Confirmed, the submitted form). He is named as leading the India Platforms team that retains the CMP tool (Confirmed, decision of 2026-08-26). A separate "Merwan" appears in the WAM Data Challenges thread on a licensing discussion, and `06_Stakeholder_Map.md` carries an explicit name-collision caution that this may or may not be the same person, pending a surname. No entry anywhere in the record states that Merwan Mereby's team develops ADM.

Set against that, Nitin Pandey is named running the automation team on WAM part identification, co-authoring the 2026-08-06 requirement estimation for asset data capture and order capture, and handling the replacement hire for an ADB-skilled data engineer. Akansh Gangil is named on ADM, DDP and WAM product execution. Neither is described as the development line.

Do not infer an organization chart from the FY27 P&L. The 19.00 FTE India roster tells you where the cost sits, not who manages it.

Also open, and material: an FY27 Product and Platform scope split is being worked with Rajesh, and the FY27 WAM scope field could not be finalized until it is agreed. A transfer question arriving while that split is unresolved may be the same question in a different form, or may be independent of it. The record does not say which.

**What triggered Sean's question is not in the record at all.** A transfer proposal from a named person, a resourcing change, a performance concern, or an organizational plan each imply a different pack and a different decision. This is the single most useful thing to learn before the meeting.

### 6.2 The nearest precedent runs the other way

On 2026-08-26, Register A9 closed on the answer that the CMP tool stays with the India Platforms team under Merwan Mereby and is not coming to Product. Same team, opposite direction, decided six weeks ago, with Sean himself as the counterpart on that thread. Stated as context. It is not an argument, and the two tools are not equivalent: CMP is a tool with a business owner moving elsewhere, ADM is a platform with a live delivery program and external commitments.

### 6.3 What would be inherited

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

### 6.4 Defining success, then the options

Success is not that a transfer completes. Success is that a stated set of use cases reaches a stated feasibility level within a stated period at a stated cost. On the evidence in Part 4, a defensible success statement would read: UC4 and UC8 measured and rated Supportable now, and UC1 and UC2 moved from Conditional to Supportable now, within twelve months, at no increase in the FY27 development expense line. That statement is offered as a starting point for the room to change, not as a target already agreed.

The four options are assessed on identical criteria. None is pre-selected and no verdict is entered.

#### Option A. Status quo. Development stays where it is.

| Criterion | Assessment |
|---|---|
| Cost | No change. $150,480 FY27 expense after capitalization |
| What it fixes | Nothing, and it breaks nothing. Delivery has been responsive on scoped work, evidenced by the 09-01 to 09-03 enrichment MVP turn |
| What it does not fix | All twelve external gates. The concentration on Akansh Gangil. The absence of completeness measurement |
| What it puts at risk | If the transfer question was prompted by a real dissatisfaction that is not in the record, doing nothing leaves it unaddressed |
| What has to be true | That the external gates are the binding constraint and the development arrangement is not |
| How it is reversed | Not applicable |
| Does it address the constraint set | No |

#### Option B. Digital Products takes over development.

| Criterion | Assessment |
|---|---|
| Cost | Unknown, and the largest single unknown in this pack. If any part of the work moves to North America it is unbudgeted at a 4.3x differential against a zero NA line. If it stays in India the labor cost is broadly unchanged and the change is managerial |
| What it fixes | Backlog control and prioritization sit with the same organization that owns the product. Removes one handoff |
| What it does not fix | All twelve external gates. The Strev SOW obligations transfer unchanged. The concentration on Akansh Gangil is unaffected or worsened during transition |
| What it puts at risk | Delivery continuity across the September release, the enrichment commitment to Violet Moyer, and the Strev QA and release governance obligations. A transition period during which the three unowned defects still have no owner |
| What has to be true | That the current arrangement is a material constraint on outcomes, which the record does not currently establish either way. And that the codebase diligence, which has not been done, returns nothing disqualifying |
| How it is reversed | Poorly. Moving a development team twice inside a year is more expensive than moving it once, and the second move would land during whatever the first move disrupted |
| Does it address the constraint set | No |

#### Option C. Partial or staged transfer.

| Criterion | Assessment |
|---|---|
| Cost | Lower than B in the near term. Product ownership and backlog control moving without the development line moving has no direct labor cost |
| What it fixes | Puts prioritization where the product accountability already sits, which is arguably the state today through Akansh Gangil in practice, and would make it explicit |
| What it does not fix | The twelve external gates. It may also formalize a split accountability, where Digital Products owns the outcome and another organization owns the capacity to deliver it |
| What it puts at risk | Ambiguity. A staged transfer with no defined end state becomes a standing arrangement by default |
| What has to be true | That a defined subset can be separated cleanly, which the codebase diligence would have to establish |
| How it is reversed | Readily, if each stage has a defined gate and a stated end state |
| Does it address the constraint set | No |

#### Option D. Stop or wind down ADM.

| Criterion | Assessment |
|---|---|
| Cost | Saves $150,480 of FY27 expense and releases 19.00 FTE. The costs are the enterprise consequences in 5.3 and the wind-down itself, neither of which is quantified |
| What it fixes | Ends spend on a capability whose benefits are largely unrealized, and forces the license-versus-supply-chain question to a decision |
| What it does not fix | The supply chain programs that earn the revenue still need whatever ADM does for them, and what that is has not been established |
| What it puts at risk | Sales Operations loses its only governed renewal signal, set at Senior Director level. The Microsoft AV enrichment commitment fails. Customer engagements running on Strev lose their data preparation path, and the extent of that dependency is unknown |
| What has to be true | That the current revenue motion does not depend on ADM, and that the internal consumers can be absorbed elsewhere. Neither is established |
| How it is reversed | Not realistically inside the FY27 horizon |
| Does it address the constraint set | It removes the question rather than addressing it |

**None of the four options addresses the constraint set.** That is the most important line in this part, and it is a finding rather than an argument for any option. A fifth path, which is not an ownership option and therefore is not listed above, would be to seek named owners and dated commitments for D8, D9, D3 and D2 from the organizations that hold them. That is a different kind of decision, and it is the one that changes the feasibility ratings.

### 6.5 Go or no-go, for completion in the meeting

| Field | Entry |
|---|---|
| Decision statement | Does ADM continue, and if so under whose development ownership |
| Options | A: status quo. B: Digital Products takes development. C: partial or staged. D: stop or wind down |
| Criterion 1: does it move the binding constraint | Evidence: Part 3.3, twelve of twenty-one dependencies external. None of A to D moves it |
| Criterion 2: cost and budget exposure | Evidence: Part 6.3. NA assignment unbudgeted at 4.3x; capitalization treatment open; Strev spend location unknown |
| Criterion 3: continuity of live commitments | Evidence: Part 6.3 live commitments row, and Part 5.3 |
| Criterion 4: knowledge concentration | Evidence: Part 6.3. Akansh Gangil, unaddressed under every option |
| Criterion 5: what the enterprise loses | Evidence: Part 5.3, with the Strev dependency question unresolved |
| Criterion 6: reversibility | Evidence: Part 6.4, per option |
| Verdict | |
| Owner | |
| Date | |
| Conditions attached | |
| Next review | |

---

## Part 7. Gap list

Merged with the outstanding requests from section 5 of `2026-09-01_Sean_WAM_Program_Update_Prep.md` rather than duplicated. The Sent column records whether the request has actually been made, because an unanswered request is evidence in its own right.

### 7.1 Gaps that block the meeting

| # | Gap | Owner of the answer | What it blocks | Sent |
|---|---|---|---|---|
| G1 | What prompted the transfer question: a proposal, a resourcing change, a performance concern, or an organizational plan | Sean McCloskey | The whole shape of Part 6. Without it the options are assessed against an unknown problem | Not sent |
| G2 | The current ADM development arrangement: what team develops it, the reporting and funding lines, who sets the backlog, and how that relates to Akansh Gangil's scope | Sean McCloskey, or Akansh Gangil | Part 6.1, and therefore any comparison between options | Not sent |
| G3 | Whether "ditch ADM" is Sean's own phrase | Sean McCloskey | Whether option D is assessed on equal terms or treated as a rhetorical bracket | Not sent |
| G4 | Who is in the meeting, and when | Sean McCloskey | Whether the pack needs a single orientation page for people without Sean's year of context | Not sent |
| G5 | Which of the four recent threads Sean has already seen through another channel | Sean McCloskey | How much of Parts 2 and 3 is new to him | Not sent |
| G6 | Confirmation that the Microsoft AV requirement is the enrichment MVP driver, and whether Violet Moyer's requirement is program-specific or general | Akansh Gangil and Violet Moyer | Part 2.1, and whether the capability is an asset or a bespoke obligation in Part 6.3 | Not sent |
| G7 | Whether the supply chain programs that earn current revenue depend on ADM specifically, or on Strev with manual loading | Amy Aguirre or Senthil Govindaswamy, with Akansh Gangil | Part 5.3, and option D cannot be assessed without it | Not sent |

### 7.2 Gaps that block the decision but not the meeting

| # | Gap | Owner of the answer | What it blocks | Sent |
|---|---|---|---|---|
| G8 | Serial number, MAC address and asset tag coverage today, split simple products versus complex builds, since the 08-27 VAS standard work change | Akansh Gangil | UC1 and UC7 ratings. Request 6 in the prep file | Drafted, not sent |
| G9 | License master data completeness: how many license part numbers carry a license term and a clean description, against the total | Akansh Gangil, with MDM and DDP | UC2 and UC4 ratings. Converts the red MDM dependency into a number. Request 7 | Drafted, not sent |
| G10 | The not-found rate on the enrichment service | Akansh Gangil | UC8 rating | Not sent |
| G11 | Current owner and expected fix date for W1, W2 and W3, or a statement that none exists | Akansh Gangil, escalating to the EUDM and DDP team | Tier 0 of the sequenced path, and every measurement above it. Request 9 | Escalation sent by Akansh Gangil; no owner produced. Register A29 trigger has not fired |
| G12 | License activation position and the state of the null and missing sales order date root cause, confirmed against a transcript or query rather than meeting notes | Akansh Gangil | D6, and the credibility of the 09-09 relief claim. Request 8 | Drafted, not sent |
| G13 | Codebase diligence: age, architecture, test coverage, documentation, build and release tooling, environment ownership, open defect backlog | Whoever owns ADM development today | Option B and option C cannot be costed | Not sent |
| G14 | Where Strev SOW spend sits in the FY27 WAM P&L, and if nowhere, what the 2027 requirement is | Akansh Gangil | Part 6.3 vendor row, and the separate Strev funding-attribution decision. Request 1 | Drafted, not sent |
| G15 | Strev sizing by investment area, separated rather than as a single total, and which items are Wesco requirements versus Strev's own product direction | Akansh Gangil, with Sunny Sharma's organization | The 2027 requirement and its attribution. Requests 2 and 3 | Drafted, not sent |
| G16 | Whether a Strev entry exists in the FY27 AOP cycle | Akansh Gangil | Request 4 | Drafted, not sent |
| G17 | Whether Ron Snyder and the Navigator owners have been consulted on the entroCIM and Ascent integration targets | David Blondel | Whether the Strev API roadmap can be presented as a portfolio position. Request 5 | Drafted, not sent |
| G18 | Resolution of the WMX 5.7 attribute conflict against the no-capability-until-2028 record | John Barlolotti or Sid Sarna | D12, D13, and the size of the D11 and D14 build | Not sent |
| G19 | Whether the DDP and EUDM sync is automated three times daily or manually triggered | Akansh Gangil | An outbound claim already in use | Open since 08-05, unresolved |
| G20 | Confirmation that the 09-01 Daniel Totino decision closes Register A1, or that architecture work continues under it | Akansh Gangil | Whether the complex-build path is settled enough to present | On this week's closure check |
| G21 | Validation of the Jen Turnage product-class grouping rule against known examples | Akansh Gangil, with Jen Turnage | D2, and whether the red MDM item has a workaround | Not sent |
| G22 | A source system for room or location per component | Daniel Totino, with GPO | D15 and the UC7 service outcome | Not sent |

### 7.3 What could not be independently established

Named explicitly, because a short list of single-source claims is more credible than a pack that hides them, and because Sean asked for independent data gathering.

Nearly every fact in this pack about ADM's data position arrives through Akansh Gangil, who is simultaneously the delivery owner, the requirements owner and the named single point of dependency for WAM and ADM. The following claims rest on a single interested source with no corroborating artifact:

The 2026-09-09 production confirmations, including that new-order license activation is resolved and that personalized views, bulk selection and edit, uppercase end-user handling and part-number upload are in production. Source is AI meeting notes from the ADM connect with Natalie, not a verbatim transcript. Treat as Stated.

The coverage claim that Exact supplier data is 90 to 95 percent present. Verbatim transcript, but self-reported by the delivery team with no independent query.

That the 08-27 VAS standard work instruction is being followed at volume. No measurement exists.

That WMX captures MAC address. Recorded as unconfirmed since 2026-07-14 and never confirmed.

That the enrichment MVP driver is the Microsoft AV requirement. Darryl-reported, 2026-09-09.

Claims that do carry independent artifacts, and which are the spine of this pack: the FY27 P&L and the AOP change log; INC5456198 and the EUDM defect thread; the Jen Turnage product-class grouping table; the Strev SOW declaration on the FY27 AOP form; the WAB approval and the Ankit Chadha resourcing refusal, both from a verbatim transcript; the Register A9 CMP decision; and the seven-area stabilization plan with the 29 open bugs confirmed on review.

---

## Part 8. Working session agenda, David Blondel and Akansh Gangil

Ninety minutes, in decision order. Each item states its objective and the artifact it must produce. This session exists to close the gaps in 7.2; the gaps in 7.1 are Sean's to answer and are not on this agenda.

| # | Item | Objective | Artifact it must produce | Minutes |
|---|---|---|---|---|
| 1 | The three defects | Establish whether an owner exists for W1, W2 and W3, or confirm that none does | A named owner and date per defect, or a written statement that none exists, suitable to put in front of Sean | 15 |
| 2 | Measurement | Agree what can be counted this week without new development | Committed figures for serial, MAC and asset tag coverage split simple versus complex, license master data completeness, and the enrichment not-found rate, each with a date | 20 |
| 3 | Complex-build path | Confirm whether the 09-01 decision closes Register A1, and what remains open in the data model | A one-page statement of the settled architecture and the open items, with owners | 15 |
| 4 | The WMX conflict | Decide who resolves the WMX 5.7 versus 2028 conflict and by when | A named approach to John Barlolotti or Sid Sarna with a date | 10 |
| 5 | Strev 2027 | Establish where SOW spend sits in the FY27 plan and what sizing is obtainable | The P&L line or its absence, and a date by which Sunny Sharma's organization returns sizing by investment area | 15 |
| 6 | Functional overview | Agree the business-language description across license, asset, serial and metadata, entitlement and renewal | David Blondel's overview, scoped to what the data supports, with the aspirational portion separated | 10 |
| 7 | Build plan | Sequence the work that is funded against the work that needs 2027 money | A sequenced plan with dependencies, resourcing and dates, marked funded versus unfunded | 15 |

Two items are deliberately absent. The ownership question is not on this agenda, because it concerns the scope of one of the two attendees and putting it in a working session would change what they say about everything else. And the entitlement data model is not on it either, because it is a product decision for Darryl and David Blondel rather than a session item.

---

## Part 9. Darryl's own position

Held in a separate file so it cannot travel with the pack: `Deliverables/WAM/2026-09-09_WAM_ADM_Darryl_Position.md`. It carries the recommendation Darryl would give if asked directly in the meeting, what he needs from Sean, and the questions he expects with his answers to them. Keeping it out of the pack is what lets Sean run his own discussion; having it ready is what lets Darryl answer in the room.

---

## Relationship to the 2026-09-02 deck brief

The nine-slide storyline in `Deliverables/WAM/2026-09-02_Sean_Deck_Brief.md` was built around two decisions: Strev 2027 funding attribution, and cross-functional air cover on internal data collection. Sean's message introduces a third and larger decision that subsumes the first and reframes the second.

**Recommendation: re-sequence rather than rebuild, and do not build the deck in this session.**

| Slide | Status against this pack |
|---|---|
| 1. Where the capability stands | Holds, and becomes Part 1 of this pack. Its claim needs the completeness rule attached |
| 2. What the business gets today | Holds, narrowed. UC4 and UC8 are the two capabilities in production, and both rate Conditional on coverage |
| 3. Complex builds, the gap | Holds, unchanged. This is UC7 |
| 4. What is blocking completion | Strengthens. Twelve of twenty-one dependencies external is a stronger statement than five constraint holders, and it is derived rather than asserted |
| 5. The evidence, three defects | Holds, and moves earlier. It is Tier 0 of the sequenced path, not supporting material |
| 6. Strev 2027 priorities | Demote to backup. It is a separate decision and belongs in a separate conversation |
| 7. Why this is a portfolio investment | Demote to backup, same reason |
| 8. The 2027 requirement | Cut from this meeting. Still blocked on G14 and G15, and it is not what Sean asked for |
| 9. What I need from you | Rebuild. The ask is now cross-functional weight on the defects and the MDM item, plus an answer on what prompted the transfer question |
| New | Ownership and constraint boundary, and the go or no-go page. Both are in the companion deck |

The audience correction in section 2.1 of the prompt applies to slides 1 through 3 in particular: Sean set this program up, so those pages carry the delta since roughly the spring rather than an introduction to the capability.

---

## Record corrections made in this session

Applied per section 9 of the governing prompt. Original statements preserved.

- `Deliverables/WAM/2026-09-01_Sean_WAM_Program_Update_Prep.md`: dated correction note appended.
- `Deliverables/WAM/2026-09-02_Sean_Deck_Brief.md`: dated correction note appended.
- `06_Stakeholder_Map.md`: checked. The Sean McCloskey entry does not carry the first-update framing, so no correction was required there. A note was added recording the corrected audience position and its source, so the correction is discoverable from the stakeholder record.
- `Briefings/`: checked. No briefing carries the first-update framing.


---

## Superseded 2026-09-10

Rebuilt as `Deliverables/WAM/2026-09-10_WAM_ADM_Evidence_Pack.md`. This version is retained for the decision trail and should not be used.

What changed and why: the eleven use cases derived here from the seven value propositions mixed development-team tasks in with use cases, corrected by Darryl on 2026-09-10 to three user use cases plus one enabler. The four-option ownership frame (status quo, take development, partial, stop) was replaced by the single question Sean actually wants answered, which is whether Digital Products takes over the development resources supplied by the Platforms team in India. Four gaps this version carried as open (what prompted the question, who is in the meeting, the current development arrangement, and whether stopping is the live question) were closed in that session.

What carries forward unchanged: the audience correction, the dependency analysis in Part 3, the three completeness defects and the conflicts in the record, and the finding that most blockers sit outside Digital Products.

Full record: `Deliverables/WAM/2026-09-10_Sean_Deck_Revision_Decisions.md` and `03_Decision_Log.md`, 2026-09-10.
