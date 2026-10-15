# CDA Product and Business Case deck generator (python-pptx).
# Inputs: the CDA pro forma (WB path below; reads the Deck Figures tab, recalculated values) and template.pptx (Wesco template) in the working directory.
# Run from a folder containing template.pptx:  python3 build_cda_business_case_deck.py  -> writes 2026-10-02_CDA_Product_and_Business_Case.pptx
# Update WB when the pro forma version changes. Source of truth for wording: this file; hand edits in PowerPoint must be folded back in here.

from pptx import Presentation
from pptx.util import Inches as In, Pt, Emu
from pptx.dml.color import RGBColor as C
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_TICK_LABEL_POSITION, XL_AXIS_CROSSES, XL_MARKER_STYLE, XL_LABEL_POSITION

NAVY=C(0x1D,0x25,0x2D); GREEN=C(0x00,0x95,0x3A); SLATE=C(0x5B,0x7A,0x8E)
MIST=C(0xDB,0xE3,0xE9); GREY=C(0x8E,0x92,0x96); WHITE=C(0xFF,0xFF,0xFF)
INK=C(0x2B,0x2B,0x2B); SOFT=C(0xC9,0xD1,0xD6)
PALE=C(0xE9,0xF3,0xEC); GREENT=C(0x00,0xAA,0x13)
# v4.7 brand data colors: Mechanical Blue family, Steel Grey tints, Granite Grey, build-year shading
MBLUE=C(0x00,0x49,0x86); MBLUE_MID=C(0x2F,0x66,0x99); MBLUE_LIGHT=C(0x5A,0x87,0xAE); MBLUE_TINT=C(0xCC,0xDA,0xE7)
STEEL_LIGHT=C(0xF1,0xF5,0xF7); STEEL_MID=C(0xDF,0xE8,0xED); STEEL_DARK=C(0xB7,0xC9,0xD3)
GRANITE=C(0x4F,0x75,0x8B); BUILD_SHADE=C(0xF2,0xF4,0xF5)
F='Arial'
prs=Presentation('template.pptx')
ids=prs.slides._sldIdLst
for sid in list(ids):
    rId=sid.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
    prs.part.drop_rel(rId); ids.remove(sid)
L={l.name:l for l in prs.slide_layouts}

def add(layout): return prs.slides.add_slide(L[layout])
NO={}   # slide title -> slide number, filled as slides are built, so cross-references follow the order
def title(s,t):
    s.shapes.title.text_frame.paragraphs[0].add_run().text=t; NO[t]=len(prs.slides._sldIdLst); return s
def drop_empty(s):
    for sh in list(s.placeholders):
        if sh.has_text_frame and not sh.text_frame.text.strip() and sh.placeholder_format.idx!=0:
            if sh.placeholder_format.type in (13,15): continue
            sh._element.getparent().remove(sh._element)
def tb(s,x,y,w,h):
    box=s.shapes.add_textbox(In(x),In(y),In(w),In(h)); tf=box.text_frame
    tf.word_wrap=True
    for a in ('margin_left','margin_right','margin_top','margin_bottom'): setattr(tf,a,0)
    return tf
def run(tf,text,size,bold=False,color=INK,space_after=2,first=False,italic=False):
    p=tf.paragraphs[0] if first else tf.add_paragraph()
    p.space_after=Pt(space_after); p.alignment=PP_ALIGN.LEFT
    r=p.add_run(); r.text=text
    r.font.size=Pt(size); r.font.bold=bold; r.font.color.rgb=color; r.font.name=F; r.font.italic=italic
    return p
def nobullet(p):
    from pptx.oxml.ns import qn
    pPr=p._p.get_or_add_pPr(); pPr.append(pPr.makeelement(qn('a:buNone'),{}))
def headline(s,text,kicker=None,upper=True):
    tf=tb(s,0.73,1.30,11.86,0.5)
    run(tf,text,13,False,SLATE,first=True)
    if kicker: run(tf,kicker.upper() if upper else kicker,10.5,True,GREEN,space_after=0)
def card(s,x,y,w,h,label,body,fill=NAVY,label_color=WHITE,body_color=SOFT,label_size=13,body_size=10):
    sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,In(x),In(y),In(w),In(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=fill; sh.line.fill.background()
    sh.adjustments[0]=0.06; sh.shadow.inherit=False
    tf=sh.text_frame; tf.word_wrap=True
    tf.margin_left=In(0.18); tf.margin_right=In(0.18); tf.margin_top=In(0.14); tf.margin_bottom=In(0.14)
    tf.vertical_anchor=MSO_ANCHOR.TOP
    run(tf,label,label_size,True,label_color,space_after=3,first=True)
    for b in body: run(tf,b,body_size,False,body_color,space_after=3)
    return sh
def stat(s,x,y,w,value,label,color=NAVY,vsize=30):
    tf=tb(s,x,y,w,1.0)
    run(tf,value,vsize,True,color,space_after=0,first=True)
    run(tf,label,9.5,False,GREY,space_after=0)
def takeaway(s,text,y=5.92,h=0.52):
    bx=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,In(0.73),In(y),In(11.86),In(h))
    bx.fill.solid(); bx.fill.fore_color.rgb=PALE; bx.line.fill.background()
    bx.adjustments[0]=0.10; bx.shadow.inherit=False
    tf=bx.text_frame; tf.word_wrap=True
    tf.margin_left=In(0.22); tf.margin_right=In(0.22); tf.margin_top=In(0.04); tf.margin_bottom=In(0.04)
    tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    run(tf,text,11.5,True,INK,space_after=0,first=True)
    return bx
def eyebrow(s,x,y,w,text,color=GREEN):
    tf=tb(s,x,y,w,0.22); run(tf,text.upper(),9,True,color,space_after=0,first=True)
def arrow(s,x,y,w=0.34,h=0.24):
    a=s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,In(x),In(y),In(w),In(h))
    a.fill.solid(); a.fill.fore_color.rgb=GREENT; a.line.fill.background(); a.shadow.inherit=False
    return a
def chip(s,x,y,w,h,num,text,fill=NAVY,tcolor=WHITE):
    sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,In(x),In(y),In(w),In(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=fill; sh.line.fill.background()
    sh.adjustments[0]=0.14; sh.shadow.inherit=False
    tf=sh.text_frame; tf.word_wrap=True
    tf.margin_left=In(0.14); tf.margin_right=In(0.10); tf.margin_top=In(0.04); tf.margin_bottom=In(0.04)
    tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    p=run(tf,num+'   '+text,10,True,tcolor,space_after=0,first=True)
    return sh
def marker(s,text='Illustrative and pending validation. Figures come from the working pro forma.',y=6.50):
    tf=tb(s,0.73,y,11.0,0.3); run(tf,text,8.5,False,GREY,first=True,italic=True)
def table(s,x,y,w,h,data,col_w=None,size=10.5,head_size=10,row_h=0.33):
    gf=s.shapes.add_table(len(data),len(data[0]),In(x),In(y),In(w),In(h)); t=gf.table; t.first_row=True
    if col_w:
        for i,cw in enumerate(col_w): t.columns[i].width=In(cw)
    for ri,row in enumerate(data):
        t.rows[ri].height=In(row_h)
        for ci,val in enumerate(row):
            cell=t.cell(ri,ci); cell.margin_left=In(0.1); cell.margin_right=In(0.1)
            cell.margin_top=In(0.04); cell.margin_bottom=In(0.04); cell.vertical_anchor=MSO_ANCHOR.MIDDLE
            cell.fill.solid(); cell.fill.fore_color.rgb=NAVY if ri==0 else (WHITE if ri%2 else MIST)
            p=cell.text_frame.paragraphs[0]; r=p.add_run(); r.text=str(val)
            r.font.size=Pt(head_size if ri==0 else size); r.font.bold=(ri==0 or ci==0)
            r.font.color.rgb=WHITE if ri==0 else INK; r.font.name=F
            if ci: p.alignment=PP_ALIGN.CENTER
    return t
def notes(s,t): s.notes_slide.notes_text_frame.text=t


# ---------------------------------------------------------------- figures
# Every displayed number comes from the Deck Figures tab of the recalculated pro forma.
import openpyxl
WB='/mnt/user-data/outputs/2026-10-02_CDA_Pro_Forma_v4.6.xlsx'
_ws=openpyxl.load_workbook(WB,data_only=True)['Deck Figures']
FIG={}; VAL={}; LAB={}
for _r in range(6,_ws.max_row+1):
    _k=_ws.cell(_r,2).value
    if _k and _ws.cell(_r,6).value is not None:
        FIG[_k]=_ws.cell(_r,5).value; VAL[_k]=_ws.cell(_r,4).value; LAB[_k]=_ws.cell(_r,3).value
for _k,_v in FIG.items():
    assert _v is not None and not (isinstance(_v,str) and _v.startswith('#')), _k
# every check row on the tab has to read OK, including the AOP tie-out (2027 development = submitted FY27 AOP figure)
_checks=[_k for _k in FIG if _k.endswith('_check') or _k=='staffing_tieback']
assert 'aop_tie_check' in _checks and len(_checks)>=10, _checks
for _k in _checks:
    assert FIG[_k]=='OK', _k
assert VAL['aop_tie_check']=='OK'
def g(k): return FIG[k]
def pct_words(k): return g(k).replace('%',' percent')
assert g('gm_small')==g('gm_medium')==g('gm_large')
assert VAL['golive_year_share']==0.5 and VAL['plan_years']==len(('2027','2028','2029','2030','2031'))   # the text says half a year in the go-live year, over five years
# v4.5: Kroger is the largest anchor but no longer the majority of sites. No text says "majority"; the shares are quoted from g().
assert VAL['kroger_site_share_2031']<0.5 and 0<VAL['kroger_revenue_share_2031']<1
YRS=['2027','2028','2029','2030','2031']
WORDS1={1:'one',2:'two',3:'three'}
WORDS={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty'}
def words_n(n):
    """A whole number as words for running text; digits with separators when it has no word form."""
    n=int(round(n))
    if n in WORDS: return WORDS[n]
    if n==100: return 'one hundred'
    return f'{n:,}'
def cap(t): return t[:1].upper()+t[1:]
def plural(n,one,many): return one if int(round(n))==1 else many
# commission rate as words at a sentence start ("Five"), digits when it is not a whole number
_rate=round(VAL['commission_rate']*100,6)
RATE_START=cap(words_n(_rate)) if _rate==int(_rate) else f'{_rate:g}'
assert VAL['commission_years']==VAL['contract_years']
TSS_MONTHS=plural(VAL['tss_lead_months'],'month','months')
AIMS=f"{cap(words_n(VAL['anchor_target_low']))} to {words_n(VAL['anchor_target_high'])}"   # Bob's three to five anchors
TIERS=['small','medium','large']

# 1 ---------------------------------------------------------------- title
s=add('Title Slide')
for ph in s.placeholders:
    i=ph.placeholder_format.idx
    if i==12: ph.text_frame.paragraphs[0].add_run().text='Connected Device Assurance'
    elif i==16: run(ph.text_frame,'A managed service for the devices we sell',first=True,size=14,color=INK)
    elif i==1: ph.text_frame.paragraphs[0].add_run().text='October 2, 2026'
notes(s,'Two decisions this deck is asking for: Bill Muczko to sponsor the product, and support for the FY27 AOP position. The product story runs first, the financial case second. Every figure is from the working pro forma and is illustrative until the pilot.')

# ---------------------------------------------------------------- drawing helpers (native shapes)
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.dml import MSO_LINE_DASH_STYLE as MSO_LINE
from pptx.enum.chart import XL_TICK_LABEL_POSITION, XL_AXIS_CROSSES, XL_MARKER_STYLE, XL_LABEL_POSITION
from pptx.oxml.ns import qn
from lxml import etree
import math, copy
def box(s,x,y,w,h,fill=None,line=None,lw=1.25,dash=False,rounded=True,adj=0.08):
    sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,In(x),In(y),In(w),In(h))
    if rounded: sh.adjustments[0]=adj
    if fill is None: sh.fill.background()
    else: sh.fill.solid(); sh.fill.fore_color.rgb=fill
    if line is None: sh.line.fill.background()
    else:
        sh.line.color.rgb=line; sh.line.width=Pt(lw)
        if dash: sh.line.dash_style=MSO_LINE.DASH
    sh.shadow.inherit=False
    return sh
def label_in(sh,lines,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE,margin=0.08):
    """lines: list of (text,size,bold,color)."""
    tf=sh.text_frame; tf.word_wrap=True; tf.vertical_anchor=anchor
    for a in ('margin_left','margin_right'): setattr(tf,a,In(margin))
    tf.margin_top=In(0.03); tf.margin_bottom=In(0.03)
    for i,(t,sz,b,c) in enumerate(lines):
        p=run(tf,t,sz,b,c,space_after=1,first=(i==0)); p.alignment=align
    return sh
def txt(s,x,y,w,h,lines,align=PP_ALIGN.LEFT,anchor=MSO_ANCHOR.TOP):
    tf=tb(s,x,y,w,h); tf.vertical_anchor=anchor
    for i,(t,sz,b,c) in enumerate(lines):
        p=run(tf,t,sz,b,c,space_after=1,first=(i==0)); p.alignment=align
    return tf
def conn(s,x1,y1,x2,y2,color=GREY,lw=1.25,dash=False,arrowhead=False):
    c=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,In(x1),In(y1),In(x2),In(y2))
    c.line.color.rgb=color; c.line.width=Pt(lw)
    if dash: c.line.dash_style=MSO_LINE.DASH
    if arrowhead:
        ln=c.line._get_or_add_ln()
        ln.append(ln.makeelement(qn('a:tailEnd'),{'type':'triangle','w':'med','len':'med'}))
    return c
