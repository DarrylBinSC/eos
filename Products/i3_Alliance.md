# i3 Alliance — Partner File

> Created 2026-08-06 from the Section 8 redline session. Reference file. Decisions live in `03`, risks in `04`, actions in `05`. Do not duplicate status here.

## Counterparty

i3 Power & Energy, LLC. Delaware LLC operating from a unit address in Mechanicsville, Virginia. Proprietary delivery methodology branded Build-to-Operate (B2O). Signing officer's block carries an FAIA architectural credential and a non-standard officer title; authority to bind not confirmed.

Wesco contact chain to date runs through Wesco Legal (Brandon Thompson) rather than directly. i3-side drafting is by Chuck Knight. Trigger for the engagement is the SECO opportunity.

## What the agreement is

A tiered partner program admitting Wesco at one elected tier. The economics are inverted relative to Wesco's normal channel position: **Wesco pays i3**, commits annual pipeline, dedicates i3-certified headcount trained on i3's curriculum at i3-set cost, and integrates its systems into i3's architecture. In return Wesco receives directory listing, a badge, tiered deal-flow priority, and view-only access to i3's planning tools.

Structurally i3 is the architect and the partner is a subcontracted capability. §5.2 makes i3 lead client representative systems architect on all Alliance projects; §13.4 makes i3 the sole Client Representative; §9.2 gives i3 final authority over system-design standards, interoperability standards, control-platform configuration, and Digital Architecture governance; §7.2 makes Portfolio access view-only at every tier with no ability to contribute.

## Tiers

| | Approved (1) | Preferred (2) | Strategic (3) |
|---|---|---|---|
| Annual fee | $10,000, waived Year 1 | $15,000 | Negotiated, blank on Schedule 1 |
| Pipeline commitment | None | $250,000 | $1,000,000 |
| Certified individuals | 1 | 3 | 5+, incl. 1 Master Partner |
| Section 8 Data Fidelity | Optional | Required in full | Required in full |
| Deal flow | Consideration only | First look, 10 business days | Right of First Refusal, named scope (scope field blank) |
| Engagement stage | Stage 3, execution | From Stage 2 | From Stage 1 |

The gate between Tier 1 and the upper tiers is not fee, headcount, or track record. It is Section 8. §§3.5, 3.6, and 8.8 make full acceptance a condition of eligibility, and §3.6 states the gate "turns solely on Section 8 and is independent of the Partner's agreement to any other provision." Every other clause can be negotiated successfully and Wesco still faces a binary architectural choice.

## Why Section 8 is the whole question

Section 8 decides whether entroCIM is the system of record on an Alliance project or a downstream consumer of i3's model. That question does not appear anywhere in the agreement as a risk term, an indemnity, or a liability allocation, which is why a careful legal read finds nothing wrong with it and why it needed a product read.

Evidence, from the tracked changes in the file Legal circulated: Chuck Knight entered 132 changes and Brandon Thompson 39, across every substantive section except one. Section 8 received zero. It is also the only section designated non-negotiable, and the only one where i3 asked Wesco to draft the language. Everything allocating risk moved. Nothing allocating control moved.

## CSS Platforms position

**Approved tier with the Section 8 election declined**, unless the negotiation floor is met. Zero cost in Year 1, one certified individual, no pipeline commitment, no architectural obligation on entroCIM, exitable on 60 days' notice under §14.4. It is a low-cost option that tests whether i3 produces real deal flow before Wesco commits anything material.

§8.7, drafted by i3, already defines how the relationship operates when Section 8 is declined, so the fallback is contractual rather than argued. Accepting it means knowingly taking a thin relationship: §3.4 confers no first look, no ROFR, no IDRP naming, no co-branded go-to-market, no roadmap pre-release, no joint development.

Position, sub-decisions, and floor: `03`, entry 2026-08-06.

## Section 8 redline, as returned

