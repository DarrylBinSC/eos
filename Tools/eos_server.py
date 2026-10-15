#!/usr/bin/env python3
"""
eos_server.py — local web app over the EOS register item files.

Serves a triage view of Registers/<kind>/<ID>.md on the LAN, writes edits straight back to the
item files, regenerates 03/04/05, and commits each change to git so the next briefing can read
`git log` to see what Darryl changed. Standard library only.

Run from the EOS root (the launcher Tools/eos-server.command does this):
    python3 Tools/eos_server.py            # http://0.0.0.0:8765
Env:
    EOS_PORT      default 8765
    EOS_BIND      default 0.0.0.0 (LAN). Use 127.0.0.1 to restrict to this Mac.
    EOS_PASSWORD  unset = no login (Darryl's choice 2026-10-15). Set it to require HTTP Basic auth.
"""
from __future__ import annotations

import base64
import json
import os
import re
import subprocess
import sys
import threading
import datetime as dt
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

sys.path.insert(0, str(Path(__file__).resolve().parent))
import eos_registers as R  # noqa: E402

PORT = int(os.environ.get("EOS_PORT", "8765"))
BIND = os.environ.get("EOS_BIND", "0.0.0.0")
PASSWORD = os.environ.get("EOS_PASSWORD", "")
LOCK = threading.Lock()

# Fields the browser may change, per kind. Everything else is read-only from the app.
EDITABLE = {
    "action": ["title", "register", "status", "owner", "counterparty", "type", "product", "critical", "critical_reason",
               "due", "due_note", "trigger", "next_action", "basis", "source", "closed_by", "disposition_note", "needs_triage", "tags"],
    "watch": ["title", "tier", "status", "severity", "trend", "evidence_basis", "product", "next_action", "disposition_note", "needs_triage", "tags"],
    "decision": ["title", "tier", "status", "owner", "forum", "forum_date", "next_action", "source", "product", "disposition_note", "needs_triage", "tags"],
}
CLOSED_STATUSES = {"closed", "dropped", "aged_out"}


# ----------------------------------------------------------------------------- git

def git(*args) -> tuple[int, str]:
    try:
        p = subprocess.run(["git", *args], cwd=R.ROOT, capture_output=True, text=True, timeout=30)
        return p.returncode, (p.stdout + p.stderr).strip()
    except Exception as e:  # git missing, etc.
        return 1, str(e)


def git_commit(message: str) -> str:
    if not (R.ROOT / ".git").exists():
        return "no git repo"
    git("add", "-A", "--", "Registers", "03_Decision_Log.md", "04_Executive_Watch_List.md", "05_Commitments.md")
    rc, out = git("commit", "-q", "-m", message)
    return "committed" if rc == 0 else f"nothing to commit / {out[:120]}"


# ----------------------------------------------------------------------------- item ops

def item_json(meta, body, path):
    d = dict(meta)
    d["body"] = body
    d["path"] = str(path.relative_to(R.ROOT))
    return d


def apply_patch(item_id: str, patch: dict, note: str, actor: str) -> dict:
    found = R.find_item(item_id)
    if not found:
        raise KeyError(item_id)
    meta, body, path = found
    kind = meta["kind"]
    changed = []
    for k, v in (patch or {}).items():
        if k not in EDITABLE.get(kind, []):
            continue
        if k in ("critical", "needs_triage"):
            v = bool(v)
        if k == "tags" and isinstance(v, str):
            v = [t.strip() for t in v.split(",") if t.strip()]
        if meta.get(k) != v:
            changed.append(f"{k}: {meta.get(k)!r} -> {v!r}")
            meta[k] = v
    today = R.today()
    # Disposition side effects
    if "status" in (patch or {}):
        st = meta.get("status")
        if st in CLOSED_STATUSES and not meta.get("closed_date"):
            meta["closed_date"] = today
            meta.setdefault("closed_by", "")
            if not meta.get("closed_by"):
                meta["closed_by"] = f"Darryl, EOS web app, {today}"
        if st == "open":
            meta["closed_date"] = ""
            meta["closed_by"] = ""
    if kind == "watch" and "tier" in (patch or {}):
        if meta.get("tier") == "retired":
            meta["status"] = "closed"; meta.setdefault("closed_date", today)
            if not meta.get("closed_date"):
                meta["closed_date"] = today
        else:
            meta["status"] = "open"
    if note and note.strip():
        stamp = f"\n\n{today} ({actor}): {note.strip()}\n"
        body = (body or "").rstrip("\n") + stamp
        changed.append("note")
    if not changed:
        return item_json(meta, body, path)
    meta["last_touched"] = today
    import time as _t; SELF_WRITE_UNTIL[0] = _t.time() + 12
    R.write_item(meta, body)
    R.regenerate_all()
    git_commit(f"web: {item_id} — " + "; ".join(c[:60] for c in changed[:4]))
    return item_json(meta, body, path)


