# Airwall Competitive Analysis — Wesco Buyer Lens

**Date:** 2026-09-17
**Prepared for:** Darryl Benson, Senior Director, CSS Platforms
**Trigger:** Gartner survey question forwarded by JCI asking which vendors Wesco considered alongside Johnson Controls during vendor selection, and which participated in a POC
**Companion reference:** `Products/JCI_Airwall_Competitive_Landscape.md` (per-vendor catalog)
**Related:** `Products/JCI_Partnership.md`
**Revised:** 2026-09-17, twice the same day, on Darryl's correction of the selection-history assumption and his designation of the MSP contract as the baseline for Airwall and Conductor technology use. See Section 9.
**Standing:** this is the **pre-baseline record**. It documents what was true before the MSP contract resets the terms. Retain; do not extend.

---

## Bottom line

**Answer "Not Considered" for all twelve.** Confirmed by Darryl 2026-09-17: Airwall has been in the entroCIM deployment architecture for roughly a decade, any vendor consideration was completed before he joined the company, and no Wesco selection procedure has occurred. The survey's "if applicable" qualifier applies. There is no selection procedure to report, and the response can be submitted now.

The remaining finding is narrower than it first appeared, and worth stating precisely. Wesco has a **sole-source architectural dependency on Airwall for hosted entroCIM connectivity, a decade-old selection that has never been revisited, and an unsigned supplier agreement with that vendor after eleven months of negotiation.** The dependency is real. What is absent is a *current, written* rationale, not informed judgment: Darryl has eight years of direct Airwall experience, including independent adoption of the same technology for the same job at Intelligent Buildings before May 2025. Two organizations in this industry reaching the same architectural answer independently is meaningful validation. It is simply not written down, and a decade is long enough that the market it was decided against no longer exists in the same form.

A second finding is that Gartner's list is the wrong market. Eleven of the twelve vendors solve enterprise microsegmentation, which is not the job Wesco uses Airwall for. Only Onclave Networks is a genuine architectural peer, and the most likely real-world substitutes (Tosibox, a WireGuard-based service, Cisco Secure Equipment Access, conventional site-to-site VPN) do not appear on the list at all.

---

## 1. What the survey is actually asking, and what it is not

Gartner is surveying the **Network Security Microsegmentation** market. The twelve named vendors are that market's roster: Illumio, Akamai, ColorTokens, Zero Networks, Elisity, Broadcom, Zscaler, and Cisco are microsegmentation vendors; Ordr and Asimily are connected-device visibility and risk vendors; SideChannel serves the SMB end of segmentation; Onclave is an OT zero trust overlay.

JCI positions Airwall in that market. **Wesco does not buy it for that job.** Wesco uses Airwall as the connectivity layer that lets Wesco-hosted entroCIM reach equipment and building systems inside customer networks Wesco neither owns nor administers, without requiring the customer to operate or see the platform.

That distinction matters commercially. A survey response recorded against the microsegmentation market implies Wesco evaluated Airwall as a microsegmentation product and chose it over Illumio and Zero Networks. Wesco did not. Left uncorrected, the response reads as a competitive win in a market Wesco was never shopping in.

## 2. Current state: how Wesco arrived at Airwall

| Element | Status | Basis |
|---|---|---|
| Airwall in production for hosted entroCIM | Yes | `JCI_Partnership.md`, 2026-07-15 transcript |
| Conductor hosted in Wesco Azure, HA pair plus relay | Yes, operational since approximately 2026-07-17 | Darryl, 07-17 |
| 443-only connectivity available | Confirmed 2026-07-15; future installs to be configured this way | Priya Agarwal, JCI |
| Airwall in the entroCIM deployment architecture | **Approximately ten years** | Darryl, 2026-09-17 |
| Wesco vendor selection procedure or POC against alternatives | **None. Selection completed before Darryl joined** | Darryl, 2026-09-17 |
| Darryl's direct Airwall experience | **Eight years**, including secure remote connectivity at Intelligent Buildings pre-May 2025 | Darryl, 2026-09-17 |
| Supplier agreement signed | **No.** Wesco markup sent to JCI 2026-08-31; JCI response not received | Darryl, 2026-09-01 |
| Approximately ten contractual issues open | Yes | `JCI_Partnership.md`, 2026-07-17 review |

