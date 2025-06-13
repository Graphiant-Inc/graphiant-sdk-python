# V2MonitoringCircuitsUtilizationPost200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_link_up_speed_mbps** | **int** |  | [optional] 
**queue_utilization** | [**List[V2MonitoringCircuitsUtilizationPost200ResponseDataInnerQueueUtilizationInner]**](V2MonitoringCircuitsUtilizationPost200ResponseDataInnerQueueUtilizationInner.md) |  | [optional] 
**selector** | [**V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionLocalDiaLinksInner**](V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionLocalDiaLinksInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_circuits_utilization_post200_response_data_inner import V2MonitoringCircuitsUtilizationPost200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringCircuitsUtilizationPost200ResponseDataInner from a JSON string
v2_monitoring_circuits_utilization_post200_response_data_inner_instance = V2MonitoringCircuitsUtilizationPost200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringCircuitsUtilizationPost200ResponseDataInner.to_json())

# convert the object into a dict
v2_monitoring_circuits_utilization_post200_response_data_inner_dict = v2_monitoring_circuits_utilization_post200_response_data_inner_instance.to_dict()
# create an instance of V2MonitoringCircuitsUtilizationPost200ResponseDataInner from a dict
v2_monitoring_circuits_utilization_post200_response_data_inner_from_dict = V2MonitoringCircuitsUtilizationPost200ResponseDataInner.from_dict(v2_monitoring_circuits_utilization_post200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


