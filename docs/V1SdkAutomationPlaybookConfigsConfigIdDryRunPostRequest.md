# V1SdkAutomationPlaybookConfigsConfigIdDryRunPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verbose_logs** | **bool** | When true, request ansible -vvv for this dry-run | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_configs_config_id_dry_run_post_request import V1SdkAutomationPlaybookConfigsConfigIdDryRunPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookConfigsConfigIdDryRunPostRequest from a JSON string
v1_sdk_automation_playbook_configs_config_id_dry_run_post_request_instance = V1SdkAutomationPlaybookConfigsConfigIdDryRunPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookConfigsConfigIdDryRunPostRequest.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_configs_config_id_dry_run_post_request_dict = v1_sdk_automation_playbook_configs_config_id_dry_run_post_request_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookConfigsConfigIdDryRunPostRequest from a dict
v1_sdk_automation_playbook_configs_config_id_dry_run_post_request_from_dict = V1SdkAutomationPlaybookConfigsConfigIdDryRunPostRequest.from_dict(v1_sdk_automation_playbook_configs_config_id_dry_run_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


