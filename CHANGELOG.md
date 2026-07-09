# Graphiant SDK Python Changelog

All notable changes to the Graphiant SDK Python package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [26.6.0] - 2026-07-08

### Added
- **API spec:** `graphiant_api_docs_v26.6.0.json`
- **Public VIF (PVIF) gateway:** **`GET`/`POST /v1/pvif`**, **`GET`/`PUT`/`DELETE /v1/pvif/{id}`**, **`GET /v1/pvif/{id}/details`**, **`GET /v1/pvif/summary`**; models **`V1Pvif*`** and **`ManaV2PublicVifGateway*`** (centralized/decentralized NAT, consumer LAN devices, NAT prefix strategy, write request)
- **Assurance AI adoption:** **`POST /v2/assurance/ai-adoption-summary`**, **`POST /v2/assurance/create-ai-adoption-approve-entry`**, **`POST /v2/assurance/read-ai-adoption-approve-entries`**, **`POST /v2/assurance/update-ai-adoption-approve-entry`**, **`POST /v2/assurance/delete-ai-adoption-approve-entry`**, **`POST /v2/assurance/get-app-names`**; models **`AssuranceApprovedAppEntry`**, **`AssuranceApprovedAppEntryRequest`**, **`AssuranceKpiMetric`**, **`AssuranceTopLevelKpi`**, **`AssuranceUserDefinition`**, **`AssuranceWhatWidget`**, **`AssuranceWhenWidget`**, **`AssuranceWhereWidget`**, and related **`V2AssuranceAiAdoption*`** / **`V2AssuranceGetAppNames*`** types
- **LAN segment public interfaces:** **`GET /v1/lan-segments/interfaces/public`** with **`V1LanSegmentsInterfacesPublicGetResponse`**, **`ManaV2LanSegmentPublicInterfaceEntry`**, **`ManaV2LanSegmentPublicInterfacesLists`**
- **Region gateways:** **`GET /v1/regions/{regionId}/gateways`** with **`V1RegionsRegionIdGatewaysGetResponse`**, **`ManaV2IPsecGatewayPeersConfig`**, **`ManaV2IPsecGatewayRemotePeer`**
- **ZTAgent agents:** **`GET /v1/ztagent/agents`** with **`V1ZtagentAgentsGetResponse`** and **`ConcealAgent`**
- **Mana:** **`ManaV2ZeroTrustConsumptionSummary`**

### Changed
- **Version:** Package **26.6.0**; OpenAPI bundle **`graphiant_api_docs_v26.6.0.json`** (replaces **26.5.0** bundle in-repo).
- **Schemas / docs (updated):** **`AssuranceAppNameRecord`**, **`ManaV2GuestConsumerSiteToSiteVpnConfig`**, **`ManaV2SiteDeviceSummary`**, **`UpgradeRollout`**, **`V1EnterpriseAllocationGetResponse`**, **`V1GatewaysReferenceConsumerGetResponse`**, **`DefaultApi`**, README, and generated **`docs/`** model pages.
- **SDK (generated):** Refreshed **`default_api`**, model exports, and **`docs/`** to match the **26.6.0** spec.

### Removed
- **API spec:** removed **`graphiant_api_docs_v26.5.0.json`** (superseded by **26.6.0** bundle).

## [26.5.0] - 2026-06-10

### Added
- **API spec:** `graphiant_api_docs_v26.5.0.json`
- **Extranet public VIF:** **`GET`/`POST /v1/extranet-public-vif`**, **`POST /v1/extranet-public-vif/check`**, **`GET`/`PUT`/`DELETE /v1/extranet-public-vif/{id}`**; models **`V1ExtranetPublicVif*`** and **`ManaV2PublicVif*`** (consumer/producer policy, fixed/dynamic VIF, device and summary types)
- **MSP billing:** **`GET /v1/msp/managed-enterprise-contract-info`** with **`V1MspManagedEnterpriseContractInfoGetResponse`** and **`ManaV2ManagedEnterpriseContractInfo`**
- **Site map:** **`GET /v1/sites/map/details`** with **`V1SitesMapDetailsGetResponse`**, **`ManaV2LanSegmentSitesMap`**, **`ManaV2SiteInformation`**, **`ManaV2SiteDeviceSummary`**, **`ManaV2SiteLanSegmentDeviceBuckets`**
- **Billing (common):** **`CommonBillingContract`**, **`CommonBillingTimePeriod`**

