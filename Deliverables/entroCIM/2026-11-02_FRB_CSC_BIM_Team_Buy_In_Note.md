# FRB CSC BIM Team Buy-In Note

Audience: Darryl's leads (Ron, David, Chad, Syed). Purpose: buy-in on scope, capability, timing and project implications before the bid response is finalized. Supersedes the longer bid-group note of the same date for this audience.

---

Team, FRB has clarified the BIM ask on the Cash Services Center, and I want you behind the answer before it goes to Turner this week.

**What they want.** The platform holds the building's BIM data, and eventually 3D graphics, for asset management. Not BAS visualization. They know we cannot do it today; they want a price and a roadmap. Nate believes we are the frontrunner.

**What we would build.** Two roadmap stages, both outside base entroCIM:
- A BIM data repository: a snapshot of the IFC and COBie handover data, linked to our equip records by the FRBNY Asset ID, with version tracking and API read access. IFC metadata only; no geometry.
- 3D viewing in our UI: an embedded, self-hosted IFC viewer that renders the stored model and syncs selection with entroCIM by Asset ID. We host a viewer; we do not write a 3D engine.

**What we would not do.** Author, coordinate or maintain models. Read native Revit. Become the system of record for the model (Kahua) or the asset register (TRIRIGA). Absorb model changes automatically. The platform's truth stays the installed, connected, commissioned device; the handover data is context, and where the two disagree the field wins and we report the difference.

**Timing.** Handover data does not exist until Q1 2029 (Substantial Completion 2/28/29). The repository is due before Smart Building start-up in December 2028, 3D before commissioning in February 2029. Both fit the 2028 roadmap with a year of margin. Detailed scope and acceptance are agreed in the submittal window, December to March.

**Commercially.** FRB pays a development charge per stage, licenses the capability as an advanced feature, and pays for loading their data at each release. We retain the IP and sell it to other customers.

**What I need from you this week.**
- Ron: a rough effort and timing estimate for both stages on the basis above, and whether the COBie-to-Haystack mapping is feasible.
- Chad: whether the delivery team can produce a COBie workbook for our furnished equipment at Turner's data drops, and the deployment model for model data at FRB.
- David: where this sits in the entroCIM roadmap and price list.
- All: anything in the draft response you would not sign up to. Better now than in 2028.

Draft response is in the FRB folder. Thirty minutes tomorrow if a call is faster.
