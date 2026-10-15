# 2026-10-14: onboarding review (new body) replaces 'inlet filter' and 'no new approval body' (Darryl); sentence subtitles removed.
# Vibe Coding Productization: Mike Wassil meeting deck (python-pptx, Wesco template).
# Run from a folder containing template.pptx. Helpers copied from the CDA build script.
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
    # 2026-10-14: sentence subtitles under titles removed (Darryl's standing rule); text kept in the call for the record, not drawn
    return None
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

def source(s,text,y=6.12):
    tf=tb(s,0.73,y,11.86,0.3); run(tf,text,8.5,False,GREY,first=True,italic=True)
def bracket(s,x1,x2,y,tick=0.13,color=SLATE,lw=1.25):
    ff=s.shapes.build_freeform(In(x1),In(y+tick),scale=1.0)
    ff.add_line_segments([(In(x1),In(y)),(In(x2),In(y)),(In(x2),In(y+tick))],close=False)
    sh=ff.convert_to_shape(); sh.fill.background(); sh.line.color.rgb=color; sh.line.width=Pt(lw); sh.shadow.inherit=False
    return sh
def elbow_back(s,x1,y1,x2,y2,ydrop,color=SLATE,lw=1.25,dash=True):
    """one freeform: down from (x1,y1) to ydrop, across to x2, up to y2, arrowhead at end"""
    ff=s.shapes.build_freeform(In(x1),In(y1),scale=1.0)
    ff.add_line_segments([(In(x1),In(ydrop)),(In(x2),In(ydrop)),(In(x2),In(y2))],close=False)
    sh=ff.convert_to_shape(); sh.fill.background(); sh.line.color.rgb=color; sh.line.width=Pt(lw); sh.shadow.inherit=False
    if dash: sh.line.dash_style=MSO_LINE.DASH
    ln=sh.line._get_or_add_ln(); ln.append(ln.makeelement(qn('a:tailEnd'),{'type':'triangle','w':'med','len':'med'}))
    return sh

# 1 ---------------------------------------------------------------- title
s=add('Title Slide')
for ph in s.placeholders:
    i=ph.placeholder_format.idx
    if i==12: ph.text_frame.paragraphs[0].add_run().text='Launch Studio'
    elif i==16: run(ph.text_frame,'Executive overview',first=True,size=14,color=INK)
    elif i==1: ph.text_frame.paragraphs[0].add_run().text='October 2026'
notes(s,'For the Launch Studio decision session with Sean McCloskey, with Mike Wassil in the room, which happens only if Sean supports the direction at the week-of-October-19 portfolio meeting. Two slides to present, backup behind. Darryl Benson presenting; joint initiative with Mike Wassil. Status: early concept, expected to change. Sean raised this in the October 6 AOP conversation and asked Darryl to look into it; this is the executive overview to work out next steps with him.')

# 2 ---------------------------------------------------------------- what it is (option 1A)
s=title(add('Blank-with-Title'),'Launch Studio')
headline(s,'From business prototypes to supported products, under the approvals we already have.')
NY,NH=2.05,1.55
N=[('Ideas from the business',['AI Builders Guild','Prototypes in the sandbox'],STEEL_MID,NAVY,SLATE,0.73,2.45),
   ('Onboarding review',['Business endorsement and payback','Can it become a product?'],GREEN,WHITE,WHITE,3.55,2.20),
   ('Launch Studio',['Build to standard','Host, secure, support','Retire at end of life'],NAVY,WHITE,SOFT,6.12,2.90),
   ('Supported product',['Measured value','Business-funded'],PALE,GREEN,INK,9.39,3.20)]
for i,(h,lines,fill,hc,bc,x,w) in enumerate(N):
    b=box(s,x,NY,w,NH,fill,line=(GREEN if fill==PALE else None),adj=0.08)
    label_in(b,[(h,14,True,hc)]+[(l,10.5,False,bc) for l in lines])
    if i<3:
        nx=N[i+1][5]; conn(s,x+w,NY+NH/2,nx-0.07,NY+NH/2,GREY,1.75,arrowhead=True)
