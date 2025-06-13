# V1DeviceRoutingBgpNbrsDetailsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ebgp_multi_hop_ttl** | **int** |  | [optional] 
**hold_timer** | **int** |  | [optional] 
**keep_alive_timer** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_bgp_nbrs_details_get200_response import V1DeviceRoutingBgpNbrsDetailsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingBgpNbrsDetailsGet200Response from a JSON string
v1_device_routing_bgp_nbrs_details_get200_response_instance = V1DeviceRoutingBgpNbrsDetailsGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingBgpNbrsDetailsGet200Response.to_json())

# convert the object into a dict
v1_device_routing_bgp_nbrs_details_get200_response_dict = v1_device_routing_bgp_nbrs_details_get200_response_instance.to_dict()
# create an instance of V1DeviceRoutingBgpNbrsDetailsGet200Response from a dict
v1_device_routing_bgp_nbrs_details_get200_response_from_dict = V1DeviceRoutingBgpNbrsDetailsGet200Response.from_dict(v1_device_routing_bgp_nbrs_details_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


