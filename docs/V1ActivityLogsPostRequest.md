# V1ActivityLogsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_ref** | **str** |  | [optional] 
**num_logs** | **int** |  | [optional] 
**old_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**recent_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**selector** | [**V1ActivityLogsPostRequestSelector**](V1ActivityLogsPostRequestSelector.md) |  | [optional] 
**selector_v2** | [**V1ActivityLogsPostRequestSelectorV2**](V1ActivityLogsPostRequestSelectorV2.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_activity_logs_post_request import V1ActivityLogsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ActivityLogsPostRequest from a JSON string
v1_activity_logs_post_request_instance = V1ActivityLogsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ActivityLogsPostRequest.to_json())

# convert the object into a dict
v1_activity_logs_post_request_dict = v1_activity_logs_post_request_instance.to_dict()
# create an instance of V1ActivityLogsPostRequest from a dict
v1_activity_logs_post_request_from_dict = V1ActivityLogsPostRequest.from_dict(v1_activity_logs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


