# EOS web app architecture, executive view, 2026-10-28 (python-pptx on the Wesco template).
# One slide, native shapes, left to right: who feeds it, the app, the record, the safeguards.
import sys, os
from pptx import Presentation
from pptx.util import Inches as In, Pt
from pptx.dml.color import RGBColor as C
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn
NAVY=C(0x1D,0x25,0x2D); GREEN=C(0x00,0x95,0x3A); WHITE=C(0xFF,0xFF,0xFF); INK=C(0x2B,0x2B,0x2B)
STEEL=C(0xF1,0xF5,0xF7); GREY=C(0x6E,0x73,0x78); MBLUE=C(0x00,0x49,0x86); LINE=C(0xB8,0xC0,0xC6)
F='Arial'
ROOT=os.path.dirname(os.path.abspath(__file__))
prs=Presentation(os.path.join(ROOT,'..','..','..','Reference','Templates','Wesco_Slide_Template.pptx')); ids=prs.slides._sldIdLst
for sid in list(ids): prs.part.drop_rel(sid.get(qn('r:id'))); ids.remove(sid)
L={l.name:l for l in prs.slide_layouts}
def run(tf,text,size,bold=False,color=INK,after=2,first=False,align=PP_ALIGN.LEFT):
    p=tf.paragraphs[0] if first else tf.add_paragraph(); p.space_after=Pt(after); p.alignment=align
    r=p.add_run(); r.text=text; f=r.font; f.size=Pt(size); f.bold=bold; f.color.rgb=color; f.name=F; return p
def box(s,x,y,w,h,fill=None,line=None,lw=1.0,adj=0.06):
    sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,In(x),In(y),In(w),In(h)); sh.adjustments[0]=adj
    if fill is None: sh.fill.background()
    else: sh.fill.solid(); sh.fill.fore_color.rgb=fill
    if line is None: sh.line.fill.background()
    else: sh.line.color.rgb=line; sh.line.width=Pt(lw)
    sh.shadow.inherit=False; return sh
def label(sh,lines,align=PP_ALIGN.LEFT,m=0.12,anchor=MSO_ANCHOR.MIDDLE):
    tf=sh.text_frame; tf.word_wrap=True; tf.vertical_anchor=anchor
    tf.margin_left=tf.margin_right=In(m); tf.margin_top=tf.margin_bottom=In(0.06)
    for i,(t,sz,b,c) in enumerate(lines): run(tf,t,sz,b,c,after=1,first=(i==0),align=align)
    return sh
def arrow(s,x1,y1,x2,y2,color=GREY,w=1.5,dash=False):
    c=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,In(x1),In(y1),In(x2),In(y2))
    c.line.color.rgb=color; c.line.width=Pt(w)
    ln=c.line._get_or_add_ln(); ln.append(ln.makeelement(qn('a:tailEnd'),{'type':'triangle','w':'med','len':'med'}))
    if dash: c.line.dash_style=4
    return c
def head(s,x,y,w,text):
    tf=s.shapes.add_textbox(In(x),In(y),In(w),In(0.3)).text_frame; tf.margin_left=tf.margin_top=0
    run(tf,text,11,True,MBLUE,first=True)

s=prs.slides.add_slide(L['Blank-with-Title'])
s.shapes.title.text_frame.paragraphs[0].add_run().text='EOS Web App'

# geometry: four columns
T=1.45; H=3.9
# Column 1: who feeds it
head(s,0.5,T,2.5,'WHO FEEDS IT')
inputs=[('You','Any device at home. Edit items, add notes, escalate, review.'),
        ('Claude','Working sessions and the daily brief. Files evidence, writes items and product notes.'),
        ('M365 Copilot','Meeting and email evidence, pasted to Claude.'),
        ('Team leads','Weekly Excel review, read back into the record.')]
ch=0.82; gap=0.14; y=T+0.4
for name,desc in inputs:
    b=box(s,0.5,y,2.5,ch,fill=STEEL,line=None); label(b,[(name,12,True,NAVY),(desc,9,False,INK)]); y+=ch+gap
# Column 2: the app
head(s,3.55,T,2.6,'THE APP')
app=box(s,3.55,T+0.4,2.6,H-0.4,fill=NAVY)
label(app,[('EOS server',14,True,WHITE),('One small program on my Mac, on the home network only.',10,False,WHITE),
           ('',6,False,WHITE),('\u2022  Shows the registers, Pulse, products and briefs',10,False,WHITE),
           ('\u2022  Writes every edit straight to the record',10,False,WHITE),('\u2022  Rebuilds the summary views on every change',10,False,WHITE),
           ('\u2022  Logs each change to the history',10,False,WHITE),('\u2022  Restarts itself when Claude updates its code',10,False,WHITE)],anchor=MSO_ANCHOR.TOP)
# Column 3: the record
head(s,6.7,T,2.6,'THE RECORD')
rec=box(s,6.7,T+0.4,2.6,H-0.4,fill=WHITE,line=MBLUE,lw=1.5)
label(rec,[('EOS folder',14,True,MBLUE),('Plain files, one per item. No database.',10,False,INK),('',6,False,INK),
           ('\u2022  Registers: actions, watch, decisions, Pulse',10,False,INK),('\u2022  Product notes and briefs',10,False,INK),
           ('\u2022  Evidence packages and review workbooks',10,False,INK),('',6,False,INK),
           ('Synced by iCloud to my other laptop',10,False,GREY)],anchor=MSO_ANCHOR.TOP)
# Column 4: safeguards
head(s,9.85,T,2.6,'SAFEGUARDS')
g1=box(s,9.85,T+0.4,2.6,1.6,fill=STEEL); label(g1,[('Change history',12,True,NAVY),('Every edit recorded with who, what and when. Kept on the Mac, outside iCloud.',9,False,INK)])
g2=box(s,9.85,T+2.15,2.6,1.35,fill=STEEL); label(g2,[('Off-site backup',12,True,NAVY),('Private GitHub copy of the history, updated after every change. Nothing reads from it.',9,False,INK)])
# arrows between columns (mid-height)
m=T+0.4+(H-0.4)/2
arrow(s,3.0,m,3.55,m); arrow(s,6.15,m,6.7,m)
arrow(s,9.3,T+1.2,9.85,T+1.2); arrow(s,11.15,T+2.0,11.15,T+2.15)
# Claude also writes to the record directly: thin dashed arrow from Claude card under the app
# Bottom strip
tf=s.shapes.add_textbox(In(0.5),In(5.55),In(11.95),In(0.9)).text_frame; tf.word_wrap=True; tf.margin_left=0
run(tf,'What this means',11,True,MBLUE,first=True,after=3)
run(tf,'The folder is the system. The app is a window onto it, Claude works in the same files, and the history and backup mean nothing is lost if the Mac is. No cloud service holds the data, no login is exposed outside the house, and any change can be undone from the history.',10,False,INK)
out=os.path.join(ROOT,'..','2026-10-28_EOS_Web_App_Architecture.pptx'); prs.save(out); print(out)