elbow_back(s,3.55+1.10,NY+NH,0.73+1.22,NY+NH+0.07,NY+NH+0.42,SLATE,1.25,True)
txt(s,1.95,NY+NH+0.44,2.6,0.22,[('fold in, defer, or return to the sandbox',8.5,True,SLATE)])
r1=box(s,0.73,4.42,11.86,0.58,STEEL_LIGHT,adj=0.12)
tf=r1.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_left=In(0.25)
p=run(tf,'Existing approvals stay in place',11,True,NAVY,space_after=0,first=True)
r=p.add_run(); r.text='    AI Council and intake   |   Security and WAB   |   Finance   |   Business sponsor'; r.font.size=Pt(11); r.font.color.rgb=INK; r.font.name=F
PR=[('The builder sees a studio','IT carries the governance'),('If IT touches it, IT owns it','No halfway tier'),('Choose the build route','Reuse, extend, buy, harden or rebuild'),('Count money, not activity','A value contract before build')]
PW4=(11.86-3*0.18)/4
for i,(h,b_) in enumerate(PR):
    c=box(s,0.73+i*(PW4+0.18),5.15,PW4,0.78,PALE,adj=0.10)
    tf=c.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_left=In(0.16); tf.margin_right=In(0.10)
    run(tf,h,11,True,NAVY,space_after=1,first=True); run(tf,b_,9.5,False,INK,space_after=0)
source(s,'Working name. Early concept; the model is expected to change as the pilot runs.',y=6.08)
notes(s,'The problem in one line: people across the business can now build working prototypes in days with AI-assisted building, and almost none become tools the business can rely on. A good prototype today either stays personal, drifts into use on real data with nobody owning it, or dies. '
      'Read the path left to right. The AI Builders Guild, Mike Wassil\'s community, brings ideas forward from the sandbox. Launch Studio fronts an onboarding review that vets each idea on two questions, does it come with its business\'s endorsement and a payback, and can it become a product, using a one-page intake, a value score reviewed with Finance, an overlap check, a risk tier check and a sized estimate. What passes, Launch Studio builds to standard, hosts, secures, supports and eventually retires. What does not pass is folded into an existing product, deferred, or returned to the sandbox, always with the reason. '
      'The onboarding review is new: it is how Wesco vets tools coming from the broader company. It is Launch Studio people as part of their work (David Blondel as product owner, Mike Wassil for the Guild, an architect from Ron Snyder\'s team, Darryl and Ron at commit), with executive decision-makers such as Sean and Lisa Orton where a call needs them. The approvals are not new: the AI Council, Security, WAB and Finance decide what they decide today; the Studio prepares the evidence once and routes it. '
      'Four principles. The builder sees a studio and IT carries the governance, which is why compliance goes up and friction goes down. If IT touches it, IT owns it: the business cannot own applications, so there is no halfway tier. The build route is chosen, not assumed; a rewrite is one option, and every route passes the same release tests. And every product signs a value contract before build, with the number it should move, a baseline, a proof method and a stop rule; value is reported in separate lines and never summed.')

# 3 ---------------------------------------------------------------- next steps (option 2A)
s=title(add('Blank-with-Title'),'Next steps')
headline(s,'A pilot on the current team. Four things to settle with you.')
LW=6.55; RX=0.73+LW+0.30; RW=12.59-RX
eyebrow(s,0.73,1.98,3,'Pilot')
Q=[('Q4 2026','Agree the path; first candidates graded',STEEL_MID),('Q1 2027','Two or three tools built; first measured results',STEEL_MID),('2027','Open to EES, UBS and functions if the gates hold',STEEL_LIGHT)]
QW=(LW-2*0.15)/3
for i,(q,b_,f) in enumerate(Q):
    c=box(s,0.73+i*(QW+0.15),2.22,QW,0.95,f,adj=0.10)
    tf=c.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_left=In(0.14); tf.margin_right=In(0.10)
    run(tf,q,12,True,NAVY,space_after=1,first=True); run(tf,b_,9.5,False,INK,space_after=0)
