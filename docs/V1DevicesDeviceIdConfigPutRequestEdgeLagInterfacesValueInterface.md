# V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_status** | **bool** |  | [optional] 
**alias** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ipv4** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw.md) |  | [optional] 
**ipv6** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw.md) |  | [optional] 
**lacp** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterfaceLacpConfig**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterfaceLacpConfig.md) |  | [optional] 
**lag_members** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceLagMembersValue]**](V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceLagMembersValue.md) |  | [optional] 
**minimum_members** | **int** |  | [optional] 
**mtu** | **int** |  | [optional] 
**segment** | **str** |  | [optional] 
**subinterfaces** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceSubinterfacesValue]**](V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceSubinterfacesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface import V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterface

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterface from a JSON string
v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_instance = V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterface.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterface.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_dict = v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterface from a dict
v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_from_dict = V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterface.from_dict(v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


