# Connected Asset Tracking: Area Charter
Version 1.0, 2026-09-16. Owner: Darryl Benson. Status: draft for internal use, not yet shared.

## Purpose of this area

Determine whether Wesco should partner for returnable asset tracking, build it, or combine the two, and produce the evidence that makes that a decision rather than a preference. The area exists because leadership declined a vendor subscription on 2026-09-11 and directed an internal build. The charter takes that direction seriously without accepting its premise untested.

## The question, stated precisely

Not "can we build a tracking application." We can, and quickly. The question is which layers of a tracking solution Wesco should own, given a fleet on the order of several thousand returnable assets, and what the five-year total cost and operating burden of each answer looks like.

A tracking solution has five layers. They have very different build economics:

1. **Device.** The tracker itself: radio, GNSS, battery, enclosure, mounting, certification.
2. **Connectivity.** Cellular subscription (LTE-M or NB-IoT), SIM or eSIM lifecycle, coverage and roaming.
3. **Positioning and device services.** Location solving, assistance data, over-the-air firmware and configuration, device diagnostics, command queueing.
4. **Data plane.** Ingest, decode, storage, and the asset and order data model.
5. **Application.** Maps, geozones, alerts, reports, user access.

**The full frame, with current-state evidence and the test question for each layer, is maintained at `03_Architecture/CAT_Five_Layer_Model_2026-09-16.md` and is the standing reference for this area (2026-09-16).**

Layers 4 and 5 are inside this team's current competence and are the cheap part. Layer 1 is a purchase. Layers 2 and 3 are the ones that carry recurring cost, technical risk, and an operating obligation Wesco does not have today. Any comparison that does not separate these five layers will produce a number that cannot be defended.

## Scope

In scope: returnable assets shipped to and recovered from customer and project sites (cable reels, reel stands, and similar returnable items, exact classes to be confirmed); the tracking devices attached to them; the data path from device to a Wesco system of record; association of tracked assets to sales orders; the field operating model that keeps the fleet working.

Out of scope for now: fixed-facility asset management already covered by DDP or ADM; customer-owned asset tracking as a sold service; any external commercialization commitment. The commercial option is kept open, not pursued.

## Intended end state

Internal Wesco capability first, with the commercial option preserved but not assumed. Build decisions should not add cost purely to enable a future external offering, but should avoid choices that foreclose one, specifically: data ownership, tracker portability between platforms, and a data model that is not hard-wired to one internal business unit.

## The options spectrum

These are the candidate answers. The research plan exists to price and de-risk them, not to justify one.

**Option 0: Vendor full stack (the declined baseline).** Sensolus provides device, connectivity, positioning, device management, application, and support for a single per-tracker monthly fee, with hardware replacement included. Retained as the baseline because every other option is measured against it, and because a declined option that later proves cheapest is a finding, not an embarrassment.

**Option 1: Vendor stack, Wesco application.** Sensolus retains layers 1 through 3 and provides data by API or webhook. Wesco builds the application and the asset and order data model on its own platforms. This is the option that most directly satisfies the "do not rent their software" instruction while leaving the hard layers with the party that already operates them at scale. Requires an unbundled price that does not yet exist in writing.

**Option 2: Device vendor plus Wesco platform.** Wesco buys devices from a device manufacturer, uses that manufacturer's device management service, contracts its own connectivity, and builds layers 4 and 5. More control and more moving parts than Option 1, with per-device device-management fees that reduce the apparent saving.

**Option 3: Wesco-owned stack.** Wesco buys devices, owns SIMs and connectivity, points devices at Wesco ingest, and builds device management as well as the application. Lowest recurring vendor cost, highest retained risk. The device manufacturer documentation reviewed for this charter describes this path as not recommended and names what is given up: positioning assistance (which costs accuracy and battery life), firmware and configuration management, device diagnostics, and command queueing, plus the obligation to run a scalable socket service with its own encryption and key management. See the technology baseline.

**Option 4: Hybrid by asset class.** Different economics for different assets. High-value or high-mobility assets on a managed cellular service; high-volume, low-value assets that dwell in known locations on cheaper tags read by gateways at Wesco sites. This is the option most likely to win on cost and the one most likely to be skipped because it is harder to explain.

## Principles for this area

1. Compare like for like. Every option is priced as five-year total cost of ownership across all five layers, including field operations, not as a monthly subscription against an application build estimate.
2. Internal labor is not free. Cash cost and capacity cost are stated separately.
3. Separate confirmed from reported from assumed in every artifact. The source material for this area is a machine transcript with corrupted proper nouns and no verified asset counts.
4. The physical fleet is the hard part. Decisions that look clean in architecture and ugly in a branch yard are wrong decisions.
5. Do not duplicate DDP. Establish what exists before designing around it.
6. Keep the exit. Whatever is chosen, Wesco should be able to leave it: own the data, avoid device lock-in where it costs nothing to avoid.

## Decision gates

Each gate is a point at which the area either advances or stops for evidence. No gate is a status update.

- **G1. Asset baseline.** Confirmed count, classes, sites, current loss and replacement spend, and recovery cycle times for the in-scope fleet. Without this there is no denominator and no benefit case. Blocking for G5.
- **G2. Unbundled commercial terms.** Written pricing from Sensolus for at least: full stack, data-only API access, hardware plus connectivity without application, and hardware purchase outright. Alesea equivalent if the relationship supports it.
- **G3. Technical feasibility.** Technical session held; ingest path, positioning and battery impact of leaving the vendor stack, device management options, and data model confirmed rather than assumed.
- **G4. Pilot evidence recovered.** What the 200-tracker pilot actually measured: read rates, battery, loss, damage, user adoption. This is existing evidence and should not be re-bought.
- **G5. Five-year TCO model** across Options 0 through 4, reviewed with finance, with the capacity cost of internal development stated.
- **G6. Recommendation** to the sponsor, with a build, partner, or hybrid decision and a named owner for the field operating model.

## Governance and decision rights

Not yet established, and this is a gap worth closing early. At least three parties hold a piece of this: supply chain (the business need and the funding), the IoT team (an independent vendor selection already made), and CSS Platforms (the platform and development capability). DDP holds adjacent capability. The charter does not assign decision rights it does not have. The first governance action is to establish who decides, who funds, and where the capability will live if it is built.

## Working files

- `CAT.md`, durable knowledge, area front door.
- `00_Charter/CAT_Research_Plan_2026-09-16.md`, workstreams, questions, owners, sequencing.
- `01_Technology_Research/`, technology baseline and provisioning models.
- `03_Architecture/CAT_Five_Layer_Model_2026-09-16.md`, the standing five layer frame.
- `02_Commercial/`, pricing, vendor terms, TCO model when it exists.
- `03_Architecture/`, reference architecture and data model work.
- `05_Operating_Record/`, research log, risk and dependency log, source index.
