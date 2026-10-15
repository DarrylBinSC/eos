# JCI OpenBlue Airwall MSP — One-Page Brief
As of 2026-07-17 · Working brief for Darryl · Supersedes the 07-16 Issues & Actions Summary for day-to-day use

**Position in one line:** The value is the MSP agreement as a whole — it flips Airwall licensing from 12-month prepaid orders to a consumption model (license pool, pay-on-provisioning, true-down). Hosting the Conductor in Wesco Azure is the critical enabling change we must make to the agreement; the licensing flip is the commercial payoff. Both must be durable in the contract text.

**The decision — two things land in the agreement, or no signature:**

1. **Express hosting rights** — the agreement (body or Order exhibit) permits Wesco to host and manage the Conductor and MSP infrastructure in Wesco Azure, with JCI limited to API-based license monitoring plus support access Wesco authorizes.
2. **Licensing mechanics codified durably** — pool grant, billing monthly in arrears only on provisioned licenses, true-down when provisioning drops, licenses as Wesco's movable asset. Stated in the agreement or a document it references that JCI cannot change unilaterally — **not** in MSP Program Materials subject to the unilateral-change clause.

## Settled — argue from these

- MSP model (not reseller), JCI-branded, affiliate controls, tariff absorption, notice-period asks — decided 2026-05-26.
- Conductor live in Wesco Azure. **Wesco is the hosting authority**: environment owned by Wesco, application owned by my team; patching, backup, DR, SLA, security addressed under Wesco governance. HA failover: Wesco IT, Azure IoT subscription.
- JCI's account team **verbally confirmed the model** (07-15 call): Wesco keeps hosting and provisioning its own Conductor; JCI adds a read-only metering agent; billing monthly in arrears on provisioned licenses (vs. 12-month prepay today).
- 443-only connectivity available now — our biggest deployment friction is gone.

## Open — JCI owes

1. **Hosting language** — express grant, or confirm Conductor/Relays qualify as "Non-Hosted JCI Offerings."
2. **Licensing mechanics in durable text** — where in the agreement are pool grant, provisioning-triggered billing, and true-down stated, and can JCI change that document unilaterally?
3. **Metering API data scope** — "read-only license usage" defined contractually, not verbally.
4. **Support obligations to Wesco** (L3 / escalation / SLA on the Conductor) — the only unresolved element of the hosting responsibility model.
5. Customer agreement requirement — who contracts with whom for MSP customers.
6. Final MSP pricing — the rate side of the licensing flip; mechanics favor us, rates unverified.
7. Named JCI counsel for Brian Miller.

## Open — Wesco owes

- **WAB approval** of the JCI API connection from the Conductor — before markups commit that access.
- **Legal positions** (Brian + me): indemnity breadth, liability-cap carve-outs, unilateral change rights, non-cancelable orders, price-increase notice, customer flow-down / no termination-for-convenience, competing-offerings scope (watch the entroCIM–OpenBlue overlap).
- **Order exhibit** documenting the hosting model as it runs — only negotiated element is JCI's support commitment.

## This week / next

| Action | Who | When |
|---|---|---|
| Brian Miller refresh meeting (email sent 07-17; invite on his reply) | Darryl + Brian | Week of 07-20 |
| Re-engage Gutierrez/McCorvey: Non-Hosted question, support obligations, pricing, counsel | Darryl | ~07-23 |
| Submit JCI API connection to WAB | Darryl → WAB | Before markups |
| Confirm provenance of the agreement review summary | Darryl | Now |

## Watch-outs

- **Execution ahead of contract** — the hosted model is live with no contract in place at all; every week unsigned extends unpapered exposure.
- **Verbal ≠ contractual** — the 07-15 confirmations (hosting assumption, billing mechanics) are account-team, not agreement language.
- **Unilateral-change clause vs. licensing economics** — if the consumption-billing mechanics sit in MSP Program Materials JCI can change unilaterally, the commercial value of the flip is revocable post-signature. This is the sharpest interaction between the new terms and the deal's value.

*Relationship track (separate): Kehr–Priya intro; Jeff owes 443 video, booking link, Aug-15 Ascent POC invite.*
