# V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighbor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_families** | [**Dict[str, V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValue]**](V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpAddressFamiliesValue.md) |  | [optional] 
**allow_as_in** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborAllowAsIn**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborAllowAsIn.md) |  | [optional] 
**as_override** | **bool** |  | [optional] 
**bfd** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborBfd**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborBfd.md) |  | [optional] 
**default_originate** | **str** |  | [optional] 
**ebgp_multihop_ttl** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborEbgpMultihopTtl**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborEbgpMultihopTtl.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**hold_timer** | **int** |  | [optional] 
**hold_timer_value** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborHoldTimerValue**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborHoldTimerValue.md) |  | [optional] 
**keepalive_timer** | **int** |  | [optional] 
**keepalive_timer_value** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborHoldTimerValue**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborHoldTimerValue.md) |  | [optional] 
**local_address** | **str** |  | [optional] 
**local_interface** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchSourceInterface**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchSourceInterface.md) |  | [optional] 
**max_prefix_value** | [**V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborMaxPrefixValue**](V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighborMaxPrefixValue.md) |  | [optional] 
**md5_password** | [**V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpMd5Password**](V1GatewaysPutRequestDetailsIpsecGatewayRoutingBgpMd5Password.md) |  | [optional] 
**peer_asn** | **int** |  | [optional] 
**remote_address** | **str** |  | [optional] 
**remove_private_as** | **bool** |  | [optional] 
**send_community** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_bgp_neighbors_value_neighbor import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighbor from a JSON string
v1_devices_device_id_config_put_request_core_core_vrf_bgp_neighbors_value_neighbor_instance = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighbor.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighbor.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_core_vrf_bgp_neighbors_value_neighbor_dict = v1_devices_device_id_config_put_request_core_core_vrf_bgp_neighbors_value_neighbor_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighbor from a dict
v1_devices_device_id_config_put_request_core_core_vrf_bgp_neighbors_value_neighbor_from_dict = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpNeighborsValueNeighbor.from_dict(v1_devices_device_id_config_put_request_core_core_vrf_bgp_neighbors_value_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


