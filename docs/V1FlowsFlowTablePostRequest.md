# V1FlowsFlowTablePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** |  | [optional] 
**app_name** | **str** |  | [optional] 
**cursor_ref** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**device_id** | **int** |  | [optional] 
**is_dia** | **bool** |  | [optional] 
**num_flow_records** | **int** |  | [optional] 
**selector** | [**V1FlowsFlowTablePostRequestSelector**](V1FlowsFlowTablePostRequestSelector.md) |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_flow_table_post_request import V1FlowsFlowTablePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsFlowTablePostRequest from a JSON string
v1_flows_flow_table_post_request_instance = V1FlowsFlowTablePostRequest.from_json(json)
# print the JSON string representation of the object
print(V1FlowsFlowTablePostRequest.to_json())

# convert the object into a dict
v1_flows_flow_table_post_request_dict = v1_flows_flow_table_post_request_instance.to_dict()
# create an instance of V1FlowsFlowTablePostRequest from a dict
v1_flows_flow_table_post_request_from_dict = V1FlowsFlowTablePostRequest.from_dict(v1_flows_flow_table_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


