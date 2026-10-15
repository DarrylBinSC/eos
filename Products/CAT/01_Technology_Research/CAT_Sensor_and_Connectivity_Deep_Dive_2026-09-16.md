# Connected Asset Tracking: Sensor and Connectivity Deep Dive
As of: 2026-09-16. Owner: Darryl Benson. Purpose: the technical foundation for the build versus buy review. Figures are public benchmarks and vendor-published values, not Wesco quotes, and are labeled as such. This document opens the Build vs Buy workstream (W3 and W6 in the research plan).

## Starting position

Wesco has no radio technology preference to protect. The pilot attached sensors to 100 products (Darryl, 2026-09-16), which is small enough that no installed base constrains the choice. That is a genuine advantage and it should be used deliberately: the technology can be selected on fit to the asset classes and the sites, rather than inherited from a pilot.

The question this document serves: is it worth investing in the infrastructure and building the additional elements needed to deliver on par with Sensolus, or should Wesco buy devices and API connectivity only? Map every answer onto the five layer model in `03_Architecture/CAT_Five_Layer_Model_2026-09-16.md`.

## The short version

Three things decide the technology, in this order.

1. **Where the asset goes.** An asset that leaves Wesco control and sits at an unknown customer site needs a device that carries its own wide-area connectivity. An asset that cycles between known Wesco locations can be read by infrastructure Wesco owns, at a fraction of the cost per asset.
2. **How often you need to know.** Reporting frequency is the single largest driver of battery life and therefore of field labor. Daily is cheap. Hourly is expensive. Continuous is a different product.
3. **What you do with the answer.** Continuous location supports recovery and utilization analysis. Read-point events (this asset passed this gate at this time) support cycle time and custody, cost far less, and answer most returnable asset questions.

Most mature returnable asset programs end up hybrid rather than uniform, because the economics of a tracker on a high-value asset and a tag on a commodity asset are not close.

## Class by class

### Barcode and QR

What it delivers: identity, at a moment, when someone scans it.
How: a person with a phone or scanner. No radio in the asset.
Infrastructure: none beyond the scanning app and a registry.
Power and life: none required; life is the label's physical durability.
Cost shape: pennies per label, all cost in labor and process compliance.
Fit: the identity backbone under everything else. Every tracked asset should carry a durable machine-readable identifier regardless of what else is attached, because commissioning, audits, and exception handling all depend on it. This is a prerequisite, not an alternative.

### Passive RFID

What it delivers: automatic identity capture at fixed read points, with no human scan.
How: fixed readers at dock doors, yard gates, and production exits, plus handhelds for audits and exceptions. Ruggedized RTI labels for metal and plastic; one current industrial label is published as readable at up to 21 metres with roughly five-year durability [1].
Infrastructure: readers and portals at every place you want to see the asset. That is the whole economic question with RFID.
Power and life: no battery in the tag.
Cost shape: low per asset, meaningful per read point.
Fit: strong where assets pass through a controlled gate, which covers Wesco branches, distribution centers, and yards. It gives custody and cycle time, not continuous location, and it sees nothing at a customer site unless the customer has readers, which they will not.

### Bluetooth tags

What it delivers: proximity-based location, typically 1 to 10 metres indoors, refreshed whenever something hears the tag [2].
How: the tag advertises an identifier every second or two. A fixed gateway, a handheld, or a phone hears it and relays the sighting.
Infrastructure: gateways for reliable coverage, roughly one per 200 to 600 square metres indoors depending on obstructions, connected by Ethernet, Wi-Fi, or cellular [2]. Consumer variants piggyback on phone networks, which is a coverage model Wesco cannot depend on for an operational process.
Power and life: two to seven years on coin or industrial cells [2].
Cost shape: published market benchmarks are roughly 10 to 40 US dollars per tag with 2 to 10 US dollars per month of service [2], against roughly 50 to 200 US dollars and 10 to 30 US dollars per month for cellular GPS trackers [2]. Treat these as consumer and small-business market ranges, not as enterprise volume pricing. Note that Sensolus publishes a location tag at EUR 1 per month against EUR 4 for a smart tracker [3], which is the same economic gradient inside one vendor's catalog.
Fit: excellent inside Wesco sites and yards, useless once the asset leaves unless someone with a receiver walks past it. The natural pairing is Bluetooth tags on high-volume assets plus gateways at Wesco locations, with cellular trackers reserved for assets that travel.

### Cellular LPWAN trackers (LTE-M and NB-IoT)

