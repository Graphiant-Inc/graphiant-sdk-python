# V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_link_up_speed_mbps** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**queue_utilization** | [**List[V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInnerQueueUtilizationInner]**](V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInnerQueueUtilizationInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_monitoring_circuits_utilization_post200_response_circuit_utilization_inner import V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner from a JSON string
v1_monitoring_circuits_utilization_post200_response_circuit_utilization_inner_instance = V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner.from_json(json)
# print the JSON string representation of the object
print(V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner.to_json())

# convert the object into a dict
v1_monitoring_circuits_utilization_post200_response_circuit_utilization_inner_dict = v1_monitoring_circuits_utilization_post200_response_circuit_utilization_inner_instance.to_dict()
# create an instance of V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner from a dict
v1_monitoring_circuits_utilization_post200_response_circuit_utilization_inner_from_dict = V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner.from_dict(v1_monitoring_circuits_utilization_post200_response_circuit_utilization_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


