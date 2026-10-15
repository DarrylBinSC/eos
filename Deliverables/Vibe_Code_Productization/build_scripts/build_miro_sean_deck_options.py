import html
def e(s): return html.escape(s,quote=True)
F='noto_sans'
GREEN='#00953A'; NAVY='#1D252D'; STEEL='#F1F5F7'; STEEL2='#DFE8ED'; SLATE='#5B7A8E'; PALE='#E9F3EC'; INK='#2B2B2B'; GRID='#B7C9D3'; MB='#004986'; MBT='#CCDAE7'
def rect(id,x,y,w,h,fill,label='',tc=INK,fs=14,bold=False,stroke='none',rx=10,align=None,valign=None,dash=None):
    a=f' data-text-align="{align}"' if align else ''
    v=f' data-text-align-vertical="{valign}"' if valign else ''
    d=f' stroke-dasharray="{dash}"' if dash else ''
    sw=' stroke-width="2"' if stroke!='none' else ''
    return (f'<rect id="{id}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"{sw}{d} data-content="{e(label)}" data-text-color="{tc}" data-font-family="{F}" data-font-size="{fs}"{" data-font-weight=\"bold\"" if bold else ""}{a}{v} />')
def text(x,y,s,fs,bold=False,color=INK,anchor='start'):
    return f'<text x="{x}" y="{y}" font-family="{F}" font-size="{fs}" font-weight="{"bold" if bold else "normal"}" fill="{color}" text-anchor="{anchor}">{e(s)}</text>'
def conn(a,b,label='',ss=None,es=None,shape='straight',color='#313131',dash=False):
    o=f'<line x1="0" y1="0" x2="1" y2="1" stroke="{color}" stroke-width="2" data-arrow="end" data-start="{a}" data-end="{b}" data-shape="{shape}"'
    if ss: o+=f' data-start-side="{ss}"'
    if es: o+=f' data-end-side="{es}"'
    if dash: o+=' stroke-dasharray="5,5"'
    if label: o+=f' data-content="{e(label)}"'
    return o+' />'
def divider(x1,y1,x2,y2,color=SLATE,style='dashed'):
    return f'<line data-type="divider" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2" data-line-style="{style}" />'
frames=[]
SW,SH=1280,720
def slide(id,x,y,title,headline):
    o=[rect(f'{id}bg',x,y,SW,SH,'#FFFFFF',stroke=GRID,rx=4)]
    o.append(text(x+40,y+56,title,30,True,NAVY)); o.append(text(x+40,y+90,headline,16,False,SLATE))
    return o

