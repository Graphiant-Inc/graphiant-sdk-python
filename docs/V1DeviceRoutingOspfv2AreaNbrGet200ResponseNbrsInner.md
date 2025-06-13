# V1DeviceRoutingOspfv2AreaNbrGet200ResponseNbrsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**cost** | **int** |  | [optional] 
**dead_timer** | **int** |  | [optional] 
**last_state_change** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**router_id** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_ospfv2_area_nbr_get200_response_nbrs_inner import V1DeviceRoutingOspfv2AreaNbrGet200ResponseNbrsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingOspfv2AreaNbrGet200ResponseNbrsInner from a JSON string
v1_device_routing_ospfv2_area_nbr_get200_response_nbrs_inner_instance = V1DeviceRoutingOspfv2AreaNbrGet200ResponseNbrsInner.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingOspfv2AreaNbrGet200ResponseNbrsInner.to_json())

# convert the object into a dict
v1_device_routing_ospfv2_area_nbr_get200_response_nbrs_inner_dict = v1_device_routing_ospfv2_area_nbr_get200_response_nbrs_inner_instance.to_dict()
# create an instance of V1DeviceRoutingOspfv2AreaNbrGet200ResponseNbrsInner from a dict
v1_device_routing_ospfv2_area_nbr_get200_response_nbrs_inner_from_dict = V1DeviceRoutingOspfv2AreaNbrGet200ResponseNbrsInner.from_dict(v1_device_routing_ospfv2_area_nbr_get200_response_nbrs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


