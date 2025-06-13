# V1DevicesInventoryPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_inventory_list** | [**List[V1DevicesInventoryGet200ResponseInventoryInner]**](V1DevicesInventoryGet200ResponseInventoryInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_inventory_post_request import V1DevicesInventoryPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesInventoryPostRequest from a JSON string
v1_devices_inventory_post_request_instance = V1DevicesInventoryPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1DevicesInventoryPostRequest.to_json())

# convert the object into a dict
v1_devices_inventory_post_request_dict = v1_devices_inventory_post_request_instance.to_dict()
# create an instance of V1DevicesInventoryPostRequest from a dict
v1_devices_inventory_post_request_from_dict = V1DevicesInventoryPostRequest.from_dict(v1_devices_inventory_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


