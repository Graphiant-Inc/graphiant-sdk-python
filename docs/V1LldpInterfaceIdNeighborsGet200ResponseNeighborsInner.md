# V1LldpInterfaceIdNeighborsGet200ResponseNeighborsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**interface** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**system_name** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_lldp_interface_id_neighbors_get200_response_neighbors_inner import V1LldpInterfaceIdNeighborsGet200ResponseNeighborsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1LldpInterfaceIdNeighborsGet200ResponseNeighborsInner from a JSON string
v1_lldp_interface_id_neighbors_get200_response_neighbors_inner_instance = V1LldpInterfaceIdNeighborsGet200ResponseNeighborsInner.from_json(json)
# print the JSON string representation of the object
print(V1LldpInterfaceIdNeighborsGet200ResponseNeighborsInner.to_json())

# convert the object into a dict
v1_lldp_interface_id_neighbors_get200_response_neighbors_inner_dict = v1_lldp_interface_id_neighbors_get200_response_neighbors_inner_instance.to_dict()
# create an instance of V1LldpInterfaceIdNeighborsGet200ResponseNeighborsInner from a dict
v1_lldp_interface_id_neighbors_get200_response_neighbors_inner_from_dict = V1LldpInterfaceIdNeighborsGet200ResponseNeighborsInner.from_dict(v1_lldp_interface_id_neighbors_get200_response_neighbors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


