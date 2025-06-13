# V1GroupsGet200ResponseGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**enterprise_ids** | **List[int]** |  | [optional] 
**group_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | [**V1GroupsGet200ResponseGroupsInnerPermissions**](V1GroupsGet200ResponseGroupsInnerPermissions.md) |  | [optional] 
**time_window_end** | **int** |  | [optional] 
**time_window_start** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_groups_get200_response_groups_inner import V1GroupsGet200ResponseGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GroupsGet200ResponseGroupsInner from a JSON string
v1_groups_get200_response_groups_inner_instance = V1GroupsGet200ResponseGroupsInner.from_json(json)
# print the JSON string representation of the object
print(V1GroupsGet200ResponseGroupsInner.to_json())

# convert the object into a dict
v1_groups_get200_response_groups_inner_dict = v1_groups_get200_response_groups_inner_instance.to_dict()
# create an instance of V1GroupsGet200ResponseGroupsInner from a dict
v1_groups_get200_response_groups_inner_from_dict = V1GroupsGet200ResponseGroupsInner.from_dict(v1_groups_get200_response_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


