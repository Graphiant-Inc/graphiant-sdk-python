# V1PolicyRouteTagSetsTagsSummaryGet200ResponseTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_count** | **int** |  | [optional] 
**level_one** | **int** |  | [optional] 
**level_one_tag** | **str** |  | [optional] 
**level_two** | **int** |  | [optional] 
**level_two_tag** | **str** |  | [optional] 
**level_zero** | **int** |  | [optional] 
**level_zero_tag** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_policy_route_tag_sets_tags_summary_get200_response_tags_inner import V1PolicyRouteTagSetsTagsSummaryGet200ResponseTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1PolicyRouteTagSetsTagsSummaryGet200ResponseTagsInner from a JSON string
v1_policy_route_tag_sets_tags_summary_get200_response_tags_inner_instance = V1PolicyRouteTagSetsTagsSummaryGet200ResponseTagsInner.from_json(json)
# print the JSON string representation of the object
print(V1PolicyRouteTagSetsTagsSummaryGet200ResponseTagsInner.to_json())

# convert the object into a dict
v1_policy_route_tag_sets_tags_summary_get200_response_tags_inner_dict = v1_policy_route_tag_sets_tags_summary_get200_response_tags_inner_instance.to_dict()
# create an instance of V1PolicyRouteTagSetsTagsSummaryGet200ResponseTagsInner from a dict
v1_policy_route_tag_sets_tags_summary_get200_response_tags_inner_from_dict = V1PolicyRouteTagSetsTagsSummaryGet200ResponseTagsInner.from_dict(v1_policy_route_tag_sets_tags_summary_get200_response_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


