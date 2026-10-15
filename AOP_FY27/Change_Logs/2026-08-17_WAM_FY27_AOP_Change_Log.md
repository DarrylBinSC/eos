# WAM FY27 AOP Demand Collation Template — Change Log and Open Items

**File:** `Products/WAM/COPY_wam_build_it-demand-collation-template.xlsx`
**Backup of pre-change state:** `Products/WAM/COPY_wam_build_it-demand-collation-template_BACKUP_2026-08-17.xlsx`
**Date:** 2026-08-17
**Scope of this pass:** Tabs 3 (Business Case) and 4 (Scoring) only, at Darryl's direction. Tabs 2A and 2B were not touched.
**Sources used:** the workbook itself, the FY27 entroCIM submission (for format and convention), `Products/WAM/WAM.md`, `Products/WAM/WAM_Roadmap.md`, `03_Decision_Log.md`, the 2026-08-17 weekly briefing, and the 2027 WAM Profit & Loss (DRAFT).
**Submission gate:** 2026-08-21, four days out (Register A19).

Every change below is reversible. Restore the backup to return to the pre-change state, or reset an individual cell using the "Was" column.

---

## 0. Update 2026-08-18 — P&L hours basis moved, and it resolved a documented gap

WAM headcount is **unchanged**. The 2027 WAM P&L moved from a 1,800-hour to an 1,880-hour annual basis, matching the AOP form's own calendar.

| | 08-17 | 08-18 |
|---|---|---|
| P&L DEV gross labor | $752,400 | **$785,840** |
| B18 on the form | $785,840 | $785,840, unchanged |
| Residual to explain | $33,440 | **none** |
| Net revenue at $38M | $4,075,520 | $4,068,832 |

**Section 4 below documents a $33,440 hours-basis residual that had to be stated rather than reconciled. It no longer exists.** The P&L now computes exactly the figure already on the form. B18 was not touched; B23's net-revenue figures were corrected to $3,156,832 at $32M and $4,068,832 at $38M. Margin holds at 9.9% and 10.7%, and net revenue still covers the request four to five times over.

## 0b. ecoInsight removed from B34, 2026-08-19 (Darryl)

**WAM never used ecoInsight.** Every occurrence in `CSS_Platform_Team.xlsx` sits on entroCIM Build lines (Detail1 r15/r44, Headcount r28, Scenarios r23); there are none on WAM lines. The reference reached B34 through the FY26 text, which was preserved when that field was rewritten on 08-17 and carried forward again when Revnue was added.

| | Was | Now |
|---|---|---|
| B34 Outsourced | `ecoInsight; Revnue Corp (Strev platform delivery and integration work under SOW)` | `Revnue Corp (Strev platform delivery and integration work under SOW)` |

**This was a stale claim about a vendor relationship, not a typo.** The form asserted an outsourced delivery partner that the financial model does not carry on this product, which overstates WAM's external delivery exposure. It became more visible once Darryl removed the ecoInsight contractor from the project entirely on 08-19.

**My error, worth recording.** When I rewrote B34 on 08-17 I preserved the FY26 outsourcing line without testing it against the resourcing model, then extended it by adding Revnue alongside. Preserving inherited text is usually right; preserving an inherited *factual claim* without checking it is not. The check that would have caught it is the same one that caught the B18 overstatements: read the field against the P&L rather than against the previous version of the field.

Revnue Corp remains correctly listed, on the basis established 08-17: it delivers under SOW (Strev SOW 3, ADM-to-Strev QA integration), which makes it a genuine outsourced resource rather than a licensed component. B33, B34 and B35 remain mutually consistent and consistent with Scoring B26 (`Yes`).

## 1. Cells filled that were blank

