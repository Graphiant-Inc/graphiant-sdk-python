# V2AssuranceCreateUserReportPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **int** |  | [optional] 
**email_list** | **List[str]** |  | [optional] 
**pdf_content** | **bytearray** |  | [optional] 
**raw_content** | **List[bytearray]** |  | [optional] 
**report_name** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**time_period** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_create_user_report_post_request import V2AssuranceCreateUserReportPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceCreateUserReportPostRequest from a JSON string
v2_assurance_create_user_report_post_request_instance = V2AssuranceCreateUserReportPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceCreateUserReportPostRequest.to_json())

# convert the object into a dict
v2_assurance_create_user_report_post_request_dict = v2_assurance_create_user_report_post_request_instance.to_dict()
# create an instance of V2AssuranceCreateUserReportPostRequest from a dict
v2_assurance_create_user_report_post_request_from_dict = V2AssuranceCreateUserReportPostRequest.from_dict(v2_assurance_create_user_report_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


