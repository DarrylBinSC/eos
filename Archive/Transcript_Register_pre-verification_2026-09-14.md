# Transcript Register

> **Purpose: make Copilot's access claims falsifiable.** Created 2026-09-14 after two weekly runs on the same day disagreed about which transcripts existed and which could be retrieved (`10_Pilot_Feedback_Log.md`, 2026-09-14). Copilot's statements about its own access have now been wrong in both directions: it reported two fully retrievable transcripts as truncated, and reported a non-existent transcript as truncated and then quoted from it.
>
> This register records ground truth **that Darryl verifies in Teams**, not what Copilot reports. Once the "Teams state" column is filled in, every Copilot access claim becomes checkable in seconds:
>
> - A Coverage Gap on a forum this register says is transcribed is a **failed run**. Re-run it.
> - A Coverage Gap on a forum this register says is not transcribed is a **misfiling**. It belongs in "Not transcribed at source," which is an operating signal, not a retrieval problem.
> - A quote attributed to a forum this register says is not transcribed is a **manufactured source**. Reject the row.
>
> **How to fill it in.** Open each recurring series in Teams or the calendar, check whether transcription is enabled at the series level, and record ON or OFF with the date checked. Series-level, not occurrence-level, unless the forum is marked "varies" below. Review monthly, and after any forum changes owner or cadence.
>
> **Evidence column values.** `Copilot evidence to date` is what the packages have shown, with dates. It is a starting hypothesis for the verification, never a substitute for it.

## How to read the evidence column

| Value | Meaning |
|---|---|
| **Transcript retrieved** | A package retrieved the transcript to its stated total. Transcription was on for that occurrence. |
| **Not transcribed** | A package reported `isMeetingTranscribed:false`. No transcript existed for that occurrence. |
| **Varies by occurrence** | Both of the above have been observed for the same series. Fix at the series level. |
| **Truncated, continuation failed** | Transcript exists; retrieval did not complete. A retrieval problem, not a transcription problem. |
| **No evidence** | The forum has not appeared in any package with a transcript status. |

## Core product, delivery, and governance

| Forum | Cadence | Owner | Who can switch it on | Copilot evidence to date | Teams state (verify) | Verified on | Priority |
|---|---|---|---|---|---|---|---|
| WAM Product Leadership Sync | Weekly | David Blondel | David Blondel | Not transcribed (08-25 diagnostic). Transcription ON imposed 2026-09-01 under the agenda standard; no occurrence evidenced since | | | **Confirm the 09-01 change took effect** |
| ADM connect with Natalie | Weekly | Akansh Gangil | Akansh Gangil | No evidence | | | High — where WAM data-foundation defects surface |
| WAM Product discussion | Weekly | Akansh Gangil | Akansh Gangil | No evidence | | | Medium |
| WAM Data Challenges (Problem Definition) | Weekly | **Darryl Benson** | **Darryl** | Recording artifact only, 0 usable transcript lines (09-14 re-run, `Hold - Problem Definition & Brainstorming`) | | | **High — Darryl-owned, and the 09-14 package lost material WAM discussion here** |
| DDP Entrance Call | Weekly (Mon) | Anna Baker | Anna Baker | Transcript exists; truncated, continuation failed (08-25, 0-435 of 574) | | | Low — mostly out of scope |
| WAM Product Backlog Refinement | Bi-weekly | Sakshi Mathur | Sakshi Mathur | Transcript retrieved 0-699 of 699 (09-14 re-run) | | | Confirmed working |
| WAM India Dev Team weekly | Weekly | TBC | TBC | No evidence | | | Medium |
| WAM Sprint Review | Bi-weekly | Sakshi Mathur | Sakshi Mathur | No evidence | | | Low |
| Daily Stand Up (entroCIM) | Daily | Ron Snyder | Ron Snyder | Transcript retrieved 0-355 of 355 (09-14 re-run) | | | Confirmed working |
| 2026 Deployment — Daily Scrum | Daily | Chad Steger | Chad Steger | **Varies by occurrence.** Retrieved 0-286 of 286 (09-14 re-run); not transcribed 09-08, 09-09 (re-run) and 09-09, 09-10 (run 1) | | | **High — fix at series level; the inconsistency is itself the defect** |
| entroCIM Backlog Deep Dive | Bi-weekly | David Blondel | David Blondel | Transcript retrieved 0-815 of 815 (09-14 re-run). Run 1 wrongly reported this one as truncated | | | Confirmed working |
| entroCIM Leadership Collaboration | Weekly | Ron Snyder | Ron Snyder | Not transcribed (08-25 diagnostic). Transcription ON imposed 2026-09-01 under the agenda standard; only a channel message evidenced since | | | **Confirm the 09-01 change took effect** |
| Quest Migration Weekly Check-In | Weekly | Chad Steger | Chad Steger | Not transcribed (08-25 diagnostic; 09-14 run 1; 09-14 re-run, 09-08). Consistently off across three weeks | | | **High — one request to Chad; migration governance is running blind** |
| Showcase recurring | Bi-weekly | David Blondel | David Blondel | No evidence | | | Low |
| Deployment Team Knowledge Share | Periodic | TBC | TBC | No evidence | | | Low |
| DCOE & entroCIM Weekly | Weekly | Balachandar Murali | Balachandar Murali | No evidence | | | Low |
| CSS Platforms All Hands | Periodic | Leadership | Darryl / leadership | No evidence. Decision-rich forum | | | **High — decision-rich and unevidenced** |
| Digital Products Portfolio Review | Periodic | Sean McCloskey / Chris Gazdic | Meeting owner | No evidence | | | Medium |
| Dell Service Management Process | TBC | Syed Jamshed Zaidi / Chad Steger | Meeting owner | No evidence | | | Medium — customer-facing |
| Dell Program Delivery Alignment | New | TBC | Meeting owner | No evidence | | | Medium — customer-facing |
| Wesco Asset Manager Backlog Deep Dive | Bi-weekly | TBC | Meeting owner | No evidence | | | Medium |
| EntroCIM Project Closeout Process Review | Unconfirmed | TBC | Meeting owner | No evidence | | | Low |

