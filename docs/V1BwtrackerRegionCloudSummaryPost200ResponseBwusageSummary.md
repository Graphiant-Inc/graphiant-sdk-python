# V1BwtrackerRegionCloudSummaryPost200ResponseBwusageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bwusage_top_providers** | [**List[V1BwtrackerRegionCloudSummaryPost200ResponseBwusageSummaryBwusageTopProvidersInner]**](V1BwtrackerRegionCloudSummaryPost200ResponseBwusageSummaryBwusageTopProvidersInner.md) |  | [optional] 
**cloudusage_kbps** | **float** |  | [optional] 
**percent_changed** | **float** |  | [optional] 
**provider_count** | **int** |  | [optional] 
**providerusage_kbps** | **int** |  | [optional] 
**totusage_kbps** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_bwtracker_region_cloud_summary_post200_response_bwusage_summary import V1BwtrackerRegionCloudSummaryPost200ResponseBwusageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V1BwtrackerRegionCloudSummaryPost200ResponseBwusageSummary from a JSON string
v1_bwtracker_region_cloud_summary_post200_response_bwusage_summary_instance = V1BwtrackerRegionCloudSummaryPost200ResponseBwusageSummary.from_json(json)
# print the JSON string representation of the object
print(V1BwtrackerRegionCloudSummaryPost200ResponseBwusageSummary.to_json())

# convert the object into a dict
v1_bwtracker_region_cloud_summary_post200_response_bwusage_summary_dict = v1_bwtracker_region_cloud_summary_post200_response_bwusage_summary_instance.to_dict()
# create an instance of V1BwtrackerRegionCloudSummaryPost200ResponseBwusageSummary from a dict
v1_bwtracker_region_cloud_summary_post200_response_bwusage_summary_from_dict = V1BwtrackerRegionCloudSummaryPost200ResponseBwusageSummary.from_dict(v1_bwtracker_region_cloud_summary_post200_response_bwusage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


