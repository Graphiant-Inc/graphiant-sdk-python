# StatsmonV2FecRxStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**erasure_recovered_packets** | **int** |  | [optional] 
**erasure_unrepairable_packets** | **int** |  | [optional] 
**repair_level** | **float** |  | [optional] 
**repair_packets** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.statsmon_v2_fec_rx_stats import StatsmonV2FecRxStats

# TODO update the JSON string below
json = "{}"
# create an instance of StatsmonV2FecRxStats from a JSON string
statsmon_v2_fec_rx_stats_instance = StatsmonV2FecRxStats.from_json(json)
# print the JSON string representation of the object
print(StatsmonV2FecRxStats.to_json())

# convert the object into a dict
statsmon_v2_fec_rx_stats_dict = statsmon_v2_fec_rx_stats_instance.to_dict()
# create an instance of StatsmonV2FecRxStats from a dict
statsmon_v2_fec_rx_stats_from_dict = StatsmonV2FecRxStats.from_dict(statsmon_v2_fec_rx_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


