# V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_address** | **str** |  | [optional] 
**path_mtu** | **int** |  | [optional] 
**round_trip_time** | **float** |  | [optional] 
**stats** | [**V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInnerStats**](V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInnerStats.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_hops_inner import V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInner from a JSON string
v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_hops_inner_instance = V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInner.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInner.to_json())

# convert the object into a dict
v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_hops_inner_dict = v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_hops_inner_instance.to_dict()
# create an instance of V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInner from a dict
v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_hops_inner_from_dict = V1DiagnosticPingPauseResumePost204ResponseResultTraceResultHopsInner.from_dict(v1_diagnostic_ping_pause_resume_post204_response_result_trace_result_hops_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


