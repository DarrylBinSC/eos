#!/usr/bin/env python3
"""Reflow migrated register bodies for readability without changing words (see CLAUDE.md, Registers section)."""
import re,sys
DATE=r"20\d\d-\d\d-\d\d"
# A stamp that begins an update, when it follows a sentence end. Forms seen in the registers:
#   **2026-10-14:** / **2026-10-14 (Darryl, review pass):** / **2026-10-05, Darryl (chat): ...** / 2026-10-05, Darryl (chat): ...
#   **Update 2026-10-13 (weekly evidence):** / **New input, 2026-10-14:** / Merged into this item 2026-10-05: / **Converted 2026-10-05 (Darryl, chat):**
#   09-11 (Darryl, direct): / **09-14: reopened.**
STAMP=re.compile(r"""(?<=[.;!?)*])\s+(?=
   (?:\*\*)?(?:
      (?:Update|New\ input|Corrected|Merged\ into\ this\ item|Converted|Reopened|Closed|Promoted|Demoted|Added|Re-dated|Revised|Resolved|Flag|Evidence|Status)[ ,]+(?:[^:\n*]{0,50})?"""+DATE+r"""[^:\n]{0,80}:
    | """+DATE+r"""(?:,?\s*(?:later\s*)?\(?[A-Za-z][^:\n]{0,60}\)?)?:
    | \d\d-\d\d(?:,\s*later)?(?:\s*\([A-Za-z][^)\n]{0,40}\))?:
   ))""",re.X)
ENUM=re.compile(r"\s*\((\d{1,2}|[a-h])\)\s+")
SENT_END=re.compile(r"(?<=[.;])\s+(?=(?:\*\*)?[A-Z])")

def enum_split(part):
    pieces=ENUM.split(part)
    head=pieces[0].rstrip()
    items=[]; tail=""
    for k in range(1,len(pieces)-1,2):
        txt=pieces[k+1].strip()
        if k+2>=len(pieces):            # last item: stop at its sentence end, rest becomes a following paragraph
            m=SENT_END.search(txt)
            if m: txt,tail=txt[:m.start()],txt[m.end():]
        items.append(f"{k//2+1}. {txt}")
    out=(head+"\n" if head else "")+"\n".join(items)
    return out+("\n\n"+tail if tail else "")

def reflow_para(p):
    if re.match(r"^"+DATE+r" \([^)]+\):",p): return p      # written by the app; leave
    if p.startswith("## ") or p.startswith("- ") or p.startswith("1. "): return p
    out=[]
    for part in STAMP.split(p):
        part=part.strip()
        if not part: continue
        if len(ENUM.findall(part))>=2: part=enum_split(part)
        out.append(part)
    return "\n\n".join(out)

def reflow(body):
    paras=re.split(r"\n\s*\n",body.strip("\n"))
    return "\n\n".join(reflow_para(p) for p in paras)+"\n"

def reflow_file(txt):
    if txt.startswith("---\n"):
        e=txt.find("\n---\n",4); return txt[:e+5]+reflow(txt[e+5:])
    return reflow(txt)

if __name__=="__main__":
    sys.stdout.write(reflow_file(sys.stdin.read()))
