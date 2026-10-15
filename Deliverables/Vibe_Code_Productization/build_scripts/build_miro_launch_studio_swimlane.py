import html
def e(s): return html.escape(s,quote=True)
F='noto_sans'
GREEN='#00953A'; NAVY='#1D252D'; STEEL='#F1F5F7'; STEEL2='#DFE8ED'; SLATE='#5B7A8E'; PALE='#E9F3EC'; INK='#2B2B2B'; GRID='#B7C9D3'
def rect(id,x,y,w,h,fill,label='',tc=INK,fs=16,bold=False,stroke='none',rx=12,align=None,valign=None,dash=None):
    a=f' data-text-align="{align}"' if align else ''
    v=f' data-text-align-vertical="{valign}"' if valign else ''
    d=f' stroke-dasharray="{dash}"' if dash else ''
    sw=' stroke-width="2"' if stroke!='none' else ''
    return (f'<rect id="{id}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"{sw}{d} '
            f'data-content="{e(label)}" data-text-color="{tc}" data-font-family="{F}" data-font-size="{fs}"'
            f'{" data-font-weight=\"bold\"" if bold else ""}{a}{v} />')
def text(x,y,s,fs,bold=False,color=INK,anchor='start'):
    return f'<text x="{x}" y="{y}" font-family="{F}" font-size="{fs}" font-weight="{"bold" if bold else "normal"}" fill="{color}" text-anchor="{anchor}">{e(s)}</text>'
def ta(x,y,w,s,fs,color=INK):
    return f'<textArea x="{x}" y="{y}" width="{w}" font-family="{F}" font-size="{fs}" fill="{color}">{s}</textArea>'
def conn(a,b,label='',ss=None,es=None,shape='curved',color='#313131',dash=False):
    o=f'<line x1="0" y1="0" x2="1" y2="1" stroke="{color}" stroke-width="2" data-arrow="end" data-start="{a}" data-end="{b}" data-shape="{shape}"'
    if ss: o+=f' data-start-side="{ss}"'
    if es: o+=f' data-end-side="{es}"'
    if dash: o+=' stroke-dasharray="5,5"'
    if label: o+=f' data-content="{e(label)}"'
    return o+' />'
def divider(x1,y1,x2,y2,color=SLATE,style='dashed'):
    return f'<line data-type="divider" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="3" data-line-style="{style}" />'

frames=[]
# ---------------- Option A: swimlane with line of visibility
W,H=2400,1240; P=64
out=[f'<g id="fA" transform="translate(0,0)" data-frame="Option A: Swimlane">',f'<rect data-type="frame" x="0" y="0" width="{W}" height="{H}" fill="#ffffff" data-title="Option A: Swimlane" />']
out.append(text(P,P+40,'Option A: Swimlane with a line of visibility',40,True,NAVY))
out.append(text(P,P+84,'Who does what at each stage. Above the line is what the vibe coder sees; below it, Launch Studio carries the work.',20,False,SLATE))
LW=250; X0=P+LW+20; STAGES=['Submit','Screen','Assess','Commit','Build','Launch','Run']
CW=(W-X0-P-6*12)/7; CW=int(CW)
HY=P+120
for i,s in enumerate(STAGES):
    out.append(rect(f'aH{i}',X0+i*(CW+12),HY,CW,56,PALE,s,GREEN,20,True))
LANES=['Vibe coder','Sponsor','Mike (conduit)','Product owner','Engineering and operations']
LH=150; LY0=HY+56+20
cells={
 (0,0):'Shares the prototype and a one-page summary',(0,1):'15-minute demo',(0,2):'Walks the architect through the prototype',
 (0,4):'Sprint demos and acceptance testing',(0,5):'Credited as originator; first champion',(0,6):'Prototypes the next feature in the sandbox',
 (1,0):'Co-signs the one-page summary',(1,3):'Funds build and run; releases the originator\'s time',(1,6):'Annual review of value',
 (2,0):'Brings the idea forward',(2,1):'Screens with the product owner',
 (3,1):'Sponsor, problem, overlap, data',(3,2):'Scopes the product from the prototype',(3,3):'Darryl and Ron decide; reason given',(3,4):'Owns the backlog and trade-offs',(3,6):'Turns the next prototype into backlog',
 (4,2):'Estimates build and run cost',(4,4):'Rebuilds to engineering standards',(4,5):'Security, identity, hosting, release',(4,6):'Operates, supports, retires'}
for li,l in enumerate(LANES):
    y=LY0+li*(LH+12)+(28 if li>=3 else 0)
    lanefill=STEEL if li<3 else STEEL2
    out.append(rect(f'aL{li}',P,y,LW,LH,lanefill,l,NAVY,20,True,align='left'))
    for si in range(7):
        x=X0+si*(CW+12)
        if (li,si) in cells:
            fill=GREEN if li==0 else ('#FFFFFF' if li<3 else NAVY)
            tc='#FFFFFF' if (li==0 or li>=3) else INK
            out.append(rect(f'c{li}{si}',x,y+12,CW,LH-24,fill,cells[(li,si)],tc,16,False,stroke=('none' if fill!='#FFFFFF' else GRID)))
VY=LY0+3*(LH+12)+8
out.append(divider(P,VY,W-P,VY,SLATE,'dashed'))
out.append(text(X0,VY-6,'Line of visibility: below it, Launch Studio carries security, governance, AI Council, architecture review and operations',16,True,SLATE))
out.append(conn('c06','c36','next prototype becomes the spec','right','right','elbowed',GREEN,True))
out.append('</g>'); frames.append('\n'.join(out))

