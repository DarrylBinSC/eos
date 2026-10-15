# CDA v4.2 reconciliation, 2026-09-30

Files:
- `/mnt/user-data/outputs/2026-09-30_CDA_Pro_Forma_v4.2.xlsx` (built from `/tmp/claude-0/cda/dz7.xlsx`, working copy `/tmp/claude-0/cda/CDA_Pro_Forma_v4.2_2026-09-30.xlsx`)
- `/mnt/user-data/outputs/2026-09-30_CDA_Product_and_Business_Case.pptx` (built by `/tmp/claude-0/deck/build3.py`, 20 slides)

Checks: recalc.py reports 0 errors across 2,048 formulas. Staffing row 70 reads OK in all five columns. Rate chain check (Staffing C77) OK. Deck Figures sector check OK. Commission share check OK. validate.py prints "All validations PASSED!". No em or en dashes in any slide text, table or speaker note.

## 1. Headline figures, before and after

"Before" is dz7.xlsx (v4.1) recalculated fresh; its cached values matched the recalculation exactly.

| Figure | v4.1 | v4.2 |
|---|---|---|
| Annual fee, Small | $7,352 | $6,892 (deck: $6,900) |
| Annual fee, Medium | $11,214 | $10,336 (deck: $10,300) |
| Annual fee, Large | $16,954 | $15,659 (deck: $15,700) |
| Gross margin %, 2031 | 45.2% | 45.7% |
| Cash break-even year | 2031 | 2031 |
| Peak cash requirement | -$2,235,902 | -$2,259,250 |
| Five-year revenue, 2027 to 2031 | $21,907,328 | $20,244,155 |
| TSS heads, 2031 | 7 | 7 |
| Run rate at end of 2031 (reference) | $10,132,702 | $9,353,379 |
| Service-delivery cost rate (reference) | $94.00 | $56.40 |

Why: labour is now costed at $56.40 and the fee build's 40 percent target returns it to the $94 budget rate, so the fee falls by the removed double markup on people and commissioning hours. Headcount does not move because hours are cost divided by the same rate the cost uses. Per-site gross margin stays 40 percent at every size; payback lengthens slightly (13.4 / 14.4 / 15.3 months, was 13.1 / 14.0 / 14.8) because the fee falls more than the upfront cost.

## 2. Deck Figures (column D value, column E display, source cell)

