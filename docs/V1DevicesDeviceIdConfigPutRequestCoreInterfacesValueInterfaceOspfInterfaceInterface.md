# V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bfd** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborBfd**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborBfd.md) |  | [optional] 
**cost** | **int** |  | [optional] 
**dead_interval_value** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterfaceDeadIntervalValue**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterfaceDeadIntervalValue.md) |  | [optional] 
**dr_priority** | **int** |  | [optional] 
**hello_interval_value** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterfaceHelloIntervalValue**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterfaceHelloIntervalValue.md) |  | [optional] 
**interface_name** | **str** |  | [optional] 
**mtu** | **int** |  | [optional] 
**mtu_ignore** | **bool** |  | [optional] 
**prefix_sid** | **int** |  | [optional] 
**retransmit_interval_value** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterfaceRetransmitIntervalValue**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterfaceRetransmitIntervalValue.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_ospf_interface_interface import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface from a JSON string
v1_devices_device_id_config_put_request_core_interfaces_value_interface_ospf_interface_interface_instance = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_ospf_interface_interface_dict = v1_devices_device_id_config_put_request_core_interfaces_value_interface_ospf_interface_interface_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface from a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_ospf_interface_interface_from_dict = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface.from_dict(v1_devices_device_id_config_put_request_core_interfaces_value_interface_ospf_interface_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


