# CDA Requirements Spec: write-spec Prompt

Status: DRAFT for Darryl's review. Edit freely, then return to Claude for execution with `/product-management:write-spec`.
Prepared: 2026-11-02, ahead of the requirements session with Ron Snyder.

---

## Context

You are drafting the first version of the product requirements spec (PRD) for Connected Device Assurance (CDA), a Wesco product led by Darryl Benson, Senior Director of CSS Platforms. The spec will be used in a working session today with Ron Snyder, Director of Software Development, who leads the developers, built the current entroCIM platform, and knows its internals in detail. Ron has no Nozomi Networks experience yet.

What CDA is:

- A single packaged, per-site service that gives a customer assurance over its connected devices (cameras first, then access control, IoT and OT devices, data center auxiliary systems, and IT devices via SNMP). One annual fee per site covering hardware, software and services; site size and a complexity uplift are the only commercial variables. There are no product tiers. Internally the architecture may have modules, but modules do not appear in pricing or positioning.
- Built on SkySpark and many of the entroCIM components, by the entroCIM team, as a line item on the entroCIM roadmap. CDA was not approved as a standalone FY27 AOP project; there is no incremental FY27 budget. Development continues inside the entroCIM roadmap. The 2027 core entroCIM roadmap and the CDA build are being reconciled by Darryl, Ron Snyder and David Blondel.
- Positioned internally as the data collector and the wedge that gets entroCIM into the door. The buyer-side case is that CDA is a much easier sale for a typical Wesco salesperson, who is not a technology seller. Business sponsor is Bill Muczko. Bob Caprise advises on financials. The TS team (Matt Powers, Cody Remington) has reviewed the delivery concept and raised go-to-market questions, not delivery questions.
- The cyber value proposition comes from embedded Nozomi technology: Wesco as a Nozomi MSP, with a Guardian sensor on each CDA instance. The Nozomi piece is going through Demand Intake separately with a BIR (target submission 2026-11-06), covering licensing and training starting 2027 and scaling with usage. Nothing about Nozomi integration has been validated with Nozomi or built yet.
- Relevant existing capability: entroCIM has a Panduit connector built and a Schneider EcoStruxure integration in development. Deployment model includes white-glove installs and air-gapped environments.

Darryl has already architected and brainstormed the intended functionality (see Source Material). Ron has not yet contributed. The purpose of today's session is to convert Darryl's intent into requirements Ron can size and challenge.

## Task

Produce CDA Requirements Spec v0.1: a structured PRD that Darryl can walk through with Ron Snyder in one hour, where every requirement is either something Ron can validate from his knowledge of entroCIM today, or is explicitly flagged as dependent on Nozomi and therefore an assumption or open question rather than a requirement.

## Goal

A first draft good enough that the meeting is spent on Ron's corrections, sizing and questions, not on building structure. Success is a v0.2 after the meeting that contains Ron's input and a clean list of Nozomi unknowns that can be reused verbatim as scope and questions in the Nozomi BIR.

## Constraints

