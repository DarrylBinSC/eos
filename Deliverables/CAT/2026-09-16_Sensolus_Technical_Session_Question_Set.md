# Sensolus Technical Session: Question Set
Prepared 2026-09-16 for the follow-up technical session Tom Mitchell is arranging. Intended as a working agenda for the Wesco technical participants.

## Purpose of the session

Establish what Sensolus provides at each layer of the solution, what can be unbundled, and what changes technically if Wesco takes data by API or takes device data directly. The session is for feasibility and constraints, not commercial negotiation, though the commercial questions in section 5 should be tabled so the pricing discussion can follow.

## 1. Devices and connectivity

1. Which tracker models are proposed for our asset classes, and what are the published specifications for each?
2. Which radio technologies do they use in North America (LTE-M, NB-IoT, other), and who is the network operator or operators?
3. Is connectivity supplied by Sensolus only, or can a customer supply its own SIM or eSIM profile?
4. What report rates are supported, and what is the battery life at each rate for our expected usage?
5. What is the expected field life of a device, and is the battery user-replaceable?
6. What environmental ratings and mounting options apply to cable reels and reel stands, including pressure washing, outdoor storage, and metal mounting surfaces?
7. What happens to coverage and reporting at customer sites where we control no infrastructure, and indoors?

## 2. Positioning

1. Which positioning methods do the devices use: GNSS, Wi-Fi access point scanning, cell tower identification, other?
2. Is position calculated on the device or in the Sensolus cloud?
3. If it is calculated in the cloud, what happens to accuracy and battery life if a customer does not use the Sensolus cloud?
4. What assistance data do the devices receive from Sensolus, and how often?
5. What is the realistic position accuracy in each mode, in the environments described above?

## 3. Data access and integration

1. What does the pull API provide, at what granularity, with what rate limits, and with what authentication?
2. What does the push API and webhook capability provide, including the MQTT option, and what event types can be subscribed to?
3. Is raw device telemetry available, or only processed positions and events?
4. Can Sensolus publish directly into a customer-owned MQTT broker over TLS, and if so, what is the message contract?
5. Is API access included in all plan tiers, or licensed separately?
6. What data retention applies, and in what form does our data leave at contract end?

## 4. Direct device integration

These questions establish whether Wesco could receive data from the devices without the Sensolus platform in the path.

1. Is the device endpoint configurable by the device owner, or fixed to Sensolus infrastructure?
2. What protocol and payload format do the devices use, and is the specification available to customers?
3. If a customer takes devices direct, what is lost: over-the-air firmware updates, configuration management, device diagnostics, remote commands, positioning assistance, support?
4. What is the quantified impact on battery life and positioning accuracy of operating without Sensolus cloud services?
5. Does Sensolus sell devices outright, and if so, are they usable on another platform or with a customer platform?
6. How are device credentials, encryption, and key management handled in that model?

## 5. Device management and field operations

1. How are devices provisioned and activated, and can they be shipped pre-provisioned and pre-registered to our asset identifiers?
2. What device management tooling is provided: fleet status, firmware version control, configuration profiles, health monitoring, alerting on silent devices?
3. What is the process and turnaround for a failed or damaged device, and what is covered?
4. What is the observed loss and failure rate across your installed base for comparable industrial use?
5. What does a customer typically staff to run a fleet of this size, if the customer takes on more of the stack?

## 6. Commercial questions to table

1. Pricing for each configuration: full solution; data access by API with your devices, connectivity and device management retained; hardware and connectivity without the application; hardware purchased outright.
2. What is included in each configuration on support and hardware replacement?
3. Volume tiers, contract term, and exit provisions.
4. Data ownership and portability terms.

## What we should leave with

A clear statement of which layers can be separated, what each separation costs technically, and a written pricing structure to follow. If the positioning and battery answers in section 2 and section 4 come back vague, treat that as the finding and push for specifics before any option is modeled.