def poly(s,pts,fill):
    ff=s.shapes.build_freeform(In(pts[0][0]),In(pts[0][1]),scale=1.0)
    ff.add_line_segments([(In(x),In(y)) for x,y in pts[1:]],close=True)
    sh=ff.convert_to_shape(); sh.fill.solid(); sh.fill.fore_color.rgb=fill; sh.line.fill.background(); sh.shadow.inherit=False
    return sh
def plot_layout(chart,x,y,w,h):
    pa=chart._chartSpace.chart.plotArea
    old=pa.find(qn('c:layout'))
    if old is not None: pa.remove(old)
    lay=etree.SubElement(pa,qn('c:layout')); pa.remove(lay); pa.insert(0,lay)
    ml=etree.SubElement(lay,qn('c:manualLayout'))
    for tag,val in (('layoutTarget','inner'),('xMode','edge'),('yMode','edge'),('x',x),('y',y),('w',w),('h',h)):
        etree.SubElement(ml,qn('c:'+tag)).set('val',str(val))

# 2 ---------------------------------------------------------------- after the sale
s=title(add('Blank-with-Title'),'After the initial sale')
headline(s,'Wesco sells the devices, and then nobody owns them. Firmware ages, inventories drift, and customers find out only when something fails or an auditor asks.')
SALE_X,INST_X,BW=2.03,3.28,1.15
DIV_X=4.60; YX0=4.75; YW=1.52; YG=0.045
yx=[YX0+i*(YW+YG) for i in range(5)]
for x,w_,t in [(SALE_X,BW,'Sale'),(INST_X,BW,'Install')]+[(yx[i],YW,f'Year {i+1}') for i in range(5)]:
    txt(s,x,1.93,w_,0.22,[(t.upper(),9,True,SLATE)],align=PP_ALIGN.CENTER)
LANES=[('Today',2.22,1.40),('With CDA',3.78,1.20)]
for lab,y0,h in LANES:
    txt(s,0.73,y0,1.25,h,[(lab,13,True,NAVY)],anchor=MSO_ANCHOR.MIDDLE)
conn(s,0.73,3.70,12.59,3.70,SOFT,0.75)
# Today lane
for x,t in ((SALE_X,'Sale'),(INST_X,'Install')):
    label_in(box(s,x,2.52,BW,0.60,NAVY),[(t,11,True,WHITE)])
conn(s,YX0,3.02,yx[4]+YW,3.02,GREY,1.5,dash=True)
txt(s,yx[0],2.55,3.0,0.4,[('Accountability in question',11,True,INK)])
txt(s,yx[2],2.55,3.0,0.4,[('Spreadsheet records',11,True,INK)])
WEDGE_END=yx[3]+YW
poly(s,[(YX0,3.07),(WEDGE_END,3.07),(WEDGE_END,3.58)],SOFT)
txt(s,yx[4]+0.05,3.08,YW,0.5,[('Risk builds silently',11,True,INK)])
# With CDA lane
for x,t in ((SALE_X,'Sale'),(INST_X,'Install')):
    label_in(box(s,x,3.93,BW,0.60,NAVY),[(t,11,True,WHITE)])
for x in yx:
    label_in(box(s,x,3.93,YW,0.60,GREEN),[('Annual fee',11,True,WHITE)])
txt(s,YX0,4.62,7.84,0.3,[('Inventory, patch, secure: run by Wesco, no tool for the customer to staff',10.5,False,INK)],align=PP_ALIGN.CENTER)
conn(s,DIV_X,1.95,DIV_X,5.05,SLATE,1.25,dash=True)
txt(s,DIV_X-1.5,5.10,3.0,0.25,[("Today, Wesco's role ends here",9.5,True,SLATE)],align=PP_ALIGN.CENTER)
takeaway(s,'After the sale nobody owns the devices; that gap is where recurring revenue lives.')
notes(s,'Source for the problem: Bill Muczko\'s estimate that customers are not managing camera assets effectively across about 85 percent of the Fortune 200 account base, and that where they monitor at all they use spreadsheets. It is his estimate from owning the relationships, not a measured figure. Do not harden it. '
      'The point of this slide is that the problem is ownership: the customer does not want another tool, they want somebody accountable. The five-year span is a drawing convention; the service renews each year for as long as the customer keeps it.')

# 3 ---------------------------------------------------------------- the service
s=title(add('Blank-with-Title'),'The service')
headline(s,'Wesco keeps the customer\'s connected devices inventoried, current and secure, for one annual fee per site.')
band=box(s,0.73,1.95,11.86,1.75,GREEN,adj=0.10)
txt(s,0.95,1.95,2.3,1.75,[('One annual fee per site',16,True,WHITE)],anchor=MSO_ANCHOR.MIDDLE)
SEGX=3.45; SEGW=(12.49-SEGX-0.2)/3
for i,(t,l) in enumerate([('Inventory','A current device record.'),('Patch','Firmware and configuration to baseline.'),('Secure','Posture watched and remediated with approval.')]):
    label_in(box(s,SEGX+i*(SEGW+0.1),2.07,SEGW,1.51,NAVY,adj=0.06),[(t,16,True,WHITE),(l,11,False,SOFT)])
eyebrow(s,0.73,3.95,6.0,'How it runs, on their site')
steps=[('1','Connect once'),('2','Find every device'),('3','Assess continuously'),('4','Remediate with approval')]
for i,(n,t) in enumerate(steps):
    chip(s,0.73+i*3.02,4.21,2.70,0.42,n,t)
    if i<3: arrow(s,0.73+i*3.02+2.78,4.30,0.18,0.24)
tf=tb(s,0.73,4.88,11.86,0.6)
run(tf,'Cameras first, because that is where Wesco is strongest and where the gap is widest. Access control, building and OT systems, power and cooling, and network devices follow on the same connection.',11.5,False,INK,first=True)
takeaway(s,'One service, one price, one accountable owner.')
notes(s,'Say it in one sentence and stop: we keep the devices we sold you inventoried, current and secure, and we charge one annual fee for it. The detail behind each line is in the appendix. '
      'Sellers should lead with what the customer never does: no capital purchase, no staff to hire or tool to learn, no integration project. Those are the three objections that kill managed services, and the one fee answers all three.')

# 4 ---------------------------------------------------------------- why wesco
s=title(add('Blank-with-Title'),'Why Wesco')
headline(s,'Four things this needs. Wesco already has all four, which is why this is an assembly rather than a build.',
         'Bob Caprise: "Have you ever had a Reese\'s Cup? Best idea on the planet." Two things nobody has put together.',upper=False)
BLK4=[('The install base',['Wesco is the largest Axis reseller in the market, and sells the access control, network and power devices alongside it.']),
 ('The secure connection',['Airwall gives an authorized way into a customer site that their security team will accept.']),
 ('The platform',['entroCIM already running in production, with connectors to the devices in scope.']),
 ('The people',['TSS and the managed services team already work inside customer sites every day.'])]
for i,(lab,body) in enumerate(BLK4):
    card(s,0.73+i*3.05,1.98,2.85,1.30,lab,body,fill=NAVY,label_size=12.5,body_size=9.5)
NBX,NBW,NBY=2.93,7.46,3.92
label_in(box(s,NBX,NBY,NBW,0.62,WHITE,line=NAVY,lw=1.75),[('What is new: entroCIM components for CDA and a service organization in TSS',11.5,True,NAVY)])
for i in range(4):
    conn(s,0.73+i*3.05+1.425,3.30,NBX+0.75+i*(NBW-1.5)/3,NBY-0.02,GREENT,1.75,arrowhead=True)
card(s,0.73,4.78,11.86,0.52,'Already built, in production: Axis and Hanwha connectors live in entroCIM today',[],fill=GREEN,label_size=12)
takeaway(s,'The differentiator is coverage of the site, and a single accountable owner.')
notes(s,'Bob Caprise\'s framing, worth using in the room: two good things nobody has combined. The partner piece is the one nobody has put together: the largest Axis install base combined with a leading cyber-posture sensor, sold as one service. '
      'Competing tools are one class at a time: device managers for cameras, RMM for IT, DCIM for data centers, OT platforms for plants. None of them covers the whole site. '
      f'Also worth saying plainly: this is an {words_n(VAL["build_months"])}-month build with the existing team, not a new platform. '
      f'The FY27 AOP figure is {g("aop_fy27_build")}.')

# 5 ---------------------------------------------------------------- portfolio effect
s=title(add('Blank-with-Title'),'Three platforms stronger')
headline(s,'Every covered device produces operating data, evidence and field work, and that output feeds platforms Wesco already funds.','Carried forward from the August 28 executive brief',upper=False)
card(s,0.73,2.05,3.00,3.30,'Connected Device Assurance',['Every covered device produces operating data, evidence and field work.','That output strengthens the rest of the portfolio rather than sitting inside one product.'],fill=GREEN,label_size=13,body_size=10)
rows=[('WAM','Lifecycle, failure and end-of-support signals delivered to Sales, with hardware pull-through from the service\'s own data.','Intelligent Asset Management'),
 ('Navigator','Field work orders and escalations land in Navigator, in support of the 2027 redesign integrations.','Ascent Data Center Services'),
 ('entroCIM','The platform we already own carries both service tools, raising the return on containerization.','Intelligent Facility Management')]
