const $=s=>document.querySelector(s);
let BRIEFS=[],BRIEF=null,BREAD=false,ITEMS=[],TODAY='',VIEW='triage',Q='',SEL=null,MOREW=false,DRAWER=null,PULSE=null,PF={},PALL=false;
const BASE={},SESSION=[],SAVED={};
const CLOSED=new Set(['closed','dropped','aged_out']);
const isOpen=i=>!CLOSED.has(i.status)&&i.tier!=='retired';
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const plain=s=>String(s??'').replace(/\*\*([^*]+)\*\*/g,'$1').replace(/`([^`]+)`/g,'$1').replace(/~~([^~]+)~~/g,'$1');
let toastT;function toast(t){const e=$('#toast');e.textContent=t;e.style.display='block';clearTimeout(toastT);toastT=setTimeout(()=>e.style.display='none',2200)}
async function load(){const [j,p]=await Promise.all([fetch('/api/items').then(r=>r.json()),fetch('/api/pulse').then(r=>r.ok?r.json():null).catch(()=>null),loadBriefs()]);ITEMS=j.items;TODAY=j.today;PULSE=p;render();const o=new URLSearchParams(location.search).get('open');if(o&&!DRAWER)openDrawer(o)}

const VIEWS=[['triage','Focus'],['pulse','Pulse'],['briefs','Briefs'],['products','Products'],['A','Mine'],['other','Other-owned'],['watch','Watch'],['decision','Decisions'],['needs','Needs triage'],['closed','Disposed']];
const MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],WD=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
const dn=s=>{const[y,m,d]=s.split('-').map(Number);return Date.UTC(y,m-1,d)};
const days=s=>Math.round((dn(s)-dn(TODAY))/864e5);
const fmt=s=>{if(!/^\d{4}-\d{2}-\d{2}/.test(s||''))return esc(s||'');const[y,m,d]=s.split('-').map(Number);return MON[m-1]+' '+d+(y!==+TODAY.slice(0,4)?', '+y:'')};
const cap=s=>s?s.charAt(0).toUpperCase()+s.slice(1).replace('_',' '):'';
function dueKey(i){return i.due||i.forum_date||'9999'}
function inView(i,v){
  if(v==='pulse')return i.kind==='pulse'&&i.category!=='knowledge'&&i._state==='live';
  if(v==='triage')return isOpen(i)&&((i.kind==='action'&&(i.register==='A'||i.register==='triage'||i.critical))||(i.kind==='watch'&&i.tier==='active')||(i.kind==='decision'&&i.tier==='radar'));
  if(v==='A')return isOpen(i)&&i.kind==='action'&&i.register==='A';
  if(v==='other')return isOpen(i)&&i.kind==='action'&&i.register==='other';
  if(v==='watch')return isOpen(i)&&i.kind==='watch';
  if(v==='decision')return isOpen(i)&&i.kind==='decision';
  if(v==='needs')return !!i.needs_triage;
  if(v==='closed')return !isOpen(i)&&i.kind!=='pulse';
}
/* ---------- sorting (2026-10-16): every list has a visible, stated order; choice remembered per view ---------- */
const SORTS={
 triage:{def:'urgency',opts:[['urgency','Urgency (default)'],['id','ID'],['due','Due / forum date'],['sev','Severity'],['touched','Last touched']]},
 pulse:{def:'pulse',opts:[['pulse','Attention (default)'],['id','ID'],['sev','Severity'],['seen','Last raised'],['first','First raised'],['owner','Owner'],['title','Title']]},
 A:{def:'due',opts:[['due','Due date'],['id','ID'],['title','Title'],['touched','Last touched']]},
 other:{def:'due',opts:[['due','Due date'],['id','ID'],['owner','Owner'],['crit','Critical first'],['title','Title'],['touched','Last touched']]},
 watch:{def:'id',opts:[['id','ID'],['sev','Severity'],['tier','Tier (Active first)'],['title','Title'],['touched','Last touched']]},
 decision:{def:'id',opts:[['id','ID'],['tier','Tier (Radar first)'],['due','Forum date'],['owner','Owner'],['title','Title'],['touched','Last touched']]},
 needs:{def:'id',opts:[['id','ID'],['touched','Last touched']]},
 closed:{def:'closed',opts:[['closed','Date disposed'],['id','ID'],['title','Title']]},
};
const SORTDESC={urgency:'grouped by urgency; within each group by due date, risks by severity, ties by ID',pulse:'live first, then stuck, then severity, then most recently raised'};
let SORT={};try{SORT=JSON.parse(localStorage.getItem('eos.sort')||'{}')}catch(e){SORT={}}
function defDir(k){return (k==='touched'||k==='closed'||k==='seen'||k==='first')?-1:1}
function sortOf(v){const c=SORTS[v],s=SORT[v];if(!c)return {k:'id',dir:1};return s&&c.opts.some(o=>o[0]===s.k)?s:{k:c.def,dir:defDir(c.def)}}
function saveSort(){try{localStorage.setItem('eos.sort',JSON.stringify(SORT))}catch(e){}}
const idKey=s=>{const m=String(s||'').match(/^([A-Za-z]+)-?(\d*)(.*)$/);return m?[m[1].toUpperCase(),m[2]?+m[2]:-1,m[3]]:[String(s||''),-1,'']};
function cmpId(x,y){const a=idKey(x.id),b=idKey(y.id);return a[0].localeCompare(b[0])||(a[1]-b[1])||a[2].localeCompare(b[2])}
const SEVR={'high':0,'medium-high':1,'medium':2,'low':3};
const sevr=i=>SEVR[String(i.severity||'').toLowerCase()]??9;
const dkey=i=>i.due||i.forum_date||'';
function blankLast(a,b,dir){a=String(a||'');b=String(b||'');if(!a&&!b)return 0;if(!a)return 1;if(!b)return -1;return a.localeCompare(b)*dir}
function cmpBy(k,dir){
  return (x,y)=>{let r=0;
    if(k==='id')r=cmpId(x,y)*dir;
    else if(k==='title')r=String(x.title||'').localeCompare(String(y.title||''))*dir;
    else if(k==='sev')r=(sevr(x)-sevr(y))*dir;
    else if(k==='due')r=blankLast(dkey(x),dkey(y),dir);
    else if(k==='touched')r=blankLast(x.last_touched,y.last_touched,dir);
    else if(k==='closed')r=blankLast(x.closed_date,y.closed_date,dir);
    else if(k==='seen')r=blankLast(x.last_seen,y.last_seen,dir);
    else if(k==='first')r=blankLast(x.first_seen,y.first_seen,dir);
    else if(k==='owner')r=blankLast(x.owner,y.owner,dir);
    else if(k==='crit')r=((y.critical?1:0)-(x.critical?1:0))*dir;
    else if(k==='tier'){const t={active:0,radar:0,passive:1,backlog:1,retired:2};r=((t[x.tier]??3)-(t[y.tier]??3))*dir}
    return r||cmpId(x,y)}}
function sortBar(v,n){const c=SORTS[v];if(!c)return '';const s=sortOf(v);
  const fixed=!!SORTDESC[s.k];const dated=['due','touched','closed','seen','first','owner'].includes(s.k);
  const desc=SORTDESC[s.k]||((s.dir>0?'ascending':'descending')+(dated?', blanks last':'')+', ties by ID');
  return `<div class="sortbar"><label>Sort<select id="sortSel" aria-label="Sort by">${c.opts.map(o=>`<option value="${o[0]}"${o[0]===s.k?' selected':''}>${o[1]}</option>`).join('')}</select></label>${fixed?'':`<button type="button" class="btn sm" id="sortDir" aria-label="Reverse the order">${s.dir>0?'↑ Ascending':'↓ Descending'}</button>`}<span class="sd">${n} shown · ${esc(desc)}</span></div>`}
document.addEventListener('change',e=>{if(e.target&&e.target.id==='sortSel'){SORT[VIEW]={k:e.target.value,dir:defDir(e.target.value)};saveSort();render()}});
function filtered(){
  /* membership uses the item as it was before this session's edits, so a row you just closed stays put (struck through) until you switch views */
  let a=ITEMS.filter(i=>inView(BASE[i.id]||i,VIEW));
  if(Q){const q=Q.toLowerCase();a=a.filter(i=>[i.id,i.title,i.owner,i.counterparty,i.next_action,i.body,i.forum,i.critical?'critical':'',i.severity,i.type].join(' ').toLowerCase().includes(q))}
  const kr={action:0,watch:1,decision:2};const rr={triage:0,A:1,other:2};
  const so=sortOf(VIEW);
  if(so.k!=='urgency'){a.sort(cmpBy(so.k,so.dir));return a}
  a.sort((x,y)=>(x.needs_triage?-1:0)-(y.needs_triage?-1:0)||(kr[x.kind]-kr[y.kind])||((rr[x.register]??3)-(rr[y.register]??3))||((y.critical?1:0)-(x.critical?1:0))||dueKey(x).localeCompare(dueKey(y))||(x.last_touched||'').localeCompare(y.last_touched||''));
  return a;
}
function groups(a){
  if(VIEW!=='triage'){const l=Q?'Search results':VIEWS.find(v=>v[0]===VIEW)[1];return [{k:'',l,rows:a}]}
  const g={tri:[],over:[],week:[],later:[],nodate:[],watch:[]};
  for(const i of a){
    if(i.needs_triage){g.tri.push(i);continue}
    if(i.kind==='watch'){g.watch.push(i);continue}
    const d=i.due||i.forum_date;if(!d){g.nodate.push(i);continue}
    const n=days(d);(n<0?g.over:n<7?g.week:g.later).push(i);
  }
  const so=sortOf('triage'),cf=so.k==='urgency'?null:cmpBy(so.k,so.dir);
  for(const k of ['over','week','later'])g[k].sort(cf||((x,y)=>dueKey(x).localeCompare(dueKey(y))||cmpId(x,y)));
  if(cf){g.tri.sort(cf);g.nodate.sort(cf)}
  g.watch.sort(cf||((x,y)=>(sevr(x)-sevr(y))||cmpId(x,y)));
  return [{k:'tri',l:'New · needs triage',rows:g.tri},{k:'over',l:'Overdue',rows:g.over},{k:'week',l:'Due this week',rows:g.week},{k:'',l:'Later',rows:g.later},{k:'',l:'No date',rows:g.nodate},{k:'watch',l:'Watch · active risks',rows:g.watch}].filter(x=>x.rows.length);
}
function tags(i){let t='';
  if(i.needs_triage)t+='<span class="t-tri">Needs triage</span>';
  if(i.critical)t+='<span class="t-crit">Critical</span>';
  if(i.kind==='watch'&&i.severity)t+=`<span class="t-sev ${esc(i.severity.toLowerCase())}">${esc(i.severity)}</span>`;
  return t}
function who(i){
  if(i.kind==='action')return i.register==='A'?'Mine':i.register==='triage'?'New':`${i.type||'Other-owned'}${i.owner?' · '+i.owner:''}`;
  if(i.kind==='watch')return [cap(i.tier),i.trend?'trend '+i.trend:'',i.evidence_basis].filter(Boolean).join(' · ');
  return [i.forum,i.owner].filter(Boolean).join(' · ');
}
function context(i){
  if(i.next_action)return {t:plain(i.next_action),ctx:false};
  if(i.kind==='decision'&&i.status)return {t:i.status,ctx:true};
  const b=(i.body||'').split(/\n+/).map(l=>l.replace(/^##\s.*$/,'').replace(/^\d{4}-\d{2}-\d{2} \([^)]+\):\s*/,'').replace(/^-\s*/,'').trim()).filter(Boolean)[0]||'';
  return {t:plain(b),ctx:true};
}
function statusOpts(i){return i.kind==='pulse'?['status',['live','resolved'],i.status||'live']:i.kind==='action'?['status',['open','closed','dropped'],i.status]:i.kind==='watch'?['tier',['active','passive','retired'],i.tier]:['tier',['radar','backlog'],i.tier]}
function seg(i,lg){const[k,opts,cur]=statusOpts(i);
  return `<div class="seg${lg?' lg':''}" role="group" aria-label="Status">${opts.map(o=>`<button type="button" class="${o===cur?'on':''}" aria-pressed="${o===cur}" data-id="${esc(i.id)}" data-k="${k}" data-val="${o}">${cap(o)}</button>`).join('')}</div>`}
function dueInfo(i){
  const due=i.due||i.forum_date||'';const open=isOpen(i);if(!due)return {due:'',rel:open?'':cap(i.status==='open'?i.tier:i.status),cls:''};
  const n=days(due);let rel=n<0?`${-n} day${n===-1?'':'s'} late`:n===0?'Today':n<7?WD[new Date(dn(due)).getUTCDay()]:`In ${n} days`;
  if(!open)rel=cap(i.kind==='action'?i.status:i.tier);
  return {due,rel,n,cls:open&&n<0?'late':open&&n===0?'today':''};
}
function rowHtml(i){
  const d=dueInfo(i);const c=context(i);
  return `<div class="row${SEL===i.id?' sel':''}${isOpen(i)?'':' done'}" data-id="${esc(i.id)}">
    <div class="id">${esc(i.id)}</div>
    <div class="body"><div class="title">${esc(i.title)}</div>${c.t?`<div class="next${c.ctx?' ctx':''}">${esc(c.t)}</div>`:''}<div class="meta">${tags(i)}<span>${esc(who(i))}</span></div></div>
    <div class="due ${d.cls}"><b>${fmt(d.due)}</b><span>${d.rel}</span></div>
    ${seg(i)}
  </div>`}
function render(){
  const a=filtered();const open=ITEMS.filter(isOpen);
  const A=open.filter(i=>i.kind==='action'&&i.register==='A').length,W=open.filter(i=>i.kind==='watch'&&i.tier==='active').length,D=open.filter(i=>i.kind==='decision'&&i.tier==='radar').length,N=ITEMS.filter(i=>i.needs_triage).length;
  $('#views').innerHTML=VIEWS.map(([v,l])=>`<button class="tab${v===VIEW?' on':''}" data-v="${v}"${v===VIEW?' aria-current="page"':''}>${l}${v==='briefs'?(BRIEFS.some(b=>b.date===TODAY)?'<span class="nd" title="Today\u2019s brief is in"></span>':''):v==='products'?(PRODS?`<span class="n">${PRODS.products.length}</span>`:''):`<span class="n">${ITEMS.filter(i=>inView(i,v)).length}</span>`}</button>`).join('');
  const m=(l,s,n,c)=>`<div class="cap${n>c?' over':''}"><span class="l">${l}</span><span class="s">${s}</span><span class="bar"><i style="width:${Math.min(100,n/c*100)}%"></i></span><b>${n}/${c}</b></div>`;
  const dt=new Date(dn(TODAY));
  $('#meta').innerHTML=m('Register A','A',A,15)+m('Watch active','Watch',W,20)+m('Radar','Radar',D,20)+pulseCaps()+`<div class="cap"><span class="dot"></span><span class="l">Needs triage</span><span class="s">Triage</span><b>${N}</b></div><span class="today">${VIEW==='briefs'?BRIEFS.length+' briefs':a.length+' shown'} · ${['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][dt.getUTCDay()]}, ${fmt(TODAY)}</span>`;
  $('#logBtn').innerHTML='Changes'+(SESSION.length?`<span class="badge">${SESSION.length}</span>`:'');
  if(VIEW==='briefs'){$('#list').innerHTML=briefsHtml();const hd=document.querySelector('header');if(hd)document.documentElement.style.setProperty('--hdrH',hd.offsetHeight+'px');return}
  if(VIEW==='pulse'){$('#list').innerHTML=pulseHtml();const hd=document.querySelector('header');if(hd)document.documentElement.style.setProperty('--hdrH',hd.offsetHeight+'px');return}
  if(VIEW==='products'){$('#list').innerHTML=productsHtml();const hd=document.querySelector('header');if(hd)document.documentElement.style.setProperty('--hdrH',hd.offsetHeight+'px');return}
  const gs=groups(a);
  $('#list').innerHTML=sortBar(VIEW,a.length)+(gs.map(g=>{let rows=g.rows,more='';
    if(g.k==='watch'&&rows.length>3){more=`<button class="more" data-more>${MOREW?'Show fewer':'Show '+(rows.length-3)+' more risks'}</button>`;if(!MOREW)rows=rows.slice(0,3)}
    return `<section class="group"><h2 class="ghead ${g.k}">${g.l}<span class="n">${g.rows.length}</span></h2>${rows.map(rowHtml).join('')}${more}</section>`}).join('')||'<div class="empty">Nothing here.</div>');
}
document.addEventListener('click',e=>{
  if(e.target.closest('[data-sclose]')){closeSheet();return}
  if(e.target.closest('[data-snote]')){SHEETNOTE=!SHEETNOTE;openSheet(SHEET);return}
  if(e.target.closest('[data-sfull]')){const id=SHEET;closeSheet();openDrawer(id);return}
  const so=e.target.closest('[data-sopen]');if(so){e.preventDefault();closeSheet();closeMeet();openDrawer(so.dataset.sopen);return}
  if(e.target.closest('[data-mclose]')){closeMeet();return}
  if(e.target.closest('[data-mcopy]')){copyAgenda();return}
  if(e.target.closest('[data-mfs]')){const el=$('#pv-meet');if(document.fullscreenElement)document.exitFullscreen();else if(el&&el.requestFullscreen)el.requestFullscreen().catch(()=>toast('Full screen is not available here'));else toast('Full screen is not available here');return}
  const mo=e.target.closest('[data-mopen]');if(mo){closeMeet();openDrawer(mo.dataset.mopen);return}
  if(e.target.closest('[data-pplall]')){PPLALL=!PPLALL;render();return}
  const s=e.target.closest('.seg button');if(s){e.stopPropagation();const i=ITEMS.find(x=>x.id===s.dataset.id);if(i&&i[s.dataset.k]!==s.dataset.val)patch(s.dataset.id,{[s.dataset.k]:s.dataset.val},'');return}
  if(e.target.closest('[data-cprompts]')){openPrompts();return}
  if(e.target.closest('[data-review]')){openReview();return}
  if(e.target.closest('[data-rvup]')){uploadReview();return}
  if(e.target.closest('[data-rvapply]')){applyReview();return}
  const cpy=e.target.closest('[data-cpy]');if(cpy){copyPrompt(cpy.dataset.cpy);return}
  const tc=e.target.closest('[data-toc]');if(tc){e.preventDefault();jumpSec(tc.dataset.toc);return}
  const bi=e.target.closest('[data-brief]');if(bi){openBrief(bi.dataset.brief,'list');return}
  if(e.target.closest('[data-bback]')){BREAD=false;render();scrollTo(0,0);return}
  const pw=e.target.closest('[data-pwin]');if(pw){PWIN=+pw.dataset.pwin;try{localStorage.setItem('eos.products.win',String(PWIN))}catch(x){}loadProducts('window').then(render);return}
  const pl=e.target.closest('[data-plive]');if(pl){setLive(pl.dataset.plive,pl.dataset.to==='1');return}
  const pm=e.target.closest('[data-pmore]');if(pm){PMORE[pm.dataset.pmore]=!PMORE[pm.dataset.pmore];render();return}
  if(e.target.closest('[data-phidden]')){PHID=!PHID;render();return}
  const pt=e.target.closest('.tab[data-v]');if(pt&&pt.dataset.v==='products'){VIEW='products';loadProducts('tab').then(render);scrollTo(0,0);return}
  const cb=e.target.closest('.tab[data-v]');if(cb&&cb.dataset.v==='briefs'){VIEW='briefs';loadBriefs().then(()=>{if(!BRIEF&&BRIEFS.length)openBrief(BRIEFS[0].name,'tab');else render()});scrollTo(0,0);return}
  const c=e.target.closest('.tab[data-v]');if(c){VIEW=c.dataset.v;MOREW=false;for(const k in BASE)delete BASE[k];render();scrollTo(0,0);return}
  if(e.target.closest('[data-more]')){MOREW=!MOREW;render();return}
  const es=e.target.closest('[data-esc]');if(es){e.stopPropagation();escalateP(es.dataset.id,es.dataset.esc);return}
  const ag=e.target.closest('[data-agenda]');if(ag){e.stopPropagation();openAgenda(ag.dataset.agenda);return}
  const op=e.target.closest('[data-open]');if(op){e.preventDefault();openDrawer(op.dataset.open);return}
  if(e.target.closest('[data-pclear]')){PF={};render();return}
  if(e.target.closest('#sortDir')){const so=sortOf(VIEW);SORT[VIEW]={k:so.k,dir:-so.dir};saveSort();render();return}
  if(e.target.closest('[data-pall]')){PALL=!PALL;render();return}
  const pinb=e.target.closest('[data-pin]');if(pinb){e.stopPropagation();pinAccount(pinb.dataset.pin);return}
  if(e.target.closest('[data-callall]')){CALLALL=!CALLALL;render();return}
  if(e.target.closest('[data-issall]')){ISSALL=!ISSALL;render();return}
  if(e.target.closest('[data-kopen]')){KOPEN=!KOPEN;render();return}
  if(e.target.closest('[data-popen]')){POPEN=!POPEN;render();return}
  const tko=e.target.closest('[data-trk]');if(tko){TRKOPEN[tko.dataset.trk]=!TRKOPEN[tko.dataset.trk];render();return}
  const gd=e.target.closest('[data-guide]');if(gd){openHelp(gd.dataset.guide||'Pulse');return}
  if(e.target.closest('[data-kall]')){KALL=!KALL;render();return}
  if(e.target.closest('[data-pv]')){VIEW='pulse';PF={};render();scrollTo(0,0);return}
  const pf=e.target.closest('[data-pf]');if(pf){const k=pf.dataset.pf,v=pf.dataset.val;const fromCap=!!pf.closest('#meta');PF=(!fromCap&&PF[k]===v)?{}:{[k]:v};VIEW='pulse';render();if(fromCap)scrollTo(0,0);if(PF[k]){const c=document.getElementById('pv-issues');if(c){c.scrollIntoView({block:'start'});scrollBy(0,-110)}}return}
  const pi=e.target.closest('[data-pi]');if(pi){if(PHONE())openSheet(pi.dataset.pi);else openDrawer(pi.dataset.pi);return}
  const kr=e.target.closest('[data-kid]');if(kr){openDrawer(kr.dataset.kid);return}
  const r=e.target.closest('.row[data-id]');if(r){openDrawer(r.dataset.id)}
});
$('#q').addEventListener('input',e=>{Q=e.target.value.trim();render()});
$('#searchBtn').onclick=()=>{document.body.classList.toggle('searching');if(document.body.classList.contains('searching'))$('#q').focus();else{$('#q').value='';Q='';render()}};
async function patch(id,p,note){
  const k=ITEMS.findIndex(x=>x.id===id);if(k<0)return null;
  if(!BASE[id])BASE[id]=ITEMS[k];
  const r=await fetch('/api/items/'+encodeURIComponent(id),{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({patch:p,note})});
  if(!r.ok){toast('Save failed · '+id);return null}
  const j=await r.json();
  ITEMS[k]=j;
  if(j.kind==='pulse')fetch('/api/pulse').then(r=>r.json()).then(p=>{PULSE=p;render()}).catch(()=>{});
  const what=[...Object.keys(p).filter(f=>String(p[f])!==String(BASE[id][f]??'')||f==='status'||f==='tier').map(f=>(f==='status'||f==='tier')?cap(p[f]):f.replace('_',' ')),note&&note.trim()?'note':''].filter(Boolean).join(', ')||'saved';
  SESSION.unshift({id,what,t:new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})});
  SAVED[id]=SESSION[0];
  toast('Saved · '+id+' · '+what);render();
  if(DRAWER==='item'&&SEL===id)openDrawer(id);
  return j;
}
/* ---------- pulse (2026-10-16) ---------- */
const BANDCLS={green:'b-green',amber:'b-amber',red:'b-red',neutral:'b-neutral'};
/* Trend (2026-10-19): the headline is how the team-raised load moved in 7 days, not a score out of 100. */
function th(x){if(x.delta==null)return {big:String(x.load),unit:'load',word:x.label||'Baseline',note:x.trend_from?'7-day trend from '+fmt(x.trend_from):''};
  return {big:(x.delta>0?'↑ +'+x.delta:x.delta<0?'↓ −'+Math.abs(x.delta):'→ 0'),unit:'in 7 days',word:x.label,note:'load '+x.load+(x.load_7!=null?', was '+x.load_7:'')}}
