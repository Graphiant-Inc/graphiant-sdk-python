# V1DevicesDeviceIdInterfacesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interfaces** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner.md) |  | [optional] 
**page_info** | [**V1NatEntriesDeviceIdGet200ResponsePageInfo**](V1NatEntriesDeviceIdGet200ResponsePageInfo.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_interfaces_get200_response import V1DevicesDeviceIdInterfacesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdInterfacesGet200Response from a JSON string
v1_devices_device_id_interfaces_get200_response_instance = V1DevicesDeviceIdInterfacesGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdInterfacesGet200Response.to_json())

# convert the object into a dict
v1_devices_device_id_interfaces_get200_response_dict = v1_devices_device_id_interfaces_get200_response_instance.to_dict()
# create an instance of V1DevicesDeviceIdInterfacesGet200Response from a dict
v1_devices_device_id_interfaces_get200_response_from_dict = V1DevicesDeviceIdInterfacesGet200Response.from_dict(v1_devices_device_id_interfaces_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


