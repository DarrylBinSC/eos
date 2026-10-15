> Imported 2026-07-14 from Darryl_Work_Context_Library_v1. EOS is master: update this file here; portable bundles are regenerated from EOS on demand.

# WAM Part Classification and Research Workflow

**Version:** 1.1  
**Last updated:** 2026-08-13  
**Last known operating context:** 2026-08  
**Sensitivity:** Internal / Confidential

## 0. AI Part Taxonomy Pilot (added 2026-08-13)

A second, distinct effort has emerged from this work: an AI-assisted capability that derives ADM global attributes from the Wesco internal product taxonomy, rather than from per-part external research. Do not conflate the two. The existing program (sections 1 to 9 below) researches supplier part sheets; the pilot parses internal taxonomy fields.

Pilot parameters as recorded in the requirements draft (reported, from Darryl's interview answers; confirm before relying on any of them):

| Parameter | Value |
|---|---|
| Population | 100,000 deduplicated unique parts, Wesco internal product taxonomy |
| Source fields | 10 per record, not yet identified |
| Duration | One month |
| Consumer | ADM, syncing to Anixter P360 and DDP P360 (DDPTRK-6346); Strev possible downstream |
| Delivery mechanism | File import |
| Operator | AI Data team |
| Acceptance authority | Akansh Gangil, ADM Product Owner |
| Human review capacity | ~4 hours per week |
| Quality stance | A wrong value is more harmful than a blank one |
| Phase type | Pilot with an exit gate, intended to become an ongoing process |
| Attributes claimed | Part classification (Hardware / Software / Service), warranty term, license term |

Measured baseline from the existing program, computed from the working files on 2026-08-13 (fact):

- 25,614 source rows, 20,364 unique parts, 2 usable fields (catalog_no, manufacturer_name), both 100% populated
- 1,065 distinct raw vendor strings; top 10 hold 25.0% of unique parts; 586 of 1,045 vendors have fewer than 5 parts, covering 5.4% of parts
- 299 unique parts carry more than one distinct vendor string; 15.7% of catalog numbers are purely numeric
- 5,436 unique parts classified across four workbooks; reference library at 69 brands and 17 SKU decoder entries
- Zero Extended Warranty instances in 5,436 classified parts
- Review flag rates observed: 8.0%, 18.7%, 19.7%, 32.9%

**Material issue (2026-08-13):** the pilot's stated review capacity of 4 hours per week is roughly 16 hours across a one-month pilot, which supports a flag rate of about 0.5% to 1.9% against 100,000 parts. Observed flag rates are 8% to 33%. The recommended resolution, per the decision brief, is to treat the capacity as a measurement budget (ground truth validation and disagreement adjudication) rather than a queue-clearing budget, and to deliver flagged records blank and counted. Not yet decided.

Governing artifacts, all in `Deliverables/WAM/` and all revised 2026-08-13:

| File | Role | Version |
|---|---|---|
| `Part_Taxonomy_ADM_Requirements_v2.0.md` | The pilot requirements. 93 requirements, 61 Must | v2.0 |
| `Part_Taxonomy_ADM_Requirements_v1.0_ChatGPT_original.md` | The ChatGPT output v2.0 replaces. Retained unedited | v1.0 |
| `Part_Taxonomy_AI_Requirements_Prompt.md` | Drafting prompt. Now interviews in 31 questions and reconciles the arithmetic before drafting | v1.1 |
| `Part_Taxonomy_AI_Requirements_Framework.md` | Structure and standard. Added feasibility reconciliation, priority and register discipline, sequencing | v1.1 |
| `Part_Data_AI_Lessons_Learned-20260813-095203.md` | Conditions and principles. Added 3 specification failure modes, principles 19 to 26 | v1.1 |
| `Part_Taxonomy_UseCase_Brief_and_Data_Model.md` | Process brief and ADM data model | v1.0 |
| `2026-08-13_Part_Taxonomy_Pilot_Decision_Brief.md` | Eight decisions for Akansh before build starts | v1.0 |

**Corrections filed 2026-08-13, from the critical review of v1.0.** Three defects in the generated requirements document drove changes back into the prompt, framework and lessons learned rather than only into the document: (1) population, duration and review capacity did not reconcile and the gap was filed as an open item; (2) the settled Software-versus-Service rule was paraphrased into a contradictory definition, so a cloud storage subscription classified as Service; (3) 78 of 79 requirements were marked Must and eighteen answerable questions were filed as external dependencies. The prompt now forces a reconciliation step before drafting and requires definitions already in force to be quoted rather than restated.

**Gating unknown:** whether the 100,000-part pilot population overlaps the 20,364 supplier parts already worked. Until that is established, the existing 5,436 classifications and the 69-brand reference library cannot be positioned as seed data, as ground truth, or as neither.

## 1. Executive Orientation

Darryl has developed a part-classification and research process to improve identification, classification, and enrichment of product and asset records for WAM-related use cases.

The project combines an HTML front end, Markdown instruction files, Python scripts, a local folder-based workflow, AI-assisted research and classification, and project-context documentation for continuity across ChatGPT and Claude.

## 2. Project Purpose

The workflow is intended to reduce manual research and improve the consistency of:

- Product classification
- Hardware versus software identification
- License and warranty interpretation
- Product descriptions
- Supplier and manufacturer research
- Asset and lifecycle metadata
- Data preparation for downstream systems

## 3. Local Project Structure

The historical local project folder was:

`Part_Research_V2_Test`

The workflow included a context file named:

`AI_Project_Context.md`

The purpose of that file is to preserve project architecture, folder conventions, workflow logic, instructions for AI tools, known limitations, current development state, and update history.

## 4. Cross-LLM Operating Model

- **Claude Cowork:** Works with the local folder, code, and file-maintenance workflow
- **ChatGPT:** Provides strategic review, prompt design, architecture critique, documentation, and cross-project continuity
- **Darryl:** Maintains control of the authoritative local repository and decides which updates are adopted

## 5. Classification Principles

The process should:

- Distinguish hardware, software, license, warranty, service, and ambiguous records
- Preserve source evidence
- Assign confidence
- Route uncertain classifications for human review
- Avoid fabricating product specifications
- Separate manufacturer evidence from inference
- Track corrections so the workflow improves
- Support enterprise-taxonomy and WAM requirements

## 6. AI and Automation Opportunities

- Manufacturer and supplier research
- Product-description normalization
- Attribute extraction
- Confidence scoring
- Duplicate and anomaly detection
- Suggested mappings
- Human-in-the-loop review
- Learning from corrections
- Batch processing and exception routing

## 7. Risks

- Web or source information may be inconsistent
- Product names and part numbers may be ambiguous
- AI can produce plausible but incorrect classifications
- Local scripts and instructions may drift apart
- Classification logic may not match MDM standards
- Supplier-specific exceptions can overwhelm general rules
- Context can be lost when moving among tools

## 8. Maintenance Standard

After meaningful workflow changes, update architecture, file map, input and output formats, classification rules, confidence logic, dependencies, known defects, test cases, change log, and instructions for Claude and ChatGPT.

## 9. Instructions for Another LLM

1. Read `AI_Project_Context.md` first.
2. Treat code and current files as the source of truth for implementation.
3. Distinguish workflow intent from current capability.
4. Do not rewrite working code merely for stylistic reasons.
5. Identify data-quality, auditability, and human-review implications.
6. Preserve compatibility with the existing folder workflow.
7. Recommend incremental changes with clear test criteria.

## Upstream truncation of manufacturer part numbers — evidenced 2026-08-25

> Routed from the 08-25 weekly evidence package, section 6b (Durable). Source: `ADM connect with Natalie`, 2026-08-25, verbatim transcript. Risk row in `04` (WAM/ADM data integrity); actions B43 and A29 in `05`.

**The defect.** DDP/EUDM selects and passes **truncated** manufacturer part numbers. WAM/ADM stores and matches on **full** manufacturer part numbers. Exact matching therefore fails, and the consequence is not a cosmetic data gap: **ADM misses orders entirely.**

**Why this belongs in the part-classification record rather than in a status log.** Every downstream claim WAM makes about install-base completeness, license visibility, renewal capture and coverage rests on the assumption that a part number arriving from upstream can be matched to a part number held here. That assumption is currently false for any truncated record, and no amount of supplier-data enrichment fixes it. The 08-25 evidence reports Exact data at 90 to 95 percent present with roughly 5,000 records inserted, and both facts are true simultaneously: supplier-data coverage is improving while the matching layer beneath it is broken.

**Ownership is the actual blocker.** Open "quite some days" as of 08-25, no named owner, no response to prior follow-up, no confirmed work item. Akansh Gangil is summarising and copying Darryl; Darryl escalates if that produces no owner. The fix sits with Daniel Totino's team and the EUDM team, outside Darryl's org, which is why this is an escalation problem rather than a backlog problem.

**Related dependency, same shape.** Software and licence catalogue **leaf nodes** needed to identify licence products for ADM onboarding have been awaited from Jen Turnage for roughly two weeks with no response (C32). Both are upstream data dependencies with no accountable owner, and they compound: incomplete catalogue identification plus unmatched part numbers means onboarding timelines expand without a single point to escalate.

**2026-10-14 update: a concrete example surfaced of the same classification gap.** Software/license products such as HALO-LIC-1YR may be omitted from the current catalog classification logic entirely, not merely delayed awaiting leaf nodes from Jen Turnage -- a distinct failure mode (omission vs. pending identification) worth distinguishing when this is escalated. Natalie Marquardt to review onboarding these products into ADM, no date stated (`05` B106). Also in the same evidence thread: the truncated-part-number question above (not this classification gap) was formally classified as an enhancement, not a defect, by Akansh Gangil's team -- see `WAM.md`, 2026-10-14, for that distinction. Source: RE: Connect for reviewing global attributes and next steps - Wesco Asset Management (email), 2026-10-13/14.

**Release context.** Pending-activation handling is targeted for production on 2026-09-01, alongside default end-user assignment, bulk end-user editing, and cancelled-order handling. Editable end-user ID follows afterwards. Supplier-specific custom fields (Exact MAC ID, Intersim data points) are planned for notifications pending stakeholder review.
