# V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_neighbor** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor.md) |  | [optional] 
**default** | **object** |  | [optional] 
**gateway_neighbor** | [**V1AccountMfaGet200Response**](V1AccountMfaGet200Response.md) |  | [optional] 
**interface** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterface**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterface.md) |  | [optional] 
**interface_type** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceType**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceType.md) |  | [optional] 
**vlan_id** | **int** |  | [optional] 
**wan** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWan**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWan.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterface

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterface from a JSON string
v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_instance = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterface.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterface.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_dict = v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterface from a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_from_dict = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterface.from_dict(v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


