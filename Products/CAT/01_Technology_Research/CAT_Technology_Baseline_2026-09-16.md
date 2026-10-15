# Connected Asset Tracking: Technology and Vendor Baseline
As of: 2026-09-16. Compiled by Darryl Benson from public vendor sources. Every figure below is a published or list figure, not a Wesco quote. Sources are listed at the end and numbered inline.

## Why this file exists

The build-or-partner question was framed in the 2026-09-16 discussion as an application question. It is not. This file establishes what the vendor layers contain, so the comparison can be made against the real content of the subscription rather than against its user interface.

## What the vendor subscription actually buys

Sensolus publishes a tracking-as-a-service model at EUR 4 per month for a smart tracker and EUR 1 per month for a location tag, described as all-in with no upfront hardware investment. The published inclusions are hardware, platform and software, connectivity, support, and a lifetime hardware warranty with replacements. Plans are tiered by feature set, with enterprise security (single sign-on, audit logs) and custom branding as paid add-ons [1].

Two observations follow, and both matter for the business case.

First, the Wesco figure discussed in the meeting is approximately USD 5 per tracker per month, against a published list of EUR 4. Volume, contract term, plan tier, and region can all explain the difference. None of them is confirmed, and the difference should be resolved before either number is used in a model.

Second, hardware replacement is inside that monthly fee. In any self-built option, a lost or broken tracker is a purchase, not a warranty claim. At fleet scale this is not a rounding item, and it is the line most often left out of roll-your-own comparisons.

## Devices and connectivity

The Sensolus North America tracker (TRACK 1105) uses NB-IoT and LTE-M, with dual-network operation described as providing redundancy when one network degrades. Published battery life is up to seven years, with IP68 and IP69k ratings and embedded condition sensors [2]. Sensolus devices historically also used the Sigfox 0G network [3]; the Sigfox brand has since been retired by its owner UnaBiz [4], which is a reason to confirm the connectivity roadmap of any device generation Wesco might buy rather than assume it.

LTE-M and NB-IoT are the relevant radio technologies for this use case in North America, because the assets leave Wesco control and arrive at sites where Wesco owns no infrastructure. The alternatives have narrower fits:

- LoRaWAN gives long range at low power but requires gateways within range of the asset. That works where assets dwell in known yards and fails where they sit on a customer site.
- Bluetooth tags are the cheapest per asset and require a gateway or a phone in proximity. They suit dense, known locations, which is why they appear in Option 4 of the charter rather than as a standalone answer.
- Wi-Fi access point scanning and cell tower identification serve as positioning fallbacks indoors rather than as primary connectivity.

## The layer that is easy to underestimate: positioning and device services

Digital Matter, a device manufacturer independently evaluated by the Wesco IoT team, publishes its integration options and their tradeoffs. Three paths are offered: data routed through their device management cloud (recommended), data through their telematics platform with webhooks, and devices sending directly to a third-party server. That third path, which is exactly the "collect straight from the sensors" option discussed in the meeting, is documented as not recommended, described as maximum effort, and carries specific losses [5][6]:

- Direct integration is incompatible with their location engine for GNSS scan lookups, Wi-Fi access point lookups, and cell identifier timing. Assistance data stops updating, which the vendor states degrades positioning performance and reduces battery life.
- Over-the-air firmware and configuration management is no longer automatic.
- Device diagnostics, debug messaging, and proactive monitoring are lost.
- Asynchronous message queueing for remote device commands is lost.
- The integrator must build a scalable socket service and implement encryption, authentication, and device key management itself.
- Support drops to non-priority.

The battery point deserves emphasis because it is counterintuitive. On this class of device, multi-year battery life is achieved partly by not computing position on the device. Digital Matter's Yabby Edge, for example, uses cloud-based location solving through their location engine, and publishes battery life of up to ten years at daily updates, three years on movement-based updates, and two years at hourly updates [7]. Take away the cloud assistance and the physics change, not just the feature list. This is the single most important technical fact to confirm with Sensolus, because if their battery performance depends on their cloud, then "just send the data to our MQTT broker" costs battery life, positioning accuracy, or both.

