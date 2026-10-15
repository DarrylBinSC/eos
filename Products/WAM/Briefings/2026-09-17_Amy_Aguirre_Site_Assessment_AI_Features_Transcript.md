# Site Assessment and AI Features — Amy Aguirre, Darryl Benson

**Meeting:** Site assessment / AI features, September 17, 2026, 6:00 PM UTC, 19m 30s
**Attendees:** Darryl Benson, Amy Aguirre
**Source:** Teams meeting recording transcript, complete. Extracted from `2026-09-17_Amy_Aguirre_Site_Assessment_AI_Features_Transcript.docx`, filed alongside this file.

> Read alongside `2026-09-16_Sunny_Sharma_Strev_Sync_Transcript.md`. The two conversations are one day apart and describe the Virtual Site Survey differently. Where they conflict, both statements are recorded below rather than reconciled by inference.

**What this transcript establishes, and where:**

- **1:36 to 2:18 — the July TS/TSS document is a solution brief, not a decision.** Amy: "that was a requirements document... the solution brief that the TS team had built... there have been no decisions in terms of are we going to use Avatore." TS is still researching LiDAR options. **Strev has never spoken to Avatore (5:30).** The Avatore plus Pano XV2 architecture Darryl quoted to Sunny on 09-16, and which is in the document sent to Lisa, is a wish list item, not a selected architecture.
- **2:18 to 3:32 — the business problem behind the requirement.** Site assessments are done today by contractors on pen, paper and spreadsheets, with no LiDAR and no mobile app. A remediation plan takes about six months because the plan waits on contractor deliverables, and contractors are sometimes sent back on Wesco's dime for detail they missed.
- **4:25 to 5:13 — what Strev is actually building.** An uploadable assessment or checklist (the MOP equivalent), delivered to the contractor in a mobile app, with templates reusable across similar customer engagements, giving real-time visibility of data as it is collected. TS builds the checklist content.
- **5:30 to 5:55 — the LiDAR scan was Strev's proposal, not Wesco's request.** Amy: TS "didn't realize that you can do LiDAR scanning on an Apple device. So he said, hey, would you like us to look at building in the LiDAR scanning into your checklist? And so that's how that ended up coming to be." This matters for Lisa's question about who asked for what.
- **6:40 to 6:54 — a self-service variant is on the table:** the customer performs their own LiDAR scan, removing travel and contractor cost.
- **6:54 to 8:52 — the AI element is asset extraction feeding a data service.** Photograph a cabinet, extract the assets in it via AI (proven previously with Centermis label scanning), load them into Wesco Asset Management, then Amy's team runs data validation and enrichment (warranty, end of life, end of service, discontinued, extended warranty available) and reports out for TS remediation planning.
- **9:04 to 10:13 — the people.** Wade Bursch (TS, reports to Matt Powers) is the business lead and is building the business case and the UiPath intake. Chris Wagner wrote the requirements and reports to Wade. Wade's team does the TS audits, inspections and RCDD design work. Mike Wassel attended the calls; Christian also named. Matt Powers wants a pod of engineers working this data, and wants live conference feeds with contractors, which is outside the mobile app scope.
- **10:46 to 11:20, 13:48 to 14:15 — it is a prototype, in Strev's demo environment, not in Wesco Asset Management.** Amy: "it's a prototype in Strev... today it's in a demo prototype environment within Strev. It is not within the Wesco Asset Management." Built in about a month, at no charge, following a live demo to TS that produced unanimous support. Strev still has work to do to finalize and integrate it. **This is the direct conflict with Sunny's 09-16 characterization** ("a real product, not a prototype", two months of work with the partner).
- **11:33 to 12:19 — the governance route.** Wade brings the business case and the PowerPoint; a demo has been requested in front of "Kehr" (name as transcribed, unverified). Amy is filing it as an AI use case because the LiDAR scan, the AI data extraction and the smart Excel upload are all AI.
- **12:28 to 13:27 — commercial shape, not yet priced.** Amy has asked Sunny and Christina for professional services development pricing plus a **per-site** pricing model, explicitly not asset-based. Delivery would be another entity type inside the existing white-label instance ("on the left hand side where you've got assets, contracts, suppliers, you would just have sites"), not a separate instance.
- **14:33 to 15:13 — the AI feature set is unchanged from the May position, except it has shipped.** What was a roadmap item in the May entitlement document is now available. Darryl has asked Sunny and Christina for a new entitlement document.
- **15:13 to 16:08 — $84,000 per instance to enable AI, unconfirmed until Christina sends it.** Darryl: "the per instance AI, turn on AI is $84,000... until it comes from Christina, it's not fully confirmed." Strev now has a harness that lets customers supply their own API keys.
- **16:08 to 17:54 — Amy names three features she needs in next year's budget**, and is putting the $84,000 into the WAM AOP: (1) AI data extraction, (2) the site survey capability, (3) **data normalization**, a cleanup feature that groups variant labels captured in the field (all caps, lower case, one word, two words) and normalizes the database on a selected value. The Software House upload is her worked example.
- **17:54 to 18:16 — Darryl's assumption, stated as an assumption.** He believes all three sit inside the $84,000 and that there is nothing additional to the business, and says he will confirm against Christina's entitlement document.
- **18:23 to 19:17 — ownership of the next steps.** Amy files the UiPath intake herself, since she holds the PowerPoints and the demo; Darryl asked to be optional on it. Darryl kicks off the white-label agreement amendment once the entitlement document arrives, and keeps Amy informed. Darryl asked to be invited to the Site Survey demo.

