# V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_status** | **bool** |  | [optional] 
**alias** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**duplex** | **str** |  | [optional] 
**ipv4** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw.md) |  | [optional] 
**ipv6** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw.md) |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**mpls_enabled** | **bool** |  | [optional] 
**tcp_mss_v4** | **int** |  | [optional] 
**tcp_mss_v6** | **int** |  | [optional] 
**x_talk_filter** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterface

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterface from a JSON string
v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_instance = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterface.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterface.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_dict = v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterface from a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_from_dict = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterface.from_dict(v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


