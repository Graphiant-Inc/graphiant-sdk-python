# V1InvitationEmailPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_email** | **str** |  | [optional] 
**customer_id** | **int** |  | [optional] 
**customer_name** | **str** |  (required) | 
**is_graphiant** | **bool** |  | [optional] 
**match_id** | **int** |  (required) | 
**service_id** | **int** |  (required) | 
**service_name** | **str** |  (required) | 
**service_type** | **str** | Extranet service type URL segment (e.g. peering_service, client_to_server) | [optional] 

## Example

```python
from graphiant_sdk.models.v1_invitation_email_post_request import V1InvitationEmailPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1InvitationEmailPostRequest from a JSON string
v1_invitation_email_post_request_instance = V1InvitationEmailPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1InvitationEmailPostRequest.to_json())

# convert the object into a dict
v1_invitation_email_post_request_dict = v1_invitation_email_post_request_instance.to_dict()
# create an instance of V1InvitationEmailPostRequest from a dict
v1_invitation_email_post_request_from_dict = V1InvitationEmailPostRequest.from_dict(v1_invitation_email_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


