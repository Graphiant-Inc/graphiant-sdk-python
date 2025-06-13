# V1DiagnosticSpeedtestReportPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**history_length** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_speedtest_report_put_request import V1DiagnosticSpeedtestReportPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticSpeedtestReportPutRequest from a JSON string
v1_diagnostic_speedtest_report_put_request_instance = V1DiagnosticSpeedtestReportPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticSpeedtestReportPutRequest.to_json())

# convert the object into a dict
v1_diagnostic_speedtest_report_put_request_dict = v1_diagnostic_speedtest_report_put_request_instance.to_dict()
# create an instance of V1DiagnosticSpeedtestReportPutRequest from a dict
v1_diagnostic_speedtest_report_put_request_from_dict = V1DiagnosticSpeedtestReportPutRequest.from_dict(v1_diagnostic_speedtest_report_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


