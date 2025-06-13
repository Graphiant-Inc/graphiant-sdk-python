# V1EnterpriseSnapshotGet200ResponseDeviceSnapshotMapValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**snapshots** | [**List[V1DeviceSnapshotGet200ResponseFirstSnapshot]**](V1DeviceSnapshotGet200ResponseFirstSnapshot.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_snapshot_get200_response_device_snapshot_map_value import V1EnterpriseSnapshotGet200ResponseDeviceSnapshotMapValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseSnapshotGet200ResponseDeviceSnapshotMapValue from a JSON string
v1_enterprise_snapshot_get200_response_device_snapshot_map_value_instance = V1EnterpriseSnapshotGet200ResponseDeviceSnapshotMapValue.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseSnapshotGet200ResponseDeviceSnapshotMapValue.to_json())

# convert the object into a dict
v1_enterprise_snapshot_get200_response_device_snapshot_map_value_dict = v1_enterprise_snapshot_get200_response_device_snapshot_map_value_instance.to_dict()
# create an instance of V1EnterpriseSnapshotGet200ResponseDeviceSnapshotMapValue from a dict
v1_enterprise_snapshot_get200_response_device_snapshot_map_value_from_dict = V1EnterpriseSnapshotGet200ResponseDeviceSnapshotMapValue.from_dict(v1_enterprise_snapshot_get200_response_device_snapshot_map_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


