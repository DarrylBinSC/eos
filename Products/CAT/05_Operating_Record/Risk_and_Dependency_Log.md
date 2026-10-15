# CAT: Risk and Dependency Log
As of: 2026-09-16. Initial entries from area creation. Status column is deliberately sparse; nothing has been worked yet.

## Risks

| ID | Risk | Assessment | Owner | Status |
|---|---|---|---|---|
| R1 | The build decision is made by comparing application cost to a full-stack subscription, producing a saving that does not exist | High likelihood, high impact. Framing risk, and the reason this area exists | Darryl Benson | Open |
| R2 | Internal development capacity treated as free because the staff are already employed | High likelihood, medium impact. Cash cost and capacity cost are different things and the same team carries entroCIM, WAM and CDA commitments | Darryl Benson | Open |
| R3 | Field operating burden (provisioning, batteries, loss, replacement, exceptions) is unowned and unfunded in a self-built option | Medium likelihood, high impact | Unassigned | Open |
| R4 | Leaving the vendor stack degrades positioning accuracy and battery life through loss of assistance services | Medium likelihood, high impact. Vendor-documented for at least one manufacturer; unconfirmed for Sensolus devices | Darryl Benson | Open, W3 |
| R5 | Duplication of asset tracking capability DDP has already built | Medium likelihood, medium impact, plus governance exposure | Tom Mitchell and Darryl Benson | Open |
| R6 | Fleet size assumption (approximately 8,300 assets, inferred from a $500,000 annual figure at $5 per tracker per month) is wrong, invalidating the TCO model | Medium likelihood, high impact | Tom Mitchell | Open, W1 |
| R7 | Device loss and damage rates make owned hardware materially more expensive than the subscription, where replacement is included | Unknown likelihood, high impact. Pilot data should resolve it | Unassigned | Open, W5 |
| R9 | The vendor device services layer is invisible in an application-cost comparison. The connector's data points (firmware, battery estimation, last seen alive, location source and accuracy) are all vendor-produced and would need replacing | High likelihood, high impact. Evidenced directly by the connector documentation, 2026-09-16 | Darryl Benson | Open, W3 |
| R10 | Completed integration work has created a dependency on the Sensolus cloud and an active subscription; an exit decision would break the working connector | Confirmed dependency, medium impact. Not an argument against exiting, an input to costing it | Darryl Benson | Open |
| R16 | The operations interface (new PODs) and the team retained to maintain it are left out of the build comparison. On the 2026-09-21 basis (all India, half retained) the team costs ~$145,000 a year, about 29% of the declined subscription; Option 0 remains the lowest-cost option at the inferred fleet, with Option 1 $215K behind it | High likelihood, high impact. Identified by Darryl 2026-09-18 | Darryl Benson | Open; team basis set 2026-09-21, fleet count (G1) and data price (G2) now decide |
| R8 | Recommendation lands after the FY27 planning cycle has closed on this portfolio, leaving an approved direction with no funding route | Medium likelihood, medium impact | Tom Mitchell and Darryl Benson | Open, W7 |

## Dependencies

| ID | Dependency | On whom | Needed for | Status |
|---|---|---|---|---|
| D1 | Unbundled written pricing, all configurations | Sensolus, via Tom Mitchell | G2, TCO model | **Partially met 2026-09-21: Sensolus Connect offered (API access to all data, front end removed). Price not yet given** |
| D2 | Technical session with vendor engineering | Sensolus, via Tom Mitchell | G3, feasibility | Being scheduled |
| D3 | Results of the 200-tracker pilot | Tom Mitchell and supply chain | G4, loss and battery assumptions | Not started |
| D4 | Asset baseline: counts, classes, sites, loss and replacement spend | Supply chain operations | G1, entire business case | Not started |
| D5 | DDP technical contact and current asset tracking scope | Tom Mitchell to supply contact; Cordelia is the project management contact | Architecture, governance | Not started |
| D6 | ADM and DDP integration path for sales order association | Darryl Benson's team | Architecture | Not started |
| D7 | IoT team alignment, given their independent Sensolus selection | Dharmayu Purohit and IoT leadership | Governance, recommendation credibility | Not started |
| D8 | Decision rights and funding route | Sponsor, via Tom Mitchell | G6 | Not started |
| D9 | Active Sensolus subscription and API access tier, which the entroCIM connector depends on | Sensolus, via Tom Mitchell | Continuity of the working integration; Option 1 feasibility | Confirmed as a dependency 2026-09-16 |