**Confirmed 2026-09-17.** Airwall predates Wesco's acquisition of entroCIM by a wide margin, consistent with the documented migration out of the legacy pre-acquisition hosted environment. The selection was made roughly a decade ago by the pre-acquisition entroCIM organization, against a vendor landscape that no longer resembles the current one. No Wesco procurement evaluation has ever been run, which is the accurate survey answer.

Separately, and this matters to how much weight the missing documentation should carry: **Darryl independently selected and operated Airwall for secure remote network connectivity at Intelligent Buildings** in his prior role, before May 2025. The architectural fit for this job has been validated twice, in two organizations, by an operator with eight years on the technology. That is not a substitute for a written rationale, but it is a substantial difference from an inherited dependency nobody understands.

## 3. The material issue

**Revised from the first draft.** The original framing, that Wesco holds no internal position on replacement, was wrong and Darryl corrected it. The position exists and is well founded; it is held personally rather than institutionally, and it was formed against a market that has since changed.

The accurate statement of the issue is narrower and still worth acting on:

1. **The rationale is undocumented and personally held.** It sits with Darryl and, presumably, with long-tenured entroCIM deployment staff. It is not written anywhere a successor, a security reviewer, a customer's IT organization, or Brian Miller could use it.
2. **It was decided roughly a decade ago.** Zscaler's Airgap acquisition, Elisity, Zero Networks, and the maturation of the agentless OT segmentation category all postdate it. The decision has never been tested against any of them. This is not a reason to expect a different answer, and Section 6 concludes the answer would very likely be the same. It is a reason to have a current one.
3. **The agreement is unsigned.** Negotiating from a decade-old, undocumented, sole-source dependency is a weaker position than negotiating from a current, written one, whether or not the analysis is ever shown to JCI.

**Resolution, Darryl 2026-09-17: the MSP contract becomes the baseline for Airwall and Conductor technology use.** That is a better answer than the standalone rationale document this section originally recommended, and it closes items 1 and 3 at signature rather than through a side artifact. The contract is enforceable, is the thing Wesco actually operates under, and supersedes both the decade of undocumented practice and the verbal understandings from the 2026-07-15 partner meeting.

It also relocates the risk rather than removing it. **A baseline contains only what is captured in it.** The items that must be in the agreement text, or in a referenced document JCI cannot change unilaterally, are listed in `Products/JCI_Partnership.md` under the 2026-09-17 baseline entry: licensing mechanics, express hosting rights, JCI support obligations, and metering API data scope. Darryl's own 07-17 durability requirement is the governing test, and it applies to the baseline as a whole, not only to the licensing terms it was written about.

Item 2, that the decision has never been tested against the current vendor landscape, is what this analysis answers. Section 6 concludes firmly against replacing Airwall.

## 4. Vendor assessment against Wesco's actual requirement

Wesco's requirement, stated plainly: reach customer-site building systems from a Wesco-hosted application, across customer-controlled networks, outbound-only, through a single port, with no customer operation of the platform, in front of legacy controllers that cannot host an agent, including air-gapped sites.

| Vendor | Category | Meets Wesco's requirement | Note |
|---|---|---|---|
| Onclave Networks | OT zero trust overlay | **Partially, and the closest peer** | Cryptographic overlay, agentless on legacy OT, air-gap capable, federal ATO. No building-automation or BACnet positioning found; no channel comparable to JCI's |
| Zscaler (Airgap) | Microsegmentation, cloud-delivered | Low | Agentless OT segmentation is adjacent, but requires the customer to be a Zscaler tenant or Wesco traffic in Zscaler's cloud. Heavier ask of customer IT than an outbound 443 tunnel |
| ColorTokens | Microsegmentation | Low | Gateway form factor fits legacy controllers, but solves segmentation at the site, not managed reachability from a hosted application |
| Cisco Systems | Multi-product OT security | Low for the job, **high as an objection** | Most likely alternative to be already present at a large customer site, and therefore the one customer IT is most likely to raise against introducing Airwall |
| Akamai (Guardicore) | Microsegmentation | Low | Agentless IoT/OT mode still presumes enforcement points inside an administered network |
| Elisity | Microsegmentation | Low | Requires control of the customer's Cisco or Juniper switching. Wesco neither has nor wants that |
| Illumio | Microsegmentation | None | Segments workloads. No mechanism for reaching an unowned network |
| Zero Networks | Microsegmentation | None | Orchestrates host firewalls on operating systems Wesco does not administer |
| Broadcom (vDefend/NSX) | Hypervisor firewall | None | Building systems are not VMware workloads |
| Ordr | Device visibility and risk | None for connectivity | **Adjacent to entroCIM's own asset inventory, not to Airwall.** Watch as a capability comparison |
| Asimily | Device visibility and risk | None for connectivity | Same adjacency, narrower vertical (IoMT) |
| SideChannel (Enclave) | SMB segmentation, MSP-delivered | None on capability | **Useful as precedent:** an existence proof that MSP-delivered segmentation is a normal commercial structure, not a concession JCI is granting |

