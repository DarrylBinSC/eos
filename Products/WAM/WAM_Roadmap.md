# WAM / ADM 2026 Roadmap

> **As of: 2026-08-05** — transcribed from the WAM Backlog Deep Dive deck (`Products/WAM/WAM_Backlog_Deep_Dive_2026-08-05.pdf`, 9 slides), presented 2026-08-06. **This supersedes the 2026-07-15 version** of this file, which held Akansh Gangil's track-based backlog slide (Track 1 ADM↔Strev Integration, Track 2 ADM for Sales Enablement). That version is preserved in the Prior Version section at the bottom; it is not deleted, and its track detail is still the finer-grained view of the same work.
>
> Refresh when the deck is reissued. Flag in briefings if untouched 30+ days.
>
> **Provenance note:** the deck answers the 07-30 leadership ask for a quarterly roadmap with named milestones rather than continued problem definition. Treat it as the current plan of record for WAM, superseding roadmap statements made from the July slide.

## Roadmap narrative

Stated arc: **from license visibility → proactive renewal alerts → complete coverage view.** Each quarter increases what Sales Operations can act on without account-by-account research. The value-chain slide (slide 2) is unchanged from the 07-15 executive review version and remains the canonical framing: source data → ADM (ingest, normalize, enrich, distribute) → commercial path (sales triggers and notifications) and service path (Strev experience layer per customer) → customer and commercial value.

## Q1 2026 — COMPLETE

**Theme: licenses visible in Strev**

- Sync a customer's licenses on demand via the ADM UI
- Buy price and supplier profiles included
- Edit and export licenses in ADM
- End user attribute from IAP for each license record

## Q2 2026 — COMPLETE

**Theme: coverage beyond Core and Anixter part numbers**

- Licenses captured from other ERPs, not just Wesco part numbers
- Sync runs automatically from DDP/EUDM, no manual refresh, three times a day
- Global attributes and clean taxonomies in MDM

> **Open question, parked by Darryl 2026-08-05 for a later session.** The "beyond Core and Anixter part numbers / not just Wesco part numbers" framing is not well understood and is believed to rest on a misunderstanding. It sits close to two other items and must not be conflated with either: the Q4 "coverage beyond configured supplier id" item, and the vendor part-number field limit (15 characters) that was dropping orders between EUDM and ADM. Three adjacent concepts, one shared vocabulary. **Do not use "beyond Wesco part numbers" in any outbound material until this is resolved with Akansh.** The safe business-level statement in the interim, used in the 08-05 Lisa Orton brief, is that license data now syncs from multiple source systems into a single view. Resolve before the FY27 submission if the license coverage claim is going to appear in the business case.

> **Discrepancy flagged 2026-08-05, requires Darryl's confirmation.** The deck marks the automated three-times-daily DDP/EUDM sync as Q2 complete. The record from 2026-07-16 and 2026-07-20 (`03` WAM MVP1 gate entry; `04` MVP1 row) states the EUDM license-order feed is **manually triggered daily** due to clustering issues, with an explicit instruction that automation "is not production-grade yet and must be stated honestly in exec framing." Both cannot be current. Either the automation landed between 07-20 and 08-05 and the record is stale, or the slide overstates completion. This matters because the claim has already been used in outbound material (Lisa Orton brief, 08-05) and it is the kind of claim a reviewer tests. **Not resolved in this update; carried as an open question.**

## Q3 2026 — IN PROGRESS

**Theme: reps see what's expiring**

- Expiry alerts routed to the owning rep
- End dates and end user data "we can trust", sourced from suppliers (Milestone and ExacQ)
- ADM enhancements: custom view, setting up end user per project id

**Named release date: 2026-08-10** for the Notification to Sales Rep suite and the Milestone/ExacQ data insertion (Sprint 26Q3 Sprint 3, slide 6).

## Q4 2026 — PLANNED

> **Dates superseded 2026-08-06 (Requirement Estimation: Asset Data Capture, Historical Data Migration & Order Capture Beyond Supplier ID — Nitin Pandey / Akansh Gangil).** New delivery estimates for four major data capabilities span **2026-10-08 through 2027-02-03**. This directly affects the Q4 items below: "coverage beyond configured supplier id" is the Order Capture Beyond Supplier ID item, and "asset tracking from EUDM and WMX" is the Asset Data Capture item. Neither is a Q3 or early-Q4 delivery on current estimates; the band extends into Q1 2027.
>
> **Use rule.** Do not present the Q4 theme as a 2026 completion, and do not let the near-term notification-suite narrative imply the underlying data capabilities land on the same horizon (explicit instruction in `03`, 08-06 update). The 07-17 WAM narrative reset has not been recalibrated to these dates, and the pre-recalibration framing was already used once in outbound material (Lisa Orton brief, 08-05). Entries in `03` (MVP1 gate) and `04` (WAM/ADM data integrity row) carry the full framing.

**Theme: one complete coverage view**

- Full purchase history by customer/supplier in ADM for configured products
- Coverage beyond configured supplier id
- Removing cancelled license orders automatically
- Asset tracking from EUDM and WMX

> **Dependency not shown on the slide (added 2026-08-05):** the Q4 "asset tracking from EUDM and WMX" item rests on the complex-build/WMX capability question tracked in `04` and Register A1. The standing record is that WMX lacks serial/MAC/complex-build capability "through at least 2028" absent action, and the 08-04 session produced only a working position (VAS for complex finished goods, WMX for simplified products) before rescheduling again. The roadmap item is not wrong, but it is not self-contained. Have the dependency answer ready before Q4 scope is committed externally.

## Current view for Sean, 2026-10-14 (from the Akansh/Nitin thread; the August quarters above are stale)

