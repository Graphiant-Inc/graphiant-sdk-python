# V1SoftwareGcsreleaseUploadNotesPostRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**List[V1SoftwareGcsreleaseUploadNotesPostRequestDetailsCategoryInner]**](V1SoftwareGcsreleaseUploadNotesPostRequestDetailsCategoryInner.md) |  | [optional] 
**major** | **bool** |  | [optional] 
**release_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_software_gcsrelease_upload_notes_post_request_details import V1SoftwareGcsreleaseUploadNotesPostRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of V1SoftwareGcsreleaseUploadNotesPostRequestDetails from a JSON string
v1_software_gcsrelease_upload_notes_post_request_details_instance = V1SoftwareGcsreleaseUploadNotesPostRequestDetails.from_json(json)
# print the JSON string representation of the object
print(V1SoftwareGcsreleaseUploadNotesPostRequestDetails.to_json())

# convert the object into a dict
v1_software_gcsrelease_upload_notes_post_request_details_dict = v1_software_gcsrelease_upload_notes_post_request_details_instance.to_dict()
# create an instance of V1SoftwareGcsreleaseUploadNotesPostRequestDetails from a dict
v1_software_gcsrelease_upload_notes_post_request_details_from_dict = V1SoftwareGcsreleaseUploadNotesPostRequestDetails.from_dict(v1_software_gcsrelease_upload_notes_post_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


