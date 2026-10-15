# Ascent / Navigator FY27 AOP Demand Collation Template — Change Log

**File:** `Products/Navigator/COPY_ascent-navigator_build_it-demand-collation-template.xlsx`
**Backup of pre-change state:** `Products/Navigator/COPY_ascent-navigator_build_it-demand-collation-template_BACKUP_2026-08-18.xlsx`
**Date:** 2026-08-18
**Scope:** Tabs 3 (Business Case) and 4 (Scoring) only, at Darryl's direction. Tabs 2A and 2B untouched.
**Sources:** NAV P&L tab of `CSS_Platform_Team.xlsx`; BIR # 2603158; Project Intake Navigator 2.0 (2025-10-28); `Products/Navigator/Navigator.md`; `Reference/Digital_Product_List.md`.

Companions: `Deliverables/WAM/2026-08-17_WAM_FY27_AOP_Change_Log.md`, `Deliverables/entroCIM/2026-08-17_entroCIM_FY27_AOP_Change_Log.md`.

Every value below was confirmed by Darryl before writing. Nothing was invented; the BIR and intake deck were used for business case and value proposition language only, per his instruction that they are historical reference rather than sources of current truth.

---

## 1. Why Navigator is the strongest of the three submissions

| | Navigator | WAM | entroCIM |
|---|---|---|---|
| 2027 net margin | **34.8%** | 10.7% | −18.0% |
| Investment (B18) | $1,797,280 | $785,840 | $857,052 |
| Benefit attributable to the investment | **Yes, directly** | No, different motion | N/A, loss |
| Payback claimed | **< 1 Year** | 1 to 5 Years | 1 to 5 Years |

**The reason the payback claim holds here and did not for WAM.** WAM's revenue is earned through supply chain programs the investment does not fund, which broke the attribution chain. entroCIM plans a loss. Navigator's benefit is cost avoidance *caused by* the investment: building Navigator 2.0 is what removes the IBM Maximo renewal. There is no attribution gap to argue about.

**Timing confirmed by Darryl 2026-08-18, and it materially improved the case.** The draft assumed the avoidance landed in 2028 at the IBM end-of-support cliff, which would have stretched payback beyond a year. The renewal is actually a March/April 2027 payment to IBM, inside the investment year. That makes `Payback < 1 Year` defensible rather than aggressive, and keeps B24 at 2027-12-31 consistent with the other two submissions.

**Navigator also has something neither other submission has: a dated external forcing function.** WAM and entroCIM both argue from opportunity cost, value that may not materialize. Navigator argues from IBM ending support and a renewal falling due on a known date. A reviewer cannot discount that the way a projection can be discounted.

## 2. Business Case tab, as written

| Cell | Field | Value |
|---|---|---|
| B3 | Business Sponsor | Dirk Naylor |
| B4 | Pillar lead | Sean McCloskey |
| B5 | Finance Approver | Tom Boss |
| B6 | Key Stakeholders | Ascent Operations; Ascent data centre and critical infrastructure clients; Digital Products & Business; Business Sponsor; CSS Finance; IT/Digital; Lisa Orton |
| B7 | Strategic Program | Non DDP: Applications |
| B8 | Investment Type | Carryover |
| B9 / B10 | Owning / Impacted BU | CSS (Geary) |
| B11 | Delivering Business | IT/Digital (Akash) |
| B13 | Investment Description | Left as pre-populated; already accurate |
| B14 | Risk of NOT Doing | Three categorised risks, entroCIM format |
| B15 / B16 | Target Start / Finish | 2027-01-02 / 2027-12-31 |
| B17 | In Scope FY27 | Six items |
| B18 | Total Investment Cost | **$1,797,280** |
| B21 | Value Proposition | Written |
| B22 | Financial Benefit Metric | Cost Avoidance; Software Sales |
| B23 | Pro-Forma Forecast | 129 words |
| B24 | Expected Benefits Timeline | 2027-12-31 |
| B26 / B27 / B28 | Value KPI block | **Left blank** |
| B30 | Compliance driver | Left blank |
| B32 | Customer impact | Written |
| B33 | Dependencies | Four items |
| B34 | In-house / Outsourced | Written |
| B35 | 3rd Party Solution | "None proposed. Navigator 2.0 is an Ascent-built solution." |
| B37 | Links & Attachments | **Left blank** at Darryl's direction |

**No Value KPI block, deliberately.** entroCIM carries both Financial Benefits and Value KPIs because its financial case is weak. Navigator's is strong and directly attributable, so the template's one-of-three instruction is followed cleanly rather than deviated from.

**B18 derivation, and why it is cleaner than the other two.** The NAV P&L plans 14 DEV FTE, 5 India at $22/hr and 9 North America at $94/hr, on **1,880 annual hours**. That is the AOP form's own calendar basis. WAM and entroCIM P&Ls both ran on 1,800 hours, forcing unreconcilable residuals of $33,440 and $29,472 that had to be stated on those forms. Navigator has no such gap: 5 × 22 × 1,880 = $206,800 and 9 × 94 × 1,880 = $1,590,480, totalling exactly $1,797,280. Other IT Expense is zero.

