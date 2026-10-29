#!/usr/bin/env python3
"""EOS smoke test (added 2026-10-29, from the 2026-10-28 architecture review).

Runs in seconds against the real data: loads every item file, regenerates the views without writing, builds the
summary behind every web-app tab, and asserts invariants drawn from past failures. The watcher in eos_server.py runs
it in a subprocess before restarting on a code change; if it fails the old code keeps running and the commit says so.
The morning brief runs it once before touching evidence.

Two kinds of finding:
  FAIL  a hard invariant (parse, unique IDs, every tab builds, no negative product age, ...). Blocks the restart.
  LEGACY a value rule broken by an item that was already breaking it when the rule was written. Recorded in
        Tools/smoke_baseline.json and reported, never blocking. The same rule broken by any other item is a FAIL,
        so the data can only get cleaner (a ratchet). `--rebaseline` rewrites the baseline from the current data;
        use it only after deciding the new violations are acceptable legacy, never to make a red run green.
  WARN  process limits (register caps) and baseline entries that no longer violate. Informational.

Usage: python3 Tools/eos_smoke.py [--rebaseline] [--quiet]     exit 0 = pass, 1 = fail, 2 = crashed
Each new bug becomes one more assertion here.
"""
from __future__ import annotations
import json
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import eos_registers as R  # noqa: E402

BASELINE = Path(__file__).resolve().parent / "smoke_baseline.json"

ALLOWED = {
    ("action", "status"): {"open", "closed", "dropped", "aged_out"},
    ("action", "register"): {"A", "other"},
    ("watch", "status"): {"open", "closed"},
    ("watch", "tier"): {"active", "passive", "retired"},
    ("watch", "severity"): {"High", "Medium", "Low", ""},
    ("decision", "tier"): {"radar", "backlog"},
    ("decision", "status"): {"", "open", "closed", "dropped", "made", "Approaching", "Approaching, unforumed", "Complete"},
    ("pulse", "status"): {"live", "quiet", "resolved", "dropped"},
    ("pulse", "severity"): {"High", "Medium", "Low"},
    ("pulse", "escalation"): {"", "candidate", "asked", "declined", "escalated"},
    ("pulse", "coverage"): {"", "none", "unknown", "partial", "covered"},
}
CAPS = {"watch_active": 20, "radar": 20, "register_a": 15}


class Report:
    def __init__(self, baseline: dict):
        self.baseline = baseline
        self.fails: list[str] = []
        self.legacy: list[str] = []
        self.warns: list[str] = []
        self.ok: list[str] = []
        self.seen_keys: set[str] = set()

    def fail(self, msg: str):
        self.fails.append(msg)

    def warn(self, msg: str):
        self.warns.append(msg)

    def value(self, key: str, msg: str):
        """A value-rule violation keyed by rule:id. In the baseline it is legacy; otherwise it fails."""
        self.seen_keys.add(key)
        (self.legacy if key in self.baseline else self.fails).append(f"{msg}  [{key}]")

    def passed(self, msg: str):
        self.ok.append(msg)


def _load_baseline() -> dict:
    if BASELINE.exists():
        try:
            return json.loads(BASELINE.read_text(encoding="utf-8"))
        except Exception as e:  # a broken baseline must not turn every run red silently
            return {"__error__": str(e)}
    return {}


# ----------------------------------------------------------------------------- checks

def check_items(rep: Report):
    """Every item file parses, its id matches the file name, ids are unique, field values are allowed."""
    items = []
    seen = {}
    for kind in R.KINDS:
        d = R.REG_DIR / kind
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            try:
                meta, body = R.read_item(p)
            except Exception as e:
                rep.fail(f"{p.relative_to(R.ROOT)} does not parse: {e}")
                continue
            iid = str(meta.get("id") or "")
            if iid != p.stem:
                rep.fail(f"{p.relative_to(R.ROOT)}: id '{iid}' does not match file name")
            if iid in seen:
                rep.fail(f"duplicate id {iid}: {seen[iid]} and {p.relative_to(R.ROOT)}")
            seen[iid] = p.relative_to(R.ROOT)
            if not str(meta.get("title") or "").strip():
                rep.value(f"title:{iid}", f"{iid}: no title")
            for (k, f), allowed in ALLOWED.items():
                if k == kind and f in meta:
                    v = "" if meta[f] is None else str(meta[f])
                    if v not in allowed:
                        short = v if len(v) <= 60 else v[:57] + "..."
                        rep.value(f"{f}:{iid}", f"{iid}: {f}='{short}' not in {sorted(allowed)}")
            items.append((meta, body, p))
    rep.passed(f"{len(items)} item files parse; ids unique and match file names")
    return items


