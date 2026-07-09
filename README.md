# Graphiant SDK Python

[![PyPI version](https://badge.fury.io/py/graphiant-sdk.svg)](https://badge.fury.io/py/graphiant-sdk)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://docs.graphiant.com/docs/graphiant-sdk-python)
[![CI/CD](https://github.com/Graphiant-Inc/graphiant-sdk-python/actions/workflows/test.yml/badge.svg)](https://github.com/Graphiant-Inc/graphiant-sdk-python/actions)

A comprehensive Python SDK for [Graphiant Network-as-a-Service (NaaS)](https://www.graphiant.com), with a built-in **`graphiant`** CLI for portal login and quick API calls.

More product and platform context: [Graphiant Docs](https://docs.graphiant.com).

## Table of contents

| Section | What you’ll find |
|--------|-------------------|
| [Documentation & links](#documentation--links) | Official guides, API reference, PyPI |
| [Features](#features) | SDK + CLI at a glance |
| [Quick start](#quick-start) | Install, sign in, minimal Python example |
| [**Graphiant CLI**](#graphiant-cli) | Full CLI documentation (login, configure, `invoke`, `rest`, env vars) |
| [Advanced usage](#advanced-usage) | Patterns and error handling |
| [Development](#development) | Build, test, code generation |
| [API reference (overview)](#api-reference) | Bundled OpenAPI, model docs, sample endpoints |
| [Security](#security) | Auth and environment variables |
| [Contributing](#contributing) | PR workflow |
| [Support](#support) | Links and contact |

## Documentation & links

| Resource | Link |
|----------|------|
| **SDK guide** | [Graphiant SDK Python](https://docs.graphiant.com/docs/graphiant-sdk-python) |
| **Automation** | [Graphiant Automation](https://docs.graphiant.com/docs/automation) |
| **REST API** | [Graphiant Portal REST API](https://docs.graphiant.com/docs/graphiant-portal-rest-api) |
| **Method index (repo)** | [DefaultApi.md](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/docs/DefaultApi.md) |
| **OpenAPI bundle (this build)** | [`api/graphiant_api_docs_v26.6.0.json`](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/api/graphiant_api_docs_v26.6.0.json) — source for generated paths and models |
| **Model docs (`*.md`)** | [`docs/`](https://github.com/Graphiant-Inc/graphiant-sdk-python/tree/main/docs) (same names as Python classes, e.g. `V1EdgesSummaryGetResponse.md`) |
| **PyPI** | [graphiant-sdk](https://pypi.org/project/graphiant-sdk) |
| **Changelog** | [CHANGELOG.md](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/CHANGELOG.md) |

## Features

- **Full REST coverage** — Generated client for all Graphiant API endpoints.
- **Bearer authentication** — Username/password login in code, or token from the CLI / `GRAPHIANT_ACCESS_TOKEN`.
- **Typed models** — Pydantic models and type hints.
- **`graphiant` CLI** — Portal login (Playwright), saved profiles, `invoke` / `rest` / `whoami`.

## Quick start

### 1. Install

```bash
pip install graphiant-sdk
```

This provides both **`graphiant_sdk`** (Python) and the **`graphiant`** executable.

### 2. Sign in with the CLI

Complete login in the Chromium window that opens (or paste a token when prompted). Then **load the token into your shell**:

```bash
graphiant login
source ~/.graphiant/env.sh
# or, without opening a browser (reads saved credentials):
eval "$(graphiant login env-export)"
```

Confirm: `echo $GRAPHIANT_ACCESS_TOKEN` should show a long token.

See [**Graphiant CLI**](#graphiant-cli) for options (`--timeout`, `--no-capture`, profiles, troubleshooting).

### 3. Basic Python usage

If **`GRAPHIANT_ACCESS_TOKEN`** is set—e.g. after **`graphiant login`** and sourcing `env.sh`—the client uses it and skips username/password login. Otherwise the example falls back to **`POST /v1/auth/login`**.

```python
import os

import graphiant_sdk
from graphiant_sdk.exceptions import (
    ApiException, BadRequestException, UnauthorizedException,
    ForbiddenException, NotFoundException, ServiceException,
)

host = os.environ.get("GRAPHIANT_API_HOST", "https://api.graphiant.com")
access_token = os.environ.get("GRAPHIANT_ACCESS_TOKEN", "").strip()

config = graphiant_sdk.Configuration(host=host)

if access_token:
    # Use only authorization=… on each call — do not also set config.api_key for jwtAuth,
    # or the client may send two Authorization headers and gateways (e.g. Azure) can return 400.
    bearer_token = f"Bearer {access_token}"
else:
    config.username = "your_username"
    config.password = "your_password"

api_client = graphiant_sdk.ApiClient(config)
api = graphiant_sdk.DefaultApi(api_client)

if not access_token:
    auth_request = graphiant_sdk.V1AuthLoginPostRequest(
        username=config.username,
        password=config.password,
    )
    try:
        auth_response = api.v1_auth_login_post(v1_auth_login_post_request=auth_request)
        bearer_token = f"Bearer {auth_response.token}"
        print("Authentication successful")
    except Exception as e:
        print(f"Authentication failed: {e}")
        exit(1)

# Get device summary
try:
    edges_summary = api.v1_edges_summary_get(authorization=bearer_token)
    print(f"Found {len(edges_summary.edges_summary)} devices")

    for device in edges_summary.edges_summary:
        print(f"Device: {device.hostname}, Status: {device.status}")

except Exception as e:
    print(f"Failed to get device summary: {e}")
```

## Graphiant CLI

The **`graphiant`** command ships with `graphiant-sdk`. Use it to log in via the [portal](https://portal.graphiant.com/), store a bearer token, and run quick API checks without writing a full Python script.

- **Version:** `graphiant version` matches **`graphiant_sdk.__version__`**.
- **Help:** `graphiant --help`, `graphiant login --help`, etc.
- **Python usage:** After `source ~/.graphiant/env.sh`, read `GRAPHIANT_ACCESS_TOKEN` in code — see [§3 Basic Python usage](#3-basic-python-usage).

### Shell completion (bash, zsh, fish)

Tab completion is provided by **Typer/Click** but is **not** enabled until you install it once for your shell:

```bash
graphiant --install-completion
```

Then restart the terminal or **`source ~/.zshrc`** / **`~/.bashrc`**. After that, **`graphiant <Tab>`** completes subcommands (e.g. `login`, `rest`, `whoami`) and options.

- Inspect the script without modifying your config: **`graphiant --show-completion`**
- **zsh** must run **`compinit`** (most frameworks do this already).
- The package depends on **`shellingham`** so **`--install-completion`** can detect your shell.

If you prefer to wire **zsh** manually:

```bash
echo 'eval "$(_GRAPHIANT_COMPLETE=zsh_source graphiant)"' >> ~/.zshrc
```

### Typical workflow

```bash
# 1) Log in (browser opens; paste token if prompted)
graphiant login

# 2) Load the token into *this* shell (required — see below)
source ~/.graphiant/env.sh

# 3) Sanity-check session
graphiant whoami

# 4) Call an API (token from env or saved profile)
graphiant invoke v1_edges_summary_get
graphiant rest GET /v1/edges-summary
```

### `graphiant login`

| Command / option | What it does |
|------------------|--------------|
| `graphiant login` | Opens Chromium (Playwright). Observes **`/v1/…`**, **`/v2/…`**, and **`…/auth/refresh`** traffic and captures **`Authorization: Bearer …`** (and refresh JSON when applicable). After first real token, loads portal **`/`** and reloads once. |
| `--portal-url <url>` | Portal base URL for this run (default: config or `https://portal.graphiant.com/`). |
| `-t`, `--timeout <sec>` | Wait for capture (default **90**). Then prompt to paste. **`Ctrl+C`** skips to paste. |
| `--no-capture` | No Playwright; open portal and paste token (full **`Authorization`** value including **`Bearer`**, or raw JWT). |
| `--no-browser` | Print portal URL only; paste when prompted. |
| `--profile <name>` | Store token under named profile (default **`default`**). |
| `--export` / `--no-export` | After success, also print **`export GRAPHIANT_ACCESS_TOKEN=…`** to **stdout** for scripts (default: **off**, so the token is not echoed). `~/.graphiant/env.sh` is always written. |
| `-v`, `--verbose` | Debug logging on stderr. Or **`GRAPHIANT_LOG=debug`** / **`info`** / **`warning`**. |
| `graphiant login env-export` | Print one **`export …`** line to stdout (no browser). Use: `eval "$(graphiant login env-export)"`. |

**Paste / DevTools:** If auto-capture fails, copy the **full** **`Authorization`** header from Network (including the word **`Bearer`**). The CLI does not read DevTools; it only listens inside its own Chromium session.

**If `GRAPHIANT_ACCESS_TOKEN` is empty after login:** The token is saved under **`~/.graphiant/`** in **`env.sh`**. In this terminal, run **`source ~/.graphiant/env.sh`** or **`eval "$(graphiant login env-export)"`**. You can also chain: **`graphiant login && source ~/.graphiant/env.sh`** (add your usual `login` flags before `&&`). New IDE terminals don’t inherit another tab’s `source` unless you reload it there too.

### `graphiant configure`

| Command | Purpose |
|---------|---------|
| `graphiant configure set-host <url>` | Default API base URL (e.g. `https://api.graphiant.com`). |
| `graphiant configure set-portal-url <url>` | Default portal URL for future logins. |
| `graphiant configure show` | Show host, portal, profile, token presence. |

### Call the API from the terminal

Exact method names match **`DefaultApi`** in the SDK — see [DefaultApi.md](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/docs/DefaultApi.md) or list locally:

```bash
graphiant api list --prefix v1_auth_          # table: SDK method, HTTP, path
graphiant apis --plain --prefix v1_auth_     # one SDK method name per line
graphiant invoke v1_auth_get
graphiant api invoke v1_edges_summary_get
graphiant invoke v1_edges_summary_get --kwargs '{"enterprise_id": 123}'
```

**`graphiant invoke`** sends a **single** **`Authorization`** header (the generated client’s **`authorization`** parameter only). It does **not** also apply **`jwtAuth`** from **`Configuration`**, so gateways that reject duplicate auth headers (for example **Azure Application Gateway**) accept the request.

#### Query parameters and filters

- **`graphiant invoke` / `graphiant api invoke`** — Uses the **generated `DefaultApi` method signature**. Anything that is a query string in REST becomes a **keyword argument** on that method, named in **snake_case** (OpenAPI `enterpriseId` → `enterprise_id`). Pass them inside **`--kwargs`** as JSON. You do **not** pass `authorization` manually; the CLI fills **`Bearer <token>`** for you.

  ```bash
  graphiant invoke v1_edges_summary_get --kwargs '{"enterprise_id": 123, "is_requested": true}'
  ```

  Optional arguments can be omitted. For **positional** parameters (rare), use **`--args`** with a JSON array in **parameter order**; the first slot is usually **`authorization`**, which the CLI injects if you skip it by using **`--kwargs`** only.

- **POST / PATCH with a JSON body** — Bodies use the same keyword names as **`DefaultApi`** (often a single **`v1_*_post_request`** argument whose JSON matches the Pydantic model). See **`docs/<ModelName>.md`** for fields.

  ```bash
  graphiant invoke v1_edges_summary_post --kwargs '{"v1_edges_summary_post_request": {"filter": {}}}'
  graphiant invoke v1_global_summary_post --kwargs '{"v1_global_summary_post_request": {"ntpType": true}}'
  graphiant invoke v1_global_content_filters_get
  graphiant invoke v1_global_domain_categories_get
  ```

- **`graphiant rest`** — Query strings are a single **`--query`** / **`-q`** string: **`key=value`** pairs joined with **`&`**. Values are strings (URL-encode special characters in the shell if needed).

  ```bash
  graphiant rest GET /v1/edges-summary --query 'enterpriseId=123&isRequested=true'
  ```

Raw HTTP (path under configured API host):

```bash
graphiant rest GET /v1/edges-summary
graphiant rest GET /v1/devices/1234567890123
graphiant rest POST /v1/global/summary --body '{"ntpType": true}'
```

| Command | Purpose |
|---------|---------|
| `graphiant whoami` | **`GET /v1/auth/user`** and **`GET /v1/users?id=…`**; Rich tables (session, permissions, profile). **`lastActiveAt`** (and similar protobuf timestamps) are shown in **UTC**, labeled **`(UTC)`**. |
| `graphiant logout` | Clear stored profile (see **`--profile`**). Your shell may still export **`GRAPHIANT_ACCESS_TOKEN`** — run **`unset GRAPHIANT_ACCESS_TOKEN`** in that terminal if needed. |
| `graphiant version` | Print CLI and package version. |

### Environment variables & files

| Path / variable | Role |
|-----------------|------|
| `~/.graphiant/config.json` | Default API host and portal URL. |
| `~/.graphiant/credentials.json` | Profiles and stored access tokens. |
| `~/.graphiant/env.sh` | `export GRAPHIANT_ACCESS_TOKEN=…` after each successful login. |
| `GRAPHIANT_CONFIG_DIR` | Override config directory (default **`~/.graphiant`**). |
| `GRAPHIANT_ACCESS_TOKEN` | If set, preferred over disk token for CLI/SDK in that environment. |
| `GRAPHIANT_API_HOST` | Fallback API host when not in config. |
| `GRAPHIANT_PROFILE` | Active profile name (default **`default`**). |
| `GRAPHIANT_LOG` | Login log level: **`debug`**, **`info`**, **`warning`**. |

### Capture behavior & troubleshooting

- Listeners use Playwright’s sync driver; the wait loop uses **`page.wait_for_timeout`** so **`request` / `response`** events are processed (plain **`sleep`** can miss tokens until too late).
- Placeholder values such as **`Bearer null`** on **`/v1/auth/login/pre`** are ignored; the CLI waits for a **real** session token.
- If capture times out: **`graphiant login -t 180`**, complete SSO sooner, **F5** on the portal home, **`graphiant login --no-capture`**, or **`graphiant login -v`** / **`GRAPHIANT_LOG=debug`**.

### CLI dependencies

**Typer**, **Rich**, and **Playwright** (Chromium installed on first use if missing via **`playwright install chromium`**).

### Package layout (`graphiant_cli/`, for contributors)

| Module | Role |
|--------|------|
| `main.py` | Typer app: `login`, `configure`, `api`, `rest`, `whoami` (`GET /v1/auth/user`), … |
| `browser_capture.py` | Playwright session and network capture |
| `token_parsing.py` | Headers, JSON, URL matching, token validation |
| `login_common.py` | Save credentials, user-facing success text, stdout export |
| `portal_login.py` | Portal URL helpers, `open_portal`, test re-exports |
| `config_store.py` | `~/.graphiant/` persistence |
| `cli_logging.py` | Logging (no secrets in logs) |
| `sdk_invoke.py`, `rest_client.py` | SDK invoke and raw REST |

## 🔧 Advanced Usage

### Device Configuration Management

```python
# Verify device portal status before configuration
def verify_device_portal_status(api, bearer_token, device_id):
    """Verify device is ready for configuration updates"""
    edges_summary = api.v1_edges_summary_get(authorization=bearer_token)
    
    for edge in edges_summary.edges_summary:
        if edge.device_id == device_id:
            if edge.portal_status == "Ready" and edge.tt_conn_count == 2:
                return True
            else:
                raise Exception(f"Device {device_id} not ready. "
                              f"Status: {edge.portal_status}, "
                              f"TT Connections: {edge.tt_conn_count}")
    return False

# Configure device interfaces
def configure_device_interfaces(api, bearer_token, device_id):
    """Configure device interfaces with circuits and subinterfaces"""
    
    # Define circuits
    circuits = {
        "c-gigabitethernet5-0-0": {
            "name": "c-gigabitethernet5-0-0",
            "description": "c-gigabitethernet5-0-0",
            "linkUpSpeedMbps": 50,
            "linkDownSpeedMbps": 100,
            "connectionType": "internet_dia",
            "label": "internet_dia_4",
            "qosProfile": "gold25",
            "qosProfileType": "balanced",
            "diaEnabled": False,
            "lastResort": False,
            "patAddresses": {},
            "staticRoutes": {}
        }
    }
    
    # Define interfaces
    interfaces = {
        "GigabitEthernet5/0/0": {
            "interface": {
                "adminStatus": True,
                "maxTransmissionUnit": 1500,
                "circuit": "c-gigabitethernet5-0-0",
                "description": "wan_1",
                "alias": "primary_wan",
                "ipv4": {"dhcp": {"dhcpClient": True}},
                "ipv6": {"dhcp": {"dhcpClient": True}}
            }
        },
        "GigabitEthernet8/0/0": {
            "interface": {
                "subinterfaces": {
                    "18": {
                        "interface": {
                            "lan": "lan-7-test",
                            "vlan": 18,
                            "description": "lan-7",
                            "alias": "non_production",
                            "adminStatus": True,
                            "ipv4": {"address": {"address": "10.2.7.1/24"}},
                            "ipv6": {"address": {"address": "2001:10:2:7::1/64"}}
                        }
                    }
                }
            }
        }
    }
    
    # Create configuration request
    edge_config = graphiant_sdk.ManaV2EdgeDeviceConfig(
        circuits=circuits,
        interfaces=interfaces
    )
    
    config_request = graphiant_sdk.V1DevicesDeviceIdConfigPutRequest(
        edge=edge_config
    )
    
    try:
        # Verify device is ready
        verify_device_portal_status(api, bearer_token, device_id)
        
        # Push configuration
        response = api.v1_devices_device_id_config_put(
            authorization=bearer_token,
            device_id=device_id,
            v1_devices_device_id_config_put_request=config_request
        )
        
        print(f"Configuration job submitted. Job ID: {response.job_id}")
        return response
        
    except ForbiddenException as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Configuration failed: {e}")
```

### Error Handling

```python
def handle_api_errors(func):
    """Decorator for consistent error handling"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequestException as e:
            print(f"Bad Request: {e}")
        except UnauthorizedException as e:
            print(f"Unauthorized: {e}")
        except ForbiddenException as e:
            print(f"Forbidden: {e}")
        except NotFoundException as e:
            print(f"Not Found: {e}")
        except ServiceException as e:
            print(f"Service Error: {e}")
        except ApiException as e:
            print(f"API Error: {e}")
    return wrapper

@handle_api_errors
def get_device_info(api, bearer_token, device_id):
    """Get detailed device information"""
    return api.v1_devices_device_id_get(
        authorization=bearer_token,
        device_id=device_id
    )
```

## 🛠️ Development

### Prerequisites

- Python 3.10+ (3.13 recommended)
- Git
- OpenAPI Generator **>= 7.23.0** (for code generation) — `brew install openapi-generator` or `npm install -g @openapitools/openapi-generator-cli`

### CI/CD Workflows

This repository uses GitHub Actions for continuous integration and deployment:

- **Linting** ([lint.yml](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/.github/workflows/lint.yml)): Runs Flake8 and MyPy type checking on pull requests and pushes
- **Testing** ([test.yml](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/.github/workflows/test.yml)): Runs pytest with coverage across Python 3.10, 3.11, 3.12, and 3.13; coverage uploaded on 3.13
- **Building** ([build.yml](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/.github/workflows/build.yml)): Builds wheel and source distributions
- **Releasing** ([release.yml](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/.github/workflows/release.yml)): Publishes to PyPI (manual trigger, admin-only)

See [.github/workflows/README.md](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/.github/workflows/README.md) for detailed workflow documentation.

### Building from Source

```bash
# Clone repository
git clone git@github.com:Graphiant-Inc/graphiant-sdk-python.git
cd graphiant-sdk-python

# Create virtual environment and install with dev dependencies
python3 -m venv venv && source venv/bin/activate
make install        # pip install -e ".[dev]"

# Run tests
make test           # pytest --cov=graphiant_sdk ...

# Lint (hand-written files only; generated models excluded via .flake8)
make lint

# Type check (generated models excluded via pyproject.toml)
make type-check

# Build wheel and source distribution
make build          # python -m build
```

Or without `make`:

```bash
pip install -e ".[dev]" && pytest --cov=graphiant_sdk
```

### Code Generation

To regenerate the SDK from the latest API specification:

```bash
# Quickest path — uses scripts/generate.sh with api/openapi.yaml
make generate

# Or run the script directly (supports OPENAPI_SPEC override)
OPENAPI_SPEC=api/graphiant_api_docs_v26.6.0.json bash scripts/generate.sh
```

`scripts/generate.sh` wraps the full `openapi-generator-cli generate` invocation (requires OpenAPI Generator **>= 7.23.0**). It auto-detects `openapi-generator` (Homebrew) or `openapi-generator-cli` (npm), reads the current version from `pyproject.toml`, and passes `--git-user-id`/`--git-repo-id` so generated docs never contain `GIT_USER_ID` placeholders.

> **Note:** Download the latest API bundle from the Graphiant portal under **Support Hub** → **Developer Tools** and place it in `api/`. The versioned JSON bundle (`api/graphiant_api_docs_v26.6.0.json`) is the snapshot used for this release; `api/openapi.yaml` is the primary YAML spec. Hand-written files listed in `.openapi-generator-ignore` (`graphiant_cli/`, `graphiant_sdk/api_client.py`, `configuration.py`, etc.) are never overwritten by the generator.

### Testing

```bash
make test           # pytest --cov=graphiant_sdk --cov-report=term --cov-report=xml

# Or directly:
pytest -v tests/
pytest tests/ --cov=graphiant_sdk --cov-report=html
```

## 📖 API Reference

### Source of truth (this release)

Operations and schemas are generated from **`api/graphiant_api_docs_v26.6.0.json`** (in `api/` and bundled in the PyPI wheel). For a newer portal/API, download the current bundle (Support Hub → Developer Tools) and diff paths before relying on URLs here.

| How to explore | Where |
|----------------|-------|
| **Every operation** (method, path, parameters) | [`docs/DefaultApi.md`](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/docs/DefaultApi.md) |
| **CLI: SDK name + HTTP + path** | `graphiant api list` or `graphiant apis --prefix v1_` |
| **Request/response field lists** | [`docs/*.md`](https://github.com/Graphiant-Inc/graphiant-sdk-python/tree/main/docs) — file basename matches the Python model (e.g. `V1EdgesSummaryGetResponse.md`) |
| **Python imports** | `from graphiant_sdk import …` or `graphiant_sdk.models` |

REST query parameters use **camelCase** in URLs (`enterpriseId`). Generated Python kwargs use **snake_case** (`enterprise_id`, `device_id`). Path templates below follow OpenAPI (`{deviceId}`).

### Core classes

- **`Configuration`** — API host, timeouts; do **not** set **`api_key["jwtAuth"]`** when every call passes **`authorization=`** (avoids duplicate **`Authorization`** headers on strict gateways).
- **`ApiClient`** — HTTP client used by **`DefaultApi`**.
- **`DefaultApi`** — one method per operation (e.g. **`v1_edges_summary_get`** → **GET** **`/v1/edges-summary`**).

### Example SDK models (verified in this package)

| Model (`import graphiant_sdk` or `graphiant_sdk.models`) | Typical operation |
|----------------------------------------------------------|-------------------|
| **`V1AuthLoginPostRequest`**, **`V1AuthLoginPostResponse`** | **`POST /v1/auth/login`** |
| **`V1AuthUserGetResponse`** | **`GET /v1/auth/user`** |
| **`V1EdgesSummaryGetResponse`** | **`GET /v1/edges-summary`** |
| **`V1EdgesSummaryPostRequest`** (optional **`filter`**) | **`POST /v1/edges-summary`** |
| **`V1DevicesDeviceIdGetResponse`** | **`GET /v1/devices/{deviceId}`** |
| **`V1DevicesDeviceIdConfigPutRequest`**, **`V1DevicesDeviceIdConfigPutResponse`** | **`PUT /v1/devices/{deviceId}/config`** (job accepted; **no GET** on **`…/config`** in this spec) |
| **`ManaV2EdgeDeviceConfig`** | Nested **`edge`** object inside **`V1DevicesDeviceIdConfigPutRequest`** |
| **`V1GlobalSummaryPostRequest`**, **`V1GlobalSummaryPostResponse`** | **`POST /v1/global/summary`** |
| **`V2ParentalertlistPostRequest`**, **`V2ParentalertlistPostResponse`** | **`POST /v2/parentalertlist`** |

### Sample HTTP endpoints (from `graphiant_api_docs_v26.6.0.json`)

The API surface is large; this table lists **real** paths from the bundled spec. For the full set, use **`graphiant api list`** or **`DefaultApi.md`**.

| Endpoint | Method | Example `DefaultApi` method | Notes |
|----------|--------|----------------------------|-------|
| `/v1/auth/login` | POST | `v1_auth_login_post` | Body: **`V1AuthLoginPostRequest`** |
| `/v1/auth/user` | GET | `v1_auth_user_get` | Session user |
| `/v1/users` | GET | `v1_users_get` | e.g. **`id`** query (see **`graphiant whoami`**) |
| `/v1/edges-summary` | GET | `v1_edges_summary_get` | Queries e.g. **`enterpriseId`**, **`isRequested`** |
| `/v1/edges-summary` | POST | `v1_edges_summary_post` | Body: **`V1EdgesSummaryPostRequest`** |
| `/v1/devices/{deviceId}` | GET | `v1_devices_device_id_get` | Device detail |
| `/v1/devices/{deviceId}/config` | PUT | `v1_devices_device_id_config_put` | Body: **`V1DevicesDeviceIdConfigPutRequest`** |
| `/v1/global/summary` | POST | `v1_global_summary_post` | Body: **`V1GlobalSummaryPostRequest`** |
| `/v1/sites/{siteId}/circuits` | GET | `v1_sites_site_id_circuits_get` | Circuits for a site |
| `/v2/parentalertlist` | POST | `v2_parentalertlist_post` | Body: **`V2ParentalertlistPostRequest`** |

## 🔐 Security

- **Authentication**: Bearer token-based authentication
- **HTTPS**: All API communications use HTTPS
- **Credentials**: Store credentials securely using environment variables
- **Token Management**: Bearer tokens expire and should be refreshed as needed

### Environment Variables

```bash
export GRAPHIANT_HOST="https://api.graphiant.com"
export GRAPHIANT_USERNAME="your_username"
export GRAPHIANT_PASSWORD="your_password"
```

```python
import os

username = os.getenv("GRAPHIANT_USERNAME")
password = os.getenv("GRAPHIANT_PASSWORD")
host = os.getenv("GRAPHIANT_HOST", "https://api.graphiant.com")
```

**Note**: For detailed security policies, vulnerability reporting, and security best practices, see [SECURITY.md](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/SECURITY.md).

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and ensure they pass local checks:
   ```bash
   make test           # run tests with coverage
   make lint           # flake8 on hand-written files (generated excluded via .flake8)
   make type-check     # mypy (generated models excluded via pyproject.toml)
   ```
4. Commit your changes with a clear message (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

**Note**: All pull requests automatically run CI/CD checks (linting, testing across multiple Python versions). Ensure all checks pass before requesting review.

See [CONTRIBUTING.md](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/CONTRIBUTING.md) for detailed contribution guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/LICENSE) file for details.

## 🆘 Support

- **Official Documentation**: [Graphiant SDK Python Guide](https://docs.graphiant.com/docs/graphiant-sdk-python) <-> [Graphiant Automation Docs](https://docs.graphiant.com/docs/automation)
- **API Reference**: [Graphiant SDK Python API Docs](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/docs/DefaultApi.md) <-> [Graphiant Portal REST API Guide](https://docs.graphiant.com/docs/graphiant-portal-rest-api)
- **Changelog**: [CHANGELOG.md](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/CHANGELOG.md) - Detailed release notes and version history
- **Issues**: [GitHub Issues](https://github.com/Graphiant-Inc/graphiant-sdk-python/issues)
- **Email**: support@graphiant.com

## 🔗 Related Projects

- [Graphiant SDK Go](https://github.com/Graphiant-Inc/graphiant-sdk-go)
- [Graphiant Playbooks](https://github.com/Graphiant-Inc/graphiant-playbooks)

---

**Made with ❤️ by the Graphiant Team**
