# ManaV2PpPoEInterfaceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_status** | **bool** |  | [optional] 
**alias** | **str** |  | [optional] 
**authentication_type** | **str** |  | [optional] 
**circuit** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**lcp_echo_failure** | **int** |  | [optional] 
**lcp_echo_interval** | **int** |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**password** | **str** |  | [optional] 
**ppp_connect_timeout** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**v4_tcp_mss** | [**ManaV2NullableTcpMssV4**](ManaV2NullableTcpMssV4.md) |  | [optional] 
**v6_tcp_mss** | [**ManaV2NullableTcpMssV6**](ManaV2NullableTcpMssV6.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_pp_po_e_interface_config import ManaV2PpPoEInterfaceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PpPoEInterfaceConfig from a JSON string
mana_v2_pp_po_e_interface_config_instance = ManaV2PpPoEInterfaceConfig.from_json(json)
# print the JSON string representation of the object
print(ManaV2PpPoEInterfaceConfig.to_json())

# convert the object into a dict
mana_v2_pp_po_e_interface_config_dict = mana_v2_pp_po_e_interface_config_instance.to_dict()
# create an instance of ManaV2PpPoEInterfaceConfig from a dict
mana_v2_pp_po_e_interface_config_from_dict = ManaV2PpPoEInterfaceConfig.from_dict(mana_v2_pp_po_e_interface_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


