# V2MonitoringCircuitsUtilizationPost200ResponseDataInnerQueueUtilizationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_pct** | **int** |  | [optional] 
**default_queue** | **bool** |  | [optional] 
**excess_weight** | **int** |  | [optional] 
**sla_class** | **str** |  | [optional] 
**utilization_kbps** | **float** |  | [optional] 
**utilization_pct** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_circuits_utilization_post200_response_data_inner_queue_utilization_inner import V2MonitoringCircuitsUtilizationPost200ResponseDataInnerQueueUtilizationInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringCircuitsUtilizationPost200ResponseDataInnerQueueUtilizationInner from a JSON string
v2_monitoring_circuits_utilization_post200_response_data_inner_queue_utilization_inner_instance = V2MonitoringCircuitsUtilizationPost200ResponseDataInnerQueueUtilizationInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringCircuitsUtilizationPost200ResponseDataInnerQueueUtilizationInner.to_json())

# convert the object into a dict
v2_monitoring_circuits_utilization_post200_response_data_inner_queue_utilization_inner_dict = v2_monitoring_circuits_utilization_post200_response_data_inner_queue_utilization_inner_instance.to_dict()
# create an instance of V2MonitoringCircuitsUtilizationPost200ResponseDataInnerQueueUtilizationInner from a dict
v2_monitoring_circuits_utilization_post200_response_data_inner_queue_utilization_inner_from_dict = V2MonitoringCircuitsUtilizationPost200ResponseDataInnerQueueUtilizationInner.from_dict(v2_monitoring_circuits_utilization_post200_response_data_inner_queue_utilization_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


