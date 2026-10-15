# Connected Device Assurance FY27 AOP Demand Collation Template — Change Log

**File:** `Products/CDA/04_Phase_4_AOP/COPY_connected-device-assurance_build_it-demand-collation-template.xlsx`
**Backup of pre-change state:** same folder, `..._BACKUP_2026-08-18.xlsx`
**Date:** 2026-08-18
**Scope:** Tabs 3 (Business Case) and 4 (Scoring). Tabs 2A and 2B untouched.
**Submission gate:** 2026-08-21 (Darryl's ruling 08-18, same date as the other three), three days out.
**Sources:** CDA P&L tab of `CSS_Platform_Team.xlsx`; `CDA_Business_Case_Working.md`; `CDA_Wesco_Business_Case_v2.docx`; `CDA_Exec_Brief.pptx`; `CDA_Business_Case_Appendix_Supporting_Detail.md`.

The template arrived entirely blank. Every field was drafted from the existing business case and confirmed by Darryl before writing; nothing was invented.

---

## 0. Superseding update, later on 2026-08-18

Darryl added one split India resource (0.5 FTE), 6.25 to 6.75 in DEV.

| | Earlier 08-18 | Now |
|---|---|---|
| DEV FTE | 6.50 | **7.00** |
| DEV gross labor | $201,787 | **$215,573** |
| **B18** | $246,787 | **$260,573** |
| Net revenue | ($85,357) | **($88,115)** |

**The consequence that matters: CDA now crosses the $250,000 intake threshold.** It sat $3,213 under; it is now **$10,573 over**. That was flagged as a live risk earlier the same day and it has materialised.

What changes as a result: the Intake deck's Project Financials slide (slide 8) states it "must be completed for all projects with cost over $250k", so it is no longer optional, and the intake requires a business case for requests over $250K not in budget. The business case exists, so the substance is covered; the packaging obligation is what changed. Scoring B16 stays `< $1 million`.

Figures in sections 1 to 4 below are the earlier 08-18 state. B18 and B23 on the form carry the current numbers.

## 0b. Value KPI block added and pilot scope reconciled, 2026-08-19 (Darryl)

**This reverses the 08-18 decision to leave B26, B27 and B28 blank.** Darryl asked for KPIs showing what the value looks like at the customer's site.

**Pilot scope reconciled first, because the form contradicted itself.** Darryl's opening basis was three pilots of 50 to 100 cameras each (150 to 300 cameras across three customers), while B17 said "one strategic enterprise customer, two to five sites" and B23 said "an estate of 250 to 1,000 devices". His ruling: **site count does not matter, camera count is the goal — 250 to 1,000 cameras across several pilot customers.** B17 and B23 were updated to match, dropping the single-customer and site-count language.

**B26 rebuilt 2026-08-19 (Darryl): product-specific, not pilot-dependent.**

The first set measured how the pilot went rather than what the product does. Inventory completeness depended on the quality of the customer's prior records; advisory-to-remediation on their approval speed and maintenance windows; remote resolution on whatever happened to break at that site. A poorly-run or unlucky pilot would have made a working product look weak, and the numbers would not have been comparable between customers.

**The rebuilt set, five KPIs, 204 words:**

| # | KPI | Measure |
|---|---|---|
| 1 | Device coverage depth | % of covered devices at each tier: discovered by sensor, validated by direct device integration, under managed control |
| 2 | Automated discovery yield | % of devices on monitored segments discovered and profiled without manual entry |
| 3 | Advisory correlation coverage | % of covered devices with firmware version mapped to vendor advisory and end-of-support data |
| 4 | Remote change success rate | % of firmware and configuration changes completing with post-change validation passed; proportion of failures recovered without a site visit |
| 5 | Service evidence completeness | % of actions with a complete approval, execution, validation and outcome record |

**KPI 1 is built on the data-confidence ladder already in the Exec Brief** (slide 5: DISCOVERED by partner sensor, VALIDATED by direct device integration, MANAGED under controlled action). That ladder is the clearest statement of what separates this service from an inventory tool, and turning it into a measure means the KPI reports how much of an estate the platform can actually *manage* rather than merely see. It was already the product's own framing; it had simply not been used as a metric.

**Every one is now a property of the service rather than of the engagement**, so results are comparable across customers and do not move with a single site's device mix, record quality or operational maturity.

**The 25 percent remote-resolution target came out of the KPI block.** It was the only documented target, but also the single most pilot-dependent measure, since it turns on what fails at a given site. The avoided-visit economics it supported are unaffected: they remain in B23, priced at $300 to $600 per avoidable visit against a 15 percent or greater reduction target. Moving it out of the KPI set puts it where it belongs, in the benefit case rather than in a performance commitment.

**Consequence for the value section.****Consequence for the value section.** CDA now carries both Financial Benefits and Value KPIs, the same deliberate deviation from the template's one-of-three instruction that entroCIM carries. Given CDA has zero revenue in the investment year, the KPI block is arguably doing more work here than the financial section.

## 1. What makes CDA different from the other three submissions

| | CDA | Navigator | WAM | entroCIM |
|---|---|---|---|---|
| Investment Type | **New** | Carryover | Carryover | Carryover |
| 2027 revenue | **$0** | $8,600,000 | $32M to $38M | $5M to $6M |
| Investment (B18) | **$246,787** | $1,797,280 | $785,840 | $857,052 |
| 2027 net | ($85,357) | $2,994,544 | $4,075,520 | ($897,778) |
| Payback claimed | 1 to 5 Years | < 1 Year | 1 to 5 Years | 1 to 5 Years |

**CDA is the only genuinely new investment of the four, and the only one with no revenue at all in the investment year.** It is a development and validation request whose deliverable is a validated, sellable service, not a financial return. That shaped the whole submission.

**The value path decision.** Financial Benefits was chosen over Value KPIs, forward-dated. The reasoning against KPIs is structural rather than presentational: the template requires Value KPIs to measure post-production performance, and CDA has no production in 2027, so any KPI would have been either a project-execution measure the field disallows or a measure dated outside the investment year. Financial Benefits with benefit realization stated as post-gate is the honest fit.

**B23 leads with the timing constraint at Darryl's direction (08-18):** "Pilots require a post-development timeframe." Stating that first means a reviewer meets the zero-revenue year as a designed sequence rather than discovering it as a gap three paragraphs in. The "Pro-Forma to be attached" line was removed.

## 2. The P&L

Development-only, staffing January through August, nothing after.

| Line | FY2027 |
|---|---|
| Revenue | $0 |
| DEV labor, 6.25 India + 0.25 North America FTE | $201,786.72 |
| Capitalized 80% | ($161,429.38) |
| Other IT Expense (licenses and field hardware) | $45,000 |
| DEV expense | $85,357.34 |
| **Net revenue** | **($85,357.34)** |

Rates reconcile at $22 India and $94 North America on **1,880 annual hours**, matching Navigator and the AOP form's own calendar, so there is no hours-basis residual to explain. **B18 is $246,787**, being DEV gross labor plus Other IT Expense, the convention Darryl set on entroCIM. That lands Implementation Cost at `< $1 million`, which v2 of the business case had already set independently.

**Note for reference:** Darryl's answer on Target Start and Finish was the full year, 2027-01-02 to 2027-12-31, while the P&L staffs January through August. That is deliberate: the investment year is the full year and the pilot may begin inside it once the August gate is passed. The form and the P&L therefore describe different things, and both are correct.

## 3. Fields written

**Business Case:** B3 Brad Stevens; B4 Sean McCloskey; B5 Tom Boss; B6 stakeholders; B7 Non DDP: Applications; B8 New; B9/B10 CSS (Geary); B11 IT/Digital (Akash); B13 investment description; B14 risk of not doing; B15/B16 dates; B17 in scope; B18 $246,787; B21 value proposition; B22 benefit metrics; B23 pro-forma; B24 2027-12-31; B32 customer impact; B33 dependencies; B34 in-house/outsourced; B35 third party.

**Left blank deliberately:** B26, B27, B28 (Value KPI block, not the chosen path); B30 (compliance block, not the chosen path); B37 (links, at Darryl's direction).

**B14 condensed, and the source documents realigned the same day.** The working document's approved text ran about 450 words in six headed paragraphs, deliberately aligned with `CDA_AOP_Risk_of_Not_Doing_2026-07-28.md`. Darryl chose the condensed version, 222 words in the house format used by the other three submissions.

Both source documents were then updated (Darryl, 08-18) so the three artifacts carry identical text:

| Artifact | State |
|---|---|
| Collation template B14 | Condensed, 222 words |
| `CDA_AOP_Risk_of_Not_Doing_2026-07-28.md` | Revised; 07-28 text retained as superseded |
| `CDA_Business_Case_Working.md` risk section | Revised; long form retained as superseded |

**Two changes worth recording rather than making silently.** The 07-28 document specified plain header lines with no bullet marks, matching a 07-24 entroCIM draft in `entroCIM Fodder copy.xlsx`. The FY27 collation templates for WAM, entroCIM and Navigator all use bulleted `Risk of [Category]` labels with an en dash, so CDA now matches its three sibling submissions rather than a superseded entroCIM draft. That editorial instruction was struck through in place rather than deleted.

Six bullets became five. No argument was lost: the former "Fragmentation of the Connected Services Portfolio" is folded into "Risk of Stranded Platform Investment," since both rest on the same reuse logic. The 07-28 note had offered merging the last bullet into "Ceding the Category" if space-constrained; the fragmentation merge is tighter and was used instead, which is a deviation from the documented option and is noted in that file.

**Still carrying the long form:** `CDA_Wesco_Business_Case_v2.docx` and `CDA_Wesco_Business_Case_v1_Full_Text.md`. These are circulated deliverables rather than working files and were left alone. Update them at the next revision, or accept the divergence knowingly.

**B35 discloses third-party components without naming vendors,** per the standing no-vendor-names rule. It states that a partner sensor and a remote monitoring and management platform are central and under commercial validation. Given what `N/A` cost on the WAM submission, silence here would have been actively wrong: these are not optional components.

## 4. Scoring

| Cell | Criterion | Value | Source |
|---|---|---|---|
| B4 | Compliance | Low | Business case recommendation |
| B6 | Risk Mitigation | High | Business case recommendation |
| B8 | Strategic Alignment | High | Business case recommendation |
| B10 | Financial Benefits | 1 Year < Payback < 5 Years | **Translated, see below** |
| B12 | Customer Success | High | Business case recommendation |
| B14 | Operational Improvement | Medium | Business case recommendation |
| B16 | Implementation Cost | < $1 million | $246,787 |
| B18 | Execution Risk | Medium | Confirmed 08-18 |
| B20 | Complexity | Medium | Confirmed 08-18 |
| B22 | T-Shirt Size | Extra Large (32+ Weeks) | Jan to Aug is about 35 weeks |
| B24 | Change Impact | Medium | Confirmed 08-18 |
| B26 | Work Dependencies | Yes | Ten in B33 |
| B28 | Extended Duration | Yes | Development, then pilot, then production |

**B10 required translation.** `CDA_Business_Case_Working.md` recommends "Financial Benefits: Medium," but those positions were written against the Intake form, where the control is a High/Medium/Low rating. On this collation template B10 is a payback-period dropdown with three options only. `1 Year < Payback < 5 Years` is the equivalent of the intended Medium: positive return expected, revenue beginning post-gate, figures pilot-validated rather than proven. The other five recommendations mapped without change.

**Execution Risk at Medium is the one to be ready to defend.** The guidance allows Medium where mitigation plans exist for known risks, and the funded validation phase is precisely that plan. The counter-argument is that nothing is qualified yet: no signed manufacturer terms, no partner sensor agreement, no named pilot customer. Darryl confirmed Medium on 08-18. If challenged, the answer is that the request funds the qualification rather than assuming it.

## 5. Record corrections arising

**Managed Services ownership is resolved (Darryl, 2026-08-18): the service is owned by the CSS/TSS business under Brad Stevens.** `CDA_Business_Case_Working.md` records "Managed Services leadership (owner function TBC)" and the Risk and Dependency Log has carried it as an open dependency since 07-28. It is not open. B33 and B6 were written accordingly, and the source documents need updating.

This matters beyond a form field: an unowned service function is the kind of gap a reviewer uses to question whether a new service can actually be delivered. It was closed and the record had not caught up.

**Exec Brief slide 13 carries the superseded timeline.** It shows funded validation in Q4 2026 and a camera pilot in H1 2027. Darryl's 2026-08-11 correction states 2026 is not funded, development and validation run the first eight months of 2027, funding ends August 2027, and the pilot follows that gate. The P&L agrees with the correction. The form was built from the correction, but the deck is the artifact circulating with people and should be reissued.

## 6. Open items

1. ~~`CDA_AOP_Risk_of_Not_Doing_2026-07-28.md` to be updated~~ — **done 2026-08-18**, along with the working document. Three artifacts now aligned.
2. **Exec Brief slide 13** timeline still shows the superseded Q4 2026 validation and H1 2027 pilot. **Deferred by Darryl 2026-08-18: update after the AOP cycle closes.** Known incorrect; do not use slide 13 for dates in the interim.
3. **`CDA_Wesco_Business_Case_v2.docx`** still carries the long-form risk text. Circulated deliverable, left unchanged; realign at next revision.
3. **Tab 2A** carries three example rows marked "example only - please delete", and 2B carries one. Populating 2A at 6.25 India and 0.25 North America FTE across January to August will compute to the $201,787 labor figure.
4. **Submission date** taken as 2026-08-21 per Darryl 08-18. The record still shows the Erickson reconciliation as unconfirmed.

## 7. Method note

This template is a third distinct variant. Its mapping-sheet validation ranges differ from both the WAM/entroCIM copies and the Navigator copy: Pillar Lead at B150:B164, Strategic Program at D148:D154, and the scoring lists at B172:B175, B178:B180, B183:B186, B189:B191, B194:B198, B201:B202. **Always read the validation ranges from the file itself rather than assuming a prior template's offsets.** All twenty dropdown values were verified against this file's own lists.

Dropdowns are stored as an Excel extension that standard Python libraries strip on save, so all edits were made by direct XML modification. Counts verified intact after writing: 7 on Business Case, 6 on Scoring. A `yyyy-mm-dd` number format was added to `styles.xml` so the three date cells render as dates rather than serial numbers, the same fix required on Navigator.