def create_item(title: str, note: str, kind: str = "action") -> dict:
    kind = kind if kind in R.KINDS else "action"
    iid = R.next_id("T")
    today = R.today()
    meta = {
        "id": iid, "kind": kind, "register": "triage", "tier": "", "status": "open", "title": title.strip(),
        "owner": "", "due": "", "next_action": "", "created": today, "last_touched": today,
        "needs_triage": True, "source": f"Darryl, EOS web app, {today}",
    }
    body = f"{today} (Darryl, web): {note.strip()}\n" if note and note.strip() else ""
    import time as _t; SELF_WRITE_UNTIL[0] = _t.time() + 12
    p = R.write_item(meta, body)
    R.regenerate_all()
    git_commit(f"web: new {iid} — {title.strip()[:60]}")
    return item_json(meta, body, p)


def recent_log(n: int = 30) -> list[dict]:
    rc, out = git("log", f"-{n}", "--date=short", "--pretty=format:%h\t%ad\t%s")
    if rc != 0:
        return []
    rows = []
    for l in out.splitlines():
        parts = l.split("\t", 2)
        if len(parts) == 3:
            rows.append({"hash": parts[0], "date": parts[1], "subject": parts[2]})
    return rows


# ----------------------------------------------------------------------------- HTTP

class H(BaseHTTPRequestHandler):
    server_version = "EOS/1.0"

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (dt.datetime.now().strftime("%H:%M:%S"), fmt % args))

    # -- helpers
    def _auth_ok(self) -> bool:
        if not PASSWORD:
            return True
        h = self.headers.get("Authorization", "")
        if h.startswith("Basic "):
            try:
                user, _, pw = base64.b64decode(h[6:]).decode().partition(":")
                return pw == PASSWORD
            except Exception:
                return False
        return False

    def _send(self, code: int, body: bytes, ctype="application/json; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code, obj):
        self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"))

    def _body(self) -> dict:
        n = int(self.headers.get("Content-Length", "0") or 0)
        raw = self.rfile.read(n) if n else b""
        try:
            return json.loads(raw.decode("utf-8")) if raw else {}
        except Exception:
            return {}

    def _gate(self) -> bool:
        if self._auth_ok():
            return True
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="EOS"')
        self.send_header("Content-Length", "0")
        self.end_headers()
        return False

    # -- routes
    def do_GET(self):
        if not self._gate():
            return
        u = urlparse(self.path)
        q = parse_qs(u.query)
        if u.path in ("/", "/index.html"):
            return self._send(200, HTML.encode("utf-8"), "text/html; charset=utf-8")
        if u.path == "/api/items":
            with LOCK:
                items = [item_json(m, b, p) for m, b, p in R.load_items()]
            if q.get("open", ["0"])[0] == "1":
                items = [i for i in items if i.get("status") not in CLOSED_STATUSES and i.get("tier") != "retired"]
            return self._json(200, {"items": items, "today": R.today()})
        m = re.fullmatch(r"/api/items/([A-Za-z0-9_.-]+)", u.path)
        if m:
            with LOCK:
                f = R.find_item(m.group(1))
            if not f:
                return self._json(404, {"error": "not found"})
            return self._json(200, item_json(*f))
        if u.path == "/api/log":
            return self._json(200, {"log": recent_log(int(q.get("n", ["30"])[0]))})
        return self._json(404, {"error": "no route"})

    def do_PATCH(self):
        if not self._gate():
            return
        u = urlparse(self.path)
        m = re.fullmatch(r"/api/items/([A-Za-z0-9_.-]+)", u.path)
        if not m:
            return self._json(404, {"error": "no route"})
        d = self._body()
        try:
            with LOCK:
                out = apply_patch(m.group(1), d.get("patch") or {}, d.get("note") or "", d.get("actor") or "Darryl, web")
            return self._json(200, out)
        except KeyError:
            return self._json(404, {"error": "not found"})
        except Exception as e:
            return self._json(500, {"error": str(e)})

    def do_POST(self):
        if not self._gate():
            return
        u = urlparse(self.path)
        d = self._body()
        if u.path == "/api/items":
            if not (d.get("title") or "").strip():
                return self._json(400, {"error": "title required"})
            with LOCK:
                out = create_item(d["title"], d.get("note", ""), d.get("kind", "action"))
            return self._json(201, out)
        if u.path == "/api/regenerate":
            with LOCK:
                counts = R.regenerate_all()
                msg = git_commit("regenerate 03/04/05 from Registers/")
            return self._json(200, {"counts": counts, "git": msg})
        return self._json(404, {"error": "no route"})


# ----------------------------------------------------------------------------- UI

HTML = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EOS Registers</title>
<style>
:root{--bg:#f6f7f9;--card:#fff;--ink:#1d252d;--muted:#5d6b7a;--line:#dfe3e8;--accent:#1f5fbf;--hi:#fff4e0;--crit:#b23b3b;--ok:#2a7f4f;--chip:#eef1f5}
@media (prefers-color-scheme:dark){:root{--bg:#14181d;--card:#1d232a;--ink:#e8ecf1;--muted:#9aa6b2;--line:#2c343d;--accent:#7fb0ff;--hi:#3a3020;--crit:#ff8a8a;--ok:#7fd3a0;--chip:#2a323b}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.4 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
header{position:sticky;top:0;background:var(--card);border-bottom:1px solid var(--line);padding:10px 16px;display:flex;gap:10px;align-items:center;flex-wrap:wrap;z-index:5}
header h1{font-size:17px;margin:0 8px 0 0;font-weight:650}
.chips{display:flex;gap:6px;flex-wrap:wrap}.chip{border:1px solid var(--line);background:var(--chip);border-radius:999px;padding:4px 10px;font-size:13px;cursor:pointer;user-select:none}
.chip.on{background:var(--accent);color:#fff;border-color:var(--accent)}
input,select,textarea,button{font:inherit;color:inherit}
input[type=search]{flex:1;min-width:160px;padding:6px 10px;border:1px solid var(--line);border-radius:8px;background:var(--bg)}
button{padding:6px 12px;border:1px solid var(--line);border-radius:8px;background:var(--card);cursor:pointer}button.primary{background:var(--accent);color:#fff;border-color:var(--accent)}
main{padding:12px 16px 80px;max-width:1400px;margin:0 auto}
.meta{color:var(--muted);font-size:13px;margin:4px 0 10px}
.row{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin-bottom:8px;display:grid;grid-template-columns:72px 1fr 150px 110px 150px;gap:10px;align-items:center;cursor:pointer}
.row>div{min-width:0}.row:hover{border-color:var(--accent)}.row.over{background:var(--hi)}
.id{font-family:ui-monospace,Menlo,monospace;font-size:13px;color:var(--muted)}
.title{font-weight:600}.sub{color:var(--muted);font-size:13px;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tag{display:inline-block;font-size:11px;padding:1px 7px;border-radius:999px;background:var(--chip);margin-right:4px;vertical-align:middle}
.tag.crit{background:var(--crit);color:#fff}.tag.tri{background:#e9a23b;color:#1d252d}.tag.high{background:#c0392b;color:#fff}.tag.med{background:#d68910;color:#fff}
.due{font-variant-numeric:tabular-nums}.due.past{color:var(--crit);font-weight:600}
select.inline{padding:4px 6px;border:1px solid var(--line);border-radius:6px;background:var(--bg)}
@media (max-width:820px){.row{grid-template-columns:1fr;gap:4px}.hide-m{display:none}}
/* drawer */
.drawer{position:fixed;inset:0;background:rgba(0,0,0,.35);display:none;z-index:10}.drawer.open{display:block}
.panel{position:absolute;right:0;top:0;bottom:0;width:min(720px,100%);background:var(--card);overflow:auto;padding:16px 18px 40px;border-left:1px solid var(--line)}
.panel h2{font-size:16px;margin:0 0 4px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:8px 12px;margin:10px 0}.grid label{font-size:12px;color:var(--muted);display:block}
.grid input,.grid select{width:100%;padding:6px 8px;border:1px solid var(--line);border-radius:6px;background:var(--bg)}
.grid .full{grid-column:1/-1}
textarea{width:100%;min-height:90px;padding:8px;border:1px solid var(--line);border-radius:6px;background:var(--bg)}
pre.body{white-space:pre-wrap;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:10px;font:13px/1.45 inherit;max-height:40vh;overflow:auto}
.bar{display:flex;gap:8px;align-items:center;margin:10px 0;flex-wrap:wrap}.spacer{flex:1}
.toast{position:fixed;bottom:16px;left:50%;transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:8px 14px;border-radius:8px;display:none;z-index:20}
@media (max-width:820px){.grid{grid-template-columns:1fr}}
</style></head><body>
<header>
 <h1>EOS Registers</h1>
 <div class="chips" id="views">
  <span class="chip on" data-v="triage">Triage</span>
  <span class="chip" data-v="A">Mine</span>
  <span class="chip" data-v="other">Other-owned</span>
  <span class="chip" data-v="watch">Watch</span>
  <span class="chip" data-v="decision">Decisions</span>
  <span class="chip" data-v="needs">Needs triage</span>
  <span class="chip" data-v="closed">Disposed</span>
 </div>
 <input type="search" id="q" placeholder="Search title, owner, ID, notes…">
 <button class="primary" id="newBtn">+ Add</button>
 <button id="logBtn">Changes</button>
</header>
<main>
 <div class="meta" id="meta"></div>
 <div id="list"></div>
</main>

<div class="drawer" id="drawer"><div class="panel" id="panel"></div></div>
<div class="toast" id="toast"></div>

<script>
const $=s=>document.querySelector(s);
let ITEMS=[],TODAY='',VIEW='triage',Q='';
const CLOSED=new Set(['closed','dropped','aged_out']);
const isOpen=i=>!CLOSED.has(i.status)&&i.tier!=='retired';
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function toast(t){const e=$('#toast');e.textContent=t;e.style.display='block';setTimeout(()=>e.style.display='none',1800)}
async function load(){const r=await fetch('/api/items');const j=await r.json();ITEMS=j.items;TODAY=j.today;render()}
function dueKey(i){return i.due||i.forum_date||'9999'}
function filtered(){
  let a=ITEMS;
  if(VIEW==='triage') a=a.filter(i=>isOpen(i)&&((i.kind==='action'&&(i.register==='A'||i.register==='triage'||i.critical))||(i.kind==='watch'&&i.tier==='active')||(i.kind==='decision'&&i.tier==='radar')));
  else if(VIEW==='A') a=a.filter(i=>isOpen(i)&&i.kind==='action'&&i.register==='A');
  else if(VIEW==='other') a=a.filter(i=>isOpen(i)&&i.kind==='action'&&i.register==='other');
  else if(VIEW==='watch') a=a.filter(i=>isOpen(i)&&i.kind==='watch');
  else if(VIEW==='decision') a=a.filter(i=>isOpen(i)&&i.kind==='decision');
  else if(VIEW==='needs') a=a.filter(i=>i.needs_triage);
  else if(VIEW==='closed') a=a.filter(i=>!isOpen(i));
  if(Q){const q=Q.toLowerCase();a=a.filter(i=>[i.id,i.title,i.owner,i.counterparty,i.next_action,i.body,i.forum].join(' ').toLowerCase().includes(q))}
  const kr={action:0,watch:1,decision:2};const rr={triage:0,A:1,other:2};
  if(VIEW==='closed') a.sort((x,y)=>(y.closed_date||'').localeCompare(x.closed_date||''));
  else a.sort((x,y)=>(x.needs_triage?-1:0)-(y.needs_triage?-1:0)||(kr[x.kind]-kr[y.kind])||((rr[x.register]??3)-(rr[y.register]??3))||((y.critical?1:0)-(x.critical?1:0))||dueKey(x).localeCompare(dueKey(y))||(x.last_touched||'').localeCompare(y.last_touched||''));
  return a;
}
function tags(i){let t='';
  if(i.needs_triage)t+='<span class="tag tri">needs triage</span>';
  if(i.kind==='action')t+=`<span class="tag">${i.register==='A'?'Mine':i.register==='triage'?'New':(i.type||'Other')}</span>`;
  if(i.critical)t+='<span class="tag crit">Critical</span>';
  if(i.kind==='watch')t+=`<span class="tag ${(i.severity||'').toLowerCase()==='high'?'high':(i.severity||'').toLowerCase()==='medium'?'med':''}">${esc(i.severity||i.tier)}</span><span class="tag">${esc(i.tier)}</span>`;
  if(i.kind==='decision')t+=`<span class="tag">${esc(i.tier)}</span>`;
  return t}
function statusSelect(i){
  if(i.kind==='action')return `<select class="inline" data-id="${i.id}" data-k="status"><option ${i.status==='open'?'selected':''}>open</option><option ${i.status==='closed'?'selected':''}>closed</option><option ${i.status==='dropped'?'selected':''}>dropped</option></select>`;
  if(i.kind==='watch')return `<select class="inline" data-id="${i.id}" data-k="tier"><option ${i.tier==='active'?'selected':''}>active</option><option ${i.tier==='passive'?'selected':''}>passive</option><option ${i.tier==='retired'?'selected':''}>retired</option></select>`;
  return `<select class="inline" data-id="${i.id}" data-k="tier"><option ${i.tier==='radar'?'selected':''}>radar</option><option ${i.tier==='backlog'?'selected':''}>backlog</option></select>`;
}
function render(){
  const a=filtered();
  const open=ITEMS.filter(isOpen);
  const A=open.filter(i=>i.kind==='action'&&i.register==='A').length,W=open.filter(i=>i.kind==='watch'&&i.tier==='active').length,D=open.filter(i=>i.kind==='decision'&&i.tier==='radar').length,N=ITEMS.filter(i=>i.needs_triage).length;
  $('#meta').textContent=`${a.length} shown · Register A ${A}/15 · Watch Active ${W}/20 · Radar ${D}/20 · Needs triage ${N} · ${TODAY}`;
  $('#list').innerHTML=a.map(i=>{
    const due=i.due||i.forum_date||'';const past=due&&due<TODAY&&isOpen(i);
    const sub=i.next_action||(i.kind==='decision'?(i.forum||''):'')||'';
    return `<div class="row ${past?'over':''}" data-id="${i.id}">
      <div class="id">${esc(i.id)}</div>
      <div><div class="title">${esc(i.title)}</div><div class="sub">${tags(i)}${esc(sub)}</div></div>
      <div class="hide-m sub" title="owner">${esc(i.owner||i.counterparty||'')}</div>
      <div class="due ${past?'past':''}">${esc(due)}</div>
      <div onclick="event.stopPropagation()">${statusSelect(i)}</div>
    </div>`}).join('')||'<div class="meta">Nothing here.</div>';
}
document.addEventListener('click',e=>{
  const c=e.target.closest('.chip[data-v]');if(c){document.querySelectorAll('#views .chip').forEach(x=>x.classList.remove('on'));c.classList.add('on');VIEW=c.dataset.v;render();return}
  const r=e.target.closest('.row[data-id]');if(r){openDrawer(r.dataset.id)}
});
document.addEventListener('change',async e=>{
  const s=e.target.closest('select.inline');if(!s)return;
  await patch(s.dataset.id,{[s.dataset.k]:s.value},'');
});
$('#q').addEventListener('input',e=>{Q=e.target.value.trim();render()});
async function patch(id,p,note){
  const r=await fetch('/api/items/'+encodeURIComponent(id),{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({patch:p,note:note})});
  if(!r.ok){toast('Save failed');return null}
  const j=await r.json();const k=ITEMS.findIndex(x=>x.id===id);if(k>=0)ITEMS[k]=j;toast('Saved · '+id);render();return j;
}
function field(l,k,v,type='text',opts){
  if(opts)return `<div><label>${l}</label><select name="${k}">${opts.map(o=>`<option ${o===v?'selected':''}>${o}</option>`).join('')}</select></div>`;
  return `<div><label>${l}</label><input name="${k}" type="${type}" value="${esc(v)}"></div>`}
function openDrawer(id){
  const i=ITEMS.find(x=>x.id===id);if(!i)return;
  let f='';
  f+=`<div class="full">${field('Title','title',i.title)}</div>`;
  if(i.kind==='action'){
    f+=field('Register','register',i.register,'',['A','other','triage'])+field('Status','status',i.status,'',['open','closed','dropped','aged_out']);
    f+=field('Owner','owner',i.owner)+field('Counterparty','counterparty',i.counterparty);
    f+=field('Type (other-owned)','type',i.type||'','',['','Delegated','Awaited'])+field('Critical','critical',String(!!i.critical),'',['false','true']);
    f+=field('Due (YYYY-MM-DD)','due',i.due)+field('Due note / gate','due_note',i.due_note);
    f+=field('Trigger','trigger',i.trigger)+field('Product','product',i.product||'');
    f+=`<div class="full">${field('Next action (one line)','next_action',i.next_action)}</div>`;
    f+=field('Critical reason','critical_reason',i.critical_reason||'')+field('Basis','basis',i.basis||'');
  }else if(i.kind==='watch'){
    f+=field('Tier','tier',i.tier,'',['active','passive','retired'])+field('Severity','severity',i.severity||'','',['','High','Medium','Low']);
    f+=field('Trend','trend',i.trend||'')+field('Evidence basis','evidence_basis',i.evidence_basis||'');
    f+=`<div class="full">${field('Next action (one line)','next_action',i.next_action||'')}</div>`+field('Product','product',i.product||'');
  }else{
    f+=field('Tier','tier',i.tier,'',['radar','backlog'])+field('Status (free text)','status',i.status||'');
    f+=field('Owner','owner',i.owner||'')+field('Forum date (YYYY-MM-DD)','forum_date',i.forum_date||'');
    f+=`<div class="full">${field('Forum','forum',i.forum||'')}</div><div class="full">${field('Next action (one line)','next_action',i.next_action||'')}</div>`+field('Product','product',i.product||'');
  }
  f+=field('Needs triage','needs_triage',String(!!i.needs_triage),'',['false','true']);
  $('#panel').innerHTML=`<div class="bar"><h2>${esc(i.id)}</h2><span class="sub">${esc(i.path)} · last touched ${esc(i.last_touched||'')}</span><span class="spacer"></span><button id="close">Close</button></div>
   <form id="f"><div class="grid">${f}</div>
   <label class="meta">Add a note (dated and appended to the item; this is the notes channel)</label><textarea name="note" placeholder="What happened, what you decided, what to tell Claude at the next brief…"></textarea>
   <div class="bar"><button type="submit" class="primary">Save</button><span class="meta">Saves to the file, regenerates 03/04/05, commits to git.</span></div></form>
   <h3 style="font-size:14px;margin:14px 0 6px">Notes and history</h3><pre class="body">${esc(i.body||'(empty)')}</pre>`;
  $('#drawer').classList.add('open');
  $('#close').onclick=()=>$('#drawer').classList.remove('open');
  $('#f').onsubmit=async ev=>{ev.preventDefault();const fd=new FormData(ev.target);const p={};let note='';
    for(const [k,v] of fd.entries()){if(k==='note'){note=v;continue}p[k]=(k==='critical'||k==='needs_triage')?(v==='true'):v}
    const j=await patch(id,p,note);if(j)openDrawer(id)};
}
$('#drawer').addEventListener('click',e=>{if(e.target.id==='drawer')$('#drawer').classList.remove('open')});
$('#newBtn').onclick=()=>{
  $('#panel').innerHTML=`<div class="bar"><h2>New item</h2><span class="spacer"></span><button id="close">Close</button></div>
   <form id="nf"><div class="grid"><div class="full"><label>Title</label><input name="title" required autofocus></div></div>
   <label class="meta">Note (optional)</label><textarea name="note"></textarea>
   <div class="bar"><button type="submit" class="primary">Add</button><span class="meta">Lands as a T-item flagged "needs triage"; Claude classifies it at the next brief.</span></div></form>`;
  $('#drawer').classList.add('open');$('#close').onclick=()=>$('#drawer').classList.remove('open');
  $('#nf').onsubmit=async ev=>{ev.preventDefault();const fd=new FormData(ev.target);
    const r=await fetch('/api/items',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:fd.get('title'),note:fd.get('note')})});
    if(r.ok){toast('Added');$('#drawer').classList.remove('open');await load()}else toast('Add failed')};
};
$('#logBtn').onclick=async()=>{const r=await fetch('/api/log?n=40');const j=await r.json();
  $('#panel').innerHTML=`<div class="bar"><h2>Recent changes (git)</h2><span class="spacer"></span><button id="close">Close</button></div>`+
   (j.log.length?`<pre class="body">${j.log.map(l=>esc(l.date+'  '+l.subject)).join('\n')}</pre>`:'<div class="meta">No git history yet.</div>');
  $('#drawer').classList.add('open');$('#close').onclick=()=>$('#drawer').classList.remove('open')};
load();
</script></body></html>
"""


# ----------------------------------------------------------------------------- watcher for edits made outside the app

SELF_WRITE_UNTIL = [0.0]


def _snapshot() -> dict:
    out = {}
    if R.REG_DIR.exists():
        for p in R.REG_DIR.rglob("*.md"):
            try:
                out[str(p)] = p.stat().st_mtime
            except FileNotFoundError:
                pass
    return out


def watch_registers(interval: float = 5.0):
    """Every few seconds, if item files changed (and not by this server), regenerate 03/04/05 and commit.
    This is how Claude's session edits and any text-editor edits get the same treatment as web edits."""
    import time
    last = _snapshot()
    prev = None  # the previous poll's snapshot while a change is settling
    while True:
        time.sleep(interval)
        try:
            now = _snapshot()
            if now == last:
                prev = None
                continue
            if time.time() < SELF_WRITE_UNTIL[0]:
                last = now; prev = None
                continue
            if prev is None or now != prev:  # keep waiting until two consecutive polls agree
                prev = now
                continue
            changed = sorted({Path(k).stem for k in set(now) ^ set(last)} |
                             {Path(k).stem for k in now if k in last and now[k] != last[k]})
            with LOCK:
                R.regenerate_all()
                msg = git_commit("edit outside the web app: " + ", ".join(changed[:12]) + (" …" if len(changed) > 12 else ""))
            sys.stderr.write(f"[watch] regenerated for {len(changed)} changed item(s): {msg}\n")
            last = _snapshot(); prev = None
        except Exception as e:
            sys.stderr.write(f"[watch] error: {e}\n")


def main():
    os.chdir(R.ROOT)
    # Catch up on anything changed while the server was not running.
    with LOCK:
        R.regenerate_all()
        print("startup:", git_commit("startup: regenerate 03/04/05 from Registers/"))
    threading.Thread(target=watch_registers, daemon=True).start()
    srv = ThreadingHTTPServer((BIND, PORT), H)
    print(f"EOS Registers server on http://{BIND}:{PORT}  (root: {R.ROOT})")
    print("Auth:", "password required" if PASSWORD else "none (LAN open)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
