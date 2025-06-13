# V1DeviceRoutingBgpNbrsCountersGet200ResponseCountersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graceful_restart** | **int** |  | [optional] 
**local_as_number** | **int** |  | [optional] 
**local_ip_address** | **str** |  | [optional] 
**local_router_id** | **str** |  | [optional] 
**peer_router_id** | **str** |  | [optional] 
**up_time** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_bgp_nbrs_counters_get200_response_counters_inner import V1DeviceRoutingBgpNbrsCountersGet200ResponseCountersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingBgpNbrsCountersGet200ResponseCountersInner from a JSON string
v1_device_routing_bgp_nbrs_counters_get200_response_counters_inner_instance = V1DeviceRoutingBgpNbrsCountersGet200ResponseCountersInner.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingBgpNbrsCountersGet200ResponseCountersInner.to_json())

# convert the object into a dict
v1_device_routing_bgp_nbrs_counters_get200_response_counters_inner_dict = v1_device_routing_bgp_nbrs_counters_get200_response_counters_inner_instance.to_dict()
# create an instance of V1DeviceRoutingBgpNbrsCountersGet200ResponseCountersInner from a dict
v1_device_routing_bgp_nbrs_counters_get200_response_counters_inner_from_dict = V1DeviceRoutingBgpNbrsCountersGet200ResponseCountersInner.from_dict(v1_device_routing_bgp_nbrs_counters_get200_response_counters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


