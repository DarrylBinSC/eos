# Products — Per-Product Deep Context

One file per product or ecosystem partner. These are living-adjacent: Claude enriches them from briefing evidence; Darryl enriches them from ChatGPT exports and direct knowledge. Each carries an "As of" date.

## Standard structure (products)

```
# [Product]
As of: YYYY-MM-DD

## What It Is / Value Proposition
## Current State (readiness, install base, release posture)
## Commercial Position (pipeline, pricing posture, competitors)
## Key Dependencies (data, teams, vendors)
## Managed Services Angle
## Benefits Realization (planned vs. realized, leading indicators)
## Key People (owner, leads, commercial, external)
## Major Risks and Open Decisions (pointer to 03/04 for current status)
## History and Lessons
```

For ecosystem partners (e.g., SkyFoundry): replace roadmap sections with Relationship Health, What We Depend On Them For, What They Get From Us, and Strategic Options.

## ChatGPT Export Prompt (per product)

```
Based on everything you know from our conversation history about [PRODUCT], write a durable product knowledge file in Markdown using these sections: What It Is / Value Proposition; Current State; Commercial Position; Key Dependencies; Managed Services Angle; Benefits Realization; Key People; Major Risks and Open Decisions; History and Lessons.

Rules: distill, don't recount conversations. Reflect my final positions, not the journey. Mark possibly-outdated facts inline "(as of [date], may have changed)". Be specific with names, systems, numbers; mark uncertainty honestly. Include an "As of: [today's date in YYYY-MM-DD]" line at the top.

File output:
- Create the result as a downloadable Markdown file (.md), not just a chat response.
- Name it exactly [PRODUCT].md with underscores for spaces: e.g. WAM.md, entroCIM.md, Connected_Safety.md, SkyFoundry.md.
- Give me a download link to the .md file.
```

## Saving Export Files

Don't save ChatGPT product exports directly over these files — `WAM.md` and `entroCIM.md` already contain current evidence that an overwrite would destroy. Instead, paste the export into a chat session and say "merge this into Products/[name]" — Claude merges history/lessons from the export with the evidence-based sections and updates the As-of date. For brand-new products with no existing file, saving the export directly into this folder as `Name.md` is fine.

## Structure (reorganized 2026-08-18)

Products with a working body of material get a **folder**; everything in that folder belongs to that product. Products with a single context file, and partner/alliance files, sit at the root.

```
Products/
  WAM/          WAM.md, WAM_Roadmap.md, WAM_Data_Architecture.md,
                Part_Classification.md, WAM_Backlog_Deep_Dive_2026-08-05.pdf,
                FY27 AOP collation template + backup
  entroCIM/     entroCIM.md, entroCIM_Roadmap.md, commercialization decks,
                architecture, FY27 AOP collation template + backup, P&L analysis
  Navigator/    Navigator.md, BIR 2603158, intake deck,
                FY27 AOP collation template + backup
  CDA/          Connected Device Assurance — all current and future material.
                Renamed from CSS_Device_Lifecycle_Ideation on 2026-08-18.
                Phase folders 00_Charter through 05_Operating_Record retained.
  CAT/          Connected Asset Tracking — returnable asset tracking research
                area, created 2026-09-16. Phase folders 00_Charter,
                01_Technology_Research, 02_Commercial, 03_Architecture,
                05_Operating_Record.
  CLM/          Contract Lifecycle Management — enterprise CLM product
                (Nanda Kumar Rajagopal scope), added 2026-09-28. CLM.md is
                the front door; source email, scope doc and process visual
                sit alongside it. Intended for Darryl's team to build and
                develop; Sean decides at AOP meetings wk of 2026-09-28.
  (root)        Single-file products and partner files
```

**Root files, and why they stay there:**

- `CMP.md`, `Connected_Safety.md`, `Spanr.md` — strategic placeholders, Medium-Low confidence. Validate before detailed recommendations. Promote to a folder if they acquire real material.
- `SkyFoundry.md`, `JCI_Partnership.md`, `JCI_Airwall_Competitive_Landscape.md`, `i3_Alliance.md` — **ecosystem partners and alliances, not products.** Kept separate deliberately: filing a partner inside one product's folder would hide it from the others and break the partner/product distinction this README defines. SkyFoundry is the closest call, since SkySpark underlies entroCIM specifically; move it if you prefer.
- `Architectures_and_Roadmaps_2026-07-29.pptx` — cross-product deck (entroCIM architecture, WAM value chain, ADM/Strev roadmap). Belongs to no single product.
- `README.md` — this file.