---

Site assessment _  AI features-20260917_180031UTC-Meeting Recording
September 17, 2026, 6:00PM
19m 30s

 started transcription

Benson, Darryl   0:11
Amy, how are you?

Aguirre, Amy   0:12
I'm good, Darrell. How are you?

Benson, Darryl   0:14
I'm good.
Camera always defaults off, which is a good thing, but they always have to remember to turn it on.

Aguirre, Amy   0:22
Yeah, for sure.

Benson, Darryl   0:23
Hey, so I talked to Sunny. I'll just start out with the most recent thing in my mind. Talked to Sunny yesterday and he wasn't up to speed on most of the, you probably know this, but he wasn't up to speed as freshly as probably you are on the survey tool.
And I was just quoting from the recommendation from TSS from July. And he was talking about how he was going to deal with Apple kits and things like that. I said, well, it looks like we're going with Avatore and a...
Pano X camera. He said, oh, oh, oh, that's different than I knew of. That's different. So wanted to talk to you about, is it, are we using Avatur just and integrating into?
Sorry, into Strev or is it within Strev? It wasn't clear to me. And then I looked at the presentation and just in looking at the documentation without seeing it, I just got a little bit like, okay, I don't quite understand what's going on. It only matters just so I understand it. There's no,
decision point here I just wanted to understand.

Aguirre, Amy   1:36
Yeah, so I'll take you back to the beginning of the project, right? So the requirements document that you see there, that was a requirements document. That was the solution brief that the TS team had built, right? So there have been no decisions in terms of

Benson, Darryl   1:54
K.

Aguirre, Amy   1:56
Are we going to use Avatar? Are we going to use a different? They are currently in the process of investigating and researching the various different LiDAR solutions that are available. There are a couple of different options in terms of how they want to or how they could potentially utilize the tool sets that

Benson, Darryl   2:03
Okay.

Aguirre, Amy   2:18
have been built for the site surveys to do virtual site surveys. So one is we have this kit with a LIDAR camera in it. Maybe we did deploy a contractor to go out there and do these, which we do today already when we do it all manually, although
There is no LIDAR. There is no mobile app. They do this all manually on spreadsheets. And it takes them about six months to build a remediation plan because they have to wait until they get all of the deliverables back from the contractor. In some cases, they actually have to send the contractor back out because they didn't get the right details. And that
is done on our dime. And so there's all these kind of business challenges that are driving their requirements. So that being said, think of that TS document as a, hey, this is our wish list. This is what we think we want to do. These are some of the things we've explored and experienced. And
And then they came to us and they said, hey, so based on what we did with Walmart, which is a very similar use case, we want the ability to take this Excel spreadsheet, which basically is a task list, right? We want to be able to upload it and provide it in a mobile application to the contractor so that we can check off all of the things and provide directions.

Benson, Darryl   3:32
Yeah.

Aguirre, Amy   3:50
so that it's not on pen and paper, it's not manual, it's not in an Excel spreadsheet. And that will give them then the opportunity to be able to, in real time, see data as it's being collected.

