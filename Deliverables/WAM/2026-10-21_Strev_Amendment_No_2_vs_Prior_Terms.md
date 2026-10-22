# Strev Amendment No. 2: What Changed Against the Prior Terms

**Date:** 2026-10-21
**Owner:** Darryl Benson
**Status:** Working analysis for the Legal review (Brian Miller). Internal.
**Documents compared:** White Label Software License and Service Agreement (2025-03-21); Amendment No. 1 (effective 2025-08-13, executed 2025-09-16); Revnue entitlement and pricing document v2.5 (May 2026, non-binding); draft Amendment No. 2 (received 2026-10-21).

::: {custom-style="Bottom Line"}
**Bottom line:** the draft is more expensive than anything previously quoted, and the reason is structural, not a price increase on a known line. It adds a second mandatory fee, an $80,000 AI Platform License, that no prior document carried. It removes the included local model, so every AI call now runs on a third-party account Wesco pays for directly. And it charges per Environment in a way that conflicts with the base agreement's treatment of non-production environments. The scope also grew: three capabilities v2.5 priced separately are now inside the bundle. Both halves of that trade need to be priced before anyone accepts the $164,000.
:::

## 1. Your read is right: both fees are required, and that is new

Exhibit A of the draft, term (1): "both must be paid for an Environment for the AI Features to be made available in that Environment." The AI Platform License ($80,000) is the fee for the right to use and sublicense Revnue's proprietary AI technology. The AI Feature Pack Base License ($84,000) is the fee for the ten listed features. Neither is optional on its own.

No prior document has an $80,000 platform fee. Revnue's v2.5 framework quoted a single $84,000 base license per environment. Its §6 states that this single-fee structure "replaces the prior per-feature per-user platform fee model and the prior three-layer (Platform Fee / Vendor Token / Managed-Service Fee) consumption model." Amendment No. 2 reintroduces two of those three layers: a Platform Fee, and a Vendor Token layer now paid by Wesco directly. That is a reversion to a model the vendor itself said it had abandoned, and it is worth saying so in the negotiation.

| Item | v2.5 (May 2026) | Amendment No. 2 (draft) |
|---|---|---|
| Platform license | None | $80,000 per Environment per year, mandatory |
| Feature Pack license | $84,000 per environment per year, 100 seats included | $84,000 per Environment per year, no seat concept |
| AI consumption | Revnue credits, $10,000 minimum per tenant, overage 1.25x; included a local model with no token cost | No Revnue charge; Wesco pays OpenAI, Anthropic or Google directly, uncapped, no local model |
| Seats | 100 included; +50 for $10,000 | Not mentioned (reads as unlimited users) |
| Tenants | Priced per Authorized Tenant | Unlimited within an Environment |

::: {custom-style="Source Note"}
Source: v2.5 §5.1 and §6.1; Amendment No. 2 §2.3 (new §2.12) and Exhibit A terms (1) and (4).
:::

## 2. The arithmetic

On Revnue's own line only, v2.5 cost $84,000 plus $10,000 per Authorized Tenant. Amendment No. 2 costs $164,000 flat. The two meet at eight tenants. Below eight, the draft is more expensive; Wesco's v2.5 planning scenarios ran one to five tenants ($94,000 to $184,000, the top figure including 175 seats and heavy credit commitments). For the tenant counts actually discussed, the draft costs more.

Three costs sit outside the $164,000 and were either inside v2.5 or absent from it:

- Third-party model usage. v2.5 credits covered the model cost and offered a Revnue-hosted local model with no external token charge as the default. The draft has no local model (§2.12(b) makes a third-party account a condition of use) and Wesco pays that provider directly. Unsized; no budget line exists.
- Support uplift. Exhibit A term (5) adds the AI Fees to Annual Contract Value for support: 20 percent (Standard) is $32,800 a year; 30 percent (Premium) is $49,200. v2.5 was silent on this.
- Renewal increases. Term (6) lets Revnue revise the AI Fees for any renewal term on 90 days' notice, with no cap. The base agreement fixes its Exhibit A prices for the five-year term with no escalator; this is the first discretionary increase right in the relationship.

Realistic first-year cost for one Environment at Standard support is therefore $196,800 plus model usage, against the $84,000 that has been carried in every internal number to date, including Amy Aguirre's FY27 AOP request.

## 3. The scope grew, which partly explains the price

The draft's AI Features list (new §1.19) absorbs three things v2.5 priced separately and adds two names v2.5 did not use.

| Amendment No. 2 feature | Status in v2.5 |
|---|---|
| (a) Anomaly Detection | In the base pack |
| (b) Preventative Maintenance Scheduling | Separate PM Feature Pack (§5.2), "not included," unpriced |
| (c) IoT Features | Separate IoT Feature Pack (§5.3), unpriced, third-party costs passed through |
| (d) Document Intelligence | In the base pack |
| (e) AI-Based Asset Filtering | Not named |
| (f) Document Extraction to Contracts, Assets and Licenses | In the base pack ("Document Metadata Extraction") |
| (g) Content Filtering | In the base pack |
| (h) AI Enrichment | Not named |
| (i) Strev AI natural-language assistant | Conversational AI add-on SKU (§5.4), private beta, unpriced |
| (j) AI Bulk Import and Update | "LLM-based Data Upload" add-on SKU (§5.4), private beta, unpriced |

Three things from v2.5 are missing from the draft and should be asked about by name. First, the Revnue-hosted local model. Second, the "Safety, PII, and Content Guardrails" (prompt-level redaction and output filtering, which v2.5 tied to Exhibit D compliance). Third, the remaining add-ons (StrevAI Agent, Field Services Agent, AI Vision, AI Device Failure Prediction), which stay unpriced and outside this amendment.

