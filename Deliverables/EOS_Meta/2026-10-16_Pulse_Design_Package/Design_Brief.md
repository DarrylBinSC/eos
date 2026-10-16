# Pulse: Design Brief

Snapshot: 2026-10-16. Owner: Darryl Benson (Senior Director, CSS Platforms digital products). Built and maintained with Claude.

## 1. What the Pulse is

The Pulse is one tab in Darryl's personal operating system (a small web app on his Mac, opened from his laptop, iPad or iPhone on the home network). It answers one question: **what are my teams carrying right now, and does any of it need me?**

Darryl leads product, development and delivery teams for four products (entroCIM, WAM, Ascent/Navigator, Connected Device Assurance). His teams run their own governance: a project process for customer deployments, two-week sprints for development. He does not track their issues. He needs to keep his finger on the pulse of the organization, see where things are going wrong early, and lean in for detail when he chooses.

Claude reads meeting transcripts and email evidence every morning and fills the Pulse. Darryl reads it, escalates the few things that need him, and uses it to run two weekly governance meetings: one with his delivery leads (Chad Steger, Syed Zaidi) and one with his development leads (Ron Snyder, David Blondel).

**What Darryl said about it (2026-10-16):** "It is one of the best features we have built into the EOS because it synthesizes and contextualizes information, making it even more usable and actionable." The first version was nearly shipped as a markdown file in a folder; his verdict was that it "would never have worked" because it would not have been seen. **Visibility is the product.** Anything the design does to make the important things visible faster is the point of this review.

## 2. Who uses it, where, how often

| Moment | Device | What he needs in seconds |
|---|---|---|
| Morning glance, between meetings | iPhone, laptop | Did anything change? Does anything need my call? How is Dell? |
| Weekly governance meeting with a team | Laptop, often screen-shared | The agenda for that team: stuck items, decisions, new, quiet, knowledge risks |
| Leaning in on an account or a person | Laptop, iPad | Everything about Dell, or everything Scott Dunn is carrying, in one place |
| Acting | Any | Escalate an item to his own Watch list, or leave it with the team; add a note |

He is an experienced executive, technical, and short on time. He reads density well but has little patience for hunting, unlabeled numbers, or anything that looks like generic dashboard decoration.

## 3. Information architecture (current order, top to bottom)

1. **Header strip, on every tab:** register caps, **Dell health score** (largest customer, pinned), **Pulse calls** (count of items needing his decision).
2. **Intro line:** the rolling 14-day window and what the Pulse is.
3. **Account health tiles:** one per account with a signal (7 today). Score out of 100, band label, what drives the score, 7-day change once history exists. Accounts with no signal are listed in one line beneath.
4. **Needs your call:** items that met an escalation test, each with Escalate and Leave with team.
5. **Your weekly governance:** two track cards (Delivery, Development) with counts and a "Weekly governance agenda" button.
6. **Sort bar + Live issues:** issues from team-governed forums, sorted by attention (live, stuck, severity, recency).
7. **Knowledge concentration:** single points of failure (one person holds knowledge a customer or release depends on), grouped by backup coverage.
8. **Team-governed forums:** cards for forums with issues; the rest in one line.
9. **People carrying the most:** owns, involved, delegated, sole-holder counts per person.

**Forum evidence.** Each forum carries the date of the newest evidence package that covered it (`last_evidence`). A forum with no evidence in the window is shown separately from one that sent evidence and raised nothing, and each track card says how many of its forums sent no evidence. Today that is 2 of 3 delivery forums and 8 of 10 development forums, so most of the page's silence means "not heard from", not "all clear".

**Filtering:** tapping an account tile, a person, a track or a forum filters the page. When filtered by an account or a person, their Pulse issues come straight after the tiles, followed by "On your registers" (the register items behind the numbers). A chip at the top shows the filter and a Clear button.

**Item detail:** a right-hand drawer (full screen on phone) with status, escalation buttons, a note box, a dated history timeline, and editable details.

**Governance agenda:** a drawer with a ready-to-copy agenda for one forum or one track.

## 4. Objects, states and rules

