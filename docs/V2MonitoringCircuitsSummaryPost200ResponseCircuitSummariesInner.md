# V2MonitoringCircuitsSummaryPost200ResponseCircuitSummariesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_delay** | **float** |  | [optional] 
**average_jitter** | **float** |  | [optional] 
**average_link_down_speed_kbps** | **float** |  | [optional] 
**average_link_up_speed_kbps** | **float** |  | [optional] 
**average_loss** | **float** |  | [optional] 
**avg_mos** | **float** |  | [optional] 
**circuit_name** | **str** |  | [optional] 
**config_link_down_speed_mbps** | **int** |  | [optional] 
**config_link_up_speed_mbps** | **int** |  | [optional] 
**connection_status** | **str** |  | [optional] 
**current_link_down_speed_kbps** | **float** |  | [optional] 
**current_link_up_speed_kbps** | **float** |  | [optional] 
**delay** | **int** |  | [optional] 
**jitter** | **int** |  | [optional] 
**last_resort** | **bool** |  | [optional] 
**loss** | **float** |  | [optional] 
**max_delay** | **float** |  | [optional] 
**max_jitter** | **float** |  | [optional] 
**max_loss** | **float** |  | [optional] 
**max_mos** | **float** |  | [optional] 
**min_delay** | **float** |  | [optional] 
**min_jitter** | **float** |  | [optional] 
**min_loss** | **float** |  | [optional] 
**min_mos** | **float** |  | [optional] 
**mos** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_circuits_summary_post200_response_circuit_summaries_inner import V2MonitoringCircuitsSummaryPost200ResponseCircuitSummariesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringCircuitsSummaryPost200ResponseCircuitSummariesInner from a JSON string
v2_monitoring_circuits_summary_post200_response_circuit_summaries_inner_instance = V2MonitoringCircuitsSummaryPost200ResponseCircuitSummariesInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringCircuitsSummaryPost200ResponseCircuitSummariesInner.to_json())

# convert the object into a dict
v2_monitoring_circuits_summary_post200_response_circuit_summaries_inner_dict = v2_monitoring_circuits_summary_post200_response_circuit_summaries_inner_instance.to_dict()
# create an instance of V2MonitoringCircuitsSummaryPost200ResponseCircuitSummariesInner from a dict
v2_monitoring_circuits_summary_post200_response_circuit_summaries_inner_from_dict = V2MonitoringCircuitsSummaryPost200ResponseCircuitSummariesInner.from_dict(v2_monitoring_circuits_summary_post200_response_circuit_summaries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


