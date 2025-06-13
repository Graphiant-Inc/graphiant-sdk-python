# V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_address** | **str** |  | [optional] 
**oper_status** | **bool** |  | [optional] 
**remote_address** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**time_since_last_oper_change** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**up** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_bgp_connection import V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection from a JSON string
v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_bgp_connection_instance = V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection.to_json())

# convert the object into a dict
v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_bgp_connection_dict = v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_bgp_connection_instance.to_dict()
# create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection from a dict
v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_bgp_connection_from_dict = V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection.from_dict(v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_bgp_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


