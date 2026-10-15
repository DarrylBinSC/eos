# Connected Asset Tracking: Provisioning and Commissioning Models
As of: 2026-09-16. Owner: Darryl Benson. Status: analysis and recommendation for review, not a decision.

## The distinction that makes this tractable

Darryl raised provisioning in the 2026-09-16 discussion as an open question: do we provision sensors in the field, or internally at Wesco before they are attached to assets? The question separates cleanly into two operations that are usually conflated, and separating them resolves most of it.

**Device provisioning** is everything that makes a tracker a working, addressable member of a managed fleet: activating the cellular subscription, loading firmware and configuration, pointing it at the correct endpoint, installing credentials, registering it in the device registry, and verifying it reports. It is a technical operation, it requires connectivity and tooling, and it fails in ways that branch staff cannot diagnose.

**Asset commissioning** is binding a provisioned tracker to a specific physical asset: mounting it, recording the tracker identifier against the asset identifier, and, where applicable, associating it with a sales order. It is a physical operation that can only happen where the tracker meets the asset.

The two do not have to happen in the same place, and they should not.

## Options

**Model A. Central provisioning at Wesco, field commissioning only.** Trackers are provisioned in bulk at a Wesco location (a designated site, or existing value-added services or kitting operations), tested, and held in an unassigned pool. They ship or are distributed already working. The field step is scan the tracker, scan or select the asset, mount, done.

**Model B. Vendor drop-ship pre-provisioned.** The vendor ships devices already activated, configured, and registered to the Wesco account. The field step is the same as Model A. Available only in options where a vendor retains the device layers.

**Model C. Field provisioning.** The tracker arrives unconfigured and is activated and bound at the point of attachment.

## Assessment

Model C should be rejected unless something forces it. Provisioning failures in the field happen at the worst moment, in a yard, with no tooling, no diagnostics, and staff who have other work. Every failure becomes either a truck roll or an asset that silently is not tracked, which is worse than not tracking it, because the data will be trusted. Cellular provisioning in particular depends on network registration that can fail for reasons invisible to the person holding the device.

Model B is the lowest internal effort and is available in Options 0 through 2 of the charter. It should be asked for explicitly in the commercial discussion, including whether the vendor will pre-bind devices to Wesco asset identifiers supplied in advance.

Model A is the recommendation for any option where Wesco owns the devices, and it is also the fallback under a partner option. It concentrates the technical work where there is tooling and expertise, produces a tested pool with known-good inventory, and reduces the field task to a scan. It also creates a natural inventory control point, which matters because trackers are small, valuable, and easy to lose before they are ever attached to anything.

**Recommendation: Model A for any self-built option, Model B where a vendor can provide it, and field work restricted to commissioning in all cases.**

## What the field step should look like

Keep it to one scan pair and no typing. A tracker carries a machine-readable identifier; the asset carries or is given one. The mobile step scans both, captures location and timestamp, and writes the binding. Where an asset has no durable identifier today, that is a prerequisite to solve, not a detail.

Design points that decide whether this works in practice:

1. **Device states must be explicit.** Provisioned and unassigned, assigned, in transit, at customer site, returned, in maintenance, retired. An unassigned tracker reporting from a customer site is an exception, not a data point.
2. **Activation on first motion or first fix**, so an unassigned pool does not generate noise or consume battery unnecessarily.
3. **Binding should happen as early in the flow as it reliably can.** Binding at pick or pack, inside a Wesco process with scanners and discipline, is more reliable than binding at delivery. The sales order association discussed in the meeting is easier at the same point, because the order context is already present in the transaction.
4. **Unbinding on return is a real step with a real owner.** A returned asset with a stale binding corrupts the record faster than a missing binding does.
5. **The system of record for the binding should be one system.** ADM is the strong candidate: it is on this team, it is connected to DDP for sales order data, and it already exists to hold asset records.

## Attachment and physical durability

Not strictly provisioning, and it belongs in the same operating decision. Mounting method, tamper and removal behavior, survivability through pressure washing and outdoor storage, and whether the device can be moved between assets all shape the loss rate, and the loss rate drives the economics of owning devices outright. The pilot of 400 trackers has this evidence and it should be recovered before any new physical testing is commissioned.

## Fleet operations, the part that is not a project

Whoever owns this owns a recurring operation: batteries, damaged and lost devices, replacement stock, the daily list of assets that stopped reporting, and the escalation path when a customer site goes dark. In the vendor subscription this is absorbed in the monthly fee, including hardware replacement. In a self-built option it is a named team, a budget line, and a service level. Costing a build without costing this is the most common way these programs are approved and then disappoint.

## Open questions for the field operating model workstream

1. Who physically attaches trackers today in the pilot, and at what point in the process?
2. Do the in-scope assets carry durable, machine-readable identifiers today?
3. What is the annual tracker loss and damage rate observed in the pilot?
4. Which Wesco location would hold a provisioning and staging function, and does it have capacity?
5. What does the branch experience have to look like for this to be used rather than worked around?
