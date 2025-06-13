# V1DevicesDeviceIdConfigPutRequestEdgeSiteToSiteVpnValueSiteToSiteVpn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_address** | **str** |  | [optional] 
**ike_initiator** | **bool** |  | [optional] 
**ipsec_label** | **str** |  | [optional] 
**lan** | **str** |  | [optional] 
**local_address_v4** | **str** |  | [optional] 
**local_address_v6** | **str** |  | [optional] 
**local_circuit** | **str** |  | [optional] 
**local_ike_peer_identity** | **str** |  | [optional] 
**mtu** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**preshared_key** | **str** |  | [optional] 
**remote_address_v4** | **str** |  | [optional] 
**remote_address_v6** | **str** |  | [optional] 
**remote_ike_peer_identity** | **str** |  | [optional] 
**routing** | [**V1GatewaysPutRequestDetailsIpsecGatewayRouting**](V1GatewaysPutRequestDetailsIpsecGatewayRouting.md) |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**vpn_profile** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_site_to_site_vpn_value_site_to_site_vpn import V1DevicesDeviceIdConfigPutRequestEdgeSiteToSiteVpnValueSiteToSiteVpn

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeSiteToSiteVpnValueSiteToSiteVpn from a JSON string
v1_devices_device_id_config_put_request_edge_site_to_site_vpn_value_site_to_site_vpn_instance = V1DevicesDeviceIdConfigPutRequestEdgeSiteToSiteVpnValueSiteToSiteVpn.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestEdgeSiteToSiteVpnValueSiteToSiteVpn.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_edge_site_to_site_vpn_value_site_to_site_vpn_dict = v1_devices_device_id_config_put_request_edge_site_to_site_vpn_value_site_to_site_vpn_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeSiteToSiteVpnValueSiteToSiteVpn from a dict
v1_devices_device_id_config_put_request_edge_site_to_site_vpn_value_site_to_site_vpn_from_dict = V1DevicesDeviceIdConfigPutRequestEdgeSiteToSiteVpnValueSiteToSiteVpn.from_dict(v1_devices_device_id_config_put_request_edge_site_to_site_vpn_value_site_to_site_vpn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


