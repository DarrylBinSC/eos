# M365 Evidence: Monday.com Deep Dive

**Research window:** October 29, 2024 through October 29, 2026  
**Prepared:** October 29, 2026  
**Purpose:** One-time Microsoft 365 evidence review of Wesco's use of monday.com, also referenced as Monday.com, Monday, and Work OS.

## Source coverage and limitations

### Searched successfully

- Outlook email, including Inbox and Sent Items
- Teams chats/messages and meeting chats surfaced by Microsoft 365 search
- Calendar and meeting records
- Meeting transcripts and recordings
- OneDrive and SharePoint-indexed files
- SharePoint and intranet pages
- Loop and other files indexed by Microsoft 365 search
- Viva Engage, separately through its connector

### Could not independently enumerate or search as distinct repositories

- Planner
- To Do
- OneNote

These sources may surface when indexed in Microsoft 365 search, but the available retrieval interfaces did not support a repository-complete search of each.

### Viva Engage

Viva Engage was separately searched for `Monday.com` and `Work OS` over the date range. Results were false positives around the ordinary word “Monday” and WMX “work” content. No substantiated monday.com platform content was found.

### SharePoint sites and libraries identifiable by name

- `Corpmarketing`
- `Corpmarketing / Shared Documents / Monday.com Platform Tutorials`
- SharePoint-hosted Digital Products meeting-recording and document content surfaced through Teams
- Personal OneDrive and SharePoint files linked in Digital Products discussions

The most clearly identifiable intranet source was `Marketing-Communications.aspx` in `Corpmarketing`; it links directly to the `Monday.com Platform Tutorials` library. (document: Corpmarketing / Site Pages / Marketing-Communications.aspx) citeturn1search718L14-L28

### Teams and meeting contexts identifiable by name

- `Digital Products / Agile Staff Meeting`
- `Connected Safety Weekly Update`
- C2P-related meeting material surfaced around the TrackIt/Tracket production-change process

The parent Team or channel name was not visible for every returned Teams message, so a complete named inventory of Teams and channels could not be substantiated.

---

## Executive picture

The evidence shows monday.com evolving rapidly from a comparatively small workflow tool into a Wesco-wide service and work-management platform. In the September 1, 2026 `Digital Products / Agile Staff Meeting`, Sean McCloskey said “monday.com is growing rapidly,” while describing governance, adoption, training and security as issues that still needed to mature with the platform. (transcript, Sean McCloskey, September 1, 2026) citeturn1search675L184-L200

The strongest quantitative evidence is internally inconsistent. In the same meeting, Sean McCloskey described growth from “144 licenses at the beginning of the year” to “850 or so,” while Chris Gazdic immediately corrected that to “Just over 1000.” Both contemporaneous counts are reported rather than reconciled. (transcript, September 1, 2026) citeturn1search528L469-L471

A late-summer Digital Products deck gives a more precise allocation totaling 962 licenses: CSS 485, Marketing 279, EES 168 and EECOL 30. (document: Digital Products portfolio deck) citeturn1search873L17

---

# 1. Contract and commercials

## What is established

A WAB production-change deck says Wesco is leveraging an existing “Monday.com Enterprise investment” and is “currently on a 3-year contract.” For an additional capacity-planning capability, it quotes:

> “$3.25/user x 12 months x 250 users = $9,750 annually”

and:

> “Since you are currently on a 3-year contract, the prorated price would be about $26,812.50 total”

Author: Graham Russ; 2026 WAB material. (document: `Monday.com - Tracket Integration - v0.3.pptx`) citeturn1search605L2

## Contract details not recovered

Nothing was found in an opened authoritative agreement or order form for:

- Original agreement or order-form effective date
- Contractual renewal date
- Notice period
- Base annual contract value
- Base per-seat rate
- Guardian add-on pricing
- monday CRM, dev or service commercial products
- AI-credit quantity or AI-credit price
- Discount percentage
- Authoritative Wesco contracting or procurement owner
- Named monday.com CSM or account executive
- Invoice or PO number
- Pending renewal quote

Search terms included: `Monday.com contract agreement order form quote renewal invoice purchase requisition procurement VMO Enterprise Guardian seats price AI credits account manager CSM`.

This is the largest remaining evidence gap. References to commercial structure were found, but not the executed contract or order form itself.

---

# 2. Licenses and users

## Counts found

