# CDA Intake deck (refreshed 2026-10-30). Starts from the Aug 2026 intake deck (Wesco Demand Intake template),
# keeps the title, the intake form and two story slides, rewrites the form for the post-AOP position,
# adds two slides (offer and delivery; where it stands) and drops the template help slides.
# Figures come from the pro forma Deck Figures tab; nothing numeric is typed here.
# Run from a folder holding SRC and WB:  python3 build_cda_intake.py
import copy, sys
from pptx import Presentation
from pptx.util import Inches as In, Pt
from pptx.dml.color import RGBColor as C
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from openpyxl import load_workbook

SRC='SUPERSEDED_2026-08-18_CDA_Intake_v2.pptx'
WB='2026-10-02_CDA_Pro_Forma_v4.6.xlsx'
OUT='2026-10-30_CDA_Intake.pptx'

wb=load_workbook(WB,data_only=True); ws=wb['Deck Figures']
FIG={}; VAL={}
for r in ws.iter_rows(min_row=4,values_only=True):
    if r[1] and r[3] is not None: FIG[r[1]]=str(r[4]) if r[4] is not None else str(r[3]); VAL[r[1]]=r[3]
def g(k): return FIG[k]

NAVY=C(0x1D,0x25,0x2D); GREEN=C(0x00,0x95,0x3A); SLATE=C(0x5B,0x7A,0x8E); MIST=C(0xDB,0xE3,0xE9)
GREY=C(0x8E,0x92,0x96); WHITE=C(0xFF,0xFF,0xFF); INK=C(0x2B,0x2B,0x2B); SOFT=C(0xC9,0xD1,0xD6); PALE=C(0xE9,0xF3,0xEC)
MBLUE=C(0x00,0x49,0x86); STEEL_LIGHT=C(0xF1,0xF5,0xF7); F='Arial'

prs=Presentation(SRC)
S=list(prs.slides)

from pptx.oxml.ns import qn
def set_para(p,text,tmpl=None):
    runs=p.runs
    if not runs:
        r=p.add_run(); r.text=text
        if tmpl is not None:
            rPr=copy.deepcopy(tmpl._r.find(qn('a:rPr')))
            if rPr is not None: r._r.insert(0,rPr)
        return
    runs[0].text=text
    for r in runs[1:]: r._r.getparent().remove(r._r)
def _tmpl_run(cell):
    tbl=cell._tc.getparent().getparent()
    for r in tbl.iter(qn('a:r')):
        if r.find(qn('a:rPr')) is not None and r.find(qn('a:rPr')).get('sz'):
            class T: pass
            t=T(); t._r=r; return t
    return None
def set_cell(cell,text):
    paras=cell.text_frame.paragraphs
    set_para(paras[0],text,_tmpl_run(cell))
    for p in paras[1:]: p._p.getparent().remove(p._p)
def shape_by_text(slide,start):
    for sh in slide.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip().startswith(start): return sh
    raise KeyError(start)
def table_by_cell(slide,r,c,start):
    for sh in slide.shapes:
        if sh.has_table:
            try:
                if sh.table.cell(r,c).text.strip().startswith(start): return sh.table
            except IndexError: pass
    raise KeyError(start)
def add_row(table):
    tr=table._tbl.tr_lst[-1]; new=copy.deepcopy(tr); table._tbl.append(new); return table.rows[len(table.rows)-1]

# ---------------------------------------------------------------- slide 1: title
t=S[0]
sh=shape_by_text(t,'Project Intake'); ps=sh.text_frame.paragraphs
set_para(ps[0],'Project Intake'); set_para(ps[1],'Connected Device Assurance (CDA)')
set_para(shape_by_text(t,'Month DD').text_frame.paragraphs[0],'October 30, 2026')

# ---------------------------------------------------------------- slide 7: the form
f=S[6]
set_para(shape_by_text(f,'Enter Project').text_frame.paragraphs[0],'Connected Device Assurance')
set_para(shape_by_text(f,'Enter Date').text_frame.paragraphs[0],'October 30, 2026')
set_para(shape_by_text(f,'Enter Name').text_frame.paragraphs[0],'Darryl Benson')
set_para(shape_by_text(f,'Enter AOP ID').text_frame.paragraphs[0],'None')
set_para(shape_by_text(f,'Intake').text_frame.paragraphs[0],'Roadmap')

