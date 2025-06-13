# V1DeviceRoutingOspfv2RibGet200ResponseRoutesInnerPathInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**egress_interface** | **str** |  | [optional] 
**last_modified** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**metric** | **int** |  | [optional] 
**next_hop** | **str** |  | [optional] 
**tag** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_ospfv2_rib_get200_response_routes_inner_path_inner import V1DeviceRoutingOspfv2RibGet200ResponseRoutesInnerPathInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingOspfv2RibGet200ResponseRoutesInnerPathInner from a JSON string
v1_device_routing_ospfv2_rib_get200_response_routes_inner_path_inner_instance = V1DeviceRoutingOspfv2RibGet200ResponseRoutesInnerPathInner.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingOspfv2RibGet200ResponseRoutesInnerPathInner.to_json())

# convert the object into a dict
v1_device_routing_ospfv2_rib_get200_response_routes_inner_path_inner_dict = v1_device_routing_ospfv2_rib_get200_response_routes_inner_path_inner_instance.to_dict()
# create an instance of V1DeviceRoutingOspfv2RibGet200ResponseRoutesInnerPathInner from a dict
v1_device_routing_ospfv2_rib_get200_response_routes_inner_path_inner_from_dict = V1DeviceRoutingOspfv2RibGet200ResponseRoutesInnerPathInner.from_dict(v1_device_routing_ospfv2_rib_get200_response_routes_inner_path_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


