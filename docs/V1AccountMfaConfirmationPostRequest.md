# V1AccountMfaConfirmationPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**confirmed** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_account_mfa_confirmation_post_request import V1AccountMfaConfirmationPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AccountMfaConfirmationPostRequest from a JSON string
v1_account_mfa_confirmation_post_request_instance = V1AccountMfaConfirmationPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AccountMfaConfirmationPostRequest.to_json())

# convert the object into a dict
v1_account_mfa_confirmation_post_request_dict = v1_account_mfa_confirmation_post_request_instance.to_dict()
# create an instance of V1AccountMfaConfirmationPostRequest from a dict
v1_account_mfa_confirmation_post_request_from_dict = V1AccountMfaConfirmationPostRequest.from_dict(v1_account_mfa_confirmation_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


