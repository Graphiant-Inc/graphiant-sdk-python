# V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_status** | **bool** |  | [optional] 
**alias** | **str** |  | [optional] 
**circuit** | **str** |  | [optional] 
**core_neighbor** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighbor.md) |  | [optional] 
**core_to_core_tunnel** | **object** |  | [optional] 
**create_link_local_address** | **bool** |  | [optional] 
**default** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**duplex** | **str** |  | [optional] 
**dynamic** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCostDynamic**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCostDynamic.md) |  | [optional] 
**flex_algos** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceFlexAlgos**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceFlexAlgos.md) |  | [optional] 
**gateway_neighbor** | [**V1AccountMfaGet200Response**](V1AccountMfaGet200Response.md) |  | [optional] 
**gw** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGw.md) |  | [optional] 
**interface_type** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceType**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceInterfaceType.md) |  | [optional] 
**ipsec** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec.md) |  | [optional] 
**ipv4** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw.md) |  | [optional] 
**ipv6** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw.md) |  | [optional] 
**lan** | **str** |  | [optional] 
**lldp_enabled** | **bool** |  | [optional] 
**loopback** | **bool** |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**mpls_enabled** | **bool** |  | [optional] 
**ospf_cost** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost.md) |  | [optional] 
**ospf_interface** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterface**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterface.md) |  | [optional] 
**peer_device_id** | **int** |  | [optional] 
**peer_hostname** | **str** |  | [optional] 
**security_zone** | **str** |  | [optional] 
**speed** | **int** |  | [optional] 
**static** | **int** |  | [optional] 
**subinterfaces** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValue]**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValue.md) |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**tcp_mss_v4** | **int** |  | [optional] 
**tcp_mss_v6** | **int** |  | [optional] 
**tunnel_interface** | **str** |  | [optional] 
**tunnel_underlay** | **str** |  | [optional] 
**wan** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceWan**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceWan.md) |  | [optional] 
**wan_management** | **object** |  | [optional] 
**x_talk_filter** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterface

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterface from a JSON string
v1_devices_device_id_config_put_request_core_interfaces_value_interface_instance = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterface.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterface.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_dict = v1_devices_device_id_config_put_request_core_interfaces_value_interface_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterface from a dict
v1_devices_device_id_config_put_request_core_interfaces_value_interface_from_dict = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterface.from_dict(v1_devices_device_id_config_put_request_core_interfaces_value_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