Against Amy's three requirements: data extraction is covered by (f). Data normalization has no named match (possibly (h), not stated). The Virtual Site Survey is absent, which confirms it stays on its own pricing track and is not part of this amendment.

**The "(in development)" qualifier.** §2.1 adds the AI Features to the Software Service list as "8. AI Features [(in development)]," with the qualifier in brackets. Work Orders and Workflows carried that label in Amendment No. 1. If it stays, Wesco would be paying $164,000 a year for a line the agreement itself marks as in development. The §5.2(i) conformance warranty, which the draft ties to "the Documentation," would then have nothing firm to attach to. Documentation for each of the ten features should be referenced in the amendment before signature.

## 4. Conflicts and gaps against the base agreement

These are the points for Brian Miller, in the order they matter commercially.

**Environment definition versus §2.2(c).** The draft defines an Environment as "a single multi-tenant deployment of the Software Service, whether hosted by Provider or by Customer," and requires a separate $164,000 for each one. The base agreement §2.2(c) grants non-production use for testing, development and training as part of the license. Additional environments are charged only as direct-cost pass-through, approved in writing, and expressly excluded from standard fee calculations.

Wesco runs a QA environment today. As drafted, testing the AI features in QA would cost a second $164,000. The amendment should either exclude non-production environments from the Environment definition or state that §2.2(c) governs them.

**Dedicated End User environments.** Exhibit A prices a "Dedicated" tier for End Users. If a dedicated deployment is an Environment under the new definition, every dedicated-tier customer carries its own $164,000 before Wesco can resell AI to it. That would end the resale case for that tier. Needs an explicit answer.

**Invoicing: annual in advance, outside the prepayment.** Base §4.1 invoices Software Service fees monthly in arrears, with payment due 30 days after an undisputed invoice and completion of the service, and a right to withhold disputed amounts. Exhibit A term (2) replaces that with annual billing in advance for the AI Fees, and term (3) bars any deduction from the $500,000 subscription prepayment Wesco made at signing. Two effects: cash goes out a year ahead rather than monthly behind, and the prepayment balance (whatever remains of it) cannot be used.

Ask for the current balance before accepting term (3).

**Non-cancellable year versus §9.2(d).** The base agreement gives Wesco termination for convenience on 90 days' notice. Term (4) makes each Environment's AI Fees non-cancellable and non-refundable for a one-year minimum. Convenience termination survives in form but forfeits the year. The carve-out "except where the Agreement expressly entitles Customer to a refund" does preserve the §5.2 and §9.3(a) refunds on Revnue's breach, which is correct and should be kept.

**Term alignment.** The base agreement runs to 2030-03-21. The AI term starts on payment and auto-renews annually with 30 days' non-renewal notice. Nothing makes it coterminous with the base agreement; a renewal could fall after the agreement expires. Add co-termination.

**Liability shift to Wesco's own AI account.** §2.12(f) makes the AI provider Wesco's vendor, not a Subcontractor, Subprocessor or Provider Personnel. It removes Revnue's §5.2 warranty and §10.1 indemnity (including §10.1(v), data breach) for anything arising from that provider. §2.12(g) adds that Revnue does not warrant AI Output accuracy.

This is a defensible structure given the keys are Wesco's, but it moves three things onto Wesco: the data-protection terms with the model provider (Exhibit D does not reach that leg), the breach exposure for WAM data at that provider, and any accuracy claims from End Users. Wesco's own End User terms will need to cover all three before AI is resold.

**Token cost recovery with no reporting.** Because Wesco's keys serve every tenant and End User, Wesco carries the model cost for all of them. v2.5 §6.7 provided monthly per-tenant, per-feature usage statements; the draft provides nothing. Without usage reporting by tenant, Wesco cannot charge the cost back or detect runaway consumption. Ask for per-tenant usage reporting and the configurable caps v2.5 §6.8 listed.

**Points that are right and should stay.** §2.12(d), no training on Customer Data or AI Output; §2.12(e), AI Output is Customer Data; §2.12(h), Revnue-owned AI source code goes into the §12 escrow; §2.12(i), provider-caused outages as Excluded Downtime is reasonable and matches Exhibit B §1.4's existing third-party exclusion.

## 5. What to take into the negotiation

::: {custom-style="Decision Required"}
**Decision required:** whether to open the negotiation on structure (one fee, not two) or on price (the $80,000). Owner: Darryl, with Amy Aguirre on the budget side, before Brian Miller's markup goes back to Revnue.
:::

Three asks, in priority order:

1. Remove the AI Platform License or fold it into a single fee, citing v2.5's own statement that the platform-fee model had been retired. If Revnue holds the two-fee structure, the $80,000 needs a stated basis.
2. Fix the Environment definition: non-production environments governed by §2.2(c); dedicated End User deployments either excluded or priced as a schedule, not at $164,000 each.
3. Price the trade: confirm what IoT Features, AI Enrichment and AI-Based Asset Filtering actually are, confirm the guardrails and a local model option are still included, and cap renewal increases (CPI or a fixed percentage) through 2030-03-21.

Secondary: per-tenant usage reporting; co-termination; the current prepayment balance; the "(in development)" qualifier; Documentation references for all ten features; confirm "Anixter Inc." remains the correct contracting entity.

---

Editorial notes: the base agreement's Exhibit A was read as replaced by Amendment No. 1 for the fee table, with §1 (prepayment) still in force. No figure here is from any source other than the four documents named at the top; the eight-tenant break-even and the support uplift are arithmetic on those figures, not vendor statements. The v2.5 add-on SKUs are still unpriced, so no comparison was possible for the items now bundled in (b), (c), (i) and (j).