### Changed
- **Version:** Package **26.5.0**; OpenAPI bundle **`graphiant_api_docs_v26.5.0.json`** (replaces **26.4.0** bundle in-repo).
- **Schemas / docs (updated):** **`AssuranceClientSession`**, **`AssuranceSite`**, **`SearchEdgeSummary`**, **`ManaV2ApplicationProfile`**, enterprise contract/patch/put request types, assurance topology request types, **`DefaultApi`**, README and generated **`docs/`** model pages.
- **SDK (generated):** Refreshed **`default_api`**, **`api_client`**, **`configuration`**, and model exports to match the **26.5.0** spec (including OpenAPI **example** metadata on many generated Pydantic fields).

### Removed
- **API spec:** removed **`graphiant_api_docs_v26.4.0.json`** (superseded by **26.5.0** bundle).

### Security
- **urllib3:** lock **2.7.0** in **Poetry** to pick up fixes for decompression-bomb resource-exhaustion issues in parts of the streaming API and sensitive-header forwarding across origins in proxied low-level redirects. The declared runtime range already allows the patched release.

## [26.4.0] - 2026-04-30

### Added
- **API spec:** `graphiant_api_docs_v26.4.0.json`
- **Global content filters:** CRUD-style operations under **`/v1/global/content-filters`** and **`/v1/global/content-filters/{globalContentFilterId}`**; models including **`V1GlobalContentFilters*`** row/rule/site/lan entry types and **`ManaV2GlobalContentFilterConfig`**, **`ManaV2GlobalContentFilterRule`**
- **Domain categories:** **`GET /v1/global/domain-categories`** with **`V1GlobalDomainCategoriesGetResponse`** and **`ManaV2DomainCategory`**
- **Software upgrade rollouts:** **`GET`/`POST`/`PUT /v1/software/rollouts`**, **`GET`/`DELETE /v1/software/rollouts/{id}`**, **`POST /v1/software/rollouts/schedule`**; models **`UpgradeRollout`**, **`UpgradeRolloutConfig`**, **`UpgradeRolloutDevice`**, **`UpgradeRecurringSchedule`**, **`UpgradeMonthlyRecurrence`**, **`UpgradeWeeklyRecurrence`**, **`UpgradeYearlyRecurrence`**, plus related **`V1SoftwareRollouts*`** request/response types
- **ZTAgent bindings:** **`GET`/`PUT /v1/ztagent/bindings`** with **`V1ZtagentBindingsGetResponse`** / **`V1ZtagentBindingsPutRequest`**
- **MACsec monitoring:** **`GET /v2/monitoring/macsec/{deviceId}/status`** with **`V2MonitoringMacsecDeviceIdStatusGetResponse`** (and nested MACsec status type)
- **Mana:** **`ManaV2RegionCoordinates`**; **`ManaV2Region`** updated in spec

### Changed
- **Version:** Package **26.4.0**; OpenAPI bundle **`graphiant_api_docs_v26.4.0.json`** (replaces **26.3.1** bundle in-repo).
- **Schemas / docs (updated):** **`AlertserviceNotificationBody`**, **`AssuranceClientSession`**, **`AssuranceRegion`**, **`UpgradeUpgradeOccurrence`**, **`UpgradeUpgradeSummary`**, **`V2AssuranceTopologyClientSummariesPostResponseSummary`**, **`DefaultApi`**, README and generated **`docs/`** model pages.
- **SDK (generated):** Refreshed **`default_api`**, **`api_client`**, **`configuration`**, and model exports to match the **26.4.0** spec.

### Removed
- **API spec:** removed **`graphiant_api_docs_v26.3.1.json`** (superseded by **26.4.0** bundle).

