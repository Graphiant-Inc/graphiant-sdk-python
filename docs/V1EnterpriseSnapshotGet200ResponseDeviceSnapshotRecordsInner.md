# V1EnterpriseSnapshotGet200ResponseDeviceSnapshotRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**snapshot_count** | **int** |  | [optional] 
**snapshots** | [**List[V1DeviceSnapshotGet200ResponseFirstSnapshot]**](V1DeviceSnapshotGet200ResponseFirstSnapshot.md) |  | [optional] 
**uptime** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_snapshot_get200_response_device_snapshot_records_inner import V1EnterpriseSnapshotGet200ResponseDeviceSnapshotRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseSnapshotGet200ResponseDeviceSnapshotRecordsInner from a JSON string
v1_enterprise_snapshot_get200_response_device_snapshot_records_inner_instance = V1EnterpriseSnapshotGet200ResponseDeviceSnapshotRecordsInner.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseSnapshotGet200ResponseDeviceSnapshotRecordsInner.to_json())

# convert the object into a dict
v1_enterprise_snapshot_get200_response_device_snapshot_records_inner_dict = v1_enterprise_snapshot_get200_response_device_snapshot_records_inner_instance.to_dict()
# create an instance of V1EnterpriseSnapshotGet200ResponseDeviceSnapshotRecordsInner from a dict
v1_enterprise_snapshot_get200_response_device_snapshot_records_inner_from_dict = V1EnterpriseSnapshotGet200ResponseDeviceSnapshotRecordsInner.from_dict(v1_enterprise_snapshot_get200_response_device_snapshot_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


