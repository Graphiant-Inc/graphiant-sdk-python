# SdkAutomationPlaybookJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_version** | **str** | graphiant.naas collection version used for this run | [optional] 
**config_description** | **str** | Config description / notes frozen at job creation (from config_snapshot); empty for older jobs | [optional] 
**config_id** | **str** | Owning playbook config id | [optional] 
**config_name** | **str** | Config display name frozen at job creation (from config_snapshot); empty for older jobs | [optional] 
**deploy_ended_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**deploy_started_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**dry_run_ended_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**dry_run_started_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**failed_phase** | **str** | When status is FAILED, which phase failed; unset when not failed | [optional] 
**job_id** | **str** | Unique id of this playbook job run | [optional] 
**logs_available** | **bool** | True when ansible logs are available for this run | [optional] 
**post_deploy_check_started_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**run_duration_ms** | **int** | Wall-clock duration in milliseconds from dry_run_started_at to run_ended_at; unset until run_ended_at is set | [optional] 
**run_ended_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**run_number** | **int** | Per-config run counter (1-based for started runs) | [optional] 
**runner_job_id** | **str** | External ansible runner job id, if the backend assigned one | [optional] 
**sdk_version** | **str** | SDK version used for this run | [optional] 
**started_by_user_id** | **str** | IAM UserInfo.user_id of who started this run; UI resolves the display name | [optional] 
**status** | **str** | Gated pipeline state (dry-run / deploy / post-deploy-check) | [optional] 
**verbose_logs** | **bool** | Whether ansible -vvv was requested for the latest phase of this run | [optional] 

## Example

```python
from graphiant_sdk.models.sdk_automation_playbook_job import SdkAutomationPlaybookJob

# TODO update the JSON string below
json = "{}"
# create an instance of SdkAutomationPlaybookJob from a JSON string
sdk_automation_playbook_job_instance = SdkAutomationPlaybookJob.from_json(json)
# print the JSON string representation of the object
print(SdkAutomationPlaybookJob.to_json())

# convert the object into a dict
sdk_automation_playbook_job_dict = sdk_automation_playbook_job_instance.to_dict()
# create an instance of SdkAutomationPlaybookJob from a dict
sdk_automation_playbook_job_from_dict = SdkAutomationPlaybookJob.from_dict(sdk_automation_playbook_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