| Evidence date or context | Count |
|---|---:|
| “Beginning of the year,” according to Sean McCloskey on September 1, 2026 | 144 |
| September 1 verbal estimate, Sean McCloskey | “850 or so” |
| Same September 1 discussion, Chris Gazdic | “Just over 1000” |
| Digital Products deck, CSS | 485 |
| Digital Products deck, Marketing | 279 |
| Digital Products deck, EES | 168 |
| Digital Products deck, EECOL | 30 |

The first three quotes are directly from the meeting transcript. (transcript, September 1, 2026) citeturn1search528L469-L471 The divisional figures appear together in `aug_deep-dive_engel-deck_digital-products-portfolio.pptx`. (document) citeturn1search873L17

The four divisional allocations sum to 962. This is arithmetic based on the document values, not a claim that 962 was the definitive enterprise license count.

## License types and provisioning

Brittany Pearce's `Monday.com SOP for Access.docx` distinguishes Supervisor/Member requests and Viewer access. Existing-team requests go through AssistMe. The SOP says to allow “24–48 hours for your SSO to be created, added to the correct Monday.com department, and for the appropriate licenses to be assigned.” (document, last update December 17, 2025) citeturn1search710L1-L14

Viewer requests specifically use the role `Monday.com_Viewer`. (document) citeturn1search710L15-L22

New teams cannot simply request seats. The SOP says that a manager requesting a new group must start a “Business Use Case for approving Monday.com for your team.” (document) citeturn1search710L23-L28

## Count gaps

Nothing was found giving a dated enterprise-wide member, viewer, guest or admin census.

Search terms: `members viewers guests admins Monday.com users license report active users adoption`.

---

# 3. Ownership and roles

There is clear evidence of ownership changing or being reorganized.

## Chris Gazdic

A Digital Products deck explicitly labels Christopher Gazdic “Product Executive” for Monday.com. Another Digital Product List names Chris Gazdic as product executive with all SBUs impacted. (document: `aug_deep-dive_engel-deck_digital-products-portfolio.pptx`) citeturn1search873L17 citeturn1search873L25

## Brittany Pearce

In the September 1 meeting, Sean McCloskey said:

> “Brittany has been the lead there, historically reporting to Chris”

He discussed moving her into Sridhar Loke's commercialization organization and tied the role directly to use cases, adoption, governance, training and security. (transcript, September 1, 2026) citeturn1search675L184-L190

The TrackIt WAB deck separately names Brittany Pearce as “Product / Application” owner and jointly as an IT/technical owner. (document) citeturn1search605L2

## John Magee

The same WAB deck names John Magee under IT/Technical ownership. (document) citeturn1search605L2

Sean McCloskey described him as listed as a project manager but “part project manager, but part developer” for CSS implementations. McCloskey said John worked only with CSS and was CSS-funded. (transcript, September 1, 2026) citeturn1search675L191-L200

## Current handoff

No authoritative Microsoft 365 artifact was recovered documenting the current product-executive handoff to Darryl Benson. That information comes from the user and is not treated here as an independently retrieved enterprise fact.

---

# 4. Security, compliance and architecture

This is one of the best-documented areas.

## Encryption and BYOK

The Digital Products deck states:

> “Tenant level encryption was WAB approved September 2025 and implemented October 2025.”

It also states:

> “BYOK for AWS was WAB approved September 2025 and implemented October 2025 with Monday.com managed encryption keys.”

At the time of that deck:

> “The transition to Wesco managed encryption keys is underway, with completion targeted for the end of August.”

(document: `aug_deep-dive_engel-deck_digital-products-portfolio.pptx`) citeturn1search873L18

No later opened source was recovered proving that the transition completed. The target date should not be treated as completion.

Search terms: `BYOK Wesco managed encryption keys completed Monday.com`.

## File uploads and EECOL

The same source says CSS Sales and Services moved document management to SharePoint and:

> “File upload functionality in Monday.com was disabled on August 17, 2026, for all teams except EECOL.”

It explains that EECOL relied on monday.com for customer document management and that compliant alternatives were being evaluated. (document) citeturn1search873L18

The source also says an additional browser-isolation layer was being evaluated “to prevent unauthorized copy/paste of sensitive data.” (document) citeturn1search873L18

## Learning and Development tenant

The deck says Learning & Development had its own monday.com licenses and would migrate to Wesco's managed tenant. Tenant encryption, BYOK and MFA were to be enabled as part of that migration. (document) citeturn1search873L18

Nothing was found proving that the consolidation completed.

## Security assessments and accepted risk

The TrackIt WAB source records:

