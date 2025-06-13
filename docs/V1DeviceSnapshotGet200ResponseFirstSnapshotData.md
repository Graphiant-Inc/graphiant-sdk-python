# V1DeviceSnapshotGet200ResponseFirstSnapshotData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ospf_installed_route_count** | **int** |  | [optional] 
**t2_session_count** | **int** |  | [optional] 
**twamp_session_count** | **int** |  | [optional] 
**bfd_session_count** | **int** |  | [optional] 
**bgp_neighbor_ip_list** | **List[str]** |  | [optional] 
**bgp_session_count** | **int** |  | [optional] 
**device_role** | **str** |  | [optional] 
**failed_services_count** | **int** |  | [optional] 
**graphnos_version** | **str** |  | [optional] 
**installed_labels** | **int** |  | [optional] 
**ipsec_session_count** | **int** |  | [optional] 
**ongoing_alerts** | **int** |  | [optional] 
**ospf_neighbor_ip_list** | **List[str]** |  | [optional] 
**ospf_session_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_device_snapshot_get200_response_first_snapshot_data import V1DeviceSnapshotGet200ResponseFirstSnapshotData

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceSnapshotGet200ResponseFirstSnapshotData from a JSON string
v1_device_snapshot_get200_response_first_snapshot_data_instance = V1DeviceSnapshotGet200ResponseFirstSnapshotData.from_json(json)
# print the JSON string representation of the object
print(V1DeviceSnapshotGet200ResponseFirstSnapshotData.to_json())

# convert the object into a dict
v1_device_snapshot_get200_response_first_snapshot_data_dict = v1_device_snapshot_get200_response_first_snapshot_data_instance.to_dict()
# create an instance of V1DeviceSnapshotGet200ResponseFirstSnapshotData from a dict
v1_device_snapshot_get200_response_first_snapshot_data_from_dict = V1DeviceSnapshotGet200ResponseFirstSnapshotData.from_dict(v1_device_snapshot_get200_response_first_snapshot_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


