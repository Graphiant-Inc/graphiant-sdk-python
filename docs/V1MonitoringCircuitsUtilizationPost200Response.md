# V1MonitoringCircuitsUtilizationPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuit_utilization** | [**List[V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner]**](V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_monitoring_circuits_utilization_post200_response import V1MonitoringCircuitsUtilizationPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1MonitoringCircuitsUtilizationPost200Response from a JSON string
v1_monitoring_circuits_utilization_post200_response_instance = V1MonitoringCircuitsUtilizationPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1MonitoringCircuitsUtilizationPost200Response.to_json())

# convert the object into a dict
v1_monitoring_circuits_utilization_post200_response_dict = v1_monitoring_circuits_utilization_post200_response_instance.to_dict()
# create an instance of V1MonitoringCircuitsUtilizationPost200Response from a dict
v1_monitoring_circuits_utilization_post200_response_from_dict = V1MonitoringCircuitsUtilizationPost200Response.from_dict(v1_monitoring_circuits_utilization_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


