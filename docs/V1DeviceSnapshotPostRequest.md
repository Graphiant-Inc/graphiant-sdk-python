# V1DeviceSnapshotPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**device_id** | **int** |  | [optional] 
**golden** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_snapshot_post_request import V1DeviceSnapshotPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceSnapshotPostRequest from a JSON string
v1_device_snapshot_post_request_instance = V1DeviceSnapshotPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1DeviceSnapshotPostRequest.to_json())

# convert the object into a dict
v1_device_snapshot_post_request_dict = v1_device_snapshot_post_request_instance.to_dict()
# create an instance of V1DeviceSnapshotPostRequest from a dict
v1_device_snapshot_post_request_from_dict = V1DeviceSnapshotPostRequest.from_dict(v1_device_snapshot_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


