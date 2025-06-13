# V1DiagnosticGnmiPingGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[V1DiagnosticGnmiPingGet200ResponseResultsInner]**](V1DiagnosticGnmiPingGet200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_gnmi_ping_get200_response import V1DiagnosticGnmiPingGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticGnmiPingGet200Response from a JSON string
v1_diagnostic_gnmi_ping_get200_response_instance = V1DiagnosticGnmiPingGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticGnmiPingGet200Response.to_json())

# convert the object into a dict
v1_diagnostic_gnmi_ping_get200_response_dict = v1_diagnostic_gnmi_ping_get200_response_instance.to_dict()
# create an instance of V1DiagnosticGnmiPingGet200Response from a dict
v1_diagnostic_gnmi_ping_get200_response_from_dict = V1DiagnosticGnmiPingGet200Response.from_dict(v1_diagnostic_gnmi_ping_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


