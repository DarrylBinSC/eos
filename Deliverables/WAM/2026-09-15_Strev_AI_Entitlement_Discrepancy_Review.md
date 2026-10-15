# Strev AI and Entitlement Work: Discrepancy Review and Remediation Plan

**Date:** 2026-09-15
**Owner:** Darryl Benson
**Status:** Working analysis. Not for external circulation.
**Trigger:** Lisa Orton forwarded the Amy Aguirre AI use case thread (2026-09-15, 14:26) to Sean McCloskey, Chris Gazdic and Darryl, stating she intends to present to Greg's team by 9/25.

---

## 1. Source Set Reconciled

| # | Source | Date | Author | What it is | Standing |
|---|---|---|---|---|---|
| S1 | `Wesco_WAM_Entitlements_AI_Feature_Pack_v2_5.pdf` | May 2026, v2.5 | Revnue Corp | Entitlement clarification, expansion catalog, AI pricing framework | Vendor document. Explicitly non-binding. 16 pages. |
| S2 | `WAM_Pricing_Model_Deck_Wesco_LightCover.pptx` | Undated | Wesco (built outside the EOS) | 12-slide combined cost model and contract-gap analysis | Wesco internal analysis |
| S3 | `Strev_AI_Analysis_Context.md` | Undated | Darryl | Prompt that produced the original analysis of S1 | Instruction document, not evidence |
| S4 | `Strev_2027_Priorities.md` | Transcribed 2026-09-02 | Strev, via Darryl | Strev vendor product enhancement priorities for the FY27 AOP | Vendor priorities list |
| S5 | Amy Aguirre / Lisa Orton email thread | 2026-09-15 | Amy Aguirre, Lisa Orton | Two Strev AI use cases being submitted through UiPath intake | Current operational evidence |

**Reference agreement chain, as reconstructed:** White Label Software License and Service Agreement dated March 21, 2025 (Anixter Inc. as contracting entity), amended by Amendment No. 1 effective 2025-08-13, which redefined "Software Service" (§2.1) and replaced Exhibit A Section 2 with the core per-asset WAM price table (§2.3). S2 is the only source in the set that records Amendment No. 1.

---

## 2. What the Analysis Got Right

Before the discrepancies, the part of this work that holds up.

The arithmetic in S2 is sound. Tier 3 base of $36,000 plus 20,001 assets at $3.00 equals $96,003; Premium support at 30 percent equals $28,800.90; core total $124,803.90. Add-ons at $54,000 and AI at $114,000 sum correctly to the $292,803.90 headline. I checked every line.

The central contractual conclusion is correct and is the most valuable thing in the deck: **AI capabilities are New Commercial Features, sit outside the no-cost Update definition at §1.18, and can be added only by written change order or amendment under §14.5.** S1 states this in three separate places (§2 definitions, §4.2 Boundary, §5 preamble). The contract as amended is silent on all of it.

The six add-on SKU count is correct and matches S1 §5.4 exactly.

---

## 3. Discrepancies

Graded by consequence, not by how obvious they are.

### Tier 1: Material. Fix before anything goes to a VP or into a change order.

**D1. The deck marks AI pricing as "Confirmed." The source document disclaims it.**

S2 slide 8 lists under the ✓ Confirmed column: "AI base $84k/env, 100 seats; +50-seat blocks $10k" and "Tenant min $10k/yr; non-commingled; overage $1.25/credit."

S1 states, in its own Purpose and Status section: *"This document does not constitute an offer, commitment, agreement, or amendment, and creates no legal or contractual obligations on either party."* And in Forward-Looking Statements: *"Pricing, conversion rates, scenario examples, beta timelines, and roadmap items in this document are illustrative and subject to change. Final terms will be pinned in the applicable change order."*

The core platform pricing on that slide is genuinely confirmed, because it sits in Amendment No. 1 under contract. The AI pricing is a vendor proposal in a document that twice says it binds nobody. Putting both in the same column, under the same checkmark, is the single most consequential error in the deck. A VP reading slide 2 takes $292,803.90 as a real number. Roughly 39 percent of it is not.

*Fact, not interpretation: the quoted disclaimers are verbatim from S1.*

**D2. The "one open item" is the wrong open item.**

S2 slides 2, 7 and 8 identify a single AI assumption: "$1 = 1 committed credit, planning only, not confirmed."

