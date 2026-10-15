# entroCIM 2026 Road Map Goals (quarterly roadmap slide)

> As of: **2026-07-15** — transcribed from the "entroCIM Road Map Goals" slide. **Dated snapshot: refresh when the slide is reissued or quarterly scope shifts; flag in briefings if untouched 30+ days.** Stated goal: refine and improve user experience, build new features and capabilities which strengthen overall entroCIM performance and meet customer needs.

## Q1 2026 — COMPLETE

- entroCIM DC UI redesign (Figma)
- Tiles Gridboard app (Go Live)
- Collection App UI
- Chiller Opt UI
- SIM VAV
- Integrations: Hanwha, AMI Connector, RF Code Sentry

## Q2 2026 *(in flight — delivery vehicle is Release 3.1.12.13, Jul 20)*

- entroCIM HQ UI (Figma)
- Collection UI Redesign
- Bookmark App
- Training Modules
- QA Framework
- Connector App — Upload Tool
- Integrations: SafeTrust, Panduit

## Q3 2026

- SkySpark Ver 4 Update *(ties to Keith Bishop's SkySpark 4 AI discussions)*
- entroCIM PM
- Graphic Builder Animation App
- Knowledge Base Migration *(\*dependency on Wesco organization initiative)*
- Connector App — Connector Diagram
- Integrations: ServiceNow, Sensolus, tbd

## Q4 2026

- Site Readiness App *(\*\*relies on Deployment PM to provide scope + customer request pending)*
- UI/UX Redesign (Go Live): DC in Q4; HQ slips to Q1 2027
- Impact Analysis
- Integrations: tbd

## Timing update, 2026-08-12 (entroCIM Backlog Deep Dive) — this slide is now stale on dates

Q3 release holds at **early October** (consistent with the 2026-10-05 date tracked in `04_Executive_Watch_List.md`). **Q4 has slipped to early 2027** — the Q4 2026 section below (Site Readiness App, UI/UX Redesign Go-Live, Impact Analysis) should be read as early-2027 delivery until a reissued slide states otherwise. Scope itself not confirmed changed, only timing. Containerization is now the confirmed mandatory deployment model going forward (`Products/entroCIM/entroCIM.md`, `03` Decisions Made) — not on this slide at all, since it predates that decision; the slide needs a full reissue, not a patch, given both the date slip and the missing architecture decision.

## Current view for Sean, 2026-10-14 (Darryl direct; the July slide above remains stale)

- **Shipping now:** Release 3.1.12.14 (Batch Point Writer, Graphics Builder grouping, Tiles Gridboard text widget, search beta, platform and security), in DCOE governance.
- **Q1 2027: entroCIM 4** (built on SkySpark 4), containerized, with the **Woolly AI launch** (Darryl: target Q1 2027). Call it entroCIM 4 outside the team.
- **Rest of 2027:** being reconciled to the new staffing level (Darryl, Ron Snyder, David Blondel; end of October): UI redesign go-live (DC then HQ), Site Readiness, Impact Analysis, CDA device and configuration assurance; two major feature releases a year (Q2, Q4) per the 2026-09-16 cadence.
- Slide: `Deliverables/Exec_Briefs/2026-10-14_Sean_Portfolio_Deck_v4.pptx`. No reissued roadmap slide from David or Ron is on file; replace this view when one is.

## Connector fact, confirmed 2026-08-12 (Darryl, direct)

Hanwha **and Axis** camera connectors are both live in production entroCIM. The transcribed Q1 slide above lists Hanwha only; Axis does not appear on it. Both are treated as production for CDA positioning (used on `CDA_Why_Wesco_Slide.pptx`). Scope of the claim: device connection and data retrieval. Per-manufacturer firmware update rights are still in qualification (`CDA/05_Operating_Record/Risk_and_Dependency_Log.md`, D1), so "already connected" is supportable and "already updating firmware" is not.

## Executive Read (Claude, 07-15)

- Q2 slide scope matches Ron's Jul 20 release scope (Bookmark, Collection redesign, Connector Upload, Tiles/Gridboard) — roadmap and release plan are aligned; good governance signal.
- The two flagged dependencies are both external to the team: Knowledge Base Migration (Wesco org initiative) and Site Readiness App (Deployment PM scope + customer request). These are the slip risks to watch, not engineering capacity.
- Back half of the year is dependency-heavier and vaguer (two "tbd" integration slots, HQ UI go-live already showing Q1 2027) — normal at mid-year, but Q3 scope should firm up at or shortly after the Jul 20 release.
- Roadmap is feature/UX-language throughout; per the standing preference, connect items to commercial value when presenting upward (e.g., ServiceNow integration → Managed Services enablement).