for i,(plat,body,outcome) in enumerate(rows):
    y=2.05+i*1.18
    arrow(s,3.755,y+0.295,0.50,0.36)
    card(s,4.28,y,4.55,0.95,plat,[body],label_size=12,body_size=9)
    arrow(s,8.865,y+0.295,0.50,0.36)
    card(s,9.40,y,3.19,0.95,outcome,[],fill=GREEN,label_size=11.5)
takeaway(s,'Built once and shared. CDA strengthens three platforms Wesco already funds rather than adding a fourth.')
notes(s,'This page comes straight from the August 28 executive brief and is the portfolio argument rather than the product argument. The August enterprise product list already describes CDA as the foundation for Intelligent Asset Management and Intelligent Facility Management, so this is the framing the company has already published. For an AOP conversation it is the answer to why the portfolio funds this rather than a point product.')

# 6 ---------------------------------------------------------------- how it sells
s=title(add('Blank-with-Title'),'How it sells')
headline(s,'Three site sizes, one annual fee each. The seller sizes the site and quotes the fee. No point counts, no license mechanics.')
eyebrow(s,0.73,1.90,5.0,'The price list',SLATE)
table(s,0.73,2.15,11.86,1.32,[
 ['Site size','Typical site','Devices covered','Annual fee'],
 ['Small','Branch, clinic, small office',f'Up to about {g("tier_devices_s")}',g('fee_small')],
 ['Medium','Larger branch, small plant, distribution point',f'Up to about {g("tier_devices_m")}',g('fee_medium')],
 ['Large','Retail store, plant, hospital, logistics hub',f'Up to about {g("tier_devices_l")}',g('fee_large')]],col_w=[2.4,4.6,2.6,2.26])
txt(s,0.73,3.60,11.86,0.25,[(f'For comparison with per-device offers: about {g("per_device_small")} / {g("per_device_medium")} / {g("per_device_large")} per device per month at Small / Medium / Large',9.5,False,GREY)])
for i,(lab,body) in enumerate([('Hard-to-connect sites',[f'A site with separate networks or restricted access needs a second collector. It is quoted at the site fee plus about {g("complexity_adder")} a year.']),
 ('Who buys it',['The person accountable for cyber risk on the site: security, facilities or IT operations, depending on the account.']),
 ('The first conversation',['Start with cameras at one site. One appliance, an agreed device list, nothing for the customer to staff.'])]):
    card(s,0.73+i*4.06,4.00,3.80,1.40,lab,body,fill=GREEN if i==2 else NAVY,label_size=12,body_size=9.5)
takeaway(s,'A seller needs three numbers and one sentence.')
marker(s,f'Illustrative. Fees are cost plus a {g("target_margin")} percent target margin on the sourced bill of materials. They are working prices, not an approved list.',5.62)
notes(s,'Prices are set deliberately and held, not recalculated per deal. Component costs move our margin, not the customer\'s price. Discounts are a decision, not an output. The points, license increments and quartermaster mechanics behind the sizes stay internal and are in the appendix. '
      f'The per-device figure is for comparison with per-device offers such as Axis Device Manager. Kroger\'s {g("kroger_per_camera_quote")} per camera needs confirming as one-time or annual.')

# 7 ---------------------------------------------------------------- what a seller earns
s=title(add('Blank-with-Title'),'What a seller earns')
headline(s,f'{RATE_START} percent of {words_n(VAL["commission_years"])}-year contract value, paid at signing, split {g("share_rep")} / {g("share_manager")} / {g("share_inside")} across the sales chain. Follows the entroCIM commission structure.')
BAR_X=5.0; BAR_MAX=6.0
maxpool=max(VAL['pool_small_1'],VAL['pool_medium_10'],VAL['pool_large_100'])
eyebrow(s,BAR_X,1.92,6.0,'Commission pool at signing, one scale',SLATE)
def _deal(k,t,noun,cy):
    n=int(VAL[f'deal_{k}_sites'])
    assert k.endswith('_'+str(n))      # the key names the deal size, the value has to agree
    return (k,f'{cap(words_n(n))} {t} {plural(n,noun,noun+"s")}',n,t[0].lower(),cy)
