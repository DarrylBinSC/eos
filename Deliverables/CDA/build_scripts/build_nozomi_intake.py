# Nozomi Guardian MSP enablement: Demand Intake deck (2026-11-06). Derived from build_cda_intake.py; Starts from the Aug 2026 intake deck (Wesco Demand Intake template),
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
OUT='Nozomi/2026-11-06_Nozomi_Guardian_Intake.pptx'
import json
NZ=json.load(open('Nozomi/nozomi_figures.json'))
def money(v): return f'${v:,.0f}'

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
set_para(ps[0],'Project Intake'); set_para(ps[1],'Nozomi Guardian MSP Enablement')
set_para(shape_by_text(t,'Month DD').text_frame.paragraphs[0],'November 6, 2026')

# ---------------------------------------------------------------- slide 7: the form
f=S[6]
set_para(shape_by_text(f,'Enter Project').text_frame.paragraphs[0],'Nozomi Guardian MSP')
set_para(shape_by_text(f,'Enter Date').text_frame.paragraphs[0],'Nov 6, 2026')
set_para(shape_by_text(f,'Enter Name').text_frame.paragraphs[0],'Darryl Benson')
set_para(shape_by_text(f,'Enter AOP ID').text_frame.paragraphs[0],'None')
prob=shape_by_text(f,'Connected devices Wesco sells').text_frame.paragraphs
set_para(prob[0],'Connected Device Assurance (CDA) is the multi-vendor, per-site managed service that keeps the connected devices Wesco sells inventoried, current, healthy and cyber-compliant after the sale. It is built on entroCIM, sponsored by Global Enterprise and delivered with Technology Services. Its cyber value proposition, discovery of every device on the site segment with firmware and vulnerability context, depends on a partner OT sensor on each CDA appliance.')
set_para(prob[2],'Nozomi Networks Guardian is the selected sensor, running as a container on the Wesco appliance with entroCIM integrating through its local API; the same capability extends to entroCIM deployments. To build, demonstrate and staff the service in 2027, Wesco needs to enroll as a Nozomi MSP, license development and lab instances, train engineers and operations leads, and take Nozomi onboarding support. An MNDA is in place. Production licenses scale with sites from 2028 and are recovered in the CDA site fee.')
ben=table_by_cell(f,0,0,'New recurring').cell(0,0).text_frame.paragraphs
items=['A cyber value proposition CDA can demonstrate to anchor accounts in 2027 and deliver from 2028',
 'Passive discovery of every connected device on the site segment, with vulnerability and firmware context, from a recognized OT security vendor',
 'Evidence customers need against CISA asset-inventory guidance, without staffing a tool themselves',
 'Opens the per-node volume negotiation that is the largest lever on the CDA fee',
 'Device visibility available to entroCIM deployments as well as CDA',
 'Complementary to Nozomi, not competitive; avoids building discovery and vulnerability assessment in entroCIM']
