# V1DiagnosticSpeedtestPostRequestParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**server_id** | **str** |  | [optional] 
**target** | [**V1DiagnosticPacketcaptureStartPostRequestTarget**](V1DiagnosticPacketcaptureStartPostRequestTarget.md) |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_speedtest_post_request_params import V1DiagnosticSpeedtestPostRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticSpeedtestPostRequestParams from a JSON string
v1_diagnostic_speedtest_post_request_params_instance = V1DiagnosticSpeedtestPostRequestParams.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticSpeedtestPostRequestParams.to_json())

# convert the object into a dict
v1_diagnostic_speedtest_post_request_params_dict = v1_diagnostic_speedtest_post_request_params_instance.to_dict()
# create an instance of V1DiagnosticSpeedtestPostRequestParams from a dict
v1_diagnostic_speedtest_post_request_params_from_dict = V1DiagnosticSpeedtestPostRequestParams.from_dict(v1_diagnostic_speedtest_post_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


