# SecuriThings Deck Review

Review of "Wesco <> SecuriThings - Overview, Pricing Framework, ROI - 6.16.26 - SHARED" (25 slides, PDF). Filed `Evidence/` (raw) and `Products/CDA/02_Phase_2_Dossiers/SecuriThings_Overview_Pricing_ROI_2026-06-16.pdf`. Reviewed 2026-10-26 at Darryl's request. The deck is vendor marketing and pricing material addressed to Wesco as a prospective end customer (its environment slide carries "Wesco's Physical Security Ecosystem, 3,000 cameras, device count 6.16.26"). Who at Wesco received it and whether an evaluation followed is not stated in the deck or the EOS record.

## Evidence strength

| Claim type | Strength | Note |
|---|---|---|
| Product scope and modules | Vendor-stated | Feature lists on slides 5, 9, 17 |
| Architecture and security posture | Vendor-stated | Azure-hosted, outbound-only connector, ISO 27001 and SOC 2 Type 2 claimed |
| Pricing framework | Vendor-stated, dated 2026-06-16, "framework" not quote | Four device bands, four modules, on-prem uplift and discount levers |
| ROI ($980K to $85K for 3,000 devices) | Vendor model, unverified | Largest line (liability incident, $440K) is an assumed avoided cost |
| Wesco device count (3,000 cameras) | Attributed to Wesco, source unstated | Recording servers and panels left blank |

## What SecuriThings is

Physical security device management and remediation, SaaS. HQ Israel, US offices; positions on Fortune 100 references and a "large partner ecosystem." Three modules on a required base:

- **Essential Visibility (required base):** dozens of VMS and ACS integrations, inventory consolidation, device up/down, geolocation, EOL/EOS and warranty, vulnerability and NDAA data, compliance status, reports.
- **Cyber Protection:** device hardening, password rotation, firmware upgrade, certificate rotation, cyber compliance reporting.
- **Operational Management:** device health metrics, alerts, root cause analysis, remote restarts, server and switch monitoring, ServiceNow and other ITSM integration, quick device login.
- **Enterprise Extension (API):** third-party data access, "very advanced use cases only."

Architecture: SecuriThings cloud on Azure; one Linux connector host in the customer data center talking to VMS, ACS and devices; outbound-only 443/8883 to the cloud. A segregated-network variant uses proxies on dual-NIC NVR servers at each site, so remote sites need no appliance. No PII, video or audio collected; encryption in transit and at rest; regular penetration tests; ISO 27001:2013 and SOC 2 Type 2 claimed.

## Pricing framework (annual subscription, hosted, 2026-06-16)

| Module | 3,000 devices | 5,000 | 9,000 | 10,000 |
|---|---|---|---|---|
| Essentials (required) | $24,592 | $38,741 | $65,691 | $71,867 |
| Cyber | $36,888 | $58,111 | $98,536 | $107,800 |
| Operations | $36,888 | $58,111 | $98,536 | $107,800 |
| Extend (API) | $12,296 | $19,370 | $32,845 | $35,933 |
| All modules | $110,663 | $174,333 | $295,608 | $323,400 |

Per device per year, derived: Essentials $8.20 (3,000) to $7.19 (10,000); all modules $36.89 to $32.34. Per device per month: roughly $0.70 to $3.10. Levers: on-premises deployment +50%; reference discount 5 to 10%; prepay 3% (3 years) to 5% (5 years); ramp discount 5 to 20%. The deck maps Essentials to the physical security budget, Cyber to the cyber budget and Operations to the IT budget, a three-budget land strategy. Minimum 12-month subscription is 2,000 devices.

Pilot routes: a complimentary static "platform preview" built from a CSV export of the VMS/ACS (type, name, manufacturer, model, firmware), with no connectivity; 30 days free via an order with a future start date and unconditional cancel; or a $10K to $20K sub-term pilot credited back on conversion within two months.

## ROI model as presented (3,000 devices, annual)

Without automation $979,500; with SecuriThings $84,500; "$298 saved per device per year." Lines: liability incident $440,000 to $44,000; certificate management $100,000 to $2,000; compliance reports $76,500 to $0; availability monitoring $75,000 to $0; asset and lifecycle $63,000 to $0; break/fix $90,000 to $36,000; firmware $50,000 to $1,000; password rotation $50,000 to $1,000; hardening $35,000 to $500. All vendor assumptions; none sourced in the deck.

## Comparison with CDA as of 2026-10-26

