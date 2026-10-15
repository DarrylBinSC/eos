# Strev Platform Priorities — 2027 AOP

> Transcribed 2026-09-02 from `Strev_AOP_2027_Priorities.docx`, provided by Darryl. Source is a priorities list, not a costed submission: it carries no cost, effort, sequence or date. Original document not yet filed in this folder.

## Scope note

This is the Strev vendor product enhancement track. It is **separate from** the internal Wesco question of how the business collects serial numbers and other asset metadata, which is an IT and process-ownership matter inside Wesco (WMX, VAS, GPO, MDM, DDP, Supplier Relations). Items in this list may or may not touch ADM's internal data-gathering constraints. The one clear interface is noted below.

## 1. Asset Data Management Enhancements

**Bulk parent-child asset mapping.** Large-scale asset hierarchy creation through bulk upload and import, so parent and child assets associate automatically during onboarding rather than being linked individually.
Business value: reduces manual setup effort, accelerates customer onboarding, improves data quality and consistency, supports larger deployment volumes.

**Automated warranty end date calculation.** Warranty end dates calculated automatically from configurable warranty rules and durations maintained within Strev.
Business value: eliminates manual date calculation, ensures consistency across tenants, simplifies asset lifecycle management, improves reporting accuracy.

## 2. Tenant Deployment and Scalability Enhancements

**Tenant configuration cloning and template management.** Clone and reuse tenant configurations across environments and customers: custom fields, asset attributes, views and dashboards, business rules, configurations and settings, user experience preferences.
Business value: accelerates customer deployments, promotes configuration standardization, reduces implementation effort, enables repeatable deployment models, improves scalability as customer adoption grows.

## 3. API and Integration Platform Enhancements

**API modernization and expansion.** Expand and standardize API capability to support Wesco platform integrations, data exchange and future scalability.

Required capabilities: asset query and retrieval; advanced search; telemetry ingestion and retrieval; metadata access and management; asset synchronization; event and status updates; support for complex asset and build structures; enhanced support for enterprise-scale integrations.

Primary integration targets: **entroCIM, Ascent**, and future Wesco platform integrations.

Business value: simplifies integration development, reduces custom integration effort, improves interoperability across platforms, supports enterprise customer requirements, enables broader solution offerings, creates a foundation for future integrations and platform expansion.

## Executive summary, as stated in the source

Primary investment areas: Asset Data Management (bulk parent-child mapping, automated warranty end date); Deployment Scalability (tenant configuration cloning and template management); API and Integration Platform (API modernization and expansion, entroCIM integration support, Ascent integration support, complex asset and build support).

Stated focus: reducing implementation effort, accelerating customer onboarding, improving integration capability, and scaling the Strev platform to support future growth and enterprise customer requirements.

## Reader's notes (Claude, 2026-09-02, not from the source)

1. **This is a portfolio investment, not a WAM one.** The named integration targets are entroCIM and Ascent. Two of the three areas, tenant cloning and API modernization, deliver value to products outside WAM. If the cost lands in the WAM FY27 P&L, the attribution will not survive review.
2. **No cost, effort or sequence.** Sean has asked for 2027 costs. This document does not contain them and cannot be converted into them without Strev.
3. **One genuine interface with the internal data-collection track.** Bulk parent-child asset mapping consumes parent-child hierarchy data, and "support for complex asset and build structures" in the API list does the same. Wesco has to be able to produce that data before Strev can ingest it in bulk. The dependency runs Wesco to Strev. Nothing else in this list depends on the internal collection question.
4. **Ron Snyder and the Navigator owners do not appear anywhere in the record as consulted** on the entroCIM and Ascent integration targets. Worth confirming before the list is presented as a portfolio position.

## Cross-reference added 2026-09-15, corrected same day

**What this list is.** This is **Wesco's** 2027 Digital Products enhancement demand on Strev: what we intend to ask the vendor to build. It is not Strev's own product roadmap. As of 2026-09-15 it has **not been communicated to Strev, not quoted, and not financed for 2027** (Darryl, direct).

**Why that matters now.** Revnue's "Feature Entitlements, Expansion Roadmap, and AI Feature Pack Pricing Framework" v2.5, May 2026, is the vendor's own commercial catalog: an AI Feature Pack at $84,000 per year per environment, a Preventative Maintenance Feature Pack, an IoT Feature Pack, and six add-on SKUs in private beta. Two Strev AI use cases entered UiPath intake on 2026-09-15 through Managed Services.

So Wesco has an **unfunded, uncommunicated 2027 enhancement ask containing no AI**, while vendor-originated AI capability from the same supplier is moving through a separate channel toward a funding decision. The exposure is sequencing: an AI commitment approved ahead of this list would set investment order by intake sequence rather than by product priority, and would do so before this list has a price against it.

**Consequent action.** `05` A43 adds a quotation request against this list to the Revnue question set, so the two can be compared on cost before either is funded.

See `Products/WAM/Wesco_WAM_Entitlements_AI_Feature_Pack_v2_5.pdf`, `Deliverables/WAM/2026-09-15_Strev_AI_Entitlement_Discrepancy_Review.md`, `Deliverables/Exec_Briefs/2026-09-15_Lisa_Orton_Strev_AI_Brief.pptx`, and `03` 2026-09-15.

**Provenance note.** Strev's original source file is not in this folder. All copies in the EOS derive from the 2026-09-02 transcription: this file, `Pandoc/processed/Strev_AOP_2027_Priorities-20260902-093108.md`, and `Pandoc/output/Strev_AOP_2027_Priorities.docx` (a Pandoc render of the transcription, not the vendor's document).

## Update 2026-09-17 — the sequencing exposure is now concrete, not theoretical

The 09-15 note above described a risk that investment order would be set by intake sequence rather than product priority. Two days later that is what is happening, and it is visible in the AOP rather than in a forecast.

**Amy Aguirre is including the $84,000 Strev AI enablement fee in the FY27 Wesco Asset Management AOP** (her own words, 2026-09-17 call). A fourth item, the **Virtual Site Survey**, is moving on a parallel track with Strev professional services development pricing and a per-site run rate requested and not yet received. Meanwhile this list, which is Wesco's own stated 2027 demand on the vendor, still has **no price against it, no communication to Strev, and no line in any AOP**.

So the vendor-originated track has a named owner preparing a funding request, and the Wesco-originated track has nobody preparing one. **Neither is funded** — an AOP line is a request that still has to clear approval and become a project in UiPath (Darryl, direct, 2026-09-17; `01` § Funding Governance) — so the distinction is not funded versus unfunded. It is that one track has an owner, a number and a route, and this list has none of the three. That is the sequencing exposure, and it is the one that decides order.

This is not an argument against the AI spend, which has a real business case behind it. It is an argument for getting a quotation against this list before the amendment is drafted, because once the amendment fixes the AI and site survey commercial terms, this list competes for whatever is left rather than being weighed against them.

`05` A43 question B11 already requests that quotation. `05` A49 is the amendment kickoff, dated 2026-09-24. **The quotation should land before the amendment is drafted, not after.**
