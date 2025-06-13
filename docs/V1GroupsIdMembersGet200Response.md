# V1GroupsIdMembersGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[V1GroupsIdMembersGet200ResponseUsersInner]**](V1GroupsIdMembersGet200ResponseUsersInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_groups_id_members_get200_response import V1GroupsIdMembersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1GroupsIdMembersGet200Response from a JSON string
v1_groups_id_members_get200_response_instance = V1GroupsIdMembersGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1GroupsIdMembersGet200Response.to_json())

# convert the object into a dict
v1_groups_id_members_get200_response_dict = v1_groups_id_members_get200_response_instance.to_dict()
# create an instance of V1GroupsIdMembersGet200Response from a dict
v1_groups_id_members_get200_response_from_dict = V1GroupsIdMembersGet200Response.from_dict(v1_groups_id_members_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


