# Session Handoff: Operational Pulse build, 2026-10-16

Written at the end of the 2026-10-16 session for the next Claude session (or another LLM). Read this file, then `CLAUDE.md`, before doing anything else. Darryl is the decision-maker; this file records where the work stands, not new decisions.

## 1. Paste this to open the new session

> Read `Reference/Session_Handoffs/2026-10-16_Pulse_Build_Handoff.md`, then `CLAUDE.md` (especially "Operational Pulse", "Pulse layout" and "Designing and Building With Darryl"). Confirm the current state in two or three sentences, verify the server and Tools files as section 6 describes, then wait for my direction. Pulse Phase 1 and Phase 2 are live and I approved Phase 1. Open item: which accounts have an open project.

## 2. What happened on 2026-10-16

1. **Daily brief** ran (`Briefings/2026-10-16_Daily.md`, with an afternoon update; evidence in `Evidence/M365_Evidence_Daily_2026-10-16.md`).
2. **Lane model decided and built.** Issues from team-governed forums (Daily Scrum, Daily Stand Up and the other governed forums) no longer go on Darryl's registers. They live in the **Operational Pulse** (`Registers/pulse/P###.md`) and reach his registers only by escalation. Six deployment-level Watch items were retired to the Pulse. Full rules: `CLAUDE.md`, "Operational Pulse (lane model)".
3. **Pulse web view built** in the eosServer (`Tools/eos_server.py`, logic in `Tools/eos_pulse.py`): account health (score out of 100), needs-your-call, live issues, governance tracks, knowledge concentration (`K###`), people.
4. **Working rules 1 to 5 agreed and filed** in `CLAUDE.md`, "Designing and Building With Darryl": surface before store; show, don't describe; check proposals against past failures; state build cost honestly; ask only what is Darryl's to decide. These came from Darryl's correction that an earlier markdown-file recommendation "would never have worked."
5. **Claude Design package** produced; Darryl brought back `Pulse_Redesign_Handoff_2026-10-16.zip` (change list C1 to C21).
6. **Redesign Phase 1 (C1 to C13, C8a) built and approved by Darryl.** Today row (calls with reasons, pinned account with split bar, Evidence "heard from n of 13"), account table with Pin, governance tracks with heard counts and not-heard states, phone order.
7. **Redesign Phase 2 (C14 to C19) built and deployed** at 4:27 PM. Issue rows with New, "Stuck · raised since" and state-aware actions; sticky filter chip; phone preview sheet; full-window governance meeting view (Copy as text, Present full screen); People top 8 with grouped columns, Sole removed; Knowledge badges and quiet footer. **Darryl has not yet reviewed Phase 2.**

## 3. Current state (verify; do not assume)

| Item | State at handoff |
|---|---|
| `Tools/eos_server.py` | Phase 2 version, md5 `455fa356430fe3d60e84c16543e072e2` |
| `Tools/eos_pulse.py` | Phase 1 version (unchanged in Phase 2), md5 `1235c76e9aa15ae8f5616fbf41fed817` |
| Server | Running on Darryl's Mac; auto-restarted on the Phase 2 deploy (commit "code change: restart server with updated Tools/", 16:27) |
| Rollback copies | `Archive/2026-10-16_pre_pulse/`, `Archive/2026-10-16_pre_pulse_redesign/` (pre-Phase 1), `Archive/2026-10-16_pre_pulse_phase2/` (Phase 1 server) |
| Pulse items | P001 to P011, K001 to K005. P006 escalated to W009. P001, P004, K005 left with the team. K002, K003 resolved. No open calls at handoff |
| Pinned account | Dell (setting `pinned: true` in `Registers/pulse/_accounts.json`); Dell 46/100, at risk (teams 44 points, registers 10) |
| Evidence | Heard from 3 of 13 forums (2 raised, 1 nothing raised, 10 not heard); from `last_evidence` in `Registers/pulse/_forums.json` |
| Docs | `CLAUDE.md` ("Pulse layout" paragraph covers Phases 1 and 2, change-history rows added); `Reference/Registers_App_User_Guide.md` (Pulse layout and Phase 2 sections) |

