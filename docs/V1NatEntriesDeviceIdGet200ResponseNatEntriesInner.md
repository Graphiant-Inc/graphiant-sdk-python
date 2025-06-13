# V1NatEntriesDeviceIdGet200ResponseNatEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_ip_address** | **str** |  | [optional] 
**destination_port** | **int** |  | [optional] 
**inside_global_ip_address** | **str** |  | [optional] 
**inside_global_port** | **int** |  | [optional] 
**inside_local_ip_address** | **str** |  | [optional] 
**inside_local_port** | **int** |  | [optional] 
**nat_type** | **str** |  | [optional] 
**outside_global_ip_address** | **str** |  | [optional] 
**outside_global_port** | **int** |  | [optional] 
**pre_destination_ip_address** | **str** |  | [optional] 
**pre_destination_port** | **int** |  | [optional] 
**vrf_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_nat_entries_device_id_get200_response_nat_entries_inner import V1NatEntriesDeviceIdGet200ResponseNatEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1NatEntriesDeviceIdGet200ResponseNatEntriesInner from a JSON string
v1_nat_entries_device_id_get200_response_nat_entries_inner_instance = V1NatEntriesDeviceIdGet200ResponseNatEntriesInner.from_json(json)
# print the JSON string representation of the object
print(V1NatEntriesDeviceIdGet200ResponseNatEntriesInner.to_json())

# convert the object into a dict
v1_nat_entries_device_id_get200_response_nat_entries_inner_dict = v1_nat_entries_device_id_get200_response_nat_entries_inner_instance.to_dict()
# create an instance of V1NatEntriesDeviceIdGet200ResponseNatEntriesInner from a dict
v1_nat_entries_device_id_get200_response_nat_entries_inner_from_dict = V1NatEntriesDeviceIdGet200ResponseNatEntriesInner.from_dict(v1_nat_entries_device_id_get200_response_nat_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


