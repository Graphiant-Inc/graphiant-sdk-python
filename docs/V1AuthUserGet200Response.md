# V1AuthUserGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**role** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**enterprise_name** | **str** |  | [optional] 
**auth** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_auth_user_get200_response import V1AuthUserGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuthUserGet200Response from a JSON string
v1_auth_user_get200_response_instance = V1AuthUserGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1AuthUserGet200Response.to_json())

# convert the object into a dict
v1_auth_user_get200_response_dict = v1_auth_user_get200_response_instance.to_dict()
# create an instance of V1AuthUserGet200Response from a dict
v1_auth_user_get200_response_from_dict = V1AuthUserGet200Response.from_dict(v1_auth_user_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


