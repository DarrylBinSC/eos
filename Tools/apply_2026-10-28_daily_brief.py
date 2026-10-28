import sys
sys.path.insert(0, 'Tools')
import eos_registers as R

TODAY = "2026-10-28"

def append_body(item_id, kind_dir, new_para, new_fields=None, bump_sightings=False, set_last_seen=None):
    path = R.REG_DIR / kind_dir / f"{item_id}.md"
    meta, body = R.read_item(path)
    body = body.rstrip() + "\n\n" + new_para.strip() + "\n"
    if bump_sightings:
        meta['sightings'] = int(meta.get('sightings', 1)) + 1
    if set_last_seen:
        meta['last_seen'] = set_last_seen
    meta['last_touched'] = TODAY
    if new_fields:
        meta.update(new_fields)
    R.write_item(meta, body)
    print(f"Updated {item_id}")

# 1. P015 - new 10-28 sighting (Modbus working)
append_body("P015", "pulse",
    '2026-10-28 (Daily Scrum, chat): Dunn, Scott: "Was still not able to get the BACnet equips to open for me but was able to get a working Modbus connector up and appears to be points reading so we can get them changed over to Modbus." Status better: Modbus now confirmed working as the path forward for Panama HVAC; BACnet still not functioning. Source: `Evidence/M365_Evidence_PulseP1_2026-10-28.md` (chat).',
    bump_sightings=True, set_last_seen="2026-10-28")

# 2. P073 - new 10-28 sighting (Robby contacted)
append_body("P073", "pulse",
    '2026-10-28 (Daily Scrum, chat): Dunn, Scott: "I also let Robby know last night we couldn\'t update the date column so will see if he has time to change that at all for us." Robby contacted; no commitment stated from him yet. Source: `Evidence/M365_Evidence_PulseP1_2026-10-28.md` (chat).',
    bump_sightings=True, set_last_seen="2026-10-28")

# 3. P018 - additive detail, same 10-21 sighting, no sightings increment
append_body("P018", "pulse",
    '2026-10-28 (Claude, daily brief): Additive detail, same 10-21 sighting (already counted): Singh, Narendra: "I think he is requested with the network team, so they have to enable that." Confirms the network-team dependency named in the existing 10-21 record. Source: `Evidence/M365_Evidence_PulseP2_2026-10-28.md` (transcript).')

# 4. P022 - new 10-27 sighting + re-raise escalation given nearing 10-30 milestone
append_body("P022", "pulse",
    '2026-10-27 (WAM Sprint Review, Loop): "EDM had not provided an ETA for correcting the source tables... country codes... remained unavailable for others." No correction owner named. Same blocker as 10-22, still no ETA, with the 2026-10-30 Data Enrichment milestone now three days out. Source: `Evidence/M365_Evidence_PulseP2_2026-10-28.md` (Loop).\n\n2026-10-28 (Claude, daily brief): Re-flagged on the boundary test -- unchanged blocker, no ETA, and the milestone this threatens is now inside the week. Escalation set back to candidate (was declined 2026-10-22).',
    new_fields={"escalation": "candidate", "escalation_test": "boundary"},
    bump_sightings=True, set_last_seen="2026-10-27")

# 5. P021 - new 10-27 sighting, no escalation change (already escalated via A29/W016)
append_body("P021", "pulse",
    '2026-10-27 (WAM Sprint Review, Loop): "Obtain timelines for shipping dates, country codes, and full vendor part numbers." Follow-up task: "Obtain a timeline from the remaining EDM team for completing the full vendor part number in UDM (Akansh)." Same status: Gangil, Akansh still working to obtain a timeline; still no ETA. Source: `Evidence/M365_Evidence_PulseP2_2026-10-28.md` (Loop).',
    bump_sightings=True, set_last_seen="2026-10-27")

# 6. P082 - set escalation on gap test (no new quote, field change + note)
append_body("P082", "pulse",
    '2026-10-28 (Claude, daily brief): Flagged on the gap test -- no owner has been named for the cross-application SkySpark API/types integration across two sightings (10-22, 10-27); escalation set to candidate.',
    new_fields={"escalation": "candidate", "escalation_test": "gap"})

# 7. K007 - additive detail, same 10-27 sighting, no sightings increment
append_body("K007", "pulse",
    '2026-10-28 (Claude, daily brief): Additive detail, same 10-27 sighting (already counted): Zaidi, Syed Jamshed committed to schedule a Dell architecture review once Elias Brewer returns, to recover the rationale behind prior implementation decisions Elias made alone. Elias is expected back today, 2026-10-28. Source: `Evidence/M365_Evidence_Daily_2026-10-28.md` (AI notes); `Evidence/M365_Evidence_PulseP1_2026-10-28.md`.')

print("--- phase 1 done ---")