## 1:1 and leadership alignment

| Forum | Cadence | Owner | Who can switch it on | Copilot evidence to date | Teams state (verify) | Verified on | Priority |
|---|---|---|---|---|---|---|---|
| Darryl / Nate Weekly 1:1 | Weekly | Nathan Kehr | Nathan Kehr | No evidence | | | Medium |
| Darryl – Ron 1:1 | Weekly | **Darryl** | **Darryl** | Not transcribed, 09-08 (09-14 re-run) | | | **High — Darryl-owned, one setting** |
| Darryl – Chad 1:1 | Weekly | **Darryl** | **Darryl** | No evidence | | | **High — Darryl-owned** |
| Weekly Sync (Amy Aguirre) | Weekly | **Darryl** | **Darryl** | Transcript retrieved 0-308 of 308 (09-14 re-run). Run 1 wrongly reported this one as truncated | | | Confirmed working |
| Digital Products / Agile Staff Meeting | Weekly | Chris Gazdic | Chris Gazdic | Transcript retrieved 0-497 of 497 (09-14 re-run) | | | Confirmed working |
| Product Team – Platform Team connect | Weekly | Keyur Patel | Keyur Patel | No evidence | | | Low |

## Commercial, finance, customer, external

| Forum | Cadence | Owner | Who can switch it on | Copilot evidence to date | Teams state (verify) | Verified on | Priority |
|---|---|---|---|---|---|---|---|
| entroCIM Sales Ops/Finance Sync | Twice-monthly | Tom Boss | Tom Boss | No evidence | | | Medium |
| WAM / External BIR: 2517699 Actuals | Monthly | John Erickson | John Erickson | No evidence | | | Medium |
| Wesco / SkyFoundry | Monthly | **Darryl** | **Darryl** | Not transcribed, 09-09 (09-14 re-run). Run 1 reported it as a truncated transcript and quoted two action items from it; no transcript exists | | | **Highest — Darryl-owned, and this is the forum where a fabricated quote originated** |
| BAE/Wesco Weekly | Weekly | Kevin Cochran | Kevin Cochran | No evidence | | | Medium — external customer |
| Smart Buildings Issues Log Catch-Up | Bi-weekly | Raj Ramroop | Raj Ramroop | No evidence | | | Low |

## Ad hoc and customer meetings seen in evidence

Not recurring forums, so not series-configurable, but recorded because they carried material content.

| Meeting | Date seen | Copilot evidence | Note |
|---|---|---|---|
| FRBNY CSC: Smart Building Descope | 2026-09-08 | Not transcribed | The FRB thread is carried in the accepted 09-14 package from run 1 only. With no transcript, recovery depends entirely on email and chat |
| PASS-06 Server Migration Cutover | 2026-08 | Not transcribed (08-25 diagnostic) | Darryl's own organisation |
| Differentiation exercise | 2026-08 | Truncated, 0-583 of 952, continuation failed | Transcript exists |
| Claude Code Model Upgrades - VAS, Assortment, QPM | 2026-09 | Out of scope | Optional-attendee forum |

## Action queue from this register

Ordered by leverage, not by effort.

1. **`Wesco / SkyFoundry`** — Darryl owns it, transcription is off, and it is the forum that produced a fabricated quote in run 1. Switch on.
2. **`Darryl – Ron 1:1`** and **`Darryl – Chad 1:1`** — Darryl owns both. Switch on.
3. **`WAM Data Challenges`** — Darryl owns it, it is his only weekly forum with no decision output to date, and the 09-14 package lost its content to a recording-only artifact. Switch on. This is also the strongest candidate for the agenda standard per `07_Operating_Cadence.md`.
4. **`Quest Migration Weekly Check-In`** and **`2026 Deployment — Daily Scrum`** — both Chad Steger's, one conversation. The Daily Scrum needs a series-level fix, not an occurrence-level one.
5. **Confirm the 2026-09-01 change took effect** on `WAM Product Leadership Sync` and `entroCIM Leadership Collaboration`. The agenda standard specified transcription on and recording off; no transcript from either has appeared in a package since.
6. **`CSS Platforms All Hands`** — decision-rich, no transcript evidence in any package. Worth asking whoever chairs it.

Items 1 to 3 are entirely within Darryl's control and cover four forums.
