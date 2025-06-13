# V1BwtrackerRegionSiteSummaryPost200ResponseBwusageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bwuage_region** | [**List[V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetailsBwusageRegionInner]**](V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetailsBwusageRegionInner.md) |  | [optional] 
**edge_count** | **int** |  | [optional] 
**provider_count** | **int** |  | [optional] 
**usage_kbps** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_bwtracker_region_site_summary_post200_response_bwusage_summary import V1BwtrackerRegionSiteSummaryPost200ResponseBwusageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V1BwtrackerRegionSiteSummaryPost200ResponseBwusageSummary from a JSON string
v1_bwtracker_region_site_summary_post200_response_bwusage_summary_instance = V1BwtrackerRegionSiteSummaryPost200ResponseBwusageSummary.from_json(json)
# print the JSON string representation of the object
print(V1BwtrackerRegionSiteSummaryPost200ResponseBwusageSummary.to_json())

# convert the object into a dict
v1_bwtracker_region_site_summary_post200_response_bwusage_summary_dict = v1_bwtracker_region_site_summary_post200_response_bwusage_summary_instance.to_dict()
# create an instance of V1BwtrackerRegionSiteSummaryPost200ResponseBwusageSummary from a dict
v1_bwtracker_region_site_summary_post200_response_bwusage_summary_from_dict = V1BwtrackerRegionSiteSummaryPost200ResponseBwusageSummary.from_dict(v1_bwtracker_region_site_summary_post200_response_bwusage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


