#!/usr/bin/env python3
"""
brief_readability.py: scan a briefing .md before it is saved (added 2026-10-19).

Why: the 2026-10-19 weekly scored grade 10.8 (fine for the reader) but 21 of its 32 text
blocks ran past 80 words, the longest 245. The briefs were hard to scan, not hard to
understand. The rule (CLAUDE.md, Daily Briefing Workflow; Reference/Communication_Preferences.md):
  - a paragraph or bullet stays at or under 60 words;
  - a sentence stays at or under 35 words;
  - a priority puts each labelled field (Business impact, Why you personally, Risk if delayed,
    Next step, Expected outcome) on its own line or as a labelled bullet.
Tables, callout source notes, code and Mermaid blocks are not scored.

Usage (from the EOS root):  python3 Tools/brief_readability.py Briefings/2026-10-19_Weekly.md
Exit code 1 if anything breaks the limits, so it can gate a save. Standard library only.
"""
import re
import sys

PARA_MAX, SENT_MAX = 60, 35


def syllables(w: str) -> int:
    w = w.lower()
    if not w[:1].isalpha():
        return 2
    n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and n > 1:
        n -= 1
    return max(1, n)


def blocks(md: str):
    md = re.sub(r"```.*?```", "", md, flags=re.S)
    md = re.sub(r'::: \{custom-style="(Source Note|Image Caption)"\}.*?\n:::', "", md, flags=re.S)
    md = re.sub(r"^:::.*$", "", md, flags=re.M)
    out, cur, section = [], [], ""
    for line in md.splitlines() + [""]:
        s = line.strip()
        if s.startswith("#"):
            section = s.lstrip("# ")
        if not s or s.startswith(("#", "|")) or re.match(r"^(- |\d+\. )", s):
            if cur:
                out.append((section, " ".join(cur)))
                cur = []
            if re.match(r"^(- |\d+\. )", s):
                cur = [re.sub(r"^(- |\d+\. )", "", s)]
            continue
        cur.append(s)
    return out


def main(path: str) -> int:
    text = open(path, encoding="utf-8").read()
    bl = blocks(text)
    plain = re.sub(r"[*`]", "", " ".join(b for _, b in bl))
    words = re.findall(r"[A-Za-z][A-Za-z'-]*|\d[\d.,/-]*", plain)
    sents = [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", plain) if len(s.split()) > 2]
    W, N = len(words), max(1, len(sents))
    S = sum(syllables(w) for w in words)
    grade = 0.39 * W / N + 11.8 * S / max(1, W) - 15.59
    long_blocks = [(sec, b) for sec, b in bl if len(b.split()) > PARA_MAX
                   and len(re.findall(r"(Business impact|Why you personally|Risk if delayed|Next step|Expected outcome):", b)) < 2]
    long_sents = [s for s in sents if len(s.split()) > SENT_MAX]
    # Priority cards (two or more field labels) are rendered one field per line by the Briefs reader,
    # so they are not scored as single blocks.
    print(f"{path}: {W} words, ~{round(W / 230)} min read, grade {grade:.1f}, "
          f"{W / N:.1f} words/sentence")
    print(f"  blocks over {PARA_MAX} words: {len(long_blocks)} of {len(bl)}; "
          f"sentences over {SENT_MAX} words: {len(long_sents)}")
    for sec, b in long_blocks[:12]:
        print(f"  - [{sec[:40]}] {len(b.split())} words: {b[:90]}...")
    for s in long_sents[:8]:
        print(f"  - sentence, {len(s.split())} words: {s[:90]}...")
    return 1 if long_blocks or long_sents else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]) if len(sys.argv) > 1 else 2)
