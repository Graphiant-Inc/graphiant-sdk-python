# V1DevicesInventoryEnterprisePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_serials** | **List[str]** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_inventory_enterprise_put_request import V1DevicesInventoryEnterprisePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesInventoryEnterprisePutRequest from a JSON string
v1_devices_inventory_enterprise_put_request_instance = V1DevicesInventoryEnterprisePutRequest.from_json(json)
# print the JSON string representation of the object
print(V1DevicesInventoryEnterprisePutRequest.to_json())

# convert the object into a dict
v1_devices_inventory_enterprise_put_request_dict = v1_devices_inventory_enterprise_put_request_instance.to_dict()
# create an instance of V1DevicesInventoryEnterprisePutRequest from a dict
v1_devices_inventory_enterprise_put_request_from_dict = V1DevicesInventoryEnterprisePutRequest.from_dict(v1_devices_inventory_enterprise_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


