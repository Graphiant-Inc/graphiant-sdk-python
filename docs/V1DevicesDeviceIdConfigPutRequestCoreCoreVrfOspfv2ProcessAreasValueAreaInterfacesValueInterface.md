# V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bfd** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterfaceBfd**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterfaceBfd.md) |  | [optional] 
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
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_areas_value_area_interfaces_value_interface import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterface

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterface from a JSON string
v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_areas_value_area_interfaces_value_interface_instance = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterface.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterface.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_areas_value_area_interfaces_value_interface_dict = v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_areas_value_area_interfaces_value_interface_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterface from a dict
v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_areas_value_area_interfaces_value_interface_from_dict = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOspfv2ProcessAreasValueAreaInterfacesValueInterface.from_dict(v1_devices_device_id_config_put_request_core_core_vrf_ospfv2_process_areas_value_area_interfaces_value_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


