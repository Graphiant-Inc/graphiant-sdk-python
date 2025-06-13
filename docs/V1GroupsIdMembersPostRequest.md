# V1GroupsIdMembersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_ids** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_groups_id_members_post_request import V1GroupsIdMembersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GroupsIdMembersPostRequest from a JSON string
v1_groups_id_members_post_request_instance = V1GroupsIdMembersPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GroupsIdMembersPostRequest.to_json())

# convert the object into a dict
v1_groups_id_members_post_request_dict = v1_groups_id_members_post_request_instance.to_dict()
# create an instance of V1GroupsIdMembersPostRequest from a dict
v1_groups_id_members_post_request_from_dict = V1GroupsIdMembersPostRequest.from_dict(v1_groups_id_members_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


