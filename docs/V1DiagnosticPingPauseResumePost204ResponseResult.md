# V1DiagnosticPingPauseResumePost204ResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ping_result** | [**V1DiagnosticPingPauseResumePost204ResponseResultPingResult**](V1DiagnosticPingPauseResumePost204ResponseResultPingResult.md) |  | [optional] 
**route_info** | [**V1DiagnosticPingPauseResumePost204ResponseResultRouteInfo**](V1DiagnosticPingPauseResumePost204ResponseResultRouteInfo.md) |  | [optional] 
**trace_result** | [**V1DiagnosticPingPauseResumePost204ResponseResultTraceResult**](V1DiagnosticPingPauseResumePost204ResponseResultTraceResult.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_ping_pause_resume_post204_response_result import V1DiagnosticPingPauseResumePost204ResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticPingPauseResumePost204ResponseResult from a JSON string
v1_diagnostic_ping_pause_resume_post204_response_result_instance = V1DiagnosticPingPauseResumePost204ResponseResult.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticPingPauseResumePost204ResponseResult.to_json())

# convert the object into a dict
v1_diagnostic_ping_pause_resume_post204_response_result_dict = v1_diagnostic_ping_pause_resume_post204_response_result_instance.to_dict()
# create an instance of V1DiagnosticPingPauseResumePost204ResponseResult from a dict
v1_diagnostic_ping_pause_resume_post204_response_result_from_dict = V1DiagnosticPingPauseResumePost204ResponseResult.from_dict(v1_diagnostic_ping_pause_resume_post204_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


