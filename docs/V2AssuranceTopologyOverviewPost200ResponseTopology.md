# V2AssuranceTopologyOverviewPost200ResponseTopology


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges** | [**List[V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner]**](V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner.md) |  | [optional] 
**nodes** | [**List[V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInner]**](V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInner.md) |  | [optional] 
**paths** | [**List[V2AssuranceTopologyOverviewPost200ResponseTopologyPathsInner]**](V2AssuranceTopologyOverviewPost200ResponseTopologyPathsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_overview_post200_response_topology import V2AssuranceTopologyOverviewPost200ResponseTopology

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyOverviewPost200ResponseTopology from a JSON string
v2_assurance_topology_overview_post200_response_topology_instance = V2AssuranceTopologyOverviewPost200ResponseTopology.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyOverviewPost200ResponseTopology.to_json())

# convert the object into a dict
v2_assurance_topology_overview_post200_response_topology_dict = v2_assurance_topology_overview_post200_response_topology_instance.to_dict()
# create an instance of V2AssuranceTopologyOverviewPost200ResponseTopology from a dict
v2_assurance_topology_overview_post200_response_topology_from_dict = V2AssuranceTopologyOverviewPost200ResponseTopology.from_dict(v2_assurance_topology_overview_post200_response_topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


