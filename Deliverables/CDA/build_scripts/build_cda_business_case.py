# CDA Business Case, refreshed 2026-10-30, on the Wesco Business Case template (edits the Aug 2026 v2 file in place by field).
# Figures from pro forma v4.6 Deck Figures; story aligned with what was told to Bill Muczko (2026-10-02) and Matt Powers (2026-10-14).
# Run from a folder holding SRC and WB:  python3 build_cda_business_case.py
import copy
from docx import Document
from openpyxl import load_workbook
SRC='SUPERSEDED_2026-08-11_CDA_Wesco_Business_Case_v2.docx'
WB='2026-10-02_CDA_Pro_Forma_v4.6.xlsx'
OUT='2026-10-30_CDA_Business_Case.docx'
wb=load_workbook(WB,data_only=True); ws=wb['Deck Figures']; FIG={}
for r in ws.iter_rows(min_row=4,values_only=True):
    if r[1] and r[3] is not None: FIG[r[1]]=str(r[4]) if r[4] is not None else str(r[3])
g=FIG.__getitem__
d=Document(SRC); T=d.tables[0]
def find_cell(start):
    for row in T.rows:
        for c in row.cells:
            if c.text.strip().startswith(start): return c
    raise KeyError(start)
from docx.oxml.ns import qn
LI_PPR=None
for p in d.paragraphs+[q for t in d.tables for row in t.rows for c in row.cells for q in c.paragraphs]:
    if p.style.name=='List Paragraph' and p._p.pPr is not None and p._p.pPr.find(qn('w:numPr')) is not None:
        LI_PPR=copy.deepcopy(p._p.pPr); break
def fill(start,paras,keep_label_paras=1):
    c=find_cell(start); ps=c.paragraphs
    for p in ps[keep_label_paras:]: p._p.getparent().remove(p._p)
    # a label paragraph that carries body text after the label keeps only its first run
    lab=c.paragraphs[0]
    for r in lab.runs[1:]:
        if r.bold is not True or not r.text.strip(): r._r.getparent().remove(r._r)
    for kind,text in paras:
        p=c.add_paragraph(text, style=('List Paragraph' if kind=='li' else None))
        if kind=='li' and LI_PPR is not None:
            old=p._p.pPr
            if old is not None: p._p.remove(old)
            p._p.insert(0,copy.deepcopy(LI_PPR))
        if kind=='b':
            for r in p.runs: r.bold=True
N=lambda t:('n',t); LI=lambda t:('li',t); B=lambda t:('b',t)

# header
c=find_cell('Business Lead'); c.paragraphs[1].runs[0].text='Bill Muczko, Business Sponsor (Global Enterprise)'
for r in c.paragraphs[1].runs[1:]: r._r.getparent().remove(r._r)
c=find_cell('Key Stakeholders'); ps=c.paragraphs
ps[0].runs[0].text='Key Stakeholders: Sean McCloskey (executive sponsor); Matt Powers (Technology Services, delivery); Bob Caprise (CSS Sales); Dirk Naylor'
for r in ps[0].runs[1:]: r._r.getparent().remove(r._r)
ps[1].runs[0].text='Owning Business: CSS, Digital Products and Platforms (CSS Platforms, entroCIM team)'
ps[2].runs[0].text='Impacted Business(es): Global Enterprise sales; Technology Services; CSS Sales; WAM and ALM'
for p in (ps[1],ps[2]):
    for r in p.runs[1:]: r._r.getparent().remove(r._r)

