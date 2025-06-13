# V1GroupsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**group_type** | **str** |  | [optional] 
**permissions** | [**V1GroupsGet200ResponseGroupsInnerPermissions**](V1GroupsGet200ResponseGroupsInnerPermissions.md) |  | [optional] 
**time_window_end** | **int** |  | [optional] 
**time_window_start** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_groups_id_patch_request import V1GroupsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GroupsIdPatchRequest from a JSON string
v1_groups_id_patch_request_instance = V1GroupsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1GroupsIdPatchRequest.to_json())

# convert the object into a dict
v1_groups_id_patch_request_dict = v1_groups_id_patch_request_instance.to_dict()
# create an instance of V1GroupsIdPatchRequest from a dict
v1_groups_id_patch_request_from_dict = V1GroupsIdPatchRequest.from_dict(v1_groups_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


