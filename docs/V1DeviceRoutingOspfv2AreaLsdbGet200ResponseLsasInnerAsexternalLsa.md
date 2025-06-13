# V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsa


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarding_address** | **str** |  | [optional] 
**metric** | **int** |  | [optional] 
**metric_type** | **str** |  | [optional] 
**network_mask** | **int** |  | [optional] 
**tag** | **int** |  | [optional] 
**tos_metric** | [**V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsaTosMetric**](V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsaTosMetric.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_asexternal_lsa import V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsa

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsa from a JSON string
v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_asexternal_lsa_instance = V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsa.from_json(json)
# print the JSON string representation of the object
print(V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsa.to_json())

# convert the object into a dict
v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_asexternal_lsa_dict = v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_asexternal_lsa_instance.to_dict()
# create an instance of V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsa from a dict
v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_asexternal_lsa_from_dict = V1DeviceRoutingOspfv2AreaLsdbGet200ResponseLsasInnerAsexternalLsa.from_dict(v1_device_routing_ospfv2_area_lsdb_get200_response_lsas_inner_asexternal_lsa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


