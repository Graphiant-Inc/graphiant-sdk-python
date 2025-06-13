# V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceWan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gw** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGw.md) |  | [optional] 
**type** | **str** |  | [optional] 
**vrf_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_wan import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceWan

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceWan from a JSON string
v1_devices_device_id_config_put_request_core_interfaces_value_interface_wan_instance = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceWan.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceWan.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_wan_dict = v1_devices_device_id_config_put_request_core_interfaces_value_interface_wan_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceWan from a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_wan_from_dict = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceWan.from_dict(v1_devices_device_id_config_put_request_core_interfaces_value_interface_wan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


