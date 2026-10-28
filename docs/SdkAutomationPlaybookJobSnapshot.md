# SdkAutomationPlaybookJobSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_key** | **str** | Catalog bundle key frozen at job creation | [optional] 
**config_id** | **str** | Config id that owned this run when the snapshot was taken | [optional] 
**description** | **str** | Config notes frozen at job creation; empty for older jobs | [optional] 
**files** | [**List[SdkAutomationModuleFile]**](SdkAutomationModuleFile.md) |  | [optional] 
**job_id** | **str** | Owning job id | [optional] 
**name** | **str** | Config display name frozen at job creation; empty for older jobs | [optional] 
**playbook** | **str** | Playbook filename frozen at job creation (e.g. network_bundle.yml); empty for older jobs | [optional] 
**tags** | **str** | Ansible --tags frozen at job creation (union of present modules&#39; associated_tags); empty for older jobs or when no tags were applied | [optional] 

## Example

```python
from graphiant_sdk.models.sdk_automation_playbook_job_snapshot import SdkAutomationPlaybookJobSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of SdkAutomationPlaybookJobSnapshot from a JSON string
sdk_automation_playbook_job_snapshot_instance = SdkAutomationPlaybookJobSnapshot.from_json(json)
# print the JSON string representation of the object
print(SdkAutomationPlaybookJobSnapshot.to_json())

# convert the object into a dict
sdk_automation_playbook_job_snapshot_dict = sdk_automation_playbook_job_snapshot_instance.to_dict()
# create an instance of SdkAutomationPlaybookJobSnapshot from a dict
sdk_automation_playbook_job_snapshot_from_dict = SdkAutomationPlaybookJobSnapshot.from_dict(sdk_automation_playbook_job_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


