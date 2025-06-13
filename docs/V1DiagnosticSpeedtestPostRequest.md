# V1DiagnosticSpeedtestPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**params** | [**V1DiagnosticSpeedtestPostRequestParams**](V1DiagnosticSpeedtestPostRequestParams.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_speedtest_post_request import V1DiagnosticSpeedtestPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticSpeedtestPostRequest from a JSON string
v1_diagnostic_speedtest_post_request_instance = V1DiagnosticSpeedtestPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticSpeedtestPostRequest.to_json())

# convert the object into a dict
v1_diagnostic_speedtest_post_request_dict = v1_diagnostic_speedtest_post_request_instance.to_dict()
# create an instance of V1DiagnosticSpeedtestPostRequest from a dict
v1_diagnostic_speedtest_post_request_from_dict = V1DiagnosticSpeedtestPostRequest.from_dict(v1_diagnostic_speedtest_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


