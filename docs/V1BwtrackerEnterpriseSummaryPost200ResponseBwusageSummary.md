# V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bwusage_role_summary** | [**List[V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummaryBwusageRoleSummaryInner]**](V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummaryBwusageRoleSummaryInner.md) |  | [optional] 
**bwusage_top_regions** | [**List[V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummaryBwusageTopRegionsInner]**](V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummaryBwusageTopRegionsInner.md) |  | [optional] 
**min_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**percent_changed** | **float** |  | [optional] 
**provider_count** | **int** |  | [optional] 
**region_count** | **int** |  | [optional] 
**site_count** | **int** |  | [optional] 
**usage_kbps** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_bwtracker_enterprise_summary_post200_response_bwusage_summary import V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummary from a JSON string
v1_bwtracker_enterprise_summary_post200_response_bwusage_summary_instance = V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummary.from_json(json)
# print the JSON string representation of the object
print(V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummary.to_json())

# convert the object into a dict
v1_bwtracker_enterprise_summary_post200_response_bwusage_summary_dict = v1_bwtracker_enterprise_summary_post200_response_bwusage_summary_instance.to_dict()
# create an instance of V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummary from a dict
v1_bwtracker_enterprise_summary_post200_response_bwusage_summary_from_dict = V1BwtrackerEnterpriseSummaryPost200ResponseBwusageSummary.from_dict(v1_bwtracker_enterprise_summary_post200_response_bwusage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