- Vendor Security Risk Assessment: May 29, 2026
- Cyber Solution Security Risk Assessment: June 22, 2026
- Risk 703 concerning customer guest accounts and local IDs, classified LOW, with MFA as mitigation and a statement that no exception was needed
- Risk 285 concerning authentication for ClockShark, Zapier and Google Drive

(document: `Monday.com - Tracket Integration - v0.3.pptx`) citeturn1search605L3

The same source classifies customer names, emails, addresses and identifiers, task assignments, sales and margin information, project descriptions, milestone dates, tasks and status updates as Confidential. (document) citeturn1search605L4

## SSO, SCIM, Entra, SIEM, DLP and residency

- SSO provisioning is explicitly evidenced in the access SOP. citeturn1search710L9-L14
- MFA is explicitly evidenced in the WAB risk material and L&D migration plan. citeturn1search605L3 citeturn1search873L18
- Nothing was found in opened evidence sufficient to establish SCIM configuration, Entra ID implementation details, SIEM export, DLP enforcement or exact data-residency geography.

Search terms: `SCIM Entra SSO MFA SIEM audit logging DLP data residency Monday.com`.

---

# 5. Integrations, apps and AI

## SharePoint

This is the clearest existing integration. On February 9, 2026, Kayla Steward wrote that her understanding was:

> “the only ongoing API connection with Wesco & Monday.com is related to file storage on SharePoint.”

(email: `Re: Monday.com API Connection Inquiry with USD/CRM`, February 9, 2026) citeturn1search635L246-L255

This is consistent with the later CSS document-management architecture using SharePoint rather than monday.com uploads. (document) citeturn1search873L18

## USD, CRM and DDP

The February email chain is important history.

Dhiraj Ranasaria said a CRM opportunity push/pull into monday.com could not be done ad hoc. The effort needed solution/API architecture, requirements with CRM and Solution Architects, an integration pattern, DEV and production WAB approval, and alignment with Wesco's MuleSoft integration pattern. (email, February 11, 2026) citeturn1search635L183-L195

On February 12, Sean McCloskey documented “No DDP release planned” for monday.com in 2026. He said the Monday-to-USD request was being evaluated and that, absent a compelling 2026 business case, the recommendation would likely be to wait until 2027. (email, February 12, 2026) citeturn1search635L138-L142

By late summer, the portfolio direction had become more affirmative:

> “Integrate Monday.com with DDP for task & workflow management tasks supporting customer requests that require professional services engagement.”

(document) citeturn1search873L17

This represents an evolution in the record. February says no 2026 DDP release; the later strategy says DDP integration is the intended direction.

## AI

The late-summer deck says:

> “Following AI Council guidance, we are no longer moving forward with Monday.com AI”

The source links that decision to monday.com's inability to disable file upload. The stated pivot was a “Copilot API integration,” allowing sales teams to access project updates through Wesco Copilot without additional monday.com licenses. (document) citeturn1search873L17

For the TrackIt production change, the WAB deck separately records “AI Council Review: N/A” and “AI Technical Review: N/A.” (document) citeturn1search605L5

Monday.com AI and the non-AI TrackIt capability should therefore not be conflated.

## Other integrations explicitly mentioned

- SharePoint: in use
- USD/CRM: evaluated or planned
- DDP: strategic roadmap
- MuleSoft: required Wesco integration pattern for the CRM/API work
- Zapier: named in a risk item
- Google Drive: named in the same risk item
- ClockShark: named in the same risk item

(document and email evidence) citeturn1search605L3 citeturn1search635L183-L195

Nothing was found substantiating implemented Monday integrations with Power BI, Power Automate, Jira, Planview or ServiceNow beyond ServiceNow/AssistMe being used for platform access requests.

---

# 6. How it is used

The platform is used more broadly than classic project management.

The Digital Products deck describes the main-use-case catalogue as:

- Resource and capacity planning
- Automated workflow and status management
- Task and work management
- Service-intake form management
- Marketing/Wrike replacement
- Sales-pipeline management
- Project management

(document) citeturn1search873L21

## Marketing

The `Marketing-Communications.aspx` intranet page says:

> “All Marketing Production requests must be submitted via monday.com forms listed on this page. Requests submitted via email or Teams will not be accepted.”

(document: `Corpmarketing / Site Pages / Marketing-Communications.aspx`) citeturn1search718L1-L8

It links a named “Marketing Production Workspace,” the SharePoint `Monday.com Platform Tutorials` library, login instructions, and specialized forms for:

