# V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInnerConnections**](V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInnerConnections.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**override_region** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_topology_post200_response_network_topology_inner_delta_nodes_added_inner import V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner from a JSON string
v1_flows_topology_post200_response_network_topology_inner_delta_nodes_added_inner_instance = V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner.from_json(json)
# print the JSON string representation of the object
print(V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner.to_json())

# convert the object into a dict
v1_flows_topology_post200_response_network_topology_inner_delta_nodes_added_inner_dict = v1_flows_topology_post200_response_network_topology_inner_delta_nodes_added_inner_instance.to_dict()
# create an instance of V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner from a dict
v1_flows_topology_post200_response_network_topology_inner_delta_nodes_added_inner_from_dict = V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner.from_dict(v1_flows_topology_post200_response_network_topology_inner_delta_nodes_added_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


