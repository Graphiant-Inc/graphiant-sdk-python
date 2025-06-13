# V1DevicesDeviceIdArpGet200ResponseArpEntryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_name** | **str** |  | [optional] 
**ipv4_address** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_arp_get200_response_arp_entry_inner import V1DevicesDeviceIdArpGet200ResponseArpEntryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdArpGet200ResponseArpEntryInner from a JSON string
v1_devices_device_id_arp_get200_response_arp_entry_inner_instance = V1DevicesDeviceIdArpGet200ResponseArpEntryInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdArpGet200ResponseArpEntryInner.to_json())

# convert the object into a dict
v1_devices_device_id_arp_get200_response_arp_entry_inner_dict = v1_devices_device_id_arp_get200_response_arp_entry_inner_instance.to_dict()
# create an instance of V1DevicesDeviceIdArpGet200ResponseArpEntryInner from a dict
v1_devices_device_id_arp_get200_response_arp_entry_inner_from_dict = V1DevicesDeviceIdArpGet200ResponseArpEntryInner.from_dict(v1_devices_device_id_arp_get200_response_arp_entry_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


