# ManaV2InterfaceCoreConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_status** | **bool** |  | [optional] 
**alias** | **str** |  | [optional] 
**circuit** | **str** |  | [optional] 
**core_neighbor** | [**ManaV2InterfaceCoreToCorePeerConfig**](ManaV2InterfaceCoreToCorePeerConfig.md) |  | [optional] 
**core_to_core_tunnel** | **object** |  | [optional] 
**create_link_local_address** | **bool** |  | [optional] 
**default** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**duplex** | **str** |  | [optional] 
**dynamic** | [**ManaV2LatencyBandwidth**](ManaV2LatencyBandwidth.md) |  | [optional] 
**flex_algos** | [**ManaV2InterfaceCoreFlexAlgoConfig**](ManaV2InterfaceCoreFlexAlgoConfig.md) |  | [optional] 
**gateway_neighbor** | [**ManaV2InterfaceCoreToGatewayPeerConfig**](ManaV2InterfaceCoreToGatewayPeerConfig.md) |  | [optional] 
**gw** | [**ManaV2NullableInterfaceIpConfig**](ManaV2NullableInterfaceIpConfig.md) |  | [optional] 
**interface_type** | [**ManaV2interfaceConfigType**](ManaV2interfaceConfigType.md) |  | [optional] 
**ipsec** | [**ManaV2InterfaceIPsecConfig**](ManaV2InterfaceIPsecConfig.md) |  | [optional] 
**ipv4** | [**ManaV2InterfaceIpConfig**](ManaV2InterfaceIpConfig.md) |  | [optional] 
**ipv6** | [**ManaV2InterfaceIpConfig**](ManaV2InterfaceIpConfig.md) |  | [optional] 
**is_maintenance_wan** | **bool** |  | [optional] 
**lan** | **str** |  | [optional] 
**lldp_enabled** | **bool** |  | [optional] 
**loopback** | **bool** |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**mpls_enabled** | **bool** |  | [optional] 
**ospf_cost** | [**ManaV2CoreLinkCost**](ManaV2CoreLinkCost.md) |  | [optional] 
**ospf_interface** | [**ManaV2NullableOspfInterfaceConfig**](ManaV2NullableOspfInterfaceConfig.md) |  | [optional] 
**peer_device_id** | **int** |  | [optional] 
**peer_hostname** | **str** |  | [optional] 
**security_zone** | **str** |  | [optional] 
**speed** | **int** |  | [optional] 
**static** | **int** |  | [optional] 
**subinterfaces** | [**Dict[str, ManaV2NullableCoreInterfaceVlanConfig]**](ManaV2NullableCoreInterfaceVlanConfig.md) |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**tcp_mss_v4** | **int** |  | [optional] 
**tcp_mss_v6** | **int** |  | [optional] 
**tunnel_interface** | **str** |  | [optional] 
**tunnel_underlay** | **str** |  | [optional] 
**wan** | [**ManaV2InterfaceWanConfig**](ManaV2InterfaceWanConfig.md) |  | [optional] 
**wan_management** | **object** |  | [optional] 
**x_talk_filter** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_interface_core_config import ManaV2InterfaceCoreConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2InterfaceCoreConfig from a JSON string
mana_v2_interface_core_config_instance = ManaV2InterfaceCoreConfig.from_json(json)
# print the JSON string representation of the object
print(ManaV2InterfaceCoreConfig.to_json())

# convert the object into a dict
mana_v2_interface_core_config_dict = mana_v2_interface_core_config_instance.to_dict()
# create an instance of ManaV2InterfaceCoreConfig from a dict
mana_v2_interface_core_config_from_dict = ManaV2InterfaceCoreConfig.from_dict(mana_v2_interface_core_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


