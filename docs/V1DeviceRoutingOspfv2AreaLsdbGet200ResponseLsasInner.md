# V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertising_router** | **str** |  | [optional] 
**age** | **int** |  | [optional] 
**asexternal_lsa** | [**V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsa**](V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsa.md) |  | [optional] 
**checksum** | **int** |  | [optional] 
**length** | **int** |  | [optional] 
**link_id** | **str** |  | [optional] 
**network_lsa** | [**V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerNetworkLsa**](V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerNetworkLsa.md) |  | [optional] 
**router_lsa** | [**V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerRouterLsa**](V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerRouterLsa.md) |  | [optional] 
**sequence_number** | **str** |  | [optional] 
**summary_lsa** | [**V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerSummaryLsa**](V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerSummaryLsa.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner import V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInner from a JSON string
v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_instance = V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInner.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInner.to_json())

# convert the object into a dict
v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_dict = v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_instance.to_dict()
# create an instance of V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInner from a dict
v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_from_dict = V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInner.from_dict(v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


