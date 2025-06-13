# V1MonitoringCircuitsSummaryPost200ResponseSummariesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_status** | **bool** |  | [optional] 
**average_link_down_speed_kbps** | **float** |  | [optional] 
**average_link_up_speed_kbps** | **float** |  | [optional] 
**avg_mos** | **float** |  | [optional] 
**config_link_down_speed_mbps** | **int** |  | [optional] 
**config_link_up_speed_mbps** | **int** |  | [optional] 
**connection_status** | **str** |  | [optional] 
**current_link_down_speed_kbps** | **float** |  | [optional] 
**current_link_up_speed_kbps** | **float** |  | [optional] 
**delay** | **int** |  | [optional] 
**jitter** | **int** |  | [optional] 
**loss** | **float** |  | [optional] 
**mos** | **float** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_monitoring_circuits_summary_post200_response_summaries_inner import V1MonitoringCircuitsSummaryPost200ResponseSummariesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1MonitoringCircuitsSummaryPost200ResponseSummariesInner from a JSON string
v1_monitoring_circuits_summary_post200_response_summaries_inner_instance = V1MonitoringCircuitsSummaryPost200ResponseSummariesInner.from_json(json)
# print the JSON string representation of the object
print(V1MonitoringCircuitsSummaryPost200ResponseSummariesInner.to_json())

# convert the object into a dict
v1_monitoring_circuits_summary_post200_response_summaries_inner_dict = v1_monitoring_circuits_summary_post200_response_summaries_inner_instance.to_dict()
# create an instance of V1MonitoringCircuitsSummaryPost200ResponseSummariesInner from a dict
v1_monitoring_circuits_summary_post200_response_summaries_inner_from_dict = V1MonitoringCircuitsSummaryPost200ResponseSummariesInner.from_dict(v1_monitoring_circuits_summary_post200_response_summaries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


