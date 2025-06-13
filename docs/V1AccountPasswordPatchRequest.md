# V1AccountPasswordPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_account_password_patch_request import V1AccountPasswordPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AccountPasswordPatchRequest from a JSON string
v1_account_password_patch_request_instance = V1AccountPasswordPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1AccountPasswordPatchRequest.to_json())

# convert the object into a dict
v1_account_password_patch_request_dict = v1_account_password_patch_request_instance.to_dict()
# create an instance of V1AccountPasswordPatchRequest from a dict
v1_account_password_patch_request_from_dict = V1AccountPasswordPatchRequest.from_dict(v1_account_password_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


