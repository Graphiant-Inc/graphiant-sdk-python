# V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**peers** | [**List[V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner]**](V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner.md) |  | [optional] 
**slice_index** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_slice_peers_get200_response_slices_inner import V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner from a JSON string
v1_devices_device_id_slice_peers_get200_response_slices_inner_instance = V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner.to_json())

# convert the object into a dict
v1_devices_device_id_slice_peers_get200_response_slices_inner_dict = v1_devices_device_id_slice_peers_get200_response_slices_inner_instance.to_dict()
# create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner from a dict
v1_devices_device_id_slice_peers_get200_response_slices_inner_from_dict = V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner.from_dict(v1_devices_device_id_slice_peers_get200_response_slices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


