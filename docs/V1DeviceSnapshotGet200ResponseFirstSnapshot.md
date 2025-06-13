# V1DeviceSnapshotGet200ResponseFirstSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**V1DeviceSnapshotGet200ResponseFirstSnapshotAuthor**](V1DeviceSnapshotGet200ResponseFirstSnapshotAuthor.md) |  | [optional] 
**category** | **str** |  | [optional] 
**created_on** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**data** | [**V1DeviceSnapshotGet200ResponseFirstSnapshotData**](V1DeviceSnapshotGet200ResponseFirstSnapshotData.md) |  | [optional] 
**golden** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_snapshot_get200_response_first_snapshot import V1DeviceSnapshotGet200ResponseFirstSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceSnapshotGet200ResponseFirstSnapshot from a JSON string
v1_device_snapshot_get200_response_first_snapshot_instance = V1DeviceSnapshotGet200ResponseFirstSnapshot.from_json(json)
# print the JSON string representation of the object
print(V1DeviceSnapshotGet200ResponseFirstSnapshot.to_json())

# convert the object into a dict
v1_device_snapshot_get200_response_first_snapshot_dict = v1_device_snapshot_get200_response_first_snapshot_instance.to_dict()
# create an instance of V1DeviceSnapshotGet200ResponseFirstSnapshot from a dict
v1_device_snapshot_get200_response_first_snapshot_from_dict = V1DeviceSnapshotGet200ResponseFirstSnapshot.from_dict(v1_device_snapshot_get200_response_first_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