| Dimension | SecuriThings (deck) | CDA (record) |
|---|---|---|
| What is sold | Software subscription; customer's team acts on it | Managed service: appliance, platform, people, field remediation, one annual fee per site |
| Device coverage | Cameras, recording servers, access control panels, switches, "other endpoints"; dozens of VMS/ACS integrations | Cameras first (Hanwha, Axis live via entroCIM); new manufacturer 8 to 12 weeks each |
| Remediation | Firmware, password, certificate rotation and hardening in software, fleet-wide | Launch scope read-only on devices (Phase 2: no write actions); remediation through service and dispatch |
| Site footprint | One connector per data center; proxies on NVRs for segregated sites; no site appliance | Appliance per site in the pro forma, chosen for local-network auto-discovery; central deployment (as entroCIM) also possible, and a parallel central model may suit large enterprises (Darryl, 2026-10-26); central case not priced |
| Price basis | Per device, by module, roughly $7 to $37 per device per year | Per site: $6,900 / $10,300 / $15,700 (Small / Medium / Large), about $78 to $172 per device per year at the modeled device counts |
| Field and supply | None in the deck | TS delivery, integrator-inclusive dispatch, procurement and licensing data (Bob Caprise's first data layer), WAM and ALM pull-through |
| Vendor neutrality | Multi-vendor by integration count | Multi-vendor by Wesco position; integration count small today |
| Security posture evidence | ISO 27001, SOC 2 Type 2 claimed | Not yet packaged for CDA |

The price gap is a software subscription against a managed service, so it is not like for like; but a seller or buyer will hear "$3 a device a month all in" against CDA's per-site fee, and the CDA record already notes Small sites price at about $17 per device per month. The seller hook from 2026-10-02 ("what does CDA do that the VMS does not?") now has a sharper form: what does CDA do that SecuriThings does not? The answer in the record is people, field execution, procurement, the Wesco relationship and the service wrapper, not the software.

## Partner or competitor

Darryl's classification (2026-10-26): a direct competitor to CDA. The partner reading below is an option Claude raised, not a position Darryl has taken. Both readings hold, depending on the account. As a competitor it covers CDA's Essential Visibility and most of Operational Management, exceeds CDA's launch scope on cyber remediation, and has the integration breadth CDA lacks. As a partner it is the device engine the Phase 2 dossier already named ("SecuriThings/Viakoo: partner candidate, broad firmware/configuration/hygiene coverage"; RFI dated 2026-08-14 in the Phase 2 forward plan, status not recorded). Points in favor of the partner reading after the 2026-10-06 AOP outcome: CDA is now built from a reduced entroCIM team, and a partner engine removes the per-manufacturer integration build and the write-action governance work from that team. Points against: margin stacking on a per-site fee that is already judged cost-plus (Sridhar Loke, 2026-10-02); SecuriThings sells direct, including apparently to Wesco itself; dependence on a third party for the core of a service positioned as Wesco-owned.

What the deck does not say: partner, reseller or MSSP pricing; whether SecuriThings would white-label or sit behind a Wesco service; API depth of the Extend module; federal or regulated-customer posture beyond NDAA data on devices; any reference to Wesco as a channel rather than a customer.

## Open questions (Darryl's to answer or route)

1. Who at Wesco received this deck in June, in what capacity, and did an evaluation or purchase for Wesco's own estate follow? If Wesco corporate security is a SecuriThings prospect, that is an internal reference customer CDA could have claimed and a buyer who went to a vendor instead.
2. Whether to run the Phase 2 RFI as a partner conversation now (SecuriThings as engine under a Wesco managed service), or to position against it. Candidate owner: Darryl with Cody Remington; Sridhar Loke for the pricing read.
3. Whether the pro forma should carry a SecuriThings-engine scenario against the current stack (per-node Nozomi, RMM, Airwall at $1,680 a year plus SkySpark and entroCIM licensing). Not run; the deck gives enough to model it.

## Embedded services (added 2026-10-26, web check at Darryl's question)

The deck sells software only: the subscription "includes support, success, training and software upgrades"; no monitoring center, no remediation people, no field service, no hardware or site survey appears anywhere in it. Public sources (secondary, press releases) show how SecuriThings covers the service layer: a Managed Service Platform launched January 2023 for integrators and MSPs to deliver remote managed services on top of the platform, and a Convergint partnership (January 2023) in which SecuriThings powers nine Convergint service centers that perform firmware upgrades, password rotations and vulnerability detection remotely for customers. SecuriThings does not run its own NOC or field service in any source found. The service layer that CDA embeds is therefore sold by SecuriThings' integrator partners, not by SecuriThings; Convergint is the named example, and Convergint is the integrator Matt Powers named on 2026-10-14 as a TS field partner.

Sources: Security Sales & Integration, 2023-02-08 (MSP platform launch, "currently only available to select partners"); SecurityInfoWatch, 2023-01-23 (Convergint service centers). Not checked: current partner list, partner pricing, whether SecuriThings has since added direct services.
