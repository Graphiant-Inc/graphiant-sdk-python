# V1EnterprisesPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_email** | **str** |  | [optional] 
**cloud_provider** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**credit_limit** | **int** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**impersonation_enabled** | **bool** |  | [optional] 
**logo** | **str** |  | [optional] 
**portal_banner** | **str** |  | [optional] 
**small_logo** | **str** |  | [optional] 
**token_expiry** | [**V1EnterprisesPatchRequestTokenExpiry**](V1EnterprisesPatchRequestTokenExpiry.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprises_patch_request import V1EnterprisesPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterprisesPatchRequest from a JSON string
v1_enterprises_patch_request_instance = V1EnterprisesPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1EnterprisesPatchRequest.to_json())

# convert the object into a dict
v1_enterprises_patch_request_dict = v1_enterprises_patch_request_instance.to_dict()
# create an instance of V1EnterprisesPatchRequest from a dict
v1_enterprises_patch_request_from_dict = V1EnterprisesPatchRequest.from_dict(v1_enterprises_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


