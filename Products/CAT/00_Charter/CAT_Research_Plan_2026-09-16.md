# Connected Asset Tracking: Research Plan
Version 1.0, 2026-09-16. Owner: Darryl Benson. Horizon: recommendation by end of October 2026.

All dates below are proposed, not agreed. Owners marked "proposed" have not accepted the assignment.

## How this plan is sequenced

Three things gate everything else: how many assets there are, what Sensolus will charge for pieces of its stack rather than all of it, and what is actually lost technically when the vendor stack is unbundled. W1, W2, and W3 run in parallel and immediately. The architecture, operating model, and business case work (W4 through W6) consumes their output. Governance (W7) runs alongside because an unowned recommendation does not get funded.

---

## W1. Asset baseline and problem quantification
Proposed owner: Tom Mitchell, with supply chain operations. Target: 2026-10-07.

The business case has no denominator without this, and the $500,000 per year figure currently in circulation is derived from an assumed fleet size rather than a counted one.

Questions to answer:

1. How many returnable assets are in scope, by class (cable reels, reel stands, others)? What is the confirmed name of each class? The transcript renders two of them as "Paraspins" and "Insta Reels" and neither is confirmed.
2. What is each asset worth, new and replacement?
3. How many are lost, written off, or unrecovered per year, and what does that cost today?
4. What is the current recovery cycle time, and what would a realistic improvement be?
5. Where do these assets go? Wesco sites only, customer sites, project sites, third-party yards? Indoors, outdoors, inside metal structures?
6. What does the business do today when an asset goes missing, and who does it?
7. What is the annual rental or replacement spend that tracking is expected to reduce?

Output: a one-page asset baseline that every later cost and benefit number references.

## W2. Commercial structure and vendor terms
Proposed owner: Tom Mitchell, commercial lead; Darryl Benson, technical input. Target: 2026-10-07.

Questions to answer:

1. What will Sensolus charge for each unbundling: full stack; data-only API access with their devices, connectivity, and device management retained; hardware plus connectivity without the application; hardware purchased outright with no ongoing service?
2. What does the current $5 per tracker per month actually include, line by line, and how does it relate to the published list price of EUR 4 per month for a smart tracker? Volume, term, plan tier, and region all plausibly explain the gap and none of them is confirmed.
3. What is included on hardware failure and loss? The published model includes a lifetime hardware warranty with replacements. What survives in an unbundled deal, and what is the replacement cost if it does not?
4. Who owns the data, and in what form does it leave at contract end?
5. Are devices portable to another platform if Wesco buys them outright, and does the vendor support or block that?
6. What are the term, volume commitment, and exit provisions?
7. Same questions for Alesea where the relationship supports asking, given its cable drum focus is directly relevant to reels.

Output: a written pricing matrix, vendor by option. Nothing in the TCO model may cite a verbal figure.

## W3. Technology and device feasibility
Owner: Darryl Benson, with the IoT team. Target: technical session by 2026-09-30, findings by 2026-10-07.

The baseline research is already filed in `01_Technology_Research/CAT_Technology_Baseline_2026-09-16.md`. The open questions it cannot answer without the vendor are:

1. What protocol do the devices actually speak, to what endpoint, and is that endpoint configurable by the device owner? MQTT over TLS to a Wesco broker is straightforward if the firmware allows it. If the devices speak a proprietary format to a vendor endpoint, direct ingest is not a configuration change.
2. What positioning modes do the devices use (GNSS, Wi-Fi access point scanning, cell tower fallback), and how much of the battery performance depends on vendor-side location solving and assistance data? This is the question most likely to be answered too optimistically. Cloud-assisted positioning is what buys multi-year battery life on this class of device.
3. What is lost in a direct-to-Wesco integration: over-the-air firmware and configuration, device diagnostics, command queueing, positioning assistance, support tier?
4. What is the expected report rate and battery life for the actual use case, and what is the battery replacement or device replacement interval?
5. What network coverage assumptions apply at the sites in W1 question 5, including inside buildings and steel structures?
6. If Wesco owns connectivity, what is the SIM or eSIM lifecycle, and who manages activation, suspension, and roaming?
7. What certification, safety, and mounting constraints apply to attaching devices to these asset classes?