DEALS=[_deal('small_1','Small','site',2.42),_deal('medium_10','Medium','site',3.22),_deal('large_100','Large','store',4.35)]
PITCH,SQ=0.125,0.10
for k,lab,n,t,cy in DEALS:
    big=(VAL['pool_'+k]==maxpool)
    rows_=math.ceil(n/10); gy=cy-(rows_*PITCH-(PITCH-SQ))/2
    for j in range(n):
        box(s,0.73+(j%10)*PITCH,gy+(j//10)*PITCH,SQ,SQ,GREEN if big else MBLUE,rounded=False)
    txt(s,2.15,cy-0.36,2.75,0.72,[(lab,12,True,NAVY),(f'{n} x {g("fee_exact_"+t)} a year',10,False,INK),(f'{cap(words_n(VAL["commission_years"]))}-year value {g("deal_"+k+"_value")}',9.5,False,GREY)],anchor=MSO_ANCHOR.MIDDLE)
    bl=max(0.05,BAR_MAX*VAL['pool_'+k]/maxpool)
    box(s,BAR_X,cy-0.19,bl,0.38,GREEN if big else MBLUE,rounded=False)
    txt(s,BAR_X+bl+0.1,cy-0.19,1.5,0.38,[(g('pool_'+k),15,True,INK)],anchor=MSO_ANCHOR.MIDDLE)
    txt(s,BAR_X,cy+0.22,7.0,0.25,[(f'Rep {g("deal_"+k+"_rep")}, manager {g("deal_"+k+"_manager")}, inside sales {g("deal_"+k+"_inside")}',9.5,False,GREY)])
takeaway(s,f'{cap(words_n(VAL["deal_large_100_sites"]))} stores pays the sales chain {g("pool_large_100")} at signing.')
marker(s,'Illustrative, pending acceptance of the commission structure for CDA. Structure from Nate Kehr, 2026-09-29.',5.62)
notes(s,f'This slide is for Bob and the sellers, not the executive path. Each deal is {words_n(VAL["commission_years"])} years of the annual fee at the number of sites shown; the bars are the commission pool, drawn to one scale. '
      f'The pool is {g("commission_rate")} percent of that contract value, paid up front at signing, and split {g("share_rep")} percent to the rep, {g("share_manager")} percent to the sales manager or director and {g("share_inside")} percent to inside sales. '
      'That is the entroCIM structure as Nate Kehr described it on September 29; it still has to be accepted for CDA.')

# 8 ---------------------------------------------------------------- one site
s=title(add('Blank-with-Title'),'One site')
headline(s,'What a site costs Wesco to stand up, what it earns, and how quickly it pays back, at each size. Kroger stores are the Large case.')
for x,c,l in ((1.75,MBLUE,f'Cost to serve, years 1 to {g("recovery_years")}'),(3.95,SOFT,'Upfront cost recovered each year'),(6.45,GREEN,'Margin kept')):
    box(s,x,1.84,0.16,0.16,c,rounded=False); txt(s,x+0.22,1.80,2.6,0.25,[(l,9.5,False,INK)])
assert FIG['bar_check']=='OK'
B0=1.75; BMAX=7.2; fmax=VAL['fee_exact_l']
TN={'s':'small','m':'medium','l':'large'}
for i,(t,n) in enumerate((('s','Small'),('m','Medium'),('l','Large'))):
    y=2.10+i*0.42
    txt(s,0.73,y,0.95,0.32,[(n,11,True,NAVY)],anchor=MSO_ANCHOR.MIDDLE)
    x=B0
    for k,fill,tc in (('serve_build_'+t,MBLUE,WHITE),('upfront_recovered_'+TN[t],SOFT,INK),('margin_kept_'+t,GREEN,WHITE)):
        wd=BMAX*VAL[k]/fmax
        label_in(box(s,x,y,wd,0.32,fill,rounded=False),[(g(k),9,True,tc)],margin=0.02)
        x+=wd
    txt(s,x+0.08,y,1.0,0.32,[(g('fee_exact_'+t),11,True,INK)],anchor=MSO_ANCHOR.MIDDLE)
    tf=tb(s,10.35,y,2.24,0.32); tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    p=run(tf,g('gm_'+TN[t]),13,True,GREEN,first=True,space_after=0)
    r2=p.add_run(); r2.text='   Wesco payback '+g('payback_'+TN[t]); r2.font.size=Pt(9.5); r2.font.color.rgb=GREY; r2.font.name=F
HRS=f'{g("service_hours_s")} / {g("service_hours_m")} / {g("service_hours_l")}'
txt(s,0.73,3.33,11.86,0.34,[(f'Cost to serve: service labor at {HRS} hours a month, software renewals ({words_n(VAL["renewal_years_in_window"])} of {words_n(VAL["recovery_years"])} years, the first is in the upfront), and a field reserve. '
    f'Upfront, recovered over {words_n(VAL["recovery_years"])} years: appliance and staging, SkySpark license, entroCIM licensing, sensing and connectivity software, commissioning.',9.5,False,GREY)])
# recovery window
RY=3.74; CHW=1.45
for j in range(int(VAL['recovery_years'])):
    chip(s,0.73+j*(CHW+0.05),RY,CHW,0.27,f'Year {j+1}','')
span_end=0.73+int(VAL['recovery_years'])*(CHW+0.05)-0.05
conn(s,0.73,RY+0.33,span_end,RY+0.33,SLATE,0.75)
conn(s,0.73,RY+0.29,0.73,RY+0.33,SLATE,0.75); conn(s,span_end,RY+0.29,span_end,RY+0.33,SLATE,0.75)
txt(s,0.73,RY+0.35,span_end-0.73,0.2,[('Upfront recovered inside the fee',9,True,SLATE)],align=PP_ALIGN.CENTER)
arrow(s,span_end+0.12,RY+0.02,0.42,0.24)
G4X=span_end+0.66
chip(s,G4X,RY,1.9,0.27,f'Year {int(VAL["recovery_years"])+1} onward','',fill=GREEN)
txt(s,G4X+2.02,RY-0.03,12.59-G4X-2.02,0.62,[(f'Fee could step down to {g("fee_year4_s")} / {g("fee_year4_m")} / {g("fee_year4_l")} at the same margin',9.5,True,INK),
    (f'or hold and earn {g("margin_if_held_year4_s")} / {g("margin_if_held_year4_m")} / {g("margin_if_held_year4_l")}',9.5,False,INK)])
eyebrow(s,0.73,4.50,6.0,'How payback is measured',SLATE)
txt(s,0.73,4.72,11.86,0.8,[('Wesco payback is the number of months a site takes to earn back the cash Wesco spends to start it: the upfront cost plus the sales commission paid at signing. Each month the site repays that from its fee, less the cost to serve. In year one the cost to serve leaves out software renewals, because the first year of licenses is bought with the upfront.',10.5,False,INK)])
takeaway(s,f'One site makes money at every size, and after year {words_n(VAL["recovery_years"])} the upfront is paid for: step the fee down, or keep it and earn more.')
marker(s,'Illustrative. Hardware, software and license costs are sourced. Service hours, margin target and volumes are estimates.',5.62)
notes(s,f'This is the slide to spend time on. If someone believes the unit, the {words_n(VAL["plan_years"])}-year plan is arithmetic. Every bar is one year of fee during the recovery window, split into what it costs to run the site, the share of the upfront cost recovered that year, and the margin kept. '
      f'The cost to serve in the bars covers years one to {words_n(VAL["recovery_years"])} and counts {words_n(VAL["renewal_years_in_window"])} of {words_n(VAL["recovery_years"])} years of software renewals, because the first year of licenses is bought with the upfront. From year {WORDS[int(VAL["recovery_years"])+1]}, with a full year of renewals, cost to serve is {g("cost_to_serve_small")} / {g("cost_to_serve_medium")} / {g("cost_to_serve_large")} a year, and that is the basis for the step-down fee. '
      f'Fees are published at {g("fee_small")} / {g("fee_medium")} / {g("fee_large")}, set from the sourced bill of materials at the {g("target_margin")} percent target, so each size earns about {g("target_margin")} percent. '
      f'After year {g("recovery_years")} the upfront is paid for. The plan assumes the fee holds, which earns {g("margin_if_held_year4_s")} / {g("margin_if_held_year4_m")} / {g("margin_if_held_year4_l")}. '
      f'The step-down to {g("fee_year4_s")} / {g("fee_year4_m")} / {g("fee_year4_l")} is a renewal lever for sales, not a plan assumption. '
      f'The Small fee is the one to watch: the per-node software stack costs the same at {g("tier_devices_s")} devices as at {g("tier_devices_l")}, which puts Small at about {g("per_device_small")} per device per month against {g("per_device_large")} at Large. '
      f'Vendor software, not labor, is the largest line in the steady-state cost to serve, {g("software_share_large")} percent of it at a Large site.'
      f' Payback counts Wesco cash only: the upfront of {g("upfront_small")} / {g("upfront_medium")} / {g("upfront_large")} plus commission of {g("commission_site_s")} / {g("commission_site_m")} / {g("commission_site_l")}, repaid from the fee less the cost to serve. Development, the team and marketing are platform costs and are recovered at the plan level, which the Plan slide shows.')

# the five anchors, shared by the Anchor accounts and Sites in the plan slides
ANCH=[('kroger','Kroger','Retail'),('cisco','Cisco','Corporate real estate'),('pharma','Pharma','To name'),('auto','Automotive','To name'),('third','Third lane','To name')]
NAMED=2   # Kroger and Cisco are named; the other three are placeholders
def av(a,k): return VAL[f'anchor_{a}_{k}']

# 8a ---------------------------------------------------------------- anchors
s=title(add('Blank-with-Title'),'Anchor accounts')
headline(s,f'{AIMS} accounts across different lanes, from our largest customers. {cap(words_n(NAMED))} are named, {words_n(len(ANCH)-NAMED)} are still to name.','Bob Caprise\'s test: if the top accounts will not buy it, nobody else will sell it',upper=False)
BANDS=[('Engaged',1.95,1.0),('Scoping',3.03,1.0),('To name',4.11,0.66)]
for lab,y,h in BANDS:
    box(s,0.73,y,11.86,h,MIST,adj=0.08)
    txt(s,0.90,y,1.2,h,[(lab,12,True,NAVY)],anchor=MSO_ANCHOR.MIDDLE)
card(s,2.15,2.00,10.36,0.90,'Kroger, retail',[f'Has asked for a device manager already, at about {g("kroger_per_camera_quote")} per camera.',
     'A per-camera fee on the Axis sale contributes to the launch.'],fill=GREEN,label_size=12,body_size=9.5)
card(s,2.15,3.08,10.36,0.90,'Cisco real estate, scoping',[f'NetBotz monitoring in MDFs worldwide: a heartbeat with no vitals and no power data. {g("anchor_cisco_sites")} sites at about {g("cisco_devices_per_site")} devices each.',
     f'In the plan from {g("anchor_cisco_start")}. Opens the data center conversation Sean asked us to validate.'],fill=SLATE,label_size=12,body_size=9.5)
for i,t in enumerate(['Pharma','Automotive','Third lane']):
    label_in(box(s,2.15+i*3.49,4.18,3.38,0.52,WHITE,line=NAVY,lw=1.5,adj=0.10),[(t,11.5,True,NAVY)])
tf=tb(s,0.73,4.86,11.86,0.6)
run(tf,f'One enterprise win carries hundreds of sites. That is why anchors matter more than pipeline at this stage: the first account both funds the launch and proves the model. The plan runs on Kroger and Cisco plus {words_n(len(ANCH)-NAMED)} accounts still to be named.',11,False,INK,first=True)
takeaway(s,'Named accounts, not a market estimate, are what makes this real.')
marker(s,'Illustrative. Kroger and Cisco figures are from the pro forma; their site and device counts are Bob Caprise\'s working figures, and the other anchors are placeholders.',5.62)
notes(s,f'Cisco is in the plan from {g("anchor_cisco_start")} and its status is still scoping: {g("anchor_cisco_sites")} MDF sites at {g("cisco_devices_per_site")} devices each, priced as Medium sites. Only Kroger has asked for anything so far. Bob Caprise is still identifying the current owner on the Cisco side, so the plan carries Cisco on his working figures. The {g("anchor_cisco_sites")} is his figure for NetBotz sites, and the device count per MDF is worth confirming with him because it sets the tier. Today those sites have a heartbeat and no vitals or power data, which is the gap the service fills, and the account opens the data center conversation Sean asked us to validate. '
      f'Naming the {words_n(len(ANCH)-NAMED)} open lanes, pharma, automotive and one more from the top accounts, is the ask to sales leadership; each one proves a different lane and a different buyer. '
      f'Three questions for Bob and Bill. Does the per-camera fee ride on Kroger\'s cameras only, or on all Wesco Axis sales? What annual camera volume would it ride on? Is Kroger\'s {g("kroger_per_camera_quote")} per camera one-time or annual? '
      f'At Kroger\'s {g("kroger_cameras_per_year")} cameras a year, the {g("camera_fee")} fee is about {g("kroger_camera_fee_annual")} a year against a {g("build_2027")} build.')

# 8b --------------------------------------------------------------- sites in the plan
s=title(add('Blank-with-Title'),'Sites in the plan')
# the five anchors have to add up to the plan, and the equation has to tie to the Model run rate
assert sum(av(a,'sites') for a,_,_ in ANCH)==VAL['sites_2031']
assert sum(av(a,'devices') for a,_,_ in ANCH)==VAL['devices_2031']
assert FIG['equation_check']=='OK' and VAL['sites_small_2031']==0     # no Small term in the equation line
assert g('equation_total')==g('run_rate_2031')
assert av('kroger','sites')==max(av(a,'sites') for a,_,_ in ANCH)        # longest bar is Kroger
assert all(g(f'anchor_{a}_name') and 'TBD' not in g(f'anchor_{a}_name') for a,_,_ in ANCH[:NAMED])
assert all('TBD' in g(f'anchor_{a}_name') for a,_,_ in ANCH[NAMED:])
assert VAL['sites_large_2031']==av('kroger','sites') and VAL['sites_medium_2031']==VAL['sites_2031']-av('kroger','sites')
assert [av(a,'tier') for a,_,_ in ANCH]==['Large']+['Medium']*4
headline(s,f'The {words_n(len(ANCH))} anchor accounts bring {g("sites_2031")} sites and {g("devices_2031")} devices by 2031.')
# --- Gantt with totals (v4.7). Every label is read from a Deck Figures key.
FULLY={a_:VAL[f'anchor_{a_}_full_year'] for a_,_,_ in ANCH}                 # a year, or 'after 2031'
RAMP={a_:VAL[f'anchor_{a_}_ramping_2031'] for a_,_,_ in ANCH}
assert FIG['installed_check']=='OK' and VAL['anchor_full_year_check']=='OK'
assert all(isinstance(FULLY[a_],(int,float)) != RAMP[a_] for a_,_,_ in ANCH)  # a ramping account has no full year yet
for a_,_,_ in ANCH:
    assert VAL[f'anchor_{a_}_sites_2031']==av(a_,'sites')
    _first=[int(y) for y in YRS if VAL[f'anchor_{a_}_sites_{y}']>0][0]
    assert _first==int(av(a_,'start')), a_                                       # the first segment is the go-live year
for y in YRS: assert sum(VAL[f'anchor_{a_}_sites_{y}'] for a_,_,_ in ANCH)==VAL[f'installed_sites_{y}']
assert VAL['installed_sites_2031']==VAL['sites_2031']
GX0,CW9G=3.55,1.40; GX1=GX0+5*CW9G                    # year grid: five equal columns
RT,PITCH,BH=1.92,0.52,0.32; RB=RT+5*PITCH             # row block top and bottom
LEG_Y=1.56; SLANT=0.40
def ycol(y): return GX0+(int(y)-int(YRS[0]))*CW9G
# legend and column headers on one row
box(s,0.73,LEG_Y+0.045,0.16,0.16,MBLUE,rounded=False); txt(s,0.95,LEG_Y,1.4,0.25,[('Named account',9.5,False,INK)],anchor=MSO_ANCHOR.MIDDLE)
box(s,2.30,LEG_Y+0.045,0.16,0.16,None,line=GRANITE,lw=1.0,dash=True,rounded=False); txt(s,2.52,LEG_Y,0.9,0.25,[('To name',9.5,False,INK)],anchor=MSO_ANCHOR.MIDDLE)
for y in YRS:
    txt(s,ycol(y),LEG_Y,CW9G,0.25,[(y,11,True,GREY if y==YRS[0] else NAVY)],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
txt(s,GX1+0.20,LEG_Y,12.59-GX1-0.20,0.25,[('2031 run rate',10.5,False,GREY)],anchor=MSO_ANCHOR.MIDDLE)
conn(s,0.73,RT-0.03,12.59,RT-0.03,SOFT,0.75)
# build-year column shading, then gridlines at the column boundaries
box(s,GX0,RT,CW9G,RB-RT,BUILD_SHADE,rounded=False).name='build_year_shade'
for i in range(6): conn(s,GX0+i*CW9G,RT,GX0+i*CW9G,RB,STEEL_MID,0.75)
txt(s,GX0+0.20,RT,CW9G-0.40,RB-RT,[('Build year',11,True,GRANITE),('Development only, no sites',10,False,GREY)],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
def seg(s,x0,x1,y0,h,fill,line,lw,dash,slant,text,tcolor,name):
    """One year of one account: a rectangle, or a parallelogram with a slanted left edge for the go-live year."""
    if slant:
        ff=s.shapes.build_freeform(In(x0),In(y0+h),scale=1.0)
        ff.add_line_segments([(In(x0+slant),In(y0)),(In(x1),In(y0)),(In(x1),In(y0+h))],close=True)
        sh=ff.convert_to_shape(); sh.fill.solid(); sh.fill.fore_color.rgb=fill; sh.shadow.inherit=False
        sh.line.color.rgb=line; sh.line.width=Pt(lw)
        if dash: sh.line.dash_style=MSO_LINE.DASH
    else:
        sh=box(s,x0,y0,x1-x0,h,fill,line=line,lw=lw,dash=dash,rounded=False)
    tf=sh.text_frame; tf.word_wrap=False; tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    tf.margin_left=In(slant+0.02); tf.margin_right=In(0.02); tf.margin_top=In(0.0); tf.margin_bottom=In(0.0)
    p=run(tf,text,12,True,tcolor,space_after=0,first=True); p.alignment=PP_ALIGN.CENTER
    sh.name=name
    return sh
SEGTXT={}
for i,(a_,nm,lane) in enumerate(ANCH):
    ry=RT+i*PITCH; by=ry+(PITCH-BH)/2
    txt(s,0.73,ry,2.75,PITCH,[(nm,12,True,NAVY),(f'{lane}, {g("anchor_"+a_+"_tier")}',10,False,GREY)],anchor=MSO_ANCHOR.MIDDLE)
    named=i<NAMED; start=int(av(a_,'start')); full=FULLY[a_] if isinstance(FULLY[a_],(int,float)) else 9999
    for y in YRS:
        if int(y)<start: continue
        if int(y)>=full: fill=MBLUE if named else STEEL_DARK            # fully deployed, and every year after
        elif int(y)==start: fill=MBLUE_LIGHT if named else STEEL_LIGHT   # go-live year
        else: fill=MBLUE_MID if named else STEEL_MID                     # still building toward the full count
        lab=g(f'anchor_{a_}_sites_{y}')+(' sites' if y==YRS[-1] else '')
        SEGTXT[(a_,y)]=lab
        seg(s,ycol(y),ycol(y)+CW9G,by,BH,fill,
            WHITE if named else GRANITE,0.75 if named else 1.0,not named,SLANT if int(y)==start else 0,
            lab,WHITE if named else NAVY,f'seg_{a_}_{y}')
    txt(s,GX1+0.20,ry,12.59-GX1-0.20,PITCH,[(f'{g("anchor_"+a_+"_runrate")} a year',12,True,NAVY),(f'{g("anchor_"+a_+"_devices")} devices',10,False,GREY)],anchor=MSO_ANCHOR.MIDDLE)
# totals row: green rule, label, installed sites at the end of each year
TY=RB+0.08
conn(s,0.73,TY,GX1,TY,GREENT,2.0)
txt(s,0.73,TY+0.06,2.75,0.34,[('Installed sites, end of year',11,True,NAVY)],anchor=MSO_ANCHOR.MIDDLE)
TOT={}
for y in YRS:
    TOT[y]=g(f'installed_sites_{y}')
    tf_=txt(s,ycol(y),TY+0.06,CW9G,0.34,[(TOT[y],14,True,GREY if y==YRS[0] else NAVY)],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    s.shapes[-1].name=f'total_{y}'
# the equation: one site's fee times the sites each anchor brings; it is the 2031 run rate
EQY=TY+0.50
conn(s,0.73,EQY,12.59,EQY,SOFT,0.75)
txt(s,0.73,EQY+0.09,11.86,0.3,[(f'{g("sites_large_2031")} Large sites × {g("fee_exact_l")} + {g("sites_medium_2031")} Medium sites × {g("fee_exact_m")} = {g("equation_total")} a year at {YRS[-1]} sites',12.5,True,INK)])
takeaway(s,f'Kroger and Cisco are {g("named_runrate_share")} of the run rate; the {words_n(len(ANCH)-NAMED)} anchors still to name are the rest.')
marker(s,'Illustrative. Kroger and Cisco site and device counts are Bob Caprise\'s working figures; pharma, automotive and the third lane are placeholders.',5.62)
# the labels on the slide are the Deck Figures values, read back from the shapes
_by={sh.name:sh for sh in s.shapes}
for (a_,y),lab in SEGTXT.items():
    _t=_by[f'seg_{a_}_{y}'].text_frame.text
    assert _t==(g(f'anchor_{a_}_sites_{y}')+(' sites' if y==YRS[-1] else '')), (a_,y,_t)
for y in YRS: assert _by[f'total_{y}'].text_frame.text==g(f'installed_sites_{y}')==FIG[f'installed_sites_{y}']
# which accounts are fully deployed in which year, and which are still ramping, from the anchor_*_full_year / anchor_*_ramping_2031 keys
NOTE_NAME={a_:(nm if i<NAMED else ('the '+nm.lower() if nm.lower().endswith('lane') else nm.lower())) for i,(a_,nm,_) in enumerate(ANCH)}
def _join(names): return names[0] if len(names)==1 else ', '.join(names[:-1])+' and '+names[-1]
_deployed={}
for a_,_,_ in ANCH:
    if not RAMP[a_]: _deployed.setdefault(int(VAL[f'anchor_{a_}_full_year']),[]).append(NOTE_NAME[a_])
_ramping=[NOTE_NAME[a_] for a_,_,_ in ANCH if RAMP[a_]]
_parts=[f'{_join(n)} {"is" if len(n)==1 else "are"} fully deployed in {y}' if k==0 else f'{_join(n)} in {y}' for k,(y,n) in enumerate(sorted(_deployed.items()))]
RAMP_SENT=(', '.join(_parts)+f'; {_join(_ramping)} {"is" if len(_ramping)==1 else "are"} still ramping in {YRS[-1]}, so the run rate grows after the plan period.')
for a_,_,_ in ANCH:     # the sentence agrees with the keys, account by account
    _before,_after=RAMP_SENT.split('; ')
    if RAMP[a_]: assert NOTE_NAME[a_] in _after and NOTE_NAME[a_] not in _before, a_
    else: assert NOTE_NAME[a_] in _before and NOTE_NAME[a_] not in _after and f'{g("anchor_"+a_+"_full_year")}' in _before, a_
_k_end=int(VAL['anchor_kroger_start'])+int(round(VAL['anchor_kroger_sites']/VAL['anchor_kroger_new_per_year']))-1
assert VAL['anchor_kroger_new_per_year']*(_k_end-int(VAL['anchor_kroger_start'])+1)==VAL['anchor_kroger_sites']
assert VAL['anchor_cisco_start']==2029 and VAL['anchor_cisco_sites_2029']<VAL['anchor_cisco_sites_2030']<VAL['anchor_cisco_sites']   # notes quote the rollout by year end from 2029
# placeholders: all three share one Medium profile and a first-year / step rollout (read from the Accounts tab for the assertion only)
_ac=openpyxl.load_workbook(WB,data_only=True)['Accounts']
for _base in (77,112,147):
    _new=[_ac.cell(_base+7,c).value for c in range(3,8)]; _new=[x for x in _new if x]
    assert _new[0]==VAL['placeholder_first_year_sites'] and all(x==VAL['placeholder_step_sites'] for x in _new[1:]), _new
    assert _ac.cell(_base+1,3).value==VAL['placeholder_points_per_site']
notes(s,'This slide is the arithmetic between One site and the Plan: one site\'s fee, multiplied by the sites each anchor brings. '
      f'Each bar shows installed sites at the end of each year, starting in the account\'s go-live year, when sites come on through the year. {YRS[0]} is the build year, with no sites. '
      f'{g("sites_large_2031")} Large sites at {g("fee_exact_l")} and {g("sites_medium_2031")} Medium sites at {g("fee_exact_m")} come to {g("equation_total")} a year at {YRS[-1]} sites, which is the {YRS[-1]} run rate the Plan slide builds toward. '
      f'{RAMP_SENT} '
      f'The run rates by account are rounded, so they can add to a tenth of a million more or less than the total. '
      f'Kroger: Large stores, {g("anchor_kroger_new_per_year")} a year from {g("anchor_kroger_start")} to {_k_end}, {g("anchor_kroger_sites")} stores and {g("anchor_kroger_devices")} devices in all. '
      f'Cisco: {g("anchor_cisco_sites")} MDF sites that are monitored today only by NetBotz, {g("cisco_devices_per_site")} devices each, rolling out from {g("anchor_cisco_start")} ({g("anchor_cisco_sites_2029")}, {g("anchor_cisco_sites_2030")} and {g("anchor_cisco_sites")} sites by year end), '
      f'with a {g("cisco_survey_fee")} one-time survey fee per new site. The survey fee is in revenue but not in the run rate, because the run rate counts site subscriptions only. '
      f'Both counts are Bob Caprise\'s working figures. Kroger is {g("kroger_site_share_2031")} of sites and {g("kroger_revenue_share_2031")} of 2031 revenue. '
      f'Run rate and 2031 revenue differ for two reasons. Under the half-year convention a site earns half a year in the year it goes live, so 2031 revenue in the Plan chart, ${float(g("revenue_2031")):.1f}M, sits below the {g("run_rate_2031")} run rate. '
      'Revenue also includes the survey and per-camera fees, which the run rate leaves out. '
      f'Pharma, automotive and the third lane follow the same Medium profile ({g("placeholder_points_per_site")} points, {g("placeholder_devices_per_site")} devices per site), '
      f'with {g("placeholder_first_year_sites")} sites in the first year and {g("placeholder_step_sites")} a year after that. They are there to show what the sponsor ask has to produce.')

# 9 ---------------------------------------------------------------- plan
s=title(add('Blank-with-Title'),'Plan, 2027 to 2031')
assert VAL['cum_cash_2031']>0 and str(int(VAL['cash_trough_year']))=='2029'
headline(s,f'Build in 2027, first sites in 2028, then recurring revenue that compounds. The cash line is the investment: it bottoms in {g("cash_trough_year")} and crosses zero in {g("break_even_year")}.')
CX9,CY,CW9,CH=0.73,2.0,11.86,2.95
VMIN,VMAX,VSTEP=-6,12,2   # v4.5: 2031 revenue is above 10 and peak cash is below -3, so the axis runs -6 to 12
REV=[g('revenue_'+y) for y in YRS]; CASH=[g('cum_cash_'+y) for y in YRS]
assert max(REV)<VMAX and min(CASH)>VMIN and CASH[-1]>0 and all(c<0 for c in CASH[:-1])
PHASES=['Build','First sites','Peak investment','Recovery','Break-even']
# option 1 (Oct 1): the phase name rides under its year as a two-line category label drawn by the chart
cd=CategoryChartData(); cd.categories=[f'{y}\n{p_}' for y,p_ in zip(YRS,PHASES)]
cd.add_series('Annual revenue',tuple(REV))
cd.add_series('Cumulative net cash',tuple(CASH))
cd.add_series('Cash invested',tuple(min(c,0) for c in CASH))
cd.add_series('Cash recovered',tuple(max(c,0) for c in CASH))
gf=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,In(CX9),In(CY),In(CW9),In(CH),cd)
ch=gf.chart
ch.has_title=False; ch.font.size=Pt(9); ch.font.name=F
ch.series[0].format.fill.solid(); ch.series[0].format.fill.fore_color.rgb=MBLUE_TINT
pl=ch.plots[0]; pl.gap_width=80; pl.has_data_labels=True; pl.data_labels.number_format='0.0'; pl.data_labels.number_format_is_linked=False
pl.data_labels.font.size=Pt(9); pl.data_labels.font.color.rgb=GREY; pl.data_labels.position=XL_LABEL_POSITION.OUTSIDE_END
cax=ch.category_axis; cax.tick_label_position=XL_TICK_LABEL_POSITION.LOW
cax.format.line.color.rgb=INK; cax.format.line.width=Pt(1.25); cax.tick_labels.font.size=Pt(9); cax.tick_labels.font.color.rgb=INK
from pptx.enum.chart import XL_TICK_MARK
cax.major_tick_mark=XL_TICK_MARK.NONE
va=ch.value_axis; va.minimum_scale=VMIN; va.maximum_scale=VMAX; va.major_unit=VSTEP
va.has_major_gridlines=True; va.major_gridlines.format.line.color.rgb=C(0xD9,0xD9,0xD9); va.major_gridlines.format.line.width=Pt(0.75)
va.tick_labels.number_format='0'; va.tick_labels.number_format_is_linked=False; va.tick_labels.font.size=Pt(9); va.tick_labels.font.color.rgb=GREY
va.format.line.fill.background(); va.major_tick_mark=XL_TICK_MARK.NONE
ch.value_axis.crosses=XL_AXIS_CROSSES.AUTOMATIC
# split the series: bar (revenue), area (invested, recovered), line (cash)
NSDECL='xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"'
def X(xml): return etree.fromstring(f'<root {NSDECL}>{xml}</root>')[0]
G9='00953A'; SL='5B7A8E'
pa=ch._chartSpace.chart.plotArea
bar=pa.find(qn('c:barChart'))
sers=bar.findall(qn('c:ser'))
for sr in sers[1:]:
    bar.remove(sr)
    for el in sr.findall(qn('c:invertIfNegative')): sr.remove(el)
s_cash,s_inv,s_rec=sers[1],sers[2],sers[3]
def after_tx(sr,els):
    pos=list(sr).index(sr.find(qn('c:tx')))+1
    for el in reversed(els): sr.insert(pos,el)
NUMFMT='#,##0.0;"−"#,##0.0'
TXPR=lambda sz,b,col: (f'<c:txPr><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="{sz}" b="{b}"><a:solidFill><a:srgbClr val="{col}"/></a:solidFill>'
                       f'<a:latin typeface="Arial"/></a:defRPr></a:pPr><a:endParaRPr lang="en-US"/></a:p></c:txPr>')
FLAGS='<c:showLegendKey val="0"/><c:showVal val="1"/><c:showCatName val="0"/><c:showSerName val="0"/><c:showPercent val="0"/><c:showBubbleSize val="0"/>'
LAST=len(YRS)-1
dl_last=(f'<c:dLbl><c:idx val="{LAST}"/><c:tx><c:rich><a:bodyPr/><a:lstStyle/>'
         f'<a:p><a:pPr><a:defRPr sz="900" b="1"/></a:pPr><a:r><a:rPr lang="en-US" sz="900" b="1"><a:solidFill><a:srgbClr val="{G9}"/></a:solidFill><a:latin typeface="Arial"/></a:rPr><a:t>+{g("cum_cash_"+YRS[LAST]):.1f}</a:t></a:r></a:p>'
         f'<a:p><a:pPr><a:defRPr sz="750"/></a:pPr><a:r><a:rPr lang="en-US" sz="750" b="0"><a:solidFill><a:srgbClr val="{G9}"/></a:solidFill><a:latin typeface="Arial"/></a:rPr><a:t>net cash</a:t></a:r></a:p>'
         f'</c:rich></c:tx><c:spPr><a:noFill/><a:ln><a:noFill/></a:ln></c:spPr><c:dLblPos val="t"/>{FLAGS}</c:dLbl>')
after_tx(s_cash,[X(f'<c:spPr><a:ln w="28575" cap="rnd"><a:solidFill><a:srgbClr val="{G9}"/></a:solidFill><a:round/></a:ln></c:spPr>'),
    X(f'<c:marker><c:symbol val="circle"/><c:size val="7"/><c:spPr><a:solidFill><a:srgbClr val="{G9}"/></a:solidFill><a:ln><a:solidFill><a:srgbClr val="{G9}"/></a:solidFill></a:ln></c:spPr></c:marker>'),
    X(f'<c:dLbls>{dl_last}<c:numFmt formatCode=\'{NUMFMT}\' sourceLinked="0"/><c:spPr><a:noFill/><a:ln><a:noFill/></a:ln></c:spPr>{TXPR(900,1,G9)}<c:dLblPos val="b"/>{FLAGS}</c:dLbls>')])
s_cash.append(X('<c:smooth val="0"/>'))
after_tx(s_inv,[X(f'<c:spPr><a:pattFill prst="ltUpDiag"><a:fgClr><a:srgbClr val="{SL}"/></a:fgClr><a:bgClr><a:srgbClr val="FFFFFF"/></a:bgClr></a:pattFill><a:ln><a:noFill/></a:ln></c:spPr>')])
after_tx(s_rec,[X(f'<c:spPr><a:solidFill><a:srgbClr val="{G9}"><a:alpha val="25000"/></a:srgbClr></a:solidFill><a:ln><a:noFill/></a:ln></c:spPr>')])
axids=bar.findall(qn('c:axId'))
ac=X('<c:areaChart><c:grouping val="standard"/><c:varyColors val="0"/></c:areaChart>')
ac.append(s_inv); ac.append(s_rec)
for ax in axids: ac.append(copy.deepcopy(ax))
lc=X('<c:lineChart><c:grouping val="standard"/><c:varyColors val="0"/></c:lineChart>')
lc.append(s_cash); lc.append(X('<c:marker val="1"/>'))
for ax in axids: lc.append(copy.deepcopy(ax))
bar.addnext(ac); ac.addnext(lc)
# series index follows display order (bar, area, area, line) so the legend entry index means the same in every renderer
for sr,n_ in ((s_inv,1),(s_rec,2),(s_cash,3)):
    sr.find(qn('c:idx')).set('val',str(n_)); sr.find(qn('c:order')).set('val',str(n_))
assert [el.tag.split('}')[1] for el in pa if el.tag.split('}')[1] in ('barChart','areaChart','lineChart','catAx','valAx')]==['barChart','areaChart','lineChart','catAx','valAx']
# legend at the top, left-aligned, without the recovered entry (legend entry 2)
ch.has_legend=True; ch.legend.position=XL_LEGEND_POSITION.TOP; ch.legend.include_in_layout=False; ch.legend.font.size=Pt(9)
leg=ch._chartSpace.chart.find(qn('c:legend'))
lp=leg.find(qn('c:legendPos'))
lp.addnext(X('<c:legendEntry><c:idx val="2"/><c:delete val="1"/></c:legendEntry>'))
LGX,LGY,LGW,LGH=0.045,0.03,0.42,0.075
ly=X(f'<c:layout><c:manualLayout><c:xMode val="edge"/><c:yMode val="edge"/><c:x val="{LGX}"/><c:y val="{LGY}"/><c:w val="{LGW}"/><c:h val="{LGH}"/></c:manualLayout></c:layout>')
leg.find(qn('c:legendEntry')).addnext(ly)
PLX,PLY,PLW,PLH=0.045,0.14,0.945,0.72
plot_layout(ch,PLX,PLY,PLW,PLH)
txt(s,CX9+CW9*(LGX+LGW)+0.1,CY+CH*LGY+0.02,1.6,0.2,[('$M, illustrative',9,False,GREY)])
# callouts
px0=CX9+CW9*PLX; pw=CW9*PLW; py0=CY+CH*PLY; ph=CH*PLH; catw=pw/5
def vy(v): return py0+(VMAX-v)/(VMAX-VMIN)*ph
def cx(i): return px0+(i+0.5)*catw
def callout(x,y,w,text):
    b_=s.shapes.add_textbox(In(x),In(y),In(w),In(0.2)); b_.fill.solid(); b_.fill.fore_color.rgb=WHITE
    tf=b_.text_frame; tf.word_wrap=False
    for a in ('margin_left','margin_right','margin_top','margin_bottom'): setattr(tf,a,In(0.02))
    run(tf,text,10,True,INK,first=True,space_after=0)
it=YRS.index(g('cash_trough_year'))
callout(cx(it)+0.28,vy(CASH[it])+0.14,1.65,f'Peak investment {g("peak_cash")}')
v0,v1=CASH[3],CASH[4]
xz=cx(3)+catw*(-v0)/(v1-v0)
callout(xz+0.14,vy(0)+0.05,1.4,f'Break-even {g("break_even_year")}')
# what the cash buys
eyebrow(s,0.73,4.98,6.0,'What the cash buys, 2027 to 2031',SLATE)
BUYS=[(1.35,g('el_development'),'Development',None),
      (4.6,g('el_cap_platform'),'entroCIM platform licenses',f'SkySpark {g("el_cap_skyspark")} external, entroCIM components {g("el_cap_entrocim")} internal'),
      (1.75,g('el_cap_othersw'),'Other software',None),(1.5,g('el_cap_hardware'),'Hardware',None),(2.4,g('el_team'),'Team, commission and marketing',None)]
bx=0.73
for wd,v,l,sub in BUYS:
    if sub is None:
        txt(s,bx,5.17,wd,0.42,[(v,12.5,True,NAVY),(l,8,False,GREY)])
    else:
        tf=txt(s,bx,5.17,wd,0.42,[(v,12.5,True,NAVY),(sub,8,False,GREY)])
        r_=tf.paragraphs[0].add_run(); r_.text='  '+l; r_.font.size=Pt(9); r_.font.bold=True; r_.font.color.rgb=SLATE; r_.font.name=F
    bx+=wd+0.04
assert bx<=12.62
takeaway(s,f'Peak investment is {g("peak_cash")} in {g("cash_trough_year")}; cash turns positive in {g("break_even_year")} at {g("gm_pct_2031")} gross margin and ends the plan at {g("cum_cash_end")}.')
marker(s,'Illustrative. Unit costs are sourced; volumes assume the anchor accounts adopt as planned.',5.62)
notes(s,'Gross margin is off this chart so it tells one story: revenue, and the cash it takes to get there. '
      f'If asked, margin rises from {pct_words("gm_pct_2028")} in 2028, the rollout year, to {pct_words("gm_pct_2031")} in 2031, as sites pass their first year and renewals mature into a steady state. '
      f'The model uses a half-year convention: a site earns half a year in the year it goes live, which is why 2031 revenue in the chart sits below the {g("run_rate_2031")} run rate. '
      'There is no revenue in 2027, so the year shows only the development investment, on the cash line. '
      f'Platform licensing is shown as a pair. The SkySpark points are drawn from a license Wesco buys from SkyFoundry, so the {g("el_cap_skyspark")} is external cash. '
      f'The entroCIM component charge, {g("el_cap_entrocim")} over the plan, is a charge from one Wesco product line to another and does not leave the company, so the external cash trough is shallower than the line shows. '
      f'Kroger is {g("kroger_revenue_share_2031")} of 2031 revenue and {g("kroger_site_share_2031")} of sites; Cisco is the second named anchor, and {words_n(len(ANCH)-NAMED)} are still to be named. '
      f'Cash turns positive in {g("break_even_year")}; the capital profile is in the appendix.')

# 10 ---------------------------------------------------------------- staffing
s=title(add('Blank-with-Title'),'Staffing')
# first year with a net new commissioning head, and the check that it is the peak rollout year (Staffing row 9, read for the assertion only)
NEWY=str(int(VAL['comm_absorbed_through'])+1)
_st=openpyxl.load_workbook(WB,data_only=True)['Staffing']
_new_sites={str(_st.cell(7,c).value):_st.cell(9,c).value for c in range(3,8)}
assert max(_new_sites,key=_new_sites.get)==NEWY and VAL['comm_new_'+NEWY]==1
headline(s,'Estimates pending acceptance. Two teams, two trends: commissioning follows new sites and is carried by Chad Steger\'s existing team through '
           f'{g("comm_absorbed_through")}, with {WORDS1[int(VAL["comm_new_"+NEWY])]} new head in {NEWY}, the peak rollout year; service delivery follows the installed base and is TSS capacity that has to be built. '
           f'Service hours were set so the published fee earns {g("target_margin")} percent, pending TSS review.')
SY=YRS[1:]
table(s,0.73,2.15,7.6,2.4,[
 ['Heads by year']+YRS,
 ['Commissioning, Chad Steger\'s team (heads)']+[g('comm_heads_'+y) for y in YRS],
 ['   New hires in the year']+[g('comm_hire_'+y) for y in YRS],
 ['Service delivery, TSS (heads)']+[g('tss_heads_'+y) for y in YRS],
 ['   New hires in the year']+[g('first_hire_month')]+[g('tss_hire_'+y) for y in SY]],col_w=[3.6,0.8,0.8,0.8,0.8,0.8],size=12,head_size=11,row_h=0.48)
stat(s,8.75,2.10,3.84,g('first_hire'),'First hire in seat',color=NAVY)
stat(s,8.75,3.45,3.84,f'{g("sites_per_fte_2031")} sites',f'and {g("devices_per_fte_2031")} devices per service FTE in 2031',color=NAVY)
tf=tb(s,0.73,4.85,11.86,0.4)
run(tf,f'Labor is costed at {g("cost_rate")}/hour and priced to the {g("budget_rate")}/hour Wesco budget rate.',11.5,False,INK,first=True)
takeaway(s,f'Commissioning needs {WORDS1[int(VAL["comm_new_"+NEWY])]} new head at peak; service delivery is the build, and it starts {words_n(VAL["tss_lead_months"])} {TSS_MONTHS} before the first site.')
marker(s,'Estimates from the pro forma staffing tab, derived from the plan\'s own cost lines. Pending TSS and Chad Steger\'s review.',5.62)
notes(s,f'The question to put to TSS is whether {g("sites_per_fte_2031")} sites per service FTE is credible. If it is not, the service hours per site are wrong and the fee moves. '
      f'Headcount comes from the cost already in the plan, so it cannot disagree with the P&L. The heads rows are cumulative, the people in seat at year end; the hires rows are the increment, the people added in that year. Commissioning hires are only the heads beyond what Chad Steger\'s existing team can absorb, and service delivery hires are the heads beyond existing TSS capacity, which is {words_n(VAL["tss_existing_capacity"])} until TSS says otherwise. '
      f'The first service hire has to be in seat by {g("first_hire")} to be trained before the first site goes live.')


# 12 ---------------------------------------------------------------- market
s=title(add('Blank-with-Title'),'Market')
headline(s,'Sized by site across the Fortune 200 and the large data center operators, not by a published market forecast.')
MW=11.86; tamv=VAL['tam']
box(s,0.73,1.95,MW,1.50,MIST,rounded=False)
samw=MW*VAL['sam']/tamv
txt(s,0.73+samw+0.2,2.02,MW-samw-0.35,0.6,[(g('tam'),18,True,INK),('Fortune 200 and data center sites that fit',10,False,INK)])
box(s,0.73,2.10,samw,1.35,SLATE,rounded=False)
txt(s,0.85,2.15,samw-0.2,0.55,[(g('sam'),15,True,WHITE),('Of those, what we can serve at launch',9.5,False,WHITE)])
planw=max(0.05,MW*VAL['run_rate_2031']/tamv)
box(s,0.73,2.80,planw,0.65,GREEN,rounded=False)
txt(s,0.73+planw+0.1,2.84,samw-planw-0.2,0.55,[(g('run_rate_2031'),13,True,WHITE),(f'2031 run rate, {g("som_share_revenue")} of what we can serve',9,False,WHITE)])
table(s,0.73,3.62,11.86,1.55,[['Where the sites are','Sites that fit','Annual value']]+
 [[LAB[f'sector_{k}_sites'],g(f'sector_{k}_sites'),g(f'sector_{k}_value')] for k in ('retail','other','mfg','dc')],col_w=[6.0,2.9,2.96],row_h=0.30)
takeaway(s,f'The plan needs about {g("som_share_revenue")} of what we can already reach.')
marker(s,'Illustrative. Site counts come from an external estimate of Fortune 200 locations plus a published US data center census, filtered for the device estates this service needs and for sites not managed today. Directional.',5.30)
notes(s,'Deliberately not the headline. The market number is the weakest figure in the deck and invites an argument that never resolves. The useful framing is the last line: the plan is a small share of what Wesco already reaches, so this does not depend on winning a market, only on serving accounts we hold. The three bars are drawn to one scale; the plan is the green sliver at the left.')

# 13 ---------------------------------------------------------------- evidence
s=title(add('Blank-with-Title'),'Evidence and estimates')
headline(s,'What is sourced today, and what a pilot has to prove.')
CHAIN=[('Unit cost',True,'Sourced bill of materials and rates.'),('Price',True,'Cost plus a set margin.'),('Sites',False,'Adoption inside accounts still to be named.'),
       ('Revenue',False,'Follows sites.'),('Cash',False,'Follows revenue and capital.')]
for i,(t,solid,why) in enumerate(CHAIN):
    x=0.73+i*2.465
    if solid: label_in(box(s,x,2.00,2.0,0.75,NAVY),[(t,14,True,WHITE)])
    else: label_in(box(s,x,2.00,2.0,0.75,WHITE,line=NAVY,lw=1.75,dash=True),[(t,14,True,NAVY)])
    if i<4: arrow(s,x+2.06,2.255,0.34,0.24)
    txt(s,x,2.85,2.0,0.45,[(why,10.5,False,INK)],align=PP_ALIGN.CENTER)
box(s,0.73,3.52,0.32,0.18,NAVY,rounded=False); txt(s,1.12,3.48,2.0,0.25,[('Evidence',9.5,False,INK)])
box(s,2.55,3.52,0.32,0.18,WHITE,line=NAVY,lw=1.25,dash=True,rounded=False); txt(s,2.94,3.48,3.0,0.25,[('Estimate until a pilot',9.5,False,INK)])
def blist(x,head,items,color):
    tf=tb(s,x,3.98,5.76,1.8)
    run(tf,head,14,True,color,space_after=6,first=True)
    for it_ in items: run(tf,'•  '+it_,11.5,False,INK,space_after=5)
blist(0.73,'What we know',['The platform, connectors and secure connection run in production today.',
      'The hardware and software bill of materials is sourced, not estimated.',
      'Sales leadership has confirmed the problem across the Fortune 200 base.'],NAVY)
blist(6.83,'What stays an estimate until a pilot',['What a customer will actually pay.','Adoption rates inside an account.',
      'TSS capacity to deliver at the planned sites-per-person ratio.','What the status quo costs the customer, which the pilot measures.'],SLATE)
takeaway(s,'The structure is sound and the costs are largely known. The volumes are a plan, and a pilot is what turns them into evidence.')
notes(s,'This slide is what makes the rest defensible. The chain reads left to right: the unit cost and the price are evidence today; sites, revenue and cash follow from adoption, which only a pilot and named accounts can show. Say plainly that market size and total cost of ownership will remain estimates for a long time, and that the way to resolve them is a pilot, not more analysis.')

# 14 ---------------------------------------------------------------- ask
s=title(add('Blank-with-Title'),'What is needed')
headline(s,'Three things, and they are sequential.')
asks=[('A business sponsor','Bill Muczko to sponsor CDA: review the case, help name anchor accounts, and advocate it inside sales leadership. No quota, no headcount.','Sales'),
 ('Anchor accounts',f'{AIMS} named accounts across retail, pharma and automotive, from the top of the account base.','Sales'),
 ('An AOP position','Continue the FY27 development investment on the strength of this case, with the pilot as the next evidence gate.','Portfolio')]
for i,(lab,body,who) in enumerate(asks):
    x=0.73+i*4.18
    card(s,x,2.15,3.50,1.62,lab,[body],fill=NAVY,label_size=16,body_size=12.5)
    if i<2: arrow(s,x+3.59,2.78,0.50,0.36)
    txt(s,x,3.92,3.50,0.3,[(who.upper(),10.5,True,SLATE)],align=PP_ALIGN.CENTER)
takeaway(s,'The sponsor decision comes first. Everything after it is work my team carries.')
notes(s,'For Bill: the ask is deliberately small and specific, and Bob Caprise has offered to reinforce it. For Sean: the AOP position is continuity, not a new request, and the pilot is the gate that decides whether it scales.')

# 15 ---------------------------------------------------------------- appendix divider
s=add('Section Divider_Dark')
for ph in s.placeholders:
    if ph.placeholder_format.idx==12: ph.text_frame.paragraphs[0].add_run().text='Appendix'
notes(s,'Detail for questions: how the fee is built, the capital profile, device coverage and the market method.')

# 16 ---------------------------------------------------------------- pricing build
s=title(add('Blank-with-Title'),'Appendix: how the fee is built')
POD_LABEL='list' if abs(VAL['pod_multiplier']-1)<1e-9 else g('pod_multiplier').replace('%','')+' percent discount'
headline(s,f'The fee is cost plus a {g("target_margin")} percent target margin on the sourced bill of materials. Once published it is held, and component costs move margin rather than price.')
t16=table(s,0.73,2.00,11.86,2.2,[
 ['Per site','Small','Medium','Large'],
 ['Hardware, node and staging']+[g('hardware_per_node')]*3,
 [f'Platform license (SkySpark, drawn from a {g("skyspark_license_points")}-point license)']+[g('skyspark_'+t) for t in TIERS],
 [f'entroCIM component licensing (at {POD_LABEL})']+[g('pods_'+t) for t in TIERS],
 ['Other software: sensing, fleet management, secure connection']+[g('other_sw_upfront')]*3,
 ['Commissioning labor']+[g('commissioning_'+t) for t in TIERS],
 ['Annual cost to serve from year two: people, software, field reserve']+[g('cost_to_serve_'+t) for t in TIERS],
 ['Service hours per month']+[g('service_hours_'+t) for t in 'sml'],
 ['Implied price per device per month']+[g('per_device_'+t) for t in TIERS],
 [f'Fee from year {WORDS[int(VAL["recovery_years"])+1]} at the same margin']+[g('fee_year4_'+t) for t in 'sml']],col_w=[5.4,2.15,2.15,2.16],size=9.5,head_size=9.5,row_h=0.22)
for _row in t16.rows:
    for _c in _row.cells: _c.margin_top=In(0.01); _c.margin_bottom=In(0.01)
tf=tb(s,0.73,4.30,11.86,1.2)
run(tf,f'Upfront cost is recovered inside the fee over {words_n(VAL["recovery_years"])} years. The upfront software purchase carries the first year of licenses and support, so the annual software line starts in year two. Hardware is replaced under the service agreement and refreshed on a {words_n(VAL["hardware_refresh_years_low"])} to {words_n(VAL["hardware_refresh_years"])} year cycle.',10.5,False,INK,first=True)
run(tf,f'A hard-to-connect site is priced by the same method: the second collector, its own licensing and software, and its commissioning, costed and marked up to the same target. That is about {g("complexity_adder")} a year on top of the size fee.',10.5,False,INK)
run(tf,f'entroCIM component licensing is Wesco\'s own software and can be discounted to make the service competitive without touching the third-party license. The model carries a multiplier for it, currently {POD_LABEL}; every point of discount moves the fee directly.',10.5,False,INK)
takeaway(s,'The fee is set once from sourced costs; after that, component costs move margin, not price.')
marker(s,'Illustrative. Hardware, software and license costs are sourced. Service hours, margin target and commissioning time are estimates.',5.62)
notes(s,f'The quartermaster model: Wesco buys a {g("skyspark_license_points")}-point SkySpark license and subdivides it, so license cost scales with the size of deployment rather than in fixed steps. None of this reaches a customer conversation.')


# 17 ---------------------------------------------------------------- capital
s=title(add('Blank-with-Title'),'Appendix: capital and cash')
headline(s,'Every dollar out by element, against every dollar in, 2027 to 2031.')
for i,(v,l) in enumerate([(g('capital_2031'),'Capital deployed by 2031'),(g('peak_cash'),'Peak cash requirement'),(g('break_even_year'),'Cash break-even'),(g('build_2027'),'2027 development investment')]):
    stat(s,0.73+i*3.05,1.88,2.85,v,l,vsize=24)
OUT=[('el_development','Development'),('el_cap_skyspark','SkySpark licenses'),('el_cap_entrocim','entroCIM licensing (internal)'),('el_cap_othersw','Other software'),
     ('el_cap_hardware','Hardware'),('el_commissioning','Commissioning'),('el_service_reserve','Service and field reserve'),('el_renewals','Renewals'),
     ('el_team','Team, commission and marketing')]
cats=[l for _,l in OUT]+['Revenue','Net cash']
n=len(cats); base=[None]*n; outv=[None]*n; rpos=[None]*n; rneg=[None]*n; tot=[None]*n
lvl=0.0
for i,(k,_) in enumerate(OUT):
    a=VAL[k]/1e6; base[i]=lvl if lvl else None; outv[i]=-a; lvl-=a
rev=VAL['el_revenue']/1e6; iR=len(OUT)
rneg[iR]=lvl; rpos[iR]=lvl+rev; lvl+=rev
assert abs(lvl-VAL['el_net_cash']/1e6)<1e-6 and lvl>0
tot[iR+1]=VAL['el_net_cash']/1e6
wd=CategoryChartData(); wd.categories=cats
for nm,vals in (('Base',base),('Outflow',outv),('Revenue above zero',rpos),('Revenue below zero',rneg),('Net cash',tot)):
    wd.add_series(nm,tuple(vals))
gw=s.shapes.add_chart(XL_CHART_TYPE.COLUMN_STACKED,In(0.73),In(2.78),In(11.86),In(2.78),wd)
cw=gw.chart; cw.has_legend=False; cw.has_title=False; cw.font.size=Pt(8.5); cw.font.name=F
cw.plots[0].gap_width=45; cw.plots[0].overlap=100
cw.category_axis.tick_label_position=XL_TICK_LABEL_POSITION.LOW
WMIN,WMAX=-25,5   # v4.5: total outflow is above 20, so the axis starts at -25
cw.value_axis.minimum_scale=WMIN; cw.value_axis.maximum_scale=WMAX; cw.value_axis.major_unit=5
cw.value_axis.has_major_gridlines=True; cw.value_axis.tick_labels.number_format='"$"0"M"'; cw.value_axis.tick_labels.number_format_is_linked=False
assert min(x for x in rneg if x is not None)>WMIN and VAL['el_net_cash']/1e6<WMAX
WX,WY,WW,WH=0.06,0.04,0.93,0.78
plot_layout(cw,WX,WY,WW,WH)
cw.category_axis.format.line.color.rgb=INK
sb,so,sp,sn,st=cw.series
sb.format.fill.background(); sb.format.line.fill.background()
so.format.fill.solid(); so.format.fill.fore_color.rgb=MBLUE
for sr in (sp,sn): sr.format.fill.solid(); sr.format.fill.fore_color.rgb=GREEN
st.format.fill.solid(); st.format.fill.fore_color.rgb=MBLUE
def plabel(series,idx,text,color=INK,pos=None):
    dl=series.points[idx].data_label
    tf=dl.text_frame; tf.text=text
    for r_ in tf.paragraphs[0].runs: r_.font.size=Pt(8.5); r_.font.bold=True; r_.font.color.rgb=color
    if pos is not None: dl.position=pos
wpx=0.73+11.86*WX; wpw=11.86*WW; wpy=2.78+2.78*WY; wph=2.78*WH; wcat=wpw/n
for i,(k,_) in enumerate(OUT):
    bottom=(base[i] or 0)+outv[i]
    txt(s,wpx+i*wcat,wpy+(WMAX-bottom)/(WMAX-WMIN)*wph+0.03,wcat,0.2,[('-'+g(k),8.5,True,INK)],align=PP_ALIGN.CENTER)
plabel(sn,iR,'+'+g('el_revenue'),WHITE,XL_LABEL_POSITION.CENTER)
plabel(st,iR+1,g('el_net_cash'),WHITE,XL_LABEL_POSITION.CENTER)
takeaway(s,f'Software licenses, not hardware, are the capital; {pct_words("entrocim_share_of_software")} of that is an internal entroCIM charge.')
marker(s,'Illustrative, from the pro forma. Finance has not reviewed the treatment.',5.62)
notes(s,'This is the slide to hold back unless asked. For an AOP conversation the relevant figure is the 2027 development investment; the capital profile follows once deployment is approved. '
      f'Read it left to right: every outflow over the {words_n(VAL["plan_years"])} years by element, then revenue, then the {g("el_net_cash")} the plan ends with. Software is {g("software_share_of_capital")} of capital deployed. '
      'entroCIM licensing is a charge from one Wesco product line to another and does not leave the company. '
      'Still to decide with Finance: whether hardware sits on the balance sheet or runs through a financing partner, how the per-camera fee is booked, and whether license purchases are capitalized and amortized or expensed.')

# 18 ---------------------------------------------------------------- coverage
s=title(add('Blank-with-Title'),'Appendix: device coverage')
headline(s,'One site, one subscription, whatever is on it. Cameras first because that is where Wesco is strongest.')
classes=[('Security cameras',['Drives the sale','Monitor and manage','Axis and Hanwha in production']),
 ('Access control and intrusion',['Drives the sale','Monitor and manage','Same buyer as cameras']),
 ('IoT and OT devices',['Drives the sale','Monitor now, manage phased','Facilities and OT buyers']),
 ('Data center auxiliary',['Drives the sale','Monitor now, manage phased','Power, cooling, lighting']),
 ('IT and network (SNMP)',['Does not drive the sale','Monitor only','Completes the security picture'])]
for i,(lab,body) in enumerate(classes):
    card(s,0.73+i*2.43,2.05,2.27,1.50,lab,body,fill=NAVY if i<4 else SLATE,label_size=11.5,body_size=9.5)
tf=tb(s,0.73,3.80,11.86,1.4)
run(tf,'Adding a device class deepens a site rather than opening a new market. A site is counted once and priced by the size of kit it needs.',11,False,INK,first=True)
run(tf,'IT and network devices are included from day one and are not sold as an IT tool. IT already manages those devices; covering them completes the security picture that the service leads with.',11,False,INK)
takeaway(s,'Adjacent markets, one site, one fee.')
notes(s,'The competitive point: every incumbent covers one class. Device managers for cameras, RMM for IT, DCIM for data centers, OT platforms for plants. Coverage of the whole site is the position.')

# 19 ---------------------------------------------------------------- audience guide
s=title(add('Blank-with-Title'),'Slides by audience')
headline(s,'One deck, three conversations. Nothing is rewritten between them, slides are only left out.','Internal page. Remove before the deck leaves Wesco.',upper=False)
GRID=[('After the initial sale','After the sale','Use','Use','Use'),
 ('The service','The service','Use','Use','Use'),
 ('Why Wesco','Why Wesco','Use','Use','Use'),
 ('Three platforms stronger','Three platforms stronger','Use','Use','Drop'),
 ('How it sells','How it sells','Use','Use','Use'),
 ('What a seller earns','What a seller earns','Drop','Use','Use'),
 ('One site','One site','Use','Use','Use'),
 ('Anchor accounts','Anchor accounts','Use','Use','Use'),
 ('Sites in the plan','Sites in the plan','Use','Use','If asked'),
 ('Plan, 2027 to 2031','Plan, 2027 to 2031','Use','Drop','Drop'),
 ('Staffing','Staffing','Use','If asked','Drop'),
 ('Market','Market','Use','Drop','Drop'),
 ('Evidence and estimates','Evidence and estimates','Use','Drop','Drop'),
 ('What is needed','What is needed','Use','Use','Drop'),
 ('Appendix: how the fee is built','How the fee is built','If asked','If asked','Drop'),
 ('Appendix: capital and cash','Capital and cash','If asked','Drop','Drop'),
 ('Appendix: device coverage','Device coverage','If asked','If asked','Use')]
# the grid names each slide by its actual title and number, and has to list every titled slide in deck order
_titled=[t for t,_ in sorted(NO.items(),key=lambda kv:kv[1]) if t!='Slides by audience']
assert [t for t,*_ in GRID]==_titled, (_titled,[t for t,*_ in GRID])
grid=[[f'{NO[t]}  {t}',a,b,c] for t,lab,a,b,c in GRID]
t19=table(s,0.73,1.95,11.86,3.42,[['Slide','Sean, AOP','Bill, sponsorship','Sellers']]+grid,
 col_w=[5.0,2.29,2.29,2.28],size=9,head_size=9,row_h=0.19)
for _row in t19.rows:
    for _c in _row.cells: _c.margin_top=In(0.01); _c.margin_bottom=In(0.01)
cnt=[WORDS[sum(1 for r in grid if r[c]=='Use')+1] for c in (1,2,3)]
tf=tb(s,0.73,5.43,11.86,0.45)
run(tf,f'Sean sees {cnt[0]} slides, Bill {cnt[1]}, a seller {cnt[2]}. Slide {NO["Appendix: how the fee is built"]} carries component costs and stays internal.',10.5,False,INK,first=True)
run(tf,f'The one slide to have ready rather than shown is {NO["Appendix: capital and cash"]}, capital and cash: the AOP figure is {g("aop_fy27_build")}, the 2027 development on slide {NO["Plan, 2027 to 2031"]} ({g("el_development")}), not the capital profile.',10.5,False,INK)
takeaway(s,'Sean gets the full case, Bill the sponsorship run, and sellers the mechanics.')
notes(s,'Do not present this slide. It is the routing note for the deck. For Bill the sequence is the problem in his account base, the service, why Wesco, how it sells, what a seller earns, one site, the anchor accounts, the sites in the plan and the ask. For Sean it is the same run without the commission slide, plus the plan, staffing, the market and the evidence slide. Sellers stop at the mechanics, what they earn and the device coverage.')

# 20 ---------------------------------------------------------------- end
s=add('End Slide_Logo_Dark')
for ph in s.placeholders:
    if ph.placeholder_format.idx==13:
        tf=ph.text_frame
        run(tf,'Darryl Benson',14,True,WHITE,first=True)
        run(tf,'Senior Director, CSS Platforms',11,False,SOFT)
notes(s,'Close on the sponsor ask.')

for sl in prs.slides: drop_empty(sl)
OUT='2026-10-02_CDA_Product_and_Business_Case.pptx'
prs.save(OUT)
print('slides',len(prs.slides._sldIdLst))

