# V2AssuranceFlowSummaryPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_ip** | **str** |  | [optional] 
**server_ip** | **str** |  | [optional] 
**server_port** | **int** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_flow_summary_post_request import V2AssuranceFlowSummaryPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceFlowSummaryPostRequest from a JSON string
v2_assurance_flow_summary_post_request_instance = V2AssuranceFlowSummaryPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceFlowSummaryPostRequest.to_json())

# convert the object into a dict
v2_assurance_flow_summary_post_request_dict = v2_assurance_flow_summary_post_request_instance.to_dict()
# create an instance of V2AssuranceFlowSummaryPostRequest from a dict
v2_assurance_flow_summary_post_request_from_dict = V2AssuranceFlowSummaryPostRequest.from_dict(v2_assurance_flow_summary_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


