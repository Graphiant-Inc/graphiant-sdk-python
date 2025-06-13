# V1DiagnosticSpeedtestServersGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | [**List[V1DiagnosticSpeedtestServersGet200ResponseServerInner]**](V1DiagnosticSpeedtestServersGet200ResponseServerInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_speedtest_servers_get200_response import V1DiagnosticSpeedtestServersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticSpeedtestServersGet200Response from a JSON string
v1_diagnostic_speedtest_servers_get200_response_instance = V1DiagnosticSpeedtestServersGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticSpeedtestServersGet200Response.to_json())

# convert the object into a dict
v1_diagnostic_speedtest_servers_get200_response_dict = v1_diagnostic_speedtest_servers_get200_response_instance.to_dict()
# create an instance of V1DiagnosticSpeedtestServersGet200Response from a dict
v1_diagnostic_speedtest_servers_get200_response_from_dict = V1DiagnosticSpeedtestServersGet200Response.from_dict(v1_diagnostic_speedtest_servers_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


