# V1DeviceRoutingVrfBgpRouteCountPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**vrf_name** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_vrf_bgp_route_count_post_request import V1DeviceRoutingVrfBgpRouteCountPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingVrfBgpRouteCountPostRequest from a JSON string
v1_device_routing_vrf_bgp_route_count_post_request_instance = V1DeviceRoutingVrfBgpRouteCountPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingVrfBgpRouteCountPostRequest.to_json())

# convert the object into a dict
v1_device_routing_vrf_bgp_route_count_post_request_dict = v1_device_routing_vrf_bgp_route_count_post_request_instance.to_dict()
# create an instance of V1DeviceRoutingVrfBgpRouteCountPostRequest from a dict
v1_device_routing_vrf_bgp_route_count_post_request_from_dict = V1DeviceRoutingVrfBgpRouteCountPostRequest.from_dict(v1_device_routing_vrf_bgp_route_count_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