| Key | Value | Display | Source | Slide |
|---|---|---|---|---|
| fee_small | 6,892.1158 | $6,900 | Site Tiers!C40 | 6, 7, 8, 16 |
| fee_medium | 10,336.2894 | $10,300 | Site Tiers!D40 | 6, 7, 8, 16 |
| fee_large | 15,658.8011 | $15,700 | Site Tiers!E40 | 6, 7, 8, 16 |
| per_device_small | 14.3586 | $14.36 | Site Tiers!C42 | 6, 16 |
| per_device_medium | 8.6136 | $8.61 | Site Tiers!D42 | 6, 16 |
| per_device_large | 6.5245 | $6.52 | Site Tiers!E42 | 6, 16 |
| cost_to_serve_small | 2,501.5828 | $2,502 | Site Tiers!C33 | 8, 16 |
| cost_to_serve_medium | 3,432.757 | $3,433 | Site Tiers!D33 | 8, 16 |
| cost_to_serve_large | 4,759.114 | $4,759 | Site Tiers!E33 | 8, 16 |
| upfront_recovered_small | 1,633.6867 | $1,634 | Site Tiers!C36 | 8 |
| upfront_recovered_medium | 2,769.0167 | $2,769 | Site Tiers!D36 | 8 |
| upfront_recovered_large | 4,636.1667 | $4,636 | Site Tiers!E36 | 8 |
| upfront_small | 4,901.06 | $4,901 | Site Tiers!C25 | 8 |
| upfront_medium | 8,307.05 | $8,307 | Site Tiers!D25 | 8 |
| upfront_large | 13,908.5 | $13,909 | Site Tiers!E25 | 8 |
| gm_small | 0.4 | 40% | Site Tiers!C43 | 8 |
| gm_medium | 0.4 | 40% | Site Tiers!D43 | 8 |
| gm_large | 0.4 | 40% | Site Tiers!E43 | 8 |
| payback_small | 13.3953 | 13.4 mo | Site Tiers!C51 | 8 |
| payback_medium | 14.4397 | 14.4 mo | Site Tiers!D51 | 8 |
| payback_large | 15.3125 | 15.3 mo | Site Tiers!E51 | 8 |
| payback_max | 16 | 16 | Site Tiers!C51:E51 | 8 |
| target_margin | 0.4 | 40 | Inputs!C33 | 6, 8, 16 |
| software_share_large | 0.7682 | 77 | Site Tiers!E31 / E33 | 8 (notes) |
| hardware_per_node | 880 | $880 | Site Tiers!C16 | 16 |
| skyspark_small | 1,195.46 | $1,195 | Site Tiers!C17 | 16 |
| skyspark_medium | 2,988.65 | $2,989 | Site Tiers!D17 | 16 |
| skyspark_large | 5,977.3 | $5,977 | Site Tiers!E17 | 16 |
| pods_small | 1,000 | $1,000 | Site Tiers!C18 | 16 |
| pods_medium | 2,500 | $2,500 | Site Tiers!D18 | 16 |
| pods_large | 5,000 | $5,000 | Site Tiers!E18 | 16 |
| other_sw_upfront | 1,600 | $1,600 | Site Tiers!C20 | 16 |
| commissioning_small | 225.6 | $226 | Site Tiers!C23 | 16 |
| commissioning_medium | 338.4 | $338 | Site Tiers!D23 | 16 |
| commissioning_large | 451.2 | $451 | Site Tiers!E23 | 16 |
| complexity_adder | 6,453.4491 | $6,500 | Site Tiers!C74 | 6, 16 |
| complex_fee_small | 13,345.5649 | $13,300 | Site Tiers!C77 | reference |
| complex_fee_medium | 16,789.7386 | $16,800 | Site Tiers!D77 | reference |
| complex_fee_large | 22,112.2502 | $22,100 | Site Tiers!E77 | reference |
| revenue_2027 | 0 | 0 | Model!C20 | 9 (chart) |
| revenue_2028 | 1,159,604.2794 | 1.16 | Model!D20 | 9 (chart) |
| revenue_2029 | 3,667,220.0744 | 3.67 | Model!E20 | 9 (chart) |
| revenue_2030 | 6,614,128.1708 | 6.61 | Model!F20 | 9 (chart) |
| revenue_2031 | 8,803,202.1183 | 8.8 | Model!G20 | 9 (chart) |
| gm_2027 | 0 | 0 | Model!C32 | 9 (chart) |
| gm_2028 | 398,708.7699 | 0.4 | Model!D32 | 9 (chart) |
| gm_2029 | 1,410,243.4896 | 1.41 | Model!E32 | 9 (chart) |
| gm_2030 | 2,542,222.4535 | 2.54 | Model!F32 | 9 (chart) |
| gm_2031 | 4,026,002.4866 | 4.03 | Model!G32 | 9 (chart) |
| gm_pct_2028 | 0.3438 | 34% | Model!D33 | 9 (notes) |
| gm_pct_2029 | 0.3846 | 38% | Model!E33 | 9 (notes) |
| gm_pct_2030 | 0.3844 | 38% | Model!F33 | 9 (notes) |
| gm_pct_2031 | 0.4573 | 46% | Model!G33 | 9 (notes) |
| sites_2031 | 684 | 684 | Model!G10 | 9 |
| devices_2031 | 85,500 | 85,500 | Model!G9 | 9 |
| run_rate_2031 | 9,353,379.485 | $9.4M | Model!G61 | 9, 12 |
| five_year_revenue | 20,244,154.6431 | $20.2M | Summary!C22 | reference |
| gm_pct_2031 | 0.4573 | 46% | Summary!C28 | 9 |
| break_even_year | 2,031 | 2031 | Summary!C31 | 9 (notes), 17 |
| peak_cash | -2,259,249.7577 | $2.3M | Summary!C32 | 17 |
| capital_2031 | 8,015,283.2512 | $8.0M | Summary!C33 | 17 |
| build_2027 | 260,573.36 | $261K | Model!C36 + Model!C37 | 9, 11 (notes), 17, 19 |
| build_labour_2027 | 215,573.36 | $216K | Model!C36 | reference |
| kroger_gm_2031 | 0.4763 | 48% | Account P&L!G11 | 11 |
| kroger_sites_2031 | 429 | 429 | Accounts!G13 | 11 |
| kroger_site_share_2031 | 0.6272 | 63% | Accounts!G13 / Model!G10 | 9 (notes) |
| kroger_revenue_share_2031 | 0.7631 | 76% | Accounts!G35 / Model!G20 | 9 (notes) |
| kroger_cameras_per_year | 8,000 | 8,000 | Inputs!F62 | 11 (notes) |
| camera_fee | 5 | $5 | Inputs!C42 | 11 (notes) |
| kroger_camera_fee_annual | 40,000 | $40K | Accounts!G18 | 11 (notes) |
| tam | 1,311,639,263.029 | $1.31B | Summary!C35 | 12 |
| sam | 415,880,129.938 | $416M | Summary!C36 | 12 |
| som_share | 0.0215 | 2.1% | Summary!C38 | 12 |
| som_share_whole | 0.0215 | 2 | Summary!C38 | 12 |
| sector_retail_sites | 48,450 | 48,450 | Market Sizing!G (rows 8) x C23 | 12 |
| sector_retail_value | 611,990,506.35 | $612M | Market Sizing!G x L (rows 8) x C23 | 12 |
| sector_other_sites | 41,140 | 41,140 | Market Sizing!G (rows 9, 10, 11, 12, 14, 15) x C23 | 12 |
| sector_other_value | 527,793,526.9338 | $528M | Market Sizing!G x L (rows 9, 10, 11, 12, 14, 15) x C23 | 12 |
| sector_mfg_sites | 9,520 | 9,520 | Market Sizing!G (rows 13) x C23 | 12 |
| sector_mfg_value | 152,633,058.5889 | $153M | Market Sizing!G x L (rows 13) x C23 | 12 |
| sector_dc_sites | 1,254.515 | 1,255 | Market Sizing!G (rows 16, 17) x C23 | 12 |
| sector_dc_value | 19,222,171.1563 | $19M | Market Sizing!G x L (rows 16, 17) x C23 | 12 |
| sector_check | OK | OK | Check against Summary!C35 | check |
| comm_heads_2028 | 1 | 1 | Staffing!D17 | 10 |
| comm_heads_2029 | 1 | 1 | Staffing!E17 | 10 |
| comm_heads_2030 | 2 | 2 | Staffing!F17 | 10 |
| comm_heads_2031 | 2 | 2 | Staffing!G17 | 10 |
| comm_new_2028 | 0 | 0 | Staffing!D18 | 10 |
| comm_new_2029 | 0 | 0 | Staffing!E18 | 10 |
| comm_new_2030 | 1 | 1 | Staffing!F18 | 10 |
| comm_new_2031 | 1 | 1 | Staffing!G18 | 10 |
| tss_heads_2028 | 1 | 1 | Staffing!D27 | 10 |
| tss_heads_2029 | 3 | 3 | Staffing!E27 | 10 |
| tss_heads_2030 | 6 | 6 | Staffing!F27 | 10 |
| tss_heads_2031 | 7 | 7 | Staffing!G27 | 10 |
| tss_new_2028 | 1 | 1 | Staffing!D27 | 10 |
| tss_new_2029 | 3 | 3 | Staffing!E27 | 10 |
| tss_new_2030 | 6 | 6 | Staffing!F27 | 10 |
| tss_new_2031 | 7 | 7 | Staffing!G27 | 10 |
| comm_absorbed_through | 2,029 | 2029 | Staffing!C18:G18 | 10 |
| tss_fte_2031 | 6.6902 | 6.7 | Staffing!G26 | reference |
| first_hire | Jul 2027 | Jul 2027 | Staffing!C33 | 10 |
| sites_per_fte_2031 | 102.2397 | 102 | Staffing!G61 | 10 |
| devices_per_fte_2031 | 12,779.9642 | 12,800 | Staffing!G62 | 10 |
| budget_rate | 94 | $94 | Inputs!C74 | 10 |
| cost_rate | 56.4 | $56.40 | Inputs!C23 | 10 |
| commission_rate | 0.05 | 5 | Inputs!C25 | 7 |
| contract_years | 3 | 3 | Inputs!C26 | 7 |
| share_rep | 0.02 | 2 | Input, Nate Kehr, 2026-09-29 | 7 |
| share_manager | 0.02 | 2 | Input, Nate Kehr, 2026-09-29 | 7 |
| share_inside | 0.01 | 1 | Input, Nate Kehr, 2026-09-29 | 7 |
| share_check | OK | OK | Check against Inputs!C25 | check |
| deal_small_1_sites | 1 | 1 | Strawman | 7 |
| deal_small_1_value | 20,700 | $20,700 | sites x fee_small (rounded as published) x Inputs!C26 | 7 |
| deal_small_1_pool | 1,035 | $1,035 | contract value x Inputs!C25 | 7 |
| deal_small_1_rep | 414 | $414 | contract value x rep share | 7 |
| deal_small_1_manager | 414 | $414 | contract value x manager share | 7 |
| deal_small_1_inside | 207 | $207 | contract value x inside share | 7 |
| deal_medium_10_sites | 10 | 10 | Strawman | 7 |
| deal_medium_10_value | 309,000 | $309,000 | sites x fee_medium (rounded as published) x Inputs!C26 | 7 |
| deal_medium_10_pool | 15,450 | $15,450 | contract value x Inputs!C25 | 7 |
| deal_medium_10_rep | 6,180 | $6,180 | contract value x rep share | 7 |
| deal_medium_10_manager | 6,180 | $6,180 | contract value x manager share | 7 |
| deal_medium_10_inside | 3,090 | $3,090 | contract value x inside share | 7 |
| deal_large_100_sites | 100 | 100 | Strawman | 7 |
| deal_large_100_value | 4,710,000 | $4,710,000 | sites x fee_large (rounded as published) x Inputs!C26 | 7 |
| deal_large_100_pool | 235,500 | $235,500 | contract value x Inputs!C25 | 7 |
| deal_large_100_rep | 94,200 | $94,200 | contract value x rep share | 7 |
| deal_large_100_manager | 94,200 | $94,200 | contract value x manager share | 7 |
| deal_large_100_inside | 47,100 | $47,100 | contract value x inside share | 7 |
| rate_chain_check | OK | OK | Staffing!C77 | check |
| staffing_tieback | OK | OK | Staffing!C70:G70 | check |

