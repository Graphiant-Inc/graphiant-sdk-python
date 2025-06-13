# V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGwVrrpGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_mode** | **bool** |  | [optional] 
**allow_inter_operability** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**preempt** | **bool** |  | [optional] 
**priority** | **int** |  | [optional] 
**tracked_interfaces** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroupTrackedInterfacesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroupTrackedInterfacesInner.md) |  | [optional] 
**virtual_ip** | **str** |  | [optional] 
**virtual_router_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGwVrrpGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGwVrrpGroup from a JSON string
v1_devices_device_id_config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group_instance = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGwVrrpGroup.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGwVrrpGroup.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group_dict = v1_devices_device_id_config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGwVrrpGroup from a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group_from_dict = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGwVrrpGroup.from_dict(v1_devices_device_id_config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


