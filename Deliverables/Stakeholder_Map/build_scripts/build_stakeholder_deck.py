# Stakeholder map deck (private). Run from a folder containing template.pptx (Wesco template).
from pptx import Presentation
from pptx.util import Inches as In, Pt
from pptx.dml.color import RGBColor as C
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE_DASH_STYLE
NAVY=C(0x1D,0x25,0x2D); GREEN=C(0x00,0x95,0x3A); SLATE=C(0x5B,0x7A,0x8E); GREY=C(0x8E,0x92,0x96)
WHITE=C(0xFF,0xFF,0xFF); INK=C(0x2B,0x2B,0x2B); MIST=C(0xDB,0xE3,0xE9); PALE=C(0xE9,0xF3,0xEC)
SUP=C(0xCD,0xEB,0xD6); NEU=C(0xE3,0xE7,0xEA); MIX=C(0xF7,0xD9,0xA8); MIXL=C(0xC7,0x7A,0x12)
AMBERBG=C(0xFD,0xF3,0xE3); MBLUE=C(0x00,0x49,0x86); STEEL=C(0xF4,0xF6,0xF7)
F='Arial'
prs=Presentation('template.pptx')
ids=prs.slides._sldIdLst
for sid in list(ids):
    prs.part.drop_rel(sid.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')); ids.remove(sid)
L={l.name:l for l in prs.slide_layouts}
def slide(t):
    s=prs.slides.add_slide(L['Blank-with-Title']); s.shapes.title.text_frame.paragraphs[0].add_run().text=t; return s
def tb(s,x,y,w,h,text,size,bold=False,color=INK,align=PP_ALIGN.LEFT,italic=False,anchor=MSO_ANCHOR.TOP):
    b=s.shapes.add_textbox(In(x),In(y),In(w),In(h)); tf=b.text_frame; tf.word_wrap=True; tf.vertical_anchor=anchor
    for a in ('margin_left','margin_right','margin_top','margin_bottom'): setattr(tf,a,0)
    lines=text if isinstance(text,list) else [text]
    for i,l in enumerate(lines):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.alignment=align; p.space_after=Pt(3)
        r=p.add_run(); r.text=l; r.font.size=Pt(size); r.font.bold=bold; r.font.color.rgb=color; r.font.name=F; r.font.italic=italic
    return b
def rect(s,x,y,w,h,fill,line=None,dash=False,shape=MSO_SHAPE.RECTANGLE,lw=0.75):
    r=s.shapes.add_shape(shape,In(x),In(y),In(w),In(h)); r.shadow.inherit=False
    if fill is None: r.fill.background()
    else: r.fill.solid(); r.fill.fore_color.rgb=fill
    if line is None: r.line.fill.background()
    else:
        r.line.color.rgb=line; r.line.width=Pt(lw)
        if dash: r.line.dash_style=MSO_LINE_DASH_STYLE.DASH
    return r
def private(s,extra=''):
    tb(s,2.05,6.62,10.55,0.25,'Private working draft. Not for distribution.'+extra,8,color=GREY,italic=True)

STY={'Ally':(GREEN,GREEN,WHITE,False),'Supportive':(SUP,GREEN,INK,False),'Neutral':(NEU,GREY,INK,False),
     'Mixed':(MIX,MIXL,INK,False),'Unknown':(WHITE,SLATE,INK,True)}
def chip(s,x,y,w,name,align,team=False):
    fill,line,txt,dash=STY[align]
    r=rect(s,x,y,w,0.27,fill,NAVY if team else line,dash,MSO_SHAPE.ROUNDED_RECTANGLE,2.25 if team else 0.75)
    r.adjustments[0]=0.25
    tf=r.text_frame; tf.margin_left=In(0.06); tf.margin_right=In(0.06); tf.margin_top=0; tf.margin_bottom=0
    tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    p=tf.paragraphs[0]; p.alignment=PP_ALIGN.CENTER; rr=p.add_run(); rr.text=name
    rr.font.size=Pt(9.5); rr.font.bold=True; rr.font.color.rgb=txt; rr.font.name=F

# ---------- slide 1: influence and alignment grid
s=slide('Influence and Alignment')
cols=['Unknown','Mixed','Neutral','Supportive','Ally']
rows=[('High',1.58),('Medium-High',1.00),('Medium',1.05),('Low-Medium',0.68)]
X0,Y0,CW=2.05,1.40,2.08
people={
 ('High','Unknown'):[('Dirk Naylor',0),('Greg O\'Brien',0)],('High','Mixed'):[('Brad Stevens',0)],
 ('High','Neutral'):[('Akash Khurana (CIO)',0)],
 ('High','Ally'):[('Sean McCloskey',0),('Nathan Kehr',0),('David Blondel',1),('Ron Snyder',1),('Chad Steger',1)],
 ('Medium-High','Neutral'):[('Merwan Mereby',0)],
 ('Medium-High','Ally'):[('Lisa Orton',0),('Chris Gazdic',0),('Bill Muczko',0)],
 ('Medium','Unknown'):[('Emily Munk',0)],('Medium','Mixed'):[('Sunny Sharma (Strev)',0)],
 ('Medium','Neutral'):[('Tom Boss',0),('Amy Aguirre',0)],
 ('Medium','Supportive'):[('Sridhar Loke',0),('Senthil Govindaswamy',0),('DJ Vaughn',0)],
 ('Medium','Ally'):[('Bob Caprise',0),('Akansh Gangil',1)],
 ('Low-Medium','Supportive'):[('Maddy Taylor',0),('Michael Wassil',0)],
}
# zone shading
gap_h=rows[0][1]+rows[1][1]
rect(s,X0,Y0,CW*3,gap_h,AMBERBG)
rect(s,X0+CW*3,Y0,CW*2,gap_h,PALE)
tb(s,X0+CW+0.1,Y0+rows[0][1]+0.25,CW-0.2,0.5,'ACCESS GAP: HIGH INFLUENCE, NOT YET ALIGNED',8,True,MIXL,PP_ALIGN.CENTER)
tb(s,X0+CW*3+0.1,Y0+0.55,CW-0.2,0.5,'LEVERAGE: HIGH INFLUENCE, ALIGNED',8,True,GREEN,PP_ALIGN.CENTER)
# grid lines and headers
y=Y0
for rname,h in rows:
    tb(s,0.95,y,1.0,h,rname,10,True,NAVY,PP_ALIGN.RIGHT,anchor=MSO_ANCHOR.MIDDLE)
    for ci,c in enumerate(cols):
        rect(s,X0+ci*CW,y,CW,h,None,MIST)
        lst=people.get((rname,c),[])
        for k,(n,team) in enumerate(lst):
            chip(s,X0+ci*CW+0.09,y+0.08+k*0.30,CW-0.18,n,c,team)
    y+=h
for ci,c in enumerate(cols):
    tb(s,X0+ci*CW,y+0.06,CW,0.25,c,10,True,NAVY,PP_ALIGN.CENTER)
tb(s,X0,y+0.32,CW*5,0.22,'ALIGNMENT TODAY  →',8.5,True,SLATE,PP_ALIGN.CENTER)
lab=tb(s,0.2,Y0+1.2,1.9,0.3,'INFLUENCE ON OUTCOMES  →',8.5,True,SLATE,PP_ALIGN.CENTER); lab.rotation=-90
lab.left=In(-0.35); lab.top=In(Y0+1.85)
# legend
lx=X0; ly=6.28
chip(s,lx,ly,1.25,"Darryl's team",'Ally',True)
tb(s,lx+1.35,ly+0.04,6.5,0.22,'Navy outline marks Darryl\'s team. Dashed outline means alignment unknown.',8.5,color=GREY)
private(s,' Alignment corrected by Darryl 2026-10-07 for Sean, Lisa, Chris Gazdic, Amy Aguirre, Maddy Taylor, Nathan Kehr, Bill Muczko, Bob Caprise; the rest is Claude\'s reading of the record.')
s.notes_slide.notes_text_frame.text=("Reading the grid: the amber zone is where influence is high and alignment is unknown, mixed or neutral. "
 "Every executive above Sean sits there. The green zone is where depth already exists: Darryl's team, Nate and Bill. "
 "Most supportive relationships sit at Medium influence. Move people as alignment changes; the grid is only as good as its last correction.")

# ---------- slide 2: decision rights by product
s=slide('Decision Rights by Product')
hdr=['Product','Sponsor / decides','Leads','Builds','Delivers','Sells / champions','Open gap']
data=[
 ['entroCIM','Dirk Naylor (sponsor); Sean McCloskey (accountable for all digital products)','David Blondel','Ron Snyder','Chad Steger','Nathan Kehr','Viability question with Sean; Brad Stevens\' integrated platform push'],
 ['CDA','Bill Muczko (sponsor); Sean McCloskey (no FY27 funding)','David Blondel','Ron Snyder, on the entroCIM team','TSS, Greg O\'Brien (not yet engaged)','Nathan Kehr, Bob Caprise, Sridhar Loke','No delivery owner yet; route opened through Emily Munk'],
 ['WAM','Sean McCloskey with Akash Khurana, CIO (takeover)','Akansh Gangil','Merwan Mereby\'s India development team','Senthil Govindaswamy','Amy Aguirre','Development sits outside Darryl\'s organization'],
 ['Navigator','Dirk Naylor (sponsor); Lisa Orton (influence)','Chris Gazdic','Ascent team','DJ Vaughn','CSS Sales','Data center overlap with entroCIM and CDA'],
 ['Vibe coding productization','Sean McCloskey (originated)','Darryl Benson','Open','Open','Business units (fund)','Concept, name and funding model open'],
 ['Aris','Sean McCloskey (receiving)','Prassada (today)','US and India team','Open','Open','Paused pending more information'],
]
W=[1.55,2.25,1.35,1.75,1.75,1.75,2.15]
gf=s.shapes.add_table(len(data)+1,len(hdr),In(0.6),In(1.55),In(sum(W)),In(4.9)); t=gf.table; t.first_row=True
for i,w in enumerate(W): t.columns[i].width=In(w)
for ri,row in enumerate([hdr]+data):
    t.rows[ri].height=In(0.4 if ri==0 else 0.72)
    for ci,val in enumerate(row):
        c=t.cell(ri,ci); c.margin_left=In(0.08); c.margin_right=In(0.08); c.margin_top=In(0.05); c.margin_bottom=In(0.05)
        c.vertical_anchor=MSO_ANCHOR.MIDDLE; c.fill.solid()
        if ri==0: c.fill.fore_color.rgb=NAVY
        elif ci==0: c.fill.fore_color.rgb=MBLUE
        elif ci==len(hdr)-1: c.fill.fore_color.rgb=AMBERBG
        else: c.fill.fore_color.rgb=WHITE if ri%2 else STEEL
        p=c.text_frame.paragraphs[0]; r=p.add_run(); r.text=val; r.font.name=F
        r.font.size=Pt(10 if ri==0 else 9.5); r.font.bold=(ri==0 or ci==0)
        r.font.color.rgb=WHITE if (ri==0 or ci==0) else INK
private(s)
s.notes_slide.notes_text_frame.text=("Read across each row for who holds each lever. The amber column is where the lever is missing or held outside Darryl's organization. "
 "CDA is the clearest case: sponsor and sales are in place, delivery is not. WAM is the structural one: Darryl holds the product but not the builders.")

# ---------- slide 3: where to act
s=slide('Where to Act')
cards=[
 ('Close the gap at the top',["Akash Khurana (CIO): reach through Sean and Lisa Orton, both his direct reports and both allies.","Dirk Naylor: Lisa Orton, the IT to CSS connection, is the established route; the data center briefing gives Sean something to carry.","Greg O'Brien: Emily Munk is the route, CDA delivery is the reason."]),
 ('Convert the neutrals',["Merwan Mereby: reports to Akash; India development and AI report to him, and the WAM takeover depends on him. No relationship yet.","Amy Aguirre: WAM commercialization runs through her.","Tom Boss: the entroCIM P&L is the viability argument."]),
 ('Use allies in rooms you are not in',["Nathan Kehr, Bill Muczko and Bob Caprise carry CDA and data centers into Greg's organization.","Chris Gazdic: the Navigator overlap makes him a co-owner of the data center story.","Brad Stevens: a heads-up before Greg's office hears about CDA; shape the unified platform rather than react to it."]),
 ('Protect the team that carries it',["David Blondel, Ron Snyder and Chad Steger hold every product row.","CDA now lands on the same people as entroCIM's reduced roadmap.","Capacity, not alignment, is the constraint inside the team."]),
]
cw=2.85; gap=0.17; x=0.73
for i,(h,body) in enumerate(cards):
    r=rect(s,x+i*(cw+gap),1.6,cw,3.85,NAVY if i==0 else STEEL,None,False,MSO_SHAPE.ROUNDED_RECTANGLE); r.adjustments[0]=0.05
    tc=WHITE if i==0 else NAVY; bc=MIST if i==0 else INK
    tb(s,x+i*(cw+gap)+0.2,1.78,cw-0.4,0.6,h,14,True,tc)
    tb(s,x+i*(cw+gap)+0.2,2.45,cw-0.4,2.9,body,12,False,bc)
band=rect(s,0.73,5.75,11.86,0.55,PALE,None,False,MSO_SHAPE.ROUNDED_RECTANGLE); band.adjustments[0]=0.12
tb(s,0.95,5.75,11.4,0.55,'Strong allies at Sean\'s level and below; Akash, Dirk and Greg are still neutral or unknown. Sean and Lisa are the routes up, and the data center briefing and vibe coding concept are what Sean can carry.',11.5,True,INK,anchor=MSO_ANCHOR.MIDDLE)
private(s,' Recommendations are Claude\'s, for Darryl\'s judgment.')
prs.save('2026-10-07_Stakeholder_Map.pptx'); print('saved')