## 3. Slides changed

Order is the new order; build2 numbers in brackets.

- 1 Title: date "September 30, 2026".
- 4 Why Wesco: kicker is Bob Caprise's Reese's Cup line, attributed, mixed case. Nothing else changed.
- 6 How it sells: fifth column "Per device per month" ($14.36 / $8.61 / $6.52), col_w 1.9 / 4.1 / 2.1 / 1.66 / 2.1 = 11.86. Fees, complexity adder (about $6,500) and the marker's 40 percent come from the tab. Marker now starts "Illustrative." Speaker note adds the Axis Device Manager comparison sentence and the Kroger $15 one-time or annual sentence.
- 7 NEW What a seller earns: three cards (One Small site, Ten Medium sites, One hundred Large stores), each with three-year contract value, commission pool and the rep / manager / inside split; green card on the largest. Headline, marker and notes as specified. Takeaway: "One hundred stores pays the sales chain $235,500 at signing."
- 8 One site [7]: all figures from the tab. Takeaway reads "inside 16 months" (see section 5). Marker starts "Illustrative." Speaker note figures from the tab (see section 5).
- 9 Plan, 2027 to 2031 [8]: chart series and side panel from the tab; "684 by 2031, Kroger plus three accounts to be named"; "$9.4M run rate"; "46 percent"; "About 85,500"; "$261K of development". Speaker note rewritten as specified (34 percent in 2028 rising to 46 percent in 2031; half-year convention; Kroger is the majority of 2031 revenue and sites). Marker now also says unit costs are sourced.
- 10 NEW Staffing: headline, table (commissioning 1 / 1 / 2 / 2, of which new 0 / 0 / 1 / 1; TSS 1 / 3 / 6 / 7, of which new 1 / 3 / 6 / 7), stats "Jul 2027" first hire and "102 sites and 12,800 devices per service FTE in 2031", the $56.40 / $94 line, takeaway, marker and notes as specified.
- 11 Anchor accounts [9]: Kroger card line changed to "contributes to the launch"; 429 stores and 48 percent from the tab. Notes add the three questions for Bob and Bill and "At Kroger's 8,000 cameras a year, the $5 fee is about $40K a year against a $261K build." Marker added (the slide shows model figures).
- 12 Market [10]: stats ($1.31B, $416M, $9.4M run rate labelled "The 2031 plan, annualized run rate", 2.1%) and sector table from the tab. Takeaway "about 2 percent". Marker starts "Illustrative."
- 13 Evidence and estimates [11]: two items added to the estimate column.
- 16 Appendix, fee build [14]: figures from the tab; row "Implied price per device per month" added; "about $6,500 a year". Marker starts "Illustrative." Takeaway band added.
- 17 Appendix, capital and cash [15]: stats from the tab ($8.0M, $2.3M, 2031, $261K).
- 19 Slides by audience [17]: grid rebuilt with rows 7 and 10 and the new numbering; counts computed in the script: "Sean sees thirteen slides, Bill ten, a seller nine. Slide 16 carries component costs..."; "...is 17, capital and cash: the AOP figure is the $261K of 2027 development on slide 9". Notes updated to include the seller and staffing slides in the routes. Takeaway band added.
- 2, 3, 5, 14, 15, 18, 20: unchanged.