assert len(ben)==len(items)
for p,txt in zip(ben,items): set_para(p,txt)
bt=table_by_cell(f,1,0,'Benefit')
set_cell(bt.cell(2,0),'Enables CDA recurring revenue (pro forma 2028)'); set_cell(bt.cell(2,1),f"${NZ['revenue']['2028']/1e6:.2f}M")
set_cell(bt.cell(3,0),'CDA recurring run rate, end of 2031'); set_cell(bt.cell(3,1),g('run_rate_2031'))
set_cell(bt.cell(4,0),'Gross margin at the CDA site fee'); set_cell(bt.cell(4,1),g('gm_large'))
set_cell(bt.cell(5,0),'Direct benefit of this request'); set_cell(bt.cell(5,1),'Enabling')
ct=table_by_cell(f,0,0,'Line item')
set_cell(ct.cell(1,0),'Seed Funding'); set_cell(ct.cell(1,1),'None')
set_cell(ct.cell(2,0),'OPEX (2027)'); set_cell(ct.cell(2,1),money(NZ['total_2027'])+' placeholder')
set_cell(ct.cell(3,0),'CAPEX'); set_cell(ct.cell(3,1),'None')
set_cell(ct.cell(4,0),'Total Cost'); set_cell(ct.cell(4,1),money(NZ['total_2027'])+' (BIR)')
for rw in ct.rows: rw.height=In(0.26)
lt=table_by_cell(f,0,0,'Role')
set_cell(lt.cell(1,1),'Sean McCloskey')
set_cell(lt.cell(2,0),'Business Sponsor (CDA)'); set_cell(lt.cell(2,1),'Bill Muczko, Global Enterprise')
set_cell(lt.cell(3,0),'Owner / Delivery Partner'); set_cell(lt.cell(3,1),'Darryl Benson; Matt Powers')
qt=table_by_cell(f,0,0,'QUESTIONS')
set_cell(qt.cell(1,1),'New'); set_cell(qt.cell(1,2),'Enables CDA, which is on the entroCIM FY27 roadmap')
set_cell(qt.cell(2,1),'No'); set_cell(qt.cell(2,2),'2027 expense on the entroCIM product budget; BIR attached')
set_cell(qt.cell(3,1),'Attached: Nozomi Guardian BIR; CDA Business Case, October 2026')
set_cell(qt.cell(4,1),'Strategy 1: Extend our leading scale and value proposition')
for rw in qt.rows: rw.height=In(0.3)
set_cell(qt.cell(5,1),'Risk (reduces cyber risk for customers); Financial Benefits')
set_cell(qt.cell(6,1),'No'); set_cell(qt.cell(6,2),'Full request is in the attached BIR')
set_cell(qt.cell(7,1),'Yes'); set_cell(qt.cell(7,2),'CSS Platforms (entroCIM team), Cyber Security, Technology Services; resource managers engaged')
kt=table_by_cell(f,0,0,'Phase')
rows=[('Intake | Demand Intake submitted with BIR','Nov 2026','Darryl Benson'),
      ('Agreement | Nozomi MSP terms and licenses','Q1 2027','Darryl Benson, Legal, Cyber Security'),
      ('Enablement | Training and lab instances live','Q2 2027','CSS Platforms; Technology Services leads'),
      ('Production | Licenses scale with CDA sites','2028 on','Recovered in the CDA site fee')]
for i,(a,b,c) in enumerate(rows,1):
    set_cell(kt.cell(i,0),a); set_cell(kt.cell(i,1),b); set_cell(kt.cell(i,2),c)
for rw in kt.rows: rw.height=In(0.28)
rt=table_by_cell(f,0,0,'Resource Dependencies')
set_cell(rt.cell(0,2),'X'); set_cell(rt.cell(1,2),'X'); set_cell(rt.cell(2,1),'Operations (Technology Services)'); set_cell(rt.cell(2,2),'X'); set_cell(rt.cell(3,2),''); set_cell(rt.cell(4,2),'')
set_cell(rt.cell(5,1),''); set_cell(rt.cell(5,2),'')
for rw in rt.rows: rw.height=In(0.22)
set_cell(table_by_cell(f,0,0,'Estimated Priority').cell(0,1),'High')
set_cell(table_by_cell(f,0,0,'Estimated Size').cell(0,1),'Small')
tu=shape_by_text(f,'Template Last Updated'); tu._element.getparent().remove(tu._element)
for sh in f.shapes:
    if sh.has_table and sh.table.cell(0,0).text.strip().startswith('Resource Dependencies'): sh.top=In(3.60)
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

