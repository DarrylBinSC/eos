# Generates the Canvas Composer SVG for the Miro board "Stakeholder Map 2026-10" (built 2026-10-07).
# Edit the people lists, alignment codes (ally/sup/neu/mix/unk) and grid placements G, then run;
# output board.svg is split into one SVG per frame and sent with the Miro connector (canvas_create_from_svg).
# Paths at the bottom write to /tmp/claude-0/miro; change as needed.
import html
S={'ally':('#00953A','#006B29','#FFFFFF',None),'sup':('#CDEBD6','#00953A','#1D252D',None),
   'neu':('#E3E7EA','#8E9296','#1D252D',None),'mix':('#F7D9A8','#C77A12','#1D252D',None),
   'unk':('#FFFFFF','#5B7A8E','#1D252D','5,5'),'self':('#1D252D','#1D252D','#FFFFFF',None),
   'prod':('#004986','#004986','#FFFFFF',None)}
F='noto_sans'
def e(s): return html.escape(s,quote=True)
def node(id,x,y,w,h,st,label,fs=14,stroke_override=None,sw=2,rx=10):
    fill,stroke,txt,dash=S[st]
    if stroke_override: stroke=stroke_override
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<rect id="{id}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} '
            f'data-content="{e(label)}" data-text-color="{txt}" data-font-family="{F}" data-font-size="{fs}" />')
def text(x,y,s,fs,bold=False,color='#1D252D',anchor='start',rot=None):
    r=f' data-rotation="{rot}"' if rot is not None else ''
    return f'<text x="{x}" y="{y}" font-family="{F}" font-size="{fs}" font-weight="{"bold" if bold else "normal"}" fill="{color}" text-anchor="{anchor}"{r}>{e(s)}</text>'
def conn(a,b,label,ss,es,shape='straight',dotted=False,color='#313131'):
    d=' stroke-dasharray="2,2"' if dotted else ''
    return (f'<line x1="0" y1="0" x2="1" y2="1" stroke="{color}" stroke-width="2" data-arrow="end" data-start="{a}" data-end="{b}" '
            f'data-shape="{shape}" data-start-side="{ss}" data-end-side="{es}" data-content="{e(label)}"{d} />')
def legend(x,y,team=False,dotted=False):
    out=[]; items=[('ally','Ally'),('sup','Supportive'),('neu','Neutral'),('mix','Mixed'),('unk','Unknown'),('self','Darryl'),('prod','Product')]
    cx=x
    out.append(text(cx,y+18,'Legend',16,True)); cx+=100
    for i,(st,lab) in enumerate(items):
        out.append(node(f'lg{st}{int(team)}{int(dotted)}',cx,y,40,26,st,'',rx=6)); out.append(text(cx+50,y+18,lab,14)); cx+=170
    if team:
        out.append(node('lgteam',cx,y,40,26,'ally','',stroke_override='#1D252D',sw=4,rx=6)); out.append(text(cx+50,y+18,"Darryl's team (navy border)",14)); cx+=280
    if dotted:
        out.append(f'<line data-type="divider" x1="{cx}" y1="{y+13}" x2="{cx+50}" y2="{y+13}" stroke="#313131" stroke-width="2" data-line-style="dotted" />')
        out.append(text(cx+60,y+18,'Route not yet established',14))
    return out

# ---------------- Frame 1
W,H=2000,2260
NX,NW,NH,GAP=160,290,72,40
def stack(y0,n): return [y0+64+i*(NH+GAP) for i in range(n)]
exec_=[('AKASH','Akash Khurana','CIO','neu'),('SEAN','Sean McCloskey','VP, all digital products','ally'),('LISA','Lisa Orton','IT to CSS connection','ally'),('DIRK','Dirk Naylor','EVP & GM, CSS','unk'),('GREG',"Greg O'Brien",'SVP & GM, TSS','unk')]
peer=[('MERWAN','Merwan Mereby','India development and AI','neu'),('MADDY','Maddy Taylor','Digital Products peer','sup'),('BRAD','Brad Stevens','VP Sales','mix'),('CHRISG','Chris Gazdic','Product Operations','ally'),('TOM','Tom Boss','Finance','neu')]
team=[('DARRYL','Darryl Benson','Sr Dir, CSS Platforms','self'),('DAVID','David Blondel','Product Executive','ally'),('AKANSH','Akansh Gangil','WAM / ADM PO','ally'),('RON','Ron Snyder','Development','ally'),('CHAD','Chad Steger','Deployment','ally')]
sales=[('NATE','Nathan Kehr','CSS Platforms sales','ally'),('WASSIL','Michael Wassil','Competitive intel','sup'),('BILL','Bill Muczko','Global Enterprise, CDA sponsor','ally'),('BOB','Bob Caprise','CSS Sales','ally'),('SRIDHAR','Sridhar Loke','Commercialization','sup'),('AMY','Amy Aguirre','WAM commercial','neu')]
deliv=[('DJ','DJ Vaughn','Navigator delivery','sup'),('EMILY','Emily Munk','Strategic Initiatives, TSS','unk'),('SENTHIL','Senthil Govindaswamy','WAM delivery','sup'),('SUNNY','Sunny Sharma','Strev, WAM vendor','sup')]
prods=[('NAV','Navigator'),('ECIM','entroCIM'),('CDA','CDA'),('WAM','WAM'),('VIBE','Vibe coding productization'),('ARIS','Aris (paused)')]
def panelh(n): return 64+n*NH+(n-1)*GAP+24
panels=[]; nodes=[]
y=200
for title,grp in [('Executive and decision rights',exec_),('Peer and platform organizations',peer),("Darryl's team",team)]:
    h=panelh(len(grp)); panels.append((NX-32,y,NW+64,h,title))
    for (id,n,r,st),ny in zip(grp,stack(y,len(grp))): nodes.append((id,NX,ny,NW,NH,st,f'<b>{n}</b><br>{r}'))
    y+=h+32
