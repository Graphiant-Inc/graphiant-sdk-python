# V1GroupsIdMembersGet200ResponseUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**mfa_factor** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_groups_id_members_get200_response_users_inner import V1GroupsIdMembersGet200ResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GroupsIdMembersGet200ResponseUsersInner from a JSON string
v1_groups_id_members_get200_response_users_inner_instance = V1GroupsIdMembersGet200ResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print(V1GroupsIdMembersGet200ResponseUsersInner.to_json())

# convert the object into a dict
v1_groups_id_members_get200_response_users_inner_dict = v1_groups_id_members_get200_response_users_inner_instance.to_dict()
# create an instance of V1GroupsIdMembersGet200ResponseUsersInner from a dict
v1_groups_id_members_get200_response_users_inner_from_dict = V1GroupsIdMembersGet200ResponseUsersInner.from_dict(v1_groups_id_members_get200_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


