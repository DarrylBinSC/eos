# Strev AI Use Cases: Product Position and Commercial Context

**Prepared for:** Lisa Orton
**From:** Darryl Benson, Senior Director, CSS Platforms
**Date:** 2026-09-15
**Purpose:** Supporting material for your 9/25 discussion with Greg's team, and context for the UiPath intake assessment of the two Strev AI use cases Amy is submitting.

---

## Why This Note

Your reply to Amy raised four things: getting the right product, architecture, security and support stakeholders engaged early; avoiding duplicated capability; deciding whether a capability belongs in the broader roadmap; and protecting Wesco IP. I agree with all four, and I want to give you the commercial and entitlement picture behind these requests so the assessment has something firm to work from.

One point up front, because it changes how the requests should be read. **These are not two feature requests. Based on the vendor's own commercial catalog, they most likely sit behind a platform-level AI licensing commitment that Wesco has not yet evaluated, budgeted, or contracted for.** That does not mean we should not pursue them. It means the intake assessors need to know what they are assessing.

---

## What Wesco Already Owns

Under the White Label Software License and Service Agreement (March 21, 2025, as amended 2025-08-13), WAM already includes meaningful capability that is easy to overlook when an AI request is on the table:

- Asset and license lifecycle management, entitlement tracking, and warranty and support management
- CSV and Excel bulk import and update, REST APIs, and API-based metadata pull from external systems
- Smart Repository document storage and post-signature contract tracking
- QR, barcode, OCR and ICR scanning, NFC and RFID, and Scandit-based label data extraction on the mobile app
- Alerting and notifications, audit trails, operational charts, geo-fencing and map views

Some of this is directly adjacent to what is being requested. Bulk import and update, and OCR and ICR label extraction, are contractually included today at no additional cost. That is worth establishing before we license anything new, and it is the first question I would want the assessment to answer.

---

## What the Two Requests Most Likely Are

Revnue's current commercial document for Wesco is *Feature Entitlements, Expansion Roadmap, and AI Feature Pack Pricing Framework*, version 2.5, May 2026. Mapping Amy's use case names against that catalog:

| Requested | Most likely catalog match | Status in the vendor's own document |
|---|---|---|
| Smart import | LLM-based Data Upload, under Enhanced AI/ML Data Import. Writes records into WAM. The vendor distinguishes it expressly from Metadata Extraction, which is read-only. | **In private beta.** Public beta targeted for Q3. **No published pricing.** Requires an active AI Feature Pack on the same tenant. |
| Data enrichment | No feature of that name appears in the catalog. The nearest capabilities are Document Metadata Extraction and Anomaly Detection. | Both sit inside the **AI Feature Pack**, which is a paid platform SKU, not an included feature. |

**This mapping is my assessment, not a confirmed fact.** Neither request uses a vendor SKU name, and I have asked Revnue to identify each by catalog name. I would not want the assessment to proceed on my inference alone.

The third opportunity in this thread, the Virtual Site Survey, does not appear in the vendor catalog at all.

---

## The Commercial Shape, and Why It Matters to Intake

Per the vendor document, the AI capabilities are structured as follows:

**The AI Feature Pack is the entry point.** $84,000 per year per environment, including 100 AI-enabled seats. Additional seats are sold only in blocks of 50 at $10,000 per block. Each activated tenant carries a separate minimum credit commitment of $10,000 per year, and those credit pools do not commingle.

**Every AI add-on requires it.** The six add-on capabilities, including LLM-based Data Upload, cannot operate without an active AI Feature Pack on the same tenant, and they draw from that tenant's credit pool. So a request that reads as one feature carries a platform commitment underneath it. The vendor's own illustrative scenarios range from $94,000 to $184,000 per year depending on tenant count and seats.

**Consumption cannot currently be modeled.** AI usage is metered in credits. The section of the document titled "Credit Definition and Conversion Rates" publishes no conversion rates, and states that there is at present no standard method to translate a credit into token usage. The practical effect: we can calculate the annual floor, but we cannot tell you what processing a given document volume will cost. Usage governance exists (thresholds, soft-stop, capped overage, and automatic pause on anomalous burn), and overage bills at 1.25 times the committed rate.

**None of this is under contract, and the vendor says so.** The document states that it does not constitute an offer, commitment or agreement, that its pricing is illustrative and subject to change, and that any expansion requires a written change order or amendment. Our contract as amended is silent on the AI Feature Pack, seat blocks, credit commitments, overage, and all six add-on SKUs.

