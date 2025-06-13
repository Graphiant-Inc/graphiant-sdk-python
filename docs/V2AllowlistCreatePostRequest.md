# V2AllowlistCreatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** |  | [optional] 
**note_text** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_allowlist_create_post_request import V2AllowlistCreatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AllowlistCreatePostRequest from a JSON string
v2_allowlist_create_post_request_instance = V2AllowlistCreatePostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AllowlistCreatePostRequest.to_json())

# convert the object into a dict
v2_allowlist_create_post_request_dict = v2_allowlist_create_post_request_instance.to_dict()
# create an instance of V2AllowlistCreatePostRequest from a dict
v2_allowlist_create_post_request_from_dict = V2AllowlistCreatePostRequest.from_dict(v2_allowlist_create_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


