# V1SdkAutomationPlaybookJobsJobIdResumePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Resumed job id | [optional] 
**status** | **str** | Job status after resume was accepted | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_jobs_job_id_resume_post_response import V1SdkAutomationPlaybookJobsJobIdResumePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookJobsJobIdResumePostResponse from a JSON string
v1_sdk_automation_playbook_jobs_job_id_resume_post_response_instance = V1SdkAutomationPlaybookJobsJobIdResumePostResponse.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookJobsJobIdResumePostResponse.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_jobs_job_id_resume_post_response_dict = v1_sdk_automation_playbook_jobs_job_id_resume_post_response_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookJobsJobIdResumePostResponse from a dict
v1_sdk_automation_playbook_jobs_job_id_resume_post_response_from_dict = V1SdkAutomationPlaybookJobsJobIdResumePostResponse.from_dict(v1_sdk_automation_playbook_jobs_job_id_resume_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


