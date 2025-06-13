# V1LogsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_ref** | **str** |  | [optional] 
**customer_view** | **bool** |  | [optional] 
**device_ids** | **List[int]** |  | [optional] 
**histogram_bucket_size_sec** | **int** |  | [optional] 
**num_logs** | **int** |  | [optional] 
**old_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**recent_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**selectors** | [**List[V1LogsPostRequestSelectorsInner]**](V1LogsPostRequestSelectorsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_logs_post_request import V1LogsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1LogsPostRequest from a JSON string
v1_logs_post_request_instance = V1LogsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1LogsPostRequest.to_json())

# convert the object into a dict
v1_logs_post_request_dict = v1_logs_post_request_instance.to_dict()
# create an instance of V1LogsPostRequest from a dict
v1_logs_post_request_from_dict = V1LogsPostRequest.from_dict(v1_logs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


