# V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_ipv4_v2** | [**V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue**](V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.md) |  | [optional] 
**primary_ipv6_v2** | [**V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue**](V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.md) |  | [optional] 
**secondary_ipv4_v2** | [**V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue**](V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.md) |  | [optional] 
**secondary_ipv6_v2** | [**V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue**](V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_dns_dns_static import V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic from a JSON string
v1_devices_device_id_config_put_request_edge_dns_dns_static_instance = V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_edge_dns_dns_static_dict = v1_devices_device_id_config_put_request_edge_dns_dns_static_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic from a dict
v1_devices_device_id_config_put_request_edge_dns_dns_static_from_dict = V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic.from_dict(v1_devices_device_id_config_put_request_edge_dns_dns_static_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