**What this means for the intake assessment:** the two requests cannot be scoped or costed as discrete features. They should be assessed as the first two use cases of a platform decision, with the platform decision made explicitly rather than arrived at through accumulated feature approvals.

---

## Your Four Concerns, Directly

**Stakeholder engagement.** Agreed, and I would go further than the intake form. Architecture and security need to look at this because the AI Feature Pack includes a locally hosted open-weight model operated inside the WAM SaaS environment, plus optional per-tenant activation of Anthropic, OpenAI and Google Gemini models. That is a data-handling and model-governance question, not only a functional one. The vendor describes PII redaction and content guardrails under the existing Cybersecurity and Data Protection Addendum, and that should be verified rather than accepted.

**Duplication with the Wesco AI file ingestion work.** This is the right question and I do not yet have the answer. What I can tell you is what our record actually shows: discussions with the IDP team on AI-enabled document ingestion were opened and have not concluded, so no comparison has been done. I am not going to assert a distinction I cannot support. I will convene the comparison with the IDP team and bring you a written position, ideally before 9/25 so you are not presenting an open question to Greg's team. If the capabilities do overlap, the right frame is a build-versus-license decision with a cost on both sides, not a feature approval.

**Roadmap integration.** There is a sequencing issue worth knowing. Our own 2027 Digital Products priority list for Strev, dated 2026-09-02, covers bulk parent-child asset mapping, automated warranty end dates, tenant configuration cloning, and API modernization. **It contains no AI scope**, and it has not yet been communicated to the vendor, quoted, or financed for 2027. If an AI commitment is approved ahead of it, investment order is set by intake sequence rather than by product priority, and it is set before we know what our own stated priorities cost. I have added a quotation request against that list to the question set going to Revnue.

**Intellectual property.** Two distinct exposures, and I would separate them. On the inbound side, the vendor document states that any capability added by change order becomes a Service under the existing Agreement and inherits its IP, confidentiality, indemnification, insurance, escrow and right-of-first-refusal provisions. That is the protection we would want, and it holds, but only if these arrive through a change order rather than through an informal enablement. On the outbound side, your concern about the Wesco AI team's ingestion work is the one I cannot yet close, and it is bound up with the duplication question above. Any evaluation that involves showing Strev how our ingestion process works needs a defined boundary set before it happens, not after.

---

## Where I Agree With You Without Reservation

Your point that development capacity is genuinely constrained, and that leveraging a third-party capability is reasonable where the capability is truly unique, is correct and matches what I see across the portfolio. With DDP and the MDM governance work already competing for the same resources, building a second ingestion path ourselves would be a real cost. If the comparison shows Strev has something we do not, licensing it is the right answer. I want the comparison done so the decision is made on evidence.

I also support Amy putting these through UiPath. That is the right mechanism and it should proceed. My ask is only that the assessors receive the commercial context above, because a request assessed as a feature and a request assessed as the leading edge of a platform commitment will get different answers.

---

## What I Am Doing

1. Sending Revnue a written question list covering catalog SKU identification for both requests, credit conversion rates, the per-environment scope of the base license, and the conflict between their AI catalog and the 2027 priorities list. Target: this week.
2. Convening the comparison between Strev Smart Import and the Wesco AI team's ingestion work with the IDP team. Target: a written position before 9/25.
3. Confirming with Amy which vendor SKU each submission corresponds to, at our standing weekly, so the intake records the right thing.
4. Establishing with Finance where an AI commitment of this size would sit in the FY27 plan, since there is currently no Strev line in the WAM P&L.

---

## What Would Help From You

If the 9/25 conversation with Greg's team is the right forum, I would ask that it treat this as a platform and governance decision rather than a use case approval, and that it produce a named owner for the build-versus-license question. I can supply material or attend, whichever is more useful.

I am available any time this week and next, and I can turn around anything you need for the 9/25 deck on short notice.

---

*Sources: Revnue Corp, "Wesco Asset Management, Powered by StrevAI: Feature Entitlements, Expansion Roadmap, and AI Feature Pack Pricing Framework," v2.5, May 2026. White Label Software License and Service Agreement, March 21, 2025, as amended by Amendment No. 1 effective 2025-08-13. Strev 2027 AOP priorities list, provided 2026-09-02. Wesco internal WAM cost model.*