eyebrow(s,0.73,3.38,3,'Funding shape')
c=box(s,0.73,3.62,LW,1.05,PALE,adj=0.08)
tf=c.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_left=In(0.18); tf.margin_right=In(0.14)
run(tf,'IT funds the standing team. Each product is a business-funded project that reimburses IT for productization, then for upkeep, through the chargeback that exists.',10.5,False,INK,space_after=2,first=True)
run(tf,'The business picks from a menu: sandbox, pilot, sponsored product, shared product. Mechanism is a decision for later, with Finance.',10.5,False,INK,space_after=0)
eyebrow(s,0.73,4.88,3,'Capacity')
c=box(s,0.73,5.12,LW,0.78,STEEL_LIGHT,adj=0.08)
tf=c.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_left=In(0.18); tf.margin_right=In(0.14)
run(tf,'Launch Studio decides what it takes into build, against a work-in-progress limit Ron sets. The current team to start.',10.5,False,INK,space_after=0,first=True)
d=box(s,RX,1.98,RW,3.92,NAVY,adj=0.05)
txt(s,RX+0.25,2.12,RW-0.5,0.3,[('FROM YOU',9.5,True,GREENT)])
D=['Your read on the direction','Where the standing team\'s funding sits','How to position this with Akash','Whether this needs an FY27 AOP line']
for i,dd in enumerate(D):
    rw_=box(s,RX+0.25,2.52+i*0.82,RW-0.5,0.66,C(0x2A,0x33,0x40),adj=0.12)
    tf=rw_.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_left=In(0.2)
    p=run(tf,f'{i+1}   ',13,True,GREENT,space_after=0,first=True)
    r=p.add_run(); r.text=dd; r.font.size=Pt(13); r.font.color.rgb=WHITE; r.font.name=F
takeaway(s,'Thirty minutes. Mike Wassil and I are aligned; this is a joint initiative.',y=6.05,h=0.45)
notes(s,'The pilot runs in CSS first, two or three tools chosen from the Guild\'s funnel for measurable value and allowed data paths. Each quarter ends with evidence, not a date. '
      'Funding: the shape is agreed between Mike, Ron and me; the mechanism is a future decision with Finance. One rule holds regardless: no sponsor, no production. '
      'Capacity: this is the line that keeps the Studio from becoming a queue. The business decides what it funds, the approval bodies decide what is allowed, and we decide what the team commits to. '
      'Decision 2 decides where reimbursements flow and is the line Akash will read first. Decision 4: the pilot can start on the current team and the approvals that exist; what it needs beyond that depends on where the standing team sits and whether the October 6 capacity changes make Launch Studio the right home for people who would otherwise be unassigned. If either points to an AOP line, better to raise it now than after the pilot.')

# 4 ---------------------------------------------------------------- divider
s=add('Section Divider_Dark')
for ph in s.placeholders:
    if ph.placeholder_format.idx==12: ph.text_frame.paragraphs[0].add_run().text='Backup'
    elif ph.placeholder_format.idx==14: ph.text_frame.paragraphs[0].add_run().text='Detail behind the two slides'

# B1 ---------------------------------------------------------------- who does what
s=title(add('Blank-with-Title'),'Who does what')
headline(s,'Three lanes. The onboarding review is new; the approvals are not.')
D=[['Lane','Who','What they do'],
   ['Find and prove','Mike Wassil and the AI Builders Guild','Surface problems, coach safe prototypes in the sandbox, gather user proof, bring ideas forward'],
   ['Grade, build and run','Launch Studio: Darryl Benson and Ron Snyder (leads), David Blondel (product owner), Ron\'s engineering team','Run the onboarding review; build to standard; host, secure, support and retire'],
   ['Onboarding review (new)','Launch Studio people as part of their work; executive decision-makers such as Sean McCloskey and Lisa Orton where needed','Vet submissions that come with their business\'s endorsement and a payback; one of four answers with the reason'],
   ['Approve','AI Council and intake, Security and WAB, Finance, the business sponsor','Approve, fund and validate as today; review depth matched to risk'],
   ['Capacity','Launch Studio leads, against a limit Ron sets','Decide what is taken into build; the business decides what it funds']]
table(s,0.73,1.95,11.86,3.72,D,col_w=[2.2,4.2,5.46],size=10.5,head_size=11,row_h=0.62)
takeaway(s,'The onboarding review vets; the approval bodies approve; the business funds; we decide what the team commits to.',y=5.85,h=0.5)
notes(s,'Roles as agreed with Mike and Ron. Mike is the conduit to the builder community, which Wesco leadership materials call the AI Builders Guild. Onboarding review row added 2026-10-14 (Darryl): a new body that vets submissions with business endorsement and payback; whether the executives are standing members or called in per decision is still open. Capacity row so that intake into build has a named decision and an owner.')

