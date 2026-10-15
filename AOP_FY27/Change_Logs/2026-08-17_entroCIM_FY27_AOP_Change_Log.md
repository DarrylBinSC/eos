# entroCIM FY27 AOP Demand Collation Template — Change Log and Open Items

**Live submission file:** `Products/entroCIM/COPY_entrocim_build_it-demand-collation-template.xlsx`
**This log documents work performed on:** `Products/entroCIM/SUPERSEDED_2026-08-17_entrocim_op-2027_it-demand-collation-template.xlsx` (with its original-state backup `..._ORIGINAL.xlsx`)
**Date:** 2026-08-17

> **Read this first (added 2026-08-18).** The analysis in this log — the P&L reconciliation, the loss finding, the sales-cost finding, the B18 re-basing, the Value KPI design — applies to the entroCIM FY27 submission and remains current. The *file* the edits were made in does not.
>
> On 2026-08-17 at 17:11 Darryl rebuilt the submission from a fresh `build_it` template and pasted content across. That rebuild is the live submission file. The `op-2027` working file these edits were made in is retained as `SUPERSEDED_`, so the reasoning survives without two files competing to look current.
>
> **Three items flagged in the rebuild on 08-18 and not carried forward here:** Investment Type reads `Non DDP: Applications`, which is not a valid value for that field (New / Carryover only); B23 lost the closing paragraphs carrying the commercial-cost framing and the improving trajectory; and D18 states costs are FY26-based while B18 carries the FY27 P&L figure. Darryl reviewed these on 08-18 and elected not to change them. Section 8 below has the detail.
**Source:** 2027 entroCIM Profit & Loss (DRAFT), provided as a screenshot; Finance revenue range $5M to $6M confirmed 2026-08-17.
**Submission gate:** 2026-08-21, four days out (Register A19).

Companion: `Deliverables/WAM/2026-08-17_WAM_FY27_AOP_Change_Log.md`. Several findings are common to both submissions.

---

## 0. Superseding update, 2026-08-18

Darryl added one split India resource (0.5 FTE) and the P&L hours basis moved from 1,800 to 1,880. **The figures throughout sections 1 to 4 below are the 08-17 state and are superseded.** Current state:

| | 08-17 | 08-18 |
|---|---|---|
| DEV FTE | 6.60 | **7.10** |
| DEV gross labor | $663,120 | **$713,272** |
| **B18** | $857,052 | **$877,732** |
| Gross margin | 48.8% | **47.3%** |
| Net revenue | ($897,778), -18.0% | **($982,960), -19.7%** |
| Breakeven | $6,840,403 | **~$7,079,000** |
| Sales cost exceeds GM by | $100,694 | **$175,846** |

**Two consequences.** The hours-basis move eliminates the $29,472 reconciliation residual this log documents in section 4; the P&L and the form now agree exactly. And the sales-cost finding gets stronger, not weaker: zeroing DEV *and* Marketing together now still leaves a $175,846 loss. Breakeven is now $1,079,000 above the top of the authorised range.

The reasoning in this log stands. Only the numbers moved.

## 0b. B6 Key Stakeholders added, 2026-08-18

B6 was **empty** on the live file. It carried "CSS" on the superseded `op-2027` working copy and was cleared in the 08-17 rebuild. Now populated from `Products/entroCIM/entroCIM.md` Key People plus the governance and dependency fields already on the form:

> CSS Digital Products & Business (Sean McCloskey); entroCIM Delivery, Release and Architecture (Ron Snyder); entroCIM Product (David Blondel); Deployment and Migration (Chad Steger); Commercial and Go-to-Market (Nathan Kehr); CSS Finance and Sales Operations (Tom Boss); DCOE (Balachandar Murali); Competitive Intelligence (Michael Wassil); Platform (Merwan Mereby); Digital Innovation Center (Sanjay Varier); CSS/TSS Managed Services (Brad Stevens); ecoInsight (3rd party vendor); SkyFoundry (ecosystem partner)

