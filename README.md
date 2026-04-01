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
| [API reference (overview)](#api-reference) | Core classes and common endpoints |
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

Complete login in the Chromium window that opens (or paste a token when prompted). Then **load the token into your shell** (the CLI cannot set parent-shell variables by itself):

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
graphiant rest GET /v1/edges/summary
```

### `graphiant login`

| Command / option | What it does |
|------------------|--------------|
| `graphiant login` | Opens Chromium (Playwright). Observes **`/v1/…`**, **`/v2/…`**, and **`…/auth/refresh`** traffic and captures **`Authorization: Bearer …`** (and refresh JSON when applicable). After first real token, loads portal **`/`** and reloads once. |
| `--portal-url <url>` | Portal base URL for this run (default: config or `https://portal.graphiant.com/`). |
| `-t`, `--timeout <sec>` | Wait for capture (default **90**). Then prompt to paste. **`Ctrl+C`** skips to paste. |
**After (25.11.1+):**
| `--no-browser` | Print portal URL only; paste when prompted. |
| `--profile <name>` | Store token under named profile (default **`default`**). |
| `--export` / `--no-export` | After success, also print **`export GRAPHIANT_ACCESS_TOKEN=…`** to **stdout** (default: **on**). `env.sh` is always written. |
| `-v`, `--verbose` | Debug logging on stderr. Or **`GRAPHIANT_LOG=debug`** / **`info`** / **`warning`**. |
| `graphiant login env-export` | Print one **`export …`** line to stdout (no browser). Use: `eval "$(graphiant login env-export)"`. |

**Paste / DevTools:** If auto-capture fails, copy the **full** **`Authorization`** header from Network (including the word **`Bearer`**). The CLI does not read DevTools; it only listens inside its own Chromium session.

**Why `GRAPHIANT_ACCESS_TOKEN` is empty after login:** The `graphiant` process is a **child** of your shell and **cannot** modify the parent’s environment. The token is saved under **`~/.graphiant/`** and in **`env.sh`**. Run **`source ~/.graphiant/env.sh`** (or **`eval "$(graphiant login env-export)"`**) in the terminal where you need the variable. New IDE terminals don’t inherit another tab’s `source` unless you reload it there too.

### `graphiant configure`

| Command | Purpose |
|---------|---------|
| `graphiant configure set-host <url>` | Default API base URL (e.g. `https://api.graphiant.com`). |
| `graphiant configure set-portal-url <url>` | Default portal URL for future logins. |
| `graphiant configure show` | Show host, portal, profile, token presence. |

### Call the API from the terminal

Exact method names match **`DefaultApi`** in the SDK — see [DefaultApi.md](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/docs/DefaultApi.md) or list locally:

```bash
graphiant api list --prefix v1_auth_
graphiant invoke v1_auth_get
graphiant api invoke v1_edges_summary_get
graphiant invoke v1_edges_summary_get --kwargs '{"enterprise_id": 123}'
```

Raw HTTP (path under configured API host):

```bash
graphiant rest GET /v1/edges/summary
graphiant rest POST /v1/resource --body '{"key": "value"}' --query 'a=b'
```

| Command | Purpose |
|---------|---------|
| `graphiant whoami` | **`GET /v1/auth`** with current token. |
| `graphiant logout` | Clear stored profile (see **`--profile`**). |
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
| `main.py` | Typer app: `login`, `configure`, `api`, `rest`, `whoami`, … |
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

- Python 3.10+ (3.12+ recommended)
- Git
- OpenAPI Generator (for code generation)

### CI/CD Workflows

This repository uses GitHub Actions for continuous integration and deployment:

- **Linting** ([lint.yml](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/.github/workflows/lint.yml)): Runs Flake8 and MyPy type checking on pull requests and pushes
- **Testing** ([test.yml](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/.github/workflows/test.yml)): Runs pytest with coverage across Python 3.10, 3.11, 3.12, and 3.13
- **Building** ([build.yml](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/.github/workflows/build.yml)): Builds wheel and source distributions
- **Releasing** ([release.yml](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/.github/workflows/release.yml)): Publishes to PyPI (manual trigger, admin-only)

See [.github/workflows/README.md](https://github.com/Graphiant-Inc/graphiant-sdk-python/blob/main/.github/workflows/README.md) for detailed workflow documentation.

### Building from Source

```bash
# Clone repository
git clone git@github.com:Graphiant-Inc/graphiant-sdk-python.git
cd graphiant-sdk-python

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Build distribution
python setup.py sdist bdist_wheel

# Install locally
pip install dist/*.tar.gz
```

### Code Generation

To regenerate the SDK from the latest API specification:

```bash
# Install OpenAPI Generator
brew install openapi-generator  # macOS
# or download from: https://github.com/OpenAPITools/openapi-generator

# Generate SDK
openapi-generator generate \
    -i graphiant_api_docs_v26.3.1.json \
    -g python \
    --git-user-id Graphiant-Inc \
    --git-repo-id graphiant-sdk-python \
    --package-name graphiant_sdk \
    --additional-properties=packageVersion=26.3.2
```

> **Note:** Download the latest API bundle from the Graphiant portal under **Support Hub** → **Developer Tools**. Set **`packageVersion`** to the SDK release you are publishing (this branch: **26.3.2**). The **`-i`** filename reflects the API doc bundle version (here `graphiant_api_docs_v26.3.1.json`) and may stay the same across patch releases when the spec is unchanged.

### Testing

```bash
# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=graphiant_sdk --cov-report=html
```

## 📖 API Reference

### Core Classes

- **`Configuration`**: Client configuration with authentication
- **`ApiClient`**: HTTP client for API requests
- **`DefaultApi`**: Main API interface with all endpoints

### Key Models

- **`V1AuthLoginPostRequest`**: Authentication request
- **`V1AuthLoginPostResponse`**: Authentication response
- **`V1EdgesSummaryGetResponse`**: Device summary response
- **`V1DevicesDeviceIdConfigPutRequest`**: Device configuration request
- **`V1DevicesDeviceIdConfigPutResponse`**: Device configuration response
- **`V1GlobalSummaryPostResponse`**: Global summary response (uses `ManaV2GlobalObjectSummary` for inner items)

### Common Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/auth/login` | POST | Authenticate and get bearer token |
| `/v1/edges/summary` | GET | Get all device summaries |
| `/v1/devices/{device_id}` | GET | Get device details |
| `/v1/devices/{device_id}/config` | PUT | Update device configuration |
| `/v1/circuits` | GET | List circuits |
| `/v1/alarms` | GET | Get system alarms |

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
3. Make your changes and ensure they pass local tests:
   ```bash
   # Run linting
   flake8 graphiant_sdk/
   mypy graphiant_sdk/
   
   # Run tests
   pytest --cov=graphiant_sdk
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
