# V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_status** | **bool** |  | [optional] 
**alias** | **str** |  | [optional] 
**circuit** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ipsec** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec.md) |  | [optional] 
**ipv4** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw.md) |  | [optional] 
**ipv6** | [**V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw**](V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw.md) |  | [optional] 
**lan** | **str** |  | [optional] 
**lldp_enabled** | **bool** |  | [optional] 
**loopback** | **bool** |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**security_zone** | **str** |  | [optional] 
**subinterfaces** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValue]**](V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValue.md) |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**tcp_mss_v4** | **int** |  | [optional] 
**tcp_mss_v6** | **int** |  | [optional] 
**v4_tcp_mss** | [**V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValueInterfaceV4TcpMss**](V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValueInterfaceV4TcpMss.md) |  | [optional] 
**v6_tcp_mss** | [**V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValueInterfaceV6TcpMss**](V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValueInterfaceV6TcpMss.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_interfaces_value_interface import V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface from a JSON string
v1_devices_device_id_config_put_request_edge_interfaces_value_interface_instance = V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_edge_interfaces_value_interface_dict = v1_devices_device_id_config_put_request_edge_interfaces_value_interface_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface from a dict
v1_devices_device_id_config_put_request_edge_interfaces_value_interface_from_dict = V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface.from_dict(v1_devices_device_id_config_put_request_edge_interfaces_value_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


