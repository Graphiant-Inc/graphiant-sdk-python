# V1LogsPost200ResponseLogsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**facility** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_logs_post200_response_logs_inner import V1LogsPost200ResponseLogsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1LogsPost200ResponseLogsInner from a JSON string
v1_logs_post200_response_logs_inner_instance = V1LogsPost200ResponseLogsInner.from_json(json)
# print the JSON string representation of the object
print(V1LogsPost200ResponseLogsInner.to_json())

# convert the object into a dict
v1_logs_post200_response_logs_inner_dict = v1_logs_post200_response_logs_inner_instance.to_dict()
# create an instance of V1LogsPost200ResponseLogsInner from a dict
v1_logs_post200_response_logs_inner_from_dict = V1LogsPost200ResponseLogsInner.from_dict(v1_logs_post200_response_logs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


