# V1DeviceSnapshotPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**golden** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**snapshot_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_snapshot_put_request import V1DeviceSnapshotPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceSnapshotPutRequest from a JSON string
v1_device_snapshot_put_request_instance = V1DeviceSnapshotPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1DeviceSnapshotPutRequest.to_json())

# convert the object into a dict
v1_device_snapshot_put_request_dict = v1_device_snapshot_put_request_instance.to_dict()
# create an instance of V1DeviceSnapshotPutRequest from a dict
v1_device_snapshot_put_request_from_dict = V1DeviceSnapshotPutRequest.from_dict(v1_device_snapshot_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


