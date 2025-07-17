# V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceSubinterfacesValueInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_status** | **bool** |  | [optional] 
**alias** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ipv4** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw.md) |  | [optional] 
**ipv6** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw.md) |  | [optional] 
**segment** | **str** |  | [optional] 
**vlan** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_subinterfaces_value_interface import V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceSubinterfacesValueInterface

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceSubinterfacesValueInterface from a JSON string
v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_subinterfaces_value_interface_instance = V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceSubinterfacesValueInterface.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceSubinterfacesValueInterface.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_subinterfaces_value_interface_dict = v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_subinterfaces_value_interface_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceSubinterfacesValueInterface from a dict
v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_subinterfaces_value_interface_from_dict = V1DevicesDeviceIdConfigPutRequestEdgeLagInterfacesValueInterfaceSubinterfacesValueInterface.from_dict(v1_devices_device_id_config_put_request_edge_lag_interfaces_value_interface_subinterfaces_value_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