S1 actually supports that rate in two places. §6.4 sets overage at "1.25× the committed-credit rate (i.e., $1.25 per overage credit)," which implies a $1.00 committed credit. §6.6 Scenario A states a $10,000 commitment as "(10,000 credits)." The dollar-per-credit basis is the least uncertain number in the model.

The real gap is one level down and the deck does not name it. S1 §6.3 is titled "Credit Definition and Conversion Rates" and publishes no conversion rates. It says: *"At present, there is no standard method to translate a single credit into a specific amount of token usage."* Yet S1 references "published per-feature conversion rates (see §6.3)" in at least five places (§2 Credit definition, §5.1, §5.4, §6.1, §6.2).

**Consequence: nobody can convert a business volume into a cost.** We cannot answer "what does processing 5,000 invoices a month cost in credits," and the vendor's own document says the method to answer it does not exist. The $94,000 floor is knowable. Expected spend is not. Overage exposure is unbounded in principle and governed only by the soft-stop controls in §6.4.

This matters directly for Amy's use cases, because ingestion volume is exactly what drives credit burn.

**D3. License Lifecycle Management: entitled or priced? The two sources disagree.**

S1 Part A lists a License Lifecycle Management module as **Included** under §1.16 and §2.1(a), covering License Allocation and Assignment Tracking, Alerts and Notifications, Entitlement Tracking, and Basic In-Platform Transactions (Extend, Transfer, Assign).

S2 slide 5 lists "License Management, $2 / license" under **AVAILABLE, NOT ENABLED**.

These cannot both be right. This is not a footnote. License and entitlement visibility is the core of the WAM value proposition, it is what the FY27 AOP case leans on, and it is the data layer that every AI use case in play is meant to serve. If it is entitled, we are understating what we already own. If it is priced at $2 per license, there is an unbudgeted variable cost sitting directly under the product's headline claim.

**D4. Part E of the vendor document does not exist.**

S1 §1 states the document is organized into five parts and describes *"Part E — Relationship to the Existing Agreement: how this document interacts with the Agreement, Exhibit A pricing, and other contractual obligations."*

The document runs 16 pages and ends at §6.8, which is the end of Part D. Part E is never written.

Part E is precisely the section that would govern precedence between this document and the Agreement, and it is the section Legal would read first. Its absence is either a production error or a deliberate omission, and we should not assume which.

**D5. The vendor's May 2026 document does not acknowledge Amendment No. 1.**

S1 cites only the March 21, 2025 Agreement, and states twice that nothing in it modifies Exhibit A. It never mentions Amendment No. 1, effective 2025-08-13, which per S2 slide 9 replaced Exhibit A Section 2 with the core per-asset price table.

So the vendor's current entitlement document is reasoning against an Exhibit A that was superseded nine months before the document was written. Either Revnue did not carry the amendment forward, or S2's characterization of Amendment No. 1 is imprecise. One of the two is wrong and we need the executed amendment to settle it.

**D6. An unfunded Wesco 2027 ask with no AI, alongside a vendor AI catalog moving through a separate channel.**

**Corrected 2026-09-15 after Darryl's direct input.** S4 is not Strev's roadmap. It is **Wesco's** 2027 Digital Products enhancement demand on Strev, and as of today it has **not been communicated to the vendor, not quoted, and not financed for 2027**.

S4 contains four items: bulk parent-child asset mapping, automated warranty end date calculation, tenant configuration cloning, and API modernization. **It contains no AI scope.**

S1, dated May 2026, is the vendor's own commercial catalog: a base AI pack, two further feature packs, and six add-on SKUs.

**The exposure is sequencing, not roadmap conflict.** Wesco's own stated 2027 product priorities carry no price and no funding line. Vendor-originated AI capability is meanwhile moving toward a funding decision through Managed Services intake. Approving the latter first sets investment order by intake sequence rather than by product priority, and does so before anyone knows what the former costs. The 09-02 reader's note already flagged that S4 carries no cost, effort or sequence; that gap is now load-bearing.

**Provenance limit.** Strev's original source document is not in the EOS. Every copy derives from the 2026-09-02 transcription. `Products/WAM/Strev_2027_Priorities.md` now records this.

### Tier 2: Real, and they will surface in a change order or a customer conversation.

**D7. "Field Services" names three different things.**

S2 slide 5 prices "Field Services w/ Mobile App (50 users)" at $16,000 per year, enabled now. S1 Part A lists the Mobile App module as Included at no fee, covering asset and document views, QR generation, QR/barcode/OCR/ICR scanning, NFC and RFID, Scandit label data extraction, basic maintenance scheduling, geo-fencing and offline mode. S1 §5.4 separately lists "StrevAI Agent for Field Services" as a private-beta AI add-on.