prob=shape_by_text(f,'Connected devices Wesco sells').text_frame.paragraphs
set_para(prob[0],'Connected devices Wesco sells, cameras first and then access control and network devices, are installed and left under-managed. They drift out of support, license and cyber compliance, their health is unknown until something fails, and nobody is accountable for them after the sale.')
set_para(prob[2],f'Connected Device Assurance (CDA) is a multi-vendor managed service sold as one annual fee per site with one service level. Wesco keeps covered devices inventoried, current and healthy from a Wesco operations center and carries remediation through to the field with the integrator attached to the account. CDA is built on entroCIM by the entroCIM team, sponsored by Global Enterprise, and opens accounts for advanced-services selling with pull-through to ALM, WAM and device refresh.')

ben=table_by_cell(f,0,0,'New recurring').cell(0,0).text_frame.paragraphs
items=[f'New recurring service revenue from the installed base, one annual fee per site ({g("run_rate_2031")} run rate across {g("sites_2031")} sites by 2031 in the pro forma; illustrative)',
 'A door opener for Global Enterprise sellers moving to advanced-services selling, with pull-through to ALM, WAM and device refresh',
 'Customers get one accountable owner across manufacturers: inventory, support status, cyber posture, health and approved firmware changes, with evidence',
 'Fewer truck rolls: faults surface before failure and eligible ones are cleared remotely',
 'Integrator-inclusive delivery: Wesco layers on top of integrator business rather than displacing it',
 'Built on entroCIM and SkySpark, so the platform investment already made carries a second product']
assert len(ben)==len(items), (len(ben),len(items))
for p,txt in zip(ben,items): set_para(p,txt)

bt=table_by_cell(f,1,0,'Benefit')
set_cell(bt.cell(2,0),'Five-year revenue, 2027 to 2031'); set_cell(bt.cell(2,1),g('five_year_revenue'))
set_cell(bt.cell(3,0),'Recurring run rate, end of 2031'); set_cell(bt.cell(3,1),g('run_rate_2031'))
set_cell(bt.cell(4,0),'Gross margin at the site fee'); set_cell(bt.cell(4,1),g('gm_large')+' per site')
set_cell(bt.cell(5,0),'Net cash, 2027 to 2031 (illustrative)'); set_cell(bt.cell(5,1),'+'+g('el_net_cash'))

ct=table_by_cell(f,0,0,'Line item')
set_cell(ct.cell(1,0),'Seed Funding'); set_cell(ct.cell(1,1),'None')
set_cell(ct.cell(2,0),'OPEX'); set_cell(ct.cell(2,1),'entroCIM budget')
set_cell(ct.cell(3,0),'CAPEX'); set_cell(ct.cell(3,1),'In the site fee')
set_cell(ct.cell(4,0),'Total Cost'); set_cell(ct.cell(4,1),'None in FY27')
for rw in ct.rows: rw.height=In(0.26)
# shift the right column down to make room for the five leadership rows
for sh in f.shapes:
    if sh.has_table and sh.table.cell(0,0).text.strip().startswith('Resource Dependencies'): sh.top=In(3.60)
    if sh.has_table and sh.table.cell(0,0).text.strip().startswith('Line item'): sh.top=In(5.53)
    if sh.has_text_frame and sh.text_frame.text.strip().startswith('Project Cost Estimate'): sh.top=In(5.31)

lt=table_by_cell(f,0,0,'Role')
set_cell(lt.cell(1,1),'Sean McCloskey')
set_cell(lt.cell(2,0),'Business Sponsor'); set_cell(lt.cell(2,1),'Bill Muczko, Global Enterprise')
set_cell(lt.cell(3,0),'Owner / Delivery Partner'); set_cell(lt.cell(3,1),'Darryl Benson; Matt Powers')