Dirk Naylor is not repeated here; he is named in B3 as Business Sponsor. Kevin Cochran (BAE) was excluded as a customer contact rather than an investment stakeholder.

**CSS/TSS Managed Services (Brad Stevens) is included deliberately.** `entroCIM.md` carries "Managed Services ownership ambiguity" as a standing risk pattern, and Darryl confirmed on 08-18 that Managed Services sits with the CSS/TSS business under Brad Stevens. Naming it on the form closes that ambiguity where a reviewer would look for it.

## 0c. B34 and B35 corrected, 2026-08-18 (Darryl)

**B35 3rd Party Solution: `N/A` replaced.** This was the identical error corrected on WAM. `N/A` asserted that no third-party solution is involved, while B33 named ecoInsight as a third-party vendor two rows above it, and SkySpark sits beneath the entire product. Now:

> SkySpark, a commercially licensed data and analytics platform from SkyFoundry, provides the database, time-series management, semantic modeling and fault detection layer beneath entroCIM. The entroCIM user experience, dashboards and application workflows are built on Wesco's own software framework above it. ecoInsight is engaged as a third-party development vendor.

**The wording is deliberate and matches a correction already closed elsewhere.** The 08-05 commercialization review (v10 slides 2, 11, 49) established the approved way to describe this relationship: SkySpark is licensed, not open-source, and the user experience and application workflows are Wesco's own framework built above it. Phrases like "powered by SkySpark" or "open IoT platform" were removed from that deck deliberately. B35 now uses the same construction, so the AOP form and the commercialization material describe the architecture identically. Naming SkyFoundry here is consistent with B6, which already lists it as an ecosystem partner.

**B34 In-house or Outsourced Resources: three FY26 spelling errors corrected** (`Exisiting`, `Depdencies`, `Outsource`), and the cross-portfolio dependencies now carry their owner names to match B33. Same correction applied to WAM on 08-17.

All three fields now agree with each other and with Scoring B26 (`Yes` on work dependencies).

## 0d. ecoInsight removed, 2026-08-19 (Darryl)

Darryl took the ecoInsight contractor off the project. The vendor resolves to **Ashray Hebbar, Engineer-Software, India, Contractor**, and he appears on **entroCIM Build lines only** in `CSS_Platform_Team.xlsx` (Detail1 r15/r44, Headcount r28, Scenarios r23).

**No financial impact.** He was already carried at 0 FTE, so entroCIM DEV stays at 7.10 FTE and $713,272 gross labor. **B18 remains $877,732.**

Four fields cleared of the reference:

| Cell | Change |
|---|---|
| B6 | ecoInsight dropped from the stakeholder list |
| B33 | ecoInsight bullet replaced with SkyFoundry (SkySpark platform licence), which is the dependency that actually persists |
| B34 | Now reads **"Outsourced: none. Delivery is internal for the investment year."** |
| B35 | ecoInsight sentence removed; the SkySpark and SkyFoundry description stands |

**B34 changed meaning, not just wording.** The field asks whether the work can be completed with internal resources only. With ecoInsight gone the honest answer is yes, and the form now says so. That is a stronger position than it looks: it removes an external delivery dependency from a submission whose scoring already carries Execution Risk at Medium.

**Delivery consequence, resolved 2026-08-19.** Hebbar was one of two developers assigned 07-30 to the entroCIM UI/UX inconsistency and table redesign work, alongside Harsha E. **Darryl confirmed Harsha E as owner**, and the work is deliberately not being re-staffed: UI/UX effort is to be focused elsewhere as Claude Design support arrives at Wesco. Register B28 updated accordingly.

**Related and already captured: the new Product Owner headcount.** Darryl is requesting an additional Product Owner for entroCIM. It appears in the headcount model as `entroCIM Build / DEV / Product Owner / NEW / 0.5 FTE / India / $22` (Headcount r43) and **is the same split India resource added on 08-18**. It is therefore already inside DEV 7.10 FTE, gross labor $713,272, and B18 $877,732. No further uplift is pending, and the submission does not understate the ask.