| Cell | Field | Value written | Basis |
|---|---|---|---|
| B6 | Key Stakeholders | CSS Sales Operations (Debbie Hunter, Natalie Marquardt); CSS Managed Services / Operations (Senthil Govindaswamy); Digital Products & Business (Sean McCloskey); WAM Product (David Blondel); ADM/DDP Delivery (Akansh Gangil); Commercialization (Amy Aguirre); Platform (Merwan Mereby); Digital Innovation Center (Sanjay Varier); MDM / Enterprise Data; Supplier Relations; Strev/Revnue | `Products/WAM/WAM.md` Key People, plus the Sales Operations audience established 2026-07-16 |
| B7 | Strategic Program | `DDP: Post Deployment (Growth)` | Same value as the FY27 entroCIM submission. WAM is a deployed, DDP-integrated platform in growth phase. **Confirm with Barbara Serdeczna or John Erickson** |
| B8 | Investment Type | `Carryover` | WAM is an existing multi-year investment, not a new start. Valid list is New / Carryover only |
| B17 | In Scope for FY27 | Six-item proposed scope, explicitly labelled NOT YET CONFIRMED | See section 5 item 3 |
| B23 | Pro-Forma Forecast | Superseded 2026-08-17 by the P&L figures — see section 4 | Replaced the template's own instruction text, which had been left in place |
| B37 | Links & Attachments | Backlog Deep Dive (08-05), Operational Hardening Summary (07-20), CSS Platform Team P&L Analysis 2027, Pro-Forma pending | Was `N/A` |

## 2. B14 — Risk of NOT Doing, rewritten

Your note in D14 flagged the prior text as carried over from FY26.

### Original FY26 text, preserved

> • Not knowing Asset Lifespan – No visibility to Asset Lifespan that could result in product upsell and the ability to provide Managed Services and/or Operational Services.
> • No Insight to Customer Behaviors – No insights to customer behaviors and trends on assets potentially sold by Wesco. Unknown insights to customer's needs can also lead to improper inventory positioning at Wesco
> • Missed new sales - Missed opportunity to Increase product sales for product replacement that could be identified via WAM.
> • Business going to Competitors – Customers may choose to purchase from our competitors or from other Integrators who offer Asset Management and Services and drives sales opportunities away from Wesco.

### First attempt, rejected

Six risks written from current delivery evidence: data foundation stalling, renewal signal not converting, Sales Operations expectations, the WMX/VAS dependency, Managed Services manual effort, channel loss. Correctly grounded but wrong register. It read as deliverable-level project risk rather than the overall value of WAM and ADM, and did not match the tone of the entroCIM FY27 submission.

### Format rules taken from the entroCIM package and applied

- One opening paragraph on the entroCIM construction: "Without continued investment, [product] risks A, B, and C. This could limit Wesco's ability to capitalize on [market demand] while increasing the future cost of [deferred foundation work]."
- Each bullet titled `Risk of [Category] –`, one sentence each.
- Risks stated at Wesco portfolio level. No system names, dates, named individuals, quarters, or sprint content.
- Conditional verbs throughout: risks, may lose, could limit, may be constrained.

### Categories used

Lost Competitive Differentiation, Missed Revenue Growth Opportunities, Reduced Scalability of Asset Management Services, Diminished Install-Base Visibility.

The first three mirror entroCIM's three directly. The fourth is WAM-specific and carries forward the install-base and inventory-positioning argument from the FY26 text, which is a genuine value axis for WAM and ADM rather than a delivery concern. Drop it if you want an exact three-bullet match with entroCIM.

**D14** now records the rewrite and points here for the original.

## 2b. Dependencies and third-party solution (added 2026-08-17, Darryl)

Two omissions Darryl caught. Both matter because they are the fields a reviewer cross-checks against the Scoring tab.

| Cell | Was | Now |
|---|---|---|
| B33 Dependencies | Digital Innovation Center (Varier); Platform (Mereby) | **Digital Products (McCloskey)** added, listed first as the owning organisation, ahead of DIC and Platform |
| B35 3rd Party Solution | `N/A` | **Strev**, the customer-facing partner platform from Revnue Corp, white-labeled within Wesco Asset Management |

**B35 was the more consequential gap.** `N/A` asserted that no third-party solution is involved, while Strev is a core component of the WAM offering and one of the structural constraints already recorded in `Products/WAM/WAM.md` under external platform integration. A reviewer comparing the architecture to the form would have found the contradiction, and "we said N/A" is a harder position to recover from than a disclosed dependency. It also now reconciles with Scoring B26 Work Dependencies, which reads `Yes`.

