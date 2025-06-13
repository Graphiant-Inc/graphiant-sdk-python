# V1DevicesInventoryGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | [**List[V1DevicesInventoryGet200ResponseInventoryInner]**](V1DevicesInventoryGet200ResponseInventoryInner.md) |  | [optional] 
**page_info** | [**V1NatEntriesDeviceIdGet200ResponsePageInfo**](V1NatEntriesDeviceIdGet200ResponsePageInfo.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_inventory_get200_response import V1DevicesInventoryGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesInventoryGet200Response from a JSON string
v1_devices_inventory_get200_response_instance = V1DevicesInventoryGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1DevicesInventoryGet200Response.to_json())

# convert the object into a dict
v1_devices_inventory_get200_response_dict = v1_devices_inventory_get200_response_instance.to_dict()
# create an instance of V1DevicesInventoryGet200Response from a dict
v1_devices_inventory_get200_response_from_dict = V1DevicesInventoryGet200Response.from_dict(v1_devices_inventory_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


