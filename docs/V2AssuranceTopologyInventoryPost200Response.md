# V2AssuranceTopologyInventoryPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_names** | **List[str]** |  | [optional] 
**client_sites** | [**List[V2AssuranceFlowSummaryPost200ResponseClientEndpointSite]**](V2AssuranceFlowSummaryPost200ResponseClientEndpointSite.md) |  | [optional] 
**regions** | [**List[V2AssuranceTopologyInventoryPost200ResponseRegionsInner]**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 
**server_sites** | [**List[V2AssuranceFlowSummaryPost200ResponseClientEndpointSite]**](V2AssuranceFlowSummaryPost200ResponseClientEndpointSite.md) |  | [optional] 
**topology_change_ts** | [**List[V1AlarmHistoryGet200ResponseHistoryInnerTime]**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_inventory_post200_response import V2AssuranceTopologyInventoryPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyInventoryPost200Response from a JSON string
v2_assurance_topology_inventory_post200_response_instance = V2AssuranceTopologyInventoryPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyInventoryPost200Response.to_json())

# convert the object into a dict
v2_assurance_topology_inventory_post200_response_dict = v2_assurance_topology_inventory_post200_response_instance.to_dict()
# create an instance of V2AssuranceTopologyInventoryPost200Response from a dict
v2_assurance_topology_inventory_post200_response_from_dict = V2AssuranceTopologyInventoryPost200Response.from_dict(v2_assurance_topology_inventory_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