## 4. Rendering defects found and fixed

- Slide 7: first render left about 0.9 in of empty card below the commission split. Enlarged the value, pool and split type and spacing so the content fills the card.
- Slide 10: first render left a band of empty space under the table. Taller table rows and larger type, second stat and the rate line moved down.
- Slide 12: adding "Illustrative." wrapped the marker to two lines, and the second line touched the takeaway band. Marker moved up to 5.40 in.
- Slide 19: with two extra rows the grid ran into the two explanatory lines. Table type 9 pt, cell top and bottom margins 0.01 in, row height 0.20 in; text moved to 5.43 in, takeaway band fits below.
- Re-rendered after fixes; every slide read, no overflow or overlap remains.

## 5. Not done exactly as specified, and why

1. Staffing headline year. The specified text says commissioning is carried by the existing team "through 2030". At 1.0 FTE capacity the model needs a second commissioning head in 2030 (2030 FTE at utilization is 1.10, which rounds up to 2 heads), so Staffing row 18 shows one net new head in 2030. The headline year is now a Deck Figures formula (comm_absorbed_through, last year before row 18 turns positive) and reads 2029. The takeaway "Commissioning is absorbed" is kept as specified; it is true through 2029 only. Darryl's own note (new heads needed by 2031) and the model disagree by one year; setting Inputs C75 to 1.1 would make both read 2030. I did not change the input.
2. build_2027. Spec says Model C36, which is build labour only ($216K). The deck and the Kroger note both use $261K, which is Model C36 + C37 (labour plus 2027 licences and field hardware). build_2027 is defined as C36 + C37 so the deck keeps $261K; build_labour_2027 (C36, $216K) is listed beside it.
3. TSS "of which new hires". Deck Figures specifies no TSS new-hire series. The model assumes no existing TSS capacity, so every TSS head is a new hire; tss_new_2028..2031 link to Staffing row 27 and equal the head counts.
4. Commission strawmen use the published (rounded) fee, not the unrounded model fee, so that three years of the fee on the slide equals the contract value on the slide. Contract years link to Inputs C26 (3).
5. Extra Deck Figures keys added because the slides display them: payback_max, target_margin, software_share_large, gm_pct words, kroger site and revenue shares (to verify the "majority" note), kroger_cameras_per_year, camera_fee, kroger_camera_fee_annual, som_share_whole, commission_rate, contract_years, share_check, rate_chain_check, staffing_tieback.
6. Slide 8 speaker note corrections. The v4.1 note said the fee is "held at $14,000" and margin is lower at Large; with cost-plus fees all sizes earn 40 percent, so that sentence is removed. It said the Large upfront cost is "more than one year of fee"; it is $13,909 against a $15,700 fee, so it now reads "close to a full year of fee". "Two thirds" software share is now the tab figure (77 percent). The takeaway's "fifteen months" became 16 months because Large payback is now 15.3 months.
7. Literals left in build3.py: "$246,787" FY27 AOP figure in the slide 4 notes (not in the workbook; slide 4 was to keep everything else), and Kroger's "$15 per camera" (a customer-quoted price the spec itself supplies, not a model figure). Non-dollar constants such as 85 percent, eight months and the 50,000-point licence are unchanged text.
8. Markers. "Illustrative." prefixed to the slide 6, 8, 12 and 16 markers, and markers added to slide 11, to meet the marker rule. Slides 7 and 10 use the specified marker text verbatim, which on slide 10 does not contain the word "illustrative".
9. Green cards. Slides 2, 4 and 5 carry more than one green card, and slide 5 has dead space in its left card; these are the unchanged build2 slides and were left as instructed.
10. README. The v4.1 note quoted the error code "#VALUE!" as text, which recalc.py's scan counts as an error (dz7 itself reports 1 error for this reason). Reworded to "VALUE errors" so the recalc reports zero.
11. Open item in the workbook, not changed: Staffing E37:E41 (role rates) are hard-coded 94, so the blended-rate check on Staffing row 47 now shows a +67 percent variance against the $56.40 cost rate. Nothing feeds the P&L from those cells. They should probably become links to Inputs C23; I left them because the brief allowed no other number changes.

