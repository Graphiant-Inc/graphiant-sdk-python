# V1DevicesDeviceIdConfigPutRequestEdgeDnsDns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudflare** | **object** |  | [optional] 
**dynamic** | [**V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsDynamic**](V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsDynamic.md) |  | [optional] 
**static** | [**V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic**](V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_dns_dns import V1DevicesDeviceIdConfigPutRequestEdgeDnsDns

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeDnsDns from a JSON string
v1_devices_device_id_config_put_request_edge_dns_dns_instance = V1DevicesDeviceIdConfigPutRequestEdgeDnsDns.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestEdgeDnsDns.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_edge_dns_dns_dict = v1_devices_device_id_config_put_request_edge_dns_dns_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeDnsDns from a dict
v1_devices_device_id_config_put_request_edge_dns_dns_from_dict = V1DevicesDeviceIdConfigPutRequestEdgeDnsDns.from_dict(v1_devices_device_id_config_put_request_edge_dns_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


