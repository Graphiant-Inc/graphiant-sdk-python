# V1AuthLoginPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_auth_login_post_request import V1AuthLoginPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuthLoginPostRequest from a JSON string
v1_auth_login_post_request_instance = V1AuthLoginPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AuthLoginPostRequest.to_json())

# convert the object into a dict
v1_auth_login_post_request_dict = v1_auth_login_post_request_instance.to_dict()
# create an instance of V1AuthLoginPostRequest from a dict
v1_auth_login_post_request_from_dict = V1AuthLoginPostRequest.from_dict(v1_auth_login_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


