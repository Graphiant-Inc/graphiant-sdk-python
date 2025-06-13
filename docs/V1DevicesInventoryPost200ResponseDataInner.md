# V1DevicesInventoryPost200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_serial** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_inventory_post200_response_data_inner import V1DevicesInventoryPost200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesInventoryPost200ResponseDataInner from a JSON string
v1_devices_inventory_post200_response_data_inner_instance = V1DevicesInventoryPost200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesInventoryPost200ResponseDataInner.to_json())

# convert the object into a dict
v1_devices_inventory_post200_response_data_inner_dict = v1_devices_inventory_post200_response_data_inner_instance.to_dict()
# create an instance of V1DevicesInventoryPost200ResponseDataInner from a dict
v1_devices_inventory_post200_response_data_inner_from_dict = V1DevicesInventoryPost200ResponseDataInner.from_dict(v1_devices_inventory_post200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


