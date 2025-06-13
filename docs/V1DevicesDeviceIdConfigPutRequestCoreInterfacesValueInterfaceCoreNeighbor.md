# V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost.md) |  | [optional] 
**ospf_cost** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost.md) |  | [optional] 
**peer_hostname** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_core_neighbor import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor from a JSON string
v1_devices_device_id_config_put_request_core_interfaces_value_interface_core_neighbor_instance = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_core_neighbor_dict = v1_devices_device_id_config_put_request_core_interfaces_value_interface_core_neighbor_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor from a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_core_neighbor_from_dict = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor.from_dict(v1_devices_device_id_config_put_request_core_interfaces_value_interface_core_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


