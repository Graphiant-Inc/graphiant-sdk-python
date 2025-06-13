# V1DiagnosticPingPauseResumePost204ResponseResultPingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_loss** | **float** |  | [optional] 
**avg_time** | **float** |  | [optional] 
**completed_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**max_time** | **float** |  | [optional] 
**min_time** | **float** |  | [optional] 
**result** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_ping_pause_resume_post204_response_result_ping_result import V1DiagnosticPingPauseResumePost204ResponseResultPingResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticPingPauseResumePost204ResponseResultPingResult from a JSON string
v1_diagnostic_ping_pause_resume_post204_response_result_ping_result_instance = V1DiagnosticPingPauseResumePost204ResponseResultPingResult.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticPingPauseResumePost204ResponseResultPingResult.to_json())

# convert the object into a dict
v1_diagnostic_ping_pause_resume_post204_response_result_ping_result_dict = v1_diagnostic_ping_pause_resume_post204_response_result_ping_result_instance.to_dict()
# create an instance of V1DiagnosticPingPauseResumePost204ResponseResultPingResult from a dict
v1_diagnostic_ping_pause_resume_post204_response_result_ping_result_from_dict = V1DiagnosticPingPauseResumePost204ResponseResultPingResult.from_dict(v1_diagnostic_ping_pause_resume_post204_response_result_ping_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