function spark(x,w,h){const s=x.series||[];w=w||120;h=h||26;if(s.length<2)return '';const mx=Math.max(...s,20),st=w/(s.length-1);
  const pts=s.map((v,i)=>`${(i*st).toFixed(1)},${(h-2-(v/mx)*(h-4)).toFixed(1)}`).join(' ');
  return `<svg class="spk ${BANDCLS[x.band]||''}" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" role="img" aria-label="Team-raised load, ${s.length} days from ${fmt(x.series_start)}: ${s.join(', ')}"><polyline points="${pts}" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/><circle cx="${((s.length-1)*st).toFixed(1)}" cy="${(h-2-(s[s.length-1]/mx)*(h-4)).toFixed(1)}" r="2.6" fill="currentColor"/></svg>`}
const fname=k=>((PULSE&&PULSE.forums)||[]).find(f=>f.key===k)?.name||k||'Unassigned forum';
function pulseCaps(){if(!PULSE)return '';const d=(PULSE.health||[]).find(h=>h.pinned);const c=(PULSE.candidates||[]).length;
  /* C10: the pinned account (a setting, Dell by default), with score and band word, on every tab */
  return (d?`<div class="cap" data-pf="account" data-val="${esc(d.account)}" title="Pinned account">${PIN_SVG(1)}<span>${esc(d.account)}</span><b class="hs ${BANDCLS[d.band]}">${esc(th(d).big)}${d.delta==null?' load':''}</b><b class="hs ${BANDCLS[d.band]}">· ${esc(d.label)}</b></div>`:'')+
   `<div class="cap" data-pv="1"><span class="l">Pulse calls</span><span class="s">Calls</span><b${c?' class="hs b-amber"':''}>${c}</b></div>`}
function ptags(i){let t='';
  if(i.severity)t+=`<span class="t-sev ${esc(String(i.severity).toLowerCase())}">${esc(i.severity)}</span>`;
  if(i.customer_visible)t+='<span class="t-cv">Customer-visible</span>';
  if(i._stuck)t+='<span class="t-stuck">Stuck</span>';
  if(i.escalated_to)t+=`<span class="t-esc">Escalated · ${esc(i.escalated_to)}</span>`;else if(i._candidate)t+='<span class="t-esc">Needs your call</span>';
  if(i._state!=='live')t+=`<span>${cap(i._state)}</span>`;
  return t}
/* Phase 2, C14: issue rows on a shared grid (48px · body · 236px actions). Badges are additive; the drawer is unchanged. */
const isNewI=i=>dn(String(i.first_seen||'1970-01-01').slice(0,10))>=dn(TODAY)-7*864e5;
const stOf=i=>i.escalated_to?'esc':i.escalation==='declined'?'left':'open';
function ibadges(i,withState){let t='';const sv=String(i.severity||'');
  if(sv)t+=`<span class="pv-b sev-${esc(sv.toLowerCase().replace(/[^a-z]/g,''))}">${esc(sv)}</span>`;
  if(i.customer_visible)t+='<span class="pv-b">Customer-visible</span>';
  if(i._stuck)t+=`<span class="pv-b stuck">Stuck · raised since ${fmt(i.first_seen)}</span>`;
  if(isNewI(i)&&i._state==='live')t+='<span class="pv-b new">New</span>';
  if(i.escalated_to)t+=`<span class="pv-b esc">Escalated · ${esc(i.escalated_to)}</span>`;
  else if(i._candidate)t+='<span class="pv-b call">Needs your call</span>';
  if(withState&&!i.escalated_to&&i.escalation==='declined')t+='<span class="pv-b">Left with team</span>';
  if(i._state!=='live')t+=`<span class="pv-b">${cap(i._state)}</span>`;
  return t}
function iacts(i){if(i._state!=='live')return '';const s=stOf(i),id=esc(i.id);
  if(s==='esc')return `<a href="#" class="pv-wl" data-open="${esc(i.escalated_to)}">Open Watch ${esc(i.escalated_to)}</a>`;
  if(s==='left')return `<span class="lw">Left with team</span><button type="button" class="btn" data-esc="escalate" data-id="${id}">Escalate</button>`;
  return `<button type="button" class="btn primary" data-esc="escalate" data-id="${id}">Escalate</button><button type="button" class="btn" data-esc="decline" data-id="${id}">Leave with team</button>`}
function prow(i){const ph=PHONE(),id=esc(i.id),cls=i._state==='live'?'':i._state==='quiet'?' dim':' done';
  const own=i.owner?'Owner: '+esc(i.owner):'<b class="no">No owner named</b>';
  const meta=[own,esc(i.account||'No account'),ph?'':esc(fname(i.forum)),(ph?'':'last raised ')+fmt(i.last_seen||i.first_seen)].filter(Boolean).join(' · ');
  const nx=!ph&&i.next_action?`<div class="nx">Next: ${esc(plain(i.next_action))}</div>`:'';
  return `<div class="pv-ir${SEL===i.id?' sel':''}${cls}" data-pi="${id}"><div class="id">${id}</div>
   <div class="bd"><button type="button" class="ttl" data-pi="${id}">${ph?`<span class="iid">${id}</span>`:''}${esc(i.title)}</button><div class="bdg">${ibadges(i)}</div><div class="ow">${meta}</div>${nx}</div>
   <div class="ac">${iacts(i)}</div></div>`}
