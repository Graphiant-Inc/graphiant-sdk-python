# V1SdkAutomationPlaybookJobsJobIdRunPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Newly created job id for the re-run | [optional] 
**status** | **str** | Initial status of the new job | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_jobs_job_id_run_post_response import V1SdkAutomationPlaybookJobsJobIdRunPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookJobsJobIdRunPostResponse from a JSON string
v1_sdk_automation_playbook_jobs_job_id_run_post_response_instance = V1SdkAutomationPlaybookJobsJobIdRunPostResponse.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookJobsJobIdRunPostResponse.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_jobs_job_id_run_post_response_dict = v1_sdk_automation_playbook_jobs_job_id_run_post_response_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookJobsJobIdRunPostResponse from a dict
v1_sdk_automation_playbook_jobs_job_id_run_post_response_from_dict = V1SdkAutomationPlaybookJobsJobIdRunPostResponse.from_dict(v1_sdk_automation_playbook_jobs_job_id_run_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


