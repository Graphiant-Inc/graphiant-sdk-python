# ManaV2LanSegmentPublicInterfacesLists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_interfaces** | [**List[ManaV2LanSegmentPublicInterfaceEntry]**](ManaV2LanSegmentPublicInterfaceEntry.md) |  | [optional] 
**public_interfaces** | [**List[ManaV2LanSegmentPublicInterfaceEntry]**](ManaV2LanSegmentPublicInterfaceEntry.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_lan_segment_public_interfaces_lists import ManaV2LanSegmentPublicInterfacesLists

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2LanSegmentPublicInterfacesLists from a JSON string
mana_v2_lan_segment_public_interfaces_lists_instance = ManaV2LanSegmentPublicInterfacesLists.from_json(json)
# print the JSON string representation of the object
print(ManaV2LanSegmentPublicInterfacesLists.to_json())

# convert the object into a dict
mana_v2_lan_segment_public_interfaces_lists_dict = mana_v2_lan_segment_public_interfaces_lists_instance.to_dict()
# create an instance of ManaV2LanSegmentPublicInterfacesLists from a dict
mana_v2_lan_segment_public_interfaces_lists_from_dict = ManaV2LanSegmentPublicInterfacesLists.from_dict(mana_v2_lan_segment_public_interfaces_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