## 5. What a real shortlist would look like today

If Wesco re-ran the selection now for the connectivity job, the credible shortlist would be:

1. **JCI OpenBlue Airwall** (incumbent). HIP-based cryptographic overlay, outbound 443, gateway for legacy controllers, building-industry alignment through JCI ownership.
2. **Onclave Networks.** The only true architectural substitute on Gartner's list.
3. **Tosibox.** Established in building automation and industrial remote access; the most likely direct substitute in a BAS context. Absent from Gartner's list because it is not a microsegmentation product.
4. **A self-built WireGuard-based overlay** (Tailscale, NetBird, or direct WireGuard) hosted in Wesco Azure. Lower licence cost, materially higher Wesco engineering and support obligation, and no vendor to escalate to.
5. **Cisco Secure Equipment Access**, where the customer is Cisco-standardized.

Conventional site-to-site IPsec VPN or SD-WAN remains the option customer IT most often proposes, and the one Airwall's outbound-only, cloaked posture is designed to beat in security review.

## 6. Switching cost assessment

**Recommendation: do not switch.** The assessment below is for negotiating awareness and risk documentation, not as a proposal.

- **Installed base, accumulated over approximately a decade.** Every live entroCIM site with hosted telemetry runs through Airwall gateways. Replacement is a per-site truck roll plus a customer security re-approval, not a software migration. Ten years of deployment means the base is larger, more varied, and more embedded in customer-side documentation and firewall rules than a recent dependency would be.
- **Customer security review.** Each customer's IT organization approved Airwall specifically. A replacement re-opens that approval at every site, which is the largest hidden cost and the one most likely to stall.
- **Wesco Azure investment.** The HA Conductor pair, relay, and the WAB approval path for the metering agent are Airwall-specific and would be written off.
- **Commercial value at risk.** The MSP agreement's value thesis, consumption billing from a pre-granted licence pool with pay-on-provisioning and true-down, is Airwall-specific. Switching forfeits the gain the negotiation is being run to secure.
- **Institutional knowledge.** A decade of deployment experience, field practice, and customer-IT approval precedent is itself an asset that does not transfer. Darryl's eight years and his team's operating familiarity are part of why deployments succeed.
- **What would actually justify reconsideration.** JCI refusing durable licensing mechanics in the agreement text; a material Airwall throughput or platform constraint blocking a committed roadmap item (video-adjacent telemetry is the visible candidate given the roughly three-camera saturation limit); or a JCI strategic move that puts OpenBlue in direct competition with entroCIM at Wesco's accounts.

## 7. Risks

| Risk | Assessment | Evidence or basis |
|---|---|---|
| Sole-source dependency, decade-old, undocumented rationale | **Moderate.** Downgraded from the first draft. The dependency is real and the rationale is unwritten, but it is not unexamined: validated independently at two organizations by an operator with eight years on the technology | Darryl, 2026-09-17 |
| Decision has never been tested against the current vendor landscape | **Low to moderate.** Likely the same answer; no current evidence for it | Analysis |
| Key-person concentration on the architectural rationale | **Moderate.** The reasoning sits with Darryl and long-tenured deployment staff, not in any document | Analysis |
| Unsigned agreement on a production-critical dependency | **High.** Eleven months of negotiation; markup with JCI since 2026-08-31, no response evidenced | `JCI_Partnership.md`, 2026-09-01 |
| Licensing mechanics revocable post-signature if they sit in MSP Program Materials subject to unilateral change | **High, and already identified.** Darryl raised this 2026-07-17 | `JCI_Partnership.md` value thesis |
| Throughput ceiling constrains future telemetry scope | **Low today, moderate if video-adjacent use cases enter the roadmap** | Field evidence 2026-07-15 |
| Gartner survey response misrepresents Wesco as a microsegmentation buyer | **Low impact, trivial to mitigate** | This analysis |
| Strategic dependency on a building-automation OEM that competes elsewhere in Wesco's ecosystem | **Moderate. Manage consciously; not a reason to move** | Analysis |

