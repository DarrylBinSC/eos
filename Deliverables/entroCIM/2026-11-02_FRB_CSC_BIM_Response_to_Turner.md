# FRBNY Cash Services Center Smart Building Bid: BIM Response

Wesco response to Bid Supplement 01, item B37 as revised, and to the Owner's clarification of the BIM objective. This response supplements Wesco's BIM and COBie reply of October 29, 2026, which remains in effect. Bracketed items are completed before submission.

## 1. Summary

- Wesco participates fully in the Project's BIM process. Wesco does not author, coordinate, or maintain BIM models, consistent with the struck modeling provisions of B37.
- Wesco delivers COBie data for the equipment it furnishes, as a workbook at the Project's COBie data drops.
- Wesco incorporates the Project's handover model and COBie data into the Smart Building Platform in three stages: one delivered within the Project, two on the entroCIM product roadmap, both in place before Smart Building start-up and commissioning in the Project schedule.
- The Owner's systems of record are unchanged. Kahua holds the turnover model and COBie workbook; the Owner's facility management system holds the asset register. The Smart Building Platform is the operational layer and holds a reference copy of the handover data, joined to live building data by the FRBNY Asset ID.
- Stage 1 is priced in the base bid. Stages 2 and 3 are offered as Add Alternates with a development charge, an annual advanced-feature license, and project services.

## 2. BIM process participation (B37; BIM Requirements 3.1, 3.4, 3.13)

Wesco will participate in the Project's BIM process as described in the BIM Execution Plan and the FRBNY BIM Requirements (Version 04, February 27, 2026): coordination and review meetings, file naming and exchange conventions on Autodesk Construction Cloud, information security for any model data Wesco receives (3.7), and COBie data for Wesco-furnished equipment (14.4 to 14.7) as assigned in the COBie Responsibility Matrix.

Consistent with the struck modeling and LOD 400/500 provisions of B37 and Turner's clarification of October 20, 2026, Wesco does not author, model, clash-detect, or maintain BIM models. The modeling, Level of Development, BIM Manager, 3D as-built and solid-model provisions of the BIM Requirements (sections 2, 3.3, 3.14, 5.1, 7, 8, 14.3 and 16.4) do not apply to the Smart Building subcontractor, which is not among the trades listed in section 8. Wesco requests Turner's written confirmation of this exclusion under section 3.1. Wesco is not providing BIM Lead services. Add Alternate H5 (post-occupancy model updates) is not offered.

## 3. COBie data for Wesco-furnished equipment (B37; BIM Requirements 14.4 to 14.7)

Wesco will deliver COBie data for the equipment it furnishes under this scope (servers, network appliances, and gateways furnished under Add Alternate H1 if elected): dimensions, material, manufacturer, model, install date, warranty, location by grid, and system association, with cut sheets, shop drawings, and applicable test results linked.

The data is delivered as a COBie workbook using the Project's shared parameters and FRBNY Asset IDs (14.7.4), at the data drops assigned to Wesco in the COBie Responsibility Matrix (14.4.3), submitted through Turner for review and upload to Kahua. Because Wesco authors no BIM model, the workbook is Wesco's form of COBie contribution; Wesco requests that the Responsibility Matrix record it that way. Pressure, compaction, and infiltration tests do not apply to Wesco-furnished equipment and are excluded.

## 4. Incorporating the Project's BIM and COBie data into the Smart Building Platform (B37, C1.1, 25 00 00 2.03 G and H)

### 4.1 The Owner's objective and the roles of each system

Wesco understands the Owner's objective: the Smart Building Platform should house the Project's BIM data, with 3D graphics over time, to support asset management across the facility rather than building automation operation.

Kahua holds the Project's turnover model and final COBie workbook as the Owner's record (14.3.3). The Owner's facility management system (IBM TRIRIGA, 14.4.5) holds the asset register. The Smart Building Platform is the operational layer: it holds the live points of the connected building and, under this proposal, a reference copy of the handover model and asset data for the assets it operates, joined to the live data by the FRBNY Asset ID (14.7.4). The platform does not become the system of record for the model or the asset register, and no data flows from the platform back to either.

The platform's operational data comes from the installed, connected, and commissioned building, not from the model. Where the handover record and the commissioned building differ, the platform reflects the building and reports the difference.

### 4.2 Stage 1: Project delivery (base bid, [line reference]; performed at closeout, 2029)

- COBie mapping (2.03 G): one-way mapping of the Project's validated final COBie workbook (14.6.1) into the platform's asset and location hierarchy, keyed on the FRBNY Asset ID, as described in Wesco's reply of October 29, 2026. The Owner's facility management system remains the asset register of record. Work-order integration with that system is priced separately under Add Alternate H2.
- 2D floor-plan graphics built from the model's 2D plan exports, with asset data and live points shown in context on each level. During construction, plans for the temporary access portal (C51) are built from the coordinated model's exports and rebuilt once from the as-built set. This is the spatial navigation offered today in place of 2.03 H, under deviation 2.03 D.
- Handover reconciliation: a report of differences between the handover record and the commissioned building (assets in the record not commissioned, connected devices absent from the record, locations that differ), issued at the end of Smart Building commissioning for the Owner's use in correcting the record.
- Model file reference: each asset and level in the platform links to its turnover record in Kahua, and the platform holds a reference copy of the IFC and COBie files within the FRBNY-hosted environment, subject to Turner's and the Owner's written permission (section 6).