**B34 In-house or Outsourced Resources** was updated for consistency, since it listed the same cross-portfolio dependencies as B33 and would otherwise have omitted Digital Products while B33 named it. Three spelling errors carried from the FY26 text were corrected in the same edit (`Exisiting`, `Depdencies`, `Outsource`).

**Correction, 2026-08-17 (Darryl).** I initially excluded Revnue from B33 and B34 on the reasoning that Strev is a licensed platform rather than a resource-providing vendor, and therefore belonged in B35 only. That was wrong, and the record contradicted it: Strev SOW 3 covers ADM-to-Strev QA integration, and release governance for the Strev QA environment is tracked as active work. Revnue delivers work under statement of work, which makes it both a dependency and an outsourced resource, not merely a licensed component.

Strev now appears in all three fields, correctly:

| Cell | Entry |
|---|---|
| B33 Dependencies | `• Strev / Revnue Corp (3rd party platform partner)`, matching the entroCIM convention for ecoInsight |
| B34 Outsourced | `ecoInsight; Revnue Corp (Strev platform delivery and integration work under SOW)` |
| B35 3rd Party Solution | Strev, the customer-facing partner platform from Revnue Corp, white-labeled within WAM |

**Why the error is worth recording rather than just fixing.** A vendor that delivers under SOW carries schedule, quality and commercial risk that a licensed component does not. Understating Revnue as a component rather than a delivery dependency would have made the submission look less externally dependent than it is, in a year where the QA integration is already a live blocker. The three fields now agree with each other and with Scoring B26 (`Yes` on work dependencies).

## 3. Scoring changes

| Cell | Criterion | Was | Now | Basis |
|---|---|---|---|---|
| B16 | Implementation Cost | `$1-5 million` | `< $1 million` | **Factual correction.** B18 stated $964,440, below $1 million, so the two fields contradicted each other. Still correct after B18 was re-based to $785,840 on 08-17, and correct at the $857,280 alternative |
| B26 | Work Dependencies | `No` | `Yes` | **Factual correction.** Business Case B33 names Digital Innovation Center (Varier) and Platform (Mereby). The entroCIM FY27 submission answers Yes on the same basis |
| B18 | Execution Risk | `Low` | `Medium ` | Low requires a small team, familiar technology, well-defined scope, incremental change. WAM FY27 has 15+ contributors, cross-portfolio dependencies, an external vendor, an unresolved asset-source question, and scope not yet agreed with Platform. Low was also internally inconsistent with T-Shirt Size `Extra Large` and Change Impact `High` |
| B14 | Operational Improvement | `Low` | `Medium ` | The guidance for Medium is "medium operational efficiencies, indirect soft benefits." WAM removes account-by-account research in Sales Ops and manual reconciliation in Managed Services onboarding. Low understated it and conflicted with the operational benefits asserted in B32. entroCIM scores Medium |
| B28 | Extended Duration | `No` | `Yes` | Investment Type is Carryover and the field guidance reads "Is this likely to be a multi-year investment?" entroCIM answers Yes. **Reverse this if the field is read strictly as the duration of this investment year alone** (2027-01-02 to 2027-12-31 is 12 months, which would make No correct) |

**Left unchanged, deliberately:** Compliance `None`, Risk Mitigation `Medium`, Strategic Alignment `Medium`, Customer Success `High`, Complexity `Medium`, T-Shirt `Extra Large`, Change Impact `High`. Change Impact `High` is defensible on the Managed Services operating-model change and, being in the Ease Assessment section, is the conservative answer. Strategic Alignment `Medium` rather than High is also the conservative reading while the license-versus-supply-chain question is open.

---

## 4. P&L reconciliation, applied 2026-08-17

Source: **2027 WAM Profit & Loss (DRAFT)**, monthly operating P&L linked to WAM staffing, provided as a screenshot. Stated basis: all named WAM resources assigned to DEV using % COGS Today, Region, Cost, and **1,800 annual hours**.

