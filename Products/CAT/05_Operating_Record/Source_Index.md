# CAT: Source Index
As of: 2026-09-16.

## Primary internal sources

| Source | Date | Type | Reliability | Used in |
|---|---|---|---|---|
| Returnable asset tracking discussion, machine transcript (Tom Mitchell, Ramesh Konidala, Dharmayu Purohit, Darryl Benson, Jake) | 2026-09-16 | Meeting transcript, automated, proper nouns corrupted | Directional. Speaker attributions are reliable; names, figures and asset class names need confirmation | CAT.md, charter, research plan |
| Darryl Benson direct knowledge (entroCIM MQTT footprint, ADM ownership, DDP connection) | 2026-09-16 | Direct | Confirmed | CAT.md, research plan |
| entroCIM Sensolus connector documentation, three Confluence page exports (`CON-Sensolus`, `CON-Sensolus Connector Data Points`, `SD-Sensolus Connector`), filed at `Products/entroCIM/Connectors/` | 2026-09-16 | Internal product documentation, provided by Darryl Benson | Confirmed for what the connector exposes; device fleet composition and deployment status not established by it | CAT.md, five layer model, entroCIM connector catalog |

## Public sources

Numbered as cited in `01_Technology_Research/CAT_Technology_Baseline_2026-09-16.md`.

1. Sensolus pricing. https://www.sensolus.com/pricing/
2. Sensolus TRACK 1105 North America announcement. https://www.sensolus.com/knowledge-hub/behind-the-tech/sensolus-unveils-nextgen-industrial-iot-tracking-solution-for-us-canada-and-mexico/
3. Sigfox Partner Network, Sensolus SNT 3 Ultra. https://partners.sigfox.com/products/stickntrack
4. Location Business News on UnaBiz retiring the Sigfox name (paywalled beyond the headline). https://locationbusinessnews.substack.com/p/no-more-sigfox-new-owner-unabiz-shuts
5. Digital Matter, choosing an integration strategy. https://support.digitalmatter.com/choosing-an-integration-strategy
6. Digital Matter, direct to third-party server considerations. https://support.digitalmatter.com/en_US/integration/direct-to-3rd-party-server-integration-considerations
7. Digital Matter, Yabby Edge Cellular. https://www.digitalmatter.com/devices/yabby-edge-cellular/
8. 1NCE pricing. https://www.1nce.com/en-us/1nce-connect/pricing
9. MapTrack retail listing, Yabby Edge. https://www.maptrack.com/store/gps-trackers/yabby-edge-lte-m-nb-iot
10. Corporate Hangar, Alesea. https://corporate-hangar.com/startups/alesea/
11. Sensolus integration documentation. https://doc.sensolus.com/

Sources 12 to 25 were added 2026-09-17 and are listed with their use in `01_Technology_Research/CAT_Layers_1_3_Independent_Execution_2026-09-17.md`. In summary: AT&T NB-IoT exit and carrier positions (12); Digital Matter Device Manager (13); 1NCE published pricing (14); Golioth published pricing (15); AWS IoT Core pricing including Device Location (16); AWS IoT Device Management pricing (17); Nordic nRF Cloud Location Services (18); Nordic acquisition of Memfault (19); Soracom SGP.32 commercial availability (20); cellular IoT certification cost components (21); Particle Tracker One pricing and platform pricing (22); Blues pricing and bundled connectivity (23); Skylo NTN service in the US and Canada (24); embedded firmware engineer compensation reference (25).

## Research and deliverables produced in this area

| File | Date | What it holds |
|---|---|---|
| `01_Technology_Research/CAT_Sensor_and_Connectivity_Deep_Dive_2026-09-16.md` | 2026-09-16 | Sensor and connectivity classes, delivery chain, power behaviour, device management, cost structure. Thirteen public sources cited inline |
| `03_Architecture/CAT_Five_Layer_Model_2026-09-16.md` | 2026-09-16 | The standing five layer frame with a test question per layer |
| `Deliverables/CAT/2026-09-16_CAT_Five_Layer_Model_Review.pptx` | 2026-09-16 | Executive and team review deck, neutral posture, appendix with connector data points, technology comparison, cost benchmarks, glossary and sources |
| `Deliverables/CAT/2026-09-16_Sensolus_Technical_Session_Question_Set.md` | 2026-09-16 | Working agenda for the vendor technical session |
| `Deliverables/CAT/2026-09-17_CAT_Layers_1_3_Independent_Execution.pptx` | 2026-09-17 | Executive companion deck on layers 1 to 3, eleven pages, illustrative cost model shown. Build script at `Deliverables/CAT/build_scripts/` |
| `01_Technology_Research/CAT_Layers_1_3_Independent_Execution_2026-09-17.md` | 2026-09-17 | What layers 1 to 3 contain, what can be bought versus built, who sells each layer, the capability gap, an illustrative five year cost model with break-even and sensitivity, timing, and five candidate risks. Fourteen public sources |

## Known gaps

No Wesco commercial documentation, pilot reporting, asset baseline, or DDP documentation is in this area yet. The connector documentation added 2026-09-16 is the first internal engineering evidence in the area. Every internal figure currently in circulation traces to the 2026-09-16 transcript.
