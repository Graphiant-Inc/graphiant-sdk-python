# V1SdkAutomationPlaybookJobsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[SdkAutomationPlaybookJob]**](SdkAutomationPlaybookJob.md) |  | [optional] 
**page_info** | [**CommonPageInfo**](CommonPageInfo.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_jobs_get_response import V1SdkAutomationPlaybookJobsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookJobsGetResponse from a JSON string
v1_sdk_automation_playbook_jobs_get_response_instance = V1SdkAutomationPlaybookJobsGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookJobsGetResponse.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_jobs_get_response_dict = v1_sdk_automation_playbook_jobs_get_response_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookJobsGetResponse from a dict
v1_sdk_automation_playbook_jobs_get_response_from_dict = V1SdkAutomationPlaybookJobsGetResponse.from_dict(v1_sdk_automation_playbook_jobs_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


