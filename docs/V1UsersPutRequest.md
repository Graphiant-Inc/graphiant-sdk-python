# V1UsersPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_users_put_request import V1UsersPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UsersPutRequest from a JSON string
v1_users_put_request_instance = V1UsersPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1UsersPutRequest.to_json())

# convert the object into a dict
v1_users_put_request_dict = v1_users_put_request_instance.to_dict()
# create an instance of V1UsersPutRequest from a dict
v1_users_put_request_from_dict = V1UsersPutRequest.from_dict(v1_users_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


