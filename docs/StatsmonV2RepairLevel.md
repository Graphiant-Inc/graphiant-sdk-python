# StatsmonV2RepairLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample** | [**StatsmonV2StatsSample**](StatsmonV2StatsSample.md) |  | [optional] 
**score** | [**StatsmonV2RepairLevelScore**](StatsmonV2RepairLevelScore.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.statsmon_v2_repair_level import StatsmonV2RepairLevel

# TODO update the JSON string below
json = "{}"
# create an instance of StatsmonV2RepairLevel from a JSON string
statsmon_v2_repair_level_instance = StatsmonV2RepairLevel.from_json(json)
# print the JSON string representation of the object
print(StatsmonV2RepairLevel.to_json())

# convert the object into a dict
statsmon_v2_repair_level_dict = statsmon_v2_repair_level_instance.to_dict()
# create an instance of StatsmonV2RepairLevel from a dict
statsmon_v2_repair_level_from_dict = StatsmonV2RepairLevel.from_dict(statsmon_v2_repair_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


