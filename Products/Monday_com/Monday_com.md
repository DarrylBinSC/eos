# Monday.com (Wesco's use of the platform)

As of: 2026-10-29 (owners named; August Deep Dive slides filed). Added to Darryl's portfolio verbally by Sean McCloskey on 2026-10-29 (Darryl direct). Previously a Run product with Chris Gazdic as Product Executive on the August 2026 Digital Product List (`Products/digital-products-portfolio-aug26.pptx`). Reference and planning material only; decisions in `03`, risks in `04`, actions in `Registers/`.

## What is known

- Sean McCloskey told Darryl he will add Wesco's use of Monday.com to Darryl's product portfolio (verbal, 2026-10-29).
- On the August 2026 Digital Product List, Monday.com is one of five Run products; Chris Gazdic is Product Executive for it, eProcurement and Prokeep.
- The record holds nothing else on Monday.com as a product: no user base, licensing, renewal date, vendor contact, administration owner, FY27 AOP line or roadmap.

## Owners (Darryl, 2026-10-29)

- **Brittany Pearce**, Senior Manager - Portfolio, Digital Products and Business Models (org chart screenshot, 2026-10-29): Monday.com owner. The chart shows her under Jim Lenart (Manager - Agile Practice, Agile Transformation), who sits under Chris Gazdic (Senior Director - Product Executive, Digital Products and Business Models, 24 reports). Reporting chain read from the chart's display order; confirm.
- **John Magee**, Senior Developer, Brittany's one direct report: Monday.com owner with her.
- Both are at a Monday.com conference the week of 2026-10-26 (Darryl); first contact after they return.

## Wesco's deployment, as presented in the August 2026 Deep Dive for John Engel (slides 17-18, Product Executive Christopher Gazdic; images in this folder)

**Usage (slide 17, "Monday.com Usage"):** 962 licenses across four groups: CSS 485 (50%), Marketing 279 (30%), EES 168 (17%), EECOL 30 (3%). CSS is the largest user by a wide margin; Darryl's own business unit is already the main consumer of the platform he is inheriting. Date of the count not stated on the slide (deck is August 2026).

**Place in the project tool stack (slide 17):** Planview for enterprise portfolio management (Project Place and Agile Place interfaces); Jira for IT software development, with key metrics to be tracked to DDP deliverables; **Monday.com for task and workflow management**; QPM and FTTX for transactional project and job management. A June 2025 evaluation of nine platforms (functionality, scalability, complexity, user experience, integration, cost, AI readiness, vendor support and reliability) sits behind this stack; the evaluation itself is not in the record.

**DDP plan (slide 17):** integrate Monday.com with DDP for task and workflow management supporting customer requests that require professional services engagement. Status not stated.

**Data and security (slide 18):**
- Tenant-level encryption: WAB approved September 2025, implemented October 2025.
- BYOK for AWS: WAB approved September 2025, implemented October 2025 with Monday.com-managed keys; transition to Wesco-managed keys underway, completion targeted end of August (2026).
- Data protection: CSS Sales and Services moved document management to SharePoint, removing the need for file uploads in Monday.com; **file upload disabled 2026-08-17 for all teams except EECOL**; EECOL still relies on Monday.com for customer document management, alternatives being evaluated; a browser-isolation layer against copy/paste of sensitive data is under evaluation.
- Managed tenant consolidation: the Learning and Development team's separate Monday.com licenses are to migrate into Wesco's managed tenant, with tenant-level encryption, BYOK and MFA enabled as part of the move.

Open from these slides (status as of August, nothing newer in the record): whether the Wesco-managed-key transition completed; whether EECOL has a document-management alternative; whether the L&D migration happened; whether the DDP integration started; what the 962-license commercial agreement is (term, renewal date, cost).

## Not yet stated (Darryl to confirm with Sean or Chris)

- Whether Brittany and John move with the product into Darryl's organization, or stay under Jim Lenart and Chris Gazdic with Darryl as Product Executive only.

- Effective date.
- What ownership covers: platform administration, licensing and renewal, the internal product-executive role, or all three.
- Handover from Chris Gazdic, and whether Chris knows.
- FY27 AOP treatment (Run cost line, and under whose budget).
- Why it moves: the reason shapes how Darryl positions it (a Run product consolidating under CSS Platforms, or a platform with a product agenda).

## Monday.com added to Darryl's portfolio (added 2026-10-29)

Lead: Sean McCloskey said he will add Wesco's use of Monday.com to Darryl's product portfolio; verbal, scope and timing not stated.

Source: Darryl direct, 2026-10-29, after a verbal update from Sean on the products he owns.

- Filed in `01` Portfolio Scope, `03` Decisions Made (2026-10-29), `06` Sean McCloskey and Chris Gazdic.
- Same day, Darryl: owners are Brittany Pearce and John Magee; both at a Monday.com conference this week. Added to `06`.
- Same day, Darryl: slides 17-18 of the August 2026 Deep Dive for John Engel filed (usage by group, tool stack, DDP plan, security program). File moved into `Products/Monday_com/` with the slide images.

