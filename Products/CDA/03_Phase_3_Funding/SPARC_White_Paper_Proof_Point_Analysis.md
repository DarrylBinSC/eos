# SPARC/VOI White Paper — Proof Point Analysis
Source: *Operationalizing IoT Compliance and Cybersecurity for Enterprise Networks*, commissioned by SPARC/VOI, authored by Cody Remmington (Wesco). Reviewed 2026-07-29. **Nothing changed in the business case or deck pending Darryl's review.**

## Why this matters

The business case currently rests on two legs: government guidance (CISA) and technical standards (NIST). Both establish that device inventory, posture, and update management are expected. Neither establishes that **customers want a partner to do it for them.** This white paper supplies that third leg, from the buyer community rather than from Wesco marketing.

**The three-legged proof:**

| Leg | Source | What it establishes |
|---|---|---|
| Requirement | CISA OT Asset Inventory Guidance (Aug 2025, nine agencies); CPG 2.0 (Dec 2025) | Owners and operators are expected to maintain device inventory, posture, and vulnerability management |
| Standard | NIST IR 8259A | What a securable device must support: identity, secure update, configuration control, state awareness |
| **Demand** | **SPARC/VOI white paper** | **Enterprise members say they cannot operationalize this alone, and identify partner-led managed delivery as the fastest path to maturity** |

## What the paper says that supports CDA directly

Quoted or closely paraphrased from the paper:

1. **The problem statement matches ours.** Devices "enter the environment through decentralized purchasing, facilities projects, line-of-business initiatives," producing "a growing population of devices... without a consistent compliance process, clear ownership model, or standardized security baseline." Many "are unmanaged, run proprietary firmware, lack standard agents, and depend on vendors or facilities teams for maintenance," some "cannot be patched on a normal cadence," others have "unclear end-of-life timelines."
2. **Tools alone are insufficient.** "Tools can accelerate compliance, but they cannot substitute for governance." The market "is strongest at discovery, classification, profiling, posture assessment" but "less effective when organizations lack clear ownership, procurement controls, lifecycle policies, or a defined decision model."
3. **Managed delivery is named as the fastest path.** For members with "distributed estates, limited internal bandwidth, regulated operations, or complex multi-stakeholder environments, a partner-led approach can be the fastest path to operational maturity." Managed services deliver "continuous monitoring, operational triage, reporting, lifecycle coordination, and a more proactive support structure than internal teams can easily sustain."
4. **The described platform profile is our architecture.** The paper's "strongest platform profile for large enterprises" is one that can "securely operate across edge, on-premises, and cloud environments, connect fragmented systems through open integration, deliver portfolio-wide visibility, and translate data into operational action for both facilities and technology teams." That is the three deployment modes, the integration layer, and the WAM and Navigator connection.
5. **It names the operational bridge we build.** Value comes from platforms that go beyond risk identification to "unifying IT and OT data, aggregating signals from multiple building and device systems... orchestrating work orders or service workflows, and enabling portfolio-wide reporting."
6. **Risk of under-utilization argues for service, not tool.** "Expert-supported operations improve time-to-value and reduce the risk that a platform becomes underutilized after deployment." This is the argument against a customer buying a point tool instead of our service.

## Proposed proof-point construction

**One-line framing for the business case and deck:**

> Government guidance says device inventory and posture management are expected. Industry standards define what a securable device requires. And the enterprise buyer community, through SPARC/VOI, has documented that members cannot operationalize this alone and identifies partner-led managed delivery as the fastest path to maturity. Connected Device Assurance is Wesco's answer to a demand the market has now written down.

**Where it lands:**

- *Investment Description or Risks of NOT Doing:* one sentence establishing documented industry demand for partner-led delivery.
- *Additional Supporting Data:* cited as a source, described accurately (see caveat below).
- *Standards slide in the Sean deck:* add a fourth row, or a right-hand callout, converting "what guidance expects" into "and what buyers say they need."

## Caveats — how to cite it honestly

