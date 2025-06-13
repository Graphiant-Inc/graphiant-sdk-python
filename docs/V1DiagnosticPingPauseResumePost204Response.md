# V1DiagnosticPingPauseResumePost204Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**V1DiagnosticPingPauseResumePost204ResponseResult**](V1DiagnosticPingPauseResumePost204ResponseResult.md) |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_ping_pause_resume_post204_response import V1DiagnosticPingPauseResumePost204Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticPingPauseResumePost204Response from a JSON string
v1_diagnostic_ping_pause_resume_post204_response_instance = V1DiagnosticPingPauseResumePost204Response.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticPingPauseResumePost204Response.to_json())

# convert the object into a dict
v1_diagnostic_ping_pause_resume_post204_response_dict = v1_diagnostic_ping_pause_resume_post204_response_instance.to_dict()
# create an instance of V1DiagnosticPingPauseResumePost204Response from a dict
v1_diagnostic_ping_pause_resume_post204_response_from_dict = V1DiagnosticPingPauseResumePost204Response.from_dict(v1_diagnostic_ping_pause_resume_post204_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