fill('Investment Description',[
 N('Connected devices Wesco sells, cameras first and then access control and network devices, are installed and then left under-managed. They drift out of support, license and cyber compliance, their health is unknown until something fails, and nobody is accountable for them after the sale. Customers who run a multi-vendor video platform have no multi-vendor way to keep the devices behind it covered; each manufacturer offers its own utility, and someone has to staff it.'),
 N(f'Connected Device Assurance (CDA) is a multi-vendor managed service sold as one annual fee per site, by site size, with one service level for every customer. Wesco discovers and inventories the covered devices, tracks support and license status, cyber posture and health, executes approved firmware and configuration changes, and escalates to the field when hands are needed on the device, with evidence of every action. Illustrative fees: {g("fee_small")} / {g("fee_medium")} / {g("fee_large")} a year for a Small / Medium / Large site ({g("tier_devices_s")} / {g("tier_devices_m")} / {g("tier_devices_l")} devices).'),
 N('How it is delivered. A Wesco operations center (a building operations center, not a network operations center) runs the service: a few people in North America, a couple in Europe, the bulk in India, with in-market people as tier 2 for larger remediation. Failed devices follow a warranty check, replacement and dispatch to the integrator tied to the account and contract. Technology Services or partners deploy the per-site appliance. Wesco layers on top of the integrators; it does not take their business.'),
 N('What it is built on. entroCIM and SkySpark, by the entroCIM team, with a partner discovery sensor on a managed appliance at each site. Central deployment, as entroCIM runs today, is available for large estates. The Axis and Hanwha camera connectors are live in entroCIM today.'),
 N('Why Wesco. We sell the devices, hold the manufacturer relationships and can carry a problem from detection through remediation to replacement and installation. CDA gives Global Enterprise sellers an advanced-services conversation at the accounts they already call on, and the service data pulls through ALM, WAM and device refresh.'),
])
fill('Business Outcome',[
 N('A recurring, multi-vendor managed service established on the Wesco installed base, measured by sites under contract, recurring run rate and site gross margin. Pro forma v4.6 (illustrative; the workbook stays within the team until Sean McCloskey has vetted the numbers):'),
 LI(f'First sites in 2028, led by Kroger; {g("sites_2031")} sites and about {g("devices_2031")} devices under management by 2031 across three to five anchor accounts.'),
 LI(f'Recurring run rate of {g("run_rate_2031")} at the end of 2031; five-year revenue {g("five_year_revenue")}; gross margin rising from {g("gm_pct_2028")} in 2028 to {g("gm_pct_2031")} in 2031, about {g("target_margin")} percent at the site fee.'),
 LI(f'Wesco payback per site of {g("payback_small")} to {g("payback_large")}; cash positive in {g("break_even_year")} with {g("el_net_cash")} of net cash over the five years, after a peak requirement of {g("peak_cash")} in {g("cash_trough_year")}.'),
 N('Customer outcomes: every covered device inventoried with support and license status; continuous posture and health; firmware and configuration changes only on recorded approval with a validated outcome; faults surfaced before failure and eligible ones cleared remotely (target 25 percent or more without a site visit, baseline set in the first deployments); a risk-based refresh plan instead of emergency replacement.'),
 N('Pull-through, not yet quantified in the pro forma: ALM and WAM attach, device refresh and replacement demand identified from service data, and the Kroger per-camera fee on new camera sales.'),
])
fill('What are the risks of NOT doing this',[
 N('Without CDA the devices Wesco sells stay unmanaged after the sale, and the recurring relationship around them goes to someone else.'),
 LI('Growing customer exposure with no Wesco answer. Customers will address this with or without us; Bill Muczko\'s read is that most are not managing camera assets at all, or are doing it on spreadsheets.'),
 LI('The category is already being sold. SecuriThings pitched Wesco itself in June 2026 as a per-device SaaS; Axis and Hanwha have single-vendor tools; some customers build their own. Each year of delay raises the cost of entry.'),
 LI('Recurring revenue and refresh demand left unserved. The installed base needs firmware, configuration, health and security upkeep for its whole life; Wesco does not participate in that today, and refresh demand stays invisible until a competitor surfaces it.'),
 LI('The seller motion Global Enterprise wants is lost. CDA is the advanced-services conversation that moves sellers from pick, pack and ship; without it, that shift has no lead offer in the camera estate.'),
 LI('The entroCIM platform carries one product. CDA reuses entroCIM, SkySpark, the connector library and secure connectivity already paid for; not proceeding leaves that reuse unrealized.'),
], keep_label_paras=1)
fill('In Scope',[
 N('Launch scope is deliberately narrow: a laser-focused assurance service, not an entroCIM-scale integration.'),
 LI('Discovery and inventory of covered devices (make, model, firmware, support and license status), cameras first, then access control and network devices as device families qualify.'),
 LI('Continuous cyber posture and health monitoring; vendor advisories matched to covered devices; prioritized work for operators rather than raw alerts.'),
 LI('Approved firmware and configuration changes executed remotely with validation, recovery path and evidence; field escalation with a complete work package to the integrator attached to the account.'),
 LI('Customer-facing posture, activity and service reporting; refresh and lifecycle recommendations delivered to Sales.'),
 LI('Per-site managed appliance (partner sensor, entroCIM components, fleet management, secure connectivity) with a central deployment option for large estates; multi-tenant service delivery and metering.'),
 LI('Operations center service delivery with Technology Services; integrator-inclusive field remediation.'),
])
fill('Nonfunctional',[
 LI('Security. Least-privilege access to customer devices, segregated credential handling, customer-approved connectivity, alignment with Wesco cyber governance and customer security review.'),
 LI('Change control and auditability. No action on a customer device without recorded authorization and an approved window; an evidence record per action, retained and exportable.'),
 LI('Multi-tenancy and data handling. Strict tenant isolation of device data, evidence and credentials. Data is used to deliver the service and, under the customer agreement, to enable connected Wesco services and refresh recommendations; not sold or disclosed outside the delivery chain.'),
 LI('Availability. Business-hours managed service at launch with defined behavior on loss of connectivity; 24x7 only if volume and economics prove it.'),
 LI('Compliance alignment. Capabilities mapped to CISA asset-inventory guidance and NIST IR 8259A without claiming certification.'),
])
fill('Out of Scope',[
 LI('No guarantee of device availability beyond the contracted monitoring, response and remediation.'),
 LI('Not a replacement for the customer\'s video management system, network management or OT security platform; CDA covers what those do not (life cycle, license, capacity and posture across vendors).'),
 LI('No security operations center, managed detection and response, threat hunting or incident response.'),
 LI('No compliance certification on the customer\'s behalf, and no ownership of the customer\'s security, procurement or risk-acceptance policy.'),
 LI('Credential rotation, certificate life-cycle management and autonomous hardening are later capabilities.'),
 LI('Not every manufacturer at launch; coverage expands by qualified device family. Cold-chain, room-readiness and similar vertical outcome integrations are entroCIM-scale work, not CDA launch scope.'),
])
fill('Which Internal and/or external customers',[
 N(f'External. Global Enterprise accounts with multi-site camera estates, sold on vertical outcomes: Kroger (engaged; {g("anchor_kroger_sites")} Large sites in the plan from {g("anchor_kroger_start")}), Cisco Connected Real Estate (in the plan at {g("anchor_cisco_sites")} sites, still scoping), and three anchors still to name in pharma, automotive and a third lane, chosen from Wesco edge-device shipment data. Buyers are security, facility and IT/OT leaders accountable for device risk; their teams approve changes and consume evidence rather than operating tools.'),
 N('Internal. Global Enterprise sellers gain an advanced-services offer and refresh signals from service data. Technology Services runs the operations center and field delivery with integrators. The entroCIM team builds and sustains the product inside the entroCIM roadmap. WAM and ALM receive device identity, life-cycle and refresh data.'),
])
fill('Dependencies',[
 LI('entroCIM 2027 roadmap capacity: CDA is built by the entroCIM team with no separate FY27 line, so its timing is sequenced against entroCIM releases (reconciliation with Ron Snyder and David Blondel, October 2026).'),
 LI('Technology Services delivery model and staffing: business review of the CDA services with Matt Powers and Cody Remington; TS review of the service-delivery heads in the pro forma.'),
 LI('Commercial construct: enterprise agreements and small-branch estates alongside the per-site fee; willingness to pay tested in the first anchor conversations.'),
 LI('Partner sensor agreement (Nozomi Guardian; MNDA in place, licensing and multi-customer terms open) and volume terms on the per-node software stack, the largest lever on the fee.'),
 LI('Manufacturer qualification by device family (Axis and Hanwha connectors live; firmware access and managed-service rights to confirm).'),
 LI('Cyber Security approval of connectivity, credential handling and remote action; Legal on liability boundary, service levels and data use.'),
])
fill('In-house or',[
 LI('Build in-house on entroCIM, by the entroCIM team: device connectors, service orchestration, approval and evidence workflow, operator work queue, customer reporting, WAM and ALM integration. These carry Wesco\'s differentiation.'),
 LI('Partner or license: discovery and vulnerability context (partner sensor), fleet management, secure connectivity, and remediation breadth where building it is not economical.'),
 LI('Deliver through a Wesco operations center with Technology Services, and in the field through the integrator attached to each account, under Wesco process, approvals and evidence standards.'),
])
fill('Resources and Capacity',[
 N('Build. The entroCIM team, within its 2027 roadmap and budget; no incremental development headcount. The pro forma carries '+g('build_2027')+' of 2027 build labor and licenses, absorbed.'),
 N(f'Deliver. Commissioning from the existing team through {g("comm_absorbed_through")}; service-delivery heads from {g("tss_heads_2028")} in 2028 to {g("tss_heads_2031")} in 2031 in the pro forma ({g("sites_per_fte_2031")} sites per FTE), funded by site fees and subject to Technology Services review. First delivery hire in seat by {g("first_hire")}.'),
 N('Also engaged: Cyber Security, Legal, Finance (pricing and margin validation), Global Enterprise sales, and the partner sensor vendor. Resource managers engaged: Darryl Benson (CSS Platforms), Matt Powers (Technology Services).'),
], keep_label_paras=2)
fill('Investment Cost (Planned year only)',[
 N('No standalone FY27 investment. CDA was not approved as a separate investment in the FY27 AOP (October 2026); it continues on the entroCIM roadmap, built by the entroCIM team, with its own FY27 numbers at zero. The pro forma estimate of '+g('build_2027')+' for 2027 build labor and licenses is absorbed in the entroCIM team budget. No seed funding or BIR is requested for CDA.'),
], keep_label_paras=2)
fill('Estimated Total Costs',[
 N(f'Five-year pro forma (v4.6, illustrative), 2027 to 2031: capital deployed {g("capital_2031")} by 2031, {g("software_share_of_capital")} of it software licenses (of which entroCIM licensing {g("el_cap_entrocim")} is an internal charge that does not leave the company); service-delivery people {g("el_service")}; software renewals {g("el_renewals")}; sustain team {g("el_sustain")}; sales commission {g("el_commission")}; marketing {g("el_marketing")}. All recovered through site fees: peak cash requirement {g("peak_cash")} in {g("cash_trough_year")}, cash positive in {g("break_even_year")}.'),
 N('Cost to serve a site runs '+g('cost_to_serve_small')+' / '+g('cost_to_serve_medium')+' / '+g('cost_to_serve_large')+' a year (Small / Medium / Large) plus '+g('upfront_small')+' / '+g('upfront_medium')+' / '+g('upfront_large')+' upfront. Per-node vendor software is the largest line and the main negotiation lever.'),
], keep_label_paras=3)
fill('Expected Benefit',[
 N(f'Revenue by year (pro forma, illustrative): 2027 none (build); 2028 ${g("revenue_2028")}M; 2029 ${g("revenue_2029")}M; 2030 ${g("revenue_2030")}M; 2031 ${g("revenue_2031")}M, a {g("run_rate_2031")} run rate at the end of 2031. Gross margin {g("gm_pct_2028")} in 2028 rising to {g("gm_pct_2031")} in 2031.'),
 N(f'Benefit types: recurring service revenue; seller access to accounts for advanced-services selling; ALM, WAM and refresh pull-through (not quantified); Kroger per-camera fee on new cameras ({g("kroger_camera_fee_annual")} a year at {g("kroger_cameras_per_year")} cameras). Value begins with the first anchor sites in 2028 and scales with sites under contract. No customer has yet been asked to pay the fees; willingness to pay is tested in the first anchor conversations.'),
], keep_label_paras=3)
fill('Links',[
 B('Working files (Deliverables/CDA)'),
 N('2026-10-02_CDA_Pro_Forma_v4.6.xlsx (the model; internal until vetted). 2026-10-02_CDA_Product_and_Business_Case.pptx (21-slide deck). 2026-10-30_CDA_Intake.pptx. 2026-10-02_CDA_Sponsorship_Meeting_Summary.md. Products/CDA/CDA.md, 2026-10-14 entry (Matt Powers meeting). 2026-10-26_CDA_vs_SecuriThings_Cost_Comparison.md.'),
 B('External guidance'),
 N('CISA, Foundations for OT Cybersecurity: Asset Inventory Guidance for Owners and Operators, August 2025. CISA, Cross-Sector Cybersecurity Performance Goals 2.0, December 2025. NIST IR 8259A, IoT Device Cybersecurity Capability Core Baseline.'),
])
d.save(OUT); print('wrote',OUT)
