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

def bracket(s,x1,x2,y,tick=0.13,color=SLATE,lw=1.25):
    ff=s.shapes.build_freeform(In(x1),In(y+tick),scale=1.0)
    ff.add_line_segments([(In(x1),In(y)),(In(x2),In(y)),(In(x2),In(y+tick))],close=False)
    sh=ff.convert_to_shape(); sh.fill.background(); sh.line.color.rgb=color; sh.line.width=Pt(lw); sh.shadow.inherit=False
    return sh
def source(s,text,y=6.12):
    tf=tb(s,0.73,y,11.86,0.3); run(tf,text,8.5,False,GREY,first=True,italic=True)

# 1 ---------------------------------------------------------------- title
s=add('Title Slide')
for ph in s.placeholders:
    i=ph.placeholder_format.idx
    if i==12: ph.text_frame.paragraphs[0].add_run().text='Launch Studio'
    elif i==1: ph.text_frame.paragraphs[0].add_run().text='October 12, 2026'
notes(s,'Discussion with Mike Wassil and Ron Snyder. Goal: agree how ideas reach us from Mike, how we choose which ones to build, and get Mike\'s reaction to a funded service model. The model is a position to test, not a decision; it still needs our team\'s review and Sean\'s approval. Launch Studio is a working name; part of the point of this meeting is Mike\'s read on whether it lands with the vibe coders.')

# 2 ---------------------------------------------------------------- challenge
s=title(add('Blank-with-Title'),'The challenge')
headline(s,'Prototypes are now easy to build. Few become software the business can rely on.')
STATS=[('60%','of vibe-coded applications expected to be retired by 2028 because they fail to deliver predictable business value','Gartner'),
       ('30%','of software engineering teams expected to be materially strained maintaining applications built by citizen developers','Gartner'),
       ('0 of 5,600','vibe-coded applications in production found with basic protections in place','Cloud Security Alliance')]
CW=(11.86-2*0.30)/3
for i,(v,l,src) in enumerate(STATS):
    x=0.73+i*(CW+0.30)
    b=box(s,x,2.05,CW,3.05,STEEL_LIGHT,adj=0.05)
    tf=b.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.TOP
    tf.margin_left=In(0.28); tf.margin_right=In(0.28); tf.margin_top=In(0.30); tf.margin_bottom=In(0.2)
    run(tf,v,44,True,NAVY if i<2 else MBLUE,space_after=8,first=True)
    run(tf,l,13,False,INK,space_after=10)
    run(tf,src.upper(),9,True,GREEN,space_after=0)
takeaway(s,'The gap is not ideas. It is the step from prototype to a supported product.',y=5.35)
source(s,'Gartner, "Govern Vibe Coding for Citizen Developers With Self-Service Platforms," June 29, 2026. Cloud Security Alliance, "The Vibe Coding Governance Gap," June 2, 2026 (basic protections: CSRF protection, security headers, scoped access).')
notes(s,'Three external data points. Gartner: by 2028, 60 percent of vibe-coded applications will be retired because they fail to deliver predictable business value, and 30 percent of software engineering teams will face material capacity strain maintaining what citizen developers built. Cloud Security Alliance: a scan of 5,600 vibe-coded applications in production found none with CSRF protection, security headers or properly scoped access policies. The point for this room: the risk is not too few ideas. It is ideas that reach production with nobody owning security, support and lifecycle, and the cost landing on engineering anyway. '
      'Source caution: the Gartner figures were read through a published summary of the report. Confirm against the Gartner original before this slide goes beyond this meeting.')