What it delivers: wide-area location and condition reporting anywhere the carrier reaches, with no Wesco infrastructure at the far end. This is the class Sensolus, Digital Matter, and the rest of the tracker market sell into.
How: the device wakes on a schedule or on movement, acquires a position, and sends a small payload over the carrier network. LTE-M supports mobility and lower latency at up to about 1 Mbps; NB-IoT is lower power and better suited to stationary assets, with higher latency and weaker handover behavior [4].
Infrastructure: none owned by Wesco. A connectivity contract and SIM or eSIM management.
Power and life: multi-year, entirely dependent on configuration. See the power section below.
Cost shape: device is capital, connectivity is small, device services are where the recurring value sits. Public connectivity benchmarks put low-duty-cycle IoT data near 0.12 US dollars per device per month [5].
Fit: the default for anything that leaves a Wesco site. The important nuance for the build question is that the radio is the easy part; what makes these devices work for years is the service layer behind them.

### LoRaWAN

What it delivers: long range at very low power, up to roughly 2 to 15 kilometres depending on terrain, at low data rates [4].
How: the device transmits to a gateway; the gateway forwards to a network server that de-duplicates, decrypts, and hands the payload to an application.
Infrastructure: Wesco would own gateways and either run or subscribe to a network server, or rely on public coverage that is not dependable across US industrial sites [6][7].
Power and life: very long, comparable to or better than NB-IoT.
Cost shape: capital in gateways, near zero recurring per device [7]. That inversion is the attraction.
Fit: good for Wesco-controlled campuses and yards where the same assets dwell. Poor for assets at customer sites. It solves the same problem Bluetooth gateways solve, at longer range and higher gateway cost.

### Satellite (NTN)

What it delivers: coverage where terrestrial networks do not reach.
How: standards-based narrowband IoT over non-terrestrial networks is now commercially offered through carrier and module partnerships, including modules combining NTN and embedded GNSS [8].
Cost shape: satellite subscription on top of, or instead of, terrestrial.
Fit: not a primary answer for Wesco returnable assets, which move through populated commercial and industrial geography. Worth knowing it exists so it is not mistaken for a gap in the analysis.

## What a tracker actually delivers

Raw telemetry, typically: position with a source and an accuracy estimate; motion and activity; shock or impact; temperature and humidity where the device carries those sensors; orientation or tilt; and device health, meaning battery level, estimated remaining life, firmware version, and last contact time.

Derived information, which is what the business actually uses: current location and last known address; geozone entry and exit; dwell time at a location; distance travelled; idle versus active status; and exception alerts. The entroCIM Sensolus connector already carries this full shape, including geozones, alerts, and process state, which is worth noting because it means the target data model is not speculative.

The gap between the two lists is a meaningful part of what a vendor platform does.

## How the data gets from the asset to the application

```
asset  ->  radio  ->  network (carrier, or Wesco gateway plus network server)
       ->  decode and device services (position solving, assistance data, firmware, diagnostics)
       ->  API or broker  ->  Wesco data plane (entroCIM, ADM)  ->  application
```

Wesco today joins this chain at the API step. The Sensolus connector polls the vendor cloud and binds the results into entroCIM. Everything left of that point is bought, not built.

Two protocol facts matter for any direct-ingest option. Cellular IoT devices commonly speak CoAP over UDP or a vendor-proprietary binary format rather than MQTT, so an existing MQTT broker is not automatically the ingest path. And where a device does support a configurable endpoint, whether it can be pointed at a Wesco endpoint at all is a firmware question that only the device vendor can answer.

## Power, which is a commercial issue rather than a technical one

Battery life on these devices is not a specification, it is an outcome of configuration and architecture. Three published findings, all from a device manufacturer's own engineering material [9]:

- **Reporting frequency is the largest single driver.** One device family is published at up to ten years on daily updates, dropping to roughly three years on movement-based updates and two years on hourly updates [10].
- **A failed upload can consume up to twenty times the power of a successful one** [9]. Poor coverage does not just cost data, it costs battery, which means coverage quality at the actual sites is a battery question as well as a visibility question.
- **Where the position is calculated changes the battery maths.** GNSS on the device is the most power-hungry method; Wi-Fi access point scanning uses considerably less; cell identifier positioning uses least and is least precise. Devices that offload position solving to a cloud service are published as achieving five to ten times the battery life of GPS-only equivalents [9].

The last point is the one that matters most to the build decision. If Wesco takes devices away from the vendor cloud that solves their positions, the battery performance quoted in the vendor's data sheet does not travel with the device. That is not a feature loss, it is a change to the physics of the deployment, and it shows up as field labor eighteen months later.

Mounting matters too: a device buried in metal acquires more slowly and burns more power doing it [9], which is directly relevant to trackers attached to steel reels and reel stands.

## Device management, the layer nobody costs

Device management is what keeps a fleet of several thousand battery-powered radios working after the pilot ends. It covers bootstrap and registration, configuration, firmware updates over the air, diagnostics and connectivity monitoring, and queued commands to devices that are asleep when you want them.

There is an open standard for it. LwM2M runs over CoAP, typically on UDP, and defines objects for device information, connectivity monitoring, and firmware update [11][12]. Using it means running an LwM2M server, or paying someone to run one [11].

