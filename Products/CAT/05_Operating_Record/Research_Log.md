# CAT: Research Log

Chronological record of what was researched, by whom, and what it established. Findings live in the topic files; this log is the trail.

## 2026-09-16: Area created, vendor and technology baseline compiled
By: Darryl Benson (Cowork session).

- Source material: machine transcript of the 2026-09-16 returnable asset tracking discussion. Proper nouns corrupted; Sensolus appears as "Senseless," Alesea as "Alicia" and "Alesea."
- Public-source research on Sensolus pricing and device specifications, Digital Matter integration strategies, Alesea origins, and cellular IoT connectivity cost floors. Filed in `01_Technology_Research/CAT_Technology_Baseline_2026-09-16.md` with numbered sources.
- Principal finding: the vendor subscription bundles device, connectivity, positioning services, device management, support, and hardware replacement. The application layer, which is the layer the internal build thesis targets, is the least expensive layer to replicate.
- Second finding: device manufacturer documentation states that sending device data directly to a third-party server forfeits positioning assistance, over-the-air firmware management, diagnostics, and command queueing, with stated impact on positioning accuracy and battery life. This is the technical core of the partner-versus-standalone decision.
- Provisioning analysis filed separately; recommendation is central provisioning with field commissioning only.

Not yet researched: Wesco's negotiated vendor terms, the 200-tracker pilot results, DDP's existing asset tracking capability, the asset baseline.

## 2026-09-16 (second entry): entroCIM Sensolus connector documentation received and cataloged
By: Darryl Benson (Cowork session), from three Confluence page exports he provided.

- Filed the source PDFs at `Products/entroCIM/Connectors/` and wrote the durable catalog, `entroCIM_Sensolus_Connector_2026-09-16.md`. entroCIM owns that fact; CAT references it rather than duplicating it.
- Principal finding: the connector is a platform-to-application integration against the Sensolus cloud API, not a device integration. Layers 4 and 5 of the five layer model are therefore already delivered for this use case, and layers 1 to 3 remain entirely with the vendor.
- Second finding: the connector's own data point list is an inventory of what the vendor device services layer produces (firmware SHA, configuration update time, battery level, calibrated battery estimation, estimated remaining battery life, last seen alive, location source, location accuracy). It doubles as the replacement specification for any self-built option.
- Third finding: `sigfoxActivationStatus` in the attribute set indicates Sigfox lineage in the fleet or API surface, while the North America product line is marketed on NB-IoT and LTE-M. Which radio the Wesco fleet uses is now an explicit open question in W3.
- Naming correction: "Insta Reel 48 W" appears as a device tag, confirming the asset class the transcript rendered as "Insta Reels."
- The five layer model was promoted from a section of the charter to a standing area artifact at `03_Architecture/CAT_Five_Layer_Model_2026-09-16.md`, at Darryl's direction, to be applied to every option, estimate, and vendor conversation in this area.

## 2026-09-16 (third entry): sensor and connectivity deep dive, and the five layer review deck
By: Darryl Benson (Cowork session).

- **New fact from Darryl:** only 100 products carried sensors in the pilot, so there is no installed base to protect and no radio technology preference. Filed in `CAT.md` and reflected in the deck.
- Sensor and connectivity research completed and filed at `01_Technology_Research/CAT_Sensor_and_Connectivity_Deep_Dive_2026-09-16.md`, with thirteen public sources. Covers barcode, passive RFID, Bluetooth, cellular LPWAN, LoRaWAN and satellite; what each delivers and how; the delivery chain from asset to application; power behaviour; device management; and cost structure by layer.
- Three findings that carry into the build versus buy review. Reporting frequency is the largest driver of battery life. A failed upload can consume up to twenty times the power of a successful one, which makes coverage quality a battery question. Devices that solve position in the cloud are published at five to ten times the battery life of device-only GPS, which means vendor data sheet battery figures do not travel with a device taken off the vendor cloud.
- Conclusion carried forward: the build versus buy question is a layer 3 question (positioning and device services). Layers 4 and 5 are built, layer 1 is a purchase in every option, and layer 2 is near free.
- Deck built and delivered: `Deliverables/CAT/2026-09-16_CAT_Five_Layer_Model_Review.pptx`. Twelve executive pages plus a six page appendix, on the Wesco master inherited from the CDA exec brief, neutral posture with no option recommended. Narrative is in the speaker notes per the communication standard.