leftend=y-32
RX=1620
tot=panelh(6)+32+panelh(4); ry=200+((leftend-200)-tot)//2
for title,grp in [('Sales and commercial',sales),('Delivery and vendors',deliv)]:
    h=panelh(len(grp)); panels.append((RX-32,ry,NW+64,h,title))
    for (id,n,r,st),ny in zip(grp,stack(ry,len(grp))): nodes.append((id,RX,ny,NW,NH,st,f'<b>{n}</b><br>{r}'))
    ry+=h+32
PX,PW,PH=890,300,96
panels.append((PX-40,200,PW+80,leftend-200,'Products'))
step=(leftend-200-64-24-PH)/5
for i,(id,n) in enumerate(prods): nodes.append((id,PX,int(200+64+i*step),PW,PH,'prod',f'<b>{n}</b>'))
f1=[f'<g id="f1" transform="translate(0,0)" data-frame="Decision Rights Map">',
    f'<rect data-type="frame" x="0" y="0" width="{W}" height="{H}" fill="#ffffff" data-title="Decision Rights Map" />',
    text(64,110,'Decision rights by product',48,True),
    text(64,160,'As of 2026-10-07. Private working draft. Not for distribution.',16,False,'#595959')]
for x,y,w,h,t in panels:
    fill,stroke=('#EAF0F6','#004986') if t=='Products' else ('#F4F6F7','#B7C9D3')
    f1.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2" />')
    f1.append(text(x+24,y+40,t,20,True,'#004986' if t=='Products' else '#1D252D'))
E=[]
H_=lambda a,b,l,ss='left',es='left': E.append(conn(a,b,l,ss,es,'elbowed'))
V=lambda a,b,l: E.append(conn(a,b,l,'bottom','top','straight'))
P=lambda a,b,l,dot=False: E.append(conn(a,b,l,'right','left','straight',dot))
V('AKASH','SEAN','manages'); H_('AKASH','LISA','manages'); H_('AKASH','MERWAN','manages')
V('LISA','DIRK','routes to'); H_('SEAN','MADDY','manages'); H_('SEAN','DARRYL','manages')
V('DARRYL','DAVID','leads'); V('DAVID','AKANSH','leads'); H_('DARRYL','RON','leads'); H_('DARRYL','CHAD','leads')
P('LISA','NAV','influences'); P('DIRK','ECIM','sponsors'); P('DIRK','NAV','sponsors'); P('SEAN','VIBE','funds, originated')
P('SEAN','ARIS','receiving'); P('AKASH','WAM','WAM takeover decision'); P('GREG','CDA','delivery home, not engaged',True)
P('BRAD','ECIM','integrated platform push',True); P('CHRISG','NAV','product executive'); P('MERWAN','WAM','builds today')
P('TOM','ECIM','P&L'); P('DARRYL','VIBE','stands up'); P('DAVID','ECIM','product executive'); P('RON','ECIM','builds')
P('RON','CDA','builds'); P('CHAD','ECIM','deploys'); P('AKANSH','WAM','product owner')
P('ECIM','NATE','sold by'); P('CDA','NATE','champion'); P('CDA','BILL','sponsor'); P('CDA','BOB','champion')
P('CDA','SRIDHAR','commercialization'); P('WAM','AMY','commercialized by'); P('ECIM','WASSIL','intel')
P('CDA','EMILY','route to Greg',True); P('WAM','SENTHIL','delivered by'); P('NAV','DJ','delivered by'); P('WAM','SUNNY','platform vendor')
f1+=E
for n in nodes: f1.append(node(*n))
f1+=legend(64,H-90,dotted=True)
f1.append('</g>')

