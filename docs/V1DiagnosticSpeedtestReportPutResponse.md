# V1DiagnosticSpeedtestReportPutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | **bytearray** | The generated report | [optional] 
**report_id** | **int** | 8 bytes (base32 encoded) identifier for the report | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_speedtest_report_put_response import V1DiagnosticSpeedtestReportPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticSpeedtestReportPutResponse from a JSON string
v1_diagnostic_speedtest_report_put_response_instance = V1DiagnosticSpeedtestReportPutResponse.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticSpeedtestReportPutResponse.to_json())

# convert the object into a dict
v1_diagnostic_speedtest_report_put_response_dict = v1_diagnostic_speedtest_report_put_response_instance.to_dict()
# create an instance of V1DiagnosticSpeedtestReportPutResponse from a dict
v1_diagnostic_speedtest_report_put_response_from_dict = V1DiagnosticSpeedtestReportPutResponse.from_dict(v1_diagnostic_speedtest_report_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


