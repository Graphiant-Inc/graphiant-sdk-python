# V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assurance_bucket** | **str** |  | [optional] 
**bucket_color** | **str** |  | [optional] 
**bucket_name_to_display** | **str** |  | [optional] 
**bucket_stats** | [**V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInnerBucketStats**](V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInnerBucketStats.md) |  | [optional] 
**child_bucket_list** | **List[str]** |  | [optional] 
**child_bucket_stats_list** | [**List[V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInnerChildBucketStatsListInner]**](V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInnerChildBucketStatsListInner.md) |  | [optional] 
**is_root** | **bool** |  | [optional] 
**is_terminal** | **bool** |  | [optional] 
**parent_bucket_list** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_applicationprofilesummary_post200_response_application_profile_summary_bucket_summary_list_inner import V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInner from a JSON string
v2_assurance_applicationprofilesummary_post200_response_application_profile_summary_bucket_summary_list_inner_instance = V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInner.to_json())

# convert the object into a dict
v2_assurance_applicationprofilesummary_post200_response_application_profile_summary_bucket_summary_list_inner_dict = v2_assurance_applicationprofilesummary_post200_response_application_profile_summary_bucket_summary_list_inner_instance.to_dict()
# create an instance of V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInner from a dict
v2_assurance_applicationprofilesummary_post200_response_application_profile_summary_bucket_summary_list_inner_from_dict = V2AssuranceApplicationprofilesummaryPost200ResponseApplicationProfileSummaryBucketSummaryListInner.from_dict(v2_assurance_applicationprofilesummary_post200_response_application_profile_summary_bucket_summary_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


