# V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_neighbor** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor.md) |  | [optional] 
**core_to_core_tunnel** | **object** |  | [optional] 
**default** | **object** |  | [optional] 
**gateway_neighbor** | [**V1AccountMfaGet200Response**](V1AccountMfaGet200Response.md) |  | [optional] 
**wan** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceTypeWan**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceTypeWan.md) |  | [optional] 
**wan_management** | **object** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_type import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceType

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceType from a JSON string
v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_type_instance = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceType.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceType.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_type_dict = v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_type_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceType from a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_type_from_dict = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceInterfaceType.from_dict(v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_interface_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


