# V1DeviceRoutingBgpNbrsPerAfiPrefixGet200ResponsePrefixesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afi_safi_name** | **str** |  | [optional] 
**prefix_rcvd** | **int** |  | [optional] 
**prefix_sent** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_bgp_nbrs_per_afi_prefix_get200_response_prefixes_inner import V1DeviceRoutingBgpNbrsPerAfiPrefixGet200ResponsePrefixesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingBgpNbrsPerAfiPrefixGet200ResponsePrefixesInner from a JSON string
v1_device_routing_bgp_nbrs_per_afi_prefix_get200_response_prefixes_inner_instance = V1DeviceRoutingBgpNbrsPerAfiPrefixGet200ResponsePrefixesInner.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingBgpNbrsPerAfiPrefixGet200ResponsePrefixesInner.to_json())

# convert the object into a dict
v1_device_routing_bgp_nbrs_per_afi_prefix_get200_response_prefixes_inner_dict = v1_device_routing_bgp_nbrs_per_afi_prefix_get200_response_prefixes_inner_instance.to_dict()
# create an instance of V1DeviceRoutingBgpNbrsPerAfiPrefixGet200ResponsePrefixesInner from a dict
v1_device_routing_bgp_nbrs_per_afi_prefix_get200_response_prefixes_inner_from_dict = V1DeviceRoutingBgpNbrsPerAfiPrefixGet200ResponsePrefixesInner.from_dict(v1_device_routing_bgp_nbrs_per_afi_prefix_get200_response_prefixes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