### FY2027 plan as stated

| Line | FY2027 |
|---|---|
| Revenue (2026 actuals +15%, planning only) | $38,000,000 |
| COGS (People + HW + SW) | $32,224,000 |
| **Gross Margin** | **$5,776,000 (15.2%)** |
| Sales (People $1.0M +3%, Other $0.5M) | $1,500,000 |
| Marketing (Sales Promotion, 2026 budget) | $50,000 |
| DEV — Resources IN, 19.00 FTE | $752,400 |
| DEV — Resources NA | zero |
| Capitalized labor, labelled 65% | ($601,920) |
| DEV expense after capitalization | $150,480 |
| Amortization (toggle Off) | – |
| **Net Revenue** | **$4,075,520 (10.7%)** |

The P&L is internally consistent: $5,776,000 − $1,500,000 − $50,000 − $150,480 = $4,075,520 exactly.

### B18 re-based: $964,440 → $785,840

The prior $964,440 was hardcoded and is **not supported by the governing model**. It implies 21.375 FTE at $24/hr on 1,880 hours, all at India rate. The variance against the P&L decomposes exactly, to the dollar:

| Driver | Variance |
|---|---|
| Headcount, 21.375 vs 19.00 FTE | $107,160 |
| Rate, $24 vs $22 (India) | $71,440 |
| Hours, 1,880 vs 1,800 annual | $33,440 |
| **Total overstatement** | **$212,040 (28.2% above plan)** |

This is the same failure mode found on entroCIM on 08-05, where the form carried $1,437,918 against a 2027 DEV plan of $727,200. Both forms were built before the resourcing model landed and neither followed it.

**B18 is now $785,840** = 19.00 FTE × $22/hr × **1,880 hours**. This carries the P&L roster and rate onto the form's mandatory calendar basis, so B18 ties to what tab 2A will compute rather than floating free of it. The residual **$33,440** against the P&L's $752,400 is the hours-basis difference alone. It cannot be reconciled away; state it rather than absorb it.

**If Finance rules the $24 rate card mandatory on the form, B18 becomes $857,280.** Still under $1 million, so Scoring B16 holds either way. The $22 versus $24 discrepancy is already open on entroCIM; one answer from Tom Boss settles both.

### Finding: the P&L capitalization label contradicts its own arithmetic

The line reads **CAPITALIZED LABOR (65%)** but the figure is $601,920, which is **80.0%** of the $752,400 gross, not 65%. At a true 65% the capitalized amount would be $489,060 and the DEV expense $263,340, not $150,480.

| | As stated (80%) | At the labelled 65% |
|---|---|---|
| Capitalized | $601,920 | $489,060 |
| DEV expense | $150,480 | $263,340 |
| Net Revenue | $4,075,520 | $3,962,660 |
| Net margin | 10.7% | 10.4% |

A $112,860 swing. One of the two is wrong and it flows to net margin. Note that **80% is the AOP template's own default capex percentage**, so the P&L formula matches the AOP default while only its label matches the 65% entroCIM convention. This reverses the recommendation in the earlier version of this log: **leave tab 2A at the 80% default** and get the P&L label corrected, rather than moving the form to 65%.

### Other observations for Tom Boss

- **Marketing is $50,000, or 0.13% of planned revenue**, and is labelled as the 2026 budget carried forward. This sits against a product whose commercialization plan includes a broader marketing launch. The commercialization narrative and the marketing line do not agree.
- **Gross margin of 15.2% is a distribution margin, not a software margin.** This independently corroborates the 08-05 finding: if WAM revenue were license and software driven, gross margin would be several times higher. The margin structure is evidence that current revenue is product pass-through through supply chain programs. Useful to Darryl because it means the finding is not merely an anecdote from one session; it is visible in the numbers Finance itself produced.
- **Revenue basis.** $38,000,000 implies a 2026 actual base of $33,043,478. The record holds a 2026 objective of $19.0M with $16.7M YTD through June (87.23% attainment), which annualizes to $33.4M and reconciles to the P&L. But it also means the 2026 objective is being overachieved by roughly 1.74x, and a reviewer seeing a $19M objective against a $38M 2027 plan will ask why. Have the answer ready: the objective and the run rate diverged, not the plan and the run rate.
- **Resources NA is zero.** No North America resource is budgeted to WAM DEV in 2027. If any US or Canada resource is assigned, cost is understated at a 4.3x differential ($94 versus $22). On entroCIM the equivalent exposure was 3.45 FTE carrying $583,740. Confirm against A25 (WAM resource determination with Sean McCloskey), overdue since 08-14.