Twelve items. One preamble insertion, seven replacements (8.1–8.6, 8.8), one amendment (8.7, kept surgical because it is Wesco's fallback and i3 wrote it), four additions (8.9 Project Data and Client Data, 8.10 no derivation and residual knowledge, 8.11 ownership security and return, 8.12 i3 obligations).

Edits made inline by Darryl in a separate copy of the master document on the work machine. Supporting documents in the shared folder: `files/i3_Section8_Edits_Email.md` (team rationale), `files/i3_Section8_Redline_for_Legal.docx` (clause-level memo), `files/i3_Section8_Decisions_Log.md` (session decision trail), `files/i3_Alliance_Agreement_Review_Notes.md` (full agreement review, 08-03).

Source document: `CDK- 0728.26Master -WESCO revision 7-30.docx`, circulated 2026-07-30 with the email `i3 Alliance Agreement for SECO Opportunity`.

## Section 12 review, 2026-09-10

Second section formally reviewed. Section 8 edits came back fully accepted, and Legal asked for Section 12. Reviewed on the commercial question Darryl posed: does Section 12 restrict Wesco from working with other partners on data center development where our contacts and i3's overlap.

**Finding: the non-circumvention clause is not the problem; the IP clause inside it is.** 12.2 and 12.3 are close to workable and do not restrict ordinary competition or Wesco's general market access. 12.4 is the material restriction. It is not project-scoped, not time-limited, perpetual through §16.6, and attaches to the §6.2 Core IP definition claiming graph models, ontologies and schemas, the layer entroCIM occupies. It restricts what Wesco can deliver to any other data center partner, indefinitely, on a standard i3 defines and never has to prove. §15.2 removes the liability cap for IP claims, so it is uncapped as well as undefined. Same IP chain as the 08-06 finding (C-i3-2), surfacing a second time through a different clause.

Four defects in 12.2 that would still reach Wesco's overlap cases: the "introduced or sourced" qualifier reads onto only the second half of 12.2(a), leaving Wesco-sourced clients caught; 12.2(b) has no knowledge, intent, or client-initiated carve-out, so a developer's own decision to change providers is exposure; "i3 Project," "involvement ends," and "directly related" are all undefined, so the six-month tail has no fixed start and no fixed subject matter; and there is no exception for distribution sales, competitive procurement, or teaming. Separately, if the §1 Partner definition ("and its affiliates") carries into Section 12, every Wesco affiliate is bound by a covenant it cannot see or comply with.

**Package returned to Brandon Thompson 2026-09-10**, same three-part structure as Section 8: rationale email, clause-level memo, decision trail here and in `03`. Eight items, priority-ordered: 12.4 replacement (definition exclusions, burden of proof on i3, residual knowledge, two-year term), 12.2 replacement, entity-scope limitation inside 12.2, new 12.6 Freedom to Partner, 12.3 documentation safe harbor, strike the "made independently" qualifier on product sales, mutual remedy with notice and cure at 12.5, reciprocity at 12.1. Concession order if the round is single-pass: hold 12.4 and 12.2(b), trade 12.1 reciprocity first.

Files: `Deliverables/i3_Alliance/2026-09-10_i3_Section12_Edits_Email.md`, `..._Redline_for_Legal.md` and `.docx`.

Five questions open with Legal, all of which change the ask: the content of the Wesco Legal comment at 12.2; whether §1 carries into Section 12; what §16.6 makes perpetual; whether the Tier 3 ROFR interacts with 12.2 (not engaged at Approved tier, material if the tier position moves); and whether Section 12 is genuinely open or will be treated as settled the way Section 8 was.

## Signature path, 2026-09-15

- **Wesco signature ownership assigned to Lee Osterman.** Legal confirmed a VP may sign without Finance input because the alliance agreement itself is not expected to generate sales directly (the revenue sits in downstream projects, not the agreement). Lee Osterman, quoted: "I will sign once it comes back." This resolves the mechanical signing question but is separate from — and does not resolve — the cross-BU executive-sponsorship/ownership gap already open in `03` (2026-09-14 Decisions Needed).
- **i3's side is already executed.** Kirk Whittington confirmed the agreement was finalized and signed by the i3 team. The document is now waiting on Wesco's return.
- **Sequencing matters: Section 12 has to go back to Brandon Thompson first.** Lee's signature is on "it," meaning the fully negotiated document — the Section 12 redline drafted 2026-09-10 has not yet been sent (`05` A41, due 2026-09-11, currently overdue). Signature cannot proceed until that round closes, so A41 is the actual pacing item, not the signature step itself.
- Source: `i3 Alliance Agreement` email thread, M365 evidence 2026-09-14 to 2026-09-15.

## Near-miss on signature, 2026-09-17

- **A document reached DocuSign completion without the Section 12 and Exhibit A corrections in it, and without the Tier 3 partner obligation resolved.** M365 evidence (`FW: Complete with Docusign: WESCO_i3 Alliance Agreement.pdf`) shows Wesco Legal (Brandon Thompson) catching this before Lee Osterman signed, not after: the forwarded, DocuSign-complete document is the version that predates the 09-10 Section 12 redline, because A41 (send the redline to Brandon Thompson, due 09-11) has not shipped. **This confirms A41 is not a paperwork delay; it is the thing standing between Wesco and signing an agreement that does not contain the protections Darryl negotiated.**
- **Signature stays paused.** Kirk Whittington, i3-side, committed to correct the issues immediately: "Yes, I will reach out to them immediately." No corrected draft has been returned as of this evidence.
- **Do not treat i3's side being "already executed" (09-15, above) as reducing urgency.** It has the opposite effect: i3 is ready to close on a version Wesco has not actually finished negotiating, so the only thing preventing an unprotected signature is this catch and Lee Osterman continuing to wait for "it" to mean the corrected document.
- Recommended action: confirm directly with Brandon Thompson that A41 ships this week, and confirm with Lee Osterman that he has not signed and will not sign the DocuSign version already circulated.
- Source: `FW: Complete with Docusign: WESCO_i3 Alliance Agreement.pdf` (email), M365 evidence 2026-09-16 to 2026-09-17.

## Open items beyond Section 8

Legal confined this round of feedback to Section 8. The following were identified in the 08-03 full review and remain unaddressed.

- **Exhibit B in-kind consideration.** Pipeline commitment may be satisfied in kind, with a license to Partner technology named as the first example, valued at i3's sole discretion. Highest-consequence clause outside Section 8. `04` Passive.
- **§1 named party.** "WESCO Distribution, Inc., and its affiliates" binds the whole affiliate group. Should be narrowed to one contracting entity.
- **§6.4 and §6.5.** The license grant clause contains an unresolved editing artifact, a duplicated phrase, and an incomplete sentence; §6.5 is empty. Unenforceable as drafted.
- **§15.2 liability cap** is asymmetric (capped at fees received, which may be near zero for i3) with IP and confidentiality carve-outs removing the cap entirely.
- **§16.4 insurance** is one-directional, limits flagged as placeholders.
- **§15.4 venue** is Richmond, Virginia.
- **Drafting defects** across §§5.1, 13.1, 13.4, 14.2, 16.4 (§12 addressed separately, 09-10) — the cleanest justification for not signing as-is, requiring no substantive argument.

## Diligence not yet done

Entity standing, capitalization, and financials. Number and identity of Build-to-Operate projects actually delivered, with contactable client references. i3's insurance certificates, specifically professional liability and cyber. Confirmation of the signing officer's authority to bind. Named list of existing Alliance Partners at each tier and whether any has negotiated Section 8. Whether the Strategic "Negotiated" fee has been set for anyone.

## Cross-portfolio note

The same structural pattern appears in the JCI MSP agreement: the commercially operative terms live in material the counterparty controls unilaterally (JCI "MSP Program Materials"; i3 §8.3 standards documentation and §8.8 Program materials). See the follow-up note in the `03` entry of 2026-08-06 for the proposed standing review question.