/* C14 footer: a real toggle with the quiet IDs named */
function allToggle(scope){const q=scope.filter(i=>i._state==='quiet'),r=scope.filter(i=>i._state!=='live'&&i._state!=='quiet');
  if(!q.length&&!r.length&&!PALL)return '';
  const what=[q.length?`${q.length} quiet: ${q.map(i=>i.id).join(', ')}`:'',r.length?`${r.length} resolved or dropped`:''].filter(Boolean).join('; ');
  return `<button type="button" class="pv-chk" role="checkbox" aria-checked="${PALL}" data-pall><span class="bx" aria-hidden="true">${PALL?'✓':''}</span>Include quiet and resolved (${esc(what)})</button>`}
function sortMini(n){const c=SORTS.pulse,s=sortOf('pulse');
  const lab=s.k==='pulse'?'Sorted by attention: stuck, severity, customer-visible, most recent':`${n} shown · `+(SORTDESC[s.k]||((s.dir>0?'ascending':'descending')+', ties by ID'));
  return `<span class="sub pv-sl">${esc(lab)}</span><span class="pv-srt"><select id="sortSel" aria-label="Sort live issues">${c.opts.map(o=>`<option value="${o[0]}"${o[0]===s.k?' selected':''}>${o[0]==='pulse'?'Attention':o[1]}</option>`).join('')}</select>${s.k==='pulse'||SORTDESC[s.k]?'':`<button type="button" class="btn sm" id="sortDir" aria-label="Reverse the order">${s.dir>0?'↑':'↓'}</button>`}</span>`}

/* Phase 2, C16: phone preview sheet. Desktop keeps the drawer. */
let SHEET=null,SHEETNOTE=false;
function openSheet(id){const i=ITEMS.find(x=>x.id===id);if(!i)return;SHEET=id;
  let el=$('#pv-sheet');if(!el){el=document.createElement('div');el.id='pv-sheet';document.body.appendChild(el)}
  const ppl=(i.people||[]).filter(p=>p!==i.owner);
  const links=(i.links||[]).map(l=>`<a href="#" data-sopen="${esc(l)}">${esc(l)}</a>`).join(' · ');
  const s=stOf(i);
  const act=i._state!=='live'?'':s==='esc'?`<button type="button" class="btn primary" data-sopen="${esc(i.escalated_to)}">Open Watch ${esc(i.escalated_to)}</button>`:s==='left'?`<button type="button" class="btn primary" data-esc="escalate" data-id="${esc(i.id)}">Escalate</button>`:`<button type="button" class="btn primary" data-esc="escalate" data-id="${esc(i.id)}">Escalate</button><button type="button" class="btn" data-esc="decline" data-id="${esc(i.id)}">Leave with team</button>`;
  el.innerHTML=`<div class="sc" data-sclose></div><div class="sh" role="dialog" aria-modal="true" aria-label="${esc(i.id)} preview"><div class="grab" aria-hidden="true"></div>
   <div class="l1"><span class="id">${esc(i.id)}</span><span>Pulse issue${i.account?' · '+esc(i.account):''}</span><button type="button" class="pv-lk cl" data-sclose>Close</button></div>
   <h2>${esc(i.title)}</h2><div class="bdg">${ibadges(i,true)}</div>
   ${i.next_action?`<div class="nb"><span>Next action</span>${esc(plain(i.next_action))}</div>`:''}
   <div class="facts"><div><span>Owner</span>${i.owner?esc(i.owner):'<b class="no">No owner named</b>'}</div><div><span>Named in evidence</span>${ppl.length?esc(ppl.join(', ')):'None named'}</div>
   <div><span>Forum</span>${esc(fname(i.forum))}</div><div><span>First and last raised</span>${fmt(i.first_seen)} · ${fmt(i.last_seen||i.first_seen)}</div>
   ${links?`<div class="w"><span>Linked</span>${links}</div>`:''}</div>
   <div class="ft"><div class="b2">${act}<button type="button" class="btn" data-snote>Add a note</button></div>
   ${SHEETNOTE?`<form id="snf" class="snf"><textarea id="snote" placeholder="What happened, what you decided, what Claude should know…"></textarea><button type="submit" class="btn primary">Save note</button></form>`:''}
   <button type="button" class="pv-lk full" data-sfull>Full detail and history</button></div></div>`;
  document.body.classList.add('locked');
  const f=$('#snf');if(f){$('#snote').focus();f.onsubmit=async ev=>{ev.preventDefault();const n=$('#snote').value;if(!n.trim())return;SHEETNOTE=false;await patch(id,{},n);if(SHEET===id)openSheet(id)}}}
function closeSheet(){SHEET=null;SHEETNOTE=false;const el=$('#pv-sheet');if(el)el.remove();if(!DRAWER)document.body.classList.remove('locked')}
/* ---------- Pulse redesign, 2026-10-16 (Claude Design handoff, Phase 1: C1-C13) ---------- */
const PIN_SVG=f=>`<svg class="pinsvg" viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M5.5 1.5h5l-.8 4.2 2.6 2.6v1.2H8.6V14L8 15.2 7.4 14V9.5H3.7V8.3l2.6-2.6z" fill="${f?'currentColor':'none'}" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg>`;
const PHONEQ=matchMedia('(max-width:820px)');const PHONE=()=>PHONEQ.matches;
let CALLALL=false,ISSALL=false,KOPEN=false,POPEN=false;const TRKOPEN={};
const joinAnd=xs=>xs.length<2?(xs[0]||''):xs.slice(0,-1).join(', ')+' and '+xs[xs.length-1];
const TYPEW={customer:'Customer',internal:'Internal',partner:'Partner'};
function evLine(f){if(f.ev_state==='not_heard')return f.last_evidence?`Not heard · last evidence ${fmt(f.last_evidence)}`:'Not heard · no evidence on file';return `Heard ${fmt(f.last_evidence)}`}
function evCount(f){if(f.ev_state==='not_heard')return '<span class="fc dash" aria-label="no evidence">—</span>';if(f.ev_state==='nothing_raised')return '<span class="fc">Nothing raised</span>';
  return `<span class="fc">${[f.live+' live',f.stuck?f.stuck+' stuck':'',f.quiet?f.quiet+' quiet':''].filter(Boolean).join(' · ')}</span>`}
const mk=st=>`<span class="pv-mk ${st==='raised'?'raised':st==='nothing_raised'?'nothing':'nh'}" aria-hidden="true"></span>`;
function verdict(t){if(t.heard>=t.total)return '';if(t.heard<=t.total/2)return 'Mostly not heard: these counts are incomplete.';
  const n=t.not_heard.map(f=>f.name);return n.length<=2?`${joinAnd(n)} not heard; their counts are unknown.`:`${n.length} forums not heard; their counts are unknown.`}
function drivers(c){return [c.live_high_visible?c.live_high_visible+' High customer-visible':'',c.live_high?c.live_high+' High internal':'',c.live_medium?c.live_medium+' Medium':'',c.live_low?c.live_low+' Low':'',c.stuck?c.stuck+' stuck':'',c.quiet?c.quiet+' quiet':'',c.candidate?c.candidate+' open call'+(c.candidate>1?'s':''):'',c.at_your_level?c.at_your_level+' register item'+(c.at_your_level>1?'s':''):''].filter(Boolean).join(' · ')}
function ptsBar(x,h){const w=v=>Math.min(100,v/60*100);const t=w(x.teams_points),r=Math.min(100-t,w(x.registers_points));
  return `<div class="pv-bar" style="height:${h||10}px" role="img" aria-label="Points lost: teams raised ${x.teams_points}, your registers ${x.registers_points}"><i class="t" style="width:${t}%"></i><i class="r" style="width:${r}%"></i></div>`}
function teamsCell(x,P){if(x.teams_points>0)return {v:x.teams_points+(x.teams_points===1?' pt':' pts'),n:[x.live?x.live+' live':'',x.quiet?x.quiet+' quiet':'',x.calls?x.calls+' call'+(x.calls>1?'s':''):''].filter(Boolean).join(' · ')};
  const sc=(P.forums||[]).find(f=>f.key==='deployment-scrum');
  if(x.open_project===false)return {v:'No open project',n:''};
  if(x.open_project==null)return {v:'None raised',n:'Project status not set'};
  if(sc&&!sc.evidence_in_window)return {v:'Not heard',n:sc.last_evidence?'Last evidence '+fmt(sc.last_evidence):'No evidence on file',nh:true};
  return {v:'None raised',n:sc?'Heard '+fmt(sc.last_evidence):''}}
function callsCard(P,cs){
  const shown=CALLALL?cs:cs.slice(0,3);
  const tag=t=>`<span class="pv-tag">${esc(t)}</span>`;
  const rows=shown.map(c=>{const i=ITEMS.find(z=>z.id===c.id)||{};
    const bd=[c.severity?`<span class="t-sev ${esc(String(c.severity).toLowerCase())}">${esc(c.severity)}</span>`:'',tag(c.category==='knowledge'?'Knowledge risk':'Issue'),c.account?tag(c.account):'',c.track?tag(TRK(c.track)):(c.forum?tag(fname(c.forum)):'')].join('');
    return `<div class="pv-call"><div class="id">${esc(c.id)}</div><button type="button" class="ttl" data-open="${esc(c.id)}">${esc(c.title)}</button><div class="why">${esc(c.reason_line||c.reason_text)}</div><div class="bd">${bd}</div><div class="acts"><button type="button" class="btn primary" data-esc="escalate" data-id="${esc(c.id)}">Escalate</button><button type="button" class="btn" data-esc="decline" data-id="${esc(c.id)}">Leave with team</button></div></div>`}).join('');
  const more=cs.length>3?`<button type="button" class="pv-lk" data-callall>${CALLALL?'Show fewer':'Show all '+cs.length}</button>`:'';
  const el=(P.escalated_live||[]);
  const foot=el.length?`<div class="pv-foot">Already escalated and still live: ${el.map(e=>`<a href="#" data-open="${esc(e.id)}">${esc(e.id)} ${esc(e.title)}</a> → <a href="#" data-open="${esc(e.watch)}">Watch ${esc(e.watch)}</a>`).join('; ')}</div>`:'';
  return `<section class="pv-card acc pv-calls" aria-label="Needs your call"><h2 class="pv-h acc">Needs your call <span class="pv-badge">${cs.length}</span></h2>${rows||'<p class="pv-empty">Nothing needs your call.</p>'}${more}${foot}</section>`}
function pinnedCard(P){const x=(P.health||[]).find(h=>h.pinned);if(!x)return '';
  const bc=BANDCLS[x.band];
  return `<button type="button" class="pv-card pv-pin" data-pf="account" data-val="${esc(x.account)}" aria-label="${esc(x.account)}, pinned account, ${esc(th(x).big)} ${esc(th(x).unit)}, ${esc(x.label)}. Select to see its items.">
   <span class="l1"><span class="nm">${esc(x.account)}</span><span class="pt">${PIN_SVG(1)} Pinned · ${esc(TYPEW[x.type]||'Customer')}</span><span class="vi">View items ›</span></span>
   <span class="l2"><span class="sc ${bc}">${esc(th(x).big)}</span><span class="of">${esc(th(x).unit)}</span><span class="bw ${bc}">${esc(x.label)}</span></span>
   <span class="pv-spk">${spark(x,260,40)}<span class="pv-spkn">${esc(th(x).note)}${x.series_start?' · since '+fmt(x.series_start):''}</span></span>
   <span class="pv-leg"><span>Teams raised <b>${x.teams_points?x.teams_points+' pts':'none'}</b></span><span>Your registers <b>${x.registers_points?x.registers_points+' pts':'none'}</b></span></span>
   <span class="pv-drv">${esc(drivers(x.components)||'No signals')}</span>
   ${PHONE()?'':'<span class="pv-foot">Pin a different account from Account health below.</span>'}</button>`}
function evidenceCard(P){const e=P.evidence;if(!e)return '';
  const order=[...P.forums].sort((a,b)=>({raised:0,nothing_raised:1,not_heard:2}[a.ev_state]-{raised:0,nothing_raised:1,not_heard:2}[b.ev_state]));
  const strip=`<div class="pv-strip" role="img" aria-label="${e.raised} forums heard with items raised, ${e.nothing_raised} heard with nothing raised, ${e.not_heard} not heard">${order.map(f=>mk(f.ev_state).replace('aria-hidden="true"',`title="${esc(f.name)}: ${esc(evLine(f))}" aria-hidden="true"`)).join('')}</div>`;
  const leg=PHONE()?`<div class="pv-evl ph">${mk('raised')} Raised <b>${e.raised}</b> · ${mk('nothing_raised')} Nothing raised <b>${e.nothing_raised}</b> · ${mk('not_heard')} Not heard <b>${e.not_heard}</b></div>`
    :`<div class="pv-evl"><span>${mk('raised')}Heard, items raised <b>${e.raised}</b></span><span>${mk('nothing_raised')}Heard, nothing raised <b>${e.nothing_raised}</b></span><span>${mk('not_heard')}Not heard <b>${e.not_heard}</b></span></div>`;
  const sil=e.not_heard>e.total/2?'<p class="pv-sil">Silence below mostly means not heard, not all clear.</p>':'';
  const byT=(e.new7_by_track||[]).map(t=>`${esc(t.name.replace(/ governance$/,''))} ${t.new7}`).join(' · ');
  const foot=PHONE()?`<button type="button" class="pv-foot pv-newrow" data-pf="new" data-val="7"><b>${e.new7} new</b> in the last 7 days ›</button>`
    :`<div class="pv-foot"><b>${e.new7} new</b> in the last 7 days${byT?' · '+byT:''} · <button type="button" class="pv-lk" data-pf="new" data-val="7">Show new</button></div>`;
  return `<section class="pv-card pv-ev" aria-label="Evidence this window"><h2 class="pv-h">Evidence this window</h2><div class="hl">Heard from ${e.heard} of ${e.total} forums</div>${strip}${leg}${sil}${foot}</section>`}
