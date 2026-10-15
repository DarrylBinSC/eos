# Launch Studio: Meeting with Mike Wassil

Monday, October 12, 2026. Darryl Benson, Ron Snyder, Mike Wassil.

::: {custom-style="Bottom Line"}
**Bottom line:** Mike is our conduit to the vibe coders. Ron and I, as a joint team, take their concepts to real business value at the right scale. The goal for this meeting is to agree how ideas reach us and how we choose which ones to build, and to test a funded service model with Mike.
:::

## The concept

Launch Studio is the working name. The line for the vibe coders: you bring the idea, we handle the rest.


Sean proposed a company-wide capability on October 6: review vibe-coded ideas coming from the business, select two or three, and productize them at scale. Because the ideas come from the business, business support is built in.

## The challenge

Building a prototype is now easy. Turning it into software the business can rely on is not, and the industry evidence shows what happens when nobody owns that step.

- Gartner expects 60% of vibe-coded applications to be retired by 2028 because they fail to deliver predictable business value.
- Gartner also expects 30% of software engineering teams to be materially strained by maintaining applications built by citizen developers.
- The Cloud Security Alliance scanned 5,600 vibe-coded applications in production and found none with basic protections in place (CSRF protection, security headers, properly scoped access).

::: {custom-style="Source Note"}
**Sources:** Gartner, "Govern Vibe Coding for Citizen Developers With Self-Service Platforms," June 29, 2026 (read via a published summary; confirm against the original before external use). Cloud Security Alliance research note, "The Vibe Coding Governance Gap," June 2, 2026.
:::

## The job we are taking on

When a business team has built a prototype that solves a real problem, it wants that solution running reliably, securely and supported for its segment, so it gets the business result without building a software organization.

The business (CSS) knows its problems and can now prototype them. Launching and sustaining production-grade software is IT's job, and that is what our team does.

## How we are set up

| Role | Who | What it covers |
|--|------|------------|
| Conduit to the vibe coders | Mike Wassil | The vibe-coding community and idea funnel; brings concepts forward |
| Joint team leads | Darryl Benson and Ron Snyder | Selection, delivery and accountability for results |
| Product owner | David Blondel | Turns a concept into a product: scope, requirements, business value |
| Development and operations | Ron Snyder's team | Builds, secures, hosts and runs the product |

CSS Platforms covers the full path from concept to a supported product. We will start with the team we have.

## A working model to test

This is a discussion position, not a decision. It still needs review with our team and Sean's approval.

- **A product studio.** We take on a small number of ideas at a time and carry each one from prototype to supported product.
- **Funding is the filter.** An idea qualifies when the sponsoring business commits to fund the build and the ongoing run cost. That keeps selection objective and the commitment visible.
- **The prototype is the specification.** David's team treats the prototype as proof of demand and as the requirements. Ron's team rebuilds it to our engineering standards, so generated code does not go to production as is.
- **If IT touches it, IT owns it.** The business cannot own applications, so there is no halfway option. A prototype is owned by the business; a product is owned by IT. One gate sits between them.

| | Prototype | Product |
|--|--------|--------|
| Owner | The business | IT |
| Where it lives | A sandbox, with no production data | Production |
| What IT does | Nothing until the gate | Rebuilds, hosts, secures, supports and eventually retires it |
| Funding | None | A build charge plus an annual run charge, through the existing IT chargeback |

- **The gate: assess and select.** Three steps. *Screen* (Mike and David, quick): a named sponsor, a clear problem, no overlap with something we already run, and what data it touches. *Assess* (David and Ron's team, short): IT reviews the prototype and estimates the build and run cost. *Commit* (Darryl and Ron, with the sponsor): funding through the chargeback, an agreed success measure and a review date. Every submission gets one of four outcomes, with a reason: accept, fold into an existing product, defer, or return to the sandbox.
- **Prototypes already in use go through the same gate.** Anything not accepted comes off production data.
- **Going forward, a starting template and hosting standard for vibe coders,** so new prototypes are easier to productize.

## The vibe coder's experience

The vibe coder sees three touchpoints: submit the prototype and a one-page summary with their sponsor, hear back within 30 days with a clear answer and the reason, and see it launched with their name on it as originator.

They stay involved with the team at every stage: a short demo at screening, walking our architect through the prototype, sprint demos, acceptance testing, championing the launch, and prototyping the next feature in their sandbox. They never fill in a governance form and never touch production code. Launch Studio carries screening and assessment, AI Council and security review, identity, hosting and architecture review, the rebuild, release and support, and lifecycle through retirement. If IT absorbs it, compliance goes up and friction goes down.

Two boundaries keep this working:

- The originator advises and accepts; David, as product owner, decides the backlog.
- At Commit the sponsor commits the funding and the originator's time for demos and acceptance. If the originator moves on, the product continues under IT and the sponsor.

## Questions for Mike

**The funnel**

1. What is in the funnel today, how many ideas, and from which parts of the business?
2. How many of these prototypes are already in use or touching production data?
3. How should ideas come to us: format, cadence and the minimum information we need to assess one?

**Selection and funding**

4. How do we choose two or three? Candidate criteria: business value, reuse across segments, data access, security exposure and ongoing support load.
5. Has any submitting leader said they would fund the build or the ongoing run cost?
6. What happens today to an idea that is good but that nobody owns?

**Governance and follow-through**

7. What governance does a vibe-coded idea already pass through before it reaches us, and what is left for us (AI Council review, security, identity, hosting)?
8. How do we close the loop with the people who submitted ideas we do not select?
**The vibe coders**

9. Would a starting template and hosting standard help them, and who would they expect to own it?
10. Would "Launch Studio" and "you bring the idea, we handle the rest" land with them?
11. Can sponsors realistically release the originator's time for demos and acceptance?

## What Ron brings

- An early proof point: AI-assisted development cut the estimated effort on an internal search build from 80 hours to 10. This is an estimate, not yet measured.
- Engineering standards already in place for containerized hosting, release and code quality.
- Direct experience taking an AI capability through the AI Council approval path.

## Keep in mind

- Sean has asked for AI benefits to be measured (rework, defects, cycle time), not described. Build measurement into each selected product from the start.
- Mike is the conduit, not the decision forum. Hold the gate and the funding model as positions to test and listen for his reaction; do not commit to them in the meeting.
- If the answer to question 2 is a large number, those are unowned applications on production data. Route them through the same gate; do not offer to absorb them.

## Outcomes wanted

- Agreement on how ideas move from Mike to us.
- Two or three selection criteria we all accept, and Mike's reaction to funding as the filter.
- A first look at candidate ideas, or a date when we will get one.
- Mike's read on the vibe coder's role and the Launch Studio name.
- Agreement on whether to take a joint view to Sean the week of October 19, after he returns from PTO.
