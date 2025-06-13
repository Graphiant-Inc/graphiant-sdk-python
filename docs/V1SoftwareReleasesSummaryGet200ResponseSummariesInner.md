# V1SoftwareReleasesSummaryGet200ResponseSummariesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**V1SoftwareReleasesSummaryGet200ResponseSummariesInnerKey**](V1SoftwareReleasesSummaryGet200ResponseSummariesInnerKey.md) |  | [optional] 
**name** | **str** |  | [optional] 
**release** | **str** |  | [optional] 
**release_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_software_releases_summary_get200_response_summaries_inner import V1SoftwareReleasesSummaryGet200ResponseSummariesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1SoftwareReleasesSummaryGet200ResponseSummariesInner from a JSON string
v1_software_releases_summary_get200_response_summaries_inner_instance = V1SoftwareReleasesSummaryGet200ResponseSummariesInner.from_json(json)
# print the JSON string representation of the object
print(V1SoftwareReleasesSummaryGet200ResponseSummariesInner.to_json())

# convert the object into a dict
v1_software_releases_summary_get200_response_summaries_inner_dict = v1_software_releases_summary_get200_response_summaries_inner_instance.to_dict()
# create an instance of V1SoftwareReleasesSummaryGet200ResponseSummariesInner from a dict
v1_software_releases_summary_get200_response_summaries_inner_from_dict = V1SoftwareReleasesSummaryGet200ResponseSummariesInner.from_dict(v1_software_releases_summary_get200_response_summaries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


