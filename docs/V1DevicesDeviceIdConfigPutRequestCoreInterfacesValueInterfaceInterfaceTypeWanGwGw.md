# V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue**](V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.md) |  | [optional] 
**dhcp** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGwDhcp**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGwDhcp.md) |  | [optional] 
**vrrp** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGwVrrp**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGwVrrp.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_interface_type_wan_gw_gw import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw from a JSON string
v1_devices_device_id_config_put_request_core_interfaces_value_interface_interface_type_wan_gw_gw_instance = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_interface_type_wan_gw_gw_dict = v1_devices_device_id_config_put_request_core_interfaces_value_interface_interface_type_wan_gw_gw_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw from a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_interface_type_wan_gw_gw_from_dict = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceTypeWanGwGw.from_dict(v1_devices_device_id_config_put_request_core_interfaces_value_interface_interface_type_wan_gw_gw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


