# V1SdkAutomationPlaybookJobsJobIdApprovePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verbose_logs** | **bool** | When true, request ansible -vvv for the deploy phase | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_jobs_job_id_approve_put_request import V1SdkAutomationPlaybookJobsJobIdApprovePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookJobsJobIdApprovePutRequest from a JSON string
v1_sdk_automation_playbook_jobs_job_id_approve_put_request_instance = V1SdkAutomationPlaybookJobsJobIdApprovePutRequest.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookJobsJobIdApprovePutRequest.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_jobs_job_id_approve_put_request_dict = v1_sdk_automation_playbook_jobs_job_id_approve_put_request_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookJobsJobIdApprovePutRequest from a dict
v1_sdk_automation_playbook_jobs_job_id_approve_put_request_from_dict = V1SdkAutomationPlaybookJobsJobIdApprovePutRequest.from_dict(v1_sdk_automation_playbook_jobs_job_id_approve_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


