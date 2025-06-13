# V1FlowsTopologyPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_topology** | [**List[V1FlowsTopologyPost200ResponseNetworkTopologyInner]**](V1FlowsTopologyPost200ResponseNetworkTopologyInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_topology_post200_response import V1FlowsTopologyPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsTopologyPost200Response from a JSON string
v1_flows_topology_post200_response_instance = V1FlowsTopologyPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1FlowsTopologyPost200Response.to_json())

# convert the object into a dict
v1_flows_topology_post200_response_dict = v1_flows_topology_post200_response_instance.to_dict()
# create an instance of V1FlowsTopologyPost200Response from a dict
v1_flows_topology_post200_response_from_dict = V1FlowsTopologyPost200Response.from_dict(v1_flows_topology_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


