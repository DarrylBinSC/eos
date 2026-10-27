# SkyFoundry Build 4.0.7 Release Notes (23 Oct 2026)

Source: SkyFoundry release announcement for Build 4.0.7, circulated by Ron Snyder, received from Darryl 2026-10-26. Verbatim text below; summary and assessment in `Products/SkyFoundry.md` and `Products/entroCIM/entroCIM.md`.

---

We have posted 4.0.7 as the second production release of the 4.0 series. This is one of the biggest releases yet!
Overview
xeto.dev is live
New Namespace | Install view to install/update from xeto.dev and other repos
Woolly new background agent engine
Woolly support for plan mode
Woolly chat view support for inline tables, charts, and questions
Woolly new routine observable framework
Woolly support for custom providers
New Model app and three new views for working with Xeto data
Xeto sugar types
Xeto new validation engine
Xeto RDF export
Jeto - new Xeto flavored JSON with JSON Schema support
New v5 HTTP API with Swagger/OpenAPI support
Modbus enhancements
Demogen now generates central plants and water loops
Security
As the AI models continue to improve, we are continuously looking at ways to harden our security. This build includes many hardening features for HTTP and arcbeam. Also included in this release is one very important security fix for TLS hostname verification. See post 9113 for more details.
Woolly
We are introducing a huge number of new features to the Woolly AI harness:
Chat view support for inline tables, charts, and questions
Plan mode
New AiRoutines to run agents on observable events
New multi-threaded background engine
Support for custom providers (gateways, local LLMs, etc)
Woolly has been redesigned with a new background engine that makes it seamless to run multiple agents simultaneously and quickly switch back and forth between them. The new engine also supports autonomous background agents that we call AiRoutines.
The chat view has several new features. The show tool can be used for Woolly to show you an inline table or chart now. The view data is not part of the conversation and is refreshed manually or each time the conversation is loaded. Tool calls are now shown in the conversation and can be expanded to see details. You will also note current agents running in the top, right corner - click to quickly switch between multiple agents (an orange dot indicates an agent is waiting for your input).
Woolly now includes a plan mode. We have annotated every function that performs database commits, file writes, network calls with a new <sideEffects> meta tag (you should add this to your own functions too). Woolly now has three modes:
plan: cannot call any side effects functions
confirm: will ask to call side effects functions
auto: full access to run under your user account permissions
You can toggle the mode from the Chat toolbar.
This version also includes a new feature to run background agents which we call AiRoutines. Routines are configured to run off any observable event just like the task framework. For example you can schedule a routine to run at a specific time of day or when a new spark is detected. The routine takes a prompt and can evaluate axon to accomplish the desired outcome.
Also in this build there is a new Woolly | Providers tab that lets you create custom providers. This enables you to connect thru LLM gateways, other providers, and local LLMs if they support the OpenAI protocol (which most do). See the docs for further info.
We have spent considerable time improving Woolly's ability to wield axon for getting work done. And we have added many new skills. One important skill to note is the know-perf skill that lets Woolly perform a full diagnostics check on your server's performance.
We are offering Woolly at no charge until 1-May-2027, after which a "server pro" add-on will be required.
Xeto Overview
Xeto is feature complete in 4.0.7. We have added many new features:
xeto.dev is now live for install/update/publish
Xeto CLI support to publish to remote repos
Jeto - new Xeto flavored JSON with JSON Schema support
New HTTP v5 API using Jeto that is Swagger/OpenAPI compliant
Sugar specs
New validation engine
Mixins can now declare globals
Xeto new packaging rules via include and publish tags
New libMaturity enum for libs (alpha, beta, stable)
Initial RDF support
The major Xeto features are discussed in further detail below.
Xeto.dev
The xeto.dev is live! This is the cloud based community repository to share Xeto libs and see all the documentation. We will be running a beta test for the next few weeks. If you would like to participate in testing to publish xeto libs to the website then email support@skyfoundry.com. Once the beta testing is over, we will wipe the website and open it up for the general public to create their accounts.
Xeto Sugar Specs
Sugar specs are a new feature to guarantee interoperability in the face of the exploding tag combinations. Sugar specs are based on a nominal anchor spec plus a set of tag constraints.
In the Haystack ontology we have divided nominal specs and sugar specs into different libs using a ".x" convention:
ph.equips.x: sugar specs for equips
ph.points.x: sugar specs for points
ph.elec.x: sugar specs for electrical points
See Sugar chapter for the specification.
Xeto Validation
We have replaced the original "fitsExplain" validation engine with a new validation engine. This engine is based on a formal set of validation rules identified with a Xeto instance. The new engine supports adding your own custom rules via Fantom or Axon.
As part of this redesign the fits and fitsExplains functions are replaced with a new validate() function.
See Validation chapter for more details.
Jeto
This build introduces a new JSON format with the nickname Jeto. It is a new xeto-typed flavor of JSON. Unlike Hayson it produces clean, simple JSON by relying on Xeto specs for typing information. Jeto includes support for generating JSON Schema and is the default format of the new HTTP v5 API.
See Jeto chapter for the specification.
HTTP API v5
We are introducing a new version of the HTTP API dubbed "v5". The new version is fully backward compatible with the existing version. You opt into the new version with the HTTP header "Xeto-Version:5". The v5 version generates a Swagger/OpenAPI schema under "/api/proj/openapi" using the new Jeto JSON format.
See HTTP API chapter for all the details.
Xeto RDF
We have published an initial specification for how Xeto exports to RDF. It is based on RDFS, SHACL Core, and QUDT. The new RDF exporter (turtle format) is accessed via:
ioWriteRdf() axon function
xeto::XetoIO.writeRdf in Fantom
export-rdf sub-command in the Xeto CLI
The legacy RDF format defined by Haystack 4 is officially deprecated and will be removed soon. This includes deprecation of the ioWriteTurtle and ioWriteJsonLd. I do not believe anybody is using these funcs, but if you are please let us know.
See RDF chapter for the current specification.
Xeto Packaging
This build changes some of the rules for how xeto packaging works using new lib meta tags for include and publish. We are also introducing a maturity flag for alpha, beta, and stable.
See the docs
Namespace | Install
The Namespace app has a new "Install" view. This view is similar to the Host|Install view which lets you install new pods from StackHub. But this view installs from xeto.dev and other remote Xeto repos.
Model App
We are introducing a new app called "Model" as the application for all Xeto based tools. This build includes three new views:
Composer: a xeto based builder
Point Mapper: tool to use Xeto equip templates to quickly bind points to connectors
Fit: check database entities against other specs and rule bindings
To use these new tools you will need to start adding the spec tag to your recs according to the Haystack 5.0 ontology.
Jeto and JSON
With the addition of Jeto we now have three different flavors of JSON:
v3 legacy format where scalars were colon prefixed:
"d:2026-06-15"
v4 hayson where scalars use kind discriminator:
{"_kind":"date", "val":"2026-06-15"}
v5 jeto where kind is inferred from the containing spec:
"2026-06-15"
{"val":"2026-06-15","spec":"sys::Date"}  // when not typed by container
To make the Axon APIs clear we have made the following changes:
The ioReadJson() and ioWriteJson() functions are fully backward compatible, but the v3 option is deprecated. Moving forward only use these for generic JSON.
Added ioReadHayson() and ioWriteHayson() - prefer these to the generic JSON functions now if working with Hayson JSON format
Added ioReadJeto() and ioWriteJeto() for the Jeto JSON format
JSON v3
The legacy v3 format is now deprecated. It will be removed in a future build. Please tell us if you are still using it so we can gauge impact.
There is no longer a global setting for setting the I/O functions or HTTP API to use JSON v3 via the backdoor settings tag "jsonVersion" (as discussed in the 3.0.28 build notes). There are no settings for hx.io anymore either (it's a plain lib, not an extension). And the HTTP API will now interpret the mime type "application/json" as always Hayson or Jeto based on the version. You can still use the v3 JSON with either of these explicit mime types:
application/json;version=3
application/vnd.haystack+json;version=3
And the I/O functions still accept the explicit "v3" option:
ioReadJson(file, {v3})
Ext Web Routing
ExtWeb route names: the route name for an extension's web endpoint is now its full dotted lib name; only libs under the Haxall reserved "hx." prefix are simplified to the last name in their dotted path (so "hx.shell" still routes as "shell", but "acme.foo" now routes as "acme.foo" instead of "foo"). Additionally only sys extensions may override ExtWeb.routeName; project extension overrides are not registered, and duplicate routes are now an error with first registration winning. This guarantees third party extensions cannot collide with built-in routes. Migration note: any third party extension with a web module changes its URL from /ext/{proj}/{lastName} to /ext/{proj}/{fullLibName}.
Folio and Trash
The Folio database in Haxall underwent some significant refactoring to push all read/commit security checks into the Folio base class. While these changes are primarily under-the-hood, there is one public-facing change that impacts reading recs from the trash. In order to keep reads performant for normal reads, we removed the {trash} option from the readAll() func and added new func readTrash() for reading recs from the trash.
Boot Libs
Previous 4.0 releases required adding the ph lib to your system or project level extensions. With the addition of ph.api for HTTP v5, we just decided to make ph and ph.api boot level libs enabled in every SkySpark system. Note however that Haxall does not enable ph (nor ph.api) by default.
Modbus
The Modbus connector has a new way to define points. Instead of a register map, modbusCur and modbusWrite can now name a point in a Xeto spec, and the connector reads the register details from that point's ModbusAddr (address, encoding, bit index, byte order and scale). Register maps are still supported. See the modbus docs for more details on how to use the new Xeto spec configuration.
There were also a few notable bug fixes for the connector:
Several fixes for modbusBlockGap and modbusBlockMax handling
More robust parsing of scaling expressions
Better connection handling for TCP and RTU-over-TCP
Migration
You should run migration if you have rule tuning records. The migration ensures that ruleTuning recs have the hx.rule::RuleTuning spec which is required for the rule engine to find tuning recs.
Cluster Compatibility
The 4.0.7 build is fully backward compatible over the cluster with nodes running 3.1 (down to 3.0.24 released in Mar 2020). With one exception: you cannot use live mode in a replica from a 3.1 node. If you have replica projects from 3.1 projects into a 4.0 server, then you must set your replica mode to passive.
ChangeLog
Build 4.0.7 (23 Oct 2026)
Woolly support for custom providers
Woolly new background agent engine
Woolly support for plan mode
Woolly support for inline views
Woolly new routine observable framework
New Namespace | Install view to install/update from xeto.dev
New Model | Composer view
New Model | Point Mapper view
New Model | Fit view
Xeto new validation engine
Xeto sugar specs
Xeto CLI new publish command
Xeto new packaging rules via include and publish tags
Xeto LibFiles API modified to return LibFile
Xeto mixin support for globals
Xeto RDF support
Removal of old fit/fitsExplain engine
Jeto - new Xeto flavored JSON
New v5 HTTP API with Swagger/OpenAPI support
Haystack client support for OAuth
Official deprecation of the legacy v3 JSON format
Rename JsonWriter/JsonReader to HaysonReader/HaysonWriter
New ioReadJeto, ioWriteJeto, ioWriteRdf
Deprecation of ioReadJson/ioWriteJson in favor of ioReadHayson/ioWriteHayson
Deprecation of ioWriteTurtle and ioWriteJsonLd
Redesign Filetype to be standalone with hardcoded registry (no use of defs)
Add Xeto, Jeto, RDF as new options to Shell and Export command
Remove legacy RDF (turtle + json-ld) from Filetype (removes them from skyspark UI)
Remove global support for jsonVersion 3 in hx.api settings (specify version via mime)
Tighten up extension web routeName rules
New Xeto sugar libs: ph.equips.x, ph.points.x, ph.elec.x
Remove DefsNamespace filetype and filetypes methods (still a defs feature)
Remove WebOpUtil
New xeto gen-fan tool for stubbing Fantom from Xeto
New hisWrite opt to skip onHisWrite callback
Enhance sqlInsert to perform executeBatch
Add migration for ruleTuning recs to add spec, and fix Tuning | New to add spec
Fix his filter func closures to correctly capture and update outer scopes
New readTrash() func - all other folio reads ignore the trash.
All folio read/commit security checks now enforced in Folio base class
All FolioMgrs enforce read/commit security at mixin layer instead of implementations
Remove per spark access filtering checks
User.email is now checked instead of non-nullable, new hasEmail method
Unit db fixes for specific enthalpy units from haystack forum #1196
New pi lib and pod for common presentation info like icon, color, text
Modbus connector support for frame delays
Modbus connector xeto support for ModbusAddr
Non-standard ConnExt.modelName overrides must use connFeatures name now
Demogen now generates central plants and water loops
New funcs: toTagNames
Remove sys.template prototype
Arcbeam enhancements and hardening
The ioHttp func improves cookie support
The companionPrint func now supports list of specs to generate whole funcs.xeto file
Project import improved support for large projects
Move ph and ph.api to the system boot
Fix for inet TLS host verification