Three constructs, one label. In a change order this becomes an argument.

**D8. Work Orders appear in two commercial constructs.**

S2 prices a Work Order module at $24,000 per year (available, not enabled), and S1 Part A confirms "Simple Maintenance Flow, Included, Work Orders not in scope," which is consistent. But S1 §5.2 places "Automatic Work Order Creation" inside the Preventative Maintenance Feature Pack with pricing deferred to a future change order.

We need to know whether the $24,000 module and the PM Feature Pack's work order capability are the same thing sold twice, adjacent capabilities, or a superseded SKU.

**D9. Dedicated Cloud Hosting: fixed fee or pass-through?**

S2 carries Dedicated Cloud Hosting at a fixed $36,000 per year, enabled. S1 §4.4 states that non-production or additional environments beyond the standard production environment are handled under §2.2(c) *"on a direct-cost pass-through basis, subject to Wesco's prior written approval, and not counted toward standard fees."*

Different mechanisms. If Wesco's hosting is a fixed add-on under Amendment No. 1, S1 §4.4 does not describe our arrangement. If it is pass-through, the $36,000 line is an estimate, not a price.

**D10. "Per environment" is an uncosted multiplier on the AI base fee.**

The AI base license is $84,000 per year **per environment**. S2 models one environment. We separately carry Dedicated Cloud Hosting, and S1 §4.4 contemplates additional environments. Nobody has asked whether a non-production or dedicated environment triggers a second base fee. At $84,000 a copy, this is the largest single unpriced risk in the model.

**D11. Notification thresholds contradict inside the vendor document.**

S1 §5.1 states "mandatory 75% / 90% / 100% notification thresholds." S1 §6.4 states notifications at "50%, 75%, 90%, and 100%." S3 followed §6.4. Minor in substance, but this is exactly the class of detail that gets transcribed into a change order incorrectly.

**D12. The deck is named for a price but models a cost.**

S2 is titled "WAM Pricing Model" and assumes "Default margin = 0% (no white-label markup applied)." What it actually computes is Wesco's annual cost to Revnue. Under a white-label agreement where Wesco sublicenses to End Users under §2.2 and §2.3, our cost and our customer price are different numbers. A reader who sees "WAM Pricing Model" and "$292,803.90" and takes that as what we charge will be wrong.

**D13. A pricing cliff sits one asset away from the modeled scenario.**

The tier table prices Tier 2 (5,001 to 20,000 assets) at a $24,000 base plus $4.00 per asset, and Tier 3 (20,001 to 100,000) at $36,000 plus $3.00. The deck models 20,001 assets, which is one asset into Tier 3.

At 20,000 assets the same customer pays $135,200 all in with Premium support. At 20,001 they pay $124,803.90. **Adding one asset reduces the annual fee by $10,396.10.** The Tier 3 to Tier 4 boundary is far worse: 100,000 assets costs $436,800 with support, 100,001 costs $192,401.30, a drop of over $244,000.

This is a property of the supplier price list, not an error in the deck. But slide 12 presents the per-asset curve as a smooth decline, which it is not, and any customer-facing or internal sizing conversation that hits a tier boundary will produce an indefensible-looking number. Flagging it now is cheaper than discovering it in front of Finance.

### Tier 3: Record-keeping gaps in the EOS.

**D14.** `Products/WAM/WAM.md`, the front-door knowledge file, carries no pricing, no commercial model, and no mention of the AI Feature Pack. The largest open commercial question on the product is invisible in the product file.

**D15.** `03_Decision_Log.md` has no entry for the v2.5 document, the pricing analysis, or an AI Feature Pack evaluation. None of this work is in the decision trail.

**D16.** There is no Register A, B or C item for Amy's AI use case submissions, the UiPath intake, or Lisa's 9/25 presentation.

**D17.** Per the 2026-09-10 Sean deck revision work, no Strev line is visible in the FY27 WAM P&L, and there is no Strev entry in the FY27 AOP change log set while WAM, entroCIM, CDA and Navigator all have one. A commitment in the $94,000 to $184,000 per year range has no budget home.

**D18.** S3, the prompt behind the original analysis, instructs the model to describe "published per-feature conversion rates" and "different credit conversion rates" for multi-vendor models. Per D2, S1 publishes none. **Any analysis built from S3 inherits a false premise about the source document.** S3 should be corrected before it is reused.

