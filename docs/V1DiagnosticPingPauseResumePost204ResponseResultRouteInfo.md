# V1DiagnosticPingPauseResumePost204ResponseResultRouteInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nexthop_address** | **str** |  | [optional] 
**outgoing_interface** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_ping_pause_resume_post204_response_result_route_info import V1DiagnosticPingPauseResumePost204ResponseResultRouteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticPingPauseResumePost204ResponseResultRouteInfo from a JSON string
v1_diagnostic_ping_pause_resume_post204_response_result_route_info_instance = V1DiagnosticPingPauseResumePost204ResponseResultRouteInfo.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticPingPauseResumePost204ResponseResultRouteInfo.to_json())

# convert the object into a dict
v1_diagnostic_ping_pause_resume_post204_response_result_route_info_dict = v1_diagnostic_ping_pause_resume_post204_response_result_route_info_instance.to_dict()
# create an instance of V1DiagnosticPingPauseResumePost204ResponseResultRouteInfo from a dict
v1_diagnostic_ping_pause_resume_post204_response_result_route_info_from_dict = V1DiagnosticPingPauseResumePost204ResponseResultRouteInfo.from_dict(v1_diagnostic_ping_pause_resume_post204_response_result_route_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


