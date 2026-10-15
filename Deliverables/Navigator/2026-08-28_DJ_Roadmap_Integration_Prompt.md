# Prompt for Review: Integrating DJ's Roadmap into the Navigator / entroCIM Deck

**Status:** For Darryl's approval before execution. Written 2026-08-28 after reviewing
`Deliverables/Navigator/2026-09-DJ_Navigator_Platform_Current_State_MVP1_3_Year_Roadmap.pptx`
(DJ Vaughn, Navigator Platform executive review, September 2026, 12 slides).

**Decisions taken by Darryl, 2026-08-28. Items 1 and 4 to 6 were given after the first draft of this prompt and supersede what it originally said.**

1. **Use DJ's published dates throughout, so the two decks do not confuse anyone.** This reverses the earlier decision to keep the After June 2027 caption. Dates get updated over time as work progresses.
2. DJ's roadmap content is **integrated into the roadmap page**.
3. We adopt DJ's published wording: **Navigator Intelligence**, the live visibility and reporting layer.
4. **"St. Louis" comes out everywhere.** The site panel becomes a customer site rather than one named office, so the picture holds for any Ascent customer facility.
5. **WAM and CDA stay on the connection diagrams**, despite being absent from DJ's roadmap. Darryl's read: DJ is likely not thinking about them, which is a reason to show them, not to remove them.
6. **Once the entroCIM connection exists, the CDA connection is done.** CDA rides the same secure path. This is a value point, not just an architecture detail, and it belongs on the value page.
7. The frame A row reorder and arrow correction in section 2c is approved.

---

## 1. What DJ's deck contains

| Slides | Content |
|---|---|
| 1 to 2 | Title and section divider |
| 3 | Current state: Navigator Intelligence, Maximo Today, NavWork in Development |
| 4 | Managed Services Solution: operational execution, asset and commercial record, visibility and scale |
| 5 to 7 | NavWork MVP1: operating records, record experience, workflow and reporting, migration and deployment |
| 8 | Three-year roadmap executive view: Year 1 Q3 2027 to Q2 2028, Year 2 Q3 2028 to Q2 2029, Year 3 Q3 2029 to Q2 2030 |
| 9 to 12 | Twelve quarters of feature detail, Q3 2027 through Q2 2030 |

**No diagrams anywhere.** Twelve slides of three-column bullet lists. That is the single most useful fact about how the two decks relate: his is the inventory and the sequence, ours is the picture and the value. They are complementary, and neither replaces the other.

---

## 2. Findings that change our deck

### 2a. The two decks disagree on when entroCIM integration happens

Our deck, from DJ verbally on 08-27: in-depth entroCIM integration begins after June 2027.

DJ's published deck: **Q4 2027 "Integration support - EntroCIM"**, then **Q2 2028 "Begin facility connectivity: integration expansion, meters, CM points, MOP data point gathering."**

Those reconcile as a sequence rather than a contradiction: integration work can begin in Q4 2027, and the facility data actually flows in Q2 2028. What does not survive is any reading of frame C as a state that exists in July 2027.

**Darryl's decision, revised: adopt DJ's dates.** The deck now runs on one set of dates, his published ones, and the risk of the two decks contradicting each other in front of Dirk goes away. Frame captions become:

| Frame | Caption |
|---|---|
| A | Today |
| B | Now through 2027 |
| C | From Q4 2027 |

The milestone spine, all of it DJ's: MVP complete December 2026; UAT complete March 2027; Maximo replacement complete June 2027; Q3 2027 deploy and stabilize; Q4 2027 entroCIM integration support; Q2 2028 facility connectivity, meters and CM points.

**Consequence worth stating in the speaker notes:** the interim connection carries roughly eighteen months, not six. That makes the interim step considerably more valuable than the deck currently claims, and it makes the swivel-chair period long enough to be worth removing.

### 2b. Navigator Intelligence is a visibility layer, not the operations platform

DJ's slide 3, verbatim: "Navigator is the live visibility layer for managed services while Maximo remains the operational system being replaced." Navigator Intelligence carries live dashboards, operational reporting, customer and portfolio visibility, work, asset, vendor and invoice reporting, and user, role and site access controls.

Our frames currently label it "NavIntel, current operations platform." That is not what DJ's deck says, and his is published.

**Change:** label becomes **Navigator Intelligence**, described as the live visibility and reporting layer.

### 2c. The arrow direction in frame A is wrong

We currently draw Ascent Ops into NavIntel into Maximo, as though the front end were the way into the work system. If Navigator Intelligence is the visibility layer reading from Maximo, the real flow is the other way: Ops works in Maximo, Maximo feeds Navigator Intelligence, and Navigator Intelligence gives Ops visibility.

**Proposed change, needs Darryl's word.** Reorder the bottom row to **Ascent Ops, work system, Navigator Intelligence** and draw the loop correctly. Two benefits beyond accuracy: it puts the work system in the middle, which is exactly the semantic already established for frame C (NavWork as the single integration point), and it lets NavWork sit between entroCIM and Navigator Intelligence in the drawing, which is what "entroCIM reaches NavIntel through NavWork" actually means.

Cost: node positions move relative to the current deck. Positions stay constant across the three frames inside the new version, which is what the design principle requires.

### 2d. DJ's deck closes our thinnest gap

We have been carrying an author note saying the record holds no Navigator current-state detail and that nothing on the Ascent side should be drawn without DJ. His slides 3 to 7 now supply it. That note can be retired and the frame A speaker notes can carry real content.

### 2e. WAM and CDA appear nowhere in DJ's three-year roadmap, and they stay on the diagram anyway

