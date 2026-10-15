# entroCIM Sensolus Connector
As of: 2026-09-16. Source: three Confluence page exports provided by Darryl Benson on 2026-09-16 and filed in this folder. Status: built and syncing. This file is the durable catalog of what the connector delivers; the PDFs are the primary record.

## Source documents

| File | Confluence space | What it covers |
|---|---|---|
| `2026-09-16_SD-Sensolus_Connector.pdf` | Software Development | Ten use cases the connector supports, with integration points and sample KPIs |
| `2026-09-16_CON-Sensolus_Connector_Data_Points.pdf` | Connectors | Learn hierarchy, every data point group, and a screenshot of points in sync |
| `2026-09-16_CON-Sensolus.pdf` | Connectors | Background on Sensolus devices, connectivity, and platform, with the entroCIM positioning statement |

## What was built

An entroCIM connector to the Sensolus cloud API. The connector record is `ItwSensolus Conn` and current values resolve through an `itwSensolusCur` path, which is the standard SkySpark connector pattern: entroCIM polls the Sensolus API and binds the returned attributes to points. The sync screenshot in the data points page shows points live with a 15 minute poll interval (read from the screenshot, worth confirming with the team before it is quoted anywhere).

This is a platform-layer integration against the vendor application, not a device integration. entroCIM reads what Sensolus has already collected, decoded, and positioned.

## Learn hierarchy

```
ItwSensolus Conn
  Organisations
    Wesco
      Attributes            id, name, organisationType, organisationStatus, createdAt, currency
      Assets
        <device serial>     e.g. SNT4 DFU624, SNT4 1R61TQ, SNT4 ADAVZN
          Attributes
          Subscription Info
          Firmware Info
          Battery Info
          Device Tags
          Last Geozones
          Active Alerts
          Current Process State
```

Device serials carry the SNT4 prefix, which is the Sensolus StickNTrack device family.

## Data points by group

**Attributes.** name, serial, decoratorColor, imei, iccid, mac, status, sigfoxActivationStatus, firstMessageAt, lastSeenAlive, lastDeviceConfigUpdate, productKey, productName, lastAddress, lastLocationUpdate, lastLocationSource, lastLocationAccuracy, totalDistance, lastPeriodicDetected, lastActivityDetected, lastActivity.

**Subscription Info.** contractStartDate, originalStartDate, startDate, endDate, lengthInMonths, autoStartAfterInMonths, state, startTrigger, autoRenew, autoRenewLengthInMonths, invoicingPeriodInMonths, invoicingScheme, currentBillingPeriodStart, currentBillingPeriodEnd.

**Firmware Info.** currentFirmwareSha, lastDeviceFirmwareUpdate.

**Battery Info.** batteryLevelPercentage, batteryEstimationCalibrated, estimatedRemainingBatteryLife, updatedAt, lastBatteryVoltage.

**Device Tags.** id and name per tag. Observed tag values include "NEW" and "Insta Reel 48 W", which confirms the asset class name that the 2026-09-16 meeting transcript rendered as "Insta Reels."

**Last Geozones.** id, name, image, enteredAt, coordinates. Where no geozone data exists, the connector falls back to the asset's last known position by combining lastLat and lastLng into a Coord point.

**Active Alerts.** date, alertType, title, Alert Rule (id, title), Monitored Entity (entityType, serial).

**Current Process State.** processDefinitionId, processName, state, stateLabel, exclusive, enteredAt.

## Use cases the connector is documented to support

Organization and tenant management; asset and device inventory; real-time device health monitoring; battery and device maintenance; firmware and configuration compliance; real-time location and asset tracking; asset movement and utilization monitoring; subscription lifecycle management; alert and incident management; operational process tracking; asset tag and business metadata management. Each carries sample KPIs in the Software Development page.

## Why this matters beyond entroCIM

The connector is evidence in the returnable asset tracking build-or-partner question, and it changes where that question sits. See `Products/CAT/03_Architecture/CAT_Five_Layer_Model_2026-09-16.md`.

Three points carry over:

1. The data plane and the application layer are no longer hypothetical for this use case. entroCIM already ingests Sensolus asset, location, alert, and process data and can model it. The "build our own application" half of the leadership direction is substantially de-risked and partially delivered.
2. What the connector reads reveals what the vendor's device management layer produces. Firmware SHA, last firmware update, battery level, calibrated battery estimation, estimated remaining battery life, last seen alive, last device configuration update, and Sigfox activation status are all vendor outputs. In a self-built option, nothing produces these unless Wesco builds or buys a device management plane. The connector is therefore a precise inventory of what would have to be replaced.
3. The connector depends on an active Sensolus subscription and on the Sensolus cloud. If the subscription ends, the integration stops returning data. This is a real dependency created by completed work, and it should be understood before any decision to exit the vendor.

## Known assumptions and limitations

- Device tag selection is implemented as a dropdown on device name, with the device id written into the `itwSensolusCur` path on selection. The documented assumption is that device tag data does not change frequently. If tags become a live business classification, that assumption needs revisiting.
- `sigfoxActivationStatus` in the attribute set indicates Sigfox lineage in the device fleet or the API surface. Sensolus North America devices are marketed on NB-IoT and LTE-M. Which radio the Wesco fleet actually uses is not established by these documents and matters for coverage and for any direct-ingest option.
- The three device serials in the documentation are development or test examples. Nothing here establishes fleet size, deployment status, or which assets are currently instrumented.
- Poll interval, API rate limits, historization strategy, and error handling are not documented in these pages.

## Open questions for the entroCIM team

1. What is the poll interval, and what are the Sensolus API rate limits at fleet scale?
2. Is history being stored in entroCIM, or only current values?
3. Which Sensolus API endpoints are in use, and does the account tier include them under the current contract?
4. Which devices and which asset classes are connected today, and to which organization records?
5. Who owns this connector for support once it is in production use?