- **Shipping now:** renewal notifications to reps (live since 08-17); license sync to Strev; WAM Data Enrichment 10-30; orders beyond the configured supplier ID 11-10.
- **Early 2027, asset functionality for Managed Services** (asset upload, Asset Grid): phase 1 (2027-01-04 to 01-08): asset records from EUDM orders with warranty and coverage, WMX serial numbers, asset grid with search and export; phase 2 (2027-02-10 to 02-12): end-user verification, 30/60/90-day expiry view, audit and edit. Asset upload by template lands in Q4 2026. Delivery-team estimate (Nitin Pandey, 10-14); held as targets until the roadmap reconciliation.
- **Rest of 2027:** reconciled next week on the scalable, valuable test: DDP data foundation (EUDM on Azure Databricks); asset sync to Strev once serial and MAC data is in Wesco systems; renewal attribution once orders carry a renewal flag; historical order retrieval, no date.
- Slide: `Deliverables/Exec_Briefs/2026-10-14_Sean_Portfolio_Deck_v8.pptx`.

## Sprint status at 2026-08-05 (deck slides 4-6)

**Sprint 26Q3 Sprint 2, completed:** testing of the Notification to Sales Rep suite in UAT; post-EUDM-integration bug; ADM UI slowness under large data volume.

**Sprint 26Q3 Sprint 2, ongoing:** analytics on notifications sent to sales rep; removal of cancelled sales orders from ADM; automatic identification of cancelled line license records; milestone data insertion for 2026 Q1; license activation issues; custom view in ADM UI; estimating new functionality.

**Sprint 26Q3 Sprint 3 objectives:** release the Notification to Sales Rep suite and insert Milestone/EXACQ data (both dated 08-10); find cancelled line items from EUDM; then start coverage beyond configured supplier id, full license purchase history for customer, default end customers per project/customer id, bulk edit of end customers, and an email-processing bug.

**Team capacity (slide 7):** 15 named contributors, 8 backend/data engineering, 2 UI, 5 QA.

## Executive read (Claude, 2026-08-05)

- The roadmap is now outcome-themed rather than task-listed, which is a material improvement for executive use: each quarter states what a user can do that they could not do before. It is usable in front of Dirk Naylor or Sales Operations leadership as-is.
- Q3 is the commercially significant quarter. It is the first time a governed renewal signal reaches Sales Operations, and the supplier-sourced end dates sit in the same quarter precisely because the alert is only as credible as the date behind it. That pairing is good product judgment and worth saying out loud when the roadmap is presented.
- Two of the three previously flagged defects (post-EUDM integration, ADM UI performance) are marked complete. License activation remains open, consistent with the null/missing SO date root cause in `04`.
- The 08-10 date is now on a slide rather than a verbal "not committing" from Akansh (07-28). That is a firmer position but still a target, not a confirmed release. Do not restate it as committed until the release lands.
- Q4 carries the heaviest external dependency load (supplier participation, MDM attribute adoption, the WMX/VAS asset source question). If any quarter slips, this is the one, and the causes will sit outside the development team.

---

## Prior version — 2026-07-15 (Akansh Gangil's track-based backlog slide)

> Retained for continuity. Superseded by the 08-05 deck above as the roadmap of record, but the track detail remains the finer-grained view of the same programme of work. Slide was cropped: three items marked *(truncated)*.

### Track 1: ADM <> Strev Integration

**Delivered**

- MVP 2.5 delivered and demoed 16 Mar — incorporates Amy's MVP 2.0 feedback on license sync ADM→Strev, new fields, new dashboard in Strev.
- Dynamic OAuth token for syncing data to Strev (security compliance) — 11 May.

**Active**

- Identifying all license part numbers/softwares in master data with license term and clean descriptions. **Dependency: MDM and DDP team** (flagged red on slide).
- Strev SOW 3 — integrating ADM QA to Strev QA; testing June released items.
- Discovering as-is asset flow — complex builds and other asset data syncs in Strev — WIP.
- Release governance wrt Strev QA environment — WIP.

**Next** *(highlighted = Akansh's emphasis)*

- Standard process for asset sync ADM→Strev (ADM holds data and syncs, replacing manual file uploads into Strev).
- Asset data sync ADM→Strev.
- Enhanced license data sync to Strev — immediate sync; grouping of internal customers in ADM.
- **Training of ADM to Senthil and team** (highlighted) — operational handoff signal.

**Future**

- Instantaneous sync to Strev; other misc data-sync enhancements.

### Track 2: ADM for Sales Enablement (Sales Ops)

**Delivered**

- Fetching license order data from DDP (EUDM) by vendor part # + supplier id — **3 Jul**.
- Export + audit trail in ADM — 3 Apr.
- Editing license details via UI — 3 Apr.
- Fetching end-user project name from IAP for license records lacking end-user info — 14 May *(truncated on slide)*.

**Active**

- Automated notifications to current sales rep for expirations within 60 days — **17 Jul**.
- Cancelled line items — one-time cleanup.
- Milestone 2026 data upload in ADM — July; reminder needed for 2025 and Q2 2026.
- More suppliers and part numbers onboarded in ADM — July (Natalie working with SRT).

**Next** *(highlighted = Akansh's emphasis)*

- **EUDM integration — extracting beyond configured supplier id.**
- **Extracting historical license data by customer id + supplier id.**
- **Cancelled line items removed from ADM.**
- HFU simplification for creating and updating records.
- Asset: **creating Asset Master data in ADM + fetching asset order data (ex: for APC)** *(truncated on slide)*.

**Future**

- Custom fields for asset and license; custom views for ADM pages.
- Reporting and analytics — renewal dollars by license/vendor/customer.
- Milestone and new supplier — new template integration.
- RBAC *(truncated on slide)*.
