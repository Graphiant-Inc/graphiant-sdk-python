# V1PortalPrivateInventoryDetailsGet200ResponseDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_model** | **str** |  | [optional] 
**device_serial** | **str** |  | [optional] 
**private_gcs_id** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_portal_private_inventory_details_get200_response_details_inner import V1PortalPrivateInventoryDetailsGet200ResponseDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1PortalPrivateInventoryDetailsGet200ResponseDetailsInner from a JSON string
v1_portal_private_inventory_details_get200_response_details_inner_instance = V1PortalPrivateInventoryDetailsGet200ResponseDetailsInner.from_json(json)
# print the JSON string representation of the object
print(V1PortalPrivateInventoryDetailsGet200ResponseDetailsInner.to_json())

# convert the object into a dict
v1_portal_private_inventory_details_get200_response_details_inner_dict = v1_portal_private_inventory_details_get200_response_details_inner_instance.to_dict()
# create an instance of V1PortalPrivateInventoryDetailsGet200ResponseDetailsInner from a dict
v1_portal_private_inventory_details_get200_response_details_inner_from_dict = V1PortalPrivateInventoryDetailsGet200ResponseDetailsInner.from_dict(v1_portal_private_inventory_details_get200_response_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