# 3 ---------------------------------------------------------------- gap
s=title(add('Blank-with-Title'),'The gap')
headline(s,'The business can now prototype its own solutions. Launching and sustaining them is IT\'s job.')
SIDE_W=3.55; Y0=2.10; H=2.25
lb=box(s,0.73,Y0,SIDE_W,H,NAVY,adj=0.06)
label_in(lb,[('The business (CSS)',18,True,WHITE),('Knows the problem',13.5,False,SOFT),('Builds the prototype',13.5,False,SOFT)])
rb=box(s,12.59-SIDE_W,Y0,SIDE_W,H,NAVY,adj=0.06)
label_in(rb,[('IT (CSS Platforms)',18,True,WHITE),('Launches to production grade',13.5,False,SOFT),('Secures, hosts, runs and supports',13.5,False,SOFT)])
GX1=0.73+SIDE_W+0.22; GX2=12.59-SIDE_W-0.22
ar=s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,In(GX1),In(Y0+0.55),In(GX2-GX1),In(0.95))
ar.fill.solid(); ar.fill.fore_color.rgb=GREEN; ar.line.fill.background(); ar.shadow.inherit=False; ar.adjustments[0]=0.62; ar.adjustments[1]=0.42
label_in(ar,[('Productization',15,True,WHITE)])
txt(s,GX1,Y0+1.62,GX2-GX1,0.5,[('Today there is no owned path between the two',11,True,SLATE)],align=PP_ALIGN.CENTER)
q=box(s,0.73,4.62,11.86,1.30,PALE,adj=0.08)
tf=q.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE
tf.margin_left=In(0.30); tf.margin_right=In(0.30)
run(tf,'THE JOB TO BE DONE',9,True,GREEN,space_after=4,first=True)
run(tf,'When a business team has built a prototype that solves a real problem, it wants that solution running reliably, securely and supported for its segment, so it gets the business result without building a software organization.',13,False,INK,space_after=0,italic=True)
notes(s,'The business, here CSS, knows its problems and can now prototype them with AI tools. What it cannot do, and should not have to do, is take a prototype to production: security review, identity, hosting, release, support and lifecycle. That is IT\'s job and it is what CSS Platforms already does for entroCIM. The job-to-be-done statement is the test for every idea: if the sponsor does not want the outcome running and supported, it is not a productization candidate.')

# 4 ---------------------------------------------------------------- how it works
s=title(add('Blank-with-Title'),'How it works')
headline(s,'Mike brings concepts forward. We select, build and run them.')
NW=2.05; NY=2.62; NH=1.10
gap=(11.86-5*NW)/4
NX=[0.73+i*(NW+gap) for i in range(5)]
NODES=[('Vibe coders','The business prototypes its own problems'),
       ('Mike Wassil','Conduit to the vibe coders; brings concepts forward'),
       ('Select','An idea qualifies when the business funds build and run'),
       ('Build','David Blondel, product owner; Ron Snyder\'s team rebuilds to standard'),
       ('Run','Ron Snyder\'s team hosts, operates and supports')]
for i,(n,cap_) in enumerate(NODES):
    ours=i>=2
    b=box(s,NX[i],NY,NW,NH,NAVY if ours else STEEL_MID,adj=0.10)
    label_in(b,[(n,14,True,WHITE if ours else NAVY)])
    txt(s,NX[i],NY+NH+0.15,NW,1.2,[(cap_,12,False,INK)],align=PP_ALIGN.CENTER)
for i in range(4):
    conn(s,NX[i]+NW,NY+NH/2,NX[i+1]-0.07,NY+NH/2,GREY,1.5,arrowhead=True)
bracket(s,NX[2],NX[4]+NW,2.38,tick=0.16)
txt(s,NX[2],2.02,NX[4]+NW-NX[2],0.3,[('Joint team: Darryl Benson and Ron Snyder',11,True,SLATE)],align=PP_ALIGN.CENTER)
takeaway(s,'CSS Platforms carries each selected idea from concept to a supported product, starting with the team we have.',y=5.35)
notes(s,'Roles. Mike Wassil is the conduit to the vibe-coding community and idea funnel; nothing changes in his remit. Darryl Benson and Ron Snyder lead as a joint team and own selection, delivery and accountability for results. David Blondel is product owner: scope, requirements and business value. Ron Snyder\'s team builds, secures, hosts and runs the product. '
      'What Ron brings: an early proof point where AI-assisted development cut the estimated effort on an internal search build from 80 hours to 10 (an estimate, not yet measured); engineering standards already in place for containerized hosting, release and code quality; and direct experience taking an AI capability through the AI Council approval path.')

# 5 ---------------------------------------------------------------- working model
s=title(add('Blank-with-Title'),'Working model')
headline(s,'Launch Studio selects by funding, builds from the prototype and owns what it runs.')
band=box(s,0.73,2.02,11.86,0.72,GREEN,adj=0.12)
tf=band.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_left=In(0.25)
p=run(tf,'Launch Studio',15,True,WHITE,space_after=0,first=True)
r=p.add_run(); r.text='   A small number of ideas at a time, each carried from prototype to supported product'; r.font.size=Pt(12); r.font.color.rgb=WHITE; r.font.name=F
CW=(11.86-2*0.30)/3
PILLARS=[('Select','Funding is the filter','An idea qualifies when the sponsoring business commits to fund the build and the ongoing run cost.'),
         ('Build','The prototype is the spec','The prototype proves demand and defines the requirements. IT rebuilds it to engineering standards.'),
         ('Run','IT owns the product','If IT touches it, IT owns it. Funded by a build charge and an annual run charge through the existing IT chargeback.')]
