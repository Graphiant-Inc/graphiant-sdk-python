# V1DiagnosticGnmiPingGet200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**rtt** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**tt_device_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_gnmi_ping_get200_response_results_inner import V1DiagnosticGnmiPingGet200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticGnmiPingGet200ResponseResultsInner from a JSON string
v1_diagnostic_gnmi_ping_get200_response_results_inner_instance = V1DiagnosticGnmiPingGet200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticGnmiPingGet200ResponseResultsInner.to_json())

# convert the object into a dict
v1_diagnostic_gnmi_ping_get200_response_results_inner_dict = v1_diagnostic_gnmi_ping_get200_response_results_inner_instance.to_dict()
# create an instance of V1DiagnosticGnmiPingGet200ResponseResultsInner from a dict
v1_diagnostic_gnmi_ping_get200_response_results_inner_from_dict = V1DiagnosticGnmiPingGet200ResponseResultsInner.from_dict(v1_diagnostic_gnmi_ping_get200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