# B2 ---------------------------------------------------------------- on-ramp
s=title(add('Blank-with-Title'),'The on-ramp')
headline(s,'One onboarding review, two questions, four answers.')
D=[['Question','What we grade','Tools'],
   ['Does it come with endorsement and a payback?','Business value: the number it should move, the baseline, the mechanism, who sponsors it and who uses it','One-page intake; value score reviewed with Finance; overlap check against tools we already run'],
   ['Can it become a product?','Prototype viability: data it touches, systems it connects to, build route, cost to run','Risk tier check; short engineering review of the prototype; sized estimate for build and upkeep']]
table(s,0.73,1.95,11.86,2.3,D,col_w=[2.3,4.9,4.66],size=11,head_size=11,row_h=0.7)
OUTS=['Take it in','Fold into an existing product','Defer','Return to the sandbox']
OW=(11.86-3*0.15)/4
txt(s,0.73,4.48,11.86,0.25,[('Every submission gets one of four answers, with the reason. Target: 30 days.',10.5,True,SLATE)])
for i,o in enumerate(OUTS):
    c=box(s,0.73+i*(OW+0.15),4.80,OW,0.55,NAVY if i==0 else STEEL_LIGHT,adj=0.15)
    label_in(c,[(o,11.5,True,WHITE if i==0 else NAVY)])
takeaway(s,'The grade is what the sponsor signs up to: the value score becomes the value contract, the sized estimate becomes the reimbursement project.',y=5.6,h=0.5)
notes(s,'Launch Studio fronts the on-ramp so engineering time is only spent on ideas that have earned it. The onboarding review is the body that does this; its tools are light by design: a short intake, a rubric, a tier check and a sized estimate.')

# B3 ---------------------------------------------------------------- funding menu
s=title(add('Blank-with-Title'),'Funding menu')
headline(s,'IT funds the team. The business funds each product and picks how.')
D=[['Option','The business commits','IT carries','When it fits'],
   ['Sandbox','Nothing; prototype stays on non-production data','Registration and visibility','Personal or team tools, no business reliance'],
   ['Pilot','A bounded project with a 90-day decision','Build to pilot standard, measurement','Value unproven, worth a cheap test'],
   ['Sponsored product','Reimbursement for productization, then annual upkeep','Full ownership, end to end','A production tool for one business'],
   ['Shared product','Co-funded by the segments that use it','Full ownership plus reuse across segments','Cross-segment tools']]
table(s,0.73,1.95,11.86,3.3,D,col_w=[2.0,3.6,3.1,3.16],size=11,head_size=11,row_h=0.62)
takeaway(s,'No sponsor, no production. The reimbursement mechanism is a decision for later, with Finance.',y=5.55,h=0.5)
notes(s,'The shape: IT funds the standing team; each product is a business-funded project that reimburses IT for productization and then upkeep, through the existing chargeback. The menu exists so the business decision is easy to make. Which form applies to a given product, and the accounting behind it, is settled with Finance.')

# B4 ---------------------------------------------------------------- builder experience (option B, reused)
s=title(add('Blank-with-Title'),'The builder')
headline(s,'You bring the idea. We handle the rest.')
top=box(s,0.73,1.95,11.86,2.32,PALE,adj=0.05)
eyebrow(s,0.95,2.03,6,'What the builder sees')
TW3=(11.86-0.44-2*0.20)/3
for i,(h,b_) in enumerate([('1   Submit','Share the prototype and a one-page summary with your sponsor'),('2   Hear back within 30 days','A clear answer and the reason for it'),('3   See it launched','Credited as originator and first champion with colleagues')]):
    c=box(s,0.95+i*(TW3+0.20),2.32,TW3,0.88,GREEN,adj=0.10)
    tf=c.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_left=In(0.18); tf.margin_right=In(0.14)
    run(tf,h,13,True,WHITE,space_after=2,first=True); run(tf,b_,11,False,WHITE,space_after=0)
txt(s,0.95,3.30,6,0.25,[('Involved with the team at every stage',10.5,True,NAVY)])
CH=['15-minute demo','Architect walkthrough','Sprint demos','Acceptance testing','Launch champion','Next feature as a prototype']
PW=(11.86-0.44-5*0.12)/6
for i,c_ in enumerate(CH):
    b=box(s,0.95+i*(PW+0.12),3.60,PW,0.50,WHITE,line=GREEN,lw=1.25,adj=0.5)
    label_in(b,[(c_,10.5,True,NAVY)])
