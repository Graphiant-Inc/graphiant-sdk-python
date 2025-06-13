# V1ActivityLogsPost200ResponseDetailsInnerTargetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed_failure_reason** | **str** |  | [optional] 
**end_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**events** | [**List[V1ActivityLogsPost200ResponseDetailsInnerTargetsInnerEventsInner]**](V1ActivityLogsPost200ResponseDetailsInnerTargetsInnerEventsInner.md) |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**ids** | [**List[V1ActivityLogsPostRequestSelectorJobEntity]**](V1ActivityLogsPostRequestSelectorJobEntity.md) |  | [optional] 
**start_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_activity_logs_post200_response_details_inner_targets_inner import V1ActivityLogsPost200ResponseDetailsInnerTargetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ActivityLogsPost200ResponseDetailsInnerTargetsInner from a JSON string
v1_activity_logs_post200_response_details_inner_targets_inner_instance = V1ActivityLogsPost200ResponseDetailsInnerTargetsInner.from_json(json)
# print the JSON string representation of the object
print(V1ActivityLogsPost200ResponseDetailsInnerTargetsInner.to_json())

# convert the object into a dict
v1_activity_logs_post200_response_details_inner_targets_inner_dict = v1_activity_logs_post200_response_details_inner_targets_inner_instance.to_dict()
# create an instance of V1ActivityLogsPost200ResponseDetailsInnerTargetsInner from a dict
v1_activity_logs_post200_response_details_inner_targets_inner_from_dict = V1ActivityLogsPost200ResponseDetailsInnerTargetsInner.from_dict(v1_activity_logs_post200_response_details_inner_targets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