### B22 and B23 updated

**B22** now reads Wesco Asset Management Sales, Product Pull-Thru, and Software and Renewal Sales. Product Pull-Thru was added because the 15.2% margin structure shows that is materially what the revenue is. entroCIM lists Software Sales and Product Pull-Thru on the same basis.

**B23** now carries the actual FY2027 figures with the attribution caveat, replacing the TBD placeholder.

**B23 rewritten for voice, 2026-08-17 (Darryl).** The first version was drafted in analytical voice and read as notes to Darryl rather than a submission field: it carried instructions to himself ("confirm with Tom Boss"), reasoning chains ("arithmetically true and not defensible without..."), and meta-commentary about the analysis itself. Now 149 words, structured as basis, outcome, what it means for the decision, qualifications. The analysis did not disappear; it belongs here, in this log, where the audience is Darryl. Rule captured to `Reference/Communication_Preferences.md` §3b so it applies to every submitted form field going forward.

### Revenue range authorised by Finance, 2026-08-17

Finance confirmed the same day that a planning range of **$32,000,000 to $38,000,000** may be used for 2027 revenue. B23 was updated to carry the range and its sensitivity rather than the single $38,000,000 point.

| Revenue | Gross Margin @15.2% | Net Revenue | Net margin | Investment covered |
|---|---|---|---|---|
| $32,000,000 | $4,864,000 | $3,163,520 | 9.9% | 4.0x |
| $35,000,000 | $5,320,000 | $3,619,520 | 10.3% | 4.6x |
| $38,000,000 | $5,776,000 | $4,075,520 | 10.7% | 5.2x |

Across the range net revenue moves $912,000 (22.4%) and net margin moves 0.8 points. The $38M case reproduces the P&L exactly, which confirms the sensitivity is built on the P&L's own structure.

For context on where the bounds sit: $38,000,000 is the P&L's stated 2026 actuals plus 15%, implying a 2026 base of $33,043,478. The $32,000,000 lower bound is 0.968x that base, so it is approximately 2026 actuals held flat. Both bounds remain well above the recorded 2026 objective of $19.0M ($32M is 1.68x), so the objective-versus-plan question survives the range and still needs an answer.

**Submission basis: the range itself, not a point estimate.** Darryl's direction 2026-08-17, and the reason belongs on the record because it changes who owns the gap: the CSS business does not yet have its actual 2027 forecast available, and Finance authorised the range for WAM the same day as the interim planning basis. The range will be replaced with a point estimate when the CSS forecast is issued.

This supersedes an earlier recommendation in this log to submit on the $32,000,000 lower bound. That recommendation treated the range as a choice about conservatism. It is not; it is a consequence of an upstream forecast that does not exist yet, and presenting it as a deliberate low-end selection would have obscured the actual dependency.

**What makes the range defensible rather than evasive** is that the investment case holds at every point in it. Net revenue covers the $785,840 investment 4.0x at the bottom and 5.2x at the top. A reviewer asking "what if revenue lands at the low end" gets an answer that does not change the decision, which is the whole reason a range is acceptable here. State it that way rather than apologising for the absence of a point estimate.

**Residual question the range does not resolve.** Both bounds sit well above the recorded 2026 objective of $19.0M, with $32M at 1.68x. Have the answer ready: the objective and the run rate diverged during 2026, with $16.7M attained by June against a $19.0M full-year objective. The plan is not aggressive against actuals; the objective was low against actuals.