for i,(k,h,b_) in enumerate(PILLARS):
    x=0.73+i*(CW+0.30)
    c=box(s,x,2.90,CW,2.10,NAVY,adj=0.06)
    tf=c.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.TOP
    tf.margin_left=In(0.22); tf.margin_right=In(0.22); tf.margin_top=In(0.18)
    run(tf,k.upper(),9.5,True,GREENT,space_after=4,first=True)
    run(tf,h,15,True,WHITE,space_after=6)
    run(tf,b_,13,False,SOFT,space_after=0)
st=box(s,0.73,5.18,11.86,0.55,STEEL_LIGHT,adj=0.12)
tf=st.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_left=In(0.25)
p=run(tf,'Going forward',11,True,NAVY,space_after=0,first=True)
r=p.add_run(); r.text='   A starting template and hosting standard for vibe coders, so new prototypes are easier to productize'; r.font.size=Pt(11); r.font.color.rgb=INK; r.font.name=F
source(s,'Discussion position. Pending review with our team and Sean McCloskey\'s approval.',y=5.92)
notes(s,'This is the model to test with Mike, not to commit to. The product studio is the umbrella: we take on a few ideas at a time. Funding is the filter, which keeps selection objective and makes the business commitment visible; "hard to say no to" becomes "easy to say yes to, on terms." The prototype is treated as proof of demand and as the requirements; Ron\'s team rebuilds it to standard so generated code does not go to production as is. That is our answer to the security finding on the previous slides. The product is then owned by IT, funded by the business through the chargeback. '
      'Listen for Mike\'s reaction to funding as the filter. Do not introduce the template and hosting standard as a requirement on the vibe coders; ask whether it would help them (question 9).')

# 6 ---------------------------------------------------------------- prototype to product
s=title(add('Blank-with-Title'),'Prototype to product')
headline(s,'If IT touches it, IT owns it. One gate separates a business prototype from an IT-owned product.')
ZY=2.00; ZH=2.70; ZW=3.40; GX=4.58; GW=4.17; RX=12.59-ZW
def zone(x,fill,ec,hc,bc,eyebrow_,head,lines):
    z=box(s,x,ZY,ZW,ZH,fill,adj=0.05)
    tf=z.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.TOP
    tf.margin_left=In(0.24); tf.margin_right=In(0.20); tf.margin_top=In(0.20)
    run(tf,eyebrow_,9.5,True,ec,space_after=4,first=True)
    run(tf,head,17,True,hc,space_after=10)
    for l in lines: run(tf,l,12.5,False,bc,space_after=6)
zone(0.73,STEEL_MID,GREEN,NAVY,INK,'PROTOTYPE','Owned by the business',['Built in a sandbox','No production data','Registered, so it is visible'])
zone(RX,NAVY,GREENT,WHITE,SOFT,'PRODUCT','Owned by IT',['Rebuilt to engineering standards','Hosted, secured and supported','Retired at end of life'])
g=box(s,GX,ZY,GW,ZH,GREEN,adj=0.05)
tf=g.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.TOP
tf.margin_left=In(0.24); tf.margin_right=In(0.22); tf.margin_top=In(0.20)
run(tf,'THE GATE',9.5,True,WHITE,space_after=4,first=True)
run(tf,'Assess and select',17,True,WHITE,space_after=10)
for k,v in [('Screen','sponsor, problem, overlap, data'),('Assess','IT reviews the prototype and estimates build and run'),('Commit','funding, success measure, review date')]:
    p=run(tf,k+': ',12.5,True,WHITE,space_after=6)
    r=p.add_run(); r.text=v; r.font.size=Pt(12.5); r.font.color.rgb=WHITE; r.font.name=F
conn(s,0.73+ZW,ZY+ZH/2,GX-0.07,ZY+ZH/2,GREY,1.75,arrowhead=True)
conn(s,GX+GW,ZY+ZH/2,RX-0.07,ZY+ZH/2,GREY,1.75,arrowhead=True)
OY=4.92
txt(s,0.73,OY,1.55,0.5,[('Gate outcomes',11,True,SLATE)],anchor=MSO_ANCHOR.MIDDLE)
OUTS=['Accept','Fold into an existing product','Defer','Return to the sandbox']
OX0=2.35; OW=(12.59-OX0-3*0.15)/4
for i,o in enumerate(OUTS):
    c=box(s,OX0+i*(OW+0.15),OY,OW,0.50,NAVY if i==0 else STEEL_LIGHT,adj=0.15)
    label_in(c,[(o,11.5,True,WHITE if i==0 else NAVY)])
