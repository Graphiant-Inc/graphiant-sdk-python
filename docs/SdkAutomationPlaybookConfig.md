# SdkAutomationPlaybookConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_key** | **str** | Catalog key from playbook_catalog_playbook (e.g. system_bundle) | [optional] 
**config_id** | **str** | Config id | [optional] 
**created_by_user_id** | **str** | IAM user id of the config creator; UI resolves the display name | [optional] 
**description** | **str** | Description / deployment notes | [optional] 
**files** | [**List[SdkAutomationModuleFile]**](SdkAutomationModuleFile.md) |  | [optional] 
**name** | **str** | Display name | [optional] 
**status** | **str** | Config lifecycle status (draft / staged / paused) | [optional] 

## Example

```python
from graphiant_sdk.models.sdk_automation_playbook_config import SdkAutomationPlaybookConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SdkAutomationPlaybookConfig from a JSON string
sdk_automation_playbook_config_instance = SdkAutomationPlaybookConfig.from_json(json)
# print the JSON string representation of the object
print(SdkAutomationPlaybookConfig.to_json())

# convert the object into a dict
sdk_automation_playbook_config_dict = sdk_automation_playbook_config_instance.to_dict()
# create an instance of SdkAutomationPlaybookConfig from a dict
sdk_automation_playbook_config_from_dict = SdkAutomationPlaybookConfig.from_dict(sdk_automation_playbook_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