# ================= Frame 1: Slide 1 options
W,H=2900,1700; P=64
out=[f'<g id="f1" transform="translate(0,0)" data-frame="Slide 1 options: What Launch Studio is">',f'<rect data-type="frame" x="0" y="0" width="{W}" height="{H}" fill="#ffffff" data-title="Slide 1 options: What Launch Studio is" />']
out.append(text(P,P+36,'Slide 1: What Launch Studio is',40,True,NAVY))
out.append(text(P,P+76,'Two ways to show the same idea: the business brings prototypes, the Studio grades them and takes the good ones to supported products, under existing approvals.',18,False,SLATE))
# --- Option 1A: the path with inlet filter
x0,y0=P,P+130
out.append(text(x0,y0-12,'Option 1A: The path (recommended)',20,True,GREEN))
out+=slide('a',x0,y0,'Launch Studio','From business prototypes to supported products, under the approvals we already have.')
# nodes
out.append(rect('a1',x0+40,y0+200,260,220,STEEL2,'<b>Ideas from the business</b><br>AI Builders Guild<br>prototypes in the sandbox',NAVY,15))
# funnel: trapezoid-ish using a wedge: use rect narrow
out.append(rect('a2',x0+360,y0+230,220,160,GREEN,'<b>Inlet filter</b><br>Worth doing?<br>Can it become a product?','#FFFFFF',15))
out.append(rect('a3',x0+640,y0+200,300,220,NAVY,'<b>Launch Studio</b><br>Build to standard<br>Host, secure, support<br>Retire at end of life','#FFFFFF',15))
out.append(rect('a4',x0+1000,y0+230,240,160,PALE,'<b>Supported product</b><br>Measured value<br>Business-funded',GREEN,15,stroke=GREEN))
out.append(conn('a1','a2','','right','left')); out.append(conn('a2','a3','take in','right','left')); out.append(conn('a3','a4','','right','left'))
out.append(conn('a2','a1','fold in, defer, return','bottom','bottom','curved',SLATE,True))
out.append(rect('a5',x0+40,y0+500,1200,70,STEEL,'Existing approvals stay in place: AI Council and intake  |  Security and WAB  |  Finance  |  Business sponsor',NAVY,15,True))
out.append(rect('a6',x0+40,y0+600,1200,70,PALE,'The builder sees a studio. IT carries the governance. If IT touches it, IT owns it.',NAVY,16,True))
# --- Option 1B: two zones + line of visibility
x0=P+SW+120
out.append(text(x0,y0-12,'Option 1B: Two zones, one gate',20,True,SLATE))
out+=slide('b',x0,y0,'Launch Studio','A prototype is the business\'s. A product is IT\'s. One gate between them.')
out.append(rect('b1',x0+40,y0+170,380,260,STEEL2,'<b>PROTOTYPE</b><br>Owned by the business<br><br>Built in a sandbox<br>No production data<br>Registered',NAVY,15))
out.append(rect('b2',x0+450,y0+170,380,260,GREEN,'<b>THE GATE</b><br>Grade value and viability<br><br>Sponsor commits<br>funding and a success measure','#FFFFFF',15))
out.append(rect('b3',x0+860,y0+170,380,260,NAVY,'<b>PRODUCT</b><br>Owned by IT<br><br>Rebuilt or hardened to standard<br>Hosted, supported, retired','#FFFFFF',15))
out.append(conn('b1','b2','','right','left')); out.append(conn('b2','b3','','right','left'))
out.append(divider(x0+40,y0+470,x0+1240,y0+470))
out.append(text(x0+40,y0+500,'Above the line: what the builder sees. Below: what Launch Studio carries.',14,True,SLATE))
out.append(rect('b4',x0+40,y0+520,1200,60,STEEL,'Screen and assess  |  AI Council and security  |  Identity, hosting, architecture review  |  Release and support  |  Lifecycle',NAVY,14))
out.append(rect('b5',x0+40,y0+610,1200,60,PALE,'Existing approvals stay in place. No new approval body.',NAVY,15,True))
# notes under
out.append(text(P,y0+SH+70,'1A tells the story left to right and makes the inlet filter the hero, which matches what Darryl asked for. 1B is the picture Mike has already seen. Either works; 1A says more in one glance.',16,False,INK))
out.append('</g>'); frames.append('\n'.join(out))

# ================= Frame 2: Slide 2 options
OX=W+400
out=[f'<g id="f2" transform="translate({OX},0)" data-frame="Slide 2 options: Pilot, funding, decisions">',f'<rect data-type="frame" x="0" y="0" width="{W}" height="{H}" fill="#ffffff" data-title="Slide 2 options: Pilot, funding, decisions" />']
out.append(text(P,P+36,'Slide 2: What happens next, and what we need from Sean',40,True,NAVY))
out.append(text(P,P+76,'Both carry the pilot, the funding shape, capacity and the four decisions. They differ in what leads.',18,False,SLATE))
x0,y0=P,P+130
out.append(text(x0,y0-12,'Option 2A: Decisions lead (recommended)',20,True,GREEN))
out+=slide('c',x0,y0,'Next steps','A pilot on the current team. Four things to settle with you.')
# left: pilot timeline chevrons
out.append(text(x0+40,y0+140,'PILOT',12,True,GREEN))
for i,(t,b) in enumerate([('Q4 2026','Agree the path; first candidates graded'),('Q1 2027','Two or three tools built; first measured results'),('2027','Open to EES, UBS and functions if the gates hold')]):
    out.append(rect(f'c{i}',x0+40+i*200,y0+160,190,110,STEEL2 if i<2 else STEEL,f'<b>{t}</b><br>{b}',NAVY,13))
out.append(text(x0+40,y0+310,'FUNDING SHAPE',12,True,GREEN))
out.append(rect('c3',x0+40,y0+330,580,90,PALE,'IT funds the standing team. Each product is a business-funded project that reimburses IT for productization, then upkeep. Menu: sandbox, pilot, sponsored product, shared product.',NAVY,13,align='left'))
out.append(text(x0+40,y0+460,'CAPACITY',12,True,GREEN))
out.append(rect('c4',x0+40,y0+480,580,70,STEEL,'Launch Studio decides what it takes into build, against a limit Ron sets. Current team to start.',NAVY,13,align='left'))
# right: decisions
out.append(rect('c5',x0+680,y0+140,560,440,NAVY,'',rx=12))
out.append(text(x0+710,y0+180,'FROM YOU, WEEK OF OCTOBER 19',13,True,'#00AA13'))
for i,d in enumerate(['Your read on the direction','Where the standing team\'s funding sits','How to position this with Akash','Whether this needs an FY27 AOP line']):
    out.append(rect(f'c6{i}',x0+710,y0+210+i*88,500,70,'#2A3340',f'<b>{i+1}</b>   {d}','#FFFFFF',15,align='left'))
