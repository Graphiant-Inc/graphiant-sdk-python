# StatsmonV2FecTxStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protected_packets** | **int** |  | [optional] 
**repair_level** | **float** |  | [optional] 
**sent_repair_packets** | **int** |  | [optional] 
**unprotected_packets** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.statsmon_v2_fec_tx_stats import StatsmonV2FecTxStats

# TODO update the JSON string below
json = "{}"
# create an instance of StatsmonV2FecTxStats from a JSON string
statsmon_v2_fec_tx_stats_instance = StatsmonV2FecTxStats.from_json(json)
# print the JSON string representation of the object
print(StatsmonV2FecTxStats.to_json())

# convert the object into a dict
statsmon_v2_fec_tx_stats_dict = statsmon_v2_fec_tx_stats_instance.to_dict()
# create an instance of StatsmonV2FecTxStats from a dict
statsmon_v2_fec_tx_stats_from_dict = StatsmonV2FecTxStats.from_dict(statsmon_v2_fec_tx_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