function accountsSec(P,fk,fv){
  const ph=PHONE();
  const pinBtn=x=>`<button type="button" class="pinbtn${x.pinned?' on':''}" data-pin="${esc(x.account)}" aria-pressed="${x.pinned}" aria-label="${x.pinned?esc(x.account)+' is pinned to the top':'Pin '+esc(x.account)+' to the top'}">${PIN_SVG(x.pinned)}<span>${x.pinned?'Pinned':'Pin'}</span></button>`;
  const rows=P.health.map(x=>{const bc=BANDCLS[x.band],tc=teamsCell(x,P),on=fk==='account'&&fv===x.account;
    const rg=x.registers_points?{v:x.registers_points+' pts',n:x.components.at_your_level+' item'+(x.components.at_your_level>1?'s':'')}:{v:'None',n:''};
    if(ph){const l3=`${x.teams_points?'Teams '+x.teams_points+(x.teams_points===1?' pt':' pts'):tc.v==='No open project'?'Teams: no open project':tc.v==='Not heard'?'Teams: not heard':'Teams: none raised'} · ${x.registers_points?'Your registers '+x.registers_points+' pts':'Your registers: none'}`;
      return `<div class="pv-arow ph${x.pinned?' pinned':''}${on?' sel':''}"><button type="button" class="af" data-pf="account" data-val="${esc(x.account)}"><span class="a1"><span class="an">${esc(x.account)}</span><b class="as ${bc}">${esc(th(x).big)}</b><span class="of">${esc(th(x).unit)}</span><b class="ab ${bc}">${esc(x.label)}</b></span>${spark(x,200,22)}<span class="a3">${esc(l3)}</span></button>${pinBtn(x)}</div>`}
    return `<div class="pv-arow${x.pinned?' pinned':''}${on?' sel':''}"><button type="button" class="af" data-pf="account" data-val="${esc(x.account)}">
      <span class="c-ac"><span class="an">${esc(x.account)}</span> <span class="at">${esc(TYPEW[x.type]||'Customer')}</span></span>
      <span class="c-sc"><b class="as ${bc}">${esc(th(x).big)}</b><span class="of"> ${esc(th(x).unit)}</span> <b class="ab ${bc}">${esc(x.label)}</b></span>
      <span class="c-bar">${spark(x,170,26)}</span>
      <span class="c-n"><b${tc.nh?' class="nhv"':''}>${tc.nh?mk('not_heard'):''}${esc(tc.v)}</b><small>${esc(tc.n)}</small></span>
      <span class="c-n"><b>${esc(rg.v)}</b><small>${esc(rg.n)}</small></span>
      <span class="c-drv">${esc(drivers(Object.assign({},x.components,{at_your_level:0}))||(x.registers_points?'Register items only':''))}</span>
      <span class="c-ch" aria-hidden="true">›</span></button>${pinBtn(x)}</div>`}).join('');
  const hd=ph?'':`<div class="pv-arow hd" aria-hidden="true"><span class="af"><span>Account</span><span>7-day trend</span><span>Team load, daily</span><span>Teams raised</span><span>Your registers</span><span class="c-drv">What drives it</span><span></span></span><span class="c-pinh">Pin to top</span></div>`;
  const q=(P.quiet_accounts||[]).length?`No signals this window: ${esc(P.quiet_accounts.join(', '))}. `:'';
  const ua=(P.unattributed||[]).length?`<div>Not scored because it names more than one account: ${P.unattributed.map(u=>`<a href="#" data-open="${esc(u.id)}">${esc(u.id)}</a> (${esc(u.accounts.join(', '))})`).join('; ')}. Set its account to count it once.</div>`:'';
  return `<section class="group pv-ah"><h2 class="ghead">Account health${ph?'':'<span class="sub">7-day trend in the load of open issues teams raised · load also counts your register items · select a row to filter · pin one account to the top</span>'}</h2>${hd}${rows}
    <div class="pv-afoot"><div>${q}The line is the daily team-raised load since forum-by-forum capture began; the 7-day trend starts ${P.health&&P.health[0]&&P.health[0].trend_from?fmt(P.health[0].trend_from):'after a week of history'}. Worsening or Improving means a move of at least 5 points and 15%. Friction from evidence, not customer sentiment. <button type="button" class="pv-lk" data-guide="How load and trend are calculated">How issues are weighted</button></div>${ua}</div></section>`}
function govSec(P,fk,fv){const ph=PHONE();
  const tr=(P.tracks||[]).map(t=>{const fs=t.forums.map(k=>P.forums.find(f=>f.key===k)).filter(Boolean).sort((a,b)=>({raised:0,nothing_raised:1,not_heard:2}[a.ev_state]-{raised:0,nothing_raised:1,not_heard:2}[b.ev_state]));
    const cnt=[t.live+' live',t.new7+' new',t.stuck+' stuck',t.candidates+' call'+(t.candidates===1?'':'s'),t.knowledge?t.knowledge+' knowledge risk'+(t.knowledge>1?'s':''):''].filter(Boolean).join(' · ');
    const v=verdict(t);const box=`<div class="pv-hbox"><b>Heard from ${t.heard} of ${t.total} forums</b>${v?`<div class="v">${esc(v)}</div>`:''}</div>`;
    const frows=fs.map(f=>`<button type="button" class="pv-fr${fk==='forum'&&fv===f.key?' on':''}" data-pf="forum" data-val="${esc(f.key)}">${mk(f.ev_state)}<span class="fn">${esc(f.name)}<span class="fs">${esc(evLine(f))}</span></span>${evCount(f)}</button>`).join('');
    const open=!ph||TRKOPEN[t.key];
    return `<div class="pv-trk${fk==='track'&&fv===t.key?' on':''}"><div class="r1"><div class="tt"><button type="button" class="tn" data-pf="track" data-val="${esc(t.key)}">${esc(t.name)}</button><div class="ld">With ${esc(joinAnd(t.leads||[]))}</div></div>${ph?'':`<button type="button" class="btn sm" data-agenda="track:${esc(t.key)}">Open agenda</button>`}</div>
      <div class="cn">${esc(cnt)}</div>${box}${ph?`<div class="pv-2b"><button type="button" class="btn" data-agenda="track:${esc(t.key)}">Open agenda</button><button type="button" class="btn" data-trk="${esc(t.key)}" aria-expanded="${!!TRKOPEN[t.key]}">Forums (${fs.length})</button></div>`:''}${open?`<div class="pv-frs">${frows}</div>`:''}</div>`}).join('');
  return `<section class="group pv-gov"><h2 class="ghead">Your weekly governance${ph?'':'<span class="sub">Select a forum to filter</span>'}</h2>${tr}</section>`}
function pulseHtml(){
  if(!PULSE)return '<div class="empty">The Pulse did not load. Restart the EOS server so it picks up the new version.</div>';
  const P=PULSE,ph=PHONE(),all=ITEMS.filter(i=>i.kind==='pulse'&&i.category!=='knowledge'),know=ITEMS.filter(i=>i.kind==='pulse'&&i.category==='knowledge');
  const fk=Object.keys(PF)[0],fv=fk?PF[fk]:null;
  const trk=fk==='track'?((P.tracks||[]).find(t=>t.key===fv)||{forums:[]}):null;
  const match=i=>!fk||(fk==='account'?i.account===fv:fk==='forum'?i.forum===fv:fk==='track'?trk.forums.includes(i.forum):fk==='new'?isNewI(i):(i._people||[]).includes(fv));
  const scope=all.filter(match);
  let a=scope.filter(i=>PALL||i._state==='live');
  if(Q){const q=Q.toLowerCase();a=a.filter(i=>[i.id,i.title,i.owner,i.account,i.body,(i.people||[]).join(' ')].join(' ').toLowerCase().includes(q))}
  const sv={high:0,mediumhigh:0.5,medium:1,low:2},st={live:0,quiet:1,resolved:2,dropped:3};
  const svk=i=>sv[String(i.severity||'').toLowerCase().replace(/[^a-z]/g,'')]??3;
  const pso=sortOf('pulse');
  /* attention: state, stuck, severity, customer-visible, most recent (C14 head states this order) */
  if(pso.k!=='pulse')a.sort(cmpBy(pso.k,pso.dir));else a.sort((x,y)=>(st[x._state]-st[y._state])||((y._stuck?1:0)-(x._stuck?1:0))||(svk(x)-svk(y))||((y.customer_visible?1:0)-(x.customer_visible?1:0))||String(y.last_seen||'').localeCompare(String(x.last_seen||''))||cmpId(x,y));
  const cs=P.candidates.filter(c=>{const i=ITEMS.find(z=>z.id===c.id);if(!i)return false;if(i.category==='knowledge')return !fk||fk==='new'||(fk==='track'&&i.track===fv)||(fk==='person'&&i.holder===fv)||(fk==='account'&&i.account===fv);return match(i)});
  let h=`<div class="pv"><div class="pv-title"><h2>Pulse</h2><p>Rolling ${P.window.days} days, ${fmt(P.window.start)} to ${fmt(P.window.end)}. What your team-governed forums are carrying. The teams own the work; escalate only what needs you.</p><button type="button" class="btn" data-cprompts>Copilot prompts</button><button type="button" class="btn" data-review>Weekly review</button><button type="button" class="pv-lk" data-guide>How to read this page</button></div>`;
  h+=`<div class="pv-today">${callsCard(P,cs)}${pinnedCard(P)}${evidenceCard(P)}</div>`;
  h+=accountsSec(P,fk,fv);
  /* C15: the filter chip is sticky under the header strip */
  const fname2=fk==='forum'?fname(fv):fk==='track'?(trk.name||fv):fk==='new'?'new in the last 7 days':fv;
  let L=fk?`<div class="chips pv-chip" id="pv-issues"><span class="chip">Showing ${fk==='new'?'':esc(fk)+': '}<b>${esc(fname2)}</b></span><button type="button" class="chip x" data-pclear>Clear</button></div>`:'<span id="pv-issues"></span>';
  const lim=rows=>ph&&!ISSALL&&rows.length>4?rows.slice(0,4):rows;
  const showAll=rows=>ph&&rows.length>4?`<button type="button" class="more" data-issall>${ISSALL?'Show fewer':'Show all '+rows.length+' '+(PALL?'issues':'live issues')}</button>`:'';
  const sec=(t,rows,note,ft,hd)=>`<section class="group pv-iss"><h2 class="ghead">${t}<span class="n">${rows.length}</span>${hd||''}</h2>${note?`<p class="gnote">${note}</p>`:''}${lim(rows).map(prow).join('')||`<div class="empty" style="padding:16px">None in the Pulse.${fk==='account'||fk==='person'?' Anything on your registers is listed below.':''}</div>`}${showAll(rows)}${ft||''}</section>`;
  const focus=fk==='account'||fk==='person';
  const linked=regLinked(P,fk,fv,scope.length);
  const foot=allToggle(scope);
  if(!(focus&&!scope.length&&linked)){
    if(fk==='person'){const own=a.filter(i=>(i._owners||[]).includes(fv)),inv=a.filter(i=>!(i._owners||[]).includes(fv));
      L+=sec(`Owned by ${esc(fv)}`,own,'','',sortMini(a.length))+sec(`${esc(fv)} named, someone else owns`,inv,`${esc(fv)} is named on these in the evidence (a statement, a commitment or a stated role) but is not the owner. The owner is on each row.`,foot)}
    else L+=sec(PALL?'All issues':'Live issues',a,'',foot,sortMini(a.length));
  }
  L+=linked;
  h+=`<div class="pv-g2"><div class="pv-col">${L}</div><div class="pv-col">${govSec(P,fk,fv)}</div></div>`;
  const kn=knowHtml(know,fk,fv,trk);
  const peo=peopleHtml(P,fk,fv);
  if(ph){const kl=know.filter(i=>i._state==='live'),kc=kl.filter(i=>i._candidate).length,kq=know.filter(i=>i._state==='quiet').length;
    h+=`<button type="button" class="pv-sum" data-kopen aria-expanded="${KOPEN}"><b>Knowledge concentration</b> · ${kl.length} live${kc?' · '+kc+' needs your call':''}${kq?' · '+kq+' quiet':''} <span aria-hidden="true">${KOPEN?'⌃':'›'}</span></button>${KOPEN?kn:''}`;
    h+=`<button type="button" class="pv-sum" data-popen aria-expanded="${POPEN}"><b>People carrying the most</b> · ${P.people.length} people · top: ${esc(P.people.slice(0,3).map(r=>r.name).join(', '))} <span aria-hidden="true">${POPEN?'⌃':'›'}</span></button>${POPEN?peo:''}`}
  else h+=`<div class="pv-g3"><div class="pv-col">${kn}</div><div class="pv-col">${peo}</div></div>`;
  return h+'</div>'}
/* Phase 2, C18: top 8, grouped columns, Sole removed, zero shown as a dot */
let PPLALL=false;
function peopleHtml(P,fk,fv){const ph=PHONE();
  const src=fk==='person'?P.people.filter(r=>r.name===fv):P.people;const pp=PPLALL||fk==='person'?src:src.slice(0,8);
  const z=n=>n?`${n}`:'<span class="z" aria-label="none">·</span>';
  const rows=pp.map(r=>`<button type="button" class="ppl pv-pp${fk==='person'&&fv===r.name?' on':''}" data-pf="person" data-val="${esc(r.name)}" title="${esc(r.forums.map(fname).join(', ')||'No forum')}"><span>${esc(r.name)}</span><span class="num">${z(r.owns??r.pulse)}</span><span class="num">${z(r.involved??0)}</span><span class="num">${z(r.delegated)}</span></button>`).join('');
  const more=fk!=='person'&&P.people.length>8?`<button type="button" class="more pv-pmore" data-pplall>${PPLALL?'Show top 8':'Show all '+P.people.length+' people'}</button>`:'';
  return `<section class="group pv-ppl"><h2 class="ghead">People carrying the most<span class="sub">${PPLALL||fk==='person'?P.people.length+' people':'top 8 of '+P.people.length}</span>${ph?'':'<span class="sub r">Select a name to filter</span>'}</h2>
   <div class="ppl pv-pp g" aria-hidden="true"><span></span><span class="gl">In the Pulse</span><span class="gl r">Your registers</span></div>
   <div class="ppl pv-pp h"><span>Person</span><span class="num">Owns</span><span class="num">Involved</span><span class="num">Delegated</span></div>${rows}${more}
   <p class="gnote pv-pn">Owns: owner of a live Pulse issue. Involved: named in the evidence on a live issue, not the owner. Delegated: open delegated or awaited items on your registers.</p></section>`}
/* Phase 2, C19: knowledge concentration stays the one view of single points of failure */
const KCOV={none:['No backup','red'],unknown:['Backup unknown','red'],partial:['Partly covered',''],covered:['Covered','grn']};
const TRK=k=>((PULSE&&PULSE.tracks)||[]).find(t=>t.key===k)?.name||k||'';
const bkp=i=>i.backup?i.backup:(i.coverage||'unknown')==='unknown'?'not confirmed':'none named';
function xpo(i){return (i.exposure||[]).map(x=>{x=String(x);return x==='customer'&&i.account?'Customer · '+i.account:cap(x)})}
function krow(i){const cov=KCOV[i.coverage||'unknown']||KCOV.unknown;const cls=i._state==='live'?'':i._state==='quiet'?' dim':' done';
  const bd=`<span class="pv-b ${cov[1]}">${cov[0]}</span>${xpo(i).map(x=>`<span class="pv-b">${esc(x)}</span>`).join('')}${i.escalated_to?`<span class="pv-b esc">Escalated · ${esc(i.escalated_to)}</span>`:i._candidate?'<span class="pv-b call">Needs your call</span>':''}${i.absence_date?`<span class="pv-b">Away from ${fmt(i.absence_date)}</span>`:''}${i._state!=='live'?`<span class="pv-b">${cap(i._state)}</span>`:''}`;
  return `<div class="pv-ir pv-kr${SEL===i.id?' sel':''}${cls}" data-kid="${esc(i.id)}"><div class="id">${esc(i.id)}</div>
   <div class="bd"><button type="button" class="ttl" data-open="${esc(i.id)}">${PHONE()?`<span class="iid">${esc(i.id)}</span>`:''}${esc(i.title)}</button><div class="bdg">${bd}</div><div class="ow">Held by ${esc(i.holder||'?')} · Backup: ${esc(bkp(i))}</div>${i.mitigation?`<div class="nx">${esc(plain(i.mitigation))}</div>`:''}</div></div>`}