out.append(rect('c7',x0+40,y0+600,1200,70,PALE,'Thirty minutes. Mike Wassil and I are aligned; this is a joint initiative.',NAVY,15,True))
# --- Option 2B: menu leads
x0=P+SW+120
out.append(text(x0,y0-12,'Option 2B: Menu leads',20,True,SLATE))
out+=slide('d',x0,y0,'Next steps','The business picks from a menu. We run a pilot on the current team.')
for i,(t,b1,b2) in enumerate([('Sandbox','Business: nothing','IT: registration'),('Pilot','Business: bounded project','IT: pilot build, 90-day decision'),('Sponsored product','Business: reimburses build, then upkeep','IT: owns end to end'),('Shared product','Business: co-funded','IT: owns, reuse across segments')]):
    out.append(rect(f'd{i}',x0+40+i*300,y0+140,280,170,STEEL2 if i<2 else NAVY,f'<b>{t}</b><br>{b1}<br>{b2}',NAVY if i<2 else '#FFFFFF',13))
out.append(rect('d4',x0+40,y0+340,1200,50,PALE,'No sponsor, no production. IT funds the team; business projects reimburse it.',NAVY,14,True))
for i,(t,b) in enumerate([('Q4 2026','Agree the path'),('Q1 2027','Two or three tools, first results'),('2027','Open wider if gates hold')]):
    out.append(rect(f'd5{i}',x0+40+i*400,y0+420,380,70,STEEL,f'<b>{t}</b>  {b}',NAVY,13))
out.append(rect('d6',x0+40,y0+520,1200,150,NAVY,'<b>From you:</b> direction  |  funding home  |  positioning with Akash  |  FY27 AOP line','#FFFFFF',15))
out.append(text(P,y0+SH+70,'2A puts the four decisions where Sean\'s eye lands first and keeps the funding menu to one line; the menu detail moves to backup. 2B leads with the menu, which is the newest idea but not the thing Sean has to decide next week.',16,False,INK))
out.append('</g>'); frames.append('\n'.join(out))

# ================= Frame 3: story + backup list
OX2=OX+W+400
W3,H3=1400,1700
out=[f'<g id="f3" transform="translate({OX2},0)" data-frame="Story and backup">',f'<rect data-type="frame" x="0" y="0" width="{W3}" height="{H3}" fill="#ffffff" data-title="Story and backup" />']
out.append(text(P,P+36,'The story in two slides',40,True,NAVY))
out.append(rect('s1',P,P+90,W3-2*P,150,PALE,'<b>Slide 1.</b> People across the business can now build working prototypes; almost none become tools the business can rely on. Launch Studio is the path: the business brings ideas, the Studio grades them and takes the good ones to supported, measured products, using approvals that already exist.',NAVY,16,align='left'))
out.append(rect('s2',P,P+270,W3-2*P,150,PALE,'<b>Slide 2.</b> A pilot on the current team, Q4 2026 to Q1 2027. IT funds the team, the business funds each product. Four things to settle with Sean, including whether this needs an AOP line.',NAVY,16,align='left'))
out.append(text(P,P+500,'Backup slides',30,True,NAVY))
B=[('B1 Who does what','Three lanes: Guild finds and proves; Studio grades, builds, runs; existing bodies decide. Capacity decision row.'),
   ('B2 The on-ramp','Two grading questions, the tools, four outcomes with reasons, 30-day target. Grade becomes value contract and reimbursement project.'),
   ('B3 Funding menu','Four options: what the business commits, what IT carries, when it fits. Mechanism a future decision with Finance.'),
   ('B4 The builder\'s experience','You bring the idea, we handle the rest. Touchpoints, involvement, line of visibility.'),
   ('B5 Pilot plan','Quarter by quarter with exit evidence. Candidate list to be confirmed from the Guild funnel.'),
   ('B6 Evidence base','What Mike\'s research found, labeled by strength. No unverified statistics.')]
for i,(t,b) in enumerate(B):
    out.append(rect(f'bk{i}',P,P+540+i*150,W3-2*P,130,STEEL if i%2 else STEEL2,f'<b>{t}</b><br>{b}',NAVY,15,align='left'))
out.append('</g>'); frames.append('\n'.join(out))
svg='<svg xmlns="http://www.w3.org/2000/svg">\n'+'\n'.join(frames)+'\n</svg>'
open('/tmp/claude-0/miro2/board.svg','w').write(svg); print(len(svg))
