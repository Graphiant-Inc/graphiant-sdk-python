# V1DevicesDeviceIdVrrpGet200ResponseVrrpEntryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **str** |  | [optional] 
**advertisement_rcvd** | **int** |  | [optional] 
**advertisement_sent** | **int** |  | [optional] 
**effective_priority** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**is_owner** | **bool** |  | [optional] 
**master_transition** | **int** |  | [optional] 
**new_master_reason** | **str** |  | [optional] 
**priority_zero_pkts_rcvd** | **int** |  | [optional] 
**priority_zero_pkts_sent** | **int** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_vrrp_get200_response_vrrp_entry_inner import V1DevicesDeviceIdVrrpGet200ResponseVrrpEntryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdVrrpGet200ResponseVrrpEntryInner from a JSON string
v1_devices_device_id_vrrp_get200_response_vrrp_entry_inner_instance = V1DevicesDeviceIdVrrpGet200ResponseVrrpEntryInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdVrrpGet200ResponseVrrpEntryInner.to_json())

# convert the object into a dict
v1_devices_device_id_vrrp_get200_response_vrrp_entry_inner_dict = v1_devices_device_id_vrrp_get200_response_vrrp_entry_inner_instance.to_dict()
# create an instance of V1DevicesDeviceIdVrrpGet200ResponseVrrpEntryInner from a dict
v1_devices_device_id_vrrp_get200_response_vrrp_entry_inner_from_dict = V1DevicesDeviceIdVrrpGet200ResponseVrrpEntryInner.from_dict(v1_devices_device_id_vrrp_get200_response_vrrp_entry_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


