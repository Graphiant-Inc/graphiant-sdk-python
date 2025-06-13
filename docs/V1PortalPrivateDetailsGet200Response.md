# V1PortalPrivateDetailsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[V1PortalPrivatePostRequestDetails]**](V1PortalPrivatePostRequestDetails.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_portal_private_details_get200_response import V1PortalPrivateDetailsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1PortalPrivateDetailsGet200Response from a JSON string
v1_portal_private_details_get200_response_instance = V1PortalPrivateDetailsGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1PortalPrivateDetailsGet200Response.to_json())

# convert the object into a dict
v1_portal_private_details_get200_response_dict = v1_portal_private_details_get200_response_instance.to_dict()
# create an instance of V1PortalPrivateDetailsGet200Response from a dict
v1_portal_private_details_get200_response_from_dict = V1PortalPrivateDetailsGet200Response.from_dict(v1_portal_private_details_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


