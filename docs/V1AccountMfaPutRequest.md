# V1AccountMfaPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_account_mfa_put_request import V1AccountMfaPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AccountMfaPutRequest from a JSON string
v1_account_mfa_put_request_instance = V1AccountMfaPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1AccountMfaPutRequest.to_json())

# convert the object into a dict
v1_account_mfa_put_request_dict = v1_account_mfa_put_request_instance.to_dict()
# create an instance of V1AccountMfaPutRequest from a dict
v1_account_mfa_put_request_from_dict = V1AccountMfaPutRequest.from_dict(v1_account_mfa_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