let KALL=false;
function knowHtml(know,fk,fv,trk){
  if(fk&&fk!=='person'&&fk!=='track'&&fk!=='account')return '';
  const k=know.filter(i=>!fk||(fk==='person'?(i.holder===fv||(i.backup||'').includes(fv)):fk==='track'?i.track===fv:i.account===fv));
  const live=k.filter(i=>i._state==='live'),quiet=k.filter(i=>i._state==='quiet');
  const cr={none:0,unknown:1,partial:2,covered:3};
  const rows=(KALL?k:live).slice().sort((a,b)=>((a._state==='live'?0:1)-(b._state==='live'?0:1))||((b._candidate?1:0)-(a._candidate?1:0))||((cr[a.coverage||'unknown']??1)-(cr[b.coverage||'unknown']??1))||String(b.last_seen||'').localeCompare(String(a.last_seen||'')));
  const qd=quiet.map(i=>`${i.id} (${(KCOV[i.coverage||'unknown']||KCOV.unknown)[0].toLowerCase()}${i.backup?', backup '+i.backup:''})`);
  const foot=`<div class="pv-kf">${quiet.length?`${quiet.length} quiet: ${esc(joinAnd(qd))}. `:''}Live for 45 days after last evidence.${quiet.length||KALL?` <button type="button" class="pv-lk" data-kall>${KALL?'Hide quiet':'Show quiet'}</button>`:''}</div>`;
  return `<section class="group pv-kn"><h2 class="ghead">Knowledge concentration<span class="sub">${live.length} live</span><span class="sub r">One person holds what a customer or release depends on</span></h2>${rows.map(krow).join('')||'<div class="empty" style="padding:16px">None.</div>'}${foot}</section>`}
async function pinAccount(name){const x=(PULSE.health||[]).find(h=>h.account===name);if(x&&x.pinned)return;
  const r=await fetch('/api/pulse/pin',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({account:name})});
  if(!r.ok){toast('Pin failed · '+name);return}PULSE=await r.json();
  SESSION.unshift({id:name,what:'pinned to the top',t:new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})});
  toast(name+' pinned to the top');render()}
PHONEQ.addEventListener('change',()=>render());
/* Items behind a tile or a person that live in the registers, not the Pulse (2026-10-16). Tap opens the item; the row says which register. */
function regLinked(P,fk,fv,nPulse){
  let ids=[],what='';
  if(fk==='account'){const h=(P.health||[]).find(x=>x.account===fv);ids=(h?h.register_items:[]).map(r=>r.id);
    what=`The items counted as "on your registers" in the ${esc(fv)} tile: Watch Active, your own actions, and Critical other-owned items that name ${esc(fv)}.`}
  else if(fk==='person'){const r=(P.people||[]).find(x=>x.name===fv);ids=(r?r.ids:[]).filter(id=>!/^[PK]\d/.test(id));
    what=`The open delegated or awaited items ${esc(fv)} owns, counted in the Delegated column.`}
  else return '';
  const rows=[...new Set(ids)].map(id=>ITEMS.find(i=>i.id===id)).filter(Boolean).sort(cmpId);
  if(!rows.length)return '';
  const lead=nPulse?'':`<b>No Pulse issues for ${esc(fv)}.</b> `;
  return `<section class="group"><h2 class="ghead">On your registers<span class="n">${rows.length}</span></h2><p class="gnote">${lead}${what} They live in your registers, not the Pulse; each row shows which one. Tap to open it here, or use the status buttons as you would on that tab.</p>${rows.map(rowHtml).join('')}</section>`}
/* Phase 2, C17: governance meeting view. One model feeds the presentable view and "Copy as text". */
function agendaModel(k){const P=PULSE,wk=dn(TODAY)-7*864e5,fs=i=>dn(String(i.first_seen||TODAY).slice(0,10));
  let it,m,multi=false,t=null;
  const dt=new Date(dn(TODAY)),day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][dt.getUTCDay()];
  if(k.startsWith('track:')){t=(P.tracks||[]).find(x=>x.key===k.slice(6))||{name:k,forums:[],leads:[],not_heard:[],heard:0,total:0};multi=true;
    it=ITEMS.filter(i=>i.kind==='pulse'&&i.category!=='knowledge'&&t.forums.includes(i.forum));
    m={kicker:'Weekly governance review',title:t.name,sub:`${day}, ${fmt(TODAY)} · with ${joinAnd(t.leads||[])} · evidence window ${fmt(P.window.start)} to ${fmt(P.window.end)}`,
      forums:t.forums.map(x=>P.forums.find(f=>f.key===x)).filter(Boolean)}}
  else{const f=P.forums.find(x=>x.key===k)||{name:k,key:k};it=ITEMS.filter(i=>i.kind==='pulse'&&i.category!=='knowledge'&&i.forum===k);
    m={kicker:'Governance review',title:f.name,sub:`${day}, ${fmt(TODAY)} · owner ${f.owner||'TBC'} · evidence window ${fmt(P.window.start)} to ${fmt(P.window.end)}`,forums:[f]}}
  const nh=m.forums.filter(f=>f.ev_state==='not_heard');
  m.banner=nh.length?{h:`Heard from ${m.forums.length-nh.length} of ${m.forums.length} forum${m.forums.length>1?'s':''} this window`,
    t:`Not heard: ${joinAnd(nh.map(f=>`${f.name} (${f.last_evidence?'last evidence '+fmt(f.last_evidence):'no evidence on file'})`))}. Ask for status before reading these counts as calm.`}:null;
  const live=it.filter(i=>i._state==='live');
  const sevw=i=>[i.severity,i.customer_visible?'customer-visible':'internal'].filter(Boolean).join(' · ');
  const own=i=>i.owner?'owner '+i.owner:'no owner named';
  const nx=i=>i.next_action?'Next: '+plain(i.next_action).replace(/\.$/,'')+'.':'';
  const kn=multi?ITEMS.filter(i=>i.kind==='pulse'&&i.category==='knowledge'&&i.track===t.key):[];
  const cand=P.candidates||[];const why=id=>(cand.find(c=>c.id===id)||{}).reason_line||'';
  const S=[];
  S.push({t:'Stuck: what unblocks it, who decides, by when',items:live.filter(i=>i._stuck).map(i=>({id:i.id,title:i.title,b:i,meta:`Owner: ${i.owner||'no owner named'} · last raised ${fmt(i.last_seen||i.first_seen)}${multi?' · '+fname(i.forum):''}`,next:nx(i)}))});
  S.push({t:'Needs a decision or escalation',items:[...live.filter(i=>i._candidate&&!i._stuck).map(i=>({id:i.id,title:i.title,meta:`${sevw(i)} · ${own(i)} · ${i.account||'no account'}`,next:why(i.id)||('Test: '+(P.tests[i._candidate]||i._candidate))})),
    ...kn.filter(i=>i._candidate&&i._state==='live').map(i=>({id:i.id,title:i.title,meta:`Knowledge risk · held by ${i.holder||'?'}${i.absence_date?' · away from '+fmt(i.absence_date):''} · backup ${bkp(i)}`,next:why(i.id)||'Decide: who holds this now, and when the handover is confirmed.'}))]});
  const rest=live.filter(i=>!i._stuck&&!i._candidate);
  S.push({t:'New this week',items:rest.filter(i=>fs(i)>=wk).map(i=>({id:i.id,title:i.title,meta:`${sevw(i)} · ${own(i)} · ${i.account||'no account'}${multi?' · '+fname(i.forum):''}`,next:nx(i)}))});
  const older=rest.filter(i=>fs(i)<wk);
  if(older.length)S.push({t:'Still open',items:older.map(i=>({id:i.id,title:i.title,meta:`${sevw(i)} · ${own(i)} · ${i.account||'no account'} · raised since ${fmt(i.first_seen)}`,next:nx(i)}))});
  S.push({t:'Gone quiet: resolved, or dropped?',items:it.filter(i=>i._state==='quiet').map(i=>({id:i.id,title:i.title,meta:`${[i.severity,i.account].filter(Boolean).join(' · ')} · ${own(i)} · last raised ${fmt(i.last_seen||i.first_seen)}`,next:''}))});
  if(multi)S.push({t:'Who backs up whom, and by when',items:kn.filter(i=>i._state==='live'||i._state==='quiet').map(i=>({id:i.id,title:i.title,meta:`${i.holder||'?'} · backup ${bkp(i)}${(i.exposure||[]).length?' · '+(i.exposure||[]).map(x=>String(x)==='customer'&&i.account?'customer exposure ('+i.account+')':String(x)+' exposure').join(', '):''}${i._state==='quiet'?' · quiet; confirm still current':''}`,next:i.mitigation?plain(i.mitigation):''}))});
  m.sections=S;
  m.counts=multi?[t.live+' live',t.new7+' new',t.stuck+' stuck',t.candidates+' call'+(t.candidates===1?'':'s'),t.quiet+' quiet'].join(' · '):[live.length+' live',it.filter(i=>i._state==='quiet').length+' quiet'].join(' · ');
  m.escalated=it.filter(i=>i.escalated_to).map(i=>`${i.id} → Watch ${i.escalated_to}`);
  return m}
function agendaMd(k){const m=agendaModel(k);const L=[`# ${m.title}: ${m.kicker.toLowerCase()}`,'',m.sub,''];
  if(m.banner)L.push(`${m.banner.h}. ${m.banner.t}`,'');
  m.sections.forEach((s,n)=>{L.push(`## ${n+1}. ${s.t}`,'');if(!s.items.length)L.push('- None.');s.items.forEach(x=>L.push(`- ${x.id} ${plain(x.title)}. ${x.meta}.${x.next?' '+x.next:''}`));L.push('')});
  L.push('## This track','',m.counts,'');m.forums.forEach(f=>L.push(`- ${f.name}: ${evLine(f)}`));
  if(m.escalated.length)L.push('','## Escalated to you','',...m.escalated.map(e=>'- '+e));
  return L.join('\n')}
let MEET=null;
/* Copy as text: formatted (text/html) plus plain text on the clipboard together, so Teams, Outlook and Word paste headings,
   bold and bullets while a plain editor gets the Markdown. navigator.clipboard.write needs a secure context (https or localhost);
   the app is served over plain http on the LAN, so elsewhere we select the hidden textarea and run execCommand('copy') with a
   one-shot copy handler that sets both formats (works over http inside a click). If that fails too, the text block opens already
   selected so Cmd-C / Copy finishes the job. Same pattern as copyPrompt (10-19); formatted copy added 10-20 at Darryl's request. */
function agendaHtml(k){const m=agendaModel(k),h=esc;const L=[`<h2>${h(m.title)}: ${h(m.kicker.toLowerCase())}</h2>`,`<p>${h(m.sub)}</p>`];
  if(m.banner)L.push(`<p><b>${h(m.banner.h)}.</b> ${h(m.banner.t)}</p>`);
  m.sections.forEach((s,n)=>{L.push(`<h3>${n+1}. ${h(s.t)}</h3>`);L.push('<ul>'+(s.items.length?s.items.map(x=>`<li><b>${h(x.id)} ${h(plain(x.title))}.</b> ${h(x.meta)}.${x.next?' <i>'+h(x.next)+'</i>':''}</li>`).join(''):'<li>None.</li>')+'</ul>')});
  L.push('<h3>This track</h3>',`<p>${h(m.counts)}</p>`,'<ul>'+m.forums.map(f=>`<li>${h(f.name)}: ${h(evLine(f))}</li>`).join('')+'</ul>');
  if(m.escalated.length)L.push('<h3>Escalated to you</h3>','<ul>'+m.escalated.map(e=>'<li>'+h(e)+'</li>').join('')+'</ul>');
  return L.join('\n')}
function copyAgenda(){if(!MEET)return;const txt=agendaMd(MEET),html=agendaHtml(MEET);const ta=document.getElementById('meet-ta');if(ta)ta.value=txt;
  const done=()=>toast('Agenda copied, with formatting');
  const fall=()=>{if(!ta)return toast('Copy is not available here');const d=ta.closest('details');ta.focus();ta.select();ta.setSelectionRange(0,ta.value.length);
    const onCopy=e=>{e.preventDefault();e.clipboardData.setData('text/html',html);e.clipboardData.setData('text/plain',txt)};
    document.addEventListener('copy',onCopy,{once:true});let ok=false;try{ok=document.execCommand('copy')}catch(e){ok=false}
    document.removeEventListener('copy',onCopy);
    if(ok){done();ta.blur()}else{d.open=true;d.scrollIntoView({block:'nearest'});ta.focus();ta.select();toast('Text selected: press Cmd-C (or Copy) to copy it')}};
  if(navigator.clipboard&&window.isSecureContext&&window.ClipboardItem&&navigator.clipboard.write){
    try{navigator.clipboard.write([new ClipboardItem({'text/html':new Blob([html],{type:'text/html'}),'text/plain':new Blob([txt],{type:'text/plain'})})]).then(done,fall)}catch(e){fall()}}
  else if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(txt).then(done,fall);else fall()}
