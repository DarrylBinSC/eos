# CDA vs. SecuriThings Cost Comparison

Prepared 2026-10-26 for Darryl Benson. Internal working document; carries entroCIM licensing and pro forma figures that do not leave the team (pro forma sharing rule, 2026-10-02).

Sources: SecuriThings pricing framework, "Wesco <> SecuriThings - Overview, Pricing Framework, ROI - 6.16.26 - SHARED" (vendor deck, hosted annual subscription prices, dated 2026-06-16; a framework, not a quote). CDA figures from `2026-10-02_CDA_Pro_Forma_v4.6.xlsx`, Deck Figures tab (fees held at $6,900 / $10,300 / $15,700, 2026-10-01 decision; typical devices per site 40 / 100 / 200; cost to serve from Site Tiers rows 29 to 33). Derived figures are arithmetic on those two sources and are marked. Nothing here is a like-for-like product comparison: SecuriThings sells software the customer's own staff operate; CDA sells a managed service with people, an appliance where one is used, and field remediation.

## 1. Price per device per year

| | Per device per year | Per device per month | Basis |
|---|---|---|---|
| SecuriThings, Essentials only | $8.20 (3,000) to $7.19 (10,000) | $0.68 to $0.60 | Required base; inventory, up/down, EOL/EOS, vulnerability, compliance |
| SecuriThings, Essentials + Operations | $20.49 to $17.97 | $1.71 to $1.50 | Adds health, alerts, RCA, restarts, ITSM |
| SecuriThings, all modules | $36.89 to $32.34 | $3.07 to $2.70 | Adds Cyber (firmware, password, certificate, hardening) and API |
| SecuriThings, all modules, on-premises | $55.33 to $48.51 | $4.61 to $4.04 | +50% uplift, vendor-stated |
| CDA, Small site (40 devices) | $172.50 | $14.38 | $6,900 fee |
| CDA, Medium site (100 devices) | $103.00 | $8.58 | $10,300 fee |
| CDA, Large site (200 devices) | $78.50 | $6.54 | $15,700 fee |
| CDA from year four at the same margin | $132 / $71 / $50 | $11.04 / $5.94 / $4.13 | $5,300 / $7,100 / $9,900 option, not published |

Reading: on the published fee CDA is 2.1x (Large) to 4.7x (Small) SecuriThings' all-modules price, and 10x to 24x its Essentials-only price. From year four the Large gap narrows to about 1.3x.

## 2. A 3,000-device customer, annual and five-year

SecuriThings' own environment slide uses 3,000 devices (Wesco's camera count). The same count on CDA is 15 Large sites, 30 Medium or 75 Small.

| | Year 1 to 3, annual | Five years | Per device per year, five-year average |
|---|---|---|---|
| SecuriThings, all modules | $110,663 | $553,315 (about $526K with the 5% five-year prepay) | $36.89 |
| SecuriThings, Essentials + Operations | $61,480 | $307,400 | $20.49 |
| CDA, 15 Large sites | $235,500 | $1,003,676 (years 4 and 5 at the year-four fee) | $66.91 |
| CDA, 30 Medium sites | $309,000 | $1,354,876 | $90.33 |
| CDA, 75 Small sites | $517,500 | $2,347,095 | $156.47 |

## 3. What the customer still pays for on top of SecuriThings (their own numbers)

SecuriThings' ROI slide says a 3,000-device estate costs $979,500 a year to maintain without automation and $84,500 a year with SecuriThings. The $84,500 is the labor the customer still carries: $28.17 per device per year. Adding it to the subscription gives the vendor's own all-in view of the customer's cost. These are vendor assumptions; none are sourced.