## 1. The finding that matters most

**entroCIM plans a 2027 loss of $897,778 at −18.0% net margin, and cannot reach breakeven anywhere inside the Finance-authorised revenue range.**

| Revenue | Gross Margin @48.8% | Net Revenue | Net margin |
|---|---|---|---|
| $5,000,000 | $2,439,080 | ($897,778) | −18.0% |
| $5,500,000 | $2,682,988 | ($653,870) | −11.9% |
| $6,000,000 | $2,926,896 | ($409,962) | −6.8% |

Breakeven at the current cost structure and margin requires approximately **$6,840,403**, which is $840,403 above the top of the range.

**The loss is a sales-cost problem, not a development-cost problem, and the P&L proves it arithmetically.** Sales cost of $2,539,774 is 50.8% of revenue and *exceeds* gross margin of $2,439,080 by $100,694. The plan is negative before Marketing and DEV are counted at all.

- Eliminating the entire DEV line still leaves a loss of **$600,694**
- Eliminating DEV *and* Marketing still leaves a loss of **$100,694**

This is the numerical form of the point already in `03` from 08-05: reducing delivery capacity in response to a commercial-conversion problem treats the symptom. The CSS Sales headcount-reduction request cannot fix this P&L, and the $857,052 requested on this form is not what is driving the negative margin. That framing is now in B23 and is the strongest honest defence of the investment request.

**Trajectory is improving and should be said out loud.** The 08-05 model showed revenue $4,800,000, gross margin 47%, net ($1,212,954) at −25.0%. This model shows revenue $5,000,000, gross margin 48.8%, net ($897,778) at −18.0%. The loss narrowed $315,176 and margin improved 7.0 points on roughly 80% revenue growth over 2026 actuals (implied 2026 base about $2,777,778).

## 2. Carried deliberately: the value-path contradiction

**Darryl's decision 2026-08-17: keep the Financial Benefits path as-is and flag, rather than move to Value KPIs.**

The exposure, stated plainly so it is not discovered rather than declared: the form claims the **Financial Benefits** path, the highest-priority category, and Scoring B10 asserts `1 Year < Payback < 5 Years`, against a submission-year plan that loses $897,778 and does not break even at any point in the authorised revenue range. A reviewer holding the form and the P&L together will find this quickly.

Neither B10 nor the value section was changed. B23 does state the modelled loss factually, because that is what the Pro-Forma field is for and understating it would be worse than the contradiction. The mitigation available if challenged is the trajectory plus the sales-cost finding above: the loss is narrowing, and the investment being requested is not its cause.

**Resolved differently, and better, later the same day.** Rather than switching paths, Darryl directed that the Value KPI block be populated *alongside* the Financial Benefits section. The template instructs populating one of three value sections; carrying two is a deliberate deviation and a defensible strengthening, because it means the value argument does not rest solely on a financial case the P&L does not support. If a reviewer challenges the payback claim, the KPI block carries the case rather than the submission having nothing behind it. This materially reduces the exposure described above without giving up the higher priority band.

## 2a. Value KPIs (B26, B27, B28) — added 2026-08-17

**Final state: four KPIs, 134 words, quarterly cadence, materialization 12-2027.** Arrived at across four passes; the reasoning for each is below because the reductions were substantive, not cosmetic.

**Design constraint, and the thing that shaped the whole set:** entroCIM deploys both as Wesco-hosted Azure instances and on customer premises. Airwall connects customer sites to Wesco-hosted cloud; on-prem does not use it. Arcbeam and customer-supplied VPN give services and support a path into on-prem, but that is a support path a human uses when there is a reason to, not an automated metrics pipeline. Any KPI that assumed continuous portfolio-wide telemetry would have been undeliverable.

