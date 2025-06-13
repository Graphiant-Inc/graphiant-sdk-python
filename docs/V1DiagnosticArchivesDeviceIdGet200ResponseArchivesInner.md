# V1DiagnosticArchivesDeviceIdGet200ResponseArchivesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_file_name** | **str** |  | [optional] 
**archive_id** | **int** |  | [optional] 
**archive_url** | **str** |  | [optional] 
**created** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**creator** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**progress** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_diagnostic_archives_device_id_get200_response_archives_inner import V1DiagnosticArchivesDeviceIdGet200ResponseArchivesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DiagnosticArchivesDeviceIdGet200ResponseArchivesInner from a JSON string
v1_diagnostic_archives_device_id_get200_response_archives_inner_instance = V1DiagnosticArchivesDeviceIdGet200ResponseArchivesInner.from_json(json)
# print the JSON string representation of the object
print(V1DiagnosticArchivesDeviceIdGet200ResponseArchivesInner.to_json())

# convert the object into a dict
v1_diagnostic_archives_device_id_get200_response_archives_inner_dict = v1_diagnostic_archives_device_id_get200_response_archives_inner_instance.to_dict()
# create an instance of V1DiagnosticArchivesDeviceIdGet200ResponseArchivesInner from a dict
v1_diagnostic_archives_device_id_get200_response_archives_inner_from_dict = V1DiagnosticArchivesDeviceIdGet200ResponseArchivesInner.from_dict(v1_diagnostic_archives_device_id_get200_response_archives_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