### 4.3 Stage 2: BIM data repository (Add Alternate [ref]; in place before Smart Building start-up, December 2028)

- Storage and version tracking of the Project's model data within the platform, received as IFC (Industry Foundation Classes, the open BIM exchange format and already a required turnover format under 14.3.1) together with COBie, with each model element linked to its platform asset by the FRBNY Asset ID. The platform reads the non-geometric content of the IFC; it does not read native Revit files, which are held as documents.
- API read access, so the Owner's other applications (asset management, computerized maintenance management, BIM tools) can read model and asset data held in the platform.
- Reloading of the repository from a revised model and COBie set when the Owner issues one and requests it, as a priced service, with a matched, new, missing, and moved report. The platform does not detect or absorb model changes on its own.

### 4.4 Stage 3: 3D viewing (Add Alternate [ref]; in place before Smart Building commissioning, February 2029; resolves 2.03 H)

- Viewing the stored as-built model in 3D within the platform's user interface, with asset data and live points shown in context, for asset management use. The model is displayed from the IFC turnover deliverable through an embedded viewer component hosted in the FRBNY environment; the platform does not author or edit the model. Selection in the 3D view and in the platform's asset views is synchronized by Asset ID.

### 4.5 entroCIM's Scope

entroCIM is an operations and asset data platform. It is not a BIM authoring, modeling, or coordination tool, and it will not replace Revit, the federated model, or the BIM/VDC provider as the system of record for the model. Wesco's deviation at 2.03 D describes the capability available today against 2.03 H and stands until Stage 3 is released.

## 5. Stages and Effort

| Item | Basis | Amount |
|---|---|---|
| Stage 1 (COBie mapping, floor plans, reconciliation, model file reference) | Base bid | [$ ] at [line reference] |
| Stage 2 development charge | Add Alternate [ref]; paid on stage acceptance | [$ ] |
| Stage 3 development charge | Add Alternate [ref]; paid on stage acceptance; proceeds only after Stage 2 acceptance | [$ ] |
| Advanced BIM feature license (Stages 2 and 3), per year from release | In addition to base entroCIM licensing and support; follows Deduct Alternate H3 treatment if the Owner procures licensing directly | [$ ] per year |
| Stage 2 data loading and configuration service | At Stage 2 release | [$ ] |
| Stage 3 configuration service | At Stage 3 release | [$ ] |

The development charges fund the design and build of the capability and secure the Owner's place as a launch facility. Each stage is delivered against a written scope and acceptance criteria agreed with the Owner during the Smart Building submittal period (December 2026 to March 2027). Timing is set against the Project schedule (September 2026 update): Stage 2 before Smart Building system start-up (START/TEST-2510) and Stage 3 before Smart Building commissioning functional testing (A13720), so both are available when the LOD 500 as-built model and final COBie workbook are delivered at closeout. Wesco retains all intellectual property in the capability and will offer it to other customers; the Owner receives a license to use it. Wesco would review progress with the Owner [quarterly]. Stage 1 and the base platform do not depend on Stages 2 or 3 being elected.

## 6. Model data, security, and intellectual property

Model and COBie data held in the platform is handled under the FRBNY information security requirements (3.7): the platform is deployed in the Owner's environment, access is limited to authorized personnel, and access is auditable. Turner's and the Owner's rights in the models (3.6, 3.8) and the terms of the HLW Electronic File Agreement are acknowledged; the Project's model files are used only for this Project and Site and are not used by Wesco for product development. Wesco requests Turner's and the Owner's written permission to hold a reference copy of the turnover models and COBie data in the platform for the Owner's use.

## 7. Exclusions

Creation, revision, coordination, and post-occupancy maintenance of BIM models; BIM Lead services; Add Alternate H5; reading or editing native Revit files; automatic synchronization of model changes into the platform; any data flow from the platform to the model, the COBie data set, or the Owner's asset register other than the work-order path under Add Alternate H2.

## 8. Information requested from Turner and the Owner

1. Written confirmation of Wesco's exclusion from the modeling provisions of the BIM Requirements (section 2 above).
2. The COBie version, delivery format and data-drop schedule the Project will use; the COBie Responsibility Matrix; and the Asset Information Requirements.
3. Confirmation that the FRBNY Asset ID is populated on every maintainable component in the COBie workbook and exported as a property in the IFC turnover files (7.18.4, 14.7.4).
4. Confirmation of the Owner's facility management system for COBie integration (14.4.5 names IBM TRIRIGA as an example).
5. Written permission to hold a reference copy of the turnover models and COBie data in the platform (section 6).
6. Confirmation that no data is expected to flow from the platform back to the BIM, the COBie data set, or the Owner's asset register.
