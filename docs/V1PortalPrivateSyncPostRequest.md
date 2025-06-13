# V1PortalPrivateSyncPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcs_name** | **str** |  | [optional] 
**inventory** | [**List[V1PortalPrivateSyncPostRequestInventoryInner]**](V1PortalPrivateSyncPostRequestInventoryInner.md) |  | [optional] 
**is_full_sync** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_portal_private_sync_post_request import V1PortalPrivateSyncPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1PortalPrivateSyncPostRequest from a JSON string
v1_portal_private_sync_post_request_instance = V1PortalPrivateSyncPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1PortalPrivateSyncPostRequest.to_json())

# convert the object into a dict
v1_portal_private_sync_post_request_dict = v1_portal_private_sync_post_request_instance.to_dict()
# create an instance of V1PortalPrivateSyncPostRequest from a dict
v1_portal_private_sync_post_request_from_dict = V1PortalPrivateSyncPostRequest.from_dict(v1_portal_private_sync_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


