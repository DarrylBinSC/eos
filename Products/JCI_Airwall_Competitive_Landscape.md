# JCI OpenBlue Airwall — Competitive Landscape (Vendor Catalog)
As of: 2026-09-17 (revised twice the same day: Darryl's confirmation of the selection history, and his designation of the MSP contract as the baseline for Airwall and Conductor technology use). **Standing: pre-baseline record.** Retain; do not extend.

Companion file to `JCI_Partnership.md`. Created 2026-09-17 from the vendor list JCI supplied in a Gartner survey question sent to Darryl ("Apart from Johnson Controls, what other vendors were under consideration during your vendor selection procedure, if applicable, included in a Proof of Concept?"). The twelve named vendors plus "Other" are cataloged here so the JCI knowledge base carries a durable competitive picture rather than leaving it in a survey screenshot.

**Scope note.** The survey list is drawn from Gartner's **Network Security Microsegmentation** market. Airwall is positioned in that market by JCI, but the job Wesco actually uses it for is **secure remote connectivity from Wesco-hosted entroCIM into customer-site building systems across networks Wesco does not own**. Several vendors below are strong in microsegmentation and largely irrelevant to that job. The distinction is carried through every entry and is the central argument in `Deliverables/JCI/2026-09-17_JCI_Airwall_Competitive_Analysis.md`.

**Confidence.** Vendor facts below are sourced from public vendor material and press coverage current as of 2026-09-17, with sources listed at the end. Wesco-fit judgments are analysis, not evidence. Nothing here has been confirmed with JCI or with Wesco Security or Network Architecture.

---

## Reference point: what Airwall actually is

- **Architecture:** overlay network built on **Host Identity Protocol (HIP)**. Endpoint identity is a cryptographic key, not an IP address. Airwall-protected devices are invisible to scanning and cannot be addressed by anything outside their policy group.
- **Components:** **Conductor** (central management and policy plane, Wesco-hosted in Azure as of 2026-07), **Relay** (traverses NAT and firewalls between endpoints and Conductor), **Airwall Gateways** (hardware or virtual, placed in front of legacy devices that cannot run an agent), and **Airwall Agents** for servers and laptops.
- **Connectivity posture:** outbound-only. **443-only operation confirmed available 2026-07-15** for both tunnel and Conductor management, removing the two-outbound-port friction that had been Wesco's largest customer-IT obstacle.
- **Ownership:** Tempered Networks, acquired by Johnson Controls June 2022, now sold as **OpenBlue Airwall**.
- **Tenure in the entroCIM architecture (Darryl, 2026-09-17):** approximately **ten years**. The selection was made by the pre-acquisition entroCIM organization, before Darryl joined, and no Wesco procurement evaluation has ever been run. Darryl separately carries **eight years of direct Airwall experience**, having used it for secure remote network connectivity at Intelligent Buildings before May 2025.
- **Known limit (Wesco field evidence, 2026-07-15):** roughly three video cameras saturate an Airwall. It is not a video pass-through path.

---

## Category A — Enterprise microsegmentation (east-west policy inside networks you own)

These vendors solve lateral-movement containment inside an enterprise the buyer controls. They assume administrative authority over the network, the hosts, or both. Wesco does not have that authority at customer sites.

### Illumio
- Agent-based host workload segmentation (Illumio Core, CloudSecure), with an application dependency map that is the product's strongest differentiator.
- Named a **Leader in the Forrester Wave for Microsegmentation (Aug 2026)** and a **2026 Gartner Peer Insights Customers' Choice** for Network Security Microsegmentation. The most established pure-play in the category.
- Agentless coverage for devices that cannot take an agent is delivered by pushing policy to switches and cloud security groups, not by Illumio enforcing inline.
- **Wesco fit:** none for the entroCIM connectivity job. Illumio segments workloads; it does not establish reachability into a customer network Wesco does not own. Potentially relevant to Wesco's own IT estate, which is not Darryl's scope.

### Akamai (Guardicore Segmentation)
- Guardicore acquired by Akamai in 2021. Agent-based east-west segmentation with strong historical strength in threat hunting, deception, and process-level visibility.
- Added an **agentless option for IoT and OT** enforced through network infrastructure, which is the part of the portfolio that touches Airwall's space.
- Backed by Akamai's global platform and enterprise commercial reach; typically a large-enterprise data-center purchase.
- **Wesco fit:** low. The agentless IoT/OT mode still presumes enforcement points inside a network the buyer administers. No remote-access traversal story comparable to Relay.

### ColorTokens (Xshield)
- Agent plus **Xshield Enforcement Point** gateway, which is the OT/IoT path for devices that cannot host an agent. Architecturally the closest of the Category A vendors to Airwall's gateway model.
- Positions on "breach readiness" rather than pure segmentation; launched an **Xshield AI Agent** in 2026 to automate policy generation.
- Recognized on the 2026 Constellation ShortList for microsegmentation and a 2026 Global InfoSec Award winner.
- **Wesco fit:** low to moderate. The gateway form factor would sit in front of a BAS controller the way an Airwall Gateway does, but ColorTokens solves segmentation at the site, not managed reachability from a Wesco-hosted application across the public internet.

### Zero Networks
- **Agentless by design.** Orchestrates the operating system's own host firewall (Windows and Linux) rather than installing an enforcement agent, and gates privileged ports behind **just-in-time MFA**. Distinctive and well-reviewed.
- Raised a **$55M Series C in June 2025**; carries high analyst mindshare in Gartner's 2026 microsegmentation research and is frequently named first among the newer entrants.
- Coverage for pure OT and embedded devices, which have no host firewall to orchestrate, depends on network-level enforcement and is the weaker part of the story.
- **Wesco fit:** none for the entroCIM job. The core mechanism requires host operating systems Wesco does not administer.

### Elisity
- **Identity-based microsegmentation enforced inside existing Cisco and Juniper switches** via a Virtual Edge, with no agents, no new hardware, and no network re-architecture. Elisity IdentityGraph correlates device, user, and workload identity from existing sources.
- Deliberately targeted at healthcare, manufacturing, and other environments full of unmanaged IoMT and OT devices, which is the same device population entroCIM touches.
- Deployment speed is the marketed advantage; the constraint is that the customer must run supported switching and must grant Elisity control of it.
- **Wesco fit:** low. Attractive architecture for a customer's own segmentation program, but it requires administrative control of the customer's switching fabric, which Wesco does not have and does not want.

### Broadcom (VMware vDefend / NSX)
- Distributed firewall enforced in the hypervisor. Effective east-west control, but only for workloads running on VMware.
- Now consumed through **VMware Cloud Foundation licensing** after Broadcom's post-acquisition restructuring, which has raised cost and packaging concerns across the installed base.
- No meaningful story for physical OT devices, building controllers, or anything outside the virtualized estate.
- **Wesco fit:** none. Building systems at customer sites are not VMware workloads.

### Zscaler
- Acquired **Airgap Networks (April 2024)** specifically to add agentless segmentation for IoT, OT, and LAN devices to the Zero Trust Exchange.
- Delivers segmentation as a cloud service; strongest where an organization has already standardized on Zscaler for its user and branch traffic.
- The Airgap-derived capability is the one genuinely adjacent to Airwall: agentless, device-level, aimed at environments where agents cannot be deployed.
- **Wesco fit:** low to moderate, and commercially impractical. Would require the customer to be a Zscaler tenant or Wesco to stand up a Zscaler relationship with customer traffic in path. That is a heavier ask of customer IT than an outbound 443 tunnel.

### Cisco Systems
- Not one product. The relevant set is **Cyber Vision** (passive OT asset discovery and protocol-aware visibility), **Industrial Threat Defense**, **ISE with TrustSec** (identity-based policy enforced in Cisco switching), and **Hypershield** for data-center workloads. **Secure Equipment Access** is Cisco's remote-access answer.
- The incumbent advantage is that many customers already own the enforcement points. Cyber Vision feeding ISE is a well-established OT segmentation pattern.
- The dependency is equally clear: value is concentrated where the customer runs Cisco industrial switching and routing.
- **Wesco fit:** low for the entroCIM job, but Cisco is the alternative most likely to be **already present** at a large customer site, and therefore the one most likely to be raised by a customer IT team as a reason not to introduce Airwall. Worth tracking for that reason alone.

---

## Category B — Connected-device visibility and risk (discover, classify, prioritize; enforce through others)

These vendors do not primarily enforce. They build the asset inventory and risk picture, then hand policy to an enforcement point. They are adjacent to entroCIM's own device-inventory value rather than to Airwall.

### Ordr
- Discovery, behavioral profiling, and AI classification across IT, IoT, OT, and IoMT. Platform plus **Ordr IQ** orchestration layer; claims 500+ enterprise customers.
- Generates microsegmentation policy and **enforces through 130+ existing integrations** (NAC, firewall, switching) rather than through its own inline enforcement path.
- Strongest in healthcare, with expansion into manufacturing, financial services, and critical infrastructure.
- **Wesco fit:** not a connectivity alternative to Airwall at all. More interesting as a **capability comparison to entroCIM's own asset inventory**, and as a potential partner or competitor in device-visibility conversations with facilities and security buyers.

### Asimily
- IoMT, IoT, and OT risk mitigation. Differentiates on **exploitability-based vulnerability prioritization** rather than raw CVE counts, plus configuration-level remediation guidance.
- Deep healthcare concentration; positions as proactive cyber asset defense and exposure management.
- Segmentation recommendations are an output; enforcement belongs to the customer's existing controls.
- **Wesco fit:** none for connectivity. Same adjacency observation as Ordr, in a narrower vertical.

---

## Category C — OT/IoT zero trust overlay (the true architectural peers to Airwall)

### Onclave Networks
- **The closest genuine peer to Airwall in the list.** Cryptographic overlay creating secure enclaves, described as L2 over L3, with **no infrastructure changes and no agents required on legacy OT devices**.
- Covers endpoints regardless of age, OEM, operating system, or protocol, explicitly including legacy SCADA, ICS, and PLCs. **Air-gap capable**, which matters directly to Darryl's team given air-gapped entroCIM installs.
- Credible federal and defense posture: full Zero Trust Architecture ATO, deployed on Defense Health Agency networks and at least one additional high-security federal agency.
- Publicly documented focus is industrial, utilities, manufacturing, and government. **No public evidence found of building automation or BACnet positioning**, which is where JCI's domain alignment is strongest.
- **Wesco fit:** the one vendor on the list that could have been a real architectural substitute for Airwall. Smaller company, narrower ecosystem, no building-industry channel, and no equivalent of the JCI relationship. Worth understanding rather than adopting.

---

## Category D — SMB and MSP-delivered segmentation

### SideChannel (Enclave)
- Publicly traded (NASDAQ: SDCH). Primary business is **virtual CISO services**; **Enclave** is its overlay microsegmentation and certificate lifecycle management product, built deliberately for the SMB segment that cannot absorb enterprise microsegmentation.
- Overlay architecture with integrated certificate management; sold and delivered substantially through an MSP motion.
- Materially smaller in scale and engineering depth than any Category A vendor.
- **Wesco fit:** not a candidate on capability. **Relevant for a different reason:** SideChannel is an existence proof of the MSP-delivered segmentation model Wesco is negotiating with JCI. If Wesco ever needs to argue that MSP-delivered segmentation is a legitimate commercial structure rather than an exception JCI is granting, this is a comparable.

---

## "Other" — the alternatives Gartner's list does not contain

The survey list is a microsegmentation list. The honest alternatives to the job Airwall does for Wesco are **secure remote access and overlay connectivity** products, none of which appear:

- Site-to-site IPsec VPN or SD-WAN terminated in Wesco Azure (the conventional approach, and the one customer IT most often proposes).
- **Tosibox**, widely used in building automation and industrial remote access, and the most likely direct substitute in a BAS context.
- **Cisco Secure Equipment Access**, the incumbent-adjacent option at Cisco-standardized sites.
- WireGuard-derived mesh overlays (**Tailscale**, **NetBird**, **ZeroTier**) or a self-built OpenVPN/WireGuard service.
- Cellular private APN or out-of-band cellular gateways, bypassing customer IT entirely.

**Assessment:** if Wesco were to re-run a selection today for the entroCIM connectivity job, the realistic shortlist would be Airwall, Onclave, Tosibox, and a self-built WireGuard-based service, not the Category A microsegmentation vendors. This is the single most useful output of the survey exercise.

---

## Where Airwall is genuinely differentiated for Wesco

1. **Outbound-only, single-port (443) traversal** of customer networks Wesco does not administer. Category A vendors presume administrative authority Wesco does not have.
2. **Cryptographic identity and device cloaking.** Airwall-protected devices do not appear to scanners, which shortens customer security review.
3. **Gateway form factor for legacy controllers.** BACnet and Modbus devices that cannot host an agent sit behind a gateway. ColorTokens and Onclave match this; most of the list does not.
4. **Building-industry alignment through JCI ownership.** entroCIM sells to the same buyer JCI sells to. No pure-play security vendor carries that.
5. **Air-gapped and high-security deployment viability**, which Darryl's team requires.

## Where Airwall is weak, and what it does not do

1. **It is not a microsegmentation product in the Gartner sense.** It does not do east-west policy at enterprise scale, and it should not be positioned against Illumio or Zero Networks on that ground.
2. **No device discovery, classification, or risk scoring.** Ordr and Asimily own that capability; Airwall assumes you already know what you are connecting.
3. **Throughput ceiling.** Roughly three video cameras saturate an Airwall (Wesco field evidence, 2026-07-15).
4. **Single-vendor dependency with an unresolved commercial structure.** The MSP agreement has been in negotiation since October 2025 and remains unsigned as of 2026-09-01. Architectural lock-in is real, is roughly a decade deep, and is not currently backed by settled contract terms.
5. **The architectural rationale is undocumented and personally held.** Sound, validated independently at two organizations, and written nowhere a successor, a security reviewer, or Wesco Legal could use it. **Being addressed (Darryl, 2026-09-17): the MSP contract will be the baseline for Airwall and Conductor technology use**, which closes this at signature for everything the contract captures. See `JCI_Partnership.md`.
6. **Strategic dependency on a firm that competes elsewhere in Wesco's ecosystem.** JCI is a building-automation OEM. This is a relationship to manage consciously, not a reason to move.

---

## Open questions

- ~~Did the pre-acquisition entroCIM team run a vendor selection before adopting Airwall?~~ **RESOLVED 2026-09-17 (Darryl).** Airwall has been in the deployment architecture approximately ten years; any vendor consideration was completed before Darryl joined; no Wesco selection procedure has occurred. Whether the original pre-acquisition selection weighed alternatives is unknown, roughly a decade old, and not worth pursuing.
- Has anyone at Wesco (Security, Network Architecture, or Nathan Kehr's commercial team) evaluated an Airwall alternative since acquisition? No evidence in this EOS. Now a low-value question.
- ~~Is the architectural rationale written down anywhere?~~ **ANSWERED 2026-09-17 (Darryl):** the MSP contract becomes the baseline for Airwall and Conductor technology use. The open question that replaces it: **will the baseline be complete at signature?** Licensing mechanics, express hosting rights, JCI support obligations and metering API data scope must sit in the agreement text or a document JCI cannot change unilaterally, or they fall outside it. Tracked in `JCI_Partnership.md`.
- Do customer IT organizations raise specific named alternatives during entroCIM deployment reviews, and if so which ones? This is field intelligence Wesco's deployment team likely holds and the EOS does not.
- Has JCI positioned Airwall against any of these vendors in a Wesco-involved opportunity? Not evidenced.

## Sources

Vendor and market facts above were drawn from, in order of use:

- Zero Networks, "Network Microsegmentation in 2026: Gartner Research Takeaways" — https://zeronetworks.com/blog/network-microsegmentation-in-2026-gartner-research-takeaways
- Illumio, "Illumio Named a Leader and a Customer Favorite in Microsegmentation" (Forrester Wave, 2026-08-18) — https://www.illumio.com/company/news-awards
- Akamai, "Segmentation for IoT and OT" product brief — https://www.akamai.com/resources/product-brief/segmentation-for-iot-and-ot
- ColorTokens, Xshield microsegmentation platform — https://colortokens.com/products/xshield-microsegmentation-platform/
- Zero Networks $55M Series C (2025-06-03) — https://www.businesswire.com/news/home/20250603407926/en/Zero-Networks-Raises-$55M-Series-C-to-Usher-in-the-Era-of-the-Defender
- Elisity identity-based microsegmentation — https://www.elisity.com/microsegmentation
- Broadcom, vDefend Distributed Firewall — https://www.vmware.com/products/security/vdefend-distributed-firewall
- Zscaler, "Zscaler Acquires Airgap Networks" — https://www.zscaler.com/blogs/company-news/zscaler-acquires-airgap-networks-extends-zero-trust-sase
- Cisco Industrial Threat Defense — https://www.cisco.com/site/us/en/products/security/industrial-security/index.html
- Ordr platform overview — https://ordr.net/
- Asimily product overview — https://asimily.com/product/overview/
- Onclave Networks, "The Onclave Difference" — https://onclavenetworks.com/onclave-difference/
- SideChannel, Enclave — https://sidechannel.com/enclave/
- Johnson Controls, OpenBlue Airwall — https://openblue.johnsoncontrols.com/airwall
- Tempered Networks, Host Identity Protocol — https://www.tempered.io/airwall/host-identity-protocol/
- Johnson Controls acquisition of Tempered Networks (2022-06-23) — https://www.johnsoncontrols.com/media-center/news/press-releases/2022/06/23/johnson-controls-acquires-tempered-networks

Wesco-specific facts (443-only availability, Conductor hosting in Wesco Azure, camera throughput limit, agreement status) come from `JCI_Partnership.md` and the evidence packages it cites, not from public sources.
