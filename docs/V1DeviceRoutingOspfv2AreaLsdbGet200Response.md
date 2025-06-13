# V1DeviceRoutingOspfv2AreaLsdbGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lsas** | [**List[V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInner]**](V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInner.md) |  | [optional] 
**page_info** | [**V1NatEntriesDeviceIdGet200ResponsePageInfo**](V1NatEntriesDeviceIdGet200ResponsePageInfo.md) |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_ospfv2_area_lsdb_get200_response import V1DeviceRoutingOspfv2AreaLsdbGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingOspfv2AreaLsdbGet200Response from a JSON string
v1_device_routing_ospfv2_area_lsdb_get200_response_instance = V1DeviceRoutingOspfv2AreaLsdbGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingOspfv2AreaLsdbGet200Response.to_json())

# convert the object into a dict
v1_device_routing_ospfv2_area_lsdb_get200_response_dict = v1_device_routing_ospfv2_area_lsdb_get200_response_instance.to_dict()
# create an instance of V1DeviceRoutingOspfv2AreaLsdbGet200Response from a dict
v1_device_routing_ospfv2_area_lsdb_get200_response_from_dict = V1DeviceRoutingOspfv2AreaLsdbGet200Response.from_dict(v1_device_routing_ospfv2_area_lsdb_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