## Files

- `WAM/WAM.md` — merged 2026-07-14 (baseline + evidence + context library); FY27 P&L section added 08-17
- `WAM/WAM_Data_Architecture.md` — data domains, systems (DDP/EUDM, MDM, WMX, ACT/WACT, VAS, IDP), classification, entitlement concept, failure modes
- `WAM/Part_Classification.md` — Darryl's local AI classification/research project (Part_Research_V2_Test; read AI_Project_Context.md first when working on it)
- `entroCIM/entroCIM.md` — merged 2026-07-14 (baseline + evidence + context library); FY27 P&L section added 08-17
- `entroCIM/Connectors/` — connector documentation, added 2026-09-16. `entroCIM_Sensolus_Connector_2026-09-16.md` catalogs the completed Sensolus connector; the three Confluence page exports sit alongside it. Referenced by `CAT/` rather than duplicated there
- `Navigator/Navigator.md` — updated 2026-08-18; **Darryl is the Product Executive** (supersedes the Digital Product List entry naming Chris Gazdic)
- `CAT/CAT.md` — created 2026-09-16; new area for returnable asset tracking (partner vs. build decision). Charter and research plan in `CAT/00_Charter/`; vendor and connectivity research with sources in `CAT/01_Technology_Research/`. Deliverables in `Deliverables/CAT/`
- `CLM/CLM.md` — created 2026-09-28 from the Nanda Kumar Rajagopal scope, the Chris Gazdic forward (Copilot notes of his call with Nanda) and the process/module visual. Enterprise, not CSS; not on the August 2026 Digital Product List. Intended for Darryl and his team to build and develop (Sean, verbal, 2026-09-28); final decision at the corporate AOP meetings that week. Epic map, dependencies (FileNet, Contract Intelligence, Nitro/DocuSign, Oracle, Dynamics) and open questions (Darryl's role, build vs. buy after iCertis, SOX scope)
- `CDA/CDA.md` — created 2026-09-01 to close a routing gap (CDA had phase files but no root durable-knowledge file like the other three products); phase files hold working detail and are not duplicated into it
- `JCI_Airwall_Competitive_Landscape.md` — created 2026-09-17; vendor catalog for the twelve Airwall competitors named in a JCI-forwarded Gartner survey, with Wesco-fit assessment per vendor and public sources. Companion to `JCI_Partnership.md`; analysis deliverable in `Deliverables/JCI/2026-09-17_JCI_Airwall_Competitive_Analysis.md`
- `SkyFoundry.md` — ecosystem partner (SkySpark underlies entroCIM; Xeto)
- `Spanr.md`, `Connected_Safety.md`, `CMP.md` — strategic placeholders, Medium-Low confidence

## FY27 AOP submissions

**Naming convention (set 2026-08-18).** All four collation templates use the same scheme:

- `COPY_<product>_...xlsx` — **the live working copy.** The COPY prefix marks it as ours, distinct from the master controlled in company folders
- `COPY_..._BACKUP_<date>.xlsx` — snapshot alongside each live file
- `SUPERSEDED_<date>_...xlsx` — retained for the trail, not the live file

| Product | Live file | B18 |
|---|---|---|
| WAM | `WAM/COPY_wam_build_it-...` | $785,840 |
| entroCIM | `entroCIM/COPY_entrocim_build_it-...` | $857,052 |
| Navigator | `Navigator/COPY_ascent-navigator_build_it-...` | $1,797,280 |
| CDA | `CDA/04_Phase_4_AOP/COPY_connected-device-assurance_build_it-...` | $246,787 |

Tabs 3 and 4 complete on all four; scoring 13/13 each. Change logs in `Deliverables/<product>/`.

**entroCIM carried two live files until 2026-08-18.** Darryl rebuilt the submission from a fresh template on 08-17 (previously named `FINAL - entrocim_build_it-...`); that rebuild is now the live `COPY_` file. The earlier `entrocim_op-2027_...` working file and its original-state backup are renamed `SUPERSEDED_2026-08-17_...` so only one live file per product exists.