Measurement tiers used:

| Tier | Source | Available |
|---|---|---|
| Always | Wesco licensing and commercial systems | Points licensed, sites, renewals, expansion |
| Wesco-hosted | Azure platform telemetry | Availability, ingestion, polling, alarm/FDD events, function usage |
| On-prem | Arcbeam / VPN, periodic | Same data, pulled at support touchpoints |
| Customer participation | Agreed baseline per engagement | Energy, cost, plant efficiency |

**The four KPIs, as submitted:**

| # | KPI | Measure | Measurement source |
|---|---|---|---|
| 1 | Licensed point utilization | % of licensed points in active service; target 80%+ | Licensing + hosted telemetry |
| 2 | Platform availability and data continuity | Monthly uptime, against the Managed Services service level | Hosted telemetry |
| 3 | Functional adoption depth | % of sites using 3+ of five core functions (alarming, FDD, KPIs, dashboards, reporting) | Hosted telemetry + on-prem sampled |
| 4 | Installed-base retention and expansion | Renewal rate on licensed points; net points added | Wesco licensing and commercial systems |

Rationale: KPI 1 is the leading indicator, since utilization precedes renewal and expansion. KPI 2 matters most for a platform running day-to-day operations including alarming, where availability *is* the value. KPI 3 covers the functional range in a single number and predicts renewal. KPI 4 closes the commercial loop without straying into the financial-benefits claim.

**KPI removed before submission (Darryl, 08-17): operational outcome at optimization engagements**, which would have measured plant efficiency or energy reduction against an agreed baseline, referenced to the Federal Reserve Bank chiller plant.

Darryl's reasoning, and it is the right call: Wesco may not have the ability to share customer results, and he will not promise what he cannot certainly deliver. Adding it later puts the submission ahead; committing now and failing to report creates a credibility problem in the first reporting cycle.

**The structural consequence is that the set is now entirely self-measurable.** Every remaining KPI is sourced from Wesco licensing systems or platform telemetry. The removed KPI was the only one in the customer-participation tier, meaning the only one whose measurement depended on permission Wesco does not hold. Nothing in the committed set requires a customer to agree to anything. That materially raises the probability that all four are actually reported in 2027, which is the point of a KPI commitment.

The trade is real and worth stating: this was also the only KPI that would have demonstrated value in dollars. The set now proves adoption, reliability and durability rather than financial outcome. Given that the Financial Benefits section is carried in parallel, that division is coherent, but it does mean the KPI block no longer independently answers "what is the customer getting worth."

**Decisions taken (Darryl, 08-17), in sequence:** report against stated coverage rather than committing portfolio-wide, so no new product scope is created; measure availability against the Managed Services service definition rather than naming a number on an AOP form; remove the Dell reference; remove the customer-outcome KPI entirely.

**Deliberately excluded, and why it matters:**

- **WAM and Ascent Navigator integration, and Wesco optimization and facility management services.** The record is explicit that no WAM production data flow exists today and it must be shown as roadmap only. A 2027 KPI on it would be project execution, not post-production performance, which is what the field asks for. B26 states these join the set when the integrations reach production.
- **AI-enabled analytics**, per the 2026-07-24 decision to keep AI out of AOP text and proforma and position it verbally as upside.

**B26 tightened across four passes (Darryl, 08-17):** 284 words, then 180, then 169, then 134.

The second pass compressed each KPI to one line. The third removed what still read as analysis rather than specification:

- **Dell reference removed** at Darryl's direction. The 380,000-point / 80% figures may be baked into KPI definitions later, but naming the account on the form was premature. The 80% target survives on its own; a target does not need to cite its derivation on a submission.
- **Causal framing removed from the opening.** "Each reported with its coverage denominator, because measurement access differs between Wesco-hosted and customer-hosted deployments" explained the reasoning behind the design. Replaced with "reported with stated coverage," which states the condition without arguing for it. The coverage paragraph still carries the substance; it just no longer justifies itself.
- **Verb voice shifted** from process description ("Baselines established," "report continuously") to specification ("Baselines are established," "cover... where connectivity allows"). Reads as a definition rather than a plan being worked out.

