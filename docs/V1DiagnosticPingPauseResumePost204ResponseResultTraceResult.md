# V1DiagnosticPingPauseResumePost204ResponseResultTraceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hops** | [**List[V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInner]**](V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInner.md) |  | [optional] 
**max_latency** | **float** |  | [optional] 
**max_latency_host** | **str** |  | [optional] 
**max_path_mtu** | **int** |  | [optional] 
**min_path_mtu** | **int** |  | [optional] 
**result** | **str** |  | [optional] 
**stopped_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_ping_pause_resume_post204_response_result_trace_result import V1DiagnosticPingPauseResumePost204ResponseResultTraceResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticPingPauseResumePost204ResponseResultTraceResult from a JSON string
v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_instance = V1DiagnosticPingPauseResumePost204ResponseResultTraceResult.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticPingPauseResumePost204ResponseResultTraceResult.to_json())

# convert the object into a dict
v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_dict = v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_instance.to_dict()
# create an instance of V1DiagnosticPingPauseResumePost204ResponseResultTraceResult from a dict
v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_from_dict = V1DiagnosticPingPauseResumePost204ResponseResultTraceResult.from_dict(v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


