# V2AssuranceTopologyInventoryPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 
**topology_type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_inventory_post_request import V2AssuranceTopologyInventoryPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyInventoryPostRequest from a JSON string
v2_assurance_topology_inventory_post_request_instance = V2AssuranceTopologyInventoryPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyInventoryPostRequest.to_json())

# convert the object into a dict
v2_assurance_topology_inventory_post_request_dict = v2_assurance_topology_inventory_post_request_instance.to_dict()
# create an instance of V2AssuranceTopologyInventoryPostRequest from a dict
v2_assurance_topology_inventory_post_request_from_dict = V2AssuranceTopologyInventoryPostRequest.from_dict(v2_assurance_topology_inventory_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


