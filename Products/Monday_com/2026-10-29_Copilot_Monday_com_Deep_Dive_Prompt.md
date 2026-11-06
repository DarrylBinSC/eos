# Copilot Deep Dive Prompt: Monday.com at Wesco

One-time prompt for Microsoft 365 Copilot. Paste as written. Save the result as `Evidence/M365_Evidence_MondayDeepDive_YYYY-MM-DD.md` and paste it into the EOS session; Claude routes it into `Products/Monday_com/Monday_com.md`, `06` and the registers.

```
Research everything available to me in Microsoft 365 about Wesco's use of Monday.com (also written monday.com, Monday, "Work OS"). Search all of it: email and sent items, Teams chats, channels and meeting chats, meeting recaps and transcripts, calendar, Planner and To Do, OneDrive, SharePoint sites and document libraries, Loop, OneNote, Viva Engage and the intranet. Look back 24 months. I have just been made the product executive for Wesco's use of Monday.com and I am building a complete picture of the platform, its contract, its users, its governance and its history. This is a one-time deep dive, not a status update.

RETRIEVAL RULES
- Say up front which sources you could and could not search, and which SharePoint sites and Teams you searched by name.
- A search snippet is not a retrieved document. Open each relevant document, thread or transcript and read it before quoting it. Mark each citation (email), (Teams chat), (transcript), (AI notes), (document: site/library/filename) or (calendar).
- Quote the words used. Give the author, date and source for every fact. Never infer a fact from a title alone; if only a title is visible, say so.
- Where sources conflict (two different license counts, two different renewal dates), report both with their dates and do not pick one.
- Absence is not evidence: if you find nothing on a topic, write "nothing found" and list the search terms you used.

WHAT TO FIND, in these sections

1. CONTRACT AND COMMERCIALS. Vendor agreements, order forms, quotes, renewal notices, invoices, purchase requisitions, procurement or VMO threads, and anything from monday.com's account team. Report: plan or tier (Enterprise, Guardian add-on, any other products such as CRM, dev or service), term, start and renewal dates, notice period, seat counts bought, annual cost, price per seat, AI credits or AI line items, any pricing-model change (seats plus credits), discounts, the Wesco contract owner and the vendor account manager or CSM, and any pending renewal activity.

2. LICENSES AND USERS. License counts and allocations by business unit, department or team (CSS, Marketing, EES, EECOL, Learning and Development, any others), member versus viewer versus guest counts, admin lists, any usage, adoption or active-user reports, requests for new licenses, and any reductions or reallocations. Note the date of every count.

3. OWNERSHIP AND ROLES. Who has owned Monday.com as a product executive, platform owner, administrator, super user or champion, and when. Include Chris Gazdic, Brittany Pearce and John Magee, and anyone else named. Governance bodies that have reviewed it (WAB, architecture or security review boards, AI Council, VMO), with dates and outcomes.

4. SECURITY, COMPLIANCE AND ARCHITECTURE. Tenant-level encryption, BYOK and key management (Monday-managed and Wesco-managed keys, including whether the transition completed), SSO and SCIM with Entra ID, MFA, audit logging to a SIEM, data residency, file-upload policy (the 2026-08-17 change and the EECOL exception), browser isolation, DLP, the managed-tenant consolidation of Learning and Development, security assessments, risk acceptances, exceptions and incidents.

5. INTEGRATIONS, APPS AND AI. Integrations in place or planned (DDP, SharePoint, Teams, Outlook, Power BI, Power Automate, Jira, Planview, ServiceNow, Zapier, API use), marketplace or custom apps, monday code, AI features in use (Sidekick, AI blocks, agents, vibe apps, AI workflows), who built them, and any AI governance decisions about Monday.com.

6. HOW IT IS USED. The processes and workflows each group runs on Monday.com, named boards or workspaces, templates, intake forms, dashboards and reports, and any statements of value, time saved, or dependency (for example EECOL customer document management, CSS sales and services workflows, Marketing campaign management). Include complaints, outages, support tickets and requests to replace or consolidate the tool.

7. HISTORY AND DECISIONS. The June 2025 evaluation of nine platforms and its criteria and outcome; the project tool stack decision (Planview, Jira, Monday.com, QPM and FTTX); any decision to expand, restrict or retire Monday.com; prior business cases; AOP or budget lines; and the Digital Products Portfolio reviews and Deep Dive decks that covered it (including the August 2026 Deep Dive for John Engel).

8. PEOPLE. Every person who appears in connection with Monday.com with their role as stated in the source, grouped into: owners and admins; business-unit leads and champions; IT, security and procurement contacts; vendor contacts.

9. OPEN ITEMS AND DATES. Anything undecided, overdue, pending approval, or dated in the next six months: renewal, key transition, EECOL alternative, L and D migration, DDP integration, Elevate '26 follow-ups.

10. COVERAGE STATEMENT. Which sources were searched and read, which could not be opened (with the error), the search terms used, and a count of items found per section. Then a short list of the five most important documents found, with their locations, so I can open them directly.

FORMAT. Concise Markdown, one table per section where the content is tabular (Fact | Source | Date | Author), prose otherwise. Quote exactly; do not paraphrase figures. Flag anything older than 12 months as (dated). Do not summarize my day-to-day activity and do not include unrelated search noise; if a search returned mostly noise, say so in the coverage statement.
```

Notes for the session that processes the result:
- The baseline, daily and weekly prompts in `02_Copilot_Intake_Prompts.md` list Monday.com as out of scope. Once Sean confirms the ownership, move it to the in-scope product list in all three prompts and add the product to the attribution and connection tests; until then the deep dive is the only Monday.com intake.
- Route Durable rows to `Products/Monday_com/Monday_com.md`, people to `06`, dated items to the registers under `product: "Monday.com"`.
