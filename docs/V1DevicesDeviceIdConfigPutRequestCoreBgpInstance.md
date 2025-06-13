# V1DevicesDeviceIdConfigPutRequestCoreBgpInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_families** | **List[str]** |  | [optional] 
**asn** | **int** |  | [optional] 
**route_server** | **bool** |  | [optional] 
**router_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_bgp_instance import V1DevicesDeviceIdConfigPutRequestCoreBgpInstance

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreBgpInstance from a JSON string
v1_devices_device_id_config_put_request_core_bgp_instance_instance = V1DevicesDeviceIdConfigPutRequestCoreBgpInstance.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreBgpInstance.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_bgp_instance_dict = v1_devices_device_id_config_put_request_core_bgp_instance_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreBgpInstance from a dict
v1_devices_device_id_config_put_request_core_bgp_instance_from_dict = V1DevicesDeviceIdConfigPutRequestCoreBgpInstance.from_dict(v1_devices_device_id_config_put_request_core_bgp_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


