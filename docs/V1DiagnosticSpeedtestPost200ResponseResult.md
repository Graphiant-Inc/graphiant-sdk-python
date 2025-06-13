# V1DiagnosticSpeedtestPost200ResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_ping_time** | **float** |  | [optional] 
**date_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**download_speed** | **float** |  | [optional] 
**isp** | **str** |  | [optional] 
**max_ping_time** | **float** |  | [optional] 
**min_ping_time** | **float** |  | [optional] 
**result** | **str** |  | [optional] 
**server_details** | [**V1DiagnosticSpeedtestServersGet200ResponseServerInner**](V1DiagnosticSpeedtestServersGet200ResponseServerInner.md) |  | [optional] 
**upload_speed** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_speedtest_post200_response_result import V1DiagnosticSpeedtestPost200ResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticSpeedtestPost200ResponseResult from a JSON string
v1_diagnostic_speedtest_post200_response_result_instance = V1DiagnosticSpeedtestPost200ResponseResult.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticSpeedtestPost200ResponseResult.to_json())

# convert the object into a dict
v1_diagnostic_speedtest_post200_response_result_dict = v1_diagnostic_speedtest_post200_response_result_instance.to_dict()
# create an instance of V1DiagnosticSpeedtestPost200ResponseResult from a dict
v1_diagnostic_speedtest_post200_response_result_from_dict = V1DiagnosticSpeedtestPost200ResponseResult.from_dict(v1_diagnostic_speedtest_post200_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


