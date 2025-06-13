# V1ActivityLogsPost200ResponseDetailsInnerTargetsInnerEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**state_id** | **int** |  | [optional] 
**trace_session_id** | **str** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_activity_logs_post200_response_details_inner_targets_inner_events_inner import V1ActivityLogsPost200ResponseDetailsInnerTargetsInnerEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ActivityLogsPost200ResponseDetailsInnerTargetsInnerEventsInner from a JSON string
v1_activity_logs_post200_response_details_inner_targets_inner_events_inner_instance = V1ActivityLogsPost200ResponseDetailsInnerTargetsInnerEventsInner.from_json(json)
# print the JSON string representation of the object
print(V1ActivityLogsPost200ResponseDetailsInnerTargetsInnerEventsInner.to_json())

# convert the object into a dict
v1_activity_logs_post200_response_details_inner_targets_inner_events_inner_dict = v1_activity_logs_post200_response_details_inner_targets_inner_events_inner_instance.to_dict()
# create an instance of V1ActivityLogsPost200ResponseDetailsInnerTargetsInnerEventsInner from a dict
v1_activity_logs_post200_response_details_inner_targets_inner_events_inner_from_dict = V1ActivityLogsPost200ResponseDetailsInnerTargetsInnerEventsInner.from_dict(v1_activity_logs_post200_response_details_inner_targets_inner_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


