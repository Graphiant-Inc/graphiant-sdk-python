# V1EnterprisesPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** |  | [optional] 
**admin_email** | **str** |  | [optional] 
**admin_first_name** | **str** |  | [optional] 
**admin_last_name** | **str** |  | [optional] 
**admin_time_zone** | **str** |  | [optional] 
**cloud_provider** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**credit_limit** | **int** |  | [optional] 
**logo** | **str** |  | [optional] 
**small_logo** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprises_put_request import V1EnterprisesPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterprisesPutRequest from a JSON string
v1_enterprises_put_request_instance = V1EnterprisesPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1EnterprisesPutRequest.to_json())

# convert the object into a dict
v1_enterprises_put_request_dict = v1_enterprises_put_request_instance.to_dict()
# create an instance of V1EnterprisesPutRequest from a dict
v1_enterprises_put_request_from_dict = V1EnterprisesPutRequest.from_dict(v1_enterprises_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


