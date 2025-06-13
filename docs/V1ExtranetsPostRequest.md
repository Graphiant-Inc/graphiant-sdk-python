# V1ExtranetsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**V1ExtranetsPostRequestPolicy**](V1ExtranetsPostRequestPolicy.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_post_request import V1ExtranetsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsPostRequest from a JSON string
v1_extranets_post_request_instance = V1ExtranetsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsPostRequest.to_json())

# convert the object into a dict
v1_extranets_post_request_dict = v1_extranets_post_request_instance.to_dict()
# create an instance of V1ExtranetsPostRequest from a dict
v1_extranets_post_request_from_dict = V1ExtranetsPostRequest.from_dict(v1_extranets_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


