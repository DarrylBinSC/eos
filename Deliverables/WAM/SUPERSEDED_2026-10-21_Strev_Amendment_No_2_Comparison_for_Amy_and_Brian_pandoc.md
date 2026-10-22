# Strev Amendment No. 2 (AI Features): What Changed and What It Costs

References are page and section in: the Draft (received 2026-10-21); the Agreement (White Label Software License and Service Agreement, 2025-03-21); Amend. 1 (2025-08-13); v2.5 (Revnue pricing framework, May 2026).

::: {custom-style="Bottom Line"}
**Key takeaway:** the draft defines the capability set as "AI Features" and prices it at $164,000 per Environment per year through two mandatory fees (AI Platform License, AI Feature Pack Base License); every internal number to date has used $84,000. It also changes the agreement's payment terms for these fees and charges every Environment, including QA, where the agreement treats non-production use as included.
:::

## 1. Financial changes

| # | Change | Before | Draft Amendment No. 2 | Effect |
|----|--------------|----------------------|------------------------|------------------|
| 1 | Second mandatory fee | One $84,000 base license per environment (v2.5 p. 13, §6.1); §6 states the earlier platform-fee model was retired. | $80,000 AI Platform License plus $84,000 AI Feature Pack Base License; both must be paid (Draft p. 4, Exhibit A table and term 1). | +$80,000 per Environment; a return to a fee layer the vendor said it had dropped. |
| 2 | AI usage paid by Wesco and its customers | Revnue credits, $10,000 minimum per tenant; Revnue-hosted local model at no token cost (v2.5 pp. 9-10, §5.1); usage statements per tenant (p. 15, §6.7). | No Revnue usage charge. Wesco must hold and pay its own OpenAI, Anthropic or Google account; no local model; no usage reporting (Draft p. 2, §2.12(b)). | Uncapped cost outside the contract; one Wesco account serves every tenant and End User, with no way to charge it back. |
| 3 | Support uplift | AI fees not addressed (v2.5 silent). | AI Fees count toward Annual Contract Value (Draft p. 4, term 5); Standard support is 20% of ACV, Premium 30% (Amend. 1 p. 4). | +$32,800 (Standard) or +$49,200 (Premium) per Environment. |
| 4 | Charged per Environment, QA included | Non-production use is part of the license; extra environments at direct cost only, outside standard fees (Agreement p. 3, §2.2(c)). | An Environment is any multi-tenant deployment, Provider- or Customer-hosted; each needs both fees (Draft p. 4, term 1). No carve-out for test or QA. | A second $164,000 plus support if AI is installed in QA; conflicts with §2.2(c). |
| 5 | Payment terms changed | Fees invoiced monthly in arrears, net 30 after an undisputed invoice (Agreement p. 6, §4.1); half of subscription fees drawn from the $500,000 prepayment (p. 16, Exhibit A §1.1). | AI Fees invoiced annually in advance, net 30 from receipt; no deduction from the prepayment (Draft p. 4, terms 2 and 3). | A change to the agreement's payment mechanics, not an entitlement change: a full year of cash at order; prepayment unusable. |
| 6 | Renewal price increases | Exhibit A prices fixed for the five-year term (Amend. 1 pp. 3-4); no escalator in the agreement. | Revnue may revise the AI Fees for any renewal on 90 days' notice (Draft p. 4, term 6). | First uncapped increase right in the relationship, from year two. |

## 2. Total financial impact

| Item | Previously assumed | Draft | Additional |
|-------------------------|---------------|----------------|----------------|
| AI Features license, one Environment | $84,000 | $164,000 | +$80,000 |
| Support on the AI Fees | Not modeled | $32,800 to $49,200 | +$32,800 to $49,200 |
| One Environment, year one | $84,000 | $196,800 to $213,200 | +$112,800 to $129,200 |
| QA Environment, if AI is installed there | Direct hosting cost only | $196,800 to $213,200 | +$196,800 to $213,200 |
| AI usage (OpenAI, Anthropic or Google) | Inside v2.5 credits, $10,000 per tenant minimum | Paid directly by Wesco; unsized | Unknown |
| Both Environments, year one | $84,000 | $393,600 to $426,400 plus usage | +$309,600 to $342,400 plus usage |

Ranges reflect Standard (20%) or Premium (30%) support. Year-one amounts are payable in advance at the order date, cannot be drawn from the prepayment, and are non-cancellable for the year.

## 3. Contract-term changes

| # | Term | Before | Draft Amendment No. 2 | Effect |
|----|--------------|----------------------|------------------------|------------------|
| 7 | Scope: ten capabilities | v2.5 base pack of five (pp. 9-10, §5.1); Preventative Maintenance and IoT were separate packs (p. 11); the chat assistant and LLM data upload were private-beta add-ons (p. 12, §5.4). | (a) Anomaly Detection; (b) Preventative Maintenance Scheduling; (c) IoT Features; (d) Document Intelligence; (e) AI-Based Asset Filtering; (f) Document Extraction to Contracts, Assets and Licenses; (g) Content Filtering; (h) AI Enrichment; (i) Strev AI natural-language assistant; (j) AI Bulk Import and Update (Draft p. 1, §2.2, new §1.19). | More in the bundle, which is part of the price. Downside: (c), (e) and (h) are undefined; the v2.5 guardrails and local model are not listed; the Software Service line reads "AI Features [(in development)]" (Draft p. 1, §2.1). |
| 8 | The features we asked for | Data extraction, data normalization and the Virtual Site Survey (Amy's three). | Data extraction maps to (f). Data normalization is not named; (h) may be it. The Virtual Site Survey is not in the draft at all. | Two of three unconfirmed; the site survey stays on its own pricing track. |
| 9 | Minimum term and exit | Convenience termination on 90 days' notice (Agreement p. 8, §9.2(d)); term ends 2030-03-21 (§9.1). | One-year non-cancellable, non-refundable minimum per Environment, then annual auto-renewal on 30 days' notice (Draft p. 4, term 4). | Convenience exit forfeits the year; nothing ties the AI term to the agreement's end date. |
| 10 | Liability on the AI leg | Provider warranty (Agreement p. 6, §5.2) and indemnity incl. data breach (p. 9, §10.1) cover the Services. | AI provider is Wesco's vendor, not a Subcontractor; no Revnue warranty or indemnity for its outages, data handling or output; no accuracy warranty on AI Output (Draft p. 2, §2.12(f), (g)). | Breach, data-protection and accuracy exposure sits with Wesco, and with its End User terms once AI is resold. |
| 11 | Kept | n/a | No training on Customer Data; AI Output is Customer Data; AI source code into escrow (Draft pp. 2-3, §2.12(d), (e), (h)). | Acceptable as drafted. |

My read-through points to potential effects on the FY27 AOP and the Strev renewal BIR that should be reviewed; I have not sized them here. The legal review is Brian's to lead; this document is a head start on what changed, not the review itself.