---

## 4. The Amy Thread, Mapped Against the Entitlement Document

This is where the discrepancies stop being an archival problem.

Amy is submitting two Strev AI use cases through UiPath intake: **Data enrichment** and **Smart import**. A third, the **Virtual Site Survey**, was demoed to Lisa and Matt on 9/11 with a prototype demo the following Friday.

| Amy's name for it | Closest thing in the vendor's own catalog | Commercial status per S1 | Confidence |
|---|---|---|---|
| Smart import | LLM-based Data Upload, under Enhanced AI/ML Data Import (§5.4). Writes records into WAM, expressly distinct from Metadata Extraction, which is read-only. | **In Private Beta.** "Published in Q3: Public Beta." No pricing. Requires an active AI Feature Pack on the same tenant. | Probable, not confirmed |
| Smart import (alternative reading) | CSV / Excel Bulk Import and Update (Part A) | **Included today** at no additional cost | Possible. The ambiguity is the point. |
| Data enrichment | No feature of that name exists in S1. Nearest are Document Metadata Extraction and Anomaly Detection, both inside the AI Feature Pack base. | Requires the $84,000 base pack plus a $10,000 per-tenant credit commitment | Weak. "Data enrichment" is Wesco's own term from `Reference/AI_Strategy_and_Use_Cases.md` §2, not a Strev SKU name. |
| Virtual Site Survey | Not in S1 at all. | Unknown | None |

**Three findings follow, and they are the substance of what Lisa needs.**

First, **none of the three opportunities maps cleanly to a named, priced, generally available SKU in the vendor's own May 2026 commercial catalog.** Two map to private-beta add-ons with no published pricing. One is not in the catalog at all.

Second, **the closest match to Smart Import requires an active AI Feature Pack to operate at all.** Per S1 §5.4, every add-on SKU requires an AI Feature Pack on the same Authorized Tenant and draws from that tenant's credit pool. So a request that looks like a single feature is in fact a request to enter an $84,000 per year platform commitment plus a $10,000 per tenant credit minimum. Nobody in the thread has said that.

Third, Amy's email states these are use cases Strev "has built." S1 describes the closest analogues as In Private Beta with public beta targeted for Q3 and commercial terms to be published when each enters public beta. Built and commercially available are different claims. I am not questioning Amy's good faith; I am noting that the vendor's own document does not support treating these as available today, and the intake assessors will need that resolved.

---

## 5. Remediation Plan

Sequenced so the 9/25 date is protected. Nothing here blocks Amy's UiPath submissions, which Lisa has already authorized.

### Track A: Correct the record (Darryl, this week)

| # | Action | Fixes | Due |
|---|---|---|---|
| A1 | Rebuild S2 slide 8 to split Confirmed into "Under contract" (core platform, Amendment No. 1) and "Vendor proposal, non-binding" (all AI). Restate the $292,803.90 headline as "$178,803.90 under contract plus $114,000 proposed and unpriced on consumption." | D1, D12 | 2026-09-18 |
| A2 | Replace the "one open item" callout with the real one: no credit-to-work conversion rate exists, so expected AI spend cannot be modeled, only the floor. | D2 | 2026-09-18 |
| A3 | Rename the deck to "WAM Supplier Cost Model" and add an explicit line that no white-label margin is applied and these are not customer prices. | D12 | 2026-09-18 |
| A4 | Add the tier-boundary discontinuity to the scale slide, or move the scenario off the 20,001 boundary to a defensible mid-tier volume. | D13 | 2026-09-18 |
| A5 | Correct `Strev_AI_Analysis_Context.md` to state that §6.3 publishes no conversion rates, so the prompt does not keep propagating the error. | D18 | 2026-09-16 |

### Track B: Questions to Revnue/Strev (Darryl to Sunny Sharma or the account owner)

Send as one written list. Written answers, not a call, because these end up in a change order.