qt=table_by_cell(f,0,0,'QUESTIONS')
set_cell(qt.cell(1,1),'Existing'); set_cell(qt.cell(1,2),'No Planview #; on the entroCIM FY27 roadmap')
set_cell(qt.cell(2,1),'Yes'); set_cell(qt.cell(2,2),'Within the entroCIM 2027 team budget; no standalone CDA line')
set_cell(qt.cell(3,1),'Attached: CDA Business Case, October 2026')
set_cell(qt.cell(4,1),'Strategy 1: Extend our leading scale and value proposition')
for rw in qt.rows: rw.height=In(0.3)
set_cell(qt.cell(5,1),'Financial Benefits (new recurring revenue); Customer Success')
set_cell(qt.cell(6,1),'No'); set_cell(qt.cell(6,2),'No seed funding or BIR for CDA')
set_cell(qt.cell(7,1),'Yes'); set_cell(qt.cell(7,2),'CSS Platforms (entroCIM team), Cyber Security, Technology Services; resource managers engaged')

kt=table_by_cell(f,0,0,'Phase')
rows=[('Roadmap | 2027 entroCIM roadmap reconciled with CDA','Oct 2026','Darryl Benson, Ron Snyder, David Blondel'),
      ('Delivery | TS business review of CDA services','Q4 2026','Matt Powers, Cody Remington'),
      ('Build | CDA on entroCIM, inside the 2027 roadmap','2027','Sequenced with entroCIM releases'),
      ('First sites | Anchor go-live, Kroger led','2028','Pro forma; depends on build and pricing')]
for i,(a,b,c) in enumerate(rows,1):
    set_cell(kt.cell(i,0),a); set_cell(kt.cell(i,1),b); set_cell(kt.cell(i,2),c)
for rw in kt.rows: rw.height=In(0.28)

rt=table_by_cell(f,0,0,'Resource Dependencies')
set_cell(rt.cell(0,2),'X'); set_cell(rt.cell(1,2),'X'); set_cell(rt.cell(2,2),'X'); set_cell(rt.cell(3,2),''); set_cell(rt.cell(4,2),'')
set_cell(rt.cell(2,1),'Operations (Technology Services)')
set_cell(rt.cell(5,1),''); set_cell(rt.cell(5,2),'')
for rw in rt.rows: rw.height=In(0.22)
set_cell(table_by_cell(f,0,0,'Estimated Priority').cell(0,1),'High')
tu=shape_by_text(f,'Template Last Updated'); tu._element.getparent().remove(tu._element)
set_cell(table_by_cell(f,0,0,'Estimated Size').cell(0,1),'Medium')

# ---------------------------------------------------------------- new slides
L={l.name:l for l in prs.slide_layouts}
def tb(s,x,y,w,h):
    box=s.shapes.add_textbox(In(x),In(y),In(w),In(h)); tf=box.text_frame; tf.word_wrap=True
    for a in ('margin_left','margin_right','margin_top','margin_bottom'): setattr(tf,a,0)
    return tf
def run(tf,text,size,bold=False,color=INK,space_after=2,first=False,italic=False):
    p=tf.paragraphs[0] if first else tf.add_paragraph(); p.space_after=Pt(space_after); p.alignment=PP_ALIGN.LEFT
    r=p.add_run(); r.text=text; r.font.size=Pt(size); r.font.bold=bold; r.font.color.rgb=color; r.font.name=F; r.font.italic=italic
    return p
def card(s,x,y,w,h,label,body,fill=NAVY,label_color=WHITE,body_color=SOFT,label_size=13,body_size=10):
    sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,In(x),In(y),In(w),In(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=fill; sh.line.fill.background(); sh.adjustments[0]=0.06; sh.shadow.inherit=False
    tf=sh.text_frame; tf.word_wrap=True
    tf.margin_left=In(0.18); tf.margin_right=In(0.18); tf.margin_top=In(0.14); tf.margin_bottom=In(0.14); tf.vertical_anchor=MSO_ANCHOR.TOP
    run(tf,label,label_size,True,label_color,space_after=3,first=True)
    for b in body: run(tf,b,body_size,False,body_color,space_after=3)
    return sh
def eyebrow(s,x,y,w,text,color=GREEN):
    tf=tb(s,x,y,w,0.22); run(tf,text.upper(),9,True,color,space_after=0,first=True)
def takeaway(s,text,y=5.92,h=0.52):
    bx=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,In(0.73),In(y),In(11.86),In(h))
    bx.fill.solid(); bx.fill.fore_color.rgb=PALE; bx.line.fill.background(); bx.adjustments[0]=0.10; bx.shadow.inherit=False
    tf=bx.text_frame; tf.word_wrap=True
    tf.margin_left=In(0.22); tf.margin_right=In(0.22); tf.margin_top=In(0.04); tf.margin_bottom=In(0.04); tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    run(tf,text,11.5,True,INK,space_after=0,first=True)
