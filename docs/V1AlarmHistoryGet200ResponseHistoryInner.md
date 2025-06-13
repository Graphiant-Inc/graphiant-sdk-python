# V1AlarmHistoryGet200ResponseHistoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_cleared** | **bool** |  | [optional] 
**perceived_severity** | **str** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_alarm_history_get200_response_history_inner import V1AlarmHistoryGet200ResponseHistoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AlarmHistoryGet200ResponseHistoryInner from a JSON string
v1_alarm_history_get200_response_history_inner_instance = V1AlarmHistoryGet200ResponseHistoryInner.from_json(json)
# print the JSON string representation of the object
print(V1AlarmHistoryGet200ResponseHistoryInner.to_json())

# convert the object into a dict
v1_alarm_history_get200_response_history_inner_dict = v1_alarm_history_get200_response_history_inner_instance.to_dict()
# create an instance of V1AlarmHistoryGet200ResponseHistoryInner from a dict
v1_alarm_history_get200_response_history_inner_from_dict = V1AlarmHistoryGet200ResponseHistoryInner.from_dict(v1_alarm_history_get200_response_history_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


