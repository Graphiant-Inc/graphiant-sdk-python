# V1AuthLoginPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** |  | [optional] 
**auth** | **bool** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_auth_login_post200_response import V1AuthLoginPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuthLoginPost200Response from a JSON string
v1_auth_login_post200_response_instance = V1AuthLoginPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1AuthLoginPost200Response.to_json())

# convert the object into a dict
v1_auth_login_post200_response_dict = v1_auth_login_post200_response_instance.to_dict()
# create an instance of V1AuthLoginPost200Response from a dict
v1_auth_login_post200_response_from_dict = V1AuthLoginPost200Response.from_dict(v1_auth_login_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