Frame C shows five connections into NavWork. DJ's published roadmap through Q2 2030 covers exactly one of them, entroCIM. WAM and CDA are not line items in any quarter.

**Darryl's ruling: they stay on the diagram.** DJ is likely not thinking about them, and the diagram is where that becomes visible. Removing them would hide the gap rather than close it.

**And the gap is smaller than it looks, which is the point to make on the page.** Once the entroCIM connection exists, the CDA connection is done: CDA rides the same secure path into the site, so it needs no separate integration project. That turns CDA from an unscheduled dependency into a consequence of work already committed. Draw CDA's path as sharing the secure connection, say so in the speaker notes, and add it to the value page as an outcome.

WAM remains genuinely unscheduled. That one goes to the weekly call.

### 2f. Two possible scope overlaps, and the first one matters

**Q2 2028, under NavWork: "Meters, CM points, MOP data point gathering."** Meters and CM points are entroCIM's core competence and are precisely what the interim connection at St. Louis delivers. The question to put to DJ is whether that quarter is NavWork receiving facility data from entroCIM, or NavWork building its own facility data collection. If it is the second, the same capability is being built twice, and it should be settled long before Q2 2028.

**Q4 2028: "Heat map, scorecard, operational outlook."** Analytics adjacent to entroCIM's analytics. Lower stakes than the first, worth one question.

Neither goes on a slide. Both go to the weekly call.

---

## 3. Slide 7 rebuild: the roadmap page

Replace the blank five-lane grid entirely. DJ has published his answer, so the frame is obsolete.

**Form:** a milestone strip across the top, then four phase cards, using the card and banner vocabulary already in the deck.

**Milestone strip**, five markers on one horizontal axis running Q4 2026 to Q2 2030:

- Dec 2026, MVP complete, UAT begins
- Mar 2027, UAT complete, migration begins
- Jun 2027, Maximo replacement complete
- Q4 2027, entroCIM integration support begins
- Q2 2028, facility connectivity: meters and CM points

**Four cards.** The first is ours and covers what DJ's deck does not: everything before deployment. The other three are his Year 1, 2 and 3 in his own words.

| Card | Period | Content |
|---|---|---|
| Replace Maximo | Through June 2027 | MVP complete Dec 2026; UAT Dec 2026 to Mar 2027; integration and migration from Mar 2027; IBM renewal decision Mar or Apr 2027; replacement complete Jun 2027 |
| Year 1, Deploy and Connect | Q3 2027 to Q2 2028 | Deploy and stabilize NavWork; maintain Navigator Intelligence; establish tenant and client access; **begin entroCIM connectivity** |
| Year 2, Expand Operations | Q3 2028 to Q2 2029 | Vendor and customer capabilities; **facility data and field activity**; rounds, inspections and contracts; inventory and workforce functions |
| Year 3, Scale and Extend | Q3 2029 to Q2 2030 | Planning and administrative tools; automation and scorecards; safety, audit and failure analysis; additional support functions |

**Highlight the entroCIM items** in a distinct colour so the integration track reads off the page at a glance. That is the one thing DJ's deck does not show and ours can: where entroCIM sits across his three years.

**Banner:** roadmap content from DJ Vaughn's Navigator Platform executive review, September 2026. Attribution matters here; the page is his content in our visual language, and it should say so.

**Optional eighth page, Darryl's call.** A two-row quarter timeline carrying all twelve of DJ's quarter themes, Q3 2027 to Q2 2030, with the entroCIM quarters marked. It answers "when does anything happen" at a glance without reproducing forty-eight bullets. Recommend including it as a back page rather than in the main flow.

---

## 4. Full change list

| Page | Change |
|---|---|
| 1 Overview | No change beyond the Navigator Intelligence relabel if it appears |
| 2 Today | Panel becomes a customer site, no St. Louis. Relabel to Navigator Intelligence, live visibility and reporting layer. Reorder the bottom row and correct the arrow direction (2c, approved). Rewrite speaker notes using DJ's slide 3 content. Retire the author note about missing Navigator detail |
| 3 Now through 2027 | Recaptioned. No St. Louis. Speaker notes carry that the interim period runs to roughly Q2 2028, not June 2027, so the swivel-chair carries about eighteen months |
| 4 From Q4 2027 | Recaptioned to DJ's dates. CDA drawn as riding the same secure connection as entroCIM. Speaker notes carry the WAM gap and the Q2 2028 overlap question |
| 5 Value | NavIntel line becomes the live visibility and reporting layer. Add the CDA point: the entroCIM connection is the enabler, and CDA needs no separate integration once it exists |
| 6 Roadmap | Rebuilt per section 3 |
| 7 Optional | Twelve-quarter timeline as a back page |

---

## 5. What stays off the slides

Owners, dates for people, asks, and open items continue to be weekly-call material. Specifically kept off the page and carried in speaker notes or the register:

- WAM being absent from the three-year roadmap
- The Q2 2028 meters and CM points overlap question
- The Q4 2028 analytics overlap question
- MVP1 scope against the December 2026 date

---

## 6. Validation criteria

- Every roadmap item on page 6 traces to a specific slide in DJ's deck, in his words where practical.
- The entroCIM track is visually distinct across all three of his years.
- Page 4 and page 6 no longer imply different dates for the same event.
- Navigator Intelligence is described the same way on every page it appears.
- Frames A, B and C still share identical node positions after the row reorder.
- Attribution to DJ appears on the roadmap page.
- No em dashes, no owners or asks on slides, no reference to this system by name.
