# ManaV2InterfaceVlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**circuit** | **str** |  | [optional] 
**config_updated_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**description** | **str** |  | [optional] 
**duplex** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**gateway_address_v4** | **str** |  | [optional] 
**gateway_address_v6** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**ipv4** | [**ManaV2InterfaceAddress**](ManaV2InterfaceAddress.md) |  | [optional] 
**ipv6** | [**ManaV2InterfaceAddress**](ManaV2InterfaceAddress.md) |  | [optional] 
**ipv6_addresses** | [**List[ManaV2InterfaceAddress]**](ManaV2InterfaceAddress.md) |  | [optional] 
**lan** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**oper_updated_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**parent_mac_address** | **str** |  | [optional] 
**pppoe_interfaces** | [**List[ManaV2Interface]**](ManaV2Interface.md) |  | [optional] 
**security_zone** | **str** |  | [optional] 
**speed_mbps** | **int** |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**tcp_mss_v4** | **int** |  | [optional] 
**tcp_mss_v6** | **int** |  | [optional] 
**up** | **bool** |  | [optional] 
**vlan** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_interface_vlan import ManaV2InterfaceVlan

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2InterfaceVlan from a JSON string
mana_v2_interface_vlan_instance = ManaV2InterfaceVlan.from_json(json)
# print the JSON string representation of the object
print(ManaV2InterfaceVlan.to_json())

# convert the object into a dict
mana_v2_interface_vlan_dict = mana_v2_interface_vlan_instance.to_dict()
# create an instance of ManaV2InterfaceVlan from a dict
mana_v2_interface_vlan_from_dict = ManaV2InterfaceVlan.from_dict(mana_v2_interface_vlan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


