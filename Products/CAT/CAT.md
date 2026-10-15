# Connected Asset Tracking (CAT)
As of: 2026-09-16. Area created this date following the returnable asset tracking discussion (Tom Mitchell, Ramesh Konidala, Dharmayu Purohit, Darryl Benson, Jake). This file is the front door for the area; the phase folders hold working detail and are not duplicated here.

**Naming note.** "CAT" is the internal working name for the area, chosen over "returnable asset tracking" so the scope can extend to other tracked asset classes without a rename. Before any external or customer-facing use, the name needs a second look: CAT is a heavily established brand in industrial equipment, and the collision is avoidable now and expensive later.

**Evidence quality note.** The source transcript is machine-transcribed and several proper nouns are corrupted in it. "Senseless" is Sensolus. "Alicia" and "Alesea" are the same vendor, Alesea. Asset names heard as "Paraspins" and "Insta Reels" were carried as reported. "Insta Reels" is now confirmed: "Insta Reel 48 W" appears as a device tag in the entroCIM Sensolus connector documentation (2026-09-16). "Paraspins" remains unconfirmed. Vendor names, asset class names, and unit counts all need confirmation before any of this material goes into a business case.

## What It Is / Value Proposition

A capability to track returnable physical assets (cable reels, reel stands, and similar returnable items shipped to customer sites and expected back) so that Wesco knows where each unit is, how long it has been there, which sales order it is associated with, and when it should be recovered. The near-term value is operational: reduced asset loss, faster recovery and turn, less unnecessary replacement purchasing, and accurate answers to the question "where is the material for sales order X." The area exists because leadership has asked whether Wesco should build this rather than subscribe to a vendor solution.

Two framings are in play and they are not the same thing. Supply chain is buying an outcome (assets tracked, at a predictable cost). Leadership is questioning an architecture (whether a subscription to a vendor application is still necessary now that application development is faster). The area has to answer the second without losing the first.

## Current State

Reported (from the 2026-09-16 discussion, not independently verified):

- A pilot ran through to early spring 2026 on returnable assets, to compare both systems and their user interfaces. **Design confirmed by Darryl 2026-09-18: 100 Wesco products, each carrying one Alesea and one Sensolus tracker, 200 trackers in total.** The record previously read this as 200 of each (400 trackers); that was a transcript misreading and has been corrected here, in the charter, logs, `03`, and the five layer review deck. Because both trackers rode the same asset, the pilot is a paired, head-to-head comparison under identical conditions, which makes its vendor conclusion stronger than a split-fleet pilot would. The start date is unclear in the transcript and needs confirmation.
- **Only 100 products carried sensors in the pilot** (Darryl, 2026-09-16). Nothing in the deployed estate constrains the technology choice, so Wesco has no radio preference to protect and the selection can be made on fit to the asset classes and sites. The sample is also small: 100 assets per vendor is enough to compare vendors, and thin for estimating a fleet loss rate.
- The pilot conclusion favored Sensolus. Alesea was assessed as roughly four years behind Sensolus in development, even allowing for Alesea's upgrades.
- The IoT team independently evaluated Sensolus against Digital Matter and others and also selected Sensolus.
- Both vendor options price at approximately $5 per tracker per month, which Tom Mitchell sized at roughly $500,000 per year over a three-year agreement. That implies an in-scope fleet of roughly 8,300 assets, which is an inference from his figures and needs confirmation.
- Wesco currently collects data from the Sensolus application, not from the sensors directly. Confirmed by documentation on 2026-09-16: the entroCIM team has built and is syncing a Sensolus connector.
- The business case for a Sensolus deployment was presented to Hemant Porwal on the Friday before the meeting, which is 2026-09-11 if the meeting took place on 2026-09-16 (both dates inferred, not stated). He declined the rental model and directed the team to work with IT on building the capability internally, citing AI-assisted application development. On the morning of the meeting he reported building a GPS tracking app prototype himself in about two minutes and sent Tom a link, which Tom could not open. The prototype has not been seen by anyone in the discussion, so nothing is known about what it does.

Wesco-side capability that is confirmed from Darryl's own knowledge:

- entroCIM runs MQTT ingest in production today, so MQTT over cellular telemetry is not new infrastructure for this team.
- **The entroCIM Sensolus connector is built and syncing** (`ItwSensolus Conn`, current values through an `itwSensolusCur` path, polling the Sensolus cloud API). It learns an Organisations to Assets hierarchy and binds device attributes, subscription, firmware, battery, device tags, last geozones, active alerts, and current process state. Catalog and source documents: `Products/entroCIM/Connectors/entroCIM_Sensolus_Connector_2026-09-16.md`. This means the data plane exists for the partner-data option, and that the integration depends on an active Sensolus subscription. **Correction, Darryl 2026-09-18: the connector is good at pulling data in, and that is all it does. The operations interface does not exist.** Any option beyond Option 0 (the vendor's own application) needs new entroCIM PODs to give the operations team the interface they need, at an effort similar to CDA's FY27 development plan (about 7.0 FTE, eight months), built by the India team at $22/hour and half retained afterwards to maintain and enhance the product (Darryl, 2026-09-21). Layer 5 is therefore a build plus a standing team, not a sunk cost. This is the correction that moves the financial model most: see `Deliverables/CAT/2026-09-18_CAT_Financial_Model.xlsx`.
- Asset Data Manager (ADM), part of the Wesco Asset Management platform, sits on Darryl's team and is connected to the DDP core database, which is the route to sales order association.
- DDP has already built asset tracking capability of its own. What it covers relative to GPS-based tracking of returnable assets is not yet established.

## Technology position

Open, deliberately. The sensor and connectivity landscape is researched in `01_Technology_Research/CAT_Sensor_and_Connectivity_Deep_Dive_2026-09-16.md`: barcode and RFID for read-point custody, Bluetooth tags read by infrastructure Wesco owns, cellular trackers for anything that leaves a Wesco site, LoRaWAN for controlled campuses, satellite for coverage gaps. The likely answer is mixed by asset class rather than uniform, because a tag read by our own gateways and a tracker carrying its own network are not close in cost.

## Commercial Position

**Requesting business unit (Darryl, 2026-09-18):** the request starts as an EES request and may extend to UBS as it matures.

Internal capability first. The immediate consumer is Wesco supply chain, not an external customer. The commercial option is deliberately kept open: if the capability is built on Wesco platforms and proves out internally, it can be evaluated later as a sellable service, with Wesco as customer zero. No external commitment should be made before the internal case is decided.

The cost comparison that decides this is not application cost. The vendor subscription bundles hardware, connectivity, positioning services, device management, support, and hardware replacement. A self-built option replaces a single monthly figure with capital spend on devices, a connectivity contract, a device management plane, and an internal support obligation that does not currently exist. The standing frame for every cost conversation in this area is the five layer model in `03_Architecture/CAT_Five_Layer_Model_2026-09-16.md`: device, connectivity, positioning and device services, data plane, application. Wesco already owns the two layers that are cheap to own and none of the three that are expensive to own. See `01_Technology_Research/CAT_Technology_Baseline_2026-09-16.md` for what each vendor layer contains and what is lost when it is removed.

## Key Dependencies

- Sensolus, for unbundled pricing (data-only API access, hardware-only, hardware plus connectivity) and for the technical session Tom Mitchell is arranging.
- The Sensolus subscription itself, which the completed entroCIM connector now depends on. Ending the subscription stops the integration returning data.
- The IoT team (Dharmayu Purohit and colleagues), which independently selected Sensolus and is the other internal party with a position on this.
- DDP, for sales order data and for reconciling against asset tracking they have already built. Cordelia is the project management contact; the DDP technical contact was to be supplied by Tom.
- ADM and the WAM data model, if ADM is to be the system of record for the asset and tracker registry.
- entroCIM and SkySpark, if the telemetry and analytics layer is built there. Modeling mobile, geolocated assets in a platform built for building points is an open technical question, not a solved one.
- Supply chain operations, for the asset baseline (counts, classes, sites, loss rates) that the business case depends on entirely.

## Managed Services Angle

If Wesco owns the devices rather than renting them, Wesco owns the field operating burden that the vendor currently absorbs: activation, commissioning, battery replacement, damaged and lost device replacement, RMA, and the daily question of why a given asset stopped reporting. This is a managed service whether or not it is named one, and it needs an owner and a funded support model before any self-build option is recommended. The same discipline that applies to external managed services in this portfolio applies here.

## Benefits Realization

Planned, not realized. No benefit should be claimed from the pilot beyond what the pilot measured. The benefit case rests on asset loss avoidance, recovery cycle time, and replacement purchasing avoided, and none of those numbers are in hand yet. The prior WAM benefits reporting history in this portfolio is the reason to hold that line.

## Key People

- **Tom Mitchell**, leading the returnable asset tracking effort and the vendor relationship; arranging the Sensolus technical session and the DDP conversation.
- **Hemant Porwal**, executive sponsor of the build-internally direction; declined the vendor subscription model the Friday before the 2026-09-16 discussion. Name confirmed by Darryl 2026-09-18 as Hemant Porwal (also the VAS Configurator owner in `Reference/Digital_Product_List.md`). Title to be confirmed.
- **Ramesh Konidala**, participant, raised ALM/ADM early in the discussion.
- **Dharmayu Purohit**, IoT team; described the gateway, MQTT over TLS, local control plane, and aggregate view pattern.
- **Jake**, participant, raised the question of what the self-built option actually saves. Last name to be confirmed.
- **Cordelia**, DDP project management contact.
- **Darryl Benson**, brought in for platform, integration, and application development capability; owner of this area.

## Major Risks and Open Decisions

Current status lives in the living documents; this file does not duplicate register state. Registers have not yet been updated for this area.

- **The central decision: partner, hybrid, or standalone.** Open. The options spectrum and the evidence needed to choose between them are in `00_Charter/CAT_Charter_2026-09-16.md`.
- **Risk: the roll-your-own thesis is tested against the wrong cost.** Replicating a user interface is cheap and fast. Replicating device management, positioning assistance, connectivity management, and field support is neither. If the comparison is framed as "our app versus their app," the decision will be made on a number that does not describe the work.
- **Risk: internal development cost treated as free.** Darryl's position in the discussion was that this would be existing staff, not new hires, so the labor is not incremental spend. That is true of cash cost and false of capacity. The same team carries entroCIM, WAM, and CDA commitments, and the opportunity cost needs to be stated in the business case rather than left implicit.
- **Risk: the field operating model is the failure point, not the technology.** Provisioning, commissioning, battery and device replacement, and recovery are where self-managed hardware fleets degrade. See `01_Technology_Research/CAT_Provisioning_Models_2026-09-16.md`.
- **Risk: the vendor device services layer is invisible until it is removed.** The connector reads firmware SHA, configuration update time, battery level, calibrated battery estimation, estimated remaining battery life, last seen alive, location source and location accuracy. Every one of those is produced by a vendor service. In a self-built option nothing produces them unless Wesco builds or buys a device management plane. The connector data point list is the specification of what would have to be replaced.
- **Risk: completed work has created a vendor dependency that an exit decision would break.** The entroCIM connector depends on the Sensolus cloud and an active subscription. This is a normal consequence of integrating, and it should be stated plainly in any option that assumes leaving.
- **Open question: what the pilot actually measured.** 200 trackers on 100 products ran for months. Read rates, battery performance, loss rates, and user behavior from that pilot are the best evidence available and are not yet in this area's record.
- **Open question: DDP overlap.** DDP has built asset tracking. Duplicating it would be a governance failure as much as a technical one.

## History and Lessons

- 2025 late to 2026 early spring: 200-tracker paired pilot (one Alesea and one Sensolus tracker on each of 100 products) on returnable assets. Sensolus preferred on both tracks.
- Friday before 2026-09-16 (2026-09-11 if the meeting date is correct): business case for a Sensolus deployment presented; the subscription model was declined and an internal build directed.
- 2026-09-16: entroCIM Sensolus connector documentation provided by Darryl and filed under `Products/entroCIM/Connectors/`. The connector is built and syncing.
- 2026-09-16: cross-team discussion including CSS Platforms. Next steps agreed were a technical session with Sensolus, a commercial discussion on unbundled pricing, and a conversation with DDP. This area was created the same day.
- 2026-09-17: independent-execution analysis of layers 1-3 delivered (`01_Technology_Research/CAT_Layers_1_3_Independent_Execution_2026-09-17.md`) — this is the research action Darryl accepted in the 09-16 session, substantially complete the next day. Bottom line: independent execution is an assembly-plus-operation, not a build; break-even fleet size is roughly 18,000 assets against an inferred fleet of roughly 8,300, which does not clear it. Gate G2 (whether Sensolus will sell data-only access at roughly $3.50/tracker/month or less) is now the highest-value next action, ahead of further technology work. Ramesh Konidala is separately owed a follow-up call on Sensolus (M365 evidence 2026-09-17); not yet scheduled.
- 2026-09-18: pilot design corrected by Darryl (100 products, one tracker per vendor on each, 200 trackers, not 400). Five-year financial model built (`Deliverables/CAT/2026-09-18_CAT_Financial_Model.xlsx`); it ties to the 09-17 figures and adds a five-year break-even of ~24,700 assets once the build is included.
- 2026-09-21: labor basis set by Darryl (POD development fractional and all India at $22/hour, CDA-scale effort then half retained; layer 1 to 3 engineering split 70% India / 30% US operations at the $94/hour North America rate). Model v3 and both decks revised. At the inferred fleet, five years fully costed: Option 0 $2.49M, Option 1 $2.70M, Option 3 $4.67M. **The decisive number is now the G2 price: below about $3.07 per tracker per month, Option 1 beats the declined subscription with the retained product team counted.**
- 2026-09-21 (later): **Sensolus offered "Sensolus Connect", API access to all data with their front end removed from the cost.** That is Option 1's scope; no price yet. Decision rule at the inferred fleet: Connect wins below $3.07 per tracker per month; at $3.50 it needs about 10,700 counted assets to win. Price-point table in `Deliverables/CAT/2026-09-21_CAT_Financial_Model.xlsx`, Sensitivity section 3. Scope checks outstanding: hardware, connectivity and replacement still included; which layer 3 services survive the API boundary; API limits; term; and what happens to the connector if the subscription lapses.


## EES requirements gathering assigned (added 2026-09-28)

Source: 2027 entroCIM Roadmap Discussion transcript, 2026-09-16. Darryl, direct, to David Blondel: "you're going to have to interview... the EES team on what are their requirements... [and] document all those use cases," before asset-tracking development begins. Tracked as `05` B87, owed to Darryl/product leadership. This is the requirements-gathering step the central partner/hybrid/standalone decision needs and does not yet have. Sensolus connector initial development is reconfirmed complete this window (independent testing and Showcase integration still remain, per the existing record above).
