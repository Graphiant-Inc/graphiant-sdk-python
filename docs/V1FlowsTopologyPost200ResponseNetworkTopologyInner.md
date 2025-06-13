# V1FlowsTopologyPost200ResponseNetworkTopologyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuit_status** | **Dict[str, int]** |  | [optional] 
**delta** | [**V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta**](V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta.md) |  | [optional] 
**edges** | [**List[V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInner]**](V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInner.md) |  | [optional] 
**flows** | **int** |  | [optional] 
**nodes** | [**List[V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner]**](V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner.md) |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_topology_post200_response_network_topology_inner import V1FlowsTopologyPost200ResponseNetworkTopologyInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsTopologyPost200ResponseNetworkTopologyInner from a JSON string
v1_flows_topology_post200_response_network_topology_inner_instance = V1FlowsTopologyPost200ResponseNetworkTopologyInner.from_json(json)
# print the JSON string representation of the object
print(V1FlowsTopologyPost200ResponseNetworkTopologyInner.to_json())

# convert the object into a dict
v1_flows_topology_post200_response_network_topology_inner_dict = v1_flows_topology_post200_response_network_topology_inner_instance.to_dict()
# create an instance of V1FlowsTopologyPost200ResponseNetworkTopologyInner from a dict
v1_flows_topology_post200_response_network_topology_inner_from_dict = V1FlowsTopologyPost200ResponseNetworkTopologyInner.from_dict(v1_flows_topology_post200_response_network_topology_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


