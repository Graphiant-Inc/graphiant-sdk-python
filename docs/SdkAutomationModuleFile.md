# SdkAutomationModuleFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | YAML file contents | [optional] 
**filename** | **str** | Original upload filename (informational; not used for routing) | [optional] 
**module_key** | **str** | Catalog key from playbook_catalog_module (e.g. system_config_file) | [optional] 

## Example

```python
from graphiant_sdk.models.sdk_automation_module_file import SdkAutomationModuleFile

# TODO update the JSON string below
json = "{}"
# create an instance of SdkAutomationModuleFile from a JSON string
sdk_automation_module_file_instance = SdkAutomationModuleFile.from_json(json)
# print the JSON string representation of the object
print(SdkAutomationModuleFile.to_json())

# convert the object into a dict
sdk_automation_module_file_dict = sdk_automation_module_file_instance.to_dict()
# create an instance of SdkAutomationModuleFile from a dict
sdk_automation_module_file_from_dict = SdkAutomationModuleFile.from_dict(sdk_automation_module_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


