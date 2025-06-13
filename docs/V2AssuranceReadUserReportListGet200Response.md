# V2AssuranceReadUserReportListGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_report_list** | [**List[V2AssuranceReadUserReportListGet200ResponseUserReportListInner]**](V2AssuranceReadUserReportListGet200ResponseUserReportListInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_read_user_report_list_get200_response import V2AssuranceReadUserReportListGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceReadUserReportListGet200Response from a JSON string
v2_assurance_read_user_report_list_get200_response_instance = V2AssuranceReadUserReportListGet200Response.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceReadUserReportListGet200Response.to_json())

# convert the object into a dict
v2_assurance_read_user_report_list_get200_response_dict = v2_assurance_read_user_report_list_get200_response_instance.to_dict()
# create an instance of V2AssuranceReadUserReportListGet200Response from a dict
v2_assurance_read_user_report_list_get200_response_from_dict = V2AssuranceReadUserReportListGet200Response.from_dict(v2_assurance_read_user_report_list_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


