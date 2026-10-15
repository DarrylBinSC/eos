# WAM roadmap reconciled with the ADM constraints

> Working file for the WAM roadmap reconciliation (week of 2026-10-19, Darryl, Akansh Gangil, David Blondel). Built 2026-10-14 from Akansh's ADM constraints slide (10-14 version, with owners and status) and Nitin Pandey's phased delivery plan and estimation spreadsheet. Also carried as the backup slide "WAM roadmap and constraints" in `Deliverables/Exec_Briefs/2026-10-14_Sean_Portfolio_Deck_v12.pptx`. Internal; constraint rows quote the product owner's slide.

## The finding

Nothing on the roadmap resolves a constraint. Every roadmap item past what is live today builds the consuming side of data the WAM team does not own. The dependency is not only an execution risk; without the data, the feature ships but adoption and scale fall short.

## Mapping

Constraint numbers (C1 to C6) follow the order on Akansh's ADM constraints slide, 2026-10-14 version: C1 trimmed part numbers in EUDM; C2 null shipping and country data; C3 missing license and asset durations; C4 missing serial and MAC data; C5 no parent-child relationships; C6 unidentifiable renewal orders. The same numbers appear on the Sean deck (WAM roadmap diamonds, both backup slides).

| Roadmap item | Timing | Depends on (constraint) | Constraint owner | Status (10-14) | Ask in flight |
|---|---|---|---|---|---|
| Orders beyond configured supplier ID | 2026-11-10 | C1 Trimmed part numbers in EUDM | EUDM/AMS | In analysis | Upstream EUDM enhancement; no date |
| WAM Data Enrichment (Strev upload prep) | 2026-10-30 | C2 Null shipping and country data; ships on the "max ship date" fallback if unfixed | UDM | In analysis | UDM/EUDM root cause fix; no date. Sales Ops and Managed Services should know before release that the fallback is an approximation |
| Asset Grid phase 1: warranty and coverage | 2027-01-04 to 01-08 | C3 Missing license and asset durations | Supplier relationship team (via Jarod Booth) | To coordinate | Supplier data hydration (`05` B1, no evidenced movement since 08-17) |
| Asset Grid phase 1: serial numbers from WMX | 2027-01-04 to 01-08 | C4 Missing serial and MAC data; WMX serial integration pending analysis; WMX refreshes 6 hours after EUDM | WMX/VAS GPOs | In analysis | GPO alignment on the to-be process; Alan Martin's cross-SBU session 10-15 |
| Asset Grid phase 2: 30/60/90-day expiry view | 2027-02-10 to 02-12 | C3 Missing license and asset durations | Supplier relationship team | To coordinate | Same as above; no equivalent executive ask |
| Asset sync ADM to Strev | 2027, reconciled | C4 Serial and MAC data in Wesco systems | WMX/VAS GPOs | In analysis | Sean ask 3 territory via the GPOs |
| Renewal attribution (closed-loop renewal revenue) | 2027, reconciled | C6 Unidentifiable renewal orders; renewal flag at order creation | Dan Totino / DDP GPOs | Not started | Sean ask 3: support with Dan Totino's team |
| Not on the roadmap | | C5 No parent-child relationships (complex builds) | VAS | Not started | VAS API or EUDM data feed; `05` C44 |
| Historical order retrieval | No committed date (withdrawn 10-14; Nitin's sheet still schedules it to 2027-02-16) | Historical EUDM retrieval; none of the six named constraints | DDP/EUDM | | Confirm which is current |

Items with no external dependency: renewal notifications (live), license sync to Strev (running), asset upload by template (Q4), DDP data foundation work itself.

## What follows

1. **January is exposed twice.** Warranty and coverage need durations nobody has committed to supply; serial numbers exist only for what WMX captures today. Say so before the release so a thin January does not read as a delivery failure.
2. **The two Sean asks are the right two** (renewal flag via Dan Totino; serial and MAC via the GPOs). **The durations constraint has no equivalent ask** and touches three roadmap items. Candidate third ask, or a direct request to Jarod Booth's organization through David Blondel.
3. **Reconciliation test for next week:** a feature whose dependency has no owner, no date and a status no better than "in analysis" should slip or be re-scoped to what the data supports. "Scalable and valuable" means the data behind it is coming.
4. **Open conflict to settle with Akansh:** historical data withdrawn versus still scheduled in Nitin's sheet.