def marker(s,text='Illustrative and pending validation. Figures come from the working pro forma (v4.6, 2026-10-02).',y=6.50):
    tf=tb(s,0.73,y,11.0,0.3); run(tf,text,8.5,False,GREY,first=True,italic=True)
def table(s,x,y,w,h,data,col_w=None,size=10.5,head_size=10,row_h=0.33):
    gf=s.shapes.add_table(len(data),len(data[0]),In(x),In(y),In(w),In(h)); t=gf.table; t.first_row=True
    if col_w:
        for i,cw in enumerate(col_w): t.columns[i].width=In(cw)
    for ri,row in enumerate(data):
        t.rows[ri].height=In(row_h)
        for ci,val in enumerate(row):
            cell=t.cell(ri,ci); cell.margin_left=In(0.1); cell.margin_right=In(0.1); cell.margin_top=In(0.04); cell.margin_bottom=In(0.04)
            cell.vertical_anchor=MSO_ANCHOR.MIDDLE; cell.fill.solid(); cell.fill.fore_color.rgb=NAVY if ri==0 else (WHITE if ri%2 else MIST)
            p=cell.text_frame.paragraphs[0]; r=p.add_run(); r.text=str(val)
            r.font.size=Pt(head_size if ri==0 else size); r.font.bold=(ri==0 or ci==0); r.font.color.rgb=WHITE if ri==0 else INK; r.font.name=F
            if ci: p.alignment=PP_ALIGN.CENTER
    return t
def new(title_text):
    s=prs.slides.add_slide(L['Blank-with-Title']); s.shapes.title.text_frame.paragraphs[0].add_run().text=title_text
    for sh in list(s.placeholders):
        if sh.placeholder_format.idx!=0 and sh.has_text_frame and not sh.text_frame.text.strip() and sh.placeholder_format.type not in (13,15):
            sh._element.getparent().remove(sh._element)
    return s
def notes(s,t): s.notes_slide.notes_text_frame.text=t

# Slide: the offer and how it is delivered
a=new('The offer and how it is delivered')
tf=tb(a,0.73,1.30,11.86,0.5); run(tf,'One annual fee per site, one service level, delivered from a Wesco operations center with the integrator attached to the account.',13,False,SLATE,first=True)
eyebrow(a,0.73,2.0,5.6,'The offer')
table(a,0.73,2.3,5.6,1.7,[['Site size','Devices (typical)','Annual fee','Per device per month'],
    ['Small',g('tier_devices_s'),g('fee_small'),g('per_device_small')],
    ['Medium',g('tier_devices_m'),g('fee_medium'),g('per_device_medium')],
    ['Large',g('tier_devices_l'),g('fee_large'),g('per_device_large')]],col_w=[1.2,1.5,1.4,1.5])
