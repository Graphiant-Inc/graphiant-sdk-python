# V1AccountMfaPut200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**qr_code** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_account_mfa_put200_response import V1AccountMfaPut200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AccountMfaPut200Response from a JSON string
v1_account_mfa_put200_response_instance = V1AccountMfaPut200Response.from_json(json)
# print the JSON string representation of the object
print(V1AccountMfaPut200Response.to_json())

# convert the object into a dict
v1_account_mfa_put200_response_dict = v1_account_mfa_put200_response_instance.to_dict()
# create an instance of V1AccountMfaPut200Response from a dict
v1_account_mfa_put200_response_from_dict = V1AccountMfaPut200Response.from_dict(v1_account_mfa_put200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


