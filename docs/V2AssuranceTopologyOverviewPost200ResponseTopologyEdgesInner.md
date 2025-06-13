# V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_node_id** | **str** |  | [optional] 
**performance** | [**List[V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInnerPerformanceInner]**](V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInnerPerformanceInner.md) |  | [optional] 
**source_node_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_overview_post200_response_topology_edges_inner import V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner from a JSON string
v2_assurance_topology_overview_post200_response_topology_edges_inner_instance = V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner.to_json())

# convert the object into a dict
v2_assurance_topology_overview_post200_response_topology_edges_inner_dict = v2_assurance_topology_overview_post200_response_topology_edges_inner_instance.to_dict()
# create an instance of V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner from a dict
v2_assurance_topology_overview_post200_response_topology_edges_inner_from_dict = V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner.from_dict(v2_assurance_topology_overview_post200_response_topology_edges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


