# Drafting Prompt: AI Part Taxonomy Requirements Document

How to use this: copy everything inside the code block below into Copilot (or another approved assistant) and answer the questions it asks before it generates anything. The prompt is designed to interview you first, because the quality of the document depends almost entirely on the specificity of your answers. Where you do not know an answer, say so rather than guessing; the prompt will record it as an open item instead of inventing content.

Before you start, have available: the actual source data or a profile of it with real counts, the ADM attribute list and its current sign-off status, your review capacity in hours per week, and any governing specification that already defines a category boundary. That last item matters more than it looks. If a rule is already in force and you do not paste it in, the assistant will write its own version, and the version it writes will differ from yours in exactly the cases the rule exists to settle.

Companion documents: `Part_Taxonomy_AI_Requirements_Framework.md` (the structure and standard), `Part_Data_AI_Lessons_Learned.md` (the conditions and principles the prompt carries).

Revision: v1.1, 2026-08-13. Added the feasibility reconciliation step, three interview question groups, four known conditions, three failure modes, six constraints, and six validation criteria, following a critical review of the first document produced with v1.0. The v1.0 output was well-formed as requirements and unusable as build guidance: it stated a population, a duration and a review capacity that could not all hold, restated a settled category definition into a contradictory one, marked 78 of 79 requirements Must, and filed eighteen answerable questions as external dependencies. Every addition below targets one of those.

---