conn(s,0.73,4.42,12.59,4.42,SLATE,1.5,dash=True)
txt(s,10.0,4.18,2.59,0.22,[('Line of visibility',9.5,True,SLATE)],align=PP_ALIGN.RIGHT)
bot=box(s,0.73,4.55,11.86,1.25,STEEL_MID,adj=0.06)
eyebrow(s,0.95,4.63,8,'Launch Studio carries it for them',color=NAVY)
BW5=(11.86-0.44-4*0.15)/5
for i,c_ in enumerate(['Grade and assess','AI Council and security review','Identity, hosting and architecture review','Rebuild, release and support','Lifecycle and retirement']):
    b=box(s,0.95+i*(BW5+0.15),4.92,BW5,0.70,NAVY,adj=0.10)
    label_in(b,[(c_,11,True,WHITE)])
takeaway(s,'If IT absorbs it, compliance goes up and friction goes down.',y=5.95,h=0.47)
notes(s,'The builder never fills in a governance form and never touches production code. The originator advises and accepts; the product owner decides the backlog. The sponsor commits funding and the originator\'s time for demos and acceptance. If the originator moves on, the product continues under IT and the sponsor.')

# B5 ---------------------------------------------------------------- pilot plan
s=title(add('Blank-with-Title'),'Pilot plan')
headline(s,'Each quarter ends with evidence, not a date.')
D=[['Quarter','Goal','Exit evidence'],
   ['Q4 2026','Agree the path. Inventory the Guild\'s ideas, grade the first candidates, set the value rules and the capacity limit','Signed charter; candidate baselines; funding and capacity decisions'],
   ['Q1 2027','Run a first cohort. Two or three tools through the filter and into build; sponsors lead adoption','Authorized pilots; first measured results or stop decisions'],
   ['Q2 2027','Prove it repeats. Compare outcomes, reuse parts, fix handoffs','Process applied twice; value reconciled with Finance'],
   ['Q3 2027 onward','Open the path to EES, UBS and functions through their sponsors, if the gates hold','Owners and support agreed for new teams; no bypass of the filter']]
table(s,0.73,1.95,11.86,3.3,D,col_w=[1.8,5.6,4.46],size=10.5,head_size=11,row_h=0.62)
source(s,'Candidate tools are chosen from the Guild funnel after grading; none is named here until it has been through the filter.',y=5.5)
notes(s,'Dates are proposed. Evidence, not the calendar, moves the plan. Mike\'s research package lists candidate areas; they are placeholders until graded and are deliberately not shown to Sean.')

# B6 ---------------------------------------------------------------- evidence base
s=title(add('Blank-with-Title'),'Evidence base')
headline(s,'What the research found, labeled by how much weight it carries.')
D=[['Finding','Basis','Weight'],
   ['AI use is near universal; measured profit impact is rare, and the firms that show it redesign work and measure it','Large surveys by major consulting firms, 2025 to 2026','External finding, self-reported'],
   ['AI makes building fast; review and proof are now the slow steps','Industry surveys of software leaders, 2025 to 2026','External finding'],
   ['Unreviewed AI-generated code fails security tests in known, testable ways','Security vendor testing, 2025 to 2026','Company-reported'],
   ['Programs that filter early and assign owners scale; programs that count participation produce few lasting tools','Published cases from industrial suppliers and technology firms','Company-reported'],
   ['Most vibe-coded applications will be retired for failing to deliver predictable value','Analyst forecast, read via a secondary summary','Forecast; original not yet licensed']]
table(s,0.73,1.95,11.86,3.5,D,col_w=[6.0,3.6,2.26],size=10.5,head_size=11,row_h=0.6)
source(s,'Full sources, dates and limits are in Mike Wassil\'s Launch Studio research report, October 12, 2026. No statistic is quoted here that has not been traced to its original.',y=5.7)
notes(s,'Keep this slide qualitative. The point for Sean is that the model rests on evidence and that we know which evidence is strong. The research report carries the figures with their sources and caveats; quote from it, not from memory.')

# end
s=add('End Slide_Logo_Dark')
for ph in s.placeholders:
    if ph.placeholder_format.idx==13:
        tf=ph.text_frame
        run(tf,'Darryl Benson',14,True,WHITE,first=True)
        run(tf,'Senior Director, CSS Platforms',11,False,SOFT)
        run(tf,'with Mike Wassil, Digital Products',11,False,SOFT)

for sl in prs.slides: drop_empty(sl)
OUT_='2026-10-14_Launch_Studio_Executive_Overview_Deck.pptx'
prs.save(OUT_)
print('slides',len(prs.slides._sldIdLst))
