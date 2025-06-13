# V1FlowsFlowTablePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_ref** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**flow_table** | [**List[V1FlowsFlowTablePost200ResponseFlowTableInner]**](V1FlowsFlowTablePost200ResponseFlowTableInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_flow_table_post200_response import V1FlowsFlowTablePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsFlowTablePost200Response from a JSON string
v1_flows_flow_table_post200_response_instance = V1FlowsFlowTablePost200Response.from_json(json)
# print the JSON string representation of the object
print(V1FlowsFlowTablePost200Response.to_json())

# convert the object into a dict
v1_flows_flow_table_post200_response_dict = v1_flows_flow_table_post200_response_instance.to_dict()
# create an instance of V1FlowsFlowTablePost200Response from a dict
v1_flows_flow_table_post200_response_from_dict = V1FlowsFlowTablePost200Response.from_dict(v1_flows_flow_table_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


