# Research and Evidence Standard
As of: 2026-10-13. Version 0.1, proposed by Claude after the Launch Studio review; Darryl to confirm or edit.

Why this file exists. On 2026-10-07 a two-search research pass put a misattributed statistic on a slide ("CSA found 0 of 5,600 apps had basic protections"; CSA had repeated a vendor scan reported by VentureBeat) and a forecast from a vendor summary presented as a statistic. Mike Wassil's AI-researched Launch Studio package (2026-10-12, about 130 sources, evidence labeled by strength, with a change log and a counterarguments section) caught both. The gap was method, not effort. These rules close it. They apply to any figure, claim or quotation that leaves the team, and to the EOS record itself.

## 1. Sourcing rules

1. **Cite the original, not the summary.** A vendor page, a press release, a news article or a research note that repeats a figure is not the source of the figure. Follow the chain to the organization that produced the number. If the chain cannot be followed, say so on the page.
2. **Attribute to whoever did the work.** "X reports that Y found" is the honest form when X is relaying Y. Never collapse the chain into "X found."
3. **Paywalled or unseen originals are forecasts or claims, not facts.** Label them ("Gartner forecast, via secondary summary; original not read") on the slide, not only in the notes.
4. **Numbers must reconcile within the source.** A headline that says 5,000 and a body that says 5,600 is a flag, not a rounding difference. Do not use a figure that disagrees with itself.
5. **One figure, one basis.** Survey self-reports, controlled trials, company case studies and forecasts do not carry the same weight and are not placed side by side as if they did.

## 2. Evidence labels (use on anything outbound; the briefing's Evidence Basis column already does this for internal items)

| Label | Meaning | Treatment |
|--|------|------|
| Internal requirement | A Wesco document says it today | Cite the document and version; reconfirm currency before calling anything operational |
| External finding | Survey, trial or analysis by a named research body | Quote the figure with n and date; note self-report where it applies |
| Company-reported | A company or its vendor reports its own result | Say "company-reported"; no independent audit assumed |
| Forecast | A prediction | Label as forecast; never as a statistic |
| Proposed design | Our recommendation | Mark as proposed; not current policy |
| Open question | Could not confirm | Needs an owner and a date |

## 3. Required sections in a decision memo, proposal or case that goes upward or across an organizational boundary

- **Claims table:** claim, evidence, the safe conclusion, and the leap we are not making. One row per load-bearing claim.
- **Counterarguments:** the strongest case against, with evidence, and the response. Not a risk list; the actual opposing argument.
- **What exists today:** before asserting a gap, map the current process, owners and documents. "There is no path" is a claim that needs the map behind it. (The Gap slide of the 10-12 deck asserted no owned path while the Questions slide asked what reviews already exist.)
- **What this does not claim:** one short paragraph.
- **Source corrections:** when a draft revises an earlier document, list what was removed or relabeled and why. Corrections are visible, never silent.
- **Currency caution** on any internal document cited: version, date, and whether it has been reconfirmed.

## 4. Research method

- **Write the brief before the research.** Scope, questions, sources to prefer and avoid, internal documents to read, audience, and the form of the output. The brief is a filed artifact (`Deliverables/<initiative>/YYYY-MM-DD_<topic>_Research_Brief.md`) and is portable to any tool, which matters because Darryl works across several. Mike's package was built from such a brief; ours was built from two searches.
- **Run a research pass before a position deck, not after.** For anything that will carry external evidence, run the deep-research skill (or an equivalent tool) from the brief, save the raw output to `Evidence/` untouched, and build from it. Two searches and two page fetches are a scoping check, not research.
- **Read the internal landscape first.** For any governance, process or operating-model proposal, read the existing Wesco documents (AI Council FAQ, intake and C2P material, sandbox policy, security standards) and the EOS decision log before asserting what is missing.
- **Check the vocabulary.** Find the terms leadership already uses and use them ("AI Builders Guild," "AI-assisted building"), per the standing rule to use the requester's words.
- **Verify before it goes on a slide.** Any figure on a slide gets a second look against its original before delivery. A caveat in the speaker notes does not count.

## 5. Detail matched to maturity (cross-reference)

Research depth and deliverable depth are different things. Research should be thorough early, because that is when a wrong number is cheapest to remove. The deliverable stays short while the idea is being explored; see `Communication_Preferences.md`, "Match graphic detail to the maturity of the idea." A one-page brief with a claims table can rest on 50 sources.

## 6. When reviewing someone else's AI-researched document

- Ask for the brief that produced it. The brief is the clearest statement of intent.
- Judge the evidence labels and the change log before the conclusions; a package that corrects its own sources is more trustworthy than one that does not, and more trustworthy than one that corrects only ours.
- Separate what the research supports from what the authoring organization is proposing. Mike's decision-rights and funding changes were design choices, not research findings, and his own appendix B says so.
- Check named examples that touch the portfolio (the six candidate pilots on his slide 21) against the register before treating them as demand evidence.