## 6. Rebuild after corrections

The coordinator corrected the delivered workbook after hand-back: Staffing E37:E41 now link to Inputs C23 (blended-rate variance on row 47 is 0), and Staffing row 18 is `=MAX(0,{col}17-ROUNDDOWN(Inputs!$C$75,0))`, giving whole net new commissioning heads of 0, 0, 0, 1, 1 for 2027 to 2031. The workbook was not changed further.

- build3.py now reads `/mnt/user-data/outputs/2026-09-30_CDA_Pro_Forma_v4.2.xlsx`. The pre-correction script is kept as `build3_pre_corrections.py`.
- Every Deck Figures value the deck uses is the same as before the correction. The staffing series are unchanged (commissioning 1 / 1 / 2 / 2, of which new 0 / 0 / 1 / 1; TSS 1 / 3 / 6 / 7), and every check reads OK.
- Slide 10 headline now reads "...carried by Chad Steger's existing team through 2029, with one new head in 2030, the peak rollout year; service delivery follows the installed base and is TSS capacity that has to be built." The years and the head count come from the tab. The script also asserts that 2030 has the most new sites (Staffing row 9: 143 / 193 / 228 / 120 for 2028 to 2031).
- Slide 10 takeaway: "Commissioning needs one new head at peak; service delivery is the build, and it starts six months before the first site."
- Validation passed. Slides 6, 7, 9, 10, 11 and 19 were rendered and read with no defects. No em or en dashes. The deliverable pptx was overwritten.
- Section 5 items 1 (headline year and "absorbed") and 11 (role rates on Staffing E37:E41) are resolved by these corrections.

## 7. Third round: POD multiplier, hires by year, cash chart

Workbook (`/mnt/user-data/outputs/2026-09-30_CDA_Pro_Forma_v4.2.xlsx`, same name and version). Recalc: 0 errors across 2,096 formulas. Staffing row 70 OK in all columns, rate chain OK, sector check OK, share check OK. Apart from the new rows, every existing value in the workbook is the same as before this round.

- Inputs row 76: entroCIM component licensing multiplier, 1.00 (input). Site Tiers C18:E18 and the POD term in C68 are multiplied by it, and the G18 note is updated. At 1.00 nothing moves. A test on a scratch copy at 0.75 (not delivered) gave PODs of $750 / $1,875 / $3,750, fees of $6,678 / $9,802 / $14,589 and a complexity adder of $6,315, which confirms that the maintenance, the second collector and the fees all follow the multiplier.
- Inputs row 77: service delivery capacity TSS can absorb, 0.0 FTE (input).
- Staffing row 28: net new service delivery heads, `=MAX(0,{col}27-ROUNDDOWN(Inputs!$C$77,0))`: 0 / 1 / 3 / 6 / 7 for 2027 to 2031.
- Staffing section K, rows 78 to 80. Commissioning hires in the year (row 79): 0 / 0 / 0 / 1 / 0. Service delivery hires in the year (row 80): 0 / 1 / 2 / 3 / 1.
- Deck Figures: tss_new_2028..2031 now point to Staffing row 28 (values unchanged at 1 / 3 / 6 / 7). New keys:

| Key | Value | Display | Source |
|---|---|---|---|
| cum_cash_2027 | -260,573 | -0.26 | Model!C49 |
| cum_cash_2028 | -1,878,005 | -1.88 | Model!D49 |
| cum_cash_2029 | -2,259,250 | -2.26 | Model!E49 |
| cum_cash_2030 | -1,047,811 | -1.05 | Model!F49 |
| cum_cash_2031 | 3,328,196 | 3.33 | Model!G49 |
| comm_hire_2028..2031 | 0 / 0 / 1 / 0 | same | Staffing!D79:G79 |
| tss_hire_2028..2031 | 1 / 2 / 3 / 1 | same | Staffing!D80:G80 |
| pod_multiplier | 1.00 | 0% (discount) | Inputs!C76 |

- README v4.2 note: sentences added on the multiplier and on TSS capacity and hires by team.

Deck (overwritten; the previous script is kept as `build3_pre_round3.py`). Validation passed; slides 9, 10 and 16 were rendered and read; no em or en dashes.

- Slide 9: two native charts. On the left, revenue and gross margin columns (x 0.73, w 5.9). On the right, cumulative net cash as a green line with markers (x 6.83, w 5.76), with category labels low, major gridlines and no legend. The line reads -0.3 / -1.9 / -2.3 / -1.1 / 3.3. The text panel is replaced by one line under the charts. Headline and takeaway are as specified. Notes add that 2027 shows only the development investment and that gross margin is not shown for 2027. The script asserts that cash bottoms in 2029 and is positive in 2031, matching what the headline says.
- Slide 10: both sub-rows are relabelled "New hires in the year" and read comm_hire and tss_hire (0 / 0 / 1 / 0 and 1 / 2 / 3 / 1). Heads rows are unchanged. Notes explain that heads are cumulative and hires are the increment.
- Slide 16: unchanged figures at multiplier 1.00, confirmed on render.
- Departures: the line under the slide 9 charts sits at y 5.30 in rather than 5.35 in, for clearance above the marker at 5.62 in. The "-2.3" and "-1.1" data labels sit close to the line but stay legible.

## 8. Visual rebuild

Workbook changes are limited to new Deck Figures keys and label changes. The labels changed are Site Tiers B18 ("entroCIM component licensing"), BOM C9 ("...SkySpark licence and entroCIM licensing"), BOM D34 ("entroCIM licensing") and the three Deck Figures labels that said "PODs"; no formulas changed. The strawman deals now use the exact fee: deal_*_value is sites x fee (unrounded) x 3. Outside Deck Figures, no model value changed.

Checks: recalc 0 errors across 2,228 formulas. Staffing row 70 OK in every column. Rate chain OK. Sector check OK. Share check OK. Components check OK. Capital-by-element check OK (hardware plus the three software elements equal Model H47 within $1; the array exponent evaluated in LibreOffice, so no helper cells were needed). Waterfall check OK (all elements tie to Model H48 within $1).

New Deck Figures keys (rows 174 onward):