The internal position taken in the meeting, that MQTT over LTE would be inexpensive for this team because entroCIM already runs MQTT, is correct as far as it goes. Wesco can receive the messages. What Wesco would additionally have to build or buy is the layer above the messages: device management, assistance, and diagnostics.

## Cost floors for the self-built path

These are public benchmarks that establish orders of magnitude for the TCO model. They are not quotes and must not be used as Wesco pricing.

- **Connectivity.** 1NCE publishes a one-time USD 14 payment for ten years of IoT connectivity, including 500 MB of data and 250 SMS, across 2G, 3G, 4G, LTE-M and NB-IoT in 170 countries, with no monthly recurring charge [8]. For a low-duty-cycle tracker, raw connectivity is therefore on the order of USD 0.12 per device per month. Raw connectivity is not the cost driver.
- **Hardware.** A single-unit retail listing for a Digital Matter Yabby Edge LTE-M tracker is USD 175 [9]. Volume pricing through a distribution channel will be materially lower, and Wesco is unusually well positioned to buy hardware well. At an assumed 8,300 units, even a favorable unit price puts device capital spend in the high hundreds of thousands, one time, before connectivity, platform, and labor.
- **Device management.** Charged per device by the manufacturer on the recommended path, which erodes part of the saving that motivates leaving the vendor platform.

The shape of the answer, before any modeling: connectivity is nearly free, hardware is a capital purchase Wesco can negotiate well, the application is cheap for this team to build, and the expensive, risky parts are device services and the field operating burden. That is why Option 1 in the charter (vendor keeps the hardware layers, Wesco builds the application) is the option most likely to satisfy the sponsor's instruction at the lowest retained risk, and why Option 3 needs the most scrutiny before anyone commits to it.

## The other vendor in the pilot

Alesea originated with Prysmian, a cable manufacturer, as an internal tool for cable drum management before being offered externally. It comprises a device, a web platform, and an app, and tracks drum location, cable consumption per drum, impacts, and installation quality. Approximately 60,000 drums across 90 customers are reported [10]. Its cable drum specificity is directly relevant to reels, which is worth weighing against the pilot conclusion that it trails Sensolus in development.

## What this file cannot tell you

- Wesco's actual negotiated pricing with either vendor, in any configuration.
- Whether Sensolus firmware permits a customer-configured endpoint.
- How much of Sensolus battery performance depends on their cloud services.
- Real-world read rates and battery performance on Wesco assets. The 200-tracker pilot holds that evidence and it should be recovered rather than re-purchased.

## Sources

1. Sensolus, Pricing. https://www.sensolus.com/pricing/
2. Sensolus, TRACK 1105 IoT asset tracker for North America. https://www.sensolus.com/knowledge-hub/behind-the-tech/sensolus-unveils-nextgen-industrial-iot-tracking-solution-for-us-canada-and-mexico/
3. Sigfox Partner Network, Sensolus tracker SNT 3 Ultra. https://partners.sigfox.com/products/stickntrack
4. Location Business News, "No More Sigfox: New Owner UnaBiz Shuts Down Name." https://locationbusinessnews.substack.com/p/no-more-sigfox-new-owner-unabiz-shuts (headline and description only; full article paywalled, treat as directional)
5. Digital Matter, Choosing an Integration Strategy. https://support.digitalmatter.com/choosing-an-integration-strategy
6. Digital Matter, Direct to 3rd Party Server Integration, Considerations. https://support.digitalmatter.com/en_US/integration/direct-to-3rd-party-server-integration-considerations
7. Digital Matter, Yabby Edge Cellular. https://www.digitalmatter.com/devices/yabby-edge-cellular/
8. 1NCE, IoT SIM plan and pricing. https://www.1nce.com/en-us/1nce-connect/pricing
9. MapTrack, Yabby Edge LTE-M/NB-IoT listing. https://www.maptrack.com/store/gps-trackers/yabby-edge-lte-m-nb-iot
10. Corporate Hangar, Alesea. https://corporate-hangar.com/startups/alesea/
11. Sensolus integration documentation index (pull API, push API, webhooks including MQTT). https://doc.sensolus.com/