| 3,000 devices, five years | Subscription | Residual labor (vendor's figure) | All-in | Per device per year |
|---|---|---|---|---|
| SecuriThings, all modules | $553,315 | $422,500 | $975,815 | $65.05 |
| SecuriThings, Essentials + Operations | $307,400 | $422,500 | $729,900 | $48.66 |
| CDA, 15 Large sites | included | included | $1,003,676 | $66.91 |
| CDA, 30 Medium sites | included | included | $1,354,876 | $90.33 |

Reading: on SecuriThings' own residual-labor assumption, a Large-site CDA customer pays about the same over five years as a SecuriThings all-modules customer, and gets Wesco's people, field remediation and dispatch for it. At Medium the CDA premium is about 40 percent; at Small it is roughly 2.4x. The vendor's "without automation" baseline, $326.50 per device per year, is the ceiling either offer is priced under.

## 3b. Price difference with the service layer added to SecuriThings (Darryl's framing, 2026-10-26)

Assumption: the customer has not bought services from an integrator. To get what CDA embeds, a SecuriThings customer buys the subscription and then buys or staffs the service hours. Two ways to value those hours, both per device per year at 3,000 devices:

- **CDA's own service content at the Wesco budget rate:** the hours CDA delivers (1.5 / 2.25 / 3.25 per site per month) at $94 an hour. The $94 rate carries Wesco's target margin, so it stands in for a purchased rate. Conservative: it prices only the hours, not an integrator's deployment, truck rolls or program management.
- **The vendor's own residual-labor figure:** $28.17 per device per year (SecuriThings ROI slide; unsourced).

| Per device per year, years 1 to 3 | Small (40) | Medium (100) | Large (200) |
|---|---|---|---|
| SecuriThings, all modules | $36.89 | $36.89 | $36.89 |
| CDA service hours at $94 | $42.30 | $25.38 | $18.33 |
| **SecuriThings + hours** | **$79.19** | **$62.27** | **$55.22** |
| **CDA fee** | **$172.50** | **$103.00** | **$78.50** |
| Difference, CDA over SecuriThings + hours | +$93.31 (2.2x) | +$40.73 (1.65x) | +$23.28 (1.42x) |
| Same, using the vendor's residual labor ($65.05) | +$107.45 | +$37.95 | +$13.45 |
| Same, if the customer buys Essentials + Operations only ($20.49 + hours) | +$109.71 | +$57.13 | +$39.68 |
| CDA from year four at the same margin | $132.43 | $71.31 | $49.53 |
| Difference from year four, CDA over SecuriThings + hours | +$53.24 | +$9.04 | **-$5.69** |

For the 3,000-device, 15-Large-site case: CDA is $69,840 a year above SecuriThings plus hours in years 1 to 3, and $17,070 a year below it from year four if the year-four fee is offered.

What the gap is made of at Large: CDA's $78.50 is $23.62 of cost to serve in the price build, $23.18 of upfront recovery (appliance, SkySpark and entroCIM licenses, commissioning, recovered over three years) and $31.70 of margin. SecuriThings plus hours at $55.22 has no upfront recovery in it. So the years-1-to-3 premium at Large is, to within a few dollars, the platform recovery; once it is recovered CDA is the cheaper offer with the service included. At Medium and Small the premium is structural, because the same stack is spread over fewer devices.

Left out of the SecuriThings side, all of which would raise it: the connector host and its deployment, an integrator's margin and program management if the hours are bought rather than staffed, truck rolls (CDA carries an $88 field reserve per site), and the on-premises uplift (+50%) if the customer will not accept Azure hosting.

## 4. What it costs Wesco to deliver (not customer-facing)

| Per device per year | Small | Medium | Large |
|---|---|---|---|
| CDA cost to serve (people, software renewals, field reserve) | $79.46 | $42.79 | $29.72 |
| of which software and license maintenance | $51.88 | $26.68 | $18.28 |
| CDA upfront per site (appliance, SkySpark and entroCIM licenses, other software, commissioning) | $4,901 | $8,307 | $13,909 |

Reading: Wesco's cost to serve a Large site, $29.72 per device, is about what SecuriThings charges a customer for all modules ($32 to $37). CDA's software stack alone (SkySpark, entroCIM licensing, Nozomi, RMM, Airwall) costs $18 to $52 per device per year to run, which is more than SecuriThings' Essentials + Operations price at every tier and more than its all-modules price at Small. The per-site model prices the same stack whether a site has 40 devices or 200, which is why Small is where the comparison fails.

## 5. Deployment model (Darryl, 2026-10-26)

CDA can be deployed centrally in the same way entroCIM is. The device-centric, appliance-per-site model was chosen so that local networks are covered by the auto-discovery tool, which typically works better than a centralized model; in large enterprises a parallel, centrally deployed model may be the better fit. SecuriThings is central by construction (one connector host per data center, proxies on NVRs for segregated sites). The pro forma prices the appliance-per-site model only; a central CDA variant (no $880 appliance per site, license draw by central deployment rather than per site) is not modeled, and the small-branch cases raised on 2026-10-02 (banks, under ten devices) would price differently under it.

## 6. What the comparison does not settle

- SecuriThings' prices are a June 2026 framework to Wesco as an end customer; enterprise, partner and MSSP terms are not stated.
- The CDA fee includes labor at 1.5 / 2.25 / 3.25 service hours per site per month; whether that covers the Cyber-module functions SecuriThings automates (firmware, password and certificate rotation at fleet scale) depends on the launch scope, which is read-only on devices today.
- Device counts per tier are modeling assumptions (40 / 100 / 200), not account data.
- The residual-labor figure in section 3 is the vendor's.

## 7. Raw costs side by side (added 2026-10-26, end of day)

SecuriThings' figures are its prices to a customer at 3,000 devices (its own cost is unknown). CDA's figures are Wesco's costs before margin, from the pro forma: steady-state software renewals (full, not the price-build "renewals counted"), service labor at the $56.40 cost rate, the field reserve, and the upfront components spread over the three-year recovery. Per device per year.

| | SecuriThings (3,000 devices) | | CDA Small (40) | CDA Medium (100) | CDA Large (200) |
|---|---|---|---|---|---|
| Essentials | $8.20 | Software renewals (SkySpark, entroCIM, Nozomi, RMM, Airwall) | $51.88 | $26.68 | $18.28 |
| Cyber Protection | $12.30 | Service labor at cost | $25.38 | $15.23 | $11.00 |
| Operational Management | $12.30 | Field reserve | $2.20 | $0.88 | $0.44 |
| Enterprise Extension (API) | $4.10 | Upfront, over 3 years: appliance and staging | $7.33 | $2.93 | $1.47 |
| | | Upfront: SkySpark license draw | $9.96 | $9.96 | $9.96 |
| | | Upfront: entroCIM licensing (internal charge) | $8.33 | $8.33 | $8.33 |
| | | Upfront: sensing and connectivity software | $13.33 | $5.33 | $2.67 |
| | | Upfront: commissioning | $1.88 | $1.13 | $0.75 |
| **All modules** | **$36.89** | **Total cost, years 1 to 3** | **$120.30** | **$70.48** | **$52.90** |
| All modules, on-premises | $55.33 | Total cost from year four (no upfront) | $79.46 | $42.79 | $29.72 |
| | | Published fee (for reference) | $172.50 | $103.00 | $78.50 |

Reading: Wesco's raw cost at Large in years 1 to 3 ($52.90) is 1.4x SecuriThings' all-modules customer price, and from year four ($29.72) is below it. The software line alone ($18.28 at Large, $51.88 at Small) is the part to watch: it is Wesco's cost for the stack, before any people, and at Small it already exceeds SecuriThings' all-modules price. SkySpark and entroCIM licensing are a flat $18.29 per device per year at every tier over the recovery period because the license draw scales with devices; the appliance, other software and commissioning are what penalize Small.

## 8. Software-only option: CDA without the services (Darryl's direction, 2026-10-26)

Darryl: an option may be needed to price CDA when the customer wants someone else to supply the services, which means pulling the people out of the cost to serve. Arithmetic on the current model, at the 40 percent target margin, with service labor removed and the field reserve retained:

| | Small | Medium | Large |
|---|---|---|---|
| Fee, years 1 to 3 (software, reserve, upfront recovery, margin) | $6,328 ($158.20/device) | $9,208 ($92.08) | $13,967 ($69.83) |
| Fee from year four | $3,605 ($90.13) | $4,593 ($45.93) | $6,240 ($31.20) |
| SecuriThings all modules, for reference | $36.89 | $36.89 | $36.89 |

Reading: a software-only CDA at Large reaches SecuriThings' price only from year four; in years 1 to 3 it is 1.6x. At Medium and Small it does not get there. This is arithmetic on today's assumptions, not a priced option; it is the case for revisiting them.

**Assumptions Darryl has said need revisiting (2026-10-26), with the candidates this comparison surfaced:** devices per site (40 / 100 / 200 are placeholders; the per-site stack is the same at 40 as at 200); the appliance-per-site basis (a central deployment removes the appliance and changes the license draw); the sensing and connectivity software at a flat $1,600 per site; the three-year recovery period against a competitor with no upfront; service hours per site; and whether the fee is built per site or per device for enterprise rollouts (the 2026-10-02 enterprise-pricing question). Not yet logged as a register item; Darryl's call.

## 9. Recurring and one-time separated (Darryl's direction, 2026-10-26; supersedes the blended views above for working purposes)

The three-year amortization of the upfront is taken out of the annual figures. Annual is recurring cost only; deployment is a separate one-time cost per site. SecuriThings' prices are annual subscription; its deployment cost (connector host, integration setup) is not stated in the deck and is shown as unknown.

**Annual recurring, per device per year**

| | SecuriThings (3,000 devices) | | CDA Small (40) | CDA Medium (100) | CDA Large (200) |
|---|---|---|---|---|---|
| Essentials | $8.20 | Software renewals | $51.88 | $26.68 | $18.28 |
| Cyber Protection | $12.30 | Service labor at cost | $25.38 | $15.23 | $11.00 |
| Operational Management | $12.30 | Field reserve | $2.20 | $0.88 | $0.44 |
| Enterprise Extension | $4.10 | | | | |
| **All modules (customer price)** | **$36.89** | **Wesco raw cost, full service** | **$79.46** | **$42.79** | **$29.72** |
| Essentials + Operations | $20.49 | Wesco raw cost, software only (people out) | $54.08 | $27.56 | $18.72 |
| All modules, on-premises | $55.33 | | | | |

**Annual fee at the 40 percent target margin, per site and per device**

| | Small | Medium | Large |
|---|---|---|---|
| Full service | $5,297 ($132.43) | $7,131 ($71.31) | $9,906 ($49.53) |
| Software only (people out) | $3,605 ($90.13) | $4,593 ($45.93) | $6,240 ($31.20) |
| SecuriThings all modules + CDA's service hours at $94 (from section 3b) | $79.19 | $62.27 | $55.22 |
| SecuriThings all modules alone | $36.89 | $36.89 | $36.89 |
| Full service minus SecuriThings + hours | +$53.24 | +$9.04 | -$5.69 |
| Software only minus SecuriThings all modules | +$53.24 | +$9.04 | -$5.69 |

**One-time deployment, per site (separate)**

| | Small | Medium | Large |
|---|---|---|---|
| Wesco cost (appliance $880, SkySpark draw, entroCIM licensing, sensing and connectivity software $1,600, commissioning) | $4,901 ($122.53/device) | $8,307 ($83.07) | $13,908 ($69.54) |
| Charged at the 40 percent margin | $8,168 ($204.21) | $13,845 ($138.45) | $23,181 ($115.90) |
| SecuriThings deployment | not stated; connector host and integration setup are the customer's or an integrator's; pilot offers imply low setup |

Reading, once the deployment is a separate line:
- On recurring cost alone, CDA at Large is cheaper than SecuriThings on every basis: Wesco's raw cost ($29.72) is below SecuriThings' all-modules price, and the full-service fee at target margin ($49.53) is below SecuriThings plus the service hours ($55.22). Medium is within $9 per device. Small remains 1.7x.
- Software only, CDA's recurring fee at Large ($31.20) is below SecuriThings all modules ($36.89) and at Medium ($45.93) is $9 above it; the raw software cost at Large ($18.72) is below SecuriThings' Essentials + Operations price.
- The whole of CDA's price disadvantage in the earlier views was the deployment. As a one-time line it is $69.54 to $122.53 per device at cost, $116 to $204 at margin, against a competitor that charges nothing stated for deployment. How that line is presented (charged, amortized into year one, waived against a term, or absorbed) is the pricing decision, and it is a different decision from the recurring fee.
- Deployment per device is driven by the per-site fixed items (appliance $880, sensing and connectivity software $1,600, commissioning); the license draw is the same $18.29 per device at every tier over three years, or $54.86 per device one-time. A central deployment changes the fixed items, not the license draw, unless the draw basis changes too.
