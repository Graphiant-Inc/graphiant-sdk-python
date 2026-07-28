# ManaV2OspfInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**ManaV2OspfAuthentication**](ManaV2OspfAuthentication.md) |  | [optional] 
**bfd** | [**ManaV2BfdInstance**](ManaV2BfdInstance.md) |  | [optional] 
**bfd_neighbors** | [**List[ManaV2BfdNeighbor]**](ManaV2BfdNeighbor.md) |  | [optional] 
**cost** | **int** |  | [optional] 
**dead_interval** | **int** |  | [optional] 
**dead_interval_value** | **int** |  | [optional] 
**dr_priority** | **int** |  | [optional] 
**hello_interval** | **int** |  | [optional] 
**hello_interval_value** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**if_index** | **int** |  | [optional] 
**interface** | **str** |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**mtu_ignore** | **bool** |  | [optional] 
**prefix_sid** | **int** |  | [optional] 
**retransmit_interval** | **int** |  | [optional] 
**retransmit_interval_value** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_ospf_interface import ManaV2OspfInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2OspfInterface from a JSON string
mana_v2_ospf_interface_instance = ManaV2OspfInterface.from_json(json)
# print the JSON string representation of the object
print(ManaV2OspfInterface.to_json())

# convert the object into a dict
mana_v2_ospf_interface_dict = mana_v2_ospf_interface_instance.to_dict()
# create an instance of ManaV2OspfInterface from a dict
mana_v2_ospf_interface_from_dict = ManaV2OspfInterface.from_dict(mana_v2_ospf_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