**Pulse issue (P###).** Raised in a team-governed forum. Fields that matter to the display: title, account, forum, severity (High, Medium, Low), customer-visible, owner, people named, first seen, last seen, times raised, next action, escalation state.

| State | Rule | Display today |
|---|---|---|
| Live | Raised in the last 14 days | Normal row |
| Quiet | Not raised for 14+ days; not confirmed resolved | Dimmed, behind "Include quiet and resolved" |
| Resolved | Darryl or evidence says so | Struck through, behind the same toggle |
| Stuck | Still being raised 10+ business days after first raised | Amber "Stuck" badge |
| Needs your call | Met a test: asked, crossed a boundary, stuck, no owner | Blue "Needs your call"; listed in Needs your call |
| Escalated | Darryl escalated it; a Watch item was created | Blue "Escalated · W###" |
| Left with team | Darryl decided it is theirs | Drops out of Needs your call |

**Knowledge entry (K###).** One person and one knowledge area. Fields: area, holder, backup, coverage (no backup, backup unknown, partly covered, covered), exposure (customer, release, migration, support), mitigation, absence date, track. Live for 45 days after the last evidence. Needs a call when no backup is confirmed and a customer or release depends on it, or when an absence or departure is near or past with handover unconfirmed.

**Account health score.** 0 to 100. Starts at 100 and subtracts: live High customer-visible issue 8, High internal 6, Medium 3, Low 1, stuck 4 extra, quiet 1, open call 3, open item about the account on Darryl's own registers 5. Bands: 80+ Healthy (green), 60 to 79 Strained (amber), below 60 At risk (red). A knowledge entry with an account counts as an open call against it. Each register item counts against one account only: its `account` field if set, otherwise the single account its title names. An item that names two accounts is not scored and is listed under the tiles ("Not scored because it names more than one account") until its account is set. Items linked to each other count once. It is an operational-friction index from evidence, not customer sentiment. **Lesson already learned:** Darryl first read bare scores as issue counts; it is now shown as "36/100 · health score." Keep scores unmistakable.

**People.** Owns (owner of a live Pulse issue), Involved (named in the evidence with a statement, commitment or role, not owner; attendance never counts), Delegated (open register items they own), Sole (knowledge areas they hold with no confirmed backup).

## 5. Constraints the design must respect

- **One self-contained HTML file** served by a small Python standard-library server. Vanilla JavaScript and CSS, no frameworks, no build step, no CDN, no web fonts, no external images. System font stack. Inline SVG is fine.
- **Light and dark** via CSS custom properties (tokens in the `:root` blocks of the prototype). Every new color needs both modes.
- **Phone first-class:** iPhone Safari at 390px wide. Touch targets 44px. No horizontal page scroll.
- **"No evidence received" must look different from "nothing raised."** A forum, track or account that sent no evidence in the window is unknown, not calm. Show it as its own state, with its own word and treatment, everywhere a count of zero could appear (track cards, forum cards, agendas, account tiles). A zero from a forum that was heard from and a zero from a forum that was not must never look the same.
- **Color is never the only signal.** Every band, badge and state carries a word.
- **Content is generated.** Titles can be long (100+ characters), names vary, counts range from 0 to 120. Empty states matter.
- **Same visual language as the rest of the app** (Triage, Mine, Watch and other register tabs share the header, rows, drawer and buttons). A change to shared components affects every tab.
- **No new back end** is assumed. If a design needs a new field or computed value, say so; it can usually be added.

## 6. What could be better (Claude's observations, for the designer to test, not instructions)

1. **Above-the-fold priority.** On a laptop the tiles take two rows and push "Needs your call" down. On a phone, "Needs your call" is several screens down. The single most important thing on the page may not be first.
2. **Tile repetition.** Every tile says "Trend starts once a week of history exists." The driver line ("4 High customer-visible · 2 Medium · 1 stuck...") is informative but hard to scan.
3. **Score legibility at a glance.** Seven tiles, each a number and a band. Would a compact ranked strip, a bar, or a sparkline (once history exists) read faster?
4. **Track cards vs forum cards.** Two card groups with similar counts. Do both earn their space, or should forums nest under tracks?
5. **Length.** The page is long; People has 73 entries (top 15 shown). Is there a better summary-then-drill pattern?
6. **Knowledge concentration vs People "Sole" column.** Same signal shown twice. Is one view enough?
7. **Filter discoverability.** Tiles, people rows, track and forum cards are all filters, but nothing says so until you tap. The chip appears only at the top.
8. **Drawer density.** The issue drawer is good for detail; is there a lighter preview for quick reading on phone?
9. **Governance agenda as a meeting surface.** It is used screen-shared in team meetings. Could it be a presentable view rather than a drawer of text?
10. **Change since last visit.** Nothing shows what is new since Darryl last looked. "New this week" exists per forum, but not per visit.
11. **Silence vs no evidence (a requirement; see section 5).** Ten of thirteen forums sent no evidence in the window. The page now says so in a line of text, but a quiet forum and an unheard forum still look much alike at a glance, and the Development track card (1 live, 0 stuck, 8 of 10 forums unheard) reads as calm. Propose how "no evidence received" is shown as a distinct state.
12. **What a tile score is made of.** A score blends two things: what the teams are raising (Pulse issues) and items on Darryl's own registers about that account. For five of seven accounts today the registers are most or all of the deduction (Federal Reserve: 0 Pulse issues, 25 points from five register items). Whether to keep one blended number is Darryl's call, but the design should let him see the two parts separately at a glance.

## 7. What to keep

- Score shown as "/100" with a band word.
- Owner visible on every issue row ("Owner: …" or "No owner named").
- One-tap Escalate and Leave with team, in the list and in the drawer.
- The stated sort order on every list.
- Filtering by account or person leading straight to their items, including the register items behind the numbers.
- Plain language. No marketing tone, no decorative charts.

## 8. What to send back

So the changes can be implemented directly in the existing file:

1. **Annotated mockups** of the Pulse at desktop (1400px) and phone (390px), light and dark.
2. **A change list**, one row per change: component, what changes, why (which problem in section 6 or a new one), priority (now, next, later), and whether it touches shared components used by other tabs.
3. **Any new data a design needs** (already available: `last_evidence` and `evidence_in_window` per forum, `no_evidence` per track, `unattributed` register items, and `counted`/`same_as` on each register item behind a tile) (a field, a count, a history series), named plainly.
4. **Copy changes** as exact wording.

## 9. Files in this package

- `pulse_prototype.html`: the live page, production code, with a snapshot of real data embedded. Open it in any browser; everything is clickable. Notes, status changes and escalations work during the visit and are not saved.
- `screenshots/`: desktop light and dark, phone, issue drawer, knowledge drawer, governance agenda, filtered by account, filtered by a person with no Pulse issues.
- `pulse_sample_data.json`: the same snapshot as structured data (items, computed summary, user guide).
- `Claude_Design_Prompt.md`: a ready-to-paste opening prompt.