Benson, Darryl   4:02
Would you treat so in my career, I?
run lots of site assessments and so I we're talking the same language. Would you call that like the we call them we call them MOPS method of procedure or or SOPs that MOPS or SOPS is that initial spreadsheet where you're telling the supplier what to do kind of the MOP for that that scope?

Aguirre, Amy   4:25
Yeah, yeah. And so the TS team is responsible for building that. And they call it an assessment or a checklist. And so every customer engagement might have a little bit of variation as it pertains to that. But they've got what they wanted to be able to do is have templates so that they could, if they know that they've got a customer that is

Benson, Darryl   4:32
Okay.
Yeah, yeah.

Aguirre, Amy   4:48
has a similar use case, maybe they're doing it for Elevance and TD Bank now wants to do it or BMO wants to do it. There are similarities, maybe a few modifications. They want to be able to take that template, load it, make a couple of just minor changes within the application and then be able to quickly get off and running, right? It'll help.
decrease their prep time and also decrease their delivery time. So.
So that's what we did. We sat down with them. They gave us their requirements. We had a number of different interviews. We tested a bunch of different things with them. We found...

Benson, Darryl   5:27
With it with Avatore or just with TSS, just...

Aguirre, Amy   5:30
No, we've never spoken to Avatoire. We TSS, so the TSS team. And those are the meetings that Mike Wassel was sitting in on, right? So we told them, yeah, this is definitely something we can do. We did something very similar for Walmart. There were a couple of things that Sunny and the team had researched and investigated. One of them was LIDAR scanning. So when they gave us the required

Benson, Darryl   5:32
Okay.
Okay, okay.

Aguirre, Amy   5:55
Initially, they didn't realize that you can do LIDAR scanning on an Apple device. So he said, hey, would you like us to look at building in the LIDAR scanning into your checklist? And so that's how that ended up coming to be.
And...
Now that they've seen that there is that possibility, there are some tweaks that we probably would want to make if we did want to utilize the application or the Apple devices to do the LiDAR scanning. One of the applications that they had talked about potentially using is having the customer
you know, go in and do their own LIDAR scanning. And right. And that would then give us the ability not to have to go travel there, not to have to go send a contractor so they could do these assessments, kind of self-service type of a service offer.

Benson, Darryl   6:40
Walker.
Yep.
Yeah, just get in the game, yeah.

Aguirre, Amy   6:54
That's right. So there were so another a couple of other elements where obviously we are trying to sell more products, right? And so they wanted to see, you know, can we take a picture of a cabinet and can we extract all the assets that are in that cabinet?
you know, automatically utilizing AI. So that was another capability that we utilized. We can do that with, we showed that we could do that with Centremis and scanning labels, taking pictures of label and extracting data. And now we showed it with the cabinets. So we're bringing in those assets. And that's really important because then
My team can come in, right? And what we're building as a service around data validation and data enrichment. So very similar to what we did for Centremis. We went in and we said, okay, let's look at, are these within warranty? Are they end of life? Are they end of service?
Are they discontinued? Is there a warranty associated? Is there an extended warranty available? And we're populating all that information into the WESCO Asset Management Tool, so you've got a better picture. And then once that data is built, we can provide reporting, analytics, outcomes,
through some of the dashboard and capabilities within the tool for the TS organization. And they can build their remediation plans based on that. So.
That was really the intent and the spirit in which the application was developed and the team. And so I worked closely with Wade Bursch, Christian, Chris Wagner, like you said, Mike Wassel was on the calls.
Um, and then directly with Sunny development team to to to pull that together.

Benson, Darryl   8:52
So what's the final, what is Wade? I don't know Wade, but what's he bringing to the company? He's going to go through a process and do intake for something.

Aguirre, Amy   9:04
Yeah, so Wade, so we, you saw the PowerPoint. So we did a live demo for them to determine, hey, is this, they built the prototype, we did a live demo for them. We said, okay, is this, will this work? Is this something that you, you know, you want to want to do? And it was unanimous, right, at that point in time. We didn't have an answer from them until after we did that demo.

Benson, Darryl   9:18
Yep.

Aguirre, Amy   9:27
And obviously Matt Powers, so Wade Bursch works for Matt Powers. Wade is on the TS team. They do all of the RCDD work, the land, yeah, they're designers, right? They're engineers. And so what Matt Powers wants to do is he wants to create a pod of engineers that can

