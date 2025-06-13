# V1PolicyRouteTagSetsTagsGet200ResponseTagsInnerNextSetInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**next_set** | [**List[V1PolicyRouteTagSetsTagsGet200ResponseTagsInnerNextSetInnerNextSetInner]**](V1PolicyRouteTagSetsTagsGet200ResponseTagsInnerNextSetInnerNextSetInner.md) |  | [optional] 
**tag** | **str** |  | [optional] 
**tag_value** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_policy_route_tag_sets_tags_get200_response_tags_inner_next_set_inner import V1PolicyRouteTagSetsTagsGet200ResponseTagsInnerNextSetInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1PolicyRouteTagSetsTagsGet200ResponseTagsInnerNextSetInner from a JSON string
v1_policy_route_tag_sets_tags_get200_response_tags_inner_next_set_inner_instance = V1PolicyRouteTagSetsTagsGet200ResponseTagsInnerNextSetInner.from_json(json)
# print the JSON string representation of the object
print(V1PolicyRouteTagSetsTagsGet200ResponseTagsInnerNextSetInner.to_json())

# convert the object into a dict
v1_policy_route_tag_sets_tags_get200_response_tags_inner_next_set_inner_dict = v1_policy_route_tag_sets_tags_get200_response_tags_inner_next_set_inner_instance.to_dict()
# create an instance of V1PolicyRouteTagSetsTagsGet200ResponseTagsInnerNextSetInner from a dict
v1_policy_route_tag_sets_tags_get200_response_tags_inner_next_set_inner_from_dict = V1PolicyRouteTagSetsTagsGet200ResponseTagsInnerNextSetInner.from_dict(v1_policy_route_tag_sets_tags_get200_response_tags_inner_next_set_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


