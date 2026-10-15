# Portfolio Status Slide — entroCIM and Wesco Asset Manager
Cells for the two empty columns. July reporting cycle (as-of 2026-07-31, June financials). Milestone horizon: through 2026-09-30. Paste-ready.

---

## Row 1: IOT Platforms — entroCIM (PM: Chris Gazdic)

### Upcoming Milestones

- Quest-to-Azure migration complete — Sept 1
- SkySpark 4 platform update, connector and application migration — Q3
- Q3 release: entroCIM PM, Graphic Builder Animation, Connector Diagram — Oct 5
- Integrations: ServiceNow Field Service, Sensolus — Q3
- Knowledge Base migration — Q3 (dependent on Wesco enterprise initiative)

### Key Accomplishments and Next steps

Accomplishments

- Release 3.1.12.13 shipped July 20 on quarterly cadence, DCOE approved
- Delivered Bookmark app, redesigned Collection app, Connector Upload app, Tiles/Gridboard enhancements
- Production release controls instituted: version tagging, dual reviewer, JIRA-linked commits, documented test evidence
- Docker containerization progressing under approved security governance

Next steps

- Complete Azure cutover and retire the legacy environment
- Confirm Q3 release scope and date; resolve ServiceNow dev-environment access to unblock connector work

---

## Row 2: Platforms — Wesco Asset Manager (PM: Chris Gazdic)

### Upcoming Milestones

- Notification to Sales Rep suite release, US and Canada — Aug 10
- Milestone and ExacQ supplier data insertion into ADM — Aug 10
- Broader marketing launch — September (revised from August)
- Default end-user and bulk end-user editing — Q3
- Asset data capture, historical migration, order capture beyond supplier id — Oct 8 onward

### Key Accomplishments and Next steps

Accomplishments

- DDP/EUDM enterprise data integration live July 3
- License data now syncs from multiple source systems into a single view
- Notification to Sales Rep suite completed UAT testing
- Two post-go-live defects closed: EUDM integration bug, ADM UI performance at volume

Next steps

- Release the notification suite and close the license activation defect
- Confirm the asset source for complex builds before Q4 asset-tracking scope is committed
- Recalibrate the roadmap and customer messaging to the revised data-capability estimates

---

## Trimmed alternates (if the cells overflow)

**entroCIM, Upcoming Milestones — 3 lines**

- Quest-to-Azure migration complete — Sept 1
- SkySpark 4 platform update — Q3
- Q3 release, Oct 5; ServiceNow and Sensolus integrations, Q3

**WAM, Upcoming Milestones — 3 lines**

- Notification to Sales Rep suite, US and Canada — Aug 10
- Broader marketing launch — September
- Asset data capture and order capture beyond supplier id — Oct 8 onward

---

## Speaker notes

**entroCIM.** July was an execution quarter and the release landed on its committed date, which matters because customers plan around the quarterly cadence. The more durable change is process, not scope: the DCOE review produced permanent production controls (tagging, two reviewers, JIRA-linked commits) that apply to every future release, not just this one. The Sept 1 Azure completion removes the platform's largest remaining infrastructure dependency; the 2025 delays behind it (leadership restructuring and a lead-engineer vacancy) are resolved. Q3 is dependency-heavier than Q2. Two of the five milestones sit outside the team: the Knowledge Base migration waits on a Wesco enterprise initiative, and the ServiceNow connector is currently blocked because the development-environment access request was declined. The Q3 release date is deliberately shown as TBD; scope is known, the date is not committed.

**WAM.** The July 3 DDP/EUDM go-live is an enterprise data connection, not a resolution of the underlying MDM, supplier, and classification work; state it as a capability milestone. The August 10 notification release is the first time a governed renewal signal reaches Sales Operations, and the Milestone/ExacQ supplier data lands the same day on purpose, because the alert is only as credible as the end date behind it. Expectations here are set at Senior Director level in Sales Operations.

The important separation to hold in the room: the near-term notification rollout and the underlying data-capability roadmap are on different horizons. Revised estimates from Nitin Pandey and Akansh Gangil (08-06) put asset data capture, historical data migration, and order capture beyond supplier id between Oct 8 2026 and Feb 3 2027. Do not let the August notification release imply the data capabilities behind it land on the same timeline. This has not yet been recalibrated in the WAM narrative used since 07-17, including the Lisa Orton brief.

