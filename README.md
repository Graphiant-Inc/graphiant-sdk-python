# Graphiant SDK Python

[![PyPI version](https://badge.fury.io/py/graphiant-sdk.svg)](https://badge.fury.io/py/graphiant-sdk)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://docs.graphiant.com/docs/graphiant-sdk-python)

A comprehensive Python SDK for [Graphiant Network-as-a-Service (NaaS)](https://www.graphiant.com), providing seamless integration with Graphiant's network automation platform.

## 📚 Documentation

- **Official Documentation**: [Graphiant SDK Python Guide](https://docs.graphiant.com/docs/graphiant-sdk-python)
- **API Reference**: [DefaultApi.md](docs/DefaultApi.md)
- **Package**: [PyPI - graphiant-sdk](https://pypi.org/project/graphiant-sdk/)

## ✨ Features

- **Complete API Coverage**: Full access to all Graphiant REST API endpoints
- **Authentication**: Built-in bearer token authentication
- **Device Management**: Comprehensive device configuration and monitoring
- **Network Operations**: Circuit management, interface configuration, and routing
- **Error Handling**: Robust exception handling with detailed error messages
- **Type Safety**: Full type hints and validation using Pydantic models
- **CLI Support**: Command-line interface for quick operations

## 🚀 Quick Start

### Installation

Install the package from PyPI:

```bash
pip install graphiant-sdk
```

### Basic Usage

```python
import graphiant_sdk
from graphiant_sdk.exceptions import (
    ApiException, BadRequestException, UnauthorizedException, 
    ForbiddenException, NotFoundException, ServiceException
)

# Create client configuration
config = graphiant_sdk.Configuration(
    host="https://portal.graphiant.com",
    username="your_username",
    password="your_password"
)

# Initialize API client
api_client = graphiant_sdk.ApiClient(config)
api = graphiant_sdk.DefaultApi(api_client)

# Authenticate and get bearer token
auth_request = graphiant_sdk.V1AuthLoginPostRequest(
    username=config.username,
    password=config.password
)

try:
    auth_response = api.v1_auth_login_post(v1_auth_login_post_request=auth_request)
    bearer_token = f'Bearer {auth_response.token}'
    print(f"Authentication successful")
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
    edge_config = graphiant_sdk.V1DevicesDeviceIdConfigPutRequestEdge(
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

- Python 3.12+
- Git
- OpenAPI Generator (for code generation)

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
    -i graphiant_api_docs_v25.7.1.json \
    -g python \
    --git-user-id Graphiant-Inc \
    --git-repo-id graphiant-sdk-python \
    --package-name graphiant_sdk \
    --additional-properties=packageVersion=25.7.1
```

> **Note**: Latest API documentation can be downloaded from the Graphiant portal under "Support Hub" > "Developer Tools".

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
- **`V1EdgesSummaryGet200Response`**: Device summary response
- **`V1DevicesDeviceIdConfigPutRequest`**: Device configuration request

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
export GRAPHIANT_HOST="https://portal.graphiant.com"
export GRAPHIANT_USERNAME="your_username"
export GRAPHIANT_PASSWORD="your_password"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [Graphiant Docs](https://docs.graphiant.com/)
- **API Reference**: [DefaultApi.md](docs/DefaultApi.md)
- **Issues**: [GitHub Issues](https://github.com/Graphiant-Inc/graphiant-sdk-python/issues)
- **Community**: [Graphiant Community](https://community.graphiant.com/)

## 🔗 Related Projects

- [Graphiant SDK Go](https://github.com/Graphiant-Inc/graphiant-sdk-go)
- [Graphiant Portal REST API](https://docs.graphiant.com/docs/graphiant-portal-rest-api)
- [Graphiant Playbooks](https://github.com/Graphiant-Inc/graphiant-playbooks)

---

**Made with ❤️ by the Graphiant Team**
