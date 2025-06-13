# V1EnterprisesPatchRequestTokenExpiry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** |  | [optional] 
**time_unit** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprises_patch_request_token_expiry import V1EnterprisesPatchRequestTokenExpiry

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterprisesPatchRequestTokenExpiry from a JSON string
v1_enterprises_patch_request_token_expiry_instance = V1EnterprisesPatchRequestTokenExpiry.from_json(json)
# print the JSON string representation of the object
print(V1EnterprisesPatchRequestTokenExpiry.to_json())

# convert the object into a dict
v1_enterprises_patch_request_token_expiry_dict = v1_enterprises_patch_request_token_expiry_instance.to_dict()
# create an instance of V1EnterprisesPatchRequestTokenExpiry from a dict
v1_enterprises_patch_request_token_expiry_from_dict = V1EnterprisesPatchRequestTokenExpiry.from_dict(v1_enterprises_patch_request_token_expiry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


