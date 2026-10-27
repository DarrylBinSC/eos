# JCI Airwall MSP Agreement: Wesco Markup Positions

Date 2026-10-23. Prepared for Darryl Benson ahead of the JCI response review. Summarizes the Wesco markup sent to JCI on 2026-08-31 (Brian Miller redline of the OpenBlue Airwall MSP Reseller Agreement, "AXE Edits 8.31.2026") against JCI's template, so each JCI response can be checked against what we asked for. Rows are coded (T, F, L, Q) for reference in the meeting. JCI's response has not been reviewed; nothing below reflects their position.

::: {custom-style="Bottom Line"}
**Bottom line:** the markup asks for seven things that carry the deal value: hosting rights on Wesco systems, 60-day change notice with a termination-and-refund remedy, a 4% annual price cap with firm prices on accepted Orders, 120-day payment terms, removal of the customer flow-down and JCI third-party-beneficiary rights, mutual liability and a narrowed indemnity, and Wesco IP ownership. The licensing mechanics (pool, pay-on-provisioning, monthly in arrears, true-down) are still in Exhibit B and the MSP Program Materials, which JCI can change unilaterally.
:::

::: {custom-style="Decision Required"}
**Decision required in the meeting:** which asks are walk-away terms (hosting rights, licensing mechanics locked in the agreement text, price cap) and which are tradeable (Territory, payment days, audit scope). Owner: Darryl, with Brian Miller on the legal text.
:::

## 1. Terms Wesco changed

| Ref | Term | JCI template | Wesco markup (08-31) | Why it matters |
|-----|------|--------------|----------------------|----------------|
| T1 | Hosting rights | Use limited to "Hosted" offerings; deploy limited to "Non-Hosted" | Both qualifiers struck, so Wesco may use and deploy all JCI Offerings on Reseller or Customer systems; Exhibit E MSP definition covers "hosting OB Airwall Software on its own systems" | Contractual basis for the Wesco-hosted Conductor in Azure |
| T2 | Product changes | JCI may change or remove features at any time, no liability | 60 days' notice; if materially adverse and unresolved within 60 days, Wesco may terminate affected Orders on 30 days and receive a refund of prepaid fees | Protects the entroCIM deployment base from EOL or feature removal |
| T3 | Pricing | 30-day notice on price lists and increases | 60-day notice; increases capped at 4% per year; prices on accepted Orders firm for the Subscription | Caps exposure on a decade-deep sole-source dependency |
| T4 | Payment | Due 30 days from invoice | Due 120 days; first year invoiced for the full year term, then monthly (see Q1) | Cash terms; the first-year clause needs confirming |
| T5 | Customer terms | Wesco must bind each Customer to the JCI Customer Agreement, evidence it on request, indemnify JCI for any failure; JCI is third-party beneficiary of every Reseller Customer Agreement; customer early termination owes JCI the remaining-term fees | All struck. JCI Customer Agreement and Terms of Service attached as fixed Exhibits C and D (not web links); customer early-termination reimbursement limited to Advisory Services costs | Customers never touch Airwall in the hosted model; removes a per-customer paper and indemnity burden |
| T6 | Competing products | Reseller may not sell competing products during the Term | Struck | Keeps the connectivity layer substitutable |
| T7 | Liability | Cap is one year's payments; Reseller indemnity and customer-agreement failures carved out of the cap; Non-JCI Product liability capped at $10,000, one-way | Cap is amounts paid or payable under the Agreement, mutual; Reseller indemnity carve-out removed; Non-JCI Product liability mutual and capped at amounts paid | Symmetry; removes uncapped exposure on Wesco's side |
| T8 | Indemnity | Broad Reseller indemnity | Replaced with a narrow IP indemnity (MSP Bundled Offering infringes a patent or registered copyright), stated as Reseller's sole indemnification obligation | Matches JCI's own IP indemnity to Wesco |
| T9 | Term and exit | Auto-renew with 30-day non-renewal notice; 90-day convenience termination, JCI only on FCPA | 180-day non-renewal notice; 180-day convenience termination either Party; FCPA termination mutual; repeat-breach termination excludes immaterial payment delays | Longer runway to migrate customers if the relationship ends |
| T10 | Reseller IP | Silent | New clause: Wesco owns all software, tools, dashboards, integrations, configurations and workflows it creates, including those that interface with JCI Offerings | Protects entroCIM IP at the Airwall boundary |
| T11 | Data and security | Silent | JCI to comply with Wesco's Data Privacy, Protection and Cyber Security Requirements (wesco.com/supplierterms), incorporated by reference | Needed before WAB approves the metering API connection |
| T12 | Other | Territory US and Canada; audit of all books, documents and materials; Reseller must maximize JCI distribution | Territory global; audit limited to books and records, five-year lookback; marketing obligation struck; Anixter Inc. named as Reseller; order of precedence now ranks Exhibits A, B, E, D, C above the Order and Program Materials | Housekeeping, but precedence matters (see L1) |

## 2. Licensing mechanics (Exhibit B, the deal value)

| Ref | Item | Where it sits | Status in the markup |
|-----|------|---------------|----------------------|
| F1 | Pool grant, provision and revoke at will, fees on highest monthly Concurrent Licenses, invoiced monthly in arrears | Exhibit B, unchanged JCI text | Present but references the MSP Program Materials for fee detail |
| F2 | Development environment free of charge for the subscription | Exhibit B 1(c), Wesco insertion | New ask |
| F3 | Metering API: read-only license usage from the Conductor, Reseller may not disallow access | Exhibit B 2 and Exhibit E | Brian's comment stands: technical detail on API access needed for Wesco cybersecurity (WAB) |
| F4 | Conversion of the existing estate (prepaid balances, pool transfer at current count, older hardware eligibility, effective date) | Not in the markup | Gap. Darryl's 09-17 position: the whole estate converts at signature |

## 3. Lead-in for the review (Brian)

| Ref | Point |
|-----|-------|
| L1 | Durability: F1 mechanics live in Exhibit B plus the Program Materials; the Program Materials remain unilaterally changeable and rank last in precedence. Ask that Exhibit B state the mechanics in full, or that the Program Materials cannot alter fee structure. |
| L2 | JCI support obligations to Wesco (L3, escalation, SLA on the Conductor software): the markup only asks for a copy of the SLA for incorporation. Still the one open element of the responsibility matrix. |
| L3 | Non-cancelable Orders and non-refundable fees (3(b)) were left standing; the only relief is the T2 product-change remedy. Confirm that is intentional. |
| L4 | Exhibit B 1(f) Subscription Management: Brian's comment "what does this mean?" is unanswered; it lets JCI require Wesco to adopt new processes and tools via Program Materials. |
| L5 | Tariffs: open comment on whether purchases are subject to tariff; 05-26 decision was that Wesco absorbs tariff impact. |

## 4. Questions to settle before or in the meeting

| Ref | Question |
|-----|----------|
| Q1 | T4 first-year full-term invoicing is a Wesco insertion. Does it reflect the conversion of existing prepaid orders, or does it undercut the monthly-in-arrears thesis for year one? Confirm with Brian. |
| Q2 | 180-day EOL notice (05-26 decision) is not in the markup as a distinct term; T2 gives 60 days plus a remedy. Is that sufficient? |
| Q3 | Who is JCI's counsel on this response? Brian has not had a named counterpart. |