| Key | Value | Display | Source |
|---|---|---|---|
| serve_people_s | 338.40 | $338 | Site Tiers!C29 |
| serve_people_m | 676.80 | $677 | Site Tiers!D29 |
| serve_people_l | 1,015.20 | $1,015 | Site Tiers!E29 |
| serve_software_s | 2,075.18 | $2,075 | Site Tiers!C31 |
| serve_software_m | 2,667.96 | $2,668 | Site Tiers!D31 |
| serve_software_l | 3,655.91 | $3,656 | Site Tiers!E31 |
| serve_reserve_s | 88 | $88 | Site Tiers!C32 |
| serve_reserve_m | 88 | $88 | Site Tiers!D32 |
| serve_reserve_l | 88 | $88 | Site Tiers!E32 |
| up_hardware_s | 880 | $880 | Site Tiers!C16 |
| up_hardware_m | 880 | $880 | Site Tiers!D16 |
| up_hardware_l | 880 | $880 | Site Tiers!E16 |
| up_skyspark_s | 1,195.46 | $1,195 | Site Tiers!C17 |
| up_skyspark_m | 2,988.65 | $2,989 | Site Tiers!D17 |
| up_skyspark_l | 5,977.30 | $5,977 | Site Tiers!E17 |
| up_entrocim_s | 1000 | $1,000 | Site Tiers!C18 |
| up_entrocim_m | 2500 | $2,500 | Site Tiers!D18 |
| up_entrocim_l | 5000 | $5,000 | Site Tiers!E18 |
| up_othersw_s | 1600 | $1,600 | Site Tiers!C20 |
| up_othersw_m | 1600 | $1,600 | Site Tiers!D20 |
| up_othersw_l | 1600 | $1,600 | Site Tiers!E20 |
| up_commissioning_s | 225.60 | $226 | Site Tiers!C23 |
| up_commissioning_m | 338.40 | $338 | Site Tiers!D23 |
| up_commissioning_l | 451.20 | $451 | Site Tiers!E23 |
| fee_exact_s | 6,892.12 | $6,892 | Site Tiers!C40 |
| fee_exact_m | 10,336.29 | $10,336 | Site Tiers!D40 |
| fee_exact_l | 15,658.80 | $15,659 | Site Tiers!E40 |
| margin_kept_s | 2,756.85 | $2,757 | Site Tiers!C40 - C33 - C36 |
| margin_kept_m | 4,134.52 | $4,135 | Site Tiers!D40 - D33 - D36 |
| margin_kept_l | 6,263.52 | $6,264 | Site Tiers!E40 - E33 - E36 |
| components_check | OK | OK | Site Tiers rows 16 to 33 |
| pool_small_1 | 1,033.82 | $1,034 | deal_small_1_pool |
| pool_medium_10 | 15,504.43 | $15,504 | deal_medium_10_pool |
| pool_large_100 | 234,882.02 | $234,882 | deal_large_100_pool |
| el_development | 260,573.36 | $261K | Model!H36 + H37 |
| el_sustain | 1,352,817.63 | $1.4M | Model!H38 |
| el_commission | 1,403,006.92 | $1.4M | Model!H39 |
| el_marketing | 200000 | $200K | Model!H40 |
| el_commissioning | 279,856.80 | $280K | Model!H24 |
| el_service | 1,385,879.95 | $1.4M | Model!H25 |
| el_renewals | 3,896,660.28 | $3.9M | Model!H26 |
| el_field_reserve | 121880 | $122K | Model!H27 + H28 + H29 |
| el_revenue | 20,244,154.64 | $20.2M | Model!H20 |
| el_net_cash | 3,328,196.45 | $3.3M | Model!H48 |
| el_team | 2,955,824.55 | $3.0M | el_sustain + el_commission + el_marketing |
| el_service_reserve | 1,507,759.95 | $1.5M | el_service + el_field_reserve |
| el_cap_hardware | 619,886.22 | $620K | Accounts rows 23, 58, 93, 128, 163 (C:G) |
| el_cap_skyspark | 3,413,197.77 | $3.4M | Accounts new sites x escalation x Site Tiers row 17 by tier |
| el_cap_entrocim | 2,855,133.40 | $2.9M | Accounts new sites x escalation x Site Tiers row 18 by tier |
| el_cap_othersw | 1,127,065.86 | $1.1M | Accounts new sites x escalation x Site Tiers row 20 by tier |
| capital_element_check | OK | OK | Model!H47 |
| software_share_of_capital | 0.92 | 92% | el_cap software / Model!H47 |
| entrocim_share_of_software | 0.39 | 39% | el_cap_entrocim / software capital |
| waterfall_check | OK | OK | Model!H48 |
| annual_cash_2027 | -260,573.36 | -0.26 | Model!C48 |
| annual_cash_2028 | -1,617,431.30 | -1.62 | Model!D48 |
| annual_cash_2029 | -381,245.09 | -0.38 | Model!E48 |
| annual_cash_2030 | 1,211,439.00 | 1.21 | Model!F48 |
| annual_cash_2031 | 4,376,007.21 | 4.38 | Model!G48 |
| cum_cash_end | 3,328,196.45 | $3.3M | Model!G49 |
| cash_trough_year | 2029 | 2029 | Model!C49:G49 |
| som_share_revenue | 0.02 | 2.2% | Summary!C25 / Summary!C36 |
| comm_heads_2027 | 0 | 0 | Staffing!C17 |
| tss_heads_2027 | 0 | 0 | Staffing!C27 |
| comm_hire_2027 | 0 | 0 | Staffing!C79 |
| first_hire_month | Jul 2027 | Jul hire | Staffing!C33 |

Slides changed. The deck was validated, every slide was rendered and read, and there are no em or en dashes and no "PODs" anywhere in slide text or notes. The contact sheet is `2026-09-30_CDA_Deck_Contact_Sheet.jpg`.

- 2 After the sale: two lanes, Today and With CDA (Sale, Install, Year 1 to 5). Dashed divider labelled "Today, Wesco's role ends here". Today lane has a dashed baseline, two labels and a grey wedge to "Risk builds quietly". The CDA lane has five green "Annual fee" blocks. The four upper and two lower cards are removed, the takeaway is new, and there is no marker. Notes carry Bill's 85 percent as the source and say the five-year span is a drawing convention.
- 3 The service: green "One annual fee per site" band holding three navy segments (Inventory, Patch, Secure), with the chips beneath. The two cards are removed; their "never does" content moved into the notes.
- 4 Why Wesco: four navy blocks; green arrows converge on an outline box "What is new..."; one green card "Already built, in production...". The two sentences that sat between the cards moved to the notes.
- 5 Three platforms stronger: arrows 0.5 x 0.36 in, green.
- 6 How it sells: four-column price table; grey 9.5 pt per-device comparison line.
- 7 What a seller earns: site squares (1, 10, 100), "N x fee a year" with the three-year value, commission-pool bars to one scale (largest green), and the split under each bar.
- 8 One site: three stacked bars (cost to serve navy, upfront recovered light grey, margin kept green) scaled to the exact fee, with 40% and payback at the right. A components line and the exact-fee table sit beneath. The stat row and card are removed; new takeaway.
- 9 Plan: revenue and margin columns; cumulative-cash line with the value axis fixed at -3 to 4. The zero line is drawn by the category axis crossing at zero. Phase labels are aligned to the category positions using a manual plot layout. Callouts read "Peak investment $2.3M" and "Break-even 2031". A six-figure "What the cash buys" strip, new headline and takeaway, and notes on the internal entroCIM charge.
- 10 Staffing: 2027 column added (heads 0, commissioning hires 0, TSS hires "Jul hire").
- 11 Anchor accounts: three bands (Engaged, Scoping, To name): Kroger green, Cisco slate, three outlined empty cards.
- 12 Market: nested bars to one scale (TAM, SAM, plan sliver in green) and the sector table. The takeaway uses the revenue share (2.2%).
- 13 Evidence and estimates: moved to the Blank-with-Title layout. Five-box chain (Unit cost and Price solid; Sites, Revenue and Cash dashed) with reasons and a legend. Two short lists beneath.
- 14 What is needed: three navy cards left to right with green arrows; owner labels in slate.
- 17 Capital and cash: waterfall by element (invisible base series; navy outflows, green revenue, navy net-cash total) with element labels below each step. The four stats are kept; new headline and takeaway. The "still needs a decision" card content moved to the notes.
- 16: unchanged; the entroCIM row label and per-device row already read from keys.
- 1, 15, 18, 19, 20: unchanged.

