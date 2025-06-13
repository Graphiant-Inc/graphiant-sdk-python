# V1DevicesRoutingVrfProtocolRouteCountGet200ResponseCountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** |  | [optional] 
**route_count** | [**V1DeviceRoutingVrfBgpEibgpRouteCountGet200ResponseEbgpRouteCount**](V1DeviceRoutingVrfBgpEibgpRouteCountGet200ResponseEbgpRouteCount.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_routing_vrf_protocol_route_count_get200_response_counts_inner import V1DevicesRoutingVrfProtocolRouteCountGet200ResponseCountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesRoutingVrfProtocolRouteCountGet200ResponseCountsInner from a JSON string
v1_devices_routing_vrf_protocol_route_count_get200_response_counts_inner_instance = V1DevicesRoutingVrfProtocolRouteCountGet200ResponseCountsInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesRoutingVrfProtocolRouteCountGet200ResponseCountsInner.to_json())

# convert the object into a dict
v1_devices_routing_vrf_protocol_route_count_get200_response_counts_inner_dict = v1_devices_routing_vrf_protocol_route_count_get200_response_counts_inner_instance.to_dict()
# create an instance of V1DevicesRoutingVrfProtocolRouteCountGet200ResponseCountsInner from a dict
v1_devices_routing_vrf_protocol_route_count_get200_response_counts_inner_from_dict = V1DevicesRoutingVrfProtocolRouteCountGet200ResponseCountsInner.from_dict(v1_devices_routing_vrf_protocol_route_count_get200_response_counts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