## 8. Recommendations

| # | Recommendation | Owner | Next action | Timing (recommended, not committed) |
|---|---|---|---|---|
| 1 | ~~Confirm whether an Airwall selection or POC occurred~~ | Darryl | **RESOLVED 2026-09-17.** Airwall in place approximately ten years; selection completed before Darryl joined; no Wesco procedure | Closed |
| 2 | **Submit the survey: "Not Considered" for all twelve.** If free text is offered, one sentence: Wesco's use case is secure remote connectivity for a hosted application rather than enterprise microsegmentation, the platform predates the current ownership by approximately a decade, and no competitive evaluation was conducted in this tenure | Darryl | Complete and submit | Unblocked, ready now |
| 3 | ~~Record a standalone architectural rationale~~ | — | **SUPERSEDED 2026-09-17.** The MSP contract is the baseline for Airwall and Conductor technology use | Closed |
| 3a | **Verify at markup close that the baseline is complete**, since only what the contract captures is inside it: licensing mechanics, express hosting rights, JCI support obligations, metering API data scope, each in the agreement text or a document JCI cannot change unilaterally | Darryl / Brian Miller | Confirm placement item by item against the 07-17 review list | Before signature |
| 3b | Capture the signed terms as a structured baseline in the EOS | Darryl / Claude | Deferred; premature while the agreement is unsigned | At signature |
| 4 | Keep the durable-licensing-mechanics requirement as the priority item with Brian Miller. This is the term that determines whether the deal's value survives signature | Darryl / Brian Miller | Confirm placement in agreement text or a document JCI cannot change unilaterally | Next JCI legal exchange |
| 5 | Collect field intelligence on which alternatives customer IT organizations name during entroCIM deployment security reviews | Deployment team | Add a question to the deployment review checklist | Next deployment cycle |
| 6 | Treat Ordr and Asimily as a **capability watch item for entroCIM's asset inventory**, not as Airwall competitors | Darryl / David Blondel | Note in product roadmap review | Next roadmap cycle |

## 9. Assumptions, and what would change this assessment

**Resolved 2026-09-17, Darryl direct.** The first draft's load-bearing assumption was that Airwall predates the acquisition and that no Wesco selection occurred. Darryl confirmed it and went further: Airwall has been in the entroCIM deployment architecture for **approximately ten years**, any vendor consideration was completed **before he joined the company**, and he has **eight years of direct Airwall experience**, having used it for secure remote network connectivity at **Intelligent Buildings before May 2025**.

Three things changed as a result, and they are marked in place above: the survey answer is now settled rather than conditional (Section 8, rec 2); the sole-source risk is downgraded from moderate-to-high to moderate, because the architecture has been independently validated twice even though it has not been documented once (Section 7); and the material issue is restated as a documentation and currency gap rather than an absence of judgment (Section 3).

**Assumptions still open, clearly labeled:**

- All live hosted entroCIM telemetry runs through Airwall. Consistent with the record; not independently verified against a site inventory.
- No Wesco group outside Darryl's scope has evaluated an Airwall alternative since acquisition. Absence of evidence, not evidence of absence, though this now matters much less.
- The pre-acquisition entroCIM selection, roughly a decade old, considered alternatives at the time. Unknown and probably unrecoverable. Not worth pursuing.

**What is confirmed:** the ten-year deployment history and absence of a Wesco selection procedure (Darryl, 2026-09-17); Conductor hosting in Wesco Azure, 443-only availability, the roughly three-camera throughput limit, the unsigned agreement status, and the open contractual issues (`JCI_Partnership.md`).

**What would change the assessment:** JCI refusing durable licensing mechanics in the agreement text; a roadmap commitment to video-adjacent telemetry that meets the throughput ceiling; or a JCI competitive move against entroCIM at Wesco accounts. A prior selection record is no longer among them.

---

*Vendor-level detail, architecture notes, and public sources are in `Products/JCI_Airwall_Competitive_Landscape.md`.*
