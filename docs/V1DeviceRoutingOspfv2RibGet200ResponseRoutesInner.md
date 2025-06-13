# V1DeviceRoutingOspfv2RibGet200ResponseRoutesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_prefix** | **str** |  | [optional] 
**path** | [**List[V1DeviceRoutingOspfv2RibGet200ResponseRoutesInnerPathInner]**](V1DeviceRoutingOspfv2RibGet200ResponseRoutesInnerPathInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_ospfv2_rib_get200_response_routes_inner import V1DeviceRoutingOspfv2RibGet200ResponseRoutesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingOspfv2RibGet200ResponseRoutesInner from a JSON string
v1_device_routing_ospfv2_rib_get200_response_routes_inner_instance = V1DeviceRoutingOspfv2RibGet200ResponseRoutesInner.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingOspfv2RibGet200ResponseRoutesInner.to_json())

# convert the object into a dict
v1_device_routing_ospfv2_rib_get200_response_routes_inner_dict = v1_device_routing_ospfv2_rib_get200_response_routes_inner_instance.to_dict()
# create an instance of V1DeviceRoutingOspfv2RibGet200ResponseRoutesInner from a dict
v1_device_routing_ospfv2_rib_get200_response_routes_inner_from_dict = V1DeviceRoutingOspfv2RibGet200ResponseRoutesInner.from_dict(v1_device_routing_ospfv2_rib_get200_response_routes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