takeaway(s,'Funding for every product: a build charge plus an annual run charge, through the existing IT chargeback.',y=5.60,h=0.50)
source(s,'Working model for discussion. Charges to be set with Finance.',y=6.18)
notes(s,'The principle: the business cannot own applications. If IT touches an application, IT owns it. So there are two zones and one gate. On the left, the business owns its prototypes: built in a sandbox, no production data, registered so we and Mike can see what exists. On the right, IT owns the product end to end: rebuilt to standard, hosted, secured, supported, and retired when it stops earning its keep. '
      'The gate has three steps. Screen is light and quick (Mike and David): is there a named sponsor, a clear problem, does it overlap something we already have, and what data does it touch. Assess is a short IT review of the prototype (David and an architect from Ron\'s team) that produces the ownership estimate: build cost and annual run cost. Reviewing a prototype is not touching it. Commit is where the sponsor signs the funding through the chargeback, agrees how success is measured, and accepts a review date. Darryl and Ron decide at Commit. '
      'Four outcomes, each with a reason given back to the submitter: accept; fold into an existing product (the idea becomes a feature of something we already run); defer (good idea, no funding or no capacity yet); return to the sandbox. '
      'Prototypes already in use go through the same gate. Anything not accepted comes off production data. '
      'Sean has asked for AI benefits to be measured (rework, defects, cycle time), not described. The success measure agreed at Commit is how we do that for every product.')

# 6b ---------------------------------------------------------------- the vibe coder (option B)
s=title(add('Blank-with-Title'),'The vibe coder')
headline(s,'You bring the idea. We handle the rest.')
top=box(s,0.73,1.95,11.86,2.32,PALE,adj=0.05)
eyebrow(s,0.95,2.03,6,'What the vibe coder sees')
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
for i,c_ in enumerate(['Screen and assess','AI Council and security review','Identity, hosting and architecture review','Rebuild, release and support','Lifecycle and retirement']):
    b=box(s,0.95+i*(BW5+0.15),4.92,BW5,0.70,NAVY,adj=0.10)
    label_in(b,[(c_,11,True,WHITE)])
takeaway(s,'If IT absorbs it, compliance goes up and friction goes down.',y=5.95,h=0.47)
notes(s,'The vibe coder sees three touchpoints: submit, hear back within 30 days with a reason, see it launched with their name on it. Along the way they stay involved with the team: a short demo at screening, walking our architect through the prototype, sprint demos, acceptance testing, championing the launch, and prototyping the next feature in their sandbox. '
      'Below the line, Launch Studio carries everything else: screening and assessment, AI Council and security review, identity, hosting and architecture review, the rebuild, release and support, and lifecycle through retirement. The vibe coder never fills in a governance form and never touches production code. '
      'Two boundaries keep this working. The originator advises and accepts; David, as product owner, decides the backlog. And the sponsor commits two things at the gate: the funding, and the originator\'s time for demos and acceptance. If the originator moves on, the product continues under IT and the sponsor. '
      'Ask Mike whether this, and the Launch Studio name, would land with his community.')

# 7 ---------------------------------------------------------------- questions
s=title(add('Blank-with-Title'),'Questions')
headline(s,'What we need from Mike to shape intake and selection.')
QS=[('The funnel',['What is in the funnel today, and from which parts of the business?','How many prototypes are already in use or touching production data?','What should a submission include, and how often?']),
    ('Selection and funding',['Which criteria choose two or three: value, reuse, data, security, support load?','Has any sponsor offered to fund the build or the run cost?','What happens today to a good idea that nobody owns?']),
    ('Governance',['What review does an idea already pass before it reaches us?','How do we close the loop on ideas we do not select?']),
    ('The vibe coders',['Would a starting template and hosting standard help them?','Would "Launch Studio" land with them?','Can sponsors release their time for demos and acceptance?'])]
