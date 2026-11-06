# FRB CSC BIM Teams Note

Audience: FRB Cash Services Review group (Sarah, Leanne, Valli, Chad, Syed, Ron, David, Nate). Draft for Darryl to send.

---

Team, a recap of what we learned today on the FRB CSC BIM requirement, and what it changes. The working draft of our response is in the FRB folder (FRB CSC BIM Response Draft); please review it against the points below.

**What the customer actually wants (Nate's call with Raj)**
- The Fed wants the Smart Building Platform to house BIM data, and eventually 3D graphics, for holistic asset management. This is not about BAS operation or visualization.
- Not a deal breaker if we cannot do it today. They want a price and a roughly two-year roadmap for what it takes.
- Nate believes we are still the frontrunner.

**What the revised B37 says, by section**
- The two modeling sentences are struck (model to LOD, clash detection, federated model; Revit 2026 at LOD 400 and 500). We never had that capability and it is gone.
- Three obligations remain or were added: participate in the BIM process per the BIM Implementation Plan; provide COBie data for the equipment we furnish; receive the trades' Revit 2026 models and COBie data and incorporate them into the platform per the specifications and C1.1.
- 3D is a written requirement, not just Raj's comment: spec 25 00 00, 2.03 H (3D model navigation), reached through C1.1 and the new B37 sentence. Our 2.03 D deviation is still pending Owner review. We keep the deviation and offer the roadmap as the way it gets resolved.

**What the Turner BIM documents add (05A Requirements, 05B BIM Lead scope, 05C HLW file agreement). This one changes what we do.**
- 05A binds all Trade Contractors and includes BIM costs by default (3.1). It does not exclude anyone; our exclusion from the modeling sections rests only on the struck B37 text. Our response states the exclusion by section number and asks Turner to confirm it in writing.
- The Owner's systems of record are named: TRIRIGA for the asset register (14.4.5) and Kahua for the turnover model and final COBie workbook (14.3.3). entroCIM is neither. Our role is the operational layer: live data from the connected building, with a reference copy of the handover model and asset data joined to it by the FRBNY Asset ID (14.7.4). Nothing flows from entroCIM back to the model or the register.
- IFC is already a required turnover format (14.3.1), so our roadmap builds on IFC and COBie, never on reading native Revit.
- COBie recurs. Workbooks are due at Design, Construction and Handover at Turner's data drops. Our COBie deliverable for furnished equipment is a workbook at each drop, per the Responsibility Matrix, and has to be priced that way.
- Turner holds sole rights to use the models (3.6), and model data falls under FRBNY security protocols (3.7). We ask written permission to hold a reference copy in the platform.
- 05C is the HLW file agreement we must sign to receive any drawings: project-only use, no release, indemnity. Legal reviews before signature, and we cannot use project files to build or test the roadmap.
- 05B is Turner's BIM Lead scope. It is not ours; Sarah to confirm we are not being asked for it.

**Schedule (September 2026 update)**
- Final leveling ends tomorrow, 11/3. Award execution 12/1 to 12/7. Submittals 12/8 to 3/10/27.
- Smart Building start-up 12/8/28. Commissioning 1/9/29 to 3/5/29. Substantial Completion 2/28/29. The LOD 500 as-built and final COBie land about 3/30/29.
- So the handover data we would consume does not exist until Q1 2029. Our roadmap is stated against those milestones: data repository before start-up, 3D before commissioning. Both sit inside our 2028 roadmap with margin.
- Our response needs to reach Turner this week.

**How we are structuring the offer**
- Stage 1, in the bid: COBie mapping at closeout, 2D floor plans, links to the turnover record, and a reconciliation report of where the commissioned building differs from the model.
- Stage 2, roadmap: a BIM data repository in entroCIM (IFC and COBie snapshot, Asset ID link table, versioning, API read access). Reload from a revised model only on request, as a service.
- Stage 3, roadmap: 3D viewing in the entroCIM UI, from the stored IFC, synced by Asset ID. An embedded self-hosted viewer, not a 3D engine of our own.
- Commercially: a development charge per stage as Add Alternates, with scope and acceptance agreed at each stage start and Stage 3 contingent on Stage 2; an annual advanced-feature license once released, outside base entroCIM licensing; and project services to load and configure FRB's data at each release. We retain the IP.
- entroCIM's truth is the installed, connected, commissioned device. Model changes do not propagate into the platform and we will not say they do.

**Actions**
- Ron: feasibility of the COBie-to-Haystack mapping, rough effort and timing for Stage 2 (IFC metadata and COBie repository, link table, API) and Stage 3 (embedded viewer), and whether the platform can hold model files today or only link to them. This gates the price lines.
- Chad: confirm the delivery team can produce a COBie workbook for our furnished equipment at the data drops, the floor-plan method in the 10/29 reply, and the deployment model for model data at FRB (Owner-hosted or air-gapped) with Ron.
- Sarah: obtain the BIM Execution Plan, the COBie Responsibility Matrix, the Asset Information Requirements and FRBNY Exhibit H; pull the exact text of 25 00 00 2.03 D, G and H; confirm we are not being asked for BIM Lead services; ask Turner whether its subcontract terms attach schedule remedies to Add Alternate development work.
- Leanne and Valli: price lines for Stage 1, the Stage 2 and 3 development charges, the feature license, the stage services, and the H3 treatment of the feature license, once Ron's estimate is in.
- Brandon: the HLW file agreement, 05A 3.6 to 3.9, and the IP wording for the development charge.
- Nate: confirm with Raj that TRIRIGA is the FM system the COBie data targets, and that the Owner accepts IFC as the model exchange alongside native Revit.
- David and I: the feature license price and where this sits in the entroCIM price list, and the roadmap dates we put in writing.

Given the schedule, let's aim to have the response to Sarah by Thursday. I am happy to walk through the draft on a call tomorrow if that is faster.
