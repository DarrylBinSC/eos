# Pulse Design Package, 2026-10-16

Rebuilt 2026-10-16 after three fixes to the Pulse data: K005 (a Dell knowledge risk) now counts against Dell and in the Delivery track and agenda; a register item counts against one account only, and linked items count once; each forum shows whether evidence arrived in the window. Dell reads 43/100 (was 36). C57 (Dell server pricing for the FRB Cash Services project) is attributed to Federal Reserve, which stays at 75/100. Screenshots and data are from the rebuilt snapshot.

This package is for Claude Design (claude.ai), a separate product from the operating-system session. Claude Design produces the mockups and change list; implementation happens back in the operating-system session.

For a design review of the Pulse page in Claude Design.

1. Read `Design_Brief.md` (10 minutes). It is the source of truth for purpose, rules, constraints and what to send back.
2. Open `pulse_prototype.html` in a browser. It is the production page with an embedded data snapshot; nothing is saved.
3. In Claude Design, attach the prototype, the brief and the `screenshots` folder, and paste `Claude_Design_Prompt.md`.
4. Bring the change list back to Claude in the operating-system session to implement in `Tools/eos_server.py`.

**Data sensitivity.** The prototype and `pulse_sample_data.json` contain real customer names (Dell, Ford, Federal Reserve and others), employee names, and internal delivery issues as of 2026-10-16. Share accordingly. An anonymized version can be produced on request.