# ---------------- Option B: blueprint bands
OX=2400+600; W,H=2400,1240
out=[f'<g id="fB" transform="translate({OX},0)" data-frame="Option B: Two bands">',f'<rect data-type="frame" x="0" y="0" width="{W}" height="{H}" fill="#ffffff" data-title="Option B: Two bands" />']
out.append(text(P,P+40,'Option B: What the vibe coder sees, what Launch Studio carries',40,True,NAVY))
out.append(text(P,P+84,'Three touchpoints for the vibe coder. Everything below the line is handled for them.',20,False,SLATE))
TY=P+130; BW=W-2*P
out.append(rect('bTop',P,TY,BW,500,PALE,'',rx=16))
out.append(text(P+32,TY+48,'The vibe coder',28,True,GREEN))
TW=int((BW-64-2*40)/3)
TP=[('1  Submit','Share the prototype and a one-page summary with your sponsor'),('2  Hear back within 30 days','A clear answer and the reason for it'),('3  See it launched','Credited as originator; first champion with colleagues')]
for i,(h,b) in enumerate(TP):
    x=P+32+i*(TW+40)
    out.append(rect(f'bT{i}',x,TY+80,TW,170,GREEN,f'<b>{h}</b><br>{b}',"#FFFFFF",20,align='left',valign='top'))
out.append(text(P+32,TY+300,'Where they stay embedded with the team',20,True,NAVY))
CH=['15-minute demo','Architect walkthrough','Sprint demos','Acceptance testing','Launch champion','Next feature as a prototype']
CWd=int((BW-64-5*20)/6)
for i,c in enumerate(CH):
    out.append(rect(f'bC{i}',P+32+i*(CWd+20),TY+330,CWd,120,'#FFFFFF',c,NAVY,18,True,stroke=GREEN,rx=60))
VY=TY+500+60
out.append(divider(P,VY,W-P,VY,SLATE,'dashed'))
out.append(text(P,VY-14,'Line of visibility',18,True,SLATE))
BY=VY+60
out.append(rect('bBot',P,BY,BW,H-BY-P,STEEL2,'',rx=16))
out.append(text(P+32,BY+48,'Launch Studio carries it for them',28,True,NAVY))
BC=['Screen and assess','AI Council and security review','Identity, hosting and architecture review','Rebuild, release and support','Lifecycle and retirement']
BWd=int((BW-64-4*30)/5)
for i,c in enumerate(BC):
    out.append(rect(f'bB{i}',P+32+i*(BWd+30),BY+80,BWd,150,NAVY,c,'#FFFFFF',20,True))
out.append('</g>'); frames.append('\n'.join(out))

# ---------------- Option C: the loop
OX2=OX+2400+600; W,H=2000,1240
out=[f'<g id="fC" transform="translate({OX2},0)" data-frame="Option C: The loop">',f'<rect data-type="frame" x="0" y="0" width="{W}" height="{H}" fill="#ffffff" data-title="Option C: The loop" />']
out.append(text(P,P+40,'Option C: The loop',40,True,NAVY))
out.append(text(P,P+84,'The vibe coder never leaves the loop. Everything in production belongs to IT.',20,False,SLATE))
NW,NH=360,130
N={'proto':(P+40,560,STEEL2,NAVY,'Prototype','Owned by the business'),
   'gate':(820,200,GREEN,'#FFFFFF','The gate','Screen, assess, commit'),
   'build':(1560,420,NAVY,'#FFFFFF','Build','Rebuilt to standard'),
   'launch':(1560,760,NAVY,'#FFFFFF','Launch','Released and supported'),
   'run':(820,1000,NAVY,'#FFFFFF','Run','Operated, reviewed, retired')}
ROLE={'proto':'Vibe coder builds it in the sandbox','gate':'Demo and architect walkthrough','build':'Sprint demos and acceptance','launch':'Credited; first champion','run':'Prototypes the next feature'}
for k,(x,y,f,tc,h,b) in N.items():
    w=NW if k!='build' and k!='launch' else 360
    xx=min(x,W-P-w)
    N[k]=(xx,y)
    out.append(rect(k,xx,y,w,NH,f,f'<b>{h}</b><br>{b}',tc,22))
for a,b,lab,ss,es in [('proto','gate','','top','left'),('gate','build','accept','right','top'),('build','launch','','bottom','top'),('launch','run','','bottom','right'),('run','proto','next feature starts as a prototype','left','bottom')]:
    out.append(conn(a,b,lab,ss,es,'curved',GREEN if b=='proto' else '#313131',b=='proto'))
for k,(x,y) in N.items():
    pass
out.append(f'<circle id="core" cx="1000" cy="700" r="190" fill="{PALE}" stroke="{GREEN}" stroke-width="2" data-content="{e("<b>Vibe coder</b><br>embedded at every stage<br>never touches production")}" data-text-color="{GREEN}" data-font-family="{F}" data-font-size="22" />')
cap=[('gate',820,200+NH+12),('build',1560-0,420+NH+12),('launch',1560,760+NH+12),('run',820,1000+NH+12),('proto',P+40,560+NH+12)]
for k,x,y in cap:
    xx=N[k][0]
    out.append(ta(xx,y,360,f'<i>{e(ROLE[k])}</i>',16,SLATE))
out.append('</g>'); frames.append('\n'.join(out))

svg='<svg xmlns="http://www.w3.org/2000/svg">\n'+'\n'.join(frames)+'\n</svg>'
open('/tmp/claude-0/miro/board.svg','w').write(svg)
print(len(svg))