- Campaigns and deliverables
- Images, supplier logos and Brandfolder
- Technical publications
- Canva templates
- External-communications approval

(document) citeturn1search718L14-L40

It also exposes a monday.com Report Issues form. (document) citeturn1search718L79-L85

## Technical Services and engineering

The TrackIt use case was designed to give engineering time and capacity visibility across “140+ globally distributed engineers,” with workload balancing, utilization, planning and forecasting. (document: `Monday.com - Tracket Integration - v0.3.pptx`) citeturn1search605L2

## CSS and services

The later strategic framing calls monday.com a “Foundational workflow platform supporting Technical Services and Supply Chain Services through standardized processes, cross-functional coordination, and scalable work management.” (document: `CSS_Digital_Products_Strategic_Update.pptx`) citeturn1search703L1

The forward-looking architecture is explicit: USD/CRM is the sales front door, and monday.com is the “services workflow and project execution layer.” (document) citeturn1search703L1

---

# History and governance trajectory

1. **June 2025:** A nine-platform tool comparison assessed functionality, scalability, complexity, user experience, integrations, cost effectiveness, AI readiness, and vendor support and reliability. monday.com was positioned as the task and workflow-management tool, alongside Planview for enterprise portfolio management and Jira for IT development. (document) citeturn1search873L17

2. **September and October 2025:** WAB approved tenant-level encryption and BYOK. Implementation followed in October, initially using monday.com-managed encryption keys. (document) citeturn1search873L18

3. **December 17, 2025:** The access SOP documents structured AssistMe provisioning and a separate business-use-case approval path for new teams. (document) citeturn1search710L23-L28

4. **February 2026:** USD/CRM integration demand surfaced. Solution Design required formal architecture, WAB and MuleSoft alignment. Digital Products documented no 2026 DDP release and leaned toward 2027 unless the business case justified acceleration. (email) citeturn1search635L138-L142 citeturn1search635L183-L195

5. **May and June 2026:** TrackIt underwent vendor and Cyber Solution security assessments. A WAB package documented Enterprise licensing, product and technical ownership, and risks. (document) citeturn1search605L2-L5

6. **August 17, 2026:** monday.com file uploads were disabled tenant-wide except EECOL. CSS had shifted document storage to SharePoint. (document) citeturn1search873L18

7. **Late summer 2026:** AI Council direction stopped the Monday.com AI path and redirected effort toward a Copilot API approach. (document) citeturn1search873L17

8. **September 1, 2026:** Leadership explicitly recognized that platform scale had outrun parts of the operating model. Sean McCloskey questioned governance for approving use cases, adoption measurement, training and security, and DDP migration while describing Brittany Pearce as the historical lead and John Magee as the CSS implementation resource. (transcript) citeturn1search675L184-L203

---

# Product-executive fact base

## Strong evidence

- Enterprise licensing and a three-year contract exist. citeturn1search605L2
- Adoption grew dramatically in 2026, but contemporaneous totals conflict. citeturn1search528L469-L471
- The most precise divisional allocation retrieved is CSS 485, Marketing 279, EES 168 and EECOL 30. citeturn1search873L17
- Chris Gazdic, Brittany Pearce and John Magee are central historical owners or operators, in distinct roles. citeturn1search873L17 citeturn1search605L2
- Governance exists, but leadership identified governance, adoption and support maturity as unfinished work. citeturn1search675L184-L203
- Security controls underwent substantial tightening in 2025 and 2026, especially encryption, BYOK and removal of file uploads. citeturn1search873L18
- AI Council stopped native Monday.com AI expansion and pushed toward Copilot integration. citeturn1search873L17
- The strategic target is increasingly clear: sales demand originates in USD/CRM; monday.com becomes the workflow and execution layer for services, eventually aligned with DDP. citeturn1search703L1

## Material diligence gaps

1. Executed contract, order form and amendments
2. Authoritative current license census versus purchased seats
3. Renewal date, notice deadline and total annual committed spend
4. monday.com account executive or CSM
5. Current admin and super-admin roster
6. Confirmation that Wesco-managed BYOK completed
7. Confirmation that L&D tenant consolidation completed
8. SCIM and Entra configuration, and SIEM or audit-log architecture
9. Current inventory of boards, workspaces, automations and integrations by business unit
10. Formal decision record establishing the current product-executive handoff

These are not assumptions or negative findings. They are items for which nothing authoritative was found in the opened evidence using searches including `contract order form renewal Guardian AI credits license users admins BYOK SCIM Entra SIEM L&D Monday.com`.
