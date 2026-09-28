# V1SdkAutomationPlaybookJobsJobIdResumePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deploy** | **bool** | When true, resume straight into deploy; otherwise resume as a dry-run | [optional] 
**verbose_logs** | **bool** | When true, request ansible -vvv for the resumed phase | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_jobs_job_id_resume_post_request import V1SdkAutomationPlaybookJobsJobIdResumePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookJobsJobIdResumePostRequest from a JSON string
v1_sdk_automation_playbook_jobs_job_id_resume_post_request_instance = V1SdkAutomationPlaybookJobsJobIdResumePostRequest.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookJobsJobIdResumePostRequest.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_jobs_job_id_resume_post_request_dict = v1_sdk_automation_playbook_jobs_job_id_resume_post_request_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookJobsJobIdResumePostRequest from a dict
v1_sdk_automation_playbook_jobs_job_id_resume_post_request_from_dict = V1SdkAutomationPlaybookJobsJobIdResumePostRequest.from_dict(v1_sdk_automation_playbook_jobs_job_id_resume_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