## 4. Open items

**Decision required from Darryl (rule 5: his to decide).**
1. **Which accounts have an open project?** Sets `open_project: true/false` per account in `_accounts.json`. Until set, the account table's Teams column reads "Project status not set." Do not infer it.

**Waiting on Darryl.**
2. **Phase 2 review.** Ask what to change after he has used it on the laptop and the phone. Suggested checks: tap an issue on the phone and use Add a note; open Delivery's agenda and use Present full screen.

**Not to build unless Darryl asks.**
3. C20 (since your last visit) and C21 (trend; needs two or more weeks of `_health.json` history).

**Standing.**
4. Calibrate account-health weights with Darryl in the first weekly. Falsification test: if Dell health has not informed a conversation or decision within three weekly cycles, recalibrate or cut it.
5. At every brief, set `last_evidence` in `_forums.json` for each forum the evidence package covered, whether or not it raised anything. Without it, silence reads as "not heard" (by design) and the Evidence card goes stale.

## 5. Deviations from the Claude Design handoff (already reported to Darryl)

- Meeting view adds a "Still open" section only when a track has live issues older than a week that are neither stuck nor calls (the handoff listed five sections; dropping them would hide live work).
- People table dropped the Forums column, matching the mockup; a name's forums show on hover.
- Account Teams cell shows "Project status not set" pending item 1 above.

## 6. How to work in this folder (gotchas learned this session)

- **Edit on the device.** Use the device shell (`device_bash`) for files in the connected folder. Build and test larger code changes in a cloud copy, then commit back with the device file's current `mtimeMs` as the guard.
- **Staged file names are cached.** Committing a staged file whose path was used earlier in the session wrote the *old* content once. Give every staged output a unique name (for example `eos_server_phase3.py`) and verify the md5 on the device after every commit.
- **Never run git write commands from the device shell.** The server commits its own changes; git log, diff and show are fine.
- **Server restarts itself** when files in `Tools/` change and compile. Confirm with a "code change: restart server" commit in git log. If none appears, the server is probably not running; tell Darryl to relaunch `Tools/eos-server.command`.
- **Test before deploy.** Run a copy with `EOS_ROOT=<copy> EOS_PORT=8799 EOS_BIND=127.0.0.1 python3 Tools/eos_server.py` and check desktop (1400px), tablet (1050px) and phone (390px), light and dark, with Playwright: no horizontal scroll, no console errors, phone targets 44px or more.
- **Registers are generated views** (03, 04, 05, 11). Never edit them by hand; edit `Registers/<kind>/ID.md` or use the web app.
- **People on Pulse items** come from statements, commitments or stated roles in evidence, never meeting attendance alone.
- **Darryl's word outranks Copilot evidence.** Do not suggest the M365 connector (company policy). `08_Field_Notes.md` is retired.

## 7. Key code locations

- `Tools/eos_pulse.py`: `summary()` (health rows with `registers_points`, `teams_points`, `pinned`; forums with `ev_state`; tracks with `heard`, `total`, `not_heard`; candidates with `reason_line`; `evidence`), `set_pinned()`, `HEALTH_WEIGHTS`, `DEFAULT_PINNED = "Dell"`.
- `Tools/eos_server.py` (single-file UI in the raw string `HTML`): Pulse CSS under the `pv-` prefix (Phase 2 block marked "Pulse redesign Phase 2"); JS `pulseHtml`, `callsCard`, `pinnedCard`, `evidenceCard`, `accountsSec`, `govSec`, `prow`, `ibadges`, `iacts`, `openSheet`, `peopleHtml`, `knowHtml`, `krow`, `agendaModel`, `agendaMd`, `openAgenda`; route `POST /api/pulse/pin`.
- Design source: Darryl's zip `Pulse_Redesign_Handoff_2026-10-16.zip` (change list, design spec, mockups). It is not in the folder; ask Darryl for it if a change needs the spec.

## 8. Maintaining this file

This is a point-in-time handoff. When the next session closes or supersedes an item in section 4, update `CLAUDE.md` (the durable record) and write a new dated handoff rather than editing this one.
