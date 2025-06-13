# V1AppsBandwidthPost200ResponseStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dl_bw** | **float** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**ul_bw** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_apps_bandwidth_post200_response_stats_inner import V1AppsBandwidthPost200ResponseStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppsBandwidthPost200ResponseStatsInner from a JSON string
v1_apps_bandwidth_post200_response_stats_inner_instance = V1AppsBandwidthPost200ResponseStatsInner.from_json(json)
# print the JSON string representation of the object
print(V1AppsBandwidthPost200ResponseStatsInner.to_json())

# convert the object into a dict
v1_apps_bandwidth_post200_response_stats_inner_dict = v1_apps_bandwidth_post200_response_stats_inner_instance.to_dict()
# create an instance of V1AppsBandwidthPost200ResponseStatsInner from a dict
v1_apps_bandwidth_post200_response_stats_inner_from_dict = V1AppsBandwidthPost200ResponseStatsInner.from_dict(v1_apps_bandwidth_post200_response_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


