# V1PortalPrivatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**V1PortalPrivatePostRequestDetails**](V1PortalPrivatePostRequestDetails.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_portal_private_post_request import V1PortalPrivatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1PortalPrivatePostRequest from a JSON string
v1_portal_private_post_request_instance = V1PortalPrivatePostRequest.from_json(json)
# print the JSON string representation of the object
print(V1PortalPrivatePostRequest.to_json())

# convert the object into a dict
v1_portal_private_post_request_dict = v1_portal_private_post_request_instance.to_dict()
# create an instance of V1PortalPrivatePostRequest from a dict
v1_portal_private_post_request_from_dict = V1PortalPrivatePostRequest.from_dict(v1_portal_private_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


