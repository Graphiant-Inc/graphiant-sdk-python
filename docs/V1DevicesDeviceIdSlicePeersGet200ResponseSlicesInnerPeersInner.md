# V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_connection** | [**V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection**](V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection.md) |  | [optional] 
**connection_quality** | **str** |  | [optional] 
**device_id** | **int** |  | [optional] 
**gdi** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**ipsec_connection** | [**V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection**](V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection.md) |  | [optional] 
**state** | **str** |  | [optional] 
**wan_addresses** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner import V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner from a JSON string
v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_instance = V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner.to_json())

# convert the object into a dict
v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_dict = v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_instance.to_dict()
# create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner from a dict
v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_from_dict = V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner.from_dict(v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


