# V1FlowsFlowTablePostRequestSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuit_name** | **List[str]** |  | [optional] 
**sla_class** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_flow_table_post_request_selector import V1FlowsFlowTablePostRequestSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsFlowTablePostRequestSelector from a JSON string
v1_flows_flow_table_post_request_selector_instance = V1FlowsFlowTablePostRequestSelector.from_json(json)
# print the JSON string representation of the object
print(V1FlowsFlowTablePostRequestSelector.to_json())

# convert the object into a dict
v1_flows_flow_table_post_request_selector_dict = v1_flows_flow_table_post_request_selector_instance.to_dict()
# create an instance of V1FlowsFlowTablePostRequestSelector from a dict
v1_flows_flow_table_post_request_selector_from_dict = V1FlowsFlowTablePostRequestSelector.from_dict(v1_flows_flow_table_post_request_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