Kept: the Federal Reserve Bank reference in KPI 4. Darryl approved naming both customers earlier and only directed Dell's removal. It serves a different purpose from the Dell anchor, being an example engagement rather than a numeric baseline, and it is a one-line deletion if he wants consistency.

**Voice lesson, third instance this session.** The same defect appeared in the WAM B23 draft, the entroCIM B23 draft, and now B26: analytical register leaking into submitted fields. The pattern is specific and worth naming, since it is not verbosity but *justification* — explaining why a choice was made, inside a field whose only job is to state the choice. Reinforces `Reference/Communication_Preferences.md` §3b; the rule there has been extended to cover causal framing and verb voice.

**Em dash sweep, both files.** Separators in the KPI list were em dashes, which cut against the standing preference in `Reference/Communication_Preferences.md`. Replaced with colons, and every field authored this session across both submissions was swept: WAM D18, entroCIM B26, B37 and D18 also carried them. Zero remaining.

**B27 Target Measurement Cadence: `Quarterly`.** Matches executive reporting rhythm. Monthly would be operationally useful but over-commits to an AOP audience.

**B28 Expected KPI Materialization Timeline: `12-2027`.** Baselines established Q1 2027, first quarterly report Q2 2027, targets materializing by year end. Consistent with B24 Expected Benefits Timeline of 2027-12-31.

**Open item this creates.** Committing to portfolio-wide reporting on KPIs 1 to 3 would require on-prem instances to report telemetry back, a capability that may not exist today. The current wording avoids that by stating coverage instead. If broader coverage becomes desirable, containerization — now the mandatory deployment model — is the natural place to carry a reporting agent, and that would be FY27 scope rather than a reporting convention.

## 3. Changes applied

| Cell | Field | Was | Now | Basis |
|---|---|---|---|---|
| B18 | Total Investment Cost | $1,437,918 | **$857,052** | Re-based to the P&L. See section 4 |
| D18 | Notes | "Does not include COGs" | Full reconciliation; the COGS exclusion is retained and was correct | |
| B8 | Investment Type | `M&A` | `Carryover` | **Invalid value corrected.** The valid list is New / Carryover only; `M&A` belongs to the Strategic Program list in B7. The cell carries two overlapping validations in the template, which is how the wrong value got in |
| B16 (Scoring) | Implementation Cost | `$1-5 million` | `< $1 million` | Follows the re-based B18 of $857,052 |
| B34 | In-house or Outsourced | `Yes` | Prose answer naming in-house team, DIC, Platform, and ecoInsight | `Yes` did not answer the question asked. Content taken from B33 |
| B37 | Links & Attachments | `N/A` | 2027 entroCIM P&L, CSS Platform Team P&L Analysis 2027, Commercialization decks, FY27 AOP Findings Import Package | |
| B23 | Pro-Forma Forecast | Template instruction text | Range, sensitivity, trajectory, and the commercial-cost framing. 179 words, executive register | Was never populated; the field still held its own guidance text. Rewritten for voice per Darryl 08-17 — see below |

**Note on B23 voice.** The first draft of this field was written in analytical register and read as notes to Darryl: instructions to himself ("confirm with Tom Boss"), reasoning chains, and meta-commentary about the analysis. Rewritten to 179 words for a reviewer audience, structured as basis, outcome, what it means for the decision, qualifications. The same correction was applied to the WAM submission. Rule captured to `Reference/Communication_Preferences.md` §3b: the form is executive-ready, the log is candid, and they do not share a voice. The analysis removed from the field is retained in section 1 of this log.

## 4. B18 re-based: $1,437,918 → $857,052