function openAgenda(k){MEET=k;const m=agendaModel(k);
  let el=$('#pv-meet');if(!el){el=document.createElement('div');el.id='pv-meet';el.setAttribute('role','dialog');el.setAttribute('aria-modal','true');document.body.appendChild(el)}
  const bd=b=>b?ibadges(b):'';
  const secs=m.sections.map((s,n)=>`<section class="ms"><h3><span class="nm">${n+1}</span>${esc(s.t)}</h3>${s.items.length?s.items.map(x=>`<div class="mi"><span class="id">${esc(x.id)}</span><div><button type="button" class="mt" data-mopen="${esc(x.id)}">${esc(x.title)}</button>${x.b?`<div class="bdg">${bd(x.b)}</div>`:''}<div class="mm">${esc(x.meta)}</div>${x.next?`<div class="mn">${esc(x.next)}</div>`:''}</div></div>`).join(''):'<div class="mi none">None.</div>'}</section>`).join('');
  const rail=`<aside class="mr"><div class="rh">This track</div><div class="rc">${esc(m.counts)}</div><div class="rh">Forums</div>${m.forums.map(f=>`<div class="rf">${mk(f.ev_state)}<div>${esc(f.name)}<small>${esc(evLine(f))}${f.ev_state==='raised'?' · '+f.live+' live':''}</small></div></div>`).join('')}${m.escalated.length?`<div class="rh sep">Escalated to you</div>${m.escalated.map(e=>`<div class="rc">${esc(e)}</div>`).join('')}`:''}</aside>`;
  el.innerHTML=`<div class="mw"><div class="mh"><div><div class="kk">${esc(m.kicker)}</div><h2>${esc(m.title)}</h2><div class="sb">${esc(m.sub)}</div></div>
   <div class="mb"><button type="button" class="btn primary" data-mcopy>Copy as text</button><button type="button" class="btn" data-mfs>${document.fullscreenElement?'Exit full screen':'Present full screen'}</button><button type="button" class="btn" data-mclose>Close</button></div></div>
   ${m.banner?`<div class="mban"><span class="hx" aria-hidden="true"></span><div><b>${esc(m.banner.h)}</b><p>${esc(m.banner.t)}</p></div></div>`:''}
   <div class="mg"><div class="msecs">${secs}</div>${rail}</div>
   <details class="mtxt" id="meet-txt"><summary>Agenda as text</summary><textarea id="meet-ta" readonly spellcheck="false">${esc(agendaMd(k))}</textarea></details></div>`;
  document.body.classList.add('locked');el.scrollTop=0;el.focus&&el.setAttribute('tabindex','-1');el.focus()}
function closeMeet(){MEET=null;if(document.fullscreenElement)document.exitFullscreen().catch(()=>{});const el=$('#pv-meet');if(el)el.remove();if(!DRAWER&&!SHEET)document.body.classList.remove('locked')}
document.addEventListener('fullscreenchange',()=>{const b=document.querySelector('[data-mfs]');if(b)b.textContent=document.fullscreenElement?'Exit full screen':'Present full screen'});
async function escalateP(id,decision){
  const r=await fetch('/api/pulse/'+encodeURIComponent(id)+'/escalate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({decision})});
  if(!r.ok){toast('Save failed · '+id);return}const j=await r.json();
  SESSION.unshift({id,what:j.watch?'escalated to '+j.watch:'left with team',t:new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})});
  toast(j.watch?`${id} escalated · ${j.watch} is on your Watch list`:`${id} left with the team`);
  await load();if(SHEET===id)openSheet(id);if(DRAWER==='item'&&SEL===id)openDrawer(id)}
/* ---------- panel ---------- */
function layout(){const open=!!DRAWER;const dock=open&&innerWidth>=1100&&DRAWER==='item';
  document.body.classList.toggle('docked',dock);$('#scrim').style.display=open&&!dock?'block':'none';$('#drawer').classList.toggle('open',open);document.body.classList.toggle('locked',open&&!dock)}
function showDrawer(kind){DRAWER=kind;layout()}
function closeDrawer(){DRAWER=null;SEL=null;layout();render()}
addEventListener('resize',layout);
addEventListener('keydown',e=>{if(e.key!=='Escape')return;if(SHEET){closeSheet();return}if(MEET&&!document.fullscreenElement){closeMeet();return}if(DRAWER)closeDrawer()});
$('#scrim').onclick=closeDrawer;
function head(id,meta){return `<div class="p-meta"><button type="button" class="p-back" data-close>‹ Back</button>${id?`<span class="id">${esc(id)}</span>`:''}<span>${meta}</span><button type="button" class="p-close" data-close>Close</button></div>`}
function history(i){
  const out=[];let sec='';
  for(const p of (i.body||'').split(/\n\s*\n/)){const t=p.trim();if(!t)continue;
    const h=t.match(/^##\s+(.*)/);if(h){sec=h[1];out.push(null);continue}
    const m=t.match(/^(\d{4}-\d{2}-\d{2}) \(([^)]+)\):\s*([\s\S]*)/);
    const body=x=>plain(x.replace(/^(\s*)[-*] /gm,'$1• '));
    if(m)out.push({d:fmt(m[1]),w:m[2]==='Darryl, web'?'You, from the web':m[2],t:body(m[3]),isNew:m[1]===TODAY&&m[2]==='Darryl, web'});
    else if(out.length&&out[out.length-1])out[out.length-1].t+='\n\n'+body(t);
    else out.push({d:'',w:sec||'Record',t:body(t)});
  }
  for(let k=out.length;k--;)if(!out[k])out.splice(k,1);
  return out.reverse();
}
function field(l,k,v,type='text',opts,full){
  const inner=opts?`<select name="${k}">${opts.map(o=>`<option ${o===v?'selected':''}>${o}</option>`).join('')}</select>`:`<input name="${k}" type="${type}" value="${esc(v)}">`;
  return `<div${full?' class="full"':''}><label>${l}${inner}</label></div>`}
function fields(i){let f=field('Title','title',i.title,'text',null,true);
  if(i.kind==='action'){
    f+=field('Register','register',i.register,'',['A','other','triage'])+field('Status','status',i.status,'',['open','closed','dropped','aged_out']);
    f+=field('Owner','owner',i.owner)+field('Counterparty','counterparty',i.counterparty);
    f+=field('Type (other-owned)','type',i.type||'','',['','Delegated','Awaited'])+field('Critical','critical',String(!!i.critical),'',['false','true']);
    f+=field('Due (YYYY-MM-DD)','due',i.due)+field('Due note / gate','due_note',i.due_note);
    f+=field('Trigger','trigger',i.trigger)+field('Product','product',i.product||'');
    f+=field('Next action (one line)','next_action',i.next_action,'text',null,true);
    f+=field('Critical reason','critical_reason',i.critical_reason||'')+field('Basis','basis',i.basis||'');
  }else if(i.kind==='watch'){
    f+=field('Tier','tier',i.tier,'',['active','passive','retired'])+field('Severity','severity',i.severity||'','',['','High','Medium','Low']);
    f+=field('Trend','trend',i.trend||'')+field('Evidence basis','evidence_basis',i.evidence_basis||'');
    f+=field('Next action (one line)','next_action',i.next_action||'','text',null,true)+field('Product','product',i.product||'');
  }else if(i.kind==='pulse'&&i.category==='knowledge'){
    f+=field('Held by','holder',i.holder||'')+field('Backup (name, or blank)','backup',i.backup||'');
    f+=field('Coverage','coverage',i.coverage||'unknown','',['none','unknown','partial','covered'])+field('Exposure (comma list: customer, release, migration, support)','exposure',(i.exposure||[]).join(', '));
    f+=field('Absence or departure date (YYYY-MM-DD)','absence_date',i.absence_date||'')+field('Track','track',i.track||'','',['','delivery','development']);
    f+=field('Mitigation under way','mitigation',i.mitigation||'','text',null,true);
    f+=field('Status','status',i.status||'live','',['live','resolved','dropped'])+field('Escalation','escalation',i.escalation||'','',['','candidate','escalated','declined']);
    return f;
  }else if(i.kind==='pulse'){
    f+=field('Status','status',i.status||'live','',['live','resolved','dropped'])+field('Severity','severity',i.severity||'','',['','High','Medium','Low']);
    f+=field('Account','account',i.account||'')+field('Product','product',i.product||'');
    f+=field('Owner (team)','owner',i.owner||'')+field('Customer-visible','customer_visible',String(!!i.customer_visible),'',['false','true']);
    f+=field('Escalation','escalation',i.escalation||'','',['','candidate','escalated','declined'])+field('Escalation test','escalation_test',i.escalation_test||'','',['','asked','boundary','stuck','gap']);
    f+=field('Next action (one line)','next_action',i.next_action||'','text',null,true);
    return f;
  }else{
    f+=field('Tier','tier',i.tier,'',['radar','backlog'])+field('Status (free text)','status',i.status||'');
    f+=field('Owner','owner',i.owner||'')+field('Forum date (YYYY-MM-DD)','forum_date',i.forum_date||'');
    f+=field('Forum','forum',i.forum||'','text',null,true)+field('Next action (one line)','next_action',i.next_action||'','text',null,true)+field('Product','product',i.product||'');
  }
  return f+field('Needs triage','needs_triage',String(!!i.needs_triage),'',['false','true'])}
function openDrawer(id){
  const i=ITEMS.find(x=>x.id===id);if(!i)return;
  const same=SEL===id&&DRAWER==='item';
  const keepNote=same&&$('#note')?$('#note').value:'',keepDet=same&&$('#det')?$('#det').open:false,keepScroll=same?$('#drawer').scrollTop:0;
  SEL=id;
  const reg=i.kind==='pulse'&&i.category==='knowledge'?'Knowledge concentration · '+TRK(i.track):i.kind==='pulse'?'Pulse · '+fname(i.forum)+(i.severity?' · '+i.severity:''):i.kind==='action'?(i.register==='A'?'Register A · Mine':i.register==='triage'?'New item':'Other-owned'+(i.type?' · '+i.type:'')):i.kind==='watch'?'Watch'+(i.severity?' · '+i.severity:''):'Decision · '+cap(i.tier);
  const d=dueInfo(i);const due=d.due?`${i.kind==='decision'?'Forum':'Due'} ${fmt(d.due)} · ${d.n<0?-d.n+' day'+(d.n===-1?'':'s')+' late':d.n===0?'today':'in '+d.n+' days'}`:(i.trigger?'No date · waits on: '+esc(i.trigger):'No due date');
  const pdue=i.kind==='pulse'&&i.category==='knowledge'?`${(KCOV[i.coverage||'unknown']||KCOV.unknown)[0]} · held by ${esc(i.holder||'?')} · evidence ${i.sightings||1}× since ${fmt(i.first_seen)} · last ${fmt(i.last_seen||i.first_seen)}`:i.kind==='pulse'?`Raised ${i.sightings||1}× · first ${fmt(i.first_seen)} · last ${fmt(i.last_seen||i.first_seen)} · ${cap(i._state)}${i._stuck?' · stuck':''}`:null;
  const pesc=i.kind!=='pulse'?'':i.escalated_to?`<div class="p-esc"><span class="why">On your Watch list as <a href="#" data-open="${esc(i.escalated_to)}">${esc(i.escalated_to)}</a>. The team still owns the work.</span></div>`:`<div class="p-esc">${i._candidate?`<span class="why">Needs your call: ${esc((PULSE&&PULSE.tests[i._candidate])||i._candidate)}</span>`:i.escalation==='declined'?'<span class="why">You left this with the team. You can still escalate it.</span>':'<span class="why">With the team. Escalate only if it needs you.</span>'}<button type="button" class="btn primary" data-esc="escalate" data-id="${esc(i.id)}">Escalate to my Watch list</button>${i.escalation==='declined'?'':`<button type="button" class="btn" data-esc="decline" data-id="${esc(i.id)}">Leave with team</button>`}</div>`;
  const nFields=(fields(i).match(/<label>/g)||[]).length;
  const sv=SAVED[id];
  $('#panel').innerHTML=`<div class="p-top">${head(i.id,esc(reg))}
     <h2 class="p-title">${esc(i.title)}</h2>
     ${i.next_action?`<div class="p-next">${esc(plain(i.next_action))}</div>`:''}
     <div class="p-due${d.cls==='late'&&!pdue?' late':''}">${pdue||due}${i.critical?' · <span class="t-crit">Critical</span>':''}</div></div>
   <form id="nf2" class="p-act">${seg(i,true)}${pesc}
     <textarea id="note" name="note" placeholder="Add a note: what happened, what you decided, what Claude should know…">${esc(keepNote)}</textarea>
     <div class="p-save"><button type="submit" class="btn primary">Save note</button><span class="hint${sv?' ok':''}">${sv?`Saved ${sv.t} · ${esc(sv.what)} · committed`:'Status saves on tap. Notes are dated, appended and committed.'}</span></div></form>
   <div class="p-sec"><h3 class="p-label">History</h3>
     ${history(i).map(h=>`<div class="h${h.isNew?' new':''}"><div class="d">${h.d}</div><div><div class="w">${esc(h.w)}</div><div class="t">${esc(h.t)}</div></div></div>`).join('')||'<div class="h"><div></div><div class="t" style="color:var(--muted)">No notes yet.</div></div>'}
     <details id="det"${keepDet?' open':''}><summary><span class="sl">Details</span><span>${nFields} fields · ${esc(i.path||'')}</span></summary>
       <form id="f"><div class="fgrid">${fields(i)}</div><div class="p-save"><button type="submit" class="btn primary">Save details</button><span class="hint">Last touched ${fmt(i.last_touched)}</span></div></form></details>
   </div>`;
  showDrawer('item');if(!same)$('#drawer').scrollTop=0;else $('#drawer').scrollTop=keepScroll;
  render();
  $('#nf2').onsubmit=async ev=>{ev.preventDefault();const n=$('#note').value;if(!n.trim()){$('#note').focus();return}$('#note').value='';await patch(id,{},n)};
  $('#f').onsubmit=async ev=>{ev.preventDefault();const fd=new FormData(ev.target);const p={};
    /* 2026-10-20: send only the fields you changed, so a form opened before a session edit cannot write stale values back over it (C72). */
    const cur=ITEMS.find(x=>x.id===id)||{};
    for(const [k,v] of fd.entries()){const nv=(k==='critical'||k==='needs_triage'||k==='customer_visible')?(v==='true'):v;
      if(String(nv)!==String(cur[k]??''))p[k]=nv}
    if(!Object.keys(p).length){toast('No changes');return}
    await patch(id,p,'')};
}
$('#panel').addEventListener('click',e=>{if(e.target.closest('[data-close]'))closeDrawer()});
/* Markdown-style lists in the note box: "1. " or "- " starts a list; Return continues it; Return on an empty item ends it. */
$('#panel').addEventListener('keydown',e=>{
  const t=e.target;if(!(t instanceof HTMLTextAreaElement)||e.key!=='Enter'||e.shiftKey||e.metaKey||e.ctrlKey||e.isComposing)return;
  const v=t.value,pos=t.selectionStart;const ls=v.lastIndexOf('\n',pos-1)+1;const line=v.slice(ls,pos);
  const m=line.match(/^(\s*)(?:([-*•])|(\d+)([.)]))(\s+)(.*)$/);if(!m)return;
  e.preventDefault();
  const [,ind,bul,num,punc,sp,rest]=m;
  if(!rest.trim()){t.setRangeText('',ls,pos,'end');t.setRangeText('\n',ls,ls,'end');return}
  const next=bul?`${ind}${bul}${sp}`:`${ind}${+num+1}${punc}${sp}`;
  t.setRangeText('\n'+next,pos,t.selectionEnd,'end');
  t.dispatchEvent(new Event('input',{bubbles:true}));
});
$('#newBtn').onclick=()=>{
  SEL=null;
  $('#panel').innerHTML=`<div class="p-top">${head('', 'New item')}</div>
   <form id="nf" class="p-act" style="border:0"><div class="fgrid"><div class="full"><label>Title<input name="title" required autocomplete="off" enterkeyhint="done"></label></div></div>
   <textarea name="note" placeholder="Note (optional)"></textarea>
   <div class="p-save"><button type="submit" class="btn primary">Add</button><span class="hint">Lands as a T-item flagged “needs triage”; Claude classifies it at the next brief.</span></div></form>`;
  showDrawer('new');$('#nf [name=title]').focus();
  $('#nf').onsubmit=async ev=>{ev.preventDefault();const fd=new FormData(ev.target);
    const r=await fetch('/api/items',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:fd.get('title'),note:fd.get('note')})});
    if(!r.ok){toast('Add failed');return}const id=(await r.json()).id;await load();
    SESSION.unshift({id,what:'added',t:new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})});
    toast('Added '+id+' · needs triage');closeDrawer()};
};
$('#logBtn').onclick=async()=>{const j=await (await fetch('/api/log?n=40')).json();
  SEL=null;
  $('#panel').innerHTML=`<div class="p-top">${head('','Changes')}<h2 class="p-title">This session</h2></div>
   <div class="p-sec">${SESSION.length?`<div class="log">${SESSION.map(s=>`<span class="d">${esc(s.t)}</span><span><b>${esc(s.id)}</b> · ${esc(s.what)}</span>`).join('')}</div>`:'<div style="color:var(--muted);font-size:14px">Nothing changed yet.</div>'}</div>
   <div class="p-sec"><h3 class="p-label">Recent commits (git)</h3>${j.log.length?`<div class="log">${j.log.map(l=>`<span class="d">${fmt(l.date)}</span><span>${esc(l.subject)}</span>`).join('')}</div>`:'<div style="color:var(--muted)">No git history yet.</div>'}</div>`;
  showDrawer('log');render()};
