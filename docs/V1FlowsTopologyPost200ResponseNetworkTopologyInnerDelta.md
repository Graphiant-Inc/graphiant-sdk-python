# V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges_added** | [**List[V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInner]**](V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInner.md) |  | [optional] 
**edges_deleted** | [**List[V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInner]**](V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInner.md) |  | [optional] 
**nodes_added** | [**List[V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner]**](V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner.md) |  | [optional] 
**nodes_deleted** | [**List[V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner]**](V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_topology_post200_response_network_topology_inner_delta import V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta from a JSON string
v1_flows_topology_post200_response_network_topology_inner_delta_instance = V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta.from_json(json)
# print the JSON string representation of the object
print(V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta.to_json())

# convert the object into a dict
v1_flows_topology_post200_response_network_topology_inner_delta_dict = v1_flows_topology_post200_response_network_topology_inner_delta_instance.to_dict()
# create an instance of V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta from a dict
v1_flows_topology_post200_response_network_topology_inner_delta_from_dict = V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta.from_dict(v1_flows_topology_post200_response_network_topology_inner_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