The prior figure was **$774,798, or 116.8%, above the governing plan.** The P&L plans DEV at 6.60 FTE (3.50 India, 3.10 North America) for gross labor of $663,120. The form carried a 16.15 FTE roster, 9.55 FTE above plan.

**Correcting my own earlier read:** I initially inferred the form was mixing COGS/SERV resources into an investment request as a category error. Darryl's own D18 note said "Does not include COGs," so the *intent* was already correct. The failure is roster staleness, not a category mistake, though the roster did carry individuals the P&L treats as COGS/SERV (the 08-05 reconciliation named Clark, Papanna and Reed).

New figure, per Darryl's direction 08-17 to use DEV only and to include Other IT Expense:

| Component | Amount |
|---|---|
| 3.50 FTE India × $22/hr × 1,880 hrs | $144,760 |
| 3.10 FTE North America × $94/hr × 1,880 hrs | $547,832 |
| **Labor subtotal** | **$692,592** |
| Other IT Expense (per P&L) | $164,460 |
| **Total** | **$857,052** |

The **$29,472** difference between the $692,592 labor figure and the P&L's $663,120 is the hours-basis difference alone: the form computes on a 1,880-hour calendar, the P&L on 1,800. Not reconcilable; state it.

**At the $24 rate card** labor becomes $705,752 and the total $870,212. Still under $1 million, so B16 holds either way.

## 5. Findings common to both submissions

**The capitalization label defect is in both P&Ls.** entroCIM's line reads `CAPITALIZED LABOR (65%)` but $530,496 on $663,120 gross is **80.0%**. WAM's reads the same and computes the same 80.0%. Two files, identical defect, which points to one shared formula with a stale label rather than two independent errors. One message to Tom Boss covers both. At a true 65% entroCIM's DEV expense rises to $396,552 and the loss widens to $997,246.

**Consequence: leave tab 2A at the template's 80% default** on both files. 80% is the template default *and* what both P&Ls compute; only the labels say 65%.

**The 2B month headers read 2026 on both files** while 2A reads 2027. Confirmed template defect, not a per-file error. Raise with Barbara Serdeczna. This is why the $164,460 Other IT Expense has **not** been written to entroCIM's 2B yet: the months are wrong. B18 carries it; 2B should carry it once the headers are corrected.

**The India rate differs between the P&Ls ($22) and the AOP rate card ($24)** on both submissions. One ruling from Tom Boss settles both.

**Both forms carried hardcoded totals that did not follow the resourcing model.** WAM was 28.2% over; entroCIM was 116.8% over. Two of two. **Check Ascent/Navigator before Friday rather than assuming it is clean.**

## 6. Still open on this file

1. **B17 In Scope for Investment Year is still the template's own instruction text.** Your D17 note reads "Need clarification from Darryl, David, and Ron." This is a required field and remains the largest content gap on the form. I did not invent scope for it.
2. **B26, B28, B30 still hold template instruction text.** These belong to the Value KPI and Compliance blocks, which are not the chosen path, so leaving them is defensible, but confirm the reviewer does not expect them blank rather than filled with guidance text.
3. **B6 Key Stakeholders reads only "CSS."** Thin against the WAM equivalent. Consider naming the actual stakeholders.
4. **Tab 2A roster still reflects the 16.15 FTE population**, not the P&L's 6.60 DEV FTE. B18 now disagrees with what 2A would compute. Reconciling 2A is the remaining structural work on this file.
5. **D22 note remains open:** whether the Financial Benefit Metric changes year over year, and that the Pro-Forma depends on it.
6. **A `~$` lock file was present in the WAM folder earlier.** Close both workbooks in Excel before opening the edited versions.

## 7. Method note

The template's dropdowns are stored as an Excel extension that standard Python libraries strip silently on save. All edits here were made by direct XML modification for that reason, and dropdown counts were verified intact afterwards (7 on Business Case, 6 on Scoring, matching the pre-edit file). Verify the same on any future programmatic edit.
