# ManaV2Interface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**circuit** | **str** |  | [optional] 
**circuit_name** | **str** |  | [optional] 
**config_updated_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**configured_max_transmission_unit** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**duplex** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**gateway_address_v4** | **str** |  | [optional] 
**gateway_address_v6** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**ip_sec** | [**ManaV2InterfaceIPsec**](ManaV2InterfaceIPsec.md) |  | [optional] 
**ipv4** | [**ManaV2InterfaceAddress**](ManaV2InterfaceAddress.md) |  | [optional] 
**ipv6** | [**ManaV2InterfaceAddress**](ManaV2InterfaceAddress.md) |  | [optional] 
**ipv6_addresses** | [**List[ManaV2InterfaceAddress]**](ManaV2InterfaceAddress.md) |  | [optional] 
**lag_interface** | [**ManaV2LagInterface**](ManaV2LagInterface.md) |  | [optional] 
**lan** | **str** |  | [optional] 
**lldp_enabled** | **bool** |  | [optional] 
**macsec** | [**ManaV2InterfaceMaCsec**](ManaV2InterfaceMaCsec.md) |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**oper_updated_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**phy_address** | **str** |  | [optional] 
**pppoe_interface** | [**ManaV2PpPoEInterface**](ManaV2PpPoEInterface.md) |  | [optional] 
**pppoe_interfaces** | [**List[ManaV2Interface]**](ManaV2Interface.md) |  | [optional] 
**protocol** | **str** |  | [optional] 
**security_zone** | **str** |  | [optional] 
**sfp_optical_strength** | [**List[ManaV2InterfaceSfpOpticalStrength]**](ManaV2InterfaceSfpOpticalStrength.md) |  | [optional] 
**speed_mbps** | **int** |  | [optional] 
**subinterfaces** | [**List[ManaV2InterfaceVlan]**](ManaV2InterfaceVlan.md) |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**tcp_mss_v4** | **int** |  | [optional] 
**tcp_mss_v6** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**up** | **bool** |  | [optional] 
**vrf_function_id** | **int** |  | [optional] 
**vrf_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_interface import ManaV2Interface

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2Interface from a JSON string
mana_v2_interface_instance = ManaV2Interface.from_json(json)
# print the JSON string representation of the object
print(ManaV2Interface.to_json())

# convert the object into a dict
mana_v2_interface_dict = mana_v2_interface_instance.to_dict()
# create an instance of ManaV2Interface from a dict
mana_v2_interface_from_dict = ManaV2Interface.from_dict(mana_v2_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