## 2026-09-17: Layers 1 to 3 independent execution deep dive
By: Darryl Benson (Cowork session).

- Question asked: what infrastructure, skills and cost would be required for Wesco to execute layers 1, 2 and 3 without a partner, who plays in that space, what is the gap, and what is the timing. Filed at `01_Technology_Research/CAT_Layers_1_3_Independent_Execution_2026-09-17.md` with fourteen new public sources, numbered 12 to 25 in the source index.
- **Principal finding: independent execution is an assembly plus an operation, not a build.** Positioning, device management and observability are all purchasable as metered infrastructure from at least four categories of supplier. Nothing at layers 1 to 3 needs to be engineered from first principles, and custom hardware should be rejected unless a requirement forces it.
- **Second finding, and the one that should drive the conversation: on an illustrative five year model the answer turns on whether internal labor is counted.** At the inferred fleet of 8,300 assets the self-assembled stack is approximately $1.41M if labor is treated as free and approximately $4.62M if sustaining engineering and fleet operations are costed. The declined subscription sits between them at approximately $2.49M.
- **Third finding: break-even is approximately 18,000 assets**, falling to approximately 8,800 if sustaining engineering is excluded and only the operations staff are counted. The inferred fleet is below both. G1 is therefore not a denominator for the model, it is the decision.
- **Fourth finding: the fastest route to an answer is commercial.** If Sensolus prices data access with layers 1 to 3 retained at roughly $3.50 per tracker per month or less, Option 1 wins on cost, risk and time and the architecture question closes. G2 is the highest value next action in the area.
- Market timing established: AT&T has exited NB-IoT and migrated to LTE-M, which settles the North American radio question; SGP.32 reached commercial availability in July 2026, which makes owning connectivity viable without carrier lock-in; and the device services market has consolidated into purchasable infrastructure, illustrated by Nordic acquiring Memfault in June 2025. The components of an independent stack are more available than they were, which strengthens the case for owning the capability and weakens any case for building the components.
- Gap analysis produced by capability rather than by technology. The permanent gap is the fleet operations function: unowned, unfunded, three to six months to stand up, and the longest pole in any self-build schedule.
- Five candidate risks raised for the risk log, R11 to R15, covering funding the assembly as an application project, hardware lock-in reintroduced through device services, the SkySpark and Haystack mobile asset modelling question, fleet operations approved but unstaffed, and connectivity modelled at the prepaid rate.

Still not researched: Wesco negotiated terms, pilot results, DDP capability, asset baseline. Unchanged from 2026-09-16 and now blocking more than it was.

## 2026-09-17 (second entry): data path and protocol addendum
By: Darryl Benson (Cowork session).

- Question raised: how LTE-M data reaches Wesco and over what protocol. Answered and filed as a dated addendum to `03_Architecture/CAT_Five_Layer_Model_2026-09-16.md` rather than as an edit, so the original frame stands.
- **Correction worth carrying into the vendor session: LTE-M is a bearer, not a protocol.** The application protocol on top of it is a separate choice that sets battery life, whether a device can be commanded, and how much of layer 3 arrives with it.
- **Confirmed: no device traffic reaches Wesco today.** Device sessions terminate in the Sensolus cloud and the connector polls their REST API over HTTPS. Data freshness in entroCIM is set by a polling interval and vendor processing, not by the device report rate.
- Three direct ingest patterns compared: UDP with proprietary binary payload, CoAP over DTLS carrying LwM2M, and MQTT over TLS. LwM2M is the only one that brings device management with the protocol. MQTT is the least new Wesco infrastructure and the highest power cost at the device. A protocol gateway that terminates CoAP or UDP and republishes to MQTT internally resolves most of the tension.
- Network path flagged as a separate decision belonging in the layer 2 contract: public internet with TLS, private APN with IPsec, or carrier cloud interconnect into a Wesco VPC. Expensive to retrofit.
- **Gating question added for the vendor session:** whether the device endpoint is configurable by the owner and whether the payload specification is released. If the endpoint is fixed to vendor infrastructure, every direct ingest option is unavailable regardless of price. It should be asked early rather than in section 4 order.

## 2026-09-17 (third entry): layers 1 to 3 companion deck built
By: Darryl Benson (Cowork session).

