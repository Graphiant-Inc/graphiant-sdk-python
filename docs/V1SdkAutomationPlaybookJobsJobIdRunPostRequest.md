# V1SdkAutomationPlaybookJobsJobIdRunPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_dry_run** | **bool** | When true, skip dry-run and gate and deploy directly | [optional] 
**verbose_logs** | **bool** | When true, request ansible -vvv for the new run | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_jobs_job_id_run_post_request import V1SdkAutomationPlaybookJobsJobIdRunPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookJobsJobIdRunPostRequest from a JSON string
v1_sdk_automation_playbook_jobs_job_id_run_post_request_instance = V1SdkAutomationPlaybookJobsJobIdRunPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookJobsJobIdRunPostRequest.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_jobs_job_id_run_post_request_dict = v1_sdk_automation_playbook_jobs_job_id_run_post_request_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookJobsJobIdRunPostRequest from a dict
v1_sdk_automation_playbook_jobs_job_id_run_post_request_from_dict = V1SdkAutomationPlaybookJobsJobIdRunPostRequest.from_dict(v1_sdk_automation_playbook_jobs_job_id_run_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