1. Two-column discipline. Every functional requirement is tagged either `[entroCIM]` (Ron can validate today: SkySpark, existing entroCIM components, Haystack tagging, data collection, connectors, deployment, air-gapped delivery, UI patterns) or `[Nozomi]` (depends on Guardian, Nozomi APIs, MSP licensing, Nozomi training or support). `[Nozomi]` items are written as assumptions or questions, never as settled requirements. Do not state how Guardian behaves, what it exposes, or how it licenses as fact.
2. Non-goals are explicit and include at least: CDA is not an IT device management or RMM product; CDA is not a standalone SOC or managed detection service; CDA does not replace a customer's existing security tooling; no product tiers; no module-level pricing.
3. Commercial model is fixed and must not be redesigned: one annual fee per site, size plus complexity uplift, zero capital cost to the customer. Do not propose tiers, add-ons, or per-device pricing.
4. Funding reality is fixed: no incremental FY27 budget, development by the entroCIM team inside the entroCIM roadmap, Nozomi licensing and training via a separate BIR from 2027. Phasing must be consistent with that. Do not imply a standalone project, a dedicated team, or seed funding.
5. Reuse first. Where a requirement can be met by an existing entroCIM component or pattern, say so and name it; where it is net-new, say so. Where you cannot tell, mark it `[Ron to confirm]`. Do not guess.
6. Cameras are the first device class (Wesco's concentration in that business, the Axis install base). Later device classes appear as roadmap phases, not as v1 requirements.
7. Audience for the document is Ron and David Blondel. Technical language is fine. Do not write marketing copy or restate the business case; one short problem statement is enough.
8. Separate facts, assumptions and inferences. Anything taken from Source Material that is a plan or an idea rather than a confirmed decision is labeled as such.
9. US English. No em dashes. Product name styled "entroCIM". Refer to entroCIM component licensing as "entroCIM components," never "PODs."
10. Length: target 4 to 6 pages of Markdown. Prefer tables for requirements and open questions.

## Source Material

Read in this order. Later items rank below earlier ones where they conflict; `CDA.md` and `CDA_Start_Here.md` are canonical.

Folder: `Products/CDA/` in the Executive Operating System.

1. `CDA_Start_Here.md` (orientation and current state)
2. `CDA.md` (canonical product file; dated sections, newest last)
3. `02_Phase_2_Dossiers/CDA_Architecture_Executive.md` and `CDA_Architecture_Executive.mermaid` (Darryl's architecture)
4. `02_Phase_2_Dossiers/CSS_Platforms_2027_Phase_2_Updated_Deep_Dive.md` (functional brainstorm and deep dive; treat as ideation, not decisions)
5. `03_Phase_3_Funding/CDA_Business_Case_Working.md` (scope, service definition, pricing model as decided; use for scope boundaries, not for the business case narrative)
6. `05_Operating_Record/Risk_and_Dependency_Log.md` (known risks and dependencies; carry forward anything that is a requirement constraint)
7. `02_Phase_2_Dossiers/SecuriThings_Deck_Review_2026-10-26.md` and `RMM_Category_Review_2026-07-28.md` (competitive context; use only to sharpen non-goals and differentiation, not to add features)

Do not use the executive briefs, intake decks or Sean review decks as requirement sources; they are positioning material and some content is superseded (the Assure/Manage tiering in the August 2026 brief was retired on 2026-09-29).

Where the Source Material is silent on something a PRD needs, write `[Not in source; Darryl to confirm]` rather than filling the gap.

## Required Analysis

1. Problem statement and buyer. One paragraph each. Who buys, who operates, what they get that they do not have today.
2. Users and operating roles. Customer site operator, Wesco delivery (install and commissioning), Wesco managed service (ongoing monitoring and service), Wesco sales. Keep to what each role needs from the product, not org design.
3. Functional requirements, grouped by capability area. Suggested areas, adjust if the sources support a better grouping: device discovery and inventory; device health and availability monitoring; configuration and firmware posture; cyber posture and anomaly signals; alerting, workflow and service actions; reporting and customer-facing views; data model and tagging (Haystack); connectors and integrations (Panduit, EcoStruxure, camera vendors, SNMP); deployment and commissioning (including air-gapped); multi-site and multi-tenant operation; security of the platform itself. Each requirement row: ID, requirement, tag (`[entroCIM]` / `[Nozomi]`), reuse status (existing component / extension / net-new / `[Ron to confirm]`), priority (P0 for first camera-site release, P1, Later), source reference.
4. Non-goals, per Constraint 2, with one line of reasoning each.
5. Nozomi dependency register. Every `[Nozomi]` item collected in one table: assumption as currently held, what we need to learn, who can answer (Nozomi, Ron's team after training, TS), and whether it blocks P0. This table is intended to be lifted into the BIR.
6. Phasing. Phase 1: first camera-site release on existing entroCIM components with the minimum Nozomi integration that delivers the cyber value proposition. Phase 2 and Later: additional device classes and depth. State phase exit criteria. Do not assign dates; the roadmap reconciliation with Ron and David owns dates.
7. Success metrics. A small set, split into product metrics (coverage, time to detect, time to commission a site) and business metrics (sites sold, attach to entroCIM). Mark each as measurable today or requiring instrumentation.
8. Acceptance criteria for Phase 1, written so Ron's team can test them.
9. Open questions for Ron, as a separate, numbered list ordered by how much they change the sizing. These are the questions to spend the meeting on.
10. Open questions for Darryl, separately: anything the sources did not settle and only Darryl can.

## Output Format

Markdown, one file, titled `CDA Requirements Spec v0.1`. Sections in this order:

1. Status and purpose (three lines: version, date, what this draft is for)
2. Problem statement and buyer
3. Users and roles
4. Goals and non-goals
5. Functional requirements (tables by capability area)
6. Nozomi dependency register (table)
7. Phasing and exit criteria
8. Success metrics
9. Phase 1 acceptance criteria
10. Questions for Ron (numbered, ordered by sizing impact)
11. Questions for Darryl
12. Source references (file and section for each requirement cited)

No subtitles under section headings. Short, plain headings. Tables preferred over nested bullets. No em dashes.

## Validation Criteria

Before returning the draft, check and state the result of each:

1. Every functional requirement carries a tag, a reuse status, a priority and a source reference.
2. No `[Nozomi]` row is phrased as a settled requirement.
3. No requirement implies tiers, add-ons, per-device pricing, a standalone project, a dedicated team or FY27 incremental budget.
4. Every non-goal in Constraint 2 is present.
5. The Nozomi dependency register can be read on its own and reused in the BIR without edits.
6. Questions for Ron are things only Ron (or his team) can answer; questions about the business, customers or priorities are in the Darryl list instead.
7. Anything not supported by Source Material is marked `[Not in source; Darryl to confirm]` and nothing has been invented to fill a gap.
8. Spelling is US English; "entroCIM" is styled correctly throughout; "PODs" does not appear; there are no em dashes.
9. Length is within 4 to 6 pages.

List any validation item that failed and why, rather than silently fixing it in a way that changes meaning.
