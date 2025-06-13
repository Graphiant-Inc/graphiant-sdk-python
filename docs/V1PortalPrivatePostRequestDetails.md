# V1PortalPrivatePostRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**is_disable** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**onboarding_gw_addr** | **str** |  | [optional] 
**portal_url** | **str** |  | [optional] 
**public_portal_url** | **str** |  | [optional] 
**root_ca** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_portal_private_post_request_details import V1PortalPrivatePostRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of V1PortalPrivatePostRequestDetails from a JSON string
v1_portal_private_post_request_details_instance = V1PortalPrivatePostRequestDetails.from_json(json)
# print the JSON string representation of the object
print(V1PortalPrivatePostRequestDetails.to_json())

# convert the object into a dict
v1_portal_private_post_request_details_dict = v1_portal_private_post_request_details_instance.to_dict()
# create an instance of V1PortalPrivatePostRequestDetails from a dict
v1_portal_private_post_request_details_from_dict = V1PortalPrivatePostRequestDetails.from_dict(v1_portal_private_post_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