def check_actions(rep: Report, items):
    a_open = 0
    for meta, body, p in items:
        if p.parent.name != "action":
            continue
        iid = meta["id"]
        st = str(meta.get("status") or "")
        if st in ("closed", "dropped", "aged_out") and not meta.get("closed_date"):
            rep.value(f"closed_date:{iid}", f"{iid}: status {st} but no closed_date")
        if st == "open" and meta.get("register") == "A":
            a_open += 1
            if not meta.get("due") and not meta.get("trigger"):
                rep.fail(f"{iid}: open Register A item with no due date and no trigger (dating rule)")
    if a_open > CAPS["register_a"]:
        rep.warn(f"Register A open = {a_open}, cap {CAPS['register_a']} (disposal sweep due)")
    rep.passed(f"Register A: {a_open} open, all dated or triggered")


def check_pulse(rep: Report, items):
    import eos_pulse as P
    forums = {f["key"]: f for f in P.load_forums()}
    tracks = {t.get("key") for t in P.load_tracks()}
    accounts = [a for a in P.load_accounts()]
    names = {a["name"] for a in accounts}
    pinned = [a["name"] for a in accounts if a.get("pinned")]
    if len(pinned) != 1:
        rep.fail(f"_accounts.json: exactly one pinned account expected, found {pinned}")
    for k, f in forums.items():
        if f.get("track") not in tracks:
            rep.fail(f"_forums.json: forum '{k}' has track '{f.get('track')}' not in {sorted(t for t in tracks if t)}")
    live = 0
    for meta, body, p in items:
        if p.parent.name != "pulse":
            continue
        iid = meta["id"]
        if P.is_knowledge(meta):
            continue
        if meta.get("status") == "live":
            live += 1
        fkey = str(meta.get("forum") or "")
        if not fkey:
            rep.fail(f"{iid}: Pulse issue with no forum (it sits in no governance track; 2026-10-28 defect)")
        elif fkey not in forums:
            rep.fail(f"{iid}: forum '{fkey}' is not in _forums.json")
        if not meta.get("first_seen"):
            rep.fail(f"{iid}: Pulse issue with no first_seen (account trend cannot place it)")
        acc = str(meta.get("account") or "")
        if acc and acc not in names:
            rep.fail(f"{iid}: account '{acc}' is not a roster name in _accounts.json")
    rep.passed(f"Pulse: {live} live issues, every one with a known forum, first_seen and roster account")


def check_products(rep: Report, items):
    import eos_products as PR
    roster = PR.load_roster()
    pnames = {p["name"] for p in roster.get("products", [])}
    for meta, body, p in items:
        prod = str(meta.get("product") or "")
        if prod and prod not in pnames and meta.get("status") not in ("closed", "dropped", "aged_out"):
            rep.value(f"product:{meta['id']}", f"{meta['id']}: product '{prod}' is not a roster name")
    for w in (7, 14, 30):
        s = PR.summary(w)
        for c in s.get("products", []):
            age = c.get("age_days")
            if isinstance(age, (int, float)) and age < 0:
                rep.fail(f"Products tab: {c.get('name')} age_days={age} (negative; the 2026-10-28 185d bug)")
    rep.passed(f"Products tab builds for 7/14/30-day windows; {len(pnames)} roster products, no negative ages")


