# V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_aggregations** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpAggregationsValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpAggregationsValue.md) |  | [optional] 
**bgp_multipath** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfEbgpMultipath**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfEbgpMultipath.md) |  | [optional] 
**bgp_neighbors** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValue.md) |  | [optional] 
**bgp_redistribution** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue.md) |  | [optional] 
**carrier** | **str** |  | [optional] 
**circuit_type** | **str** |  | [optional] 
**connection_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**dia_enabled** | **bool** |  | [optional] 
**drop_mechanism** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**last_resort** | **bool** |  | [optional] 
**link_down_speed_mbps** | **int** |  | [optional] 
**link_up_speed_mbps** | **int** |  | [optional] 
**loopback** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**pat_addresses** | [**V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses**](V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses.md) |  | [optional] 
**qos_profile** | **str** |  | [optional] 
**qos_profile_type** | **str** |  | [optional] 
**static_routes** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValue]**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfStaticRoutesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_circuits_value import V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValue from a JSON string
v1_devices_device_id_config_put_request_edge_circuits_value_instance = V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValue.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValue.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_edge_circuits_value_dict = v1_devices_device_id_config_put_request_edge_circuits_value_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValue from a dict
v1_devices_device_id_config_put_request_edge_circuits_value_from_dict = V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValue.from_dict(v1_devices_device_id_config_put_request_edge_circuits_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


