# V1DiagnosticPingPauseResumePostRequestParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_address** | **str** |  | [optional] 
**hop_stats_count** | **int** |  | [optional] 
**interface** | **str** |  | [optional] 
**payload_size** | **int** |  | [optional] 
**port** | **int** |  | [optional] 
**probe_count** | **int** |  | [optional] 
**src_address** | **str** |  | [optional] 
**tos** | **int** |  | [optional] 
**vrf_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_ping_pause_resume_post_request_params import V1DiagnosticPingPauseResumePostRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticPingPauseResumePostRequestParams from a JSON string
v1_diagnostic_ping_pause_resume_post_request_params_instance = V1DiagnosticPingPauseResumePostRequestParams.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticPingPauseResumePostRequestParams.to_json())

# convert the object into a dict
v1_diagnostic_ping_pause_resume_post_request_params_dict = v1_diagnostic_ping_pause_resume_post_request_params_instance.to_dict()
# create an instance of V1DiagnosticPingPauseResumePostRequestParams from a dict
v1_diagnostic_ping_pause_resume_post_request_params_from_dict = V1DiagnosticPingPauseResumePostRequestParams.from_dict(v1_diagnostic_ping_pause_resume_post_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