- `Deliverables/CAT/2026-09-17_CAT_Layers_1_3_Independent_Execution.pptx`. Eleven pages, standalone companion to the five layer review, built on the same Wesco master. Audience is the executive sponsor and Tom Mitchell. Narrative in the speaker notes per the communication standard, no subtitles, no dates assigned.
- Sequence: where this lands, partner or supplier, what the three layers contain, who sells what, the gap, what it costs, where break-even sits, how long it takes, what the market timing says, what decides it.
- The cost model is shown and labelled illustrative on every page that carries it. The five year spread and the break-even figure are presented as a model to be argued with, not as a business case.
- Build script filed alongside at `Deliverables/CAT/build_scripts/build_cat_layers_1_3_deck.py` so the deck can be regenerated after the G1 and G2 numbers land.
- Deck posture: still no option recommended. It names two asks, the unbundled price and the counted fleet, and one gating technical question for the vendor session.


## 2026-09-18: pilot design corrected; five-year financial model built
By: Darryl Benson (Cowork session).

- **Correction from Darryl:** the pilot was 100 Wesco products, each carrying one Alesea and one Sensolus tracker, 200 trackers in total. The record had read the transcript as 200 of each (400). Corrected in `CAT.md`, the charter, the research plan, the risk log (D3), the three technology research files, `03_Decision_Log.md`, and the five layer review deck (slide 2 card and notes, slide 11). The layers 1-3 deck carries no pilot reference and was not changed. Implication: the pilot is a paired, same-asset comparison, which strengthens the vendor conclusion; at 100 assets per vendor it is thin evidence for a fleet loss rate, which matters at G4.
- Financial model built: `Deliverables/CAT/2026-09-18_CAT_Financial_Model.xlsx`, build script in `Deliverables/CAT/build_scripts/`. Reproduces every 09-17 figure at default inputs (Reconciliation tab). Illustrative, not a business case.
- **Two findings not in the 09-17 analysis.** (1) The ~18,000 break-even is a run-rate figure that excludes the initial build; on a five-year basis including the $700k build and Year 1 fleet purchase, break-even is ~24,700 assets. (2) With only fleet operations counted and all engineering treated as free, self-assembly still costs ~$121k more than the declined subscription over five years. Option 1 price ceilings: $2.83/tracker/month beats the labor-free case, $5.24 beats ops-counted, $9.28 beats fully costed; the $3.50 G2 threshold sits between the first two.

## 2026-09-18 (second entry): application layer corrected; financial model v2
By: Darryl Benson (Cowork session).

- **Correction from Darryl:** the entroCIM Sensolus connector pulls data in and nothing more. Every option beyond Option 0 needs new PODs for the operations team's interface, at an effort similar to CDA's FY27 development plan, with the same team retained to maintain and enhance the product. Filed in `CAT.md` and as a dated correction in `03_Architecture/CAT_Five_Layer_Model_2026-09-16.md`. Earlier statements that layers 4 and 5 were built, in both decks and in the 09-16 and 09-17 research, are wrong for layer 5.
- Benchmark used (from `AOP_FY27/Change_Logs/2026-08-18_CDA_FY27_AOP_Change_Log.md`): 6.75 India FTE at $22/hour plus 0.25 North America FTE at $94/hour, 1,880 hours, eight-month build, $45,000 other IT. Annual team cost $323,360.
- Copilot reviewed v1 independently. Adopted: Year 0 build period with time-zero NPV; constant-dollar labelling with a real discount rate; device and SIM refresh driven by life and term; input validation and sheet protection; break-evens rounded up and stated on run-rate, five-year and NPV bases; a twelve-driver sensitivity table and cumulative lines for every option; source document column on Inputs. Not adopted: named ranges (not needed at this size); residual value (disclosed as conservative against Option 3 instead).
- v1 renamed `SUPERSEDED_2026-09-18_CAT_Financial_Model_v1.xlsx`. v2 is the live `2026-09-18_CAT_Financial_Model.xlsx`; the Reconciliation tab proves it reproduces 09-17 with the product team switched off and walks the Option 3 figure from $4.62M to $6.67M.
- **Result at 8,300 assets, fully costed, five years:** Option 0 $2.49M, Option 1 $3.62M, Option 3 $6.67M. Option 0 is lowest. Option 1 beats Option 0 only below ~$1.23/tracker/month (or ~20,900 assets at $3.50). Option 3 break-even ~40,400 assets on five-year cash, ~58,000 on NPV.
- **The largest open lever is internal:** whether the PODs team is dedicated to CAT or shared across CDA and entroCIM. Now logged as R16.
- Both decks now carry superseded content: the "layers 4 and 5 built" framing (09-16 slides 3 and 6; 09-17 slides 4 and 9) and the 09-17 cost and break-even pages (slides 2, 7, 8). Not yet revised.