### Security
- **pytest** (dev / CI): require **≥ 9.0.3** for **CVE-2025-71176** (insecure **`/tmp/pytest-of-{user}`** handling on UNIX; local users could cause **denial of service** or possibly **gain privileges**). See [pytest PR #14279](https://github.com/pytest-dev/pytest/pull/14279).

## [26.3.3] - 2026-04-10

### Changed
- **Version:** Package **26.3.3** (same bundled OpenAPI input file as **26.3.2**: `graphiant_api_docs_v26.3.1.json`).
- **CLI:** **`strip_bearer_prefix`** in **`rest_client`** avoids **`Authorization: Bearer Bearer …`** when **`GRAPHIANT_ACCESS_TOKEN`** or stored credentials already include the **`Bearer `** prefix; **`graphiant rest`** and **`graphiant invoke`** use it.
- **CLI (shell completion):** Declare **`add_completion=True`**, call **`app(prog_name="graphiant")`** so Click/Typer completion uses **`_GRAPHIANT_COMPLETE`**. Add runtime dependency **`shellingham`** (Typer uses it for **`graphiant --install-completion`**). Document setup in the README.
- **CLI:** On **HTTP 403** with API JSON **`displayError`: `Token Expired`** (e.g. from **`graphiant rest`** or **`graphiant whoami`**), print a short **re-login** hint instead of only the raw body; **`graphiant invoke`** treats matching **`ApiException`** bodies the same way.
- **CLI (`graphiant api list` / `graphiant apis`):** Prints a **Rich table** with **SDK method**, **HTTP verb**, and **path** (parsed from the generated client) next to each operation. Use **`--plain`** / **`-1`** for one method name per line (previous behavior).
- **CLI (`graphiant invoke` / `graphiant api invoke`):** The OpenAPI client no longer sets **`Configuration.api_key["jwtAuth"]`** for CLI invokes. Operations already send **`Authorization`** from the **`authorization`** parameter; combining both produced **two** auth headers (e.g. **`Authorization`** and **`authorization`**), which **Microsoft Azure Application Gateway** rejects with **400 Bad Request**.
- **CLI (`graphiant whoami`):** Calls **`GET /v1/auth/user`** and **`GET /v1/users?id=…`** to resolve **user** display name; **Rich tables** for session, permissions, and profile (no **`/v1/enterprises`** lookup). **`lastActiveAt`** and protobuf **`{seconds,nanos}`** values are formatted as human-readable **UTC** with an explicit **`(UTC)`** label; trailing raw auth **JSON** dump removed.
- **CLI (`graphiant login`):** Default is **`--no-export`** so the bearer token is **not** printed to **stdout** after login (avoids echoing credentials in the terminal). Token is still written to **`~/.graphiant/env.sh`**; use **`graphiant login --export`** or **`graphiant login env-export`** when a shell export line on stdout is required.
- **CLI:** After **`graphiant logout`**, the CLI reminds you to run **`unset GRAPHIANT_ACCESS_TOKEN`** when the shell still exports the old token. README **`graphiant logout`** row updated.
- **Documentation:** README API reference sample endpoints, **`graphiant rest`** / **`invoke`** examples, and related fixes (e.g. **`/v1/edges-summary`** path).

## [26.3.2] - 2026-03-27

### Changed
- **Version:** Package **26.3.2** (same bundled OpenAPI input file as 26.3.1: `graphiant_api_docs_v26.3.1.json`).
- **Python:** Minimum supported version is **3.10** (`requires-python`, `setup.py`, CI, and contributor docs).
- **Dependencies:** Direct **Pygments ≥ 2.20**; dev dependency **filelock ≥ 3.20.3** in Poetry (see `pyproject.toml` / `poetry.lock`).

### Security
- **Pygments** minimum raised to mitigate known ReDoS issues in older releases.
- **filelock** (dev, pulled in by the **tox** / **virtualenv** stack): minimum **≥ 3.20.3** to avoid vulnerable releases affected by a **time-of-check–time-of-use (TOCTOU)** race in **SoftFileLock** that could allow **symlink attacks** during lock file creation (upstream patched releases; this repo uses **Python ≥ 3.10** so **filelock** 3.20.x can be resolved).

### Documentation
- README, CONTRIBUTING, GitHub Actions workflow docs, issue template, and `.travis.yml` updated for Python **3.10+** only (removed **3.9** from test matrices and examples).

## [26.3.1] - 2026-03-26

### Added
- **API spec:** `graphiant_api_docs_v26.3.1.json`
- **Schemas:**
  - `ManaV2BgpDynamicNeighborOperPeer`
  - `ManaV2NullableMaCsecRekeyInterval`
  - `ManaV2NullableMaCsecReplayProtectionWindowSize`
- **API endpoints (added):** none
- **CLI (`graphiant`):** Bundled command-line tool (console script `graphiant` → `graphiant_cli.main:main`):
  - Portal login via Playwright/Chromium; bearer capture from Graphiant **`/v1/`**, **`/v2/`**, and **`…/auth/refresh`** traffic, or paste full **`Authorization: Bearer …`** / raw JWT
  - Profiles and files under **`~/.graphiant/`** (including **`env.sh`** with `GRAPHIANT_ACCESS_TOKEN`)
  - **`graphiant configure`** (API host, portal URL), **`graphiant invoke`** / **`graphiant api list`**, **`graphiant rest`**, **`graphiant whoami`**, **`graphiant logout`**, **`graphiant version`**
  - Optional logging via **`GRAPHIANT_LOG`** / **`graphiant login -v`**
  - Runtime deps: **Typer**, **Rich**, **Playwright** (Chromium installed on first use when needed)

### Changed
- **Documentation:** README rework — table of contents, documentation links table, quick start (**install → CLI sign-in → Python** with `GRAPHIANT_ACCESS_TOKEN`), expanded **Graphiant CLI** section (commands, env vars, capture/troubleshooting), clearer feature list
- **Version:**
  - Updated package version from 26.2.1 to 26.3.1
  - Updated API documentation reference to `graphiant_api_docs_v26.3.1.json`
- **API endpoints (updated):**
  - `DELETE /v1/devices/inventory/serial-num`
  - `DELETE /v2/assurance/deleteclassifiedapplication`
  - `GET /v1/device/routing/ospfv2/statistics`
  - `GET /v1/device/routing/ospfv3/statistics`
  - `GET /v1/devices/inventory`
  - `GET /v1/devices/routing/vrf/protocol-route-count`
  - `GET /v1/devices/{deviceId}/circuits/vrf-associations`
  - `GET /v1/devices/{deviceId}/vrf/protocols`
  - `GET /v1/devices/{deviceId}/vrrp`
  - `GET /v1/diagnostic/speedtest-servers`
  - `GET /v1/edges-hardware/assigned`
  - `GET /v1/edges-summary`
  - `GET /v1/enterprises`
  - `GET /v1/enterprises/managed`
  - `GET /v1/extranets-b2b-peering/consumer/{customerId}/consumer-details`
  - `GET /v1/extranets-b2b-peering/match/service-to-customer/{id}`
  - `GET /v1/extranets-monitoring/lan-segments`
  - `GET /v1/extranets-monitoring/nat-usage`
  - `GET /v1/global/device-status`
  - `GET /v1/global/ipfix/device`
  - `GET /v1/global/ntps/device`
  - `GET /v1/global/ntps/site`
  - `GET /v1/global/site-status`
  - `GET /v1/global/snmps/device`
  - `GET /v1/global/syslogs/device`
  - `GET /v1/software/releases/download`
  - `GET /v1/users/{id}/enterprises`
  - `GET /v1/users/{id}/groups`
  - `GET /v1/users/{id}/groups/enterprises`
  - `GET /v1/users/{id}/groups/root`
  - `GET /v2/monitoring/extranet/edge-status`
  - `GET /v2/monitoring/extranet/service-status`
  - `GET /v2/monitoring/extranet/service-status/details`
  - `GET /v2/monitoring/extranet/site-status`
  - `GET /v2/monitoring/extranet/status-details`
  - `POST /v1/device/routing/rib/route-count`
- **Documentation (updated):**
  - `AlertserviceIntegrationDetails`, `AlertserviceNotificationBody`
  - `AssuranceAppIdRecord`
  - `DefaultApi`
  - `ManaV2BgpNeighbor`, `ManaV2PskConfiguration`, `ManaV2SakConfiguration`
  - `SearchEdgeSummary`
  - `V1DiagnosticSpeedtestReportPutResponse`
  - `V2AssuranceCreateUserReportPostRequest`, `V2AssuranceDownloadUserReportGetResponse`
- **SDK (generated):** refreshed generated API client, configuration, and model bindings to match the 26.3.1 spec.

### Removed
- **API spec:** removed `graphiant_api_docs_v26.2.1.json`
- **API endpoints (removed):** none
- **Documentation:** removed the long README “Migration Guide” (25.10.2 → 25.11.1+) section; upgrade notes remain discoverable via Git history and [DefaultApi.md](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/docs/DefaultApi.md) / model docs as needed

## [26.2.1] - 2026-02-26

### Added
- **Auth:**
  - New endpoint: `POST /v1/users/passwords/expire`
  - New schemas: `V1UsersPasswordsExpirePostRequest`/`PostResponse`
- **Alerting:** new schema `AlertserviceZendeskDetails`
- **IAM:** new schema `IamFailedUser`
- **Device:** new schema `ManaV2NullableGatewayConfig`

### Changed
- **Version:**
  - Updated package version from 26.1.1 to 26.2.1
  - Updated API documentation reference to `graphiant_api_docs_v26.2.1.json`
- **Documentation:** updated SDK generation example to use `graphiant_api_docs_v26.2.1.json` and `packageVersion=26.2.1`
- **API endpoints (updated):**
  - `GET /v1/device/routing/bgp/nbrs/counters`
  - `GET /v1/diagnostic/gnmi-ping`
  - `GET /v1/diagnostic/speedtest-servers`
  - `GET /v1/enterprises/{enterpriseId}/device-status`
  - `GET /v1/extranets-monitoring/lan-segments`
  - `GET /v1/extranets-monitoring/nat-usage`
  - `GET /v1/global/device-status`
  - `GET /v1/global/ipfix/site`
  - `GET /v1/global/site-status`
  - `GET /v1/global/snmps/site`
  - `GET /v1/global/syslogs/site`
  - `GET /v1/software/running/details`
- **Schemas (updated):** `AlertserviceIntegration`, `AlertserviceIntegrationDetails`, `ManaV2Interface`, `ManaV2InterfaceIpConfig`, `ManaV2InterfaceVlan`, `StatsmonV2Node`, `StatsmonV2NodeCircuitInfo`, `V2DeviceDeviceIdTopologyPostRequest`

### Removed
- **API endpoints:**
  - **DELETE**
    - `DELETE /v1/enterprises/self`
    - `DELETE /v1/policy/prefix-sets/{id}`
    - `DELETE /v1/portal/apikeys`
    - `DELETE /v2/assistant/delete-conversation/{conversationId}`
    - `DELETE /v2/assistant/{conversationId}`
  - **GET**
    - `GET //v1/devices/oauth/redirect`
    - `GET /v1/alarm-history`
    - `GET /v1/alarms-events`
    - `GET /v1/alarms-list`
    - `GET /v1/device/routing/bgp/nbr/stats`
    - `GET /v1/device/routing/ospfv2/area/interfaceid`
    - `GET /v1/device/routing/ospfv3/area/interface/nbrid`
    - `GET /v1/device/routing/ospfv3/area/interfaceid`
    - `GET /v1/device/routing/vrf/bgp/graphiant-eiroute-count`
    - `GET /v1/devices/{deviceId}/edges`
    - `GET /v1/devices/{deviceId}/ndcache`
    - `GET /v1/devices/{deviceId}/policy/customapplications`
    - `GET /v1/devices/{deviceId}/versions/compare`
    - `GET /v1/devices/{deviceId}/vrf/bgp/as`
    - `GET /v1/event/device`
    - `GET /v1/event/enterprise`
    - `GET /v1/event/system`
    - `GET /v1/global/prefix-sets/device`
    - `GET /v1/global/prefix-sets/site`
    - `GET /v1/global/routing-policies/device`
    - `GET /v1/global/routing-policies/site`
    - `GET /v1/global/traffic-policies/device`
    - `GET /v1/global/traffic-policies/site`
    - `GET /v1/groups/{id}`
    - `GET /v1/portal/apikeys`
    - `GET /v1/portal/private/details`
    - `GET /v1/portal/private/inventory_details`
    - `GET /v1/software/release/notes`
    - `GET /v1/tt/{ttIdentity}/device-status`
    - `GET /v2/assurance/bucket-app-servers/all`
  - **PATCH**
    - `PATCH /v1/{id}/password/recover`
  - **POST**
    - `POST /v1/b2b-extranet-monitoring/filter`
    - `POST /v1/bwtracker/region/cloud/chart`
    - `POST /v1/bwtracker/region/cloud/csv`
    - `POST /v1/bwtracker/region/cloud/summary`
    - `POST /v1/devices/inventory/serial-num`
    - `POST /v1/diagnostic/ping-pause-resume`
    - `POST /v1/event/system/ack`
    - `POST /v1/extranet/sites-usage`
    - `POST /v1/global/config/site`
    - `POST /v1/monitoring/circuits/bandwidth`
    - `POST /v1/monitoring/circuits/incidents`
    - `POST /v1/monitoring/circuits/summary`
    - `POST /v1/monitoring/circuits/utilization`
    - `POST /v1/monitoring/circuits/visualization`
    - `POST /v1/policy/prefix-sets`
    - `POST /v1/portal/apikeys`
    - `POST /v1/portal/private`
    - `POST /v1/portal/private/register`
    - `POST /v1/portal/private/sync`
    - `POST /v2/assurance/endpoint-intel`
    - `POST /v2/assurance/flow-summary`
    - `POST /v2/assurance/topology-flows`
    - `POST /v2/assurance/version`
    - `POST /v2/monitoring/ospf`
    - `POST /v2/monitoring/queue`
    - `POST /v2/monitoring/system/generic`
    - `POST /v2/site/{siteId}/detail`
    - `POST /v2/version`
  - **PUT**
    - `PUT /v1/alarm-mute/{alarmId}`
    - `PUT /v1/policy/prefix-sets/{id}`
- **Schemas:** removed 136 component schemas (not exhaustively listed; includes alarms/assurance/events/statsmon/portal and related request/response models)

## [26.1.1] - 2026-02-03

### Added
- **Assurance – DNS proxy:**
  - New endpoints: create, read list, update, and delete DNS proxy entries
  - New schemas: `AssuranceDnsProxyEntry`, `V2AssuranceCreateDnsproxyEntryPostRequest`/`PostResponse`, `V2AssuranceUpdateDnsproxyEntryPostRequest`/`PostResponse`, `V2AssuranceReadDnsproxyListGetResponse`, `V2AssuranceDeleteDnsproxyEntryDeleteResponse`
- **B2B extranet peering:**
  - New endpoint: `PUT /v1/extranets-b2b-peering/consumer/{id}/prefixes` – update consumer prefixes
  - New endpoint: `PUT /v1/extranets-b2b-peering/match/service-to-customer/service-status` – set match service-to-customer status (e.g. pause)
  - New schemas: `V1ExtranetsB2bPeeringConsumerIdPrefixesPutRequest`/`PutResponse`, `V1ExtranetsB2bPeeringMatchServiceToCustomerServiceStatusPutRequest`/`PutResponse`
- **Device & interface – MACsec:**
  - New `macsec` support on interfaces and LAG interface config via `ManaV2InterfaceMaCsec`, `ManaV2NullableMaCsecConfiguration`, `ManaV2MaCsecConfiguration`
  - New schemas: `ManaV2PskConfiguration`, `ManaV2SakConfiguration`, `ManaV2NullablePskConfiguration`, `ManaV2NullableSakConfiguration`
- **Device – SLA conformance:**
  - New `slaConformance` on device and edge device config via `ManaV2SlaConformance`, `ManaV2NullableSlaConformance`
- **Auth – MFA:**
  - Login response extended for MFA: `email`, `mfaType`, `stateToken`, `status` on `V1AuthLoginPostResponse`

### Changed
- **Version:**
  - Updated package version from 25.12.1 to 26.1.1
  - Updated API documentation reference to `graphiant_api_docs_v26.1.1.json`
- **IAM Customer:** added `description`, `marketplaceId`
- **B2B extranet match details:** `ManaV2B2bExtranetServiceCustomerMatchDetails` extended with `consumerId`, `oldConsumerPrefixes`, `oldServicePrefixes`; `ManaV2B2BExtranetServiceCustomerMatchDetailsProducerPrefix` schema defined in components

## [25.12.1] - 2025-12-17

### Added
- **CI/CD:**
  - Added Git tag and GitHub release creation to release workflow
  - Added `create_tag` input option to release workflow (default: true)
  - Enhanced PyPI upload error handling with verbose mode and detailed diagnostics
  - Added token validation and length checking in release workflow
  - Release workflow now gracefully handles existing tags and releases (no failure on re-run)
- **Testing:**
  - Added support for Graphiant API credentials in test workflow via GitHub secrets/variables
  - Test workflow now reads `GRAPHIANT_HOST`, `GRAPHIANT_USERNAME`, `GRAPHIANT_PASSWORD` from secrets/variables
  - Integration tests (e.g., `test_sanity.py`) will run when credentials are configured
- **Documentation:**
  - Added CHANGELOG.md references in README.md documentation and support sections

### Changed
- **Version:**
  - Updated package version from 25.11.1 to 25.12.1
  - Updated API documentation reference to `graphiant_api_docs_v25.12.1.json`
- **CI/CD:**
  - Updated release workflow permissions to `contents: write` (required for tag/release creation)
  - Added `fetch-depth: 0` to checkout step for git tag operations
  - Improved PyPI upload error messages with troubleshooting guidance
  - Release workflow now uses GitHub API to check for existing releases before creating new ones
  - Tag creation step now skips creation if tag already exists instead of failing

### Fixed
- Fixed import issues for models not exported from main package:
  - `V1GroupsIdMembersPostResponse` - now imported directly from module
  - `V1AuthPutResponse` - now imported directly from module
- Enhanced error handling in release workflow for better debugging
- Fixed release workflow to prevent failures when tags or releases already exist (idempotent behavior)

## [25.11.1] - 2025-11-11

### Added
- **API Specification:**
  - Major API specification optimization and schema reuse
  - Reduced specification file size from 9.8M to 1.5M (~85% reduction)
  - Enhanced API documentation with more comprehensive descriptions

### Changed
- **Breaking Changes:**
  - Response class names no longer include HTTP status codes
    - `Post200Response` → `PostResponse`
    - `Get200Response` → `GetResponse`
    - `Put202Response` → `PutResponse`
    - `Put204Response` → `PutResponse`
    - `Post201Response` → `PostResponse`
  - Inner classes now use reusable schema names across different endpoints
  - Common schemas share the same inner class names for better code reuse
- **Documentation:**
  - Added comprehensive migration guide from 25.10.2 to 25.11.1
  - Updated README with migration instructions and examples
  - Enhanced documentation for finding endpoint request/response models

### Migration Notes
- See [README.md](README.md#-migration-guide-upgrading-from-25102-to-25111) for detailed migration instructions
- Most response classes have been updated; check API documentation for exceptions
- Inner class names have changed - refer to model documentation files for new names

## [25.10.2] - 2025-10-13

### Changed
- Updated API specification to version 25.10.2

## [25.10.1] - 2025-10-08

### Changed
- Updated API specification to version 25.10.1

## [25.9.2] - 2025-09-25

### Changed
- Updated API specification to version 25.9.2

## [25.9.1] - 2025-09-23

### Changed
- Updated API specification to version 25.9.1

## [25.8.1] - 2025-08-22

### Changed
- Updated API specification to version 25.8.1

## [25.7.1] - 2025-07-18

### Changed
- Updated API specification to version 25.7.1

## [25.6.2] - 2025-06-13

### Changed
- Updated API specification to version 25.6.2

## [25.6.1] - 2025-06-02

### Changed
- Updated API specification to version 25.6.1

---

## Release Notes Format

Each release includes:
- **Added**: New features, endpoints, or capabilities
- **Changed**: Changes in existing functionality
- **Deprecated**: Features that will be removed in future versions
- **Removed**: Removed features or endpoints
- **Fixed**: Bug fixes
- **Security**: Security-related changes

For detailed API changes, refer to the API documentation files in the `docs/` directory.