```
# Context

I am writing a Requirements Document for an AI-assisted capability that analyzes
Wesco part data and part naming taxonomy to derive structured part attributes:
whether a part is hardware, software, or another type, and any other attributes
determinable from the taxonomy and related part data.

The output must conform to Wesco's Asset Data Manager (ADM) global attribute set
on Anixter P360 and DDP P360 (Jira DDPTRK-6346). Warranty and software or
licensing attributes are global in that model, meaning any part can carry them,
so a hardware part with preloaded software carries both.

This is not a prompt-engineering exercise. The deliverable being specified is a
scalable business process with defined quality control, capable of producing the
same quality of result repeatedly, at volume, run by different people, with
evidence that it did.

# Task

Help me produce a complete, review-ready Requirements Document.

Work in three steps. Do not skip step 1 or step 2.

STEP 1: Interview me. Ask the questions in "Questions to ask me" below, in groups
of no more than five, and wait for my answers before continuing. Where an answer
is vague, incomplete, or inconsistent with another answer, ask a follow-up rather
than filling the gap yourself. Use the "Known conditions" section to challenge
answers that look implausible, and tell me directly when two of my answers cannot
both be true.

STEP 2: Reconcile the numbers before you write anything, and show me the
arithmetic. Do this as a short block in the chat and wait for my response. Take
the population size, the phase duration, the review capacity, the expected review
flag rate and the demonstrated throughput, and test whether they can all hold at
once.

  Convert review capacity into records. Hours per week times the number of weeks
  gives a minute budget. Divided by minutes per flagged record it gives the
  records that can actually be reviewed. Divided by the population it gives the
  maximum flag rate the plan permits. Show the calculation at more than one
  assumption for minutes per record. Compare the result against any measured flag
  rate I have given you.

  Convert the throughput target into a rate per working day and compare it with
  the demonstrated rate for the method I have described. State the ratio.

  Then tell me plainly whether the plan closes. If it does not, say so in that
  block, state by how much, and give me the options: reframe review capacity as a
  measurement budget rather than a queue-clearing budget, reduce the population,
  extend the duration, or add capacity. Do not offer lowering the flagging
  threshold as an option.

  Do not proceed to step 3 by recording an infeasibility as an open item. An open
  item is for something nobody knows. This is something the arithmetic already
  tells us, and hiding it in a register moves the discovery to the middle of the
  build.

STEP 3: Generate the Requirements Document using the structure, conventions and
constraints below, grounded only in my answers plus the material in this prompt.
Anything I did not answer appears in the text as [OPEN: question] and in the open
items register. Do not invent counts, accuracy figures, system names, dates,
owners, or vocabulary values.

# Goal

A document specific enough that an AI or data team can build against it, and that
I can use to objectively accept or reject what they deliver, without repeated
rounds of inadequate results caused by ambiguity in the requirements.

# Questions to ask me

Business and consumption
1. What is the business outcome in one sentence, in business terms.
2. Which system or process consumes this data, and who owns it on that side.
3. Is any of this output customer-facing, directly or indirectly.
4. What does the current state cost, in effort, cycle time, or business
   consequence.
5. Who signs acceptance of the delivered output.

Data and scope
6. Which taxonomy is in scope: the internal Wesco product taxonomy, manufacturer
   SKU naming conventions, or both. If both, how do they relate and which takes
   precedence when they conflict.
7. Which fields are available on each part record, how many records, how many
   distinct parts, how many distinct vendors, and what is the completeness rate
   of each field. Real numbers, not estimates.
8. What is the vendor concentration: what share of parts sit with the top ten
   vendors, and how many vendors have fewer than five parts.
9. What is the unit of analysis: the unique part number, the customer or order
   row, the SKU family, or the vendor.
10. Is this a one-time backfill of an existing population, an ongoing pipeline
    for incoming parts, or both.
11. What is explicitly out of scope.

Target model
12. Which ADM attributes must this capability populate, and which are out of
    scope this phase.
13. Which ADM controlled value lists are signed off, and which are still pending.
14. Are there existing assets to reuse: brand or vendor reference data, SKU
    decoding rules, or previously classified parts. If previously classified
    parts exist, how many, and how much do they overlap this population.
15. Where do the category boundaries sit, specifically between software and
    service, between an extended warranty and a support service, and between a
    license and an entitlement. Who owns those definitions.
16. Does a governing specification, team decision, or written rule already exist
    for any of those boundaries. If one does, paste it and I will quote it
    verbatim rather than writing my own version. If one exists but you cannot
    produce it, that is an open item, not permission for me to draft a
    replacement.
17. If previously classified parts exist, are they seed data, ground truth for
    accuracy measurement, or neither. They cannot be both for the same records.
18. When a value derived from the taxonomy conflicts with a value from a
    part-specific source on the same attribute, which wins, and who adjudicates.

Quality bar and capacity. Answer 19 through 23 together; I will reconcile them
against 24 and 25 in step 2, and they are the numbers most likely not to close.
19. What accuracy is required, by attribute, and what is the basis for that
    number. If no basis exists, say so; I will propose a calibration run rather
    than record fifteen open items.
20. For each attribute, which is worse: a wrong value or a blank value. This
    determines how aggressive the derivation is permitted to be.
21. What review capacity exists, in people and hours per week, to handle records
    the system flags.
22. Is that capacity intended to clear the flagged queue, or to validate a ground
    truth sample and adjudicate disagreements. These size very differently. If
    you have not considered the distinction, say so and I will show you both.
23. What is the tolerance for defects found downstream after delivery.

Operating constraints
24. What volume and timeline are targeted for this phase.
25. What throughput has this kind of work actually demonstrated to date, by what
    method, and over what period. If nothing comparable has been run, say so.
26. Where will working data and delivered output live, and what is the system of
    record.
27. Which AI platforms and tools are sanctioned, and what constraints apply to
    sending part numbers, vendor names, or customer associations to an external
    service.
28. What is the delivery mechanism to ADM or P360: API, file export, staging
    table, or not yet decided.
29. Is this phase a pilot with an exit gate, or a production build.
30. Who runs the process operationally, and is that a single person today.
31. Which of the gaps we have identified can your own team resolve, and which
    genuinely wait on someone outside it. Name the owner for each of the second
    kind. I will not file the first kind as dependencies.

# Known conditions in this data domain

These were observed in real Wesco supplier part data. Treat them as true unless I
tell you otherwise, use them to write requirements, and use them to challenge my
answers where my answers assume easier conditions than these.

- The usable source record can be as thin as two fields, a part number and a
  vendor string. Every target attribute is derived, not looked up in the source.
- Vendor names are inconsistent and abbreviated. The same brand appears as
  several distinct strings, with punctuation and corporate suffixes as noise.
  Canonical normalization must happen before any grouping or rule selection.
- Vendor names are sometimes wrong, not merely messy. There are confirmed cases
  of parts attributed to one vendor that are actually another manufacturer's
  products. The vendor field is unverified input, not a key.
- Part numbers vary in form: structured alphanumeric, purely numeric, and custom
  one-off strings with no resolvable meaning.
- Source rows outnumber unique parts. The same part recurs across customer
  populations. The fact belongs to the unique part and is inherited by rows.
- Prior answers compound. Parts resolved on an earlier population pre-covered
  hundreds of parts on each subsequent one. Reuse is the main lever on unit cost.
- Difficulty is not uniform. After the high-volume vendors are resolved, the
  residual is dominated by a long tail: one large low-information bucket plus
  hundreds of clusters of two or three parts, with materially lower yield per
  unit of effort.
- Junk and non-product rows exist in the source and should be quarantined before
  analysis effort is spent on them.
- Some parts are genuinely unresolvable. Custom and one-off numbers have no
  public or internal footprint, and more analysis does not resolve them.
- Real values fall outside the target vocabulary. Observed warranty terms include
  Lifetime, and durations not present in the fixed enum. The vocabulary will not
  cover reality on first contact.
- A defined category may have zero instances. Extended Warranty is a defined
  category that did not appear once in thousands of classified parts.
- Vendors mislabel their own products. Software, cloud platforms and licenses are
  routinely marketed as services with a term attached. This is the single most
  common classification error and must be resolved by definition before analysis
  starts.
- Source layouts differ between populations, including header position, metadata
  rows, and column arrangement. Tolerant parsing of arbitrary layouts is a source
  of silent error.
- Measured review flag rates on completed populations of this work were 8.0,
  18.7, 19.7 and 32.9 percent. Any plan assuming a materially lower rate is
  assuming an improvement nobody has demonstrated, and must say so.
- Demonstrated classification throughput with a per-part external lookup in the
  loop was roughly 5,400 unique parts over about six weeks. A target far above
  that rate implies a different method, not more effort.
- Manual research took roughly three to five minutes per part. Use one to three
  minutes per record as the working range for reviewing a flagged record unless
  I give you a measured figure.
- Review capacity is normally a measurement budget, not a queue-clearing budget.
  Clearing the flagged queue scales with the population and is unaffordable at
  volume. Validating a ground truth sample and adjudicating disagreements scales
  with the sample and is affordable. Assume the second unless I tell you
  otherwise, and state the assumption.

# Known failure modes to write requirements against

Each of these occurred. Each should be mitigated by at least one requirement.

- Weak evidence accepted at scale. Values recorded against sources naming a
  product family or a brand homepage rather than the specific part. Cost: a
  remediation pass in the hundreds of records, and loss of confidence in
  everything classified before the rule was tightened.
- Correlated quality checking. A check sharing the model, framing and input of
  the original derivation confirms it rather than testing it.
- Mechanical corruption during write. Commas inside URLs split columns during a
  merge, corrupting records invisibly. Structural integrity checking is a
  separate discipline from content review.
- Silent loss of committed work. Cloud-synced storage reverted saves without
  error. A save that returns no error is not proof of persistence.
- Work lost at the boundary of a long-running operation, because results were
  only committed at the end.
- Review backlog outgrowing review capacity, creating pressure to lower the
  flagging threshold and quietly converting a control into a formality.
- State inferred rather than recorded, so true progress had to be re-derived
  indirectly and reporting became unreliable.
- A specification whose own numbers did not reconcile. Population, duration and
  review capacity were each stated, the permitted flag rate was recorded as an
  open item to be measured later, and the arithmetic did not close by a factor of
  ten to thirty. Cost: the infeasibility surfaces in week two, when the only
  cheap response left is to weaken the flagging threshold.
- A settled definition restated in fresh words, producing a boundary that
  contradicted the rule already in force and inverted the classification of the
  most commonly misclassified item type. Cost: two runs of the same data
  disagree, and the disagreement is blamed on the model rather than the
  definition.
- Priority that did not discriminate: 78 of 79 requirements marked Must. Cost:
  the delivery team prioritizes anyway, under deadline, with no record of what
  was dropped.

# Constraints and design principles

Write requirements, not descriptions. Each requirement is one atomic statement,
uses "shall" for mandatory and "should" for desirable, is independently testable,
and states what must be true rather than which product provides it. No compound
requirements. No unverifiable adjectives such as robust, accurate, efficient, or
user-friendly unless a number is attached.

Each of the following must appear as one or more explicit requirements, not as
commentary:

- Coverage and accuracy are separate targets, stated per derivation and by vendor
  tier, never as a single blended figure.
- Unverifiable values are left blank and flagged, never filled with a plausible
  value. Blank means blank: never "N/A", "unknown", or zero.
- A value that does not map to a controlled vocabulary is flagged, never coerced
  to the nearest allowed value, and a recurring non-conformance is escalated for
  vocabulary extension.
- Derived inference and sourced fact are different evidence classes and must be
  distinguishable per record. Every record carries evidence type, source or rule
  identifier, confidence, review flag, rule version, and timestamp.
- A derivation rule may not complete records automatically until its accuracy is
  measured against a human-validated ground truth sample that was not used to
  build or tune it. State the threshold and the approving role.
- Quality assurance must be capable of disagreeing with the analysis. At least
  one method uses a different frame of reference, and its measured output is a
  disagreement rate, not a second answer.
- Deterministic conformance checks run in code on every record and block delivery
  on failure. Structural integrity on the write path is checked separately from
  content.
- Sampling is stratified by vendor tier, attribute, confidence band, and method,
  and oversamples the long tail and the low-confidence band.
- The vendor field is treated as unverified input and confirmed before it is used
  to select a derivation rule.
- Unresolvable is a terminal state routing to a business decision, not back into
  the analysis queue.
- Part-level and transaction-level facts are different layers. A part has a
  warranty duration and an effective trigger. It does not have a warranty start
  date. Dates belong to an instance of the part on an order or asset record.
- Attributes are global, not category-specific. The model shall not nest license
  fields under a software branch or make them conditional on category.
- A fact is derived once against the unique part and inherited by every row.
- Process state lives in the data, so any run determines what is done and what
  remains by reading it. Every stage is safe to re-run without duplicating work
  or corrupting prior results. Work proceeds in bounded, checkpointed units.
- A save is verified, not assumed. Delivered output is immutable and versioned.
- The permitted review flag rate must be compatible with stated review capacity.
- A human review decision that is general rather than record-specific is written
  back into the rules or reference data.
- Rules, prompts and models are versioned, every record is stamped with the
  version that produced it, and a change triggers re-validation of records
  produced under the prior version. A regression set is re-run before any change
  is adopted.
- The quality process has an available failing verdict with a defined
  consequence, and pass with follow-ups is expected to be the common outcome,
  with follow-ups tracked as work with an owner and a date.
- Precedence between evidence classes is stated, not only the distinction. Say
  which class wins when two produce different values for the same attribute on
  the same part, and name the role that adjudicates exceptions.
- The permitted review flag rate is a number in the document, computed from
  capacity per step 2, not an open item to be measured during the phase.
- The method constraint implied by the timeline is written as a requirement. If
  the rate forbids a per-part external lookup in the processing loop, say so.
- Where a target is genuinely unknown, specify a bounded calibration run that
  will produce it, with what it measures and when, rather than leaving an
  indefinite open item. One dated activity beats fifteen open registers entries.
- The disposition of any pre-existing classified work is stated: seed data,
  ground truth, or neither. It cannot be seed and ground truth for the same
  records.

Priority discipline. Must means required for acceptance of this phase, not
important or eventually necessary. Anything correct but not required for this
phase's exit gate is Should, Could, or Not this phase. Report the priority
distribution in section 1. If you find yourself marking more than about half the
requirements Must, the phase boundary has not been drawn and you should tell me
so rather than proceeding.

Register discipline. A dependency has a named owner outside the delivery team and
a status. An unanswered question the team can resolve itself is a task and does
not belong in the dependency register. Nothing appears in both the dependency
register and the open items register.

Risk discipline. Check that each mitigation points away from the defect. Where a
mitigating requirement reduces to "apply the definitions correctly" and the
definitions are the weak point, the mitigation is fictitious and the real fix is
to the definitions.

# Exemplar requirements

Write at this grain. Requirements coarser than these are not testable.

REQ-DAT-004 | Must | The solution shall treat the vendor field as unverified
input and shall confirm the manufacturer against a part-specific source or a
validated rule before the vendor is used to select a derivation rule.
Acceptance: in a stratified sample of 200 records, no record has a derivation
rule applied on the basis of an unconfirmed vendor value.
Verification: Test.

REQ-FUN-007 | Must | The solution shall state and report a separate coverage
target and accuracy target for each derivation, by vendor tier, where tiers are
defined by part count per vendor.
Acceptance: the results report shows coverage and measured accuracy by tier, and
no blended figure is presented as the accuracy of a derivation.
Verification: Inspection.

REQ-MOD-011 | Must | The solution shall record a value that does not map to an
ADM controlled value list as blank with a non-conformance flag, and shall not
substitute the nearest available value.
Acceptance: zero records contain an enumerated value outside the published list,
and every non-conforming input appears in the non-conformance report with its
original value.
Verification: Test.

REQ-QUA-003 | Must | The solution shall re-derive a stratified sample using an
input signal or method different from the primary derivation, without exposing
the primary result, and shall report the disagreement rate by attribute and by
vendor tier.
Acceptance: disagreement rate is reported per attribute, and any attribute above
the agreed threshold is withheld from automatic completion.
Verification: Demonstration.

REQ-REV-002 | Must | The solution shall not produce a review flag rate exceeding
the stated review capacity for the delivery period.
Acceptance: flagged record count per period does not exceed the documented review
capacity, and breaches are reported rather than absorbed.
Verification: Analysis.

# Output format

Produce the document with these sections. Number every requirement as
REQ-<AREA>-<nnn>, where AREA is DAT, FUN, MOD, EVD, PRC, QUA, REV, NFR, INT, or
GOV. Assign a priority of Must, Should, Could, or Not this phase.

1. Purpose, scope, and how to read this document, including requirement
   conventions and the priority scheme
2. Business context and objectives (rationale only, contains no requirements)
3. Definitions and controlled vocabulary
4. In scope and out of scope
5. Assumptions, constraints, and dependencies (three separate registers)
6. Data requirements (REQ-DAT)
7. Functional requirements: derivation and classification (REQ-FUN)
8. Data model and conformance requirements (REQ-MOD)
9. Evidence, confidence, and trust requirements (REQ-EVD)
10. Process and workflow requirements (REQ-PRC)
11. Quality assurance and verification requirements (REQ-QUA)
12. Human review and decision rights requirements (REQ-REV)
13. Non-functional requirements (REQ-NFR): throughput, cost, scalability,
    security and access, auditability, retention
14. Interface and integration requirements (REQ-INT)
15. Governance and change control requirements (REQ-GOV)
16. Acceptance criteria and phase exit conditions, including the calibration run
    where targets are not yet known
17. Risk register, each risk linked to the requirement that mitigates it
18. Sequencing: three lists. What can start immediately because it depends on
    none of the open decisions; what is blocked, on whom, and what unblocks it;
    what waits until after the exit gate. Someone should be able to begin work
    the day this document is issued without asking which part to start with
Appendix A: ADM global attribute conformance matrix
Appendix B: Requirement traceability matrix (ID, objective, priority, acceptance
            criterion, verification method, status)
Appendix C: Open items register
Appendix D: Feasibility reconciliation, showing the step 2 arithmetic and the
            resulting position on population, duration, flag rate and capacity

Section 1 also carries the priority distribution: the count of Must, Should,
Could and Not this phase.

Present requirements in tables with these columns: ID, Requirement, Priority,
Acceptance criterion, Verification method.

Use plain professional business English. No em dashes. Minimal bold. Do not use
promotional language and do not describe the document as comprehensive.

# Output delivery

Work in Markdown in the chat while we are drafting. Do not generate a file during
the interview or during the first draft, and do not generate a new file after
every change. Iteration is cheaper in Markdown and the document will go through
several passes before it is worth exporting.

When I tell you the content is agreed, produce the final document as a Word file
(.docx), formatted for review and circulation:

- Heading styles applied so the document has a navigable structure
- Requirements presented in real tables, not as text lists
- A table of contents at the front
- Page numbers
- The traceability matrix and open items register as tables

If you cannot produce a Word file directly, produce clean Markdown with proper
table syntax that converts without rework, and tell me that is what you have
done rather than presenting it as the final artifact.

# Validation criteria

Before presenting the document, check it against these and tell me where it fails
rather than silently correcting it:

1. Every requirement is atomic, testable, and free of unverifiable adjectives.
2. No requirement names a specific AI product as the mechanism.
3. Every derivation requirement has both a coverage target and an accuracy
   target, stated by tier.
4. Every requirement has an acceptance criterion and a verification method, and
   appears in the traceability matrix.
5. No number, name, date, or vocabulary value appears that I did not provide.
6. Every gap appears as [OPEN: ...] and in Appendix C, rather than being filled
   with a reasonable assumption.
7. The quality section contains at least one requirement for a check using a
   different frame of reference than the analysis, with a stated disagreement
   threshold.
8. The part-level and transaction-level boundary is stated as a requirement,
   including the treatment of start dates.
9. The vendor field is treated as unverified input in at least one requirement.
10. Unresolvable is defined as a terminal state routing to a business decision.
11. The permitted flag rate is a number, computed from stated review capacity,
    and compared against measured flag rates. It is not an open item.
12. Sections 2 and 5 contain no requirements, and sections 6 through 15 contain
    no rationale not tied to a requirement.
13. The feasibility arithmetic appears in Appendix D and the document states
    plainly whether the plan closes.
14. The throughput target is compared against a demonstrated rate, and the
    implied method constraint is written as a requirement.
15. Fewer than about half the requirements are marked Must, and the priority
    distribution is reported in section 1.
16. Every dependency has a named owner and a status, no dependency is a question
    the delivery team could answer itself, and nothing appears in both the
    dependency register and the open items register.
17. Every definition already in force is quoted with its source rather than
    paraphrased, and the defined categories in section 3 match the permitted
    value set used in section 7.
18. Precedence between evidence classes is stated as a rule.
19. Section 18 exists and someone could start work from it on the day of issue.
20. No mitigation in the risk register points at the section that creates the
    risk.

Finish with four things: the three requirements you are least confident in and
what information would resolve them; any two of my answers that appear
inconsistent with each other; any known condition from this prompt that you could
not turn into a requirement because I did not give you enough information; and a
plain statement of whether the plan closes on the step 2 arithmetic, repeated
here rather than left in Appendix D, because it is the finding most likely to be
skipped.
```