Two more things to be ready for verbally: the marketing launch moved from August to September, and the Q4 asset-tracking scope depends on an unresolved question about whether complex-build asset data comes from VAS or WMX. If any quarter slips it is Q4, and the causes sit outside the development team.

---

## Evidence and exclusions (not for the slide)

**Deliberately not stated, and why**

1. **Automated three-times-daily DDP/EUDM sync.** The 08-05 Backlog Deep Dive deck marks this Q2 complete. The 07-16 and 07-20 record states the license-order feed is manually triggered daily due to clustering issues, with an explicit instruction that the automation is not production-grade and must be stated honestly in executive framing. Both cannot be true. Unresolved with Akansh Gangil. It is the kind of claim a reviewer tests, so it stays off the slide until confirmed.
2. **"Coverage beyond Core and Anixter part numbers" / "beyond Wesco part numbers."** Parked as not well understood and believed to rest on a misunderstanding, and it sits adjacent to two different items (the Q4 configured-supplier-id scope and the 15-character vendor part number field limit). The slide uses the safe formulation: license data syncs from multiple source systems into a single view.
3. **Cancelled-order removal as an Aug 10 deliverable.** Cancelled sales orders are being removed manually ahead of the release; the automation is not built. Listed nowhere as complete.
4. **Q4 roadmap items generally.** Outside the 60 to 90 day horizon you set.
5. **entroCIM Q3 release number.** No release identifier exists in the record. The date does: **2026-10-05**, from the entroCIM Backlog Deep Dive 07-28, carried in the `04` release-communication-handoff row. Date shown, identifier omitted.
6. **Correction applied 08-10.** The first draft carried "full license purchase history by customer, coverage beyond configured supplier id — begins Q3," built from `WAM_Roadmap.md`, which predates the 08-06 Requirement Estimation document from Nitin Pandey and Akansh Gangil. That document revises four major data capabilities to **2026-10-08 through 2027-02-03**. "Order capture beyond supplier id" is the same item as the roadmap's Q4 "coverage beyond configured supplier id," and "asset data capture" is the same item as Q4 "asset tracking from EUDM and WMX." The Q3 bullet was wrong and is replaced with "Oct 8 onward." `WAM_Roadmap.md` has been updated to carry the superseding dates so the stale roadmap does not seed this error again.
7. **The DCOE as the driver of the new release controls.** Factually correct (Ron instituted them in response to DCOE pressure — Daily Stand Up 07-21, `09` and `03`), but deliberately not on the slide. The accomplishments cell already credits DCOE approval of the release, which reads as validation. Stating that the controls exist because of DCOE pressure invites a question about what the evidence gap was, against an open High watch row (`04`, "Release compliance / DCOE evidence gap") whose risk is inconsistent adoption. Ready verbally; name it on the slide only if the DCOE (Balachandar Murali) is in the audience.

**Dates that are targets, not commitments** — Aug 10 (WAM notification suite, named on a slide but described in the record as a target), Sept 1 (Azure), September (marketing launch, reported rather than confirmed). If any of these is challenged in the room, the honest answer is "planned date, not yet delivered."

**Confirmed as of the July cycle** — 3.1.12.13 shipped and DCOE approved (field note 07-23, Impact Ledger 07-22); Ron Snyder's forward production controls (07-27); DDP/EUDM live 07-03; two post-go-live defects closed (08-05 deck); notification suite UAT complete (08-05 deck, Sprint 26Q3 Sprint 2).

**One structural note.** You chose delivery and roadmap content only for these cells, so entroCIM's red Benefits block and WAM's yellow Schedule and Scope are explained by the Health Comment column alone. That works for entroCIM, where the comment names the cost right-sizing action. It is thinner for WAM: the comment says what changed (marketing delay, data challenges) but not what is being done about either, and neither the milestone list nor the next steps addresses the marketing launch as a recovery item. Be ready to answer that verbally, or add one line to the WAM next steps.