def check_generated(rep: Report, items):
    """The generated views are rebuilt (without writing) and carry every item their tier says they should."""
    import eos_pulse as P
    acts = [i for i in items if i[2].parent.name == "action"]
    watches = [i for i in items if i[2].parent.name == "watch"]
    decs = [i for i in items if i[2].parent.name == "decision"]
    t05 = R.generate_05(acts)
    t04 = R.generate_04(watches)
    t03 = R.generate_03(decs, (R.ROOT / "03_Decision_Log.md").read_text(encoding="utf-8"))
    t11 = P.generate_view()
    for name, t in (("05", t05), ("04", t04), ("03", t03), ("11", t11)):
        if not t or len(t) < 200:
            rep.fail(f"generated {name} came back empty")
    miss = []
    n_a = n_w = n_r = 0
    for meta, body, p in items:
        k = p.parent.name
        iid = meta["id"]
        if k == "action" and meta.get("status") == "open" and meta.get("register") == "A":
            n_a += 1
            if iid not in t05:
                miss.append(("05", iid))
        if k == "watch" and meta.get("tier") == "active" and meta.get("status") == "open":
            n_w += 1
            if iid not in t04:
                miss.append(("04", iid))
        if k == "decision" and meta.get("tier") == "radar" and str(meta.get("status") or "") not in ("closed", "dropped"):
            n_r += 1
            if iid not in t03:
                miss.append(("03", iid))
    for view, iid in miss:
        rep.fail(f"generated {view} does not contain open item {iid}")
    if n_w > CAPS["watch_active"]:
        rep.warn(f"Watch Active = {n_w}, cap {CAPS['watch_active']}")
    if n_r > CAPS["radar"]:
        rep.warn(f"Decision Radar = {n_r}, cap {CAPS['radar']}")
    rep.passed(f"generated views 03/04/05/11 rebuilt in memory; 05 carries all {n_a} Register A, 04 all {n_w} Active, 03 all {n_r} Radar items")


def check_tabs(rep: Report):
    """Every summary the web app's tabs call, built once each. eos_server is imported, never started."""
    import eos_pulse as P
    import eos_server as S
    P.summary()
    S.copilot_all()
    S.copilot_prompts()
    S.review_status()
    S.list_briefs()
    S.recent_log(5)
    S.data_version()
    if not isinstance(S.HTML, str) or "<html" not in S.HTML.lower():
        rep.fail("eos_server.HTML is not a page")
    rep.fail("DELIBERATE smoke failure to prove the watcher gate")
    rep.passed("every tab summary builds: Pulse, Copilot, Review, Briefs, log, version, page")


# ----------------------------------------------------------------------------- runner

def run(rebaseline: bool = False) -> tuple[bool, list[str]]:
    base = _load_baseline()
    rep = Report({} if rebaseline else base)
    if "__error__" in base:
        rep.fail(f"smoke_baseline.json does not parse: {base['__error__']}")
    items = None
    try:
        items = check_items(rep)
        for name, fn in (("actions", check_actions), ("pulse", check_pulse), ("products", check_products),
                         ("generated", check_generated)):
            try:
                fn(rep, items)
            except Exception:
                rep.fail(f"{name} check crashed:\n" + traceback.format_exc().strip())
        try:
            check_tabs(rep)
        except Exception:
            rep.fail("tabs check crashed:\n" + traceback.format_exc().strip())
    except Exception:
        rep.fail("items check crashed:\n" + traceback.format_exc().strip())
    if rebaseline:
        newb = {k: "legacy, accepted " + R.today() for k in sorted(rep.seen_keys)}
        BASELINE.write_text(json.dumps(newb, indent=1) + "\n", encoding="utf-8")
        rep.legacy, rep.fails = [f for f in rep.fails if "  [" in f], [f for f in rep.fails if "  [" not in f]
        rep.warns.append(f"baseline rewritten: {len(newb)} legacy entries")
    else:
        for k in sorted(set(base) - rep.seen_keys - {"__error__"}):
            rep.warn(f"baseline entry {k} no longer violates; remove it from smoke_baseline.json")
    lines = []
    for m in rep.fails:
        lines.append("FAIL  " + m)
    for m in rep.legacy:
        lines.append("LEGACY " + m)
    for m in rep.warns:
        lines.append("WARN  " + m)
    for m in rep.ok:
        lines.append("ok    " + m)
    verdict = f"SMOKE {'PASS' if not rep.fails else 'FAIL'}: {len(rep.fails)} fail, {len(rep.legacy)} legacy, {len(rep.warns)} warn, {len(rep.ok)} checks passed"
    lines.append(verdict)
    return (not rep.fails), lines


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    try:
        ok, lines = run(rebaseline="--rebaseline" in argv)
    except Exception:
        print("SMOKE CRASH\n" + traceback.format_exc())
        return 2
    if "--quiet" in argv:
        print(lines[-1])
    else:
        print("\n".join(lines))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
