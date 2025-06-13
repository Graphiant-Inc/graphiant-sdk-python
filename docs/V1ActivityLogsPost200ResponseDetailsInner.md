# V1ActivityLogsPost200ResponseDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**attributes** | [**List[V1ActivityLogsPostRequestSelectorJobEntity]**](V1ActivityLogsPostRequestSelectorJobEntity.md) |  | [optional] 
**category** | **str** |  | [optional] 
**disable_auto_timeout** | **bool** |  | [optional] 
**end_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**initiator_type** | **str** |  | [optional] 
**job_entities** | [**List[V1ActivityLogsPostRequestSelectorJobEntity]**](V1ActivityLogsPostRequestSelectorJobEntity.md) |  | [optional] 
**job_type** | **str** |  | [optional] 
**original_enterprise_id** | **int** |  | [optional] 
**start_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**status** | **str** |  | [optional] 
**targets** | [**List[V1ActivityLogsPost200ResponseDetailsInnerTargetsInner]**](V1ActivityLogsPost200ResponseDetailsInnerTargetsInner.md) |  | [optional] 
**trace_session_id** | **str** |  | [optional] 
**usage** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_activity_logs_post200_response_details_inner import V1ActivityLogsPost200ResponseDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ActivityLogsPost200ResponseDetailsInner from a JSON string
v1_activity_logs_post200_response_details_inner_instance = V1ActivityLogsPost200ResponseDetailsInner.from_json(json)
# print the JSON string representation of the object
print(V1ActivityLogsPost200ResponseDetailsInner.to_json())

# convert the object into a dict
v1_activity_logs_post200_response_details_inner_dict = v1_activity_logs_post200_response_details_inner_instance.to_dict()
# create an instance of V1ActivityLogsPost200ResponseDetailsInner from a dict
v1_activity_logs_post200_response_details_inner_from_dict = V1ActivityLogsPost200ResponseDetailsInner.from_dict(v1_activity_logs_post200_response_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


