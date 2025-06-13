# V1FlowsTopologyPostRequestAppSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | [optional] 
**app_name** | **str** |  | [optional] 
**sla_class** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_topology_post_request_app_selector import V1FlowsTopologyPostRequestAppSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsTopologyPostRequestAppSelector from a JSON string
v1_flows_topology_post_request_app_selector_instance = V1FlowsTopologyPostRequestAppSelector.from_json(json)
# print the JSON string representation of the object
print(V1FlowsTopologyPostRequestAppSelector.to_json())

# convert the object into a dict
v1_flows_topology_post_request_app_selector_dict = v1_flows_topology_post_request_app_selector_instance.to_dict()
# create an instance of V1FlowsTopologyPostRequestAppSelector from a dict
v1_flows_topology_post_request_app_selector_from_dict = V1FlowsTopologyPostRequestAppSelector.from_dict(v1_flows_topology_post_request_app_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


