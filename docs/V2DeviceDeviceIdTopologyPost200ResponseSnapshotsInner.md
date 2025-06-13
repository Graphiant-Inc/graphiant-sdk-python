# V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quality** | **str** |  | [optional] 
**snapshot_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_device_device_id_topology_post200_response_snapshots_inner import V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner from a JSON string
v2_device_device_id_topology_post200_response_snapshots_inner_instance = V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner.from_json(json)
# print the JSON string representation of the object
print(V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner.to_json())

# convert the object into a dict
v2_device_device_id_topology_post200_response_snapshots_inner_dict = v2_device_device_id_topology_post200_response_snapshots_inner_instance.to_dict()
# create an instance of V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner from a dict
v2_device_device_id_topology_post200_response_snapshots_inner_from_dict = V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner.from_dict(v2_device_device_id_topology_post200_response_snapshots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