Benson, Darryl   9:38
Yeah, yeah.

Aguirre, Amy   9:48
interact with this data. And there are some other elements outside of the mobile app, like they want to be able to do live conference feeds with the contractors, things like that. So Wade is the...
business lead, right, who, because Chris Wagner, who built the requirements, reports to Wade, Wade leads that group, and Wade's team does all the TS audits and inspections. And so he's going to put in the UI path per Lisa, and he's going to put in.

Benson, Darryl   10:13
Okay.
So, what are the third, what are the third-party tools that were settled on then?

Aguirre, Amy   10:29
There are no third-party tools at this point in time other than Strap. They're still doing their research in terms of, you mean the LIDAR camera?

Benson, Darryl   10:39
No, like, yeah, so, so...
Now that I understand that that's like a brief from July. The final, so Strive built something, where is it running on their servers?

Aguirre, Amy   10:46
Yeah.
That's right, it's a it's a prototype in Strav, because, as you know, we have not.

Benson, Darryl   10:52
Yeah.

Aguirre, Amy   10:59
We have not put the AI capabilities or AI through WOB, right? The way up the WOB, so...

Benson, Darryl   11:05
Yeah, yeah, that's my next topic with you, so yeah.

Aguirre, Amy   11:08
That is, so yes, so today it's in a demo prototype environment within Strav. It is not within the Wesco Asset Management.

Benson, Darryl   11:20
Oh, that's fine. I just so if if it's if it's a prototype and then we'll take so so what is Wade bringing to UI? What is Wade bringing to intake the?

Aguirre, Amy   11:33
What he is bringing, he's building the business case for the application, and then he is bringing the PowerPoint. And we've been asked to do a demo in front of Kehr on the
Application.

Benson, Darryl   11:53
West Coasset Management's already been through intake. Is he putting an, he's strictly calling this an AI use case then? Okay, cool. Okay.

Aguirre, Amy   12:02
Right, because there are, because the LIDAR scanning and then the AI data extraction, all of that, and the uploading, the smart upload of the Excel spreadsheet into the tool, that's all being done by AI, right? So we need to put it through the AI counts.

Benson, Darryl   12:19
For sure, for sure. So, so we're gonna we're gonna attach it into the Strev white label Strev as a as a product.

Aguirre, Amy   12:28
Potentially, right? So the next steps are, you know, with Sunny and Christina, I sat down with them, I said, okay, we need to get some pricing around this because this is outside of the, you know, current use case, right? And so they're going to provide us with some professional services, development, pricing.
And then they're also going to provide us with a per-site pricing model for going.

Benson, Darryl   12:56
For a site, like a site of substance pricing model, not an asset-based pricing model. OK, that's great. And then, so that might be a separate instance of Strive. You get, you would you think, or because we can we put it in the we put it in the white label version just as another feature, right?

Aguirre, Amy   13:02
Correct.
Yeah, so the way that it would look is there would be a, so you know on the left hand side where you've got assets, contracts, suppliers, you would just have sites. And so it would be another,

Benson, Darryl   13:27
It's just another feature of Strive that we'd have them build and turn on. I got you there. That's great. Just let me know and maybe invite me to the meeting. I'd like to see the demo. Yeah, I'd like to see it. It sounds cool. And it sounds like, you know, it happened pretty quickly too. So.

Aguirre, Amy   13:38
Pretty cool.
Yeah.
I did. I think it took them about a month. Yeah.

Benson, Darryl   13:48
So did they, are they going to, is that prototype phase and they're going to charge us for finalizing the development, right? This is just vibe coded. It just kind of works. It's not integrated into their platform yet fully.

Aguirre, Amy   14:03
Um, correct, correct. I mean, I it it's more than just vibe coded for sure.

Benson, Darryl   14:04
Okay.

Aguirre, Amy   14:10
Yeah, but it's.

Benson, Darryl   14:12
It's a prototype. It's not, they still need to do X amount of work to finalize it. Okay, and they didn't charge us for the prototype, but they'll make it up on the back end. That's really good news. Thank you for sharing that. The next thing, because I just want to be conscious of time, the AI entitlement, or I'll just say the AI.

