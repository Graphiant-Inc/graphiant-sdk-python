# V1DevicesInventoryGet200ResponseInventoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_on** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**created_on** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**device_model** | **str** |  | [optional] 
**device_serial** | **str** |  | [optional] 
**ek_cert** | **str** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**enterprise_name** | **str** |  | [optional] 
**gek_pub** | **str** |  | [optional] 
**is_core** | **bool** |  | [optional] 
**is_new** | **bool** |  | [optional] 
**is_requested** | **bool** |  | [optional] 
**parent_enterprise_id** | **int** |  | [optional] 
**parent_enterprise_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**use_oauth** | **bool** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_inventory_get200_response_inventory_inner import V1DevicesInventoryGet200ResponseInventoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesInventoryGet200ResponseInventoryInner from a JSON string
v1_devices_inventory_get200_response_inventory_inner_instance = V1DevicesInventoryGet200ResponseInventoryInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesInventoryGet200ResponseInventoryInner.to_json())

# convert the object into a dict
v1_devices_inventory_get200_response_inventory_inner_dict = v1_devices_inventory_get200_response_inventory_inner_instance.to_dict()
# create an instance of V1DevicesInventoryGet200ResponseInventoryInner from a dict
v1_devices_inventory_get200_response_inventory_inner_from_dict = V1DevicesInventoryGet200ResponseInventoryInner.from_dict(v1_devices_inventory_get200_response_inventory_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


