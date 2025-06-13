# V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**error** | **str** |  | [optional] 
**error_count** | **int** |  | [optional] 
**job_id** | **int** |  | [optional] 
**job_state** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_jobs_job_id_get200_response_job_status import V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus from a JSON string
v1_devices_device_id_jobs_job_id_get200_response_job_status_instance = V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus.to_json())

# convert the object into a dict
v1_devices_device_id_jobs_job_id_get200_response_job_status_dict = v1_devices_device_id_jobs_job_id_get200_response_job_status_instance.to_dict()
# create an instance of V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus from a dict
v1_devices_device_id_jobs_job_id_get200_response_job_status_from_dict = V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus.from_dict(v1_devices_device_id_jobs_job_id_get200_response_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