Aguirre, Amy   14:15
Yeah, it's a prototype.
And.
That's right.
Yeah.

Benson, Darryl   14:33
feature set that I shared with you a couple months ago, it is basically still the same from my conversation with Sunny. What what you've specifically asked for in your in your request to Lisa, and I'm not going to try to quote it because I'm not remembering exactly how you worded it, but it's basically the enrichment and the the auto.

Aguirre, Amy   14:36
Yep.
Yeah.

Benson, Darryl   14:52
Basically the two functions, and you know this, but I'm just confirming with you, that's going to be built into the core. What was in the May entitlement document was a roadmap item. It's now available. So I've asked Sunny and Christina for a new entitlement document, basically just a new version of what they already gave me.

Aguirre, Amy   15:05
Yeah.

Benson, Darryl   15:13
It's going to have all the it's going to confirm the pricing and now they've got a now that they've got a
an AI harness that allows people to put their own API keys into it, even better. They're still on paper, I don't know what he's going to charge Wesco in the white label. They want to say $84,000 per instance to enable AI. I don't know what you've negotiated with them, but
That's still in.
And I confirmed with him yesterday, until it comes from Christina, it's not fully confirmed, that the per instance AI, turn on AI is $84,000. I just wanted to make sure you're aware of that in case it slaps you guys in the pocketbook. I say you guys, the business in the pocketbook.

Aguirre, Amy   15:58
Yeah, I'm putting I'm putting the AOP together for Wasco Asset Management, and I'm going to include that 84K into the budget for us, because it's going to be, and there's a there's another there's another use case feature.

Benson, Darryl   16:08
Okay.
Okay.

Aguirre, Amy   16:19
that I want for our team, especially because we are going to be doing this research data and data analytics stuff is the data validation or the data cleanup. So they've got a feature where
When you upload the data, for example, we just uploaded a bunch of data for Software House, for example, not a vendor that WESCO works with, it's outside. But when we scanned all of the information, some of the labels were all caps, some of them were lowercase, some of them were two words, some of them were one word. So
They're they've built in a feed.

Benson, Darryl   17:00
Oh, this was that data capture in the field.

Aguirre, Amy   17:03
Yeah, data capture in the field. So in the, but in the web application, so then my team went in and they cleaned all that up, right? With the help of Strap. And then, so what they built was a feature that basically says, I'm going to capture all of the common.

Benson, Darryl   17:04
Okay.

Aguirre, Amy   17:22
items, right? And I'm going to give you an option to select which one you want to normalize on, and then they click on that and everything gets normalized in the database. So that's another feature set that I'd like to include because as we're uploading data from
our warehouses, from the field, from customers, that's going to help tremendously decrease our time to value for the customer. So those are the three that I'm looking at that we really got to have in next year's budget.

Benson, Darryl   17:54
OK, so I...
Okay, I think, and I'll find out once I get it from Christina, unless you've got it already. Christina is going to send me that entitlement doc. I think for my conversation with Sunny, that's all going to be covered, should be covered in that 84 grand. All of those, all of those features. So it shouldn't be anything additional to the business for that.

Aguirre, Amy   18:16
Yes.
Yeah.

Benson, Darryl   18:23
And from an AOP perspective, AOP, sorry, from a WOB perspective or an intake perspective, are you starting that process for the AI or would you like me to start that process for the white label version?

Aguirre, Amy   18:41
I can do it. I can just put it in the UI path. That's fine, because we're going to have to do the whole demo and I've got all the PowerPoints. So I'll just, I did ask for that third one. So yeah, I can, it's not an intense process, right?

Benson, Darryl   18:58
That's fine. Yeah, just if you don't mind making me optional on that too, be happy to lean in when you can. So once I get the entitlement, I'll kick off the contract renewal, or not renewal, amendment process, and I'll keep you informed of how that goes.

Aguirre, Amy   19:17
Yeah, yeah, that sounds good.
Shait.

Benson, Darryl   19:20
Okay, great. Cool. I'm glad we're caught up. Thank you.

Aguirre, Amy   19:24
Yeah, no problem.

Benson, Darryl   19:25
All right, have a good one. I'll see you later.

Aguirre, Amy   19:27
Okay, you have a good weekend. Bye-bye.

Benson, Darryl   19:28
You too. Bye bye.

Benson, Darryl stopped transcription