# V1AuthPut204Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_users** | **List[str]** |  | [optional] 
**all_groups** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_auth_put204_response import V1AuthPut204Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuthPut204Response from a JSON string
v1_auth_put204_response_instance = V1AuthPut204Response.from_json(json)
# print the JSON string representation of the object
print(V1AuthPut204Response.to_json())

# convert the object into a dict
v1_auth_put204_response_dict = v1_auth_put204_response_instance.to_dict()
# create an instance of V1AuthPut204Response from a dict
v1_auth_put204_response_from_dict = V1AuthPut204Response.from_dict(v1_auth_put204_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


