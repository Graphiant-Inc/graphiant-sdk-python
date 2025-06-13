# V1PolicyRouteTagSetsTagsSummaryGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[V1PolicyRouteTagSetsTagsSummaryGet200ResponseTagsInner]**](V1PolicyRouteTagSetsTagsSummaryGet200ResponseTagsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_policy_route_tag_sets_tags_summary_get200_response import V1PolicyRouteTagSetsTagsSummaryGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1PolicyRouteTagSetsTagsSummaryGet200Response from a JSON string
v1_policy_route_tag_sets_tags_summary_get200_response_instance = V1PolicyRouteTagSetsTagsSummaryGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1PolicyRouteTagSetsTagsSummaryGet200Response.to_json())

# convert the object into a dict
v1_policy_route_tag_sets_tags_summary_get200_response_dict = v1_policy_route_tag_sets_tags_summary_get200_response_instance.to_dict()
# create an instance of V1PolicyRouteTagSetsTagsSummaryGet200Response from a dict
v1_policy_route_tag_sets_tags_summary_get200_response_from_dict = V1PolicyRouteTagSetsTagsSummaryGet200Response.from_dict(v1_policy_route_tag_sets_tags_summary_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


