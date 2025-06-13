# V1AccountEmailPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_account_email_patch_request import V1AccountEmailPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AccountEmailPatchRequest from a JSON string
v1_account_email_patch_request_instance = V1AccountEmailPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1AccountEmailPatchRequest.to_json())

# convert the object into a dict
v1_account_email_patch_request_dict = v1_account_email_patch_request_instance.to_dict()
# create an instance of V1AccountEmailPatchRequest from a dict
v1_account_email_patch_request_from_dict = V1AccountEmailPatchRequest.from_dict(v1_account_email_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


