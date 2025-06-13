# V2AssuranceReadUserReportListGet200ResponseUserReportListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **List[str]** |  | [optional] 
**created_on** | **int** |  | [optional] 
**email_list** | **List[str]** |  | [optional] 
**enterprise_id** | **str** |  | [optional] 
**report_id** | **int** |  | [optional] 
**report_name** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**time_period** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_read_user_report_list_get200_response_user_report_list_inner import V2AssuranceReadUserReportListGet200ResponseUserReportListInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceReadUserReportListGet200ResponseUserReportListInner from a JSON string
v2_assurance_read_user_report_list_get200_response_user_report_list_inner_instance = V2AssuranceReadUserReportListGet200ResponseUserReportListInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceReadUserReportListGet200ResponseUserReportListInner.to_json())

# convert the object into a dict
v2_assurance_read_user_report_list_get200_response_user_report_list_inner_dict = v2_assurance_read_user_report_list_get200_response_user_report_list_inner_instance.to_dict()
# create an instance of V2AssuranceReadUserReportListGet200ResponseUserReportListInner from a dict
v2_assurance_read_user_report_list_get200_response_user_report_list_inner_from_dict = V2AssuranceReadUserReportListGet200ResponseUserReportListInner.from_dict(v2_assurance_read_user_report_list_get200_response_user_report_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