**Assumption to confirm, labelled as such in B23:** holding gross margin at 15.2% across the range is my assumption, not a Finance statement. COGS is predominantly hardware and software pass-through, so it is the line that determines whether the margin holds as volume falls. Confirm with Tom Boss.

---

## 5. Open items before 2026-08-21

Ranked by consequence. Four days remain.

**1. The Pro-Forma must isolate incremental benefit.**
This is now the single blocking item. The P&L gives real figures, but $4,075,520 net revenue is the whole WAM line, not the return on a $785,840 investment. Dividing one into the other gives a payback of roughly two to three months, which is arithmetically true and analytically indefensible: the revenue is being earned through a motion this investment does not fund.

Two defensible routes. Either Tom Boss produces a Pro-Forma isolating the revenue attributable to the FY27 scope, in which case Financial Benefits stands and Scoring B10 could justifiably move to `Payback < 1 Year`; or the submission moves to the **Value KPIs** path, a lower priority band but a case that survives scrutiny. B10 currently reads `1 Year < Payback < 5 Years`, which I have deliberately left alone as the conservative position. Do not move it up until the attribution exists.

**2. Confirm the gross-margin assumption across the revenue range** with Tom Boss, and **confirm the rate basis.** On rate: $22 (P&L) or $24 (AOP rate card), which determines whether B18 is $785,840 or $857,280. Same question already open on entroCIM.

**3. FY27 scope confirmation.**
B17 is written as a proposal and labelled as such. It cannot be finalised until the Product/Platform scope split is agreed with Rajesh and the license-versus-supply-chain-motion question is decided. The scope drafted follows the documented 2026 outcome arc into 2027; a defensible starting position, not an agreed plan. The upstream blocker is the Erickson scope question, open since 08-05 and identified in the 08-17 weekly as the pacing item for the whole submission.

**4. Tab 2A Labor is empty.** Out of scope for this pass, but it is the tab the Planview submission runs on. It should now be populated at 19.00 FTE, India, $22 (or $24 once ruled), capex 80%, which will compute to the B18 figure.

**5. Tab 2B Non-Labor month headers read 2026, not 2027**, while 2A reads 2027. Probable template defect. Raise with Barbara Serdeczna; it affects both submissions.

**6. Capex percentage — resolved, keep 80%.** The WAM P&L computes 80% despite its 65% label, and 80% is the template default. Leave 2A at 80% and get the P&L label corrected. This reverses the earlier recommendation in this log.

**7. Language not yet safe for outbound use.** Do not use "beyond Wesco part numbers" or "coverage beyond Core and Anixter part numbers" until resolved with Akansh; the standing instruction is that the framing rests on a probable misunderstanding. The safe formulation is that license data now syncs from multiple source systems into a single view. The automated three-times-daily DDP/EUDM sync discrepancy also remains open.

**8. Favourable new evidence worth using.** The notification suite shipped to production on 08-17 with analytics reporting and an upload fix beyond original scope, and the watch item dropped from High to Medium. This is the first governed renewal signal reaching Sales Operations in production, and it closes a gap Debbie Hunter's organisation has watched since 07-16. It strengthens the FY27 case materially and is not yet reflected anywhere in the template. Consider whether it belongs in B17 as delivered-baseline context, or is held for the value narrative.

---

## 6. Observation for the entroCIM submission

The entroCIM file's Investment Type field (`3. BUSINESS CASE!B8`) contains `M&A`, which is not valid for that field. The valid list is New / Carryover; `M&A` belongs to the Strategic Program list in B7. That cell carries two overlapping validations in the template, which is how the wrong value got in. Worth correcting before 08-21.

## 7. Note on file handling

A `~$` lock file is present in `Products/WAM/`, which usually means the workbook is open in Excel. Close it before opening the edited version, or Excel may present a recovery prompt and you could lose these changes.

The template's dropdowns are stored as an Excel extension that standard Python libraries silently strip on save. These edits were made by direct XML modification for that reason, and dropdown counts were verified intact afterwards (7 on Business Case, 6 on Scoring). If any future edit is made programmatically, verify the dropdowns survived before submitting.
