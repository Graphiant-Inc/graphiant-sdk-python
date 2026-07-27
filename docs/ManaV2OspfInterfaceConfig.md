# ManaV2OspfInterfaceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**ManaV2NullableOspfAuthenticationConfig**](ManaV2NullableOspfAuthenticationConfig.md) |  | [optional] 
**bfd** | [**ManaV2NullableBfdInstanceConfig**](ManaV2NullableBfdInstanceConfig.md) |  | [optional] 
**cost** | **int** |  | [optional] 
**dead_interval_value** | [**ManaV2NullableOspfDeadIntervalValue**](ManaV2NullableOspfDeadIntervalValue.md) |  | [optional] 
**dr_priority** | **int** |  | [optional] 
**hello_interval_value** | [**ManaV2NullableOspfHelloIntervalValue**](ManaV2NullableOspfHelloIntervalValue.md) |  | [optional] 
**interface_name** | **str** |  | [optional] 
**mtu** | **int** |  | [optional] 
**mtu_ignore** | **bool** |  | [optional] 
**prefix_sid** | **int** |  | [optional] 
**retransmit_interval_value** | [**ManaV2NullableOspfRetransmitIntervalValue**](ManaV2NullableOspfRetransmitIntervalValue.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_ospf_interface_config import ManaV2OspfInterfaceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2OspfInterfaceConfig from a JSON string
mana_v2_ospf_interface_config_instance = ManaV2OspfInterfaceConfig.from_json(json)
# print the JSON string representation of the object
print(ManaV2OspfInterfaceConfig.to_json())

# convert the object into a dict
mana_v2_ospf_interface_config_dict = mana_v2_ospf_interface_config_instance.to_dict()
# create an instance of ManaV2OspfInterfaceConfig from a dict
mana_v2_ospf_interface_config_from_dict = ManaV2OspfInterfaceConfig.from_dict(mana_v2_ospf_interface_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


