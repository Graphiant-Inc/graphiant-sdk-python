# V2MonitoringFecStatsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_repair_level** | **float** |  | [optional] 
**effective_qoe** | **float** |  | [optional] 
**rx_repair_level_histogram** | [**StatsmonV2FecRxRepairLevel**](StatsmonV2FecRxRepairLevel.md) |  | [optional] 
**rx_stats** | [**StatsmonV2FecRxStats**](StatsmonV2FecRxStats.md) |  | [optional] 
**tx_repair_level_histogram** | [**StatsmonV2FecTxRepairLevel**](StatsmonV2FecTxRepairLevel.md) |  | [optional] 
**tx_stats** | [**StatsmonV2FecTxStats**](StatsmonV2FecTxStats.md) |  | [optional] 
**unrepairable_rate** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_fec_stats_get_response import V2MonitoringFecStatsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringFecStatsGetResponse from a JSON string
v2_monitoring_fec_stats_get_response_instance = V2MonitoringFecStatsGetResponse.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringFecStatsGetResponse.to_json())

# convert the object into a dict
v2_monitoring_fec_stats_get_response_dict = v2_monitoring_fec_stats_get_response_instance.to_dict()
# create an instance of V2MonitoringFecStatsGetResponse from a dict
v2_monitoring_fec_stats_get_response_from_dict = V2MonitoringFecStatsGetResponse.from_dict(v2_monitoring_fec_stats_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


