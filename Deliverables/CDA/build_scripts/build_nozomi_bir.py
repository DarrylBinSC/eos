# Nozomi Guardian MSP enablement: Business Investment Request workbook (Wesco BIR Workbook 2026 Rev4, supplied by Darryl 2026-10-30, Evidence/) and figures shared with the intake deck.
# Pro forma v4.6 supplies node counts and the Guardian BOM placeholder.
# Yellow-filled cells on Detail are planning placeholders pending Nozomi's MSP quote; replace them and nothing else moves.
# Run from Deliverables/CDA:  python3 build_scripts/build_nozomi_bir.py
import json, datetime
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
TEMPLATE='../../Evidence/BIR Workbook 2026 Rev4.xlsx'
PF='2026-10-02_CDA_Pro_Forma_v4.6.xlsx'
OUT='Nozomi/2026-11-06_Nozomi_Guardian_BIR.xlsx'
FIGS='Nozomi/nozomi_figures.json'
YEL=PatternFill('solid',fgColor='FFFFFF00')

pf=load_workbook(PF,data_only=True)
model=pf['Model']; bom=pf['BOM']
years=[int(model.cell(6,c).value) for c in range(3,8)]
sites=[model.cell(10,c).value or 0 for c in range(3,8)]
revenue=[model.cell(20,c).value or 0 for c in range(3,8)]
gm=[model.cell(32,c).value or 0 for c in range(3,8)]
up=float(bom['F10'].value); ann=float(bom['G10'].value)   # Guardian per node: upfront, annual (placeholder, "To source")
new=[sites[0]]+[sites[i]-sites[i-1] for i in range(1,5)]
outlook=[]
for i,y in enumerate(years):
    outlook.append({'year':y,'new_sites':new[i],'sites':sites[i],'upfront':new[i]*up,'annual':sites[i]*ann,'total':new[i]*up+sites[i]*ann})

# ---- 2027 enablement lines (planning placeholders unless noted)
LAB_NODES=5; TRAINEES=4
lines=[
 ('Nozomi Networks / MSP program','Software - Purchased','E','MSP program enrollment and central management (Vantage or CMC) for Wesco-operated Guardian instances, year one. Placeholder pending Nozomi MSP quote.',1,25000,True),
 ('Nozomi Networks / development and lab','Software - Purchased','E',f'Guardian container licenses for development, test and demonstration instances, year one ({LAB_NODES} nodes at the pro forma BOM placeholder of ${up:,.0f} upfront plus ${ann:,.0f} annual per node).',LAB_NODES,up+ann,True),
 ('Nozomi Networks / training','Other','E',f'Nozomi certification training for CSS Platforms engineers and operations center leads ({TRAINEES} seats). Placeholder pending Nozomi training price list.',TRAINEES,3000,True),
 ('Nozomi Networks / services','Other','E','Partner onboarding and integration support: Guardian local API, container deployment on the CDA appliance, multi-tenant setup. Placeholder pending Nozomi scope.',1,15000,True),
]
total=sum(q*u for _,_,_,_,q,u,_ in lines)

wb=load_workbook(TEMPLATE)
d=wb['Detail']
d['F3']='New BIR'
d['F6']='Nozomi Guardian MSP enablement for Connected Device Assurance'
d['F7']='Information Systems'; d['F8']='NO'
d['C8']=datetime.datetime(2026,11,6); d['C9']=datetime.datetime(2027,12,31)
d['F9']='Darryl Benson'
for c in ('C3','C4','C5','C6'): d[c].fill=YEL   # site number, site name, legal entity, legacy company: Darryl to confirm for CSS Platforms
for i,(vendor,cat,pe,desc,qty,unit,ph) in enumerate(lines):
    r=13+i
    d[f'A{r}'].fill=YEL   # vendor in AP system: confirm whether Nozomi Networks is set up
    d[f'B{r}']=vendor; d[f'C{r}']=cat; d[f'D{r}']=pe; d[f'E{r}']=desc; d[f'F{r}']=qty; d[f'H{r}']=unit; d[f'K{r}']=0
    if ph: d[f'H{r}'].fill=YEL