## 2026-09-21: labor basis set by Darryl; model v3 and both decks revised
By: Darryl Benson (Cowork session).

- **Three rulings from Darryl.** (1) POD development is fractional for CAT and all India at $22/hour: CDA-scale effort (7.0 FTE, eight months) through the build, then half the team retained to maintain and enhance. (2) Layer 1 to 3 engineering splits 70% India / 30% US operations team. (3) The US share is charged at the $94/hour North America AOP rate. All three are now inputs in the model rather than assumptions.
- Model v3 is live at `Deliverables/CAT/2026-09-21_CAT_Financial_Model.xlsx`; v2 renamed `SUPERSEDED_2026-09-21_...`. Blended layer 1 to 3 engineering cost is $81,968 per FTE per year, against the $175,000 US figure used on 09-17. Reconciliation still ties to the 09-17 published figures when the team is removed and engineering is set back to $175,000.
- **Result at 8,300 assets, five years, fully costed:** Option 0 $2.49M, Option 1 $2.70M, Option 3 $4.67M. Option 0 remains lowest, but Option 1 is now within $215K of it rather than $1.13M, because the product team costs $144,760 a year rather than $323,360.
- **The G2 threshold that matters is now $3.07 per tracker per month**, the price below which Option 1 beats the declined subscription with the retained team counted. The 09-17 deck's $3.50 was close by luck, not by construction. Option 1 also breaks even with Option 0 at about 10,700 assets at the $3.50 placeholder, which is within reach of a counted fleet in a way that Option 3's 25,100 is not.
- Option 3 break-even: about 18,500 assets run-rate, 25,100 on five-year cash including the build, 36,100 on NPV.
- Both decks revised and republished. The five layer review (2026-09-16, same filename, corrections in place) no longer says layers 4 and 5 are built: slide 3's band and layer label and slide 6's subtitle, closing line and notes now state that layer 4 is built and layer 5 needs new PODs. The layers 1 to 3 deck is reissued as `2026-09-21_CAT_Layers_1_3_Independent_Execution.pptx` (09-17 version superseded) with the cost page rebuilt as Option 0 $2.5M / Option 1 $2.7M / Option 3 $4.7M, break-even at 25,000, the price ask at $3.00, the timeline row changed from "live now" to eight months of POD work, and the layer 4 and 5 statement corrected. Build scripts for both artifacts are in `Deliverables/CAT/build_scripts/`.
- Still open and now the sharpest question for the sponsor conversation: Option 1 and Option 0 are close enough at the inferred fleet that G1 and G2 decide between them. Neither has landed.

## 2026-09-21 (second entry): Sensolus Connect offered
By: Darryl Benson (Cowork session), from his call with Sensolus.

- **Sensolus offered "Sensolus Connect": API access to all of the data, with their front-end application removed from the cost.** That is Option 1's scope exactly, and it is the first movement on G2 since the area was created. **No price was given, so G2 is half satisfied: scope yes, number no.**
- Model updated to v3.1: the `p1` input is relabelled as the Sensolus Connect price (status "Offered, price pending"), and the Sensitivity sheet carries a price-point table from $1.00 to $5.00 so the answer can be read off the moment the number lands. v3 renamed `SUPERSEDED_2026-09-21_CAT_Financial_Model_v3.xlsx`.
- **Decision rule at the inferred fleet of 8,300:** Connect beats the declined full stack below **$3.07** per tracker per month. At $3.00 it saves $34K over five years; at $3.50 it costs $215K more; at $4.00, $464K more. Above the ceiling it still wins on a large enough fleet: $3.50 needs 10,700 assets, $4.00 needs 16,000, $4.50 needs 32,100, and at $5.00 it never catches the full stack.
- Every price point in that table carries the POD build, the retained product team and any bridge months, so it compares like for like with the subscription.
- **Scope questions to settle before the number means anything:** whether Connect still includes hardware, connectivity and device replacement (if not, device capex returns and this stops being Option 1); which layer 3 services survive the API boundary (positioning assistance, firmware, diagnostics, battery estimation); whether the API tier carries call or volume limits; contract term and what happens to the working entroCIM connector if the subscription lapses (R10); and whether the price is per tracker per month on the same basis as the $5 full stack.