So a self-built option does not avoid this layer, it relocates it. Either Wesco runs a device management platform, or Wesco pays a device manufacturer per device to run theirs, or Wesco operates a fleet with no remote firmware, no configuration control, and no health visibility, which is an option only until the first firmware defect.

The concrete measure of what this layer produces is already in Wesco's hands: the data points the entroCIM connector reads from Sensolus (firmware SHA, last firmware update, last configuration update, battery level, calibrated battery estimation, estimated remaining life, last seen alive, location source, location accuracy) are all device management outputs.

## Cost structure, by layer

Benchmarks only, for shaping the model. Every line needs a Wesco quote before it is used in a business case.

| Layer | What is bought | Public benchmark | Notes |
|---|---|---|---|
| Device | Tracker or tag | Bluetooth tags roughly 10 to 40 USD; cellular trackers roughly 50 to 200 USD at retail [2] | Wesco volume pricing should be materially better; single-unit retail listings run higher [13] |
| Connectivity | Cellular data | About 0.12 USD per device per month at low duty cycle, from a published 14 USD, ten-year, 500 MB plan [5] | Not the cost driver |
| Positioning and device services | Location solving, assistance, firmware, diagnostics | Charged per device by manufacturers on their managed path; not separately priced in the Sensolus bundle | The layer that carries the risk |
| Data plane | Ingest and model | Built, in entroCIM | Sunk |
| Application | Views, alerts, workflow | Partly built | Cheapest remaining work |
| Vendor bundle, for comparison | All of the above | Sensolus publishes EUR 4 per month for a smart tracker, EUR 1 for a location tag, all in, including hardware, connectivity, support and lifetime hardware warranty with replacements [3] | Wesco's discussed figure is about 5 USD per tracker per month; the gap needs reconciling |

## What this means for build versus buy

Layer 1, device: buy, in every option. Nobody is proposing Wesco make hardware.

Layer 2, connectivity: genuinely optional. Owning it is cheap and adds SIM lifecycle work. It is not where the saving is, and it is not where the risk is.

Layer 3, positioning and device services: this is the decision. Owning it means running or buying a device management platform, accepting the positioning and battery consequences of leaving the vendor's location engine, and staffing a fleet operation. Buying it means a per-device fee and a dependency.

Layers 4 and 5, data plane and application: already Wesco's, and already partly delivered.

The honest framing for the review is therefore narrow: the build versus buy question is really a question about layer 3, and it should be argued there rather than across the whole stack.

## What this research cannot answer

- Which radio technology the deployed Sensolus devices actually use, and whether their endpoint is configurable.
- Sensolus unbundled pricing for devices, connectivity, and API access separately.
- Wesco volume pricing on any device.
- Real coverage quality at the sites these assets actually reach.
- The asset baseline: counts, classes, values, loss rates. Nothing here can be turned into a business case without it.
- What the 200-tracker pilot measured, which is existing evidence that should not be re-purchased.

## Sources

1. atlasRFIDstore, RFID for returnable containers. https://www.atlasrfidstore.com/rfid-insider/rfid-for-returnable-containers-eliminating-shrink-in-supply-chains/
2. Airpinpoint, BLE tracking guide, costs and infrastructure. https://airpinpoint.com/blog/ble-tracking-guide
3. Sensolus pricing. https://www.sensolus.com/pricing/
4. Spenza, IoT connectivity comparison (LTE-M, NB-IoT, LoRaWAN, LEO NTN). https://spenza.com/iot/iot-connectivity-comparison/
5. 1NCE pricing. https://www.1nce.com/en-us/1nce-connect/pricing
6. LoRa Alliance and LORIOT, private LoRaWAN network server. https://loriot.io/enterprise-private-server.html
7. Robustel, LoRaWAN versus cellular decision guide. https://robustel.com/lorawan-vs-cellular-a-2026-decision-guide-for-industrial-iot-architecture/
8. Skylo newsroom, NB-IoT over NTN partnerships and modules. https://www.skylo.tech/newsroom/u-blox-launches-first-satellite-iot-ntn-cellular-module-with-embedded-gnss-solving-remote-connectivity-challenges
9. Digital Matter, what actually impacts battery life in GPS trackers. https://www.digitalmatter.com/blog/what-actually-impacts-battery-life-in-gps-trackers
10. Digital Matter, Yabby Edge Cellular. https://www.digitalmatter.com/devices/yabby-edge-cellular/
11. IoT For All, IoT device management using LwM2M. https://www.iotforall.com/iot-device-management-using-lwm2m
12. AVSystem IoT Developer Zone, firmware updates over the air. https://iotdevzone.avsystem.com/docs/academy/module5/
13. MapTrack retail listing, Yabby Edge. https://www.maptrack.com/store/gps-trackers/yabby-edge-lte-m-nb-iot