tf=tb(a,0.73,4.15,5.6,1.6)
run(tf,f'Covers inventory, support and license status, cyber posture, health, approved firmware and configuration changes, and field escalation, with evidence of every action. About {g("target_margin")} percent margin at the fee; Wesco payback per site {g("payback_small")} to {g("payback_large")}.',10,False,INK,first=True,space_after=4)
run(tf,'Fee held for the first three years. From year four it can step down or hold at a higher margin. Enterprise agreements and small-branch estates (fewer than ten devices a site) still need a construct; the per-site fee is the land offer.',10,False,INK,space_after=4)
run(tf,'Cameras first because that is where Wesco and the seller already are; access control and network devices follow.',10,False,INK)
eyebrow(a,6.73,2.0,5.86,'How it is delivered')
card(a,6.73,2.3,5.86,1.05,'Wesco operations center',['A building operations center, not a network operations center: a few people in North America, a couple in Europe, the bulk in India. Tier 2 remediation from in-market people.'])
card(a,6.73,3.45,5.86,1.05,'Integrator-inclusive field work',['Failed devices follow a warranty check, replacement and dispatch to the integrator tied to the account and contract. Technology Services or partners deploy the appliance.'],fill=SLATE)
card(a,6.73,4.6,5.86,1.15,'Platform Wesco already owns',['Built on entroCIM and SkySpark by the entroCIM team, with a partner sensor for discovery. One managed appliance per site by default; central deployment, as entroCIM runs today, for large estates.'],fill=MBLUE)
takeaway(a,'Wesco layers on top of the integrators, it does not take their business. That is the delivery model Technology Services agreed to on 2026-10-14.')
marker(a)
notes(a,'Fees and payback from pro forma v4.6 Deck Figures. Delivery model as aligned with Matt Powers (VP Technology Services) on 2026-10-14; the TS business review with Matt Powers and Cody Remington is the next step. Enterprise pricing construct and small-branch delivery remain open (Peter Ferrell, Sridhar Loke, 2026-10-02).')

# Slide: where it stands
b=new('Where it stands')
tf=tb(b,0.73,1.30,11.86,0.5); run(tf,'Sponsored, aligned with Technology Services, and building inside the entroCIM roadmap. The commercial construct is the open work.',13,False,SLATE,first=True)
card(b,0.73,2.0,5.86,1.75,'Sponsorship and funding',['Bill Muczko accepted the business sponsor role at the business case review on 2026-10-02.','Not approved as a standalone FY27 investment. CDA continues on the entroCIM roadmap, built by the entroCIM team, with no separate line (Sean McCloskey, 2026-10-06).','Market positioning is unchanged: CDA stands alone to customers.'])
card(b,6.73,2.0,5.86,1.75,'Delivery',['Technology Services aligned on the operations-center, integrator-inclusive model (Matt Powers, 2026-10-14).','Next: a business review of the CDA services with Matt Powers and Cody Remington, and TS review of the service-delivery staffing in the pro forma.'],fill=SLATE)
card(b,0.73,3.9,5.86,1.85,'Anchor accounts',[f'Kroger: engaged; {g("anchor_kroger_sites")} Large sites in the plan from {g("anchor_kroger_start")}.',f'Cisco Connected Real Estate: in the plan ({g("anchor_cisco_sites")} sites) and still scoping; Cisco-side owner to be identified.',f'Three lanes still to name (pharma, automotive, a third); Bob Caprise proposes picking them from edge-device shipment data. Target {g("anchor_target_low")} to {g("anchor_target_high")} anchors.'],fill=MBLUE)
card(b,6.73,3.9,5.86,1.85,'Open work',['Enterprise pricing construct beside the per-site fee, including small-branch estates without an appliance per site.','Seller value proposition: what CDA does that the VMS does not, and how it compares with SecuriThings; two or three vertical outcome plays.','Willingness to pay, tested in the first anchor conversations.','2027 roadmap reconciliation with Ron Snyder and David Blondel.'],fill=STEEL_LIGHT,label_color=NAVY,body_color=INK)
marker(b,'Status as of 2026-10-30. Site counts are planning figures from the pro forma, not customer commitments.',y=5.95)
notes(b,'Sources: sponsorship meeting summary 2026-10-02; Sean McCloskey AOP update 2026-10-06; Matt Powers transcript 2026-10-14; SecuriThings comparison 2026-10-26; pro forma v4.6.')

# ---------------------------------------------------------------- keep, order, drop
keep=[S[0],S[6],S[8],S[10],a,b,S[17]]
ids=prs.slides._sldIdLst
by_rid={sid.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'):sid for sid in ids}
order=[]
for sl in keep:
    for rId,rel in prs.part.rels.items():
        if rel.reltype.endswith('/slide') and rel.target_part is sl.part: order.append(by_rid[rId]); break
for sid in list(ids):
    if sid not in order:
        prs.part.drop_rel(sid.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')); ids.remove(sid)
for sid in order: ids.remove(sid); ids.append(sid)
prs.save(OUT); print('wrote',OUT,'slides',len(prs.slides))