# ---------------- Frame 2
cols=['Unknown','Mixed','Neutral','Supportive','Ally']; cst=['unk','mix','neu','sup','ally']
rows=[('High',300),('Medium-High',200),('Medium',250),('Low-Medium',150)]
G={('High','Unknown'):[('Dirk Naylor',0),("Greg O'Brien",0)],('High','Mixed'):[('Brad Stevens',0)],('High','Neutral'):[('Akash Khurana (CIO)',0)],
 ('High','Ally'):[('Sean McCloskey',0),('Nathan Kehr',0),('David Blondel',1),('Ron Snyder',1),('Chad Steger',1)],
 ('Medium-High','Neutral'):[('Merwan Mereby',0)],('Medium-High','Ally'):[('Lisa Orton',0),('Chris Gazdic',0),('Bill Muczko',0)],
 ('Medium','Unknown'):[('Emily Munk',0)],('Medium','Neutral'):[('Tom Boss',0),('Amy Aguirre',0)],
 ('Medium','Supportive'):[('Sridhar Loke',0),('Senthil Govindaswamy',0),('DJ Vaughn',0),('Sunny Sharma (Strev)',0)],
 ('Medium','Ally'):[('Bob Caprise',0),('Akansh Gangil',1)],('Low-Medium','Supportive'):[('Maddy Taylor',0),('Michael Wassil',0)]}
W2,H2=1960,1420; X0,Y0,CW=300,260,320
f2=[f'<g id="f2" transform="translate(2320,0)" data-frame="Influence and Alignment Grid">',
    f'<rect data-type="frame" x="0" y="0" width="{W2}" height="{H2}" fill="#ffffff" data-title="Influence and Alignment Grid" />',
    text(64,110,'Influence and alignment',48,True),
    text(64,160,'As of 2026-10-07. Private working draft. Not for distribution.',16,False,'#595959')]
gh=rows[0][1]+rows[1][1]
f2.append(f'<rect x="{X0}" y="{Y0}" width="{CW*3}" height="{gh}" fill="#FDF3E3" stroke="#F7D9A8" stroke-width="2" />')
f2.append(f'<rect x="{X0+CW*3}" y="{Y0}" width="{CW*2}" height="{gh}" fill="#E9F3EC" stroke="#CDEBD6" stroke-width="2" />')
total=sum(h for _,h in rows)
# grid lines
yy=Y0
for _,h in rows+[('',0)]:
    f2.append(f'<line data-type="divider" x1="{X0}" y1="{yy}" x2="{X0+CW*5}" y2="{yy}" stroke="#B0B0B0" stroke-width="2" />'); yy+=h
for c in range(6):
    f2.append(f'<line data-type="divider" x1="{X0+c*CW}" y1="{Y0}" x2="{X0+c*CW}" y2="{Y0+total}" stroke="#B0B0B0" stroke-width="2" />')
for ci,c in enumerate(cols): f2.append(text(X0+ci*CW+CW//2,Y0-20,c,20,True,'#1D252D','middle'))
f2.append(text(X0+CW*5//2,Y0-60,'ALIGNMENT TODAY',14,True,'#5B7A8E','middle'))
yy=Y0
for rn,h in rows:
    f2.append(text(X0-24,yy+h//2+7,rn,20,True,'#1D252D','end')); yy+=h
f2.append(text(110,Y0+total//2,'INFLUENCE ON OUTCOMES',14,True,'#5B7A8E','middle',rot=-90))
# zone labels
f2.append(text(X0+CW*1+CW//2,Y0+rows[0][1]+rows[1][1]-40,'ACCESS GAP',16,True,'#9B4A08','middle'))
f2.append(text(X0+CW*1+CW//2,Y0+rows[0][1]+rows[1][1]-18,'High influence, not yet aligned',13,False,'#9B4A08','middle'))
f2.append(text(X0+CW*3+CW//2,Y0+rows[0][1]-40,'LEVERAGE',16,True,'#067429','middle'))
f2.append(text(X0+CW*3+CW//2,Y0+rows[0][1]-18,'High influence, aligned',13,False,'#067429','middle'))
yy=Y0; k=0
for rn,h in rows:
    for ci,c in enumerate(cols):
        for i,(n,t) in enumerate(G.get((rn,c),[])):
            k+=1
            f2.append(node(f'g{k}',X0+ci*CW+20,yy+20+i*52,CW-40,40,cst[ci],f'<b>{n}</b>',stroke_override='#1D252D' if t else None,sw=4 if t else 2,rx=8))
    yy+=h
f2+=legend(64,H2-90,team=True)
f2.append('</g>')
svg='<svg xmlns="http://www.w3.org/2000/svg">\n'+'\n'.join(f1+f2)+'\n</svg>'
open('/tmp/claude-0/miro/board.svg','w').write(svg); print(len(svg), leftend, sum(1 for l in f1 if l.startswith('<line')))
