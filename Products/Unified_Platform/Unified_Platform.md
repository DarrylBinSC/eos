# Unified Platform (working name; Brad Stevens: "Innovance / Storefront / Wesco Connect / whatever we want to call it")

As of: 2026-09-03. **Source: Brad Stevens's meeting agenda, relayed by Darryl in session 2026-09-03.** New thread; nothing on it existed in this record before today. Forum: a meeting with Brad Stevens and Lisa Orton, week of 2026-09-08 (date to confirm).

**Darryl's stated position, 2026-09-03, and it is deliberately preserved as written: "I'm not convinced one way or another yet."** Do not record a Darryl position on the unified platform concept until he states one. Recommendations in `Deliverables/Unified_Platform/` are Claude's analysis offered for his decision, not his view.

## 1. What Brad Stevens asked, as received

Preserved close to verbatim so later drafts do not drift from the original ask.

**1. Holistic Platform** — Innovance / Storefront / Wesco Connect / whatever we call it. "A place where all our platforms reside and work together (dreaming I know but let's discuss)." The platforms Brad believes are being commercialized:

1. entroCIM
2. WAM
3. "AMD" (see §2 — almost certainly ADM)
4. Connected Safety
5. CX Connect (Liberty)
6. Navigator
7. "What else?"

**2. CX Connect** — who owns this? (Brad's working assumption: Ed, with Liberty.) Opportunities arising with the new Converging Technologies team to monitor and manage AV installs, which Brad believes is what CX Connect does. Sub-questions: should it be integrated into WAM/ADM? Can the NOC use it and offer a managed service?

**3. Navigator / entroCIM / ALM integration** — "We will be pitching all three value props as our overall service on future Facility Management / Data Center Management opportunities." Sub-questions: would be nice if they were all integrated; if not, where does one capability end and the next pick up?

**4. Ascent and third-party ALM** — the Ascent team is still using Navigator plus third-party ALM software (per Ben Pesek). "We need them to switch to WAM but make sure it is covering all services they offer and that we want to offer."

**5. WAM in the Service Center** — Manny is tired of using multiple tools as he moves to a more digital distribution capability. Pilot a WAM deal through the Service Center in Irving and Dacula; show him how simple the steps can be and the value it brings, and is demanded, by the customer (e.g. Microsoft AV). **Open commercial question, Brad's own: do we charge Operations for this tool, or is it a cost to IT, or a cost to Commercial for using the tool internally?**

## 2. Entity reconciliation — read this before drafting anything

Four naming and scope issues. Three are almost certainly transcription or shorthand; the first is substantive and changes the shape of the conversation.

- **"AMD" is ADM, and ADM is not a peer of WAM.** ADM (the internal data normalization and enrichment layer) and Strev (the customer-facing experience layer, white-labeled Revnue) are the two components *of* WAM. Listing ADM as a fifth commercializable platform alongside WAM double-counts one product and implies ADM could be sold or platformed separately, which is not the position in `Products/WAM/WAM.md`. **Correct this early and gently**; if it survives into a slide, every downstream count of "how many platforms" is wrong.
- **"ALM"** in thread 3 is Asset Lifecycle Management, the capability, not a product name. The Wesco platform is WAM; the customer-facing service name agreed 2026-08-26 is **Intelligent Asset Management Services**. In thread 3 Brad appears to mean WAM; in thread 4 he uses "third-party ALM software" to mean a competing product the Ascent team runs. Both readings are plausible and they are not the same thing. Confirm which he means before writing it down as one.
- **CX Connect: no record.** Zero hits across the entire EOS. Not a product file, not the Digital Product List as captured here, not the stakeholder map. Treat every property of it as unknown, including Brad's own belief about what it does ("which is what CX Connect does I believe?" — his uncertainty, preserved).
- **"Liberty" is ambiguous in this record.** It currently means Liberty LatAm (entroCIM pipeline, Nathan Kehr's All Hands list) and Panama Liberty (an entroCIM submeter onboarding, Register B26). Whether Brad's "CX Connect (Liberty)" is the same Liberty is unconfirmed. Do not assume it is.

## 3. What the record already holds against these threads

- **The integration Brad wants to pitch does not exist and is not near.** No production data flows between entroCIM, WAM, Navigator or CDA today. On DJ Vaughn's published roadmap, which Darryl ruled governing on 2026-08-28, entroCIM integration support in NavWork begins **Q4 2027** and facility connectivity (meters, CM points, MOP data) lands **Q2 2028**. NavWork itself is gated on the Maximo replacement completing June 2027, which is gated on the IBM renewal falling due March or April 2027. Detail: `Products/Navigator/Navigator.md`.
- **The portfolio already has an agreed statement of where one capability ends and the next begins** — the 2026-08-26 pitch package (`Deliverables/Portfolio_Admin/2026-08-26_Product_Pitches_and_Soft_Metrics.md`): entroCIM is operational and facility intelligence; WAM is asset lifecycle and commercial intelligence; Navigator is the operations system of record for Ascent's business; CDA is the connected-device managed service riding the entroCIM site connection. Thread 3's second sub-question is largely already answered, in language Darryl agreed. Reuse it rather than re-deriving it.
- **CDA is missing from Brad's list of six, and Brad was in the room for its sales review.** It has an FY27 AOP line ($246,787), an executive brief, and the only fresh external sales validation any of these platforms has (Chris Mooney and Bill Muczko, 2026-08-28). Its omission is worth a question, not an assumption: it may mean Brad does not see CDA as commercialized yet, which is defensible, or it may be an oversight.
- **Connected Safety and Spanr are placeholders, not platforms.** Both are Medium-Low confidence in this record with boundaries, architecture and deployments unvalidated; Connected Safety was described on 2026-07-20 as in limbo pending Sean Gregg's replacement. Putting Connected Safety on a commercialization list implies a readiness the record does not support.
- **Internal-use funding has no precedent here.** Thread 5's charge-Operations-or-IT-or-Commercial question has never been asked of any platform in this portfolio. Every WAM commercial figure of record is external attainment. This is a new question, not a variation of an old one.

## 4. Confidence ledger

| Item | Status |
|---|---|
| Brad wants a holistic platform concept discussed | **Confirmed** (his agenda, relayed by Darryl) |
| The meeting is next week with Brad Stevens and Lisa Orton | **Confirmed**, exact date unconfirmed |
| ADM is a component of WAM, not a separate platform | **Confirmed** in this record; Brad's list disagrees |
| No production integration exists between any two platforms | **Confirmed** |
| Ed (Liberty) owns CX Connect | **Reported by Brad as a question**, not confirmed |
| CX Connect monitors and manages AV installs | **Brad's belief, self-flagged as uncertain** |
| Ascent runs Navigator plus third-party ALM software | **Reported** (Brad, attributed to Ben Pesek); the specific product is unknown |
| Manny wants tool consolidation in the Service Center | **Reported** (Brad); Manny's role, surname and org are unknown here |
| Whether a unified platform is the right answer | **Open. No position taken by Darryl.** |

## 5. New names, all unconfirmed

**Ed** (CX Connect, with Liberty; surname and role unknown) · **Ben Pesek** (source for the Ascent third-party ALM fact; role and org unknown) · **Manny** (Service Center leadership, Irving and Dacula; surname and role unknown). Entries opened in `06_Stakeholder_Map.md`, 2026-09-03 section. **Irving and Dacula** are Wesco Service Center locations, first appearance in this record.

## 6. Open decisions and actions

Status lives in the registers, not here. `03` Decision Radar, 2026-09-03: the framing decision on what the unified platform is for; CX Connect ownership and portfolio placement; the internal-use funding model for WAM in the Service Center. `03` Decision Backlog: Ascent third-party ALM to WAM coverage assessment. `05` Register A: A38, A39, A40. `04` Active: the integrated-value-proposition exposure in thread 3.

## 7. Working material

`Deliverables/Unified_Platform/` holds the strategy work for the Brad and Lisa meeting. Nothing there is a Darryl position until he says so.