# Slide: Nozomi inside CDA
a=new('Nozomi Guardian inside CDA')
tf=tb(a,0.73,1.30,11.86,0.5); run(tf,'The partner sensor that gives CDA its cyber value proposition. Nozomi senses; Wesco integrates, service-wraps and is accountable.',13,False,SLATE,first=True)
eyebrow(a,0.73,2.0,5.86,'What Guardian does on the CDA appliance')
card(a,0.73,2.3,5.86,1.0,'Discovers every connected device',['Passive capture of the site device segment: cameras, access control and network gear, including devices nobody inventoried.'])
card(a,0.73,3.4,5.86,1.0,'Adds firmware and vulnerability context',['Make, model, firmware version and known vulnerabilities per device, from a recognized OT security vendor.'],fill=SLATE)
card(a,0.73,4.5,5.86,1.0,'Stays local; entroCIM integrates',['Runs as a container on the Wesco appliance. entroCIM reads Guardian\'s local API; raw traffic stays on site. Arc agents are an optional attach on customer servers.'],fill=MBLUE)
eyebrow(a,6.73,2.0,5.86,'Why Nozomi, and what is needed')
card(a,6.73,2.3,5.86,1.55,'Complementary, not competitive',['CDA centers on passive discovery and firmware validation, not pushing firmware. Nozomi fills the OT sensing layer the entroCIM team should not build.','SecuriThings and Viakoo were reviewed in Phase 2: SecuriThings is a direct competitor to CDA; neither is the sensing layer.'],fill=STEEL_LIGHT,label_color=NAVY,body_color=INK)
card(a,6.73,3.95,5.86,1.55,'Where it stands',['MNDA in place; Nozomi has offered sandbox and license access. MSP terms, Guardian container licensing on a Wesco-owned node and multi-customer terms are the open items.','Needed in 2027 to build the product: MSP enrollment, development and lab instances, training, onboarding support.'])
takeaway(a,'This request funds the 2027 enablement. Production licenses scale with CDA sites from 2028 and are recovered inside the CDA site fee.')
notes(a,'Sources: CDA Phase 2 dossiers (sensor placement rulings 2026-07-27 and 07-28), Research Log 2026-08-10 (MNDA, sandbox offer), CDA.md 2026-10-26 (SecuriThings classification). Nozomi MSP terms not yet quoted.')

# Slide: request and outlook
b=new('Request and licensing outlook')
tf=tb(b,0.73,1.30,11.86,0.5); run(tf,f'2027 enablement request of {money(NZ["total_2027"])}, planning figures pending Nozomi\'s MSP quote; production licensing then follows the CDA site plan.',13,False,SLATE,first=True)
eyebrow(b,0.73,2.0,6.4,'2027 request (BIR)')
rows=[['Line','Qty','Unit','Total']]
short={'Nozomi Networks / MSP program':'MSP program and central management','Nozomi Networks / development and lab':'Development and lab Guardian instances','Nozomi Networks / training':'Certification training (seats)','Nozomi Networks / services':'Onboarding and integration support'}
for l in NZ['lines']: rows.append([short[l['vendor']]+(' *' if l['placeholder'] else ''),str(l['qty']),money(l['unit']),money(l['qty']*l['unit'])])
rows.append(['Total 2027 request','','',money(NZ['total_2027'])])
table(b,0.73,2.3,6.4,2.2,rows,col_w=[3.4,0.7,1.1,1.2],size=10,row_h=0.34)
tf=tb(b,0.73,4.65,6.4,1.1)
run(tf,'* Planning placeholder to be replaced by Nozomi\'s quote. The lab line uses the CDA pro forma BOM figure of '+money(NZ['guardian_upfront'])+' upfront plus '+money(NZ['guardian_annual'])+' a year per node, itself marked "to source". Expense, not capital; 2027 on the entroCIM product budget.',9.5,False,INK,first=True)
eyebrow(b,7.33,2.0,5.26,'Production licensing outlook, not in this request')
orows=[['Year','New sites','Sites','Guardian licensing']]
for o in NZ['outlook']:
    if o['sites']: orows.append([str(o['year']),f"{o['new_sites']:,}",f"{o['sites']:,}",money(o['total'])])
table(b,7.33,2.3,5.26,1.9,orows,col_w=[0.9,1.2,1.0,2.16],size=10,row_h=0.34)
tf=tb(b,7.33,4.35,5.26,1.4)
run(tf,'Sites from the CDA pro forma v4.6 plan (Kroger from 2028, Cisco Connected Real Estate from 2029, three anchors to name). Licensing at the BOM placeholder: upfront on new sites plus annual on sites under contract. Recovered inside the CDA site fee at about '+g('target_margin')+' percent margin; re-set at Nozomi MSP terms. Volume terms here are the largest lever on the CDA fee.',9.5,False,INK,first=True)
marker(b,'Illustrative and pending validation. Figures from the CDA pro forma v4.6 (2026-10-02) and planning placeholders; Nozomi MSP pricing not yet quoted.',y=6.1)
notes(b,'BIR: Nozomi/2026-11-06_Nozomi_Guardian_BIR.xlsx. Figures: Nozomi/nozomi_figures.json, written by build_nozomi_bir.py from the pro forma Model and BOM tabs.')

# ---------------------------------------------------------------- keep, order, drop
keep=[S[0],S[6],a,b,S[17]]
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
