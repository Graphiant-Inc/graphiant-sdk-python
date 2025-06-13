# V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_usage** | **float** |  | [optional] 
**peak_usage** | **float** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_extranet_service_overtime_consumption_post200_response_dl_agg_stats_inner import V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner from a JSON string
v2_extranet_service_overtime_consumption_post200_response_dl_agg_stats_inner_instance = V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner.from_json(json)
# print the JSON string representation of the object
print(V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner.to_json())

# convert the object into a dict
v2_extranet_service_overtime_consumption_post200_response_dl_agg_stats_inner_dict = v2_extranet_service_overtime_consumption_post200_response_dl_agg_stats_inner_instance.to_dict()
# create an instance of V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner from a dict
v2_extranet_service_overtime_consumption_post200_response_dl_agg_stats_inner_from_dict = V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner.from_dict(v2_extranet_service_overtime_consumption_post200_response_dl_agg_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


