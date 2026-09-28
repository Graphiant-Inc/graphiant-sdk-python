# SdkAutomationPlaybookConfigSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Config id | [optional] 
**created_by_user_id** | **str** | IAM user id of the config creator; UI resolves the display name | [optional] 
**job_status** | **str** | Latest run status; unset when the config has no run yet | [optional] 
**name** | **str** | Display name | [optional] 
**run_id** | **str** | Latest job id for this config; empty if never run | [optional] 
**run_number** | **int** | Per-config run counter; 0 if never run | [optional] 
**started_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**started_by_user_id** | **str** | IAM user id of who launched the latest run | [optional] 
**status** | **str** | Config lifecycle status | [optional] 
**updated_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.sdk_automation_playbook_config_summary import SdkAutomationPlaybookConfigSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SdkAutomationPlaybookConfigSummary from a JSON string
sdk_automation_playbook_config_summary_instance = SdkAutomationPlaybookConfigSummary.from_json(json)
# print the JSON string representation of the object
print(SdkAutomationPlaybookConfigSummary.to_json())

# convert the object into a dict
sdk_automation_playbook_config_summary_dict = sdk_automation_playbook_config_summary_instance.to_dict()
# create an instance of SdkAutomationPlaybookConfigSummary from a dict
sdk_automation_playbook_config_summary_from_dict = SdkAutomationPlaybookConfigSummary.from_dict(sdk_automation_playbook_config_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