Not done exactly as specified:
1. Commission pools use the exact fees, as instructed. They read $1,034 / $15,504 / $234,882, not the $1,035 / $15,450 / $235,500 quoted in the brief, which came from the rounded fees.
2. Slide 17 takeaway: "a third" is replaced by the tab figure, "39 percent" (entroCIM licensing is 39 percent of software capital; software is 92 percent of capital). The rest of the sentence is as specified.
3. Slide 9: no pattern-filled area under zero. Shading was optional in the brief, so it was omitted. The zero line is the category axis at zero plus gridlines.
4. Slide 13: the estimate list has four items (the four named in the brief); the known list has three.
5. Slide 13 had no headline before; one was added to meet the one-headline rule: "What is sourced today, and what a pilot has to prove."
6. Slide 17: the model's field reserve ($122K) is not in the brief's element list. It is folded into "Service and field reserve" so the waterfall ties to net cash.
7. Slide 8 keeps its kicker "Large site, about 200 devices" and its headline, although the slide now shows all three sizes.
8. Slide 11: the Kroger and Cisco card lines are merged into two lines each to fit the band. The "Three more to name" card text moved to the notes.
9. Slides 2, 3, 4, 5, 13 and 14 carry no marker because they show no model figures.

## 9. US English, one-chart plan slide, platform licensing pair

Workbook: recalc 0 errors across 2,230 formulas. Staffing tie-back OK in all five years; rate chain, sector, share, components, capital-by-element and waterfall checks all OK. No numeric value changed.

- US English replacements, case-preserving, text cells only: no cell whose value starts with "=" and no Deck Figures key in column B. 64 replacements in the workbook: README 9, Inputs 9, BOM 7, Site Tiers 13, Device Classes 1, Staffing 4, Deck Figures 21. None of the listed UK spellings remain. The key `build_labour_2027` keeps its name as instructed.
- 19 replacements in `build3.py`: licence 12, licences 4, labour 2, Labour 1. None of the listed UK spellings remain in slide text or notes.
- New key: `el_cap_platform` = el_cap_skyspark + el_cap_entrocim = $6,268,331, displayed "$6.3M". Source: el_cap_skyspark + el_cap_entrocim. Slide 9.

Deck: validation passed. Slides 6, 8, 9, 10, 16 and 17 (the slides whose visible text or layout changed) were rendered and read. No em or en dashes. The contact sheet has been regenerated.

- Slide 9: one combo chart, 11.86 in wide at x 0.73, y 2.0, 2.95 in tall. Revenue is light grey columns; cumulative net cash is a green line with markers. The line is a `c:lineChart` injected into the same plot area, sharing the bar chart's two axis ids. It validated natively, so no fallback was needed. One value axis runs from -3 to 10; the category axis crosses at zero, drawing the zero line. Data labels are 0.0 on both series, with the cash labels below the points so they clear the line. The legend at the bottom names both series. Phase labels are aligned to the categories through a manual plot layout. Callouts "Peak investment $2.3M" (under the zero line at 2029) and "Break-even 2031" (at the zero crossing). Gross margin is off the chart. The takeaway is as specified, with $3.3M from `cum_cash_end`: `cum_cash_2031` is a numeric chart value, and `cum_cash_end` is the same cell (Model G49) formatted for text.
- Slide 9 strip: five items. The platform item reads "$6.3M entroCIM platform licenses", with "SkySpark $3.4M external, entroCIM components $2.9M internal" beneath. Speaker note: SkySpark points are drawn from a license bought from SkyFoundry and are external cash; the entroCIM component charge is internal. Gross margin 2028 and 2031 figures are kept in the note for questions.
- Slide 17: SkySpark and entroCIM remain separate steps.
- Noted: the slide 8 headline ("What a site costs Wesco to stand up... Kroger stores are the Large case.", no kicker) was already changed in `build3.py` before this round; it was kept as found.
