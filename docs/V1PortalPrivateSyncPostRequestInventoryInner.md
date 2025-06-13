# V1PortalPrivateSyncPostRequestInventoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_model** | **str** |  | [optional] 
**device_serial** | **str** |  | [optional] 
**is_delete** | **bool** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_portal_private_sync_post_request_inventory_inner import V1PortalPrivateSyncPostRequestInventoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1PortalPrivateSyncPostRequestInventoryInner from a JSON string
v1_portal_private_sync_post_request_inventory_inner_instance = V1PortalPrivateSyncPostRequestInventoryInner.from_json(json)
# print the JSON string representation of the object
print(V1PortalPrivateSyncPostRequestInventoryInner.to_json())

# convert the object into a dict
v1_portal_private_sync_post_request_inventory_inner_dict = v1_portal_private_sync_post_request_inventory_inner_instance.to_dict()
# create an instance of V1PortalPrivateSyncPostRequestInventoryInner from a dict
v1_portal_private_sync_post_request_inventory_inner_from_dict = V1PortalPrivateSyncPostRequestInventoryInner.from_dict(v1_portal_private_sync_post_request_inventory_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