**Capitalization.** The NAV P&L capitalizes $1,437,824 of $1,797,280, exactly 80%, and here the row label agrees at 80%. Only the explanatory footnote says 65%, the same stale note found on the WAM and entroCIM P&Ls. Third of three, confirming one shared template artifact rather than three separate errors.

## 3. Decisions taken during drafting

| Decision | Outcome |
|---|---|
| 2027 redesign as separate scope item? | **No.** Same project as the Maximo replacement; folded into B17 bullet one |
| Portfolio integration prominence | **Mention only.** Removed as a B14 risk bullet, reduced to one line at the end of B17 |
| QuickBooks as a dependency | **Removed.** It was an inference from the deck's invoice workflow, not a stated fact |
| B35 wording | **Simplified.** Rejected-alternatives detail removed |
| B37 links | **Left blank** |
| B6, B8, B14 scoring | **All High**, confirmed |

**On the B14 revision.** The first draft carried four risks including "Risk of Reduced Portfolio Integration." Elevating integration to one of four risks over-weighted precisely the thing Darryl wanted downplayed, so it was cut to three, matching entroCIM's structure exactly. Each surviving bullet is strongly sourced: the 10x license exposure and end-of-support to the BIR and intake deck; the single-instance tenancy limit to deck slide 5.

## 4. Scoring tab, as written

| Cell | Criterion | Value |
|---|---|---|
| B4 | Compliance | None |
| B6 | Risk Mitigation | **High** |
| B8 | Strategic Alignment | **High** |
| B10 | Financial Benefits | **Payback < 1 Year** |
| B12 | Customer Success | High |
| B14 | Operational Improvement | **High** |
| B16 | Implementation Cost | $1-5 million |
| B18 | Execution Risk | Medium |
| B20 | Complexity | Medium |
| B22 | T-Shirt Size | Extra Large (32+ Weeks) |
| B24 | Change Impact | High |
| B26 | Work Dependencies | Yes |
| B28 | Extended Duration | Yes |

**Four criteria score High plus a sub-one-year payback, which is materially stronger than either sibling submission.** This was raised with Darryl as a deliberate choice rather than allowed to happen by accident, and confirmed. The justifications: Risk Mitigation High because IBM end-of-support is externally documented and dated against mission-critical operations, where WAM and entroCIM have no comparable forcing function; Strategic Alignment High because the guidance sets High where deferral incurs material cost, which is exactly the renewal; Operational Improvement High because the guidance sets High for processes occurring multiple times per day, which work order and ticketing in a 24x7 operations centre satisfies.

A reviewer comparing the three submissions will notice the divergence. The position is defensible on the merits, and the merits are the forcing function.

## 5. Two defects found and corrected during the write

**This template's mapping sheet is offset by two rows** from the WAM and entroCIM copies. Scoring validation lists sit at B172:B175, B178:B180, B183:B186, B189:B191, B194:B198 and B201:B202 rather than B170:B173 and so on. An initial verification pass against the older ranges produced six false failures. All thirteen scoring values were then re-verified against this file's own validation ranges and all thirteen pass.

**Date cells wrote as raw serial numbers.** B15, B16 and B24 displayed as 46389 and 46752 because this template carries no plain date style, only `mmm yyyy` and `mmm-yy` variants. A `yyyy-mm-dd` number format was added to `styles.xml` and three new cell formats created from the originals, so the dates now render correctly and read as true dates rather than text.

## 6. Open items

1. **Tab 2A carries three example rows** explicitly marked "example only - please delete" (Joe Smyth, John Smyth, Testers), and 2B carries one. Darryl is handling 2A and 2B; noted here so they are not forgotten before submission.
2. **B34 outsourcing** states none currently identified, based on the P&L carrying all 14 FTE at internal rates. Confirm if any development or product owner capacity is contracted.
3. **Pro-Forma attachment** referenced in B23, not yet attached.

## 7. Record corrections arising from this session

**Darryl is the Product Executive for Ascent / Navigator.** Both `Products/Navigator/Navigator.md` and `Reference/Digital_Product_List.md` record Chris Gazdic, with a flag that this needed reconciling against `01_Executive_Operating_Context.md`, which places Navigator in Darryl's portfolio. Darryl confirmed 2026-08-18 that he is the Product Executive. This closes a reconciliation open since 2026-07-16. Both files require updating.

Note that B4 still carries Sean McCloskey, because the Pillar Lead dropdown contains fourteen names and Chris Gazdic is not among them; neither is the field asking for the Product Executive.

**`Products/Navigator` is now the single home for Navigator material.** `Navigator.md` was moved in from `Products/`. A search across the Executive Operating System returns no other Navigator-dedicated file outside the folder. Portfolio-wide registers that reference Navigator in list form (`Reference/Digital_Product_List.md`, `01_Executive_Operating_Context.md`) remain in place by design.

## 8. Method note

The template's dropdowns are stored as an Excel extension that standard Python libraries strip silently on save. All edits were made by direct XML modification for that reason. Dropdown counts verified intact after every write: 7 on Business Case, 6 on Scoring, matching the pre-edit file. Zip integrity confirmed. Verify the same on any future programmatic edit.
