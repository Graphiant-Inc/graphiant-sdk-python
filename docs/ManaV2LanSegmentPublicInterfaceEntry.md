# ManaV2LanSegmentPublicInterfaceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_id** | **int** | network.interface id (required) | [optional] 
**ipv4_addresses** | **List[str]** |  | [optional] 
**name** | **str** | Device interface name (BGP local_interface uses this) (required) | [optional] 
**storage_provider** | **str** | Interface storage provider (cloud provider for gateway LAN interfaces) | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_lan_segment_public_interface_entry import ManaV2LanSegmentPublicInterfaceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2LanSegmentPublicInterfaceEntry from a JSON string
mana_v2_lan_segment_public_interface_entry_instance = ManaV2LanSegmentPublicInterfaceEntry.from_json(json)
# print the JSON string representation of the object
print(ManaV2LanSegmentPublicInterfaceEntry.to_json())

# convert the object into a dict
mana_v2_lan_segment_public_interface_entry_dict = mana_v2_lan_segment_public_interface_entry_instance.to_dict()
# create an instance of ManaV2LanSegmentPublicInterfaceEntry from a dict
mana_v2_lan_segment_public_interface_entry_from_dict = ManaV2LanSegmentPublicInterfaceEntry.from_dict(mana_v2_lan_segment_public_interface_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


