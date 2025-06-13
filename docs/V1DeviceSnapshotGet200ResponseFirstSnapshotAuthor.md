# V1DeviceSnapshotGet200ResponseFirstSnapshotAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise_id** | **int** |  | [optional] 
**exp** | **int** |  | [optional] 
**original_enterprise_id** | **int** |  | [optional] 
**permissions** | [**V1GroupsGet200ResponseGroupsInnerPermissions**](V1GroupsGet200ResponseGroupsInnerPermissions.md) |  | [optional] 
**time_zone** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_snapshot_get200_response_first_snapshot_author import V1DeviceSnapshotGet200ResponseFirstSnapshotAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceSnapshotGet200ResponseFirstSnapshotAuthor from a JSON string
v1_device_snapshot_get200_response_first_snapshot_author_instance = V1DeviceSnapshotGet200ResponseFirstSnapshotAuthor.from_json(json)
# print the JSON string representation of the object
print(V1DeviceSnapshotGet200ResponseFirstSnapshotAuthor.to_json())

# convert the object into a dict
v1_device_snapshot_get200_response_first_snapshot_author_dict = v1_device_snapshot_get200_response_first_snapshot_author_instance.to_dict()
# create an instance of V1DeviceSnapshotGet200ResponseFirstSnapshotAuthor from a dict
v1_device_snapshot_get200_response_first_snapshot_author_from_dict = V1DeviceSnapshotGet200ResponseFirstSnapshotAuthor.from_dict(v1_device_snapshot_get200_response_first_snapshot_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


