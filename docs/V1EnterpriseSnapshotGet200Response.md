# V1EnterpriseSnapshotGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_snapshot_records** | [**List[V1EnterpriseSnapshotGet200ResponseDeviceSnapshotRecordsInner]**](V1EnterpriseSnapshotGet200ResponseDeviceSnapshotRecordsInner.md) |  | [optional] 
**device_snapshot_map** | [**Dict[str, V1EnterpriseSnapshotGet200ResponseDeviceSnapshotMapValue]**](V1EnterpriseSnapshotGet200ResponseDeviceSnapshotMapValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_snapshot_get200_response import V1EnterpriseSnapshotGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseSnapshotGet200Response from a JSON string
v1_enterprise_snapshot_get200_response_instance = V1EnterpriseSnapshotGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseSnapshotGet200Response.to_json())

# convert the object into a dict
v1_enterprise_snapshot_get200_response_dict = v1_enterprise_snapshot_get200_response_instance.to_dict()
# create an instance of V1EnterpriseSnapshotGet200Response from a dict
v1_enterprise_snapshot_get200_response_from_dict = V1EnterpriseSnapshotGet200Response.from_dict(v1_enterprise_snapshot_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