1. **Authored by a Wesco employee.** Cody Remmington wrote it; SPARC/VOI commissioned and published it. Cite it as **"commissioned by SPARC/VOI and authored by Wesco"** — that is both accurate and a credibility asset, since it shows Wesco is the recognized thought leader the industry body turned to. Presenting it as independent third-party validation would be a misstatement a reviewer could easily catch.
2. **It is explicitly vendor-neutral.** It does not endorse Wesco, CDA, or any product, and should never be quoted as if it does.
3. **It insists governance stays with the customer.** "Internal executive sponsorship and named asset ownership must still remain inside the enterprise." This *supports* our Out of Scope discipline: we do not claim to own the customer's governance, procurement policy, or risk acceptance. Worth reflecting explicitly, since it strengthens credibility rather than weakening scope.
4. **Brad Stevens sits on a SPARC board.** Relevant context for internal positioning: our Business Champion has visibility into the same demand signal. Use in conversation, not in the written case.

## DECIDED 2026-07-29 (Darryl): CDA covers the full compliance wrapper

CDA is proposed as process plus platform plus managed service. Cody's team may deliver the process and consulting portion as professional services. This is the differentiator the paper points at: tools cannot substitute for governance, so the provider who can supply both wins.

**Guardrail (from the paper, non-negotiable):** "internal executive sponsorship and named asset ownership must still remain inside the enterprise." Wesco helps design and operationalize the wrapper; the customer retains policy ownership, asset ownership, and risk acceptance. Every claim must sit on the correct side of that line.

### Proposed edits to the business case (for Darryl's review before applying)

**Investment Description — extend the chain.** Add a stage before "Identify the risk":
> *Establish the compliance framework.* Wesco helps the customer stand up the operating process that device compliance depends on: intake and registration of new devices, classification and risk review, approval and deployment standards, exception handling, and retirement policy. The customer owns the policy and the accountability; Wesco supplies the design, the workflow, and the evidence that keeps it running.

**In Scope — new group, "Compliance framework enablement":**
- Device intake and registration process design, integrated with purchasing, project intake, and facilities work orders
- Device classification and risk-review model, including managed and unmanaged determination and required controls by class
- Approval and deployment standards: network zone, identity model, and support plan per device class
- Exception register and remediation path for non-compliant and unsupported assets
- Retirement and replacement policy tied to end-of-support identification
- Evidence and reporting pack aligned to recognized guidance for audit use

**Out of Scope — sharpen rather than remove:**
- Ownership of the customer's security policy, procurement policy, or risk-acceptance decisions
- Acting as the customer's named asset owner or executive sponsor
(Replaces nothing; these make the boundary explicit now that process work is in scope.)

**Who does the work — extend:**
> Wesco Managed Services owns the service and service level. Wesco professional services deliver the compliance framework design and onboarding consulting. Delivery may be direct or through qualified partners under Wesco process, approvals, and evidence standards, with accountability retained by Wesco.

**Why Wesco — strengthen with the paper's own argument:**
> Industry guidance is clear that tools accelerate compliance but cannot substitute for governance. Wesco can supply both: the operating process, the platform that executes it, and the managed service that sustains it, on devices Wesco already sells and supports.

**Solution Analysis — dependencies:** add professional services capacity (Cody Remmington's team) as a named dependency and resource.

**Resources:** add Wesco professional services / consulting to the function list.

**Benefits:** add onboarding and advisory services revenue as an attach alongside subscription and pull-through.

**Costs:** consulting delivery is customer-funded services revenue rather than pure investment cost; the investment cost is limited to methodology, templates, and enablement development.

**Supporting data:** cite the white paper as *commissioned by SPARC/VOI, authored by Wesco*.

### Risks introduced by this expansion (state honestly)

1. **Scope creep into consulting.** Process design is bespoke by nature and resists the standardization the service model depends on. Mitigation: productize the wrapper as a fixed methodology with templates, delivered as a defined onboarding package, not open-ended consulting.
2. **Delivery capacity.** Cody's team capacity is unconfirmed and is now a dependency on the critical path.
3. **Liability drift.** Helping design a compliance process invites the assumption that Wesco is accountable for compliance outcomes. The Out of Scope additions above exist to prevent that; keep them.
