# V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInnerConnectionsControlConnectionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_ip** | **str** |  | [optional] 
**dest_port** | **int** |  | [optional] 
**last_established_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**quality** | **str** |  | [optional] 
**source_ip** | **str** |  | [optional] 
**source_port** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_topology_post200_response_network_topology_inner_delta_edges_added_inner_connections_control_connection_inner import V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInnerConnectionsControlConnectionInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInnerConnectionsControlConnectionInner from a JSON string
v1_flows_topology_post200_response_network_topology_inner_delta_edges_added_inner_connections_control_connection_inner_instance = V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInnerConnectionsControlConnectionInner.from_json(json)
# print the JSON string representation of the object
print(V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInnerConnectionsControlConnectionInner.to_json())

# convert the object into a dict
v1_flows_topology_post200_response_network_topology_inner_delta_edges_added_inner_connections_control_connection_inner_dict = v1_flows_topology_post200_response_network_topology_inner_delta_edges_added_inner_connections_control_connection_inner_instance.to_dict()
# create an instance of V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInnerConnectionsControlConnectionInner from a dict
v1_flows_topology_post200_response_network_topology_inner_delta_edges_added_inner_connections_control_connection_inner_from_dict = V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInnerConnectionsControlConnectionInner.from_dict(v1_flows_topology_post200_response_network_topology_inner_delta_edges_added_inner_connections_control_connection_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