**Update 2026-09-16: the entroCIM Sensolus connector is built and syncing** (`Products/entroCIM/Connectors/entroCIM_Sensolus_Connector_2026-09-16.md`). That closes part of W4 before it started and sharpens W3: the data plane exists against the vendor API, so the remaining technical unknowns are all in layers 1 to 3.

## W4. Architecture and platform fit
Owner: Darryl Benson. Target: draft 2026-10-14.

1. Where does telemetry land: the existing entroCIM MQTT infrastructure, or a separate ingest path? What does the existing MQTT footprint actually support in volume and message shape?
2. Can mobile, geolocated assets be modeled properly in SkySpark and Haystack, which are built for building points? This is an open technical question, not a settled one, and the answer shapes whether entroCIM is the right home or merely an available one.
3. What is the system of record for the asset and tracker registry? ADM is the strong candidate, sits on this team, and is connected to DDP.
4. How does sales order association work, and at what point in the process is the binding created? Binding at pick or pack is more reliable than binding at delivery.
5. What has DDP already built, and what would be duplicated? This has to be established before the architecture is drawn, not after.
6. What does the application layer actually need to do on day one, as opposed to what the vendor application does today? The vendor feature set is not automatically the requirement.

## W5. Field operating model
Owner: Darryl Benson, with supply chain operations. Target: draft 2026-10-14.

Detail is in `01_Technology_Research/CAT_Provisioning_Models_2026-09-16.md`. The decisions this workstream must close:

1. Provisioning: central at Wesco, vendor drop-ship pre-provisioned, or in the field. This is the question Darryl raised in the meeting and it has a defensible answer already (see the provisioning file); it needs confirming against how the branches actually work.
2. Commissioning: who physically attaches the tracker, at what point in the flow, and how is the tracker-to-asset binding captured?
3. What happens on return: rebind, battery check, reuse, or retire?
4. Who owns the fleet day to day, including battery replacement, damaged devices, and the daily exception list of assets that stopped reporting?
5. What is the expected annual device loss rate? This single number moves self-built economics more than any other, because in the vendor model replacement is included and in a self-built model it is a purchase order.

## W6. Business case and total cost of ownership
Proposed owner: Darryl Benson with finance support. Target: draft 2026-10-21, gated on W1, W2, W3.

1. Five-year TCO for Options 0 through 4, with capex and opex separated, and device refresh and loss modeled explicitly.
2. Internal development and ongoing support effort, stated in both cash terms (largely existing staff) and capacity terms (what those people are not doing instead). Both belong in the document; only one of them is zero.
3. Sensitivity analysis on the three variables most likely to be wrong: fleet size, device loss rate, and unbundled vendor pricing.
4. Break-even volume: below what fleet size does building lose, and above what fleet size does it win?
5. Benefit case built on W1 evidence only. No benefit claimed that the pilot did not measure or the baseline does not support.

## W7. Governance and decision rights
Proposed owner: Tom Mitchell and Darryl Benson jointly. Target: 2026-09-30.

1. Who owns this capability if it is built, and who funds it?
2. How do supply chain, the IoT team, CSS Platforms, and DDP divide the work, and who arbitrates?
3. What is the decision forum and the date the recommendation is heard?
4. What is the FY27 AOP implication if the recommendation lands after the planning cycle has closed on this portfolio?

---

## Immediate next actions

| # | Action | Proposed owner | By |
|---|---|---|---|
| 1 | Sensolus technical session scheduled, agenda per the question set in `Deliverables/CAT/` | Tom Mitchell | 2026-09-30 |
| 2 | Unbundled pricing requested in writing | Tom Mitchell | 2026-09-30 |
| 3 | DDP contact identified and conversation held on existing asset tracking | Tom Mitchell to supply contact; Darryl Benson to lead | 2026-09-30 |
| 4 | Pilot results recovered from the 200-tracker pilot | Tom Mitchell | 2026-09-30 |
| 5 | Asset baseline started | Supply chain operations, proposed | 2026-10-07 |
| 6 | Governance question tabled with the sponsor | Tom Mitchell and Darryl Benson | 2026-09-30 |

## What would change this plan

- If the fleet is materially smaller than roughly 8,300 assets, the self-built options weaken quickly because the fixed cost of a device management and support capability spreads across fewer units.
- If Sensolus declines to unbundle, the spectrum collapses to Option 0 or Option 3 and the decision becomes sharper and riskier.
- If DDP already covers a meaningful part of this, the build scope shrinks and the governance question becomes the main event.
