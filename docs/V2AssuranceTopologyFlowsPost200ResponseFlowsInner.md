# V2AssuranceTopologyFlowsPost200ResponseFlowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**client_site** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointSite**](V2AssuranceFlowSummaryPost200ResponseClientEndpointSite.md) |  | [optional] 
**first_seen_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**lan_segment** | **str** |  | [optional] 
**last_seen_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**server_ip** | **str** |  | [optional] 
**server_port** | **int** |  | [optional] 
**server_site** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointSite**](V2AssuranceFlowSummaryPost200ResponseClientEndpointSite.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_flows_post200_response_flows_inner import V2AssuranceTopologyFlowsPost200ResponseFlowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyFlowsPost200ResponseFlowsInner from a JSON string
v2_assurance_topology_flows_post200_response_flows_inner_instance = V2AssuranceTopologyFlowsPost200ResponseFlowsInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyFlowsPost200ResponseFlowsInner.to_json())

# convert the object into a dict
v2_assurance_topology_flows_post200_response_flows_inner_dict = v2_assurance_topology_flows_post200_response_flows_inner_instance.to_dict()
# create an instance of V2AssuranceTopologyFlowsPost200ResponseFlowsInner from a dict
v2_assurance_topology_flows_post200_response_flows_inner_from_dict = V2AssuranceTopologyFlowsPost200ResponseFlowsInner.from_dict(v2_assurance_topology_flows_post200_response_flows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


