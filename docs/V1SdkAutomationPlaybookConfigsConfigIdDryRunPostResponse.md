# V1SdkAutomationPlaybookConfigsConfigIdDryRunPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Created job id for the dry-run | [optional] 
**status** | **str** | Initial job status after enqueue (typically QUEUED or DRY_RUNNING) | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_configs_config_id_dry_run_post_response import V1SdkAutomationPlaybookConfigsConfigIdDryRunPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookConfigsConfigIdDryRunPostResponse from a JSON string
v1_sdk_automation_playbook_configs_config_id_dry_run_post_response_instance = V1SdkAutomationPlaybookConfigsConfigIdDryRunPostResponse.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookConfigsConfigIdDryRunPostResponse.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_configs_config_id_dry_run_post_response_dict = v1_sdk_automation_playbook_configs_config_id_dry_run_post_response_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookConfigsConfigIdDryRunPostResponse from a dict
v1_sdk_automation_playbook_configs_config_id_dry_run_post_response_from_dict = V1SdkAutomationPlaybookConfigsConfigIdDryRunPostResponse.from_dict(v1_sdk_automation_playbook_configs_config_id_dry_run_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


