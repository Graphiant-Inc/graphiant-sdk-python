# V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_replay_w_size** | **int** |  | [optional] 
**established_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**local_circuit** | **str** |  | [optional] 
**local_interface** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner.md) |  | [optional] 
**local_port** | **int** |  | [optional] 
**local_spi** | **int** |  | [optional] 
**negotiated_algorithms** | **str** |  | [optional] 
**oper_state** | **bool** |  | [optional] 
**peer_address** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**rekey_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**remote_port** | **int** |  | [optional] 
**remote_spi** | **int** |  | [optional] 
**session_id** | **int** |  | [optional] 
**source_address** | **str** |  | [optional] 
**tunnel_interface** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_ipsec_connection import V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection from a JSON string
v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_ipsec_connection_instance = V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection.to_json())

# convert the object into a dict
v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_ipsec_connection_dict = v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_ipsec_connection_instance.to_dict()
# create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection from a dict
v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_ipsec_connection_from_dict = V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection.from_dict(v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_ipsec_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


