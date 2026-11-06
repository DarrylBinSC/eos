# CDA Requirements Session Plan

Darryl Benson and Ron Snyder, 2026-11-02. Working document: CDA Requirements Spec v0.1 (Word copy sent with this plan).

::: {custom-style="Bottom Line"}
**Bottom line:** leave the hour with Ron's corrections on the spec, a reuse call on every P0 row, and a first sizing of Phase 1, so v0.2 can go to David Blondel for the roadmap reconciliation this week.
:::

## Purpose

Convert Darryl's architecture and intended functionality into requirements Ron can size and challenge. Darryl owns what the service must do and what the customer buys. Ron owns what the platform can do today, what is extension and what is net-new, and the effort. Nozomi is new to both; the spec keeps every Nozomi item as an assumption so neither of us has to defend it today.

## Before the session

Ron, 20 minutes: read sections 1 to 4 of the spec (status, problem, roles, goals and non-goals) and skim the requirement tables. Mark any row where the reuse status is wrong. Do not try to size yet.

Darryl: bring answers to Questions for Darryl 1 to 3 (firmware execution in Phase 1 or not, SNMP monitoring-only boundary, ship without Guardian or not). Ron cannot size around open ones.

## Agenda, 60 minutes

| Time | Block | What we do | Spec section |
|--|------------|--------------------------|----|
| 0 to 5 | Frame | Darryl states the three capability goals in one minute each: Nozomi analysis component with no point integration yet, auto-onboarding from Guardian data, and the rule set for executing the service. Confirm the non-goals hold. | 4 |
| 5 to 15 | Reuse pass | Walk the capability areas in order. For each, Ron calls the reuse status: existing, extension, net-new. Correct rows, do not debate wording. Flag anything he thinks is missing. | 5 |
| 15 to 35 | Sizing questions | Work Questions for Ron 1 to 3 and 11 to 13 in that order: discovery and SNMP, write actions, multi-tenancy, the Nozomi component storage pattern, programmatic onboarding and tagging, rule-set packaging. Capture Ron's answer and his confidence in it. | 10 |
| 35 to 45 | Open since July | Questions 6 and 7: Docker packaging and Arcbeam readiness, node fleet management by RMM. These have had no recorded answer since the July architecture work. | 10 |
| 45 to 55 | Phase 1 shape | Ron gives a rough sizing of Phase 1 in team-weeks against the 2027 roadmap he and David are reconciling, with the two or three rows that drive most of it. Darryl decides what moves to Phase 2 if the number does not fit. | 7, Q15 |
| 55 to 60 | Close | Agree the Nozomi questions Ron wants answered first (register N-1 to N-11) and who asks Nozomi. Confirm what each of us does before v0.2. | 6 |

## Ground rules

- A row Ron cannot place today is marked "Ron to confirm" with a date, not argued.
- Nozomi rows stay assumptions. We record what we need to learn, not what we think Guardian does.
- Scope additions go to the parking list at the end of the session and are not sized today.
- Customer names stay out of the spec; the pilot account is named only in Darryl's notes.

## Outputs

1. Spec v0.1 marked up by Ron: reuse status corrected on every P0 row, missing rows added, rows he disputes flagged.
2. Answers to the twelve sizing questions, each tagged known, estimated or unknown.
3. A first Phase 1 sizing in team-weeks with the three largest drivers named.
4. The Nozomi question list Ron needs answered before he can firm the sizing, for the BIR due Friday.
5. A parking list of ideas raised but not in scope.

## After the session

Darryl: fold Ron's markup into v0.2 the same day, resolve his own three open questions, and send v0.2 to David Blondel for the roadmap reconciliation. Lift the Nozomi register into the BIR.

Ron: confirm any "Ron to confirm" rows by the date agreed, and name who on his team takes Nozomi training first.

Next touchpoint: a 30-minute review of v0.2 with Ron and David once the roadmap reconciliation absorbs the Phase 1 sizing.