CW4=(11.86-3*0.22)/4
n=1
for i,(h,qs) in enumerate(QS):
    x=0.73+i*(CW4+0.22)
    c=box(s,x,1.98,CW4,4.10,STEEL_LIGHT,adj=0.04)
    tf=c.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.TOP
    tf.margin_left=In(0.20); tf.margin_right=In(0.18); tf.margin_top=In(0.20)
    run(tf,h,15,True,NAVY,space_after=12,first=True)
    for q_ in qs:
        p=run(tf,f'{n}   ',13,True,GREEN,space_after=14)
        r=p.add_run(); r.text=q_; r.font.size=Pt(13); r.font.color.rgb=INK; r.font.name=F
        n+=1
notes(s,'Questions 2, 5 and 6 matter most. Question 2 tells us whether we are catching ideas early or cleaning up after them. Question 5 is the first test of funding as the filter. Question 6 is the demand signal: good ideas with no owner are exactly what this service exists for. '
      'Questions 10 to 12 test the vibe coder experience with the person who knows the community best. Governance (question 7): the paths we know of are AI Council review, security review, identity and hosting. We want to know which of these an idea has already cleared before it reaches us.')

# 8 ---------------------------------------------------------------- outcomes
s=title(add('Blank-with-Title'),'Outcomes')
headline(s,'What we want to leave this meeting with.')
OUT=['Agreement on how ideas move from Mike to us',
     'Two or three selection criteria we all accept, and Mike\'s reaction to funding as the filter',
     'A first look at candidate ideas, or a date when we will get one',
     'Mike\'s read on the vibe coder\'s role and the Launch Studio name',
     'Agreement on whether to take a joint view to Sean the week of October 19']
for i,o in enumerate(OUT):
    y=2.05+i*0.86
    num=s.shapes.add_shape(MSO_SHAPE.OVAL,In(0.73),In(y),In(0.62),In(0.62))
    num.fill.solid(); num.fill.fore_color.rgb=GREEN; num.line.fill.background(); num.shadow.inherit=False
    label_in(num,[(str(i+1),16,True,WHITE)],margin=0)
    row=box(s,1.55,y,11.04,0.62,STEEL_LIGHT,adj=0.12)
    tf=row.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_left=In(0.25)
    run(tf,o,14,False,INK,space_after=0,first=True)
notes(s,'Sean is on PTO the week of October 12, so the earliest joint view to him is the week of October 19. Keep the prototype-to-product gate and funding filter as positions Mike reacts to; the decision sits with Sean.')

# 8b ---------------------------------------------------------------- backup: roles by stage (option A)
s=title(add('Blank-with-Title'),'Backup: roles by stage')
headline(s,'Who does what at each stage. The first three rows are what the vibe coder sees.')
D=[['','Submit','Screen','Assess','Commit','Build','Launch','Run'],
   ['Vibe coder','Shares the prototype and summary','15-minute demo','Walks the architect through it','','Sprint demos and acceptance','Credited; first champion','Prototypes the next feature'],
   ['Sponsor','Co-signs the summary','','','Funds build and run; releases the originator\'s time','','','Annual review of value'],
   ['Mike (conduit)','Brings the idea forward','Screens with the product owner','','','','',''],
   ['Product owner','','Sponsor, problem, overlap, data','Scopes from the prototype','Darryl and Ron decide; reason given','Owns the backlog and trade-offs','','Turns the next prototype into backlog'],
   ['Engineering and operations','','','Estimates build and run cost','','Rebuilds to standard','Security, identity, hosting, release','Operates, supports, retires']]
t=table(s,0.73,1.95,11.86,3.9,D,col_w=[1.60]+[(11.86-1.60)/7]*7,size=9.5,head_size=10.5,row_h=0.65)
YL=1.95+0.65*4
conn(s,0.73,YL,12.59,YL,GREEN,2.25,dash=True)
source(s,'Dashed line: line of visibility. Below it, Launch Studio carries security, governance, AI Council, architecture review and operations.',y=6.05)
notes(s,'Backup for detailed discussion with Ron\'s team or if Mike asks who does what. Not for presenting to Sean.')

# 9 ---------------------------------------------------------------- end
s=add('End Slide_Logo_Dark')
for ph in s.placeholders:
    if ph.placeholder_format.idx==13:
        tf=ph.text_frame
        run(tf,'Darryl Benson',14,True,WHITE,first=True)
        run(tf,'Senior Director, CSS Platforms',11,False,SOFT)

for sl in prs.slides: drop_empty(sl)
OUT_='2026-10-12_Launch_Studio_Mike_Wassil_Meeting_Deck.pptx'
prs.save(OUT_)
print('slides',len(prs.slides._sldIdLst))
