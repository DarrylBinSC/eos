# EOS Server Architecture Review

2026-10-28. Darryl and Claude. Board: https://miro.com/app/board/uXjVEUKYO5E=/

## What runs

One Python process (`Tools/eos_server.py`, standard library plus openpyxl) on Darryl's Mac, port 8765, LAN, no login. Inline single-page UI and a JSON API. Four modules: `eos_registers` (parse, write, generate 03/04/05), `eos_pulse`, `eos_products`, `eos_review`. Markdown item files with front matter are the database; Pulse configuration is JSON; 03/04/05/11 are regenerated on change. A watcher thread polls every 5 seconds, commits outside edits, and restarts the server when `Tools/*.py` changes and compiles. Three writers touch the folder: the web app, Claude sessions through the device shell, and iCloud sync. Separate processes: the Pandoc watcher and the cloud end-of-day task (chat only, never writes).

## Decisions (Darryl)

| Item | Finding | Decision |
|---|---|---|
| Git had no remote | Audit trail existed only on the Mac, inside iCloud | Private GitHub backup, server pushes after every commit. Done 2026-10-28 |
| iCloud syncing `.git` | Collision risk; first hang recorded 2026-10-15 | History moved to `.git.nosync` inside the folder; EOS folder stays in iCloud for the other laptop. Done 2026-10-28 |
| Deploys gated on compile only | 185d Products bug compiled fine | Add a smoke test the watcher runs before restart. **Done 2026-10-29** (`Tools/eos_smoke.py`; proof commits `cb94930` fail, `473cd08` pass) |
| 2,100-line server with UI inlined | Slows changes, diffs unreadable | Split UI into a static file served by the same process. **Done 2026-10-29** (`Tools/ui/`, byte-exact split, `ui change:` commits without restart; proof `5499ead`) |
| No login on LAN | Single user at home | Keep as is |
| Markdown vs JSON for items | JSON gains strict structure, loses the readable narrative body that briefs depend on; config already JSON | Keep markdown with front matter. Add allowed values per field via the smoke test rather than change format |

Not changed, on purpose: file-per-item store, stdlib HTTP server, regenerate-on-change, LAN-only posture. The system's history says what worked was what sat closest to where Darryl looks; this architecture is the simplest thing that keeps it there.

## Smoke test, as agreed

A script that loads every item file, regenerates the views, builds the summary for each tab, and asserts invariants drawn from past failures (no negative product age, no live Pulse issue without a forum, every ID unique, allowed values per field, generated counts match the files). Runs in seconds on the real data. The watcher runs it before restarting; on failure the old code keeps running and the commit message says so. The morning brief step runs it once too, so a session edit that breaks a rule is caught before the brief is built. Each new bug becomes one more assertion.