ex=wb['Explanation']
def money(v): return f'${v:,.0f}'
ol='\n'.join(f'{o["year"]}: {o["new_sites"]:,} new sites, {o["sites"]:,} under contract; licensing about {money(o["total"])} ({money(o["upfront"])} upfront, {money(o["annual"])} annual)' for o in outlook if o['sites'])
ex['A14']=f'''Opportunity / Problem Statement

Connected Device Assurance (CDA) is a multi-vendor managed service, sold as one annual fee per site, that keeps the connected devices Wesco sells (cameras first, then access control and network devices) inventoried, current, healthy and cyber-compliant after the sale. It is built on entroCIM by the entroCIM team, sponsored by Global Enterprise (Bill Muczko) and delivered with Technology Services (Matt Powers). CDA continues on the entroCIM roadmap after the FY27 AOP, with no standalone development line.

The cyber value proposition of CDA (discovery of every connected device on the site segment, firmware and vulnerability context, and the evidence customers need against CISA asset-inventory guidance) depends on a partner OT sensor running on each CDA appliance. Nozomi Networks Guardian is the selected sensor: a containerized Guardian instance on the Wesco appliance captures the device segment locally, and entroCIM integrates through Guardian's local API. The same capability extends to entroCIM deployments where customers want device visibility. Wesco cannot build the product, train the team or demonstrate the service to anchor accounts (Kroger, Cisco Connected Real Estate) without licensed Guardian instances and Nozomi training in 2027. An MNDA with Nozomi is in place and Nozomi has offered sandbox and license access; MSP terms are the next step.

Alternatives Considered

Alternative 1: Build discovery and vulnerability assessment in entroCIM. Challenges: a multi-year engineering effort outside the entroCIM team's core competence, no vulnerability intelligence feed, and no credible security posture to present to customer security teams. The AOP outcome leaves no capacity for it.

Alternative 2: Use each manufacturer's own utility (Axis, Hanwha and others). Challenges: single-vendor coverage, no passive discovery of unknown devices, and it recreates the tool sprawl CDA exists to remove.

Alternative 3: Another partner engine (SecuriThings, Viakoo or similar). Challenges: SecuriThings is a direct competitor to CDA that has pitched Wesco itself; Viakoo and others were reviewed in Phase 2 and remain partner candidates for remediation breadth, not for the OT sensing layer. Nozomi is the fit for passive discovery and OT context and is complementary to CDA, not competitive.

Recommended Solution

Enroll Wesco as a Nozomi MSP and license Guardian for the CDA build in 2027: MSP program and central management, development and lab instances, certification training for CSS Platforms engineers and operations center leads, and partner onboarding and integration support. This request covers the 2027 enablement only. Production Guardian licenses scale with sites under contract from 2028 and are recovered inside the CDA site fee (about 40 percent gross margin at the fee in the CDA pro forma v4.6). The outlook below is from the pro forma site plan at the BOM placeholder of {money(up)} upfront plus {money(ann)} a year per node and will be re-set at Nozomi's MSP terms:

{ol}

Benefits

A cyber value proposition CDA can demonstrate and sell in 2027 and deliver from 2028; a path to the per-node volume terms that are the largest lever on the CDA fee; device visibility available to entroCIM deployments; recurring service revenue (CDA pro forma: {money(revenue[1])} in 2028 rising to {money(revenue[4])} in 2031) and pull-through to ALM, WAM and device refresh.

Risks

MSP terms not yet quoted: every unit cost in this request except the BOM placeholder is a planning figure to be replaced by Nozomi's quote. Multi-customer licensing on a Wesco-owned node and Guardian container licensing are open items from the Phase 2 review. CDA build timing is sequenced against the entroCIM 2027 roadmap; a slip defers the production licenses, not this enablement.

Strategic Goals

CSS Digital Products strategy: recurring managed services on platforms Wesco owns, extending the entroCIM investment to a second product and moving Global Enterprise sellers toward advanced-services selling. Wesco Strategy 1, extend our leading scale and value proposition.

Budget

Not in the current fiscal year budget. Requested as a 2027 expense on the entroCIM product budget; CDA has no standalone FY27 line.'''

# Cost Benefit Analysis: the CDA pro forma v4.6 (the service these licenses enable), periods 0 to 5 = 2026 to 2031
cba=wb['Cost Benefit Analysis']
cols='DEFGHI'; yrs=[2026]+years
cogs=[model.cell(30,c).value or 0 for c in range(3,8)]
build=[(model.cell(36,c).value or 0)+(model.cell(37,c).value or 0) for c in range(3,8)]
sustain=[model.cell(38,c).value or 0 for c in range(3,8)]
sga=[(model.cell(39,c).value or 0)+(model.cell(40,c).value or 0) for c in range(3,8)]
for i,c in enumerate(cols):
    cba[f'{c}9']=yrs[i]; cba[f'{c}24']=yrs[i]
    if i==0: continue
    j=i-1
    cba[f'{c}27']=revenue[j]; cba[f'{c}28']=cogs[j]
    cba[f'{c}32']=build[j]+sustain[j]; cba[f'{c}34']=sga[j]
cba['E18']=total   # this request: 2027 enablement, operating expenditure
cba['D29']='=D27-D28'; cba['D42']='=D40-D41'
cba['B61']='Basis: CDA pro forma v4.6 (2026-10-02), illustrative and not yet vetted. Net sales and COGS are the CDA plan (COGS includes per-site capital amortization, so no separate capex or depreciation is entered); salaries carry the 2027 build (absorbed in the entroCIM team) and the sustain team; Other SG&A is sales commission and marketing. Row 18 (2027) is this request. Nozomi production licensing is inside COGS.'
wb.save(OUT)
json.dump({'lines':[{'vendor':a,'desc':dd,'qty':q,'unit':u,'placeholder':ph} for a,_,_,dd,q,u,ph in lines],'total_2027':total,'outlook':outlook,'guardian_upfront':up,'guardian_annual':ann,'revenue':dict(zip(years,revenue)),'gm_pct_weighted':sum(gm)/sum(revenue)},open(FIGS,'w'),indent=1)
print('wrote',OUT,'2027 request',money(total)); print(json.dumps(outlook,indent=0))
