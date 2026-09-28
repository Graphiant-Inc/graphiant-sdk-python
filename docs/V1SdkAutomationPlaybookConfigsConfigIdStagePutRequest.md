# V1SdkAutomationPlaybookConfigsConfigIdStagePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Deployment notes shown in the pending-executions UI | [optional] 
**name** | **str** | Required display name for the staged config | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_configs_config_id_stage_put_request import V1SdkAutomationPlaybookConfigsConfigIdStagePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookConfigsConfigIdStagePutRequest from a JSON string
v1_sdk_automation_playbook_configs_config_id_stage_put_request_instance = V1SdkAutomationPlaybookConfigsConfigIdStagePutRequest.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookConfigsConfigIdStagePutRequest.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_configs_config_id_stage_put_request_dict = v1_sdk_automation_playbook_configs_config_id_stage_put_request_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookConfigsConfigIdStagePutRequest from a dict
v1_sdk_automation_playbook_configs_config_id_stage_put_request_from_dict = V1SdkAutomationPlaybookConfigsConfigIdStagePutRequest.from_dict(v1_sdk_automation_playbook_configs_config_id_stage_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