## Company and product research brief filed (added 2026-10-29)

Lead: a sourced brief on monday.com the company, the product and pricing model, competitive position, extensibility and what ownership means at Wesco is filed as `2026-10-29_Monday_com_Company_and_Product_Brief.md` in this folder; it closes with first-90-day questions and eight questions for Brittany Pearce and John Magee on their return from Elevate '26.

Source: Claude research, 2026-10-29 (public sources as of that date; Elevate '26 items secondhand pending a vendor release).

- **Vendor state (Reported):** $1.4B revenue run rate, 22% growth in Q2 2026, $1.07B cash, Gartner CWM Leader 2026; in the same year a 20% workforce cut (July 2026), withdrawn 2027 target, securities class action, and a move from per-seat to seats-plus-AI-credits pricing (May 2026) that existing customers migrate onto over "a couple of years." Q3 results due 2026-11-09.
- **What it means for Wesco (Claude's assessment):** vendor viability is not the risk; the risks are a renewal that moves the 962 licenses onto consumption pricing without caps, AI agents and vibe apps spreading without governance, and Monday.com drifting into a task list that free Planner could replace. The DDP integration planned in August will run into API limits (25K calls/day on Enterprise) and the absence of native Power BI/Power Automate connectors.
- **First facts to establish:** tier (Enterprise plus the Guardian add-on is inferred from BYOK and tenant encryption, not confirmed), term, renewal date, annual cost, legacy versus credits pricing, AI and API usage.
- Elevate '26: 2026-10-28/29, Javits Center, New York; "monday Frontier" (managed services plus deployment engineers) reported from the investor Q&A.

## Copilot deep-dive prompt and designed brief (added 2026-10-29)

Lead: a one-time Copilot deep-dive prompt for Monday.com across Wesco's M365 estate is filed in this folder (`2026-10-29_Copilot_Monday_com_Deep_Dive_Prompt.md`, also indexed as section 6 of `02`); the research brief was reflowed for the Word pipeline the same day (callouts, tables with Source Notes, bracketed source tags, Sources section, one Mermaid diagram of the license model kept on Darryl's review; a tool-stack diagram and a history timeline were drawn and dropped as not adding clarity; update the table of contents on open) and also exists as a four-page designed PDF-ready version (Claude Design artifact "Monday.com Executive Brief": bottom line and vendor numbers, license model diagram, Wesco tool-stack diagram with the DDP constraint, date timeline and first-90-day plan).

- The daily, weekly and baseline Copilot prompts still list Monday.com as out of scope; change that once Sean confirms ownership.

## Copilot deep dive: three-year Enterprise contract, AI Council stopped Monday.com AI, USD/CRM front door with Monday.com as the services execution layer (added 2026-10-29)

Lead: the one-time Copilot deep dive (`Evidence/M365_Evidence_MondayDeepDive_2026-10-29.md`, 24-month window) establishes that Wesco is on a three-year Monday.com Enterprise contract, that the AI Council has already stopped native Monday.com AI in favor of a Copilot API route, and that the stated architecture is USD/CRM as the sales front door and Monday.com as the services workflow and project execution layer.

Source: Copilot deep dive, 2026-10-29. Documents it opened: `aug_deep-dive_engel-deck_digital-products-portfolio.pptx`, `Monday.com - Tracket Integration - v0.3.pptx` (Graham Russ, WAB, 2026), `Monday.com SOP for Access.docx` (Brittany Pearce, 2025-12-17), `CSS_Digital_Products_Strategic_Update.pptx`, `Re: Monday.com API Connection Inquiry with USD/CRM` (email, February 2026), Digital Products / Agile Staff Meeting transcript 2026-09-01, `Corpmarketing` intranet page.

- **Contract (Durable, Reported):** "Monday.com Enterprise investment," "currently on a 3-year contract" (TrackIt WAB deck). A capacity-planning add-on was quoted at $3.25 per user per month for 250 users, $9,750 a year, prorated to "about $26,812.50 total" for the contract remainder. Claude's arithmetic: $26,812.50 / $9,750 = 2.75 years remaining when the deck was written (May or June 2026), which puts the contract start around the first quarter of 2026 and the renewal around early 2029. Inference, not a found date. Not found: the executed agreement, order form, renewal date, notice period, annual value, per-seat rate, Guardian, AI credits, CSM or account executive.
- **Licenses (Reported, conflicting):** 144 "at the beginning of the year" to "850 or so" (Sean McCloskey, 2026-09-01), corrected in the same meeting to "just over 1000" (Chris Gazdic). The August deck's 962 (CSS 485, Marketing 279, EES 168, EECOL 30) is the only itemized count. No member/viewer/guest/admin census found.
- **Access model (Durable):** Brittany Pearce's SOP (2025-12-17): requests through AssistMe (ServiceNow), SSO, 24 to 48 hours to provision, viewer role `Monday.com_Viewer`; a new team needs a "Business Use Case for approving Monday.com for your team."
- **Ownership (Reported):** Sean McCloskey, 2026-09-01: "Brittany has been the lead there, historically reporting to Chris"; he discussed moving her into Sridhar Loke's commercialization organization and tied the role to use cases, adoption, governance, training and security. John Magee: "part project manager, but part developer" for CSS implementations, CSS-only and CSS-funded. The TrackIt WAB deck names Brittany as Product/Application owner and both as IT/technical owners. Sean's 2026-09-01 concerns, named: governance for approving use cases, adoption measurement, training, security, DDP migration. No artifact records the handoff to Darryl.
- **AI (Durable, decided by others):** August deck: "Following AI Council guidance, we are no longer moving forward with Monday.com AI," tied to Monday.com's inability to disable file upload at the time; the pivot is a "Copilot API integration" so sales teams reach project updates through Wesco Copilot without additional Monday.com licenses. This retires the "agents and vibe apps spreading" risk as framed in the 2026-10-29 research brief; the live AI question is the Copilot route and what the vendor's credit model does at renewal.
- **Security (Durable):** Vendor Security Risk Assessment 2026-05-29 and Cyber Solution SRA 2026-06-22 for TrackIt; Risk 703 (customer guest accounts and local IDs, LOW, MFA mitigation, no exception) and Risk 285 (authentication for ClockShark, Zapier, Google Drive). Data on the platform classified Confidential (customer identifiers, sales and margin, project detail). BYOK transition to Wesco-managed keys and the L&D tenant consolidation: no completion evidence found. SCIM, Entra detail, SIEM export, DLP, residency: nothing found.
- **Integrations (Durable):** the only API connection is SharePoint file storage (Kayla Steward, 2026-02-09). CRM/USD push-pull requires solution architecture, the MuleSoft integration pattern and DEV and production WAB approval (Dhiraj Ranasaria, 2026-02-11). Sean, 2026-02-12: "No DDP release planned" for Monday.com in 2026, likely wait until 2027 absent a compelling case; the August deck then states DDP integration as the direction. Nothing found for Power BI, Power Automate, Jira, Planview or ServiceNow beyond AssistMe access requests.
- **Use (Durable):** catalogue in the August deck: resource and capacity planning, automated workflow and status, task and work management, service-intake forms, Marketing (Wrike replacement), sales-pipeline management, project management. Marketing: all production requests must go through Monday.com forms (`Marketing-Communications.aspx`, Corpmarketing). Technical Services: TrackIt for time and capacity visibility across 140+ engineers. CSS strategic update: "Foundational workflow platform supporting Technical Services and Supply Chain Services."
- Routed: `06` (Brittany Pearce, John Magee, Sridhar Loke, Graham Russ, Kayla Steward, Dhiraj Ranasaria); research brief and designed brief corrected the same day.

## Audit pass on the research brief (added 2026-10-29)

Lead: an independent audit of the brief after the Copilot deep dive was folded in found it fit to send after 14 corrections, none changing the conclusions; all were applied, and the audit is filed as `2026-10-29_Monday_com_Brief_Audit.md` in this folder.

- 36 public figures re-checked against primary URLs: 32 matched; one stock figure was wrong ($317 called the 52-week high; the page gives $210.49) and the "80% below peak" figure was stale (about 70% at the 2026-10-28 close); both corrected in the brief and the designed pages.
- Two unsourced Wesco details removed from the designed tool-stack diagram (Planview sub-products, Jira metrics to DDP).
- Inferences restated as inferences: the vendor "pushes toward" consumption pricing at renewal rather than migrating the contract; the AI Council stop is a decision, not a technical control, and its stated reason (file upload could not be disabled) was addressed on 2026-08-17, so it may be revisited; the security program is "largely executed," not complete; the three-year contract and its inferred early-2029 end are flagged as unconfirmed against the order form.
- Decision rights: commercial terms are now "with Procurement" (no Wesco contract owner was found); the August deck's naming of Chris Gazdic as Product Executive is stated in the brief.

## Chris Gazdic handover meeting brief filed (added 2026-11-03)

Lead: a meeting brief for Darryl's handover conversation with Chris Gazdic (scope, people, contract, open items, eight questions for Chris, proposed next steps) is filed as `Deliverables/Monday_com/2026-11-03_Chris_Gazdic_Monday_com_Meeting_Brief.md` (.docx alongside).

Source: Claude, 2026-11-03, from this file, the 2026-10-29 research brief and audit, and `06`.

- No new facts; the brief consolidates the record. Outcomes of the meeting to be filed here and in `03` / `06` when Darryl reports them.