function md(src){const inl=t=>esc(t).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>');
  const out=[];let list=null,tbl=null;const flush=()=>{if(list){out.push(`</${list}>`);list=null}if(tbl){out.push('</table>');tbl=null}};
  for(const raw of src.split('\n')){const l=raw.trimEnd();
    if(!l.trim()){flush();continue}
    let m;
    if((m=l.match(/^(#{1,3}) (.*)/))){flush();out.push(`<h${m[1].length}>${inl(m[2])}</h${m[1].length}>`);continue}
    if((m=l.match(/^\|(.+)\|$/))){if(/^\|[\s|:-]+\|$/.test(l))continue;const cells=m[1].split('|').map(c=>c.trim());if(!tbl){flush();tbl=1;out.push('<table>');out.push('<tr>'+cells.map(c=>`<th>${inl(c)}</th>`).join('')+'</tr>')}else out.push('<tr>'+cells.map(c=>`<td>${inl(c)}</td>`).join('')+'</tr>');continue}
    if((m=l.match(/^- (.*)/))){if(list!=='ul'){flush();list='ul';out.push('<ul>')}out.push(`<li>${inl(m[1])}</li>`);continue}
    if((m=l.match(/^\d+\. (.*)/))){if(list!=='ol'){flush();list='ol';out.push('<ol>')}out.push(`<li>${inl(m[1])}</li>`);continue}
    flush();out.push(`<p>${inl(l)}</p>`)}
  flush();return out.join('')}
/* ---------- Products tab (2026-10-21): one card per live product; what changed in its file, and the open items that touch it ---------- */
let PRODS=null,PMORE={},PHID=false,PWIN=14;try{PWIN=+(localStorage.getItem('eos.products.win')||14)||14}catch(e){PWIN=14}
async function loadProducts(from){try{PRODS=await (await fetch('/api/products?window='+PWIN+'&from='+encodeURIComponent(from||''))).json()}catch(e){PRODS=null;toast('Could not load the products')}}
async function setLive(name,to){try{const r=await fetch('/api/products/live',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({product:name,live:to,window:PWIN})});if(!r.ok)throw 0;PRODS=await r.json();toast((to?'Showing ':'Hiding ')+name);render()}catch(e){toast('Could not change '+name)}}
function pAge(c){if(c.age_days==null)return ['q','no dated entries'];if(c.age_days===0)return ['','updated today'];if(c.age_days<=7)return ['','updated '+c.age_days+'d ago'];if(c.age_days<=14)return ['a','updated '+c.age_days+'d ago'];return ['q','quiet since '+fmt(c.last_entry)]}
function pLabel(i){if(i.kind==='action')return i.register==='A'?'Mine'+(i.due?' · due '+fmt(i.due):''):'Other-owned'+(i.critical?' · critical':'')+(i.due?' · '+fmt(i.due):'');if(i.kind==='watch')return 'Watch · '+esc(i.severity||'');return 'Radar'+(i.forum_date?' · '+fmt(i.forum_date):'')}
function productsHtml(){
  if(!PRODS)return '<div class="empty">Loading the products…</div>';
  const ps=PRODS.products;const live=ps.filter(p=>p.recent.length),quiet=ps.filter(p=>!p.recent.length);
  const win=`<div class="pr-win">${[7,14,30].map(w=>`<button type="button" class="${w===PWIN?'on':''}" data-pwin="${w}">${w} days</button>`).join('')}</div>`;
  const head=`<div class="pr-top"><div><div class="pr-sub">What changed in each product file in the last ${PWIN} days, and the open register items that touch it. ${live.length} with new entries, ${quiet.length} quiet.</div></div>${win}</div>`;
  const card=p=>{const [cls,ft]=pAge(p);const c=p.counts;const all=PMORE[p.name];const show=all?p.recent:p.recent.slice(0,3);
    return `<section class="pr-card${p.recent.length?'':' quiet'}"><div class="pr-h"><h2>${esc(p.name)}</h2><span class="pr-age ${cls}">${ft}</span></div>
    <div class="pr-counts"><span><b>${p.recent.length}</b> new entr${p.recent.length===1?'y':'ies'}</span><span><b>${c.mine}</b> mine</span><span><b>${c.other}</b> other-owned</span><span><b>${c.watch}</b> watch</span><span><b>${c.radar}</b> radar</span></div>
    ${show.map(r=>`<div class="pr-e"><div class="pr-d">${fmt(r.date)}${p.file.includes(',')&&r.file?' · '+esc(r.file.split('/').pop().replace('.md',''))+'':''}</div><div class="pr-eh">${esc(r.heading)}</div>${r.lead.length?`<ul>${r.lead.map(b=>`<li>${esc(b)}</li>`).join('')}</ul>`:''}${r.ids.length?`<div class="pr-ids">${r.ids.map(i=>`<a href="#" class="pr-id" data-sopen="${esc(i)}">${esc(i)}</a>`).join('')}</div>`:''}</div>`).join('')||`<div class="pr-none">Nothing new in this window. Last entry ${p.last_entry?fmt(p.last_entry):'none'}.</div>`}
    ${p.recent.length>3?`<button type="button" class="pr-more" data-pmore="${esc(p.name)}">${all?'Show fewer':(p.recent.length-3)+' more entr'+(p.recent.length-3===1?'y':'ies')+' in this window'}</button>`:''}
    <details class="pr-items"><summary>Open register items (${p.items.length})</summary>${p.items.map(i=>`<a href="#" class="pr-i" data-sopen="${esc(i.id)}"><span class="k">${esc(i.id)}</span><span class="t">${esc(i.title)}</span><span class="m">${pLabel(i)}</span></a>`).join('')||'<div class="pr-none">None matched. Set the product field on items at intake.</div>'}</details>
    <div class="pr-foot"><span>${esc(p.file)}</span><button type="button" class="pr-live" data-plive="${esc(p.name)}" data-to="0" title="Hide this product from the tab">Hide</button></div></section>`};
  const hidden=PRODS.hidden.length?`<div class="pr-hidden"><span>Not shown: ${PRODS.hidden.map(esc).join(', ')}.</span><button type="button" class="pr-more" data-phidden>${PHID?'Done':'Change'}</button>${PHID?`<div class="pr-hl">${PRODS.hidden.map(h=>`<button type="button" class="btn" data-plive="${esc(h)}" data-to="1">Show ${esc(h)}</button>`).join('')}</div>`:''}</div>`:'';
  return head+`<div class="pr-grid">${ps.map(card).join('')}</div>`+hidden}
/* ---------- Briefs tab (2026-10-19): the daily and weekly briefs, in sight, with item IDs that open the item ---------- */
async function loadBriefs(){try{const j=await (await fetch('/api/briefs')).json();BRIEFS=j.briefs||[]}catch(e){BRIEFS=[]}}
async function openBrief(name,from){try{const j=await (await fetch('/api/briefs/'+encodeURIComponent(name)+'?from='+encodeURIComponent(from||''))).json();BRIEF=j;BREAD=true}catch(e){toast('Could not open '+name)}render();if(from==='list')scrollTo(0,0)}
function wkStart(s){const d=new Date(dn(s));const w=(d.getUTCDay()+6)%7;return dn(s)-w*864e5}
function briefsHtml(){
  if(!BRIEFS.length)return '<div class="empty">No briefs in the Briefings folder yet.</div>';
  const thisWk=wkStart(TODAY),lastWk=thisWk-7*864e5,g={a:[],b:[],c:[]};
  for(const b of BRIEFS){const w=wkStart(b.date);(w>=thisWk?g.a:w>=lastWk?g.b:g.c).push(b)}
  const row=b=>`<button type="button" class="bi${BRIEF&&BRIEF.name===b.name?' on':''}" data-brief="${esc(b.name)}"><span class="bd">${WD[new Date(dn(b.date)).getUTCDay()]} ${fmt(b.date)}</span><span class="bk${b.kind==='Weekly'?' w':''}">${esc(b.kind)}</span>${b.date===TODAY?'<span class="bk w">Today</span>':''}</button>`;
  const sec=(l,a)=>a.length?`<h2 class="ghead">${l}<span class="n">${a.length}</span></h2>${a.map(row).join('')}`:'';
  const list=`<nav class="bl" aria-label="Briefs">${sec('This week',g.a)}${sec('Last week',g.b)}${sec('Earlier',g.c)}</nav>`;
  let rd='<div class="br"><div class="empty">Select a brief.</div></div>',toc='';
  if(BRIEF){const r=briefMd(BRIEF.markdown);
    const words=(BRIEF.markdown.match(/\S+/g)||[]).length,mins=Math.max(1,Math.round(words/230));
    toc=r.toc.length?`<nav class="btoc" aria-label="Sections"><div class="p-label">Sections</div>${r.toc.map(x=>`<a href="#${x.id}" data-toc="${x.id}"${x.closed?' class="cl"':''}>${esc(x.t)}</a>`).join('')}</nav>`:'';
    const sel=r.toc.length?`<select class="bsel" data-tocsel aria-label="Jump to section"><option value="">Sections</option>${r.toc.map(x=>`<option value="${x.id}">${esc(x.t)}</option>`).join('')}</select>`:'';
    rd=`<article class="br"><div class="bh"><button type="button" class="btn bback" data-bback>All briefs</button><span>${mins} min read</span>${BRIEF.docx?`<a href="/briefs/${esc(BRIEF.name.replace(/\.md$/,''))}.docx">Word version</a>`:'<span>No Word version yet</span>'}<span class="bp">Briefings/${esc(BRIEF.name)}</span>${sel}</div><div class="md brief">${r.html}</div></article>`}
  return `<div class="bv${BREAD?' reading':''}">${list}${rd}${toc}</div>`}
const IDRE=/\b(C-i3-\d+b?|[ABCDWPKTX]\d{1,3})\b/g;
function linkIds(h){return h.split(/(<code>[\s\S]*?<\/code>|<[^>]+>)/).map((s,k)=>k%2?s:s.replace(IDRE,m=>ITEMS.some(i=>i.id===m)?`<a href="#" class="iid" data-open="${m}">${m}</a>`:m)).join('')}
/* Sections a reader needs open by default; everything else (reference material) starts collapsed. */
const BOPEN=/summary|priorit|risk|my actions|register a|closure|decision required|changes since|this week.s objectives|chief of staff|calibration/i;
const BLABEL=/(Business impact|Why you personally|Why Darryl personally|Risk if delayed|Next step|Expected outcome|Recommended action):\s*/g;
function briefMd(src){
  const inl=t=>linkIds(esc(t).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/(^|[^*])\*([^*\s][^*]*)\*/g,'$1<i>$2</i>').replace(/\b(\d{4}-\d{2}-\d{2})\b/g,'<span class="dt">$1</span>'));
  let thead=[];
  const CO={'Risk':'risk','Decision Required':'dec','Source Note':'src','Bottom Line':'bl1','Image Caption':'cap'};
  /* A paragraph that carries two or more field labels becomes a card, one field per line, Next step highlighted. */
  const fields=t=>{const parts=t.split(BLABEL);if(parts.length<5)return null;
    let h=`<div class="pcard"><div class="pc-lead">${inl(parts[0].trim())}</div><dl>`;
    for(let k=1;k<parts.length;k+=2)h+=`<dt${/Next step|Recommended/.test(parts[k])?' class="nx"':''}>${esc(parts[k])}</dt><dd${/Next step|Recommended/.test(parts[k])?' class="nx"':''}>${inl(parts[k+1].trim())}</dd>`;
    return h+'</dl></div>'};
  const out=[],toc=[];let list=null,tbl=null,fence=null,fbuf=[],co=null,para=[],insec=false,sn=0,secOpen=true;
  const fp=()=>{if(para.length){const t=para.join(' ');const f=fields(t);const cov=/^Email:\s/.test(t);out.push(f||`<p${cov?' class="muted"':''}>${inl(t)}</p>`);para=[]}};
  const flush=()=>{fp();if(list){out.push(`</${list}>`);list=null}if(tbl){out.push('</table></div>');tbl=null}};
  const li=t=>{const m=t.match(/^\*\*([^*]{2,40}):\*\*\s*(.*)$/);if(m)return `<li class="kv${/Next step|Recommended/.test(m[1])?' nx':''}"><span class="k">${esc(m[1])}</span><span class="v">${inl(m[2])}</span></li>`;const f=fields(t);return f?`<li class="lic">${f}</li>`:`<li>${inl(t)}</li>`};
  for(const raw of src.split('\n')){const l=raw.trimEnd();let m;
    if(fence!==null){if(/^```/.test(l)){out.push(fence==='mermaid'?`<div class="chart">Chart (${/xychart/.test(fbuf.join(' '))?'items taken vs disposed':'diagram'}): see the Word version.</div>`:`<pre class="md-pre"><code>${esc(fbuf.join('\n'))}</code></pre>`);fence=null;fbuf=[]}else fbuf.push(raw);continue}
    if((m=l.match(/^```\s*(\w*)/))){flush();fence=m[1]||'';continue}
    if((m=l.match(/^:::\s*\{custom-style="([^"]+)"\}/))){flush();co=CO[m[1]]||'src';out.push(`<div class="co ${co}">`);continue}
    if(/^:::\s*$/.test(l)&&co){flush();out.push('</div>');co=null;continue}
    if(!l.trim()){flush();continue}
    if((m=l.match(/^## (.*)/))){flush();if(insec)out.push('</div></details>');const id='s'+(sn++);const title=m[1].replace(/\*\*/g,'');
      secOpen=BOPEN.test(title);toc.push({id,t:title.replace(/^\d+[a-z]?\.\s*/,'').replace(/`/g,''),closed:!secOpen});
      out.push(`<details class="bsec" id="${id}"${secOpen?' open':''}><summary><h2>${inl(m[1])}</h2></summary><div class="bsb">`);insec=true;continue}
    if((m=l.match(/^(#{1,3}) (.*)/))){flush();out.push(`<h${m[1].length}>${inl(m[2])}</h${m[1].length}>`);continue}
    if((m=l.match(/^\|(.+)\|$/))){fp();if(/^\|[\s|:-]+\|$/.test(l))continue;const cells=m[1].split('|').map(c=>c.trim());if(!tbl){flush();tbl=1;thead=cells;out.push('<div class="tw"><table>');out.push('<tr>'+cells.map(c=>`<th>${inl(c)}</th>`).join('')+'</tr>')}else out.push('<tr>'+cells.map((c,k)=>`<td data-th="${esc(thead[k]||'')}">${inl(c)}</td>`).join('')+'</tr>');continue}
    if((m=l.match(/^\s*- (.*)/))){fp();if(list!=='ul'){flush();list='ul';out.push('<ul>')}out.push(li(m[1]));continue}
    if((m=l.match(/^\d+\. (.*)/))){fp();if(list!=='ol'){flush();list='ol';out.push('<ol>')}out.push(li(m[1]));continue}
    if(list&&/^\s{2,}\S/.test(raw)){out[out.length-1]=out[out.length-1].replace(/<\/li>$/,' '+inl(l.trim())+'</li>');continue}
    if(list||tbl)flush();
    para.push(l)}
  flush();if(co)out.push('</div>');if(insec)out.push('</div></details>');return {html:out.join(''),toc}}
function jumpSec(id){const d=document.getElementById(id);if(!d)return;d.open=true;d.scrollIntoView({block:'start'})}
document.addEventListener('change',e=>{const s=e.target.closest('[data-tocsel]');if(s&&s.value){jumpSec(s.value);s.value=''}});
/* ---------- Copilot prompts (2026-10-19): Prompt 1 = Delivery track, Prompt 2 = Development track ---------- */
let CPR=null;
async function openPrompts(){try{CPR=await (await fetch('/api/copilot')).json()}catch(e){toast('Could not build the prompts');return}
  SEL=null;const P=CPR.pulse;
  const stp=CPR.steps.map((s,i)=>`<li class="cs ${s[0]}"><span class="ck">${s[0]==='done'?'✓':s[0]==='skip'||s[0]==='partial'?'–':i+1}</span><span>${esc(s[1])}</span></li>`).join('');
  const fx=o=>`<section class="cp${o.today&&!o.done?' need':''}"><div class="cp-h"><b>${esc(o.label)}</b><span class="cp-b ${o.today&&!o.done?'y':'n'}">${o.today?(o.done?'Done today':'Today'):'Not today'}</span></div>
    <div class="cp-m">${esc(o.sub)} Last package saved: ${o.last?fmt(o.last):'none'}.</div>
    <button type="button" class="btn${o.today&&!o.done?' primary':''}" data-cpy="${o.id}">Copy ${esc(o.label)}</button>
    <details class="cp-t"><summary>Show ${esc(o.label)} text</summary><textarea readonly id="cpt${o.id}">${esc(o.text)}</textarea></details></section>`;
  const ph=o=>`<section class="cp${o.needed?' need':''}"><div class="cp-h"><span class="cp-n">Prompt ${o.n}</span><b>Pulse · ${esc(o.label)}</b><span class="cp-b ${o.needed?'y':'n'}">${o.needed?'Needed':'Not needed'}</span></div>
    <div class="cp-m">Window ${fmt(o.window[0])} to ${fmt(o.window[1])} · ${o.forums.filter(f=>f.due).length||o.forums.length} forum${(o.forums.filter(f=>f.due).length||o.forums.length)===1?'':'s'} to search · ${o.tracked} tracked issue${o.tracked===1?'':'s'} listed</div>
    <ul class="cp-f">${o.forums.map(f=>`<li class="${f.due?'d':''}"><span>${esc(f.name)}</span><span>${f.due?'search':'heard'} · ${esc(f.why)}</span></li>`).join('')}</ul>
    <button type="button" class="btn${o.needed?' primary':''}" data-cpy="${o.n}">Copy Prompt ${o.n} · ${esc(o.label)}${o.needed?'':' (anyway)'}</button>
    <details class="cp-t"><summary>Show Prompt ${o.n} text</summary><textarea readonly id="cpt${o.n}">${esc(o.text)}</textarea></details></section>`;
  $('#panel').innerHTML=`<div class="p-top">${head('','Copilot')}<h2 class="p-title">Copilot prompts · ${esc(CPR.weekday)}</h2></div>
   <div class="p-sec"><h3 class="p-label">Today</h3><ol class="csteps">${stp}</ol><p class="cp-how">Run each prompt in its own new Copilot chat and paste the answer to Claude. Pulse answers start with "PROMPT 1 OF 2" or "PROMPT 2 OF 2", so they can come back in any order.</p></div>
   <div class="p-sec"><h3 class="p-label">Leadership evidence</h3>${CPR.fixed.map(fx).join('')}</div>
   <div class="p-sec" id="cp-pulse"><h3 class="p-label">Pulse: team-governed forums</h3><div class="cp-adv">${esc(P.advice)}</div><p class="cp-how">Prompt 1 searches the delivery forums, Prompt 2 the development forums, and only those not heard within their cadence.</p>${P.prompts.map(ph).join('')}</div>`;
  showDrawer('prompts');$('#drawer').scrollTop=0;render()}
function copyPrompt(id){const all=[...CPR.fixed.map(o=>({k:o.id,label:o.label,text:o.text})),...CPR.pulse.prompts.map(o=>({k:String(o.n),label:`Prompt ${o.n} (${o.label})`,text:o.text}))];
  const o=all.find(x=>x.k===String(id));if(!o)return;
  if(!o.text){toast(o.label+' text not found in the prompts file');return}
  const done=()=>toast(`${o.label} copied. Paste it into a new Copilot chat.`);
  const fall=()=>{const ta=document.getElementById('cpt'+id);if(!ta)return toast('Copy blocked: open the text and copy it');ta.closest('details').open=true;ta.focus();ta.select();try{document.execCommand('copy')?done():toast('Text selected: press Cmd-C to copy '+o.label)}catch(e){toast('Text selected: press Cmd-C to copy '+o.label)}};
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(o.text).then(done,fall);else fall()}
/* ---------- Weekly review workbook (2026-10-27): generate for the team, read the returned copy back ---------- */
let RV=null,RVP=null;
async function openReview(){try{RV=await (await fetch('/api/review')).json()}catch(e){toast('Could not load the review status');return}
  SEL=null;RVP=null;renderReview();showDrawer('review');$('#drawer').scrollTop=0;render()}
function renderReview(){const wb=RV.workbook;const sent=RV.sent.slice().reverse();const ret=RV.returned.slice().reverse();
  const hist=[...sent.map(s=>`<li><span>Sent ${fmt(s.date)}</span><span>workbook generated</span></li>`),...ret.map(r=>`<li><span>Read back ${fmt(r.date)}</span><span>${r.applied} change${r.applied===1?'':'s'}, ${r.created} new · ${esc(Object.entries(r.by_reviewer||{}).map(([k,v])=>k+' '+v).join(', '))}</span></li>`)].join('')||'<li><span>Nothing yet</span><span></span></li>';
  const pv=RVP?renderPreview(RVP):'';
  $('#panel').innerHTML=`<div class="p-top">${head('','Weekly review')}<h2 class="p-title">Weekly Pulse review · ${esc(RV.weekday)}</h2></div>
   <div class="p-sec"><h3 class="p-label">1 · Send (Wednesday)</h3><div class="cp"><div class="cp-m">Generates this week's workbook from the live Pulse: one row per issue, pre-filled; only Owner, Sev, Next action, Verdict, Comment and Reviewed by are unlocked. Put it in the shared team space and post the link; never email the file.${wb?` Current: <b>${esc(wb.file)}</b>, ${wb.rows} rows.`:''}</div>
     <a class="btn primary" href="/api/review/workbook?date=${RV.today}" download>Download this week's workbook</a></div></div>
   <div class="p-sec"><h3 class="p-label">2 · Read back (Monday)</h3><div class="cp"><div class="cp-m">Download the returned copy from the team space and drop it here. You see every changed row before anything is filed; nothing is written until you apply.</div>
     <input type="file" id="rvfile" accept=".xlsx" style="font-size:13px"> <button type="button" class="btn" data-rvup>Preview changes</button></div>${pv}</div>
   <div class="p-sec"><h3 class="p-label">History</h3><ul class="cp-f">${hist}</ul></div>`}
function renderPreview(p){const rvs=[...new Set(Object.values(RV.reviewers.development).flat().concat(Object.values(RV.reviewers.delivery).flat()))].sort();
  const sel=(v,k)=>`<select data-rvwho="${k}">${['<option value="">(skip)</option>',...rvs.map(r=>`<option${r===v?' selected':''}>${esc(r)}</option>`)].join('')}</select>`;
  const row=c=>{const d=c.diff;const bits=Object.entries(d).map(([f,[a,b]])=>f==='comment'?`<div><b>comment:</b> ${esc(b)}</div>`:f==='verdict'?`<div><b>${esc(b)}</b></div>`:`<div><b>${esc(f.replace('_',' '))}:</b> <s>${esc(a||'none')}</s> → ${esc(b||'none')}</div>`).join('');
    const bad=c.warnings.some(w=>/not on the reviewer list|not a reviewer for|no reviewer name/.test(w));
    return `<li class="rv-row${c.warnings.length?' warn':''}"><div class="rv-h"><button type="button" class="ttl" data-open="${esc(c.id)}">${esc(c.id)}</button> ${esc(c.title)}</div><div class="rv-d">${bits}</div><div class="rv-w">${c.warnings.map(w=>`<span>${esc(w)}</span>`).join('')}</div><div class="rv-a">Reviewer ${sel(bad?'':c.reviewer,c.id)}</div></li>`};
  const nrow=(n,i)=>`<li class="rv-row${n.warnings.length?' warn':''}"><div class="rv-h">NEW · ${esc(n.title)}</div><div class="rv-d"><div>${esc(n.team||'team not set')} · owner ${esc(n.owner||'none')} · ${esc(n.sev)}</div></div><div class="rv-w">${n.warnings.map(w=>`<span>${esc(w)}</span>`).join('')}</div><div class="rv-a">Raised by ${sel(n.warnings.length?'':n.by,'new'+i)}</div></li>`;
  const miss=p.missing_rows.length?`<div class="cp-m">${p.missing_rows.length} row${p.missing_rows.length===1?'':'s'} from the sent workbook not found in the returned copy (deleted or filtered out when saved): ${esc(p.missing_rows.join(', '))}.</div>`:'';
  const rej=p.rejected.length?`<div class="cp-m">Ignored: ${esc(p.rejected.map(r=>r.id+' ('+r.reason+')').join('; '))}.</div>`:'';
  return `<div class="cp need"><div class="cp-h"><b>${esc(p.file)}</b><span class="cp-b y">${p.changes.length} changed row${p.changes.length===1?'':'s'}, ${p.new.length} new</span></div>
    <div class="cp-m">Sent ${fmt(p.manifest_date)} with ${p.rows_sent} rows; ${p.rows_seen} came back. By reviewer: ${esc(Object.entries(p.by_reviewer).map(([k,v])=>k+' '+v).join(', ')||'none')}.</div>${miss}${rej}
    ${p.changes.length+p.new.length?`<ul class="rv-list">${p.changes.map(row).join('')}${p.new.map(nrow).join('')}</ul><button type="button" class="btn primary" data-rvapply>Apply selected and commit</button> <span class="hint">Each accepted row gets a dated line in the reviewer's name; rows set to (skip) are left as they are.</span>`:'<div class="cp-m">Nothing changed in this copy.</div>'}</div>`}
async function uploadReview(){const f=$('#rvfile').files[0];if(!f){toast('Choose the returned .xlsx first');return}
  const r=await fetch('/api/review/upload?name='+encodeURIComponent(f.name),{method:'POST',headers:{'Content-Type':'application/octet-stream'},body:await f.arrayBuffer()});const j=await r.json();
  if(!r.ok){toast(j.error||'Could not read the workbook');return}RVP=j;renderReview();render()}
async function applyReview(){if(!RVP)return;const accept=[];
  document.querySelectorAll('[data-rvwho]').forEach(s=>{const k=s.dataset.rvwho;if(!s.value)return;accept.push(k.startsWith('new')?{new:+k.slice(3),reviewer:s.value}:{id:k,reviewer:s.value})});
  if(!accept.length){toast('No rows selected');return}
  const r=await fetch('/api/review/apply',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({saved_as:RVP.saved_as,accept})});const j=await r.json();
  if(!r.ok){toast(j.error||'Apply failed');return}
  toast(`Filed ${j.applied.length} change${j.applied.length===1?'':'s'}, ${j.created.length} new · ${j.git}`);await openReview();await load()}

async function openHelp(sec){const j=await (await fetch('/api/guide')).json();SEL=null;
  $('#panel').innerHTML=`<div class="p-top">${head('','Help')}</div><div class="p-sec md">${md(j.markdown)}</div>`;
  showDrawer('help');$('#drawer').scrollTop=0;render();
  if(sec){const hs=[...document.querySelectorAll('#panel h2, #panel h3')];const h=hs.find(x=>x.textContent.trim().startsWith(sec));if(h)setTimeout(()=>h.scrollIntoView({block:'start'}),30)}}
$('#helpBtn').onclick=()=>openHelp('');
load();
/* ---------- Live refresh (2026-10-20): re-fetch when the files change, never while you are editing ---------- */
let VER=null;
function busy(){const ae=document.activeElement;const typing=ae&&(ae.tagName==='INPUT'||ae.tagName==='TEXTAREA');return !!(DRAWER||SHEET||typing)}
async function checkVersion(){try{const j=await (await fetch('/api/version',{cache:'no-store'})).json();
  if(VER===null){VER=j.version;return}
  if(j.version!==VER){if(busy())return;VER=j.version;await load();if(VIEW==='products'){await loadProducts('');render()}if(VIEW==='briefs')render();toast('Updated from the files')}}catch(e){}}
setInterval(checkVersion,30000);
document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')checkVersion()});
window.addEventListener('focus',checkVersion);
/* ?theme=light|dark forces a scheme (useful for screenshots); ?open=ID opens an item after load. */
(()=>{const t=new URLSearchParams(location.search).get('theme');if(t)document.documentElement.dataset.theme=t})();