| # | Question | Fixes |
|---|---|---|
| B1 | Part E is referenced in §1 and absent from the document. Provide it, or confirm it was withdrawn. | D4 |
| B2 | v2.5 cites only the March 21, 2025 Agreement. Confirm whether Revnue has carried forward Amendment No. 1, effective 2025-08-13, and reissue the entitlement mapping against the amended Exhibit A. | D5 |
| B3 | Is License Lifecycle Management entitled under §1.16 and §2.1(a) as Part A states, or a priced module at $2 per license as the 2025-08-13 price list indicates? | D3 |
| B4 | §6.3 publishes no credit conversion rates. Provide per-feature credit consumption for at least Document Metadata Extraction and LLM-based Data Upload, on a per-document or per-page basis, for both Local LLM and frontier-model classes. Without it we cannot budget. | D2 |
| B5 | Does the $84,000 base license apply per environment including non-production and dedicated-hosting environments? State the total base fee for Wesco's actual environment footprint. | D10 |
| B6 | Reconcile the $24,000 Work Order module against Automatic Work Order Creation in the Preventative Maintenance Feature Pack. | D8 |
| B7 | Reconcile "Field Services w/ Mobile App" at $16,000 per 50 users against Mobile App listed as Included in Part A, and against StrevAI Agent for Field Services in §5.4. | D7 |
| B8 | Is Dedicated Cloud Hosting a fixed annual fee or a §2.2(c) direct-cost pass-through? | D9 |
| B9 | §5.1 and §6.4 give different notification thresholds. Which governs? | D11 |
| B10 | Confirm the current beta and pricing status of LLM-based Data Upload and of any feature Strev is presenting to Wesco as Data Enrichment, Smart Import, or Virtual Site Survey, and identify each by its catalog SKU name. | D6, §4 |
| B11 | Provide a quotation, with effort and sequence, against Wesco's 2027 Digital Products priority list (bulk parent-child asset mapping, automated warranty end date, tenant configuration cloning, API modernization). It has not yet been formally communicated or priced, and it must be costed before any AI commitment is sequenced ahead of it. | D6 |

### Track C: Internal, cross-functional

| # | Action | Owner | Fixes | Due |
|---|---|---|---|---|
| C1 | Establish whether the Wesco AI team's file ingestion work overlaps Strev Smart Import. Route through the IDP team discussion already open in the ADM context. This is Lisa's explicit question and it is currently unanswered in our record. | Darryl to convene; IDP team to assess | §4 | Before 9/25 |
| C2 | Retrieve the executed Amendment No. 1 and the 2025-08-13 price list into `Products/WAM/`, so entitlement questions stop being answered from a vendor summary. | Darryl | D5, D3 | 2026-09-19 |
| C3 | Establish where a $94,000 to $184,000 annual AI commitment would sit in the FY27 plan, given no Strev line is visible in the WAM P&L. | Darryl with Akansh Gangil and Finance | D17 | Before any change order |
| C4 | Confirm with Amy which Strev SKU each UiPath submission corresponds to, and whether Strev has represented them as generally available. | Darryl, at the standing weekly one-on-one | §4 | 2026-09-17 |

### Track D: EOS filing (this session)

| # | Action | Fixes |
|---|---|---|
| D-1 | Add an AI Feature Pack and commercial model section to `Products/WAM/WAM.md`. | D14 |
| D-2 | Log a Decision Log entry: AI Feature Pack commercial evaluation opened, decision not taken, dependencies named. | D15 |
| D-3 | Open Register A items for the Revnue question list (B1 to B11) and the Lisa brief, and a Register C item for Amy's SKU confirmation. | D16 |
| D-4 | Add a Watch List entry for unpriced AI consumption exposure with no budget home. | D17 |
| D-5 | Cross-reference `Strev_2027_Priorities.md` and the v2.5 catalog so the two-roadmap problem is visible from either file. | D6 |

---

## 6. What I Would Not Do

I would not delay Amy's UiPath submissions. Lisa authorized them and they are the mechanism that gets these assessed. The correction needed is not to the submissions but to what the assessors are told about commercial status.

I would not present the $292,803.90 figure to any audience until A1 is done.

I would not raise the "has built" versus "private beta" point as a challenge to Amy. It is a question for Strev, and it should be asked of Strev in writing.

---

## 7. Assumptions and Limits

- **Assumption:** the pricing deck reflects the 2025-08-13 supplier price list accurately. I verified its internal arithmetic, not its inputs, because the price list itself is not in the EOS.
- **Assumption:** Amendment No. 1 is characterized accurately on slide 9. The executed amendment is not in the EOS. C2 closes this.
- **Unknown:** whether Part E of v2.5 was ever written. Its absence is a fact; the reason is not.
- **Unknown:** the mapping from Amy's use case names to Strev SKU names. Section 4 gives the most probable mapping and labels the confidence. It is not confirmed.
- **Not assessed:** legal sufficiency of any contract language. This review identifies where the documents disagree; it makes no legal conclusion.
