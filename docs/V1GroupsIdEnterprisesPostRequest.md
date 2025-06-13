# V1GroupsIdEnterprisesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise_ids** | **List[int]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_groups_id_enterprises_post_request import V1GroupsIdEnterprisesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GroupsIdEnterprisesPostRequest from a JSON string
v1_groups_id_enterprises_post_request_instance = V1GroupsIdEnterprisesPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GroupsIdEnterprisesPostRequest.to_json())

# convert the object into a dict
v1_groups_id_enterprises_post_request_dict = v1_groups_id_enterprises_post_request_instance.to_dict()
# create an instance of V1GroupsIdEnterprisesPostRequest from a dict
v1_groups_id_enterprises_post_request_from_dict = V1GroupsIdEnterprisesPostRequest.from_dict(v1_groups_id_enterprises_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


