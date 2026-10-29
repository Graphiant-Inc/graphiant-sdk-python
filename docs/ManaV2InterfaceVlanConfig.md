# ManaV2InterfaceVlanConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_status** | **bool** |  | [optional] 
**alias** | **str** |  | [optional] 
**circuit** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ipv4** | [**ManaV2InterfaceIpConfig**](ManaV2InterfaceIpConfig.md) |  | [optional] 
**ipv6** | [**ManaV2InterfaceIpConfig**](ManaV2InterfaceIpConfig.md) |  | [optional] 
**lan** | **str** |  | [optional] 
**lldp_enabled** | **bool** |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**pppoe_interfaces** | [**Dict[str, ManaV2NullablePpPoEInterfaceConfig]**](ManaV2NullablePpPoEInterfaceConfig.md) |  | [optional] 
**security_zone** | **str** |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**tcp_mss_v4** | **int** |  | [optional] 
**tcp_mss_v6** | **int** |  | [optional] 
**v4_tcp_mss** | [**ManaV2NullableTcpMssV4**](ManaV2NullableTcpMssV4.md) |  | [optional] 
**v6_tcp_mss** | [**ManaV2NullableTcpMssV6**](ManaV2NullableTcpMssV6.md) |  | [optional] 
**vlan** | **int** |  | [optional] 
**vrrp** | [**ManaV2NullableVrrpGroupConfig**](ManaV2NullableVrrpGroupConfig.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_interface_vlan_config import ManaV2InterfaceVlanConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2InterfaceVlanConfig from a JSON string
mana_v2_interface_vlan_config_instance = ManaV2InterfaceVlanConfig.from_json(json)
# print the JSON string representation of the object
print(ManaV2InterfaceVlanConfig.to_json())

# convert the object into a dict
mana_v2_interface_vlan_config_dict = mana_v2_interface_vlan_config_instance.to_dict()
# create an instance of ManaV2InterfaceVlanConfig from a dict
mana_v2_interface_vlan_config_from_dict = ManaV2InterfaceVlanConfig.from_dict(mana_v2_interface_vlan_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


