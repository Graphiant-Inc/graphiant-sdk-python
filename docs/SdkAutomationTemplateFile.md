# SdkAutomationTemplateFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | File contents, verbatim from the collection | [optional] 
**filename** | **str** | Suggested download name (e.g. sample_interface_config.yaml) | [optional] 
**module_key** | **str** | Catalog module key; empty for the bundle-level playbook not scoped to a slot | [optional] 
**source_path** | **str** | Path within the collection for provenance (e.g. playbooks/interface_management.yml) | [optional] 

## Example

```python
from graphiant_sdk.models.sdk_automation_template_file import SdkAutomationTemplateFile

# TODO update the JSON string below
json = "{}"
# create an instance of SdkAutomationTemplateFile from a JSON string
sdk_automation_template_file_instance = SdkAutomationTemplateFile.from_json(json)
# print the JSON string representation of the object
print(SdkAutomationTemplateFile.to_json())

# convert the object into a dict
sdk_automation_template_file_dict = sdk_automation_template_file_instance.to_dict()
# create an instance of SdkAutomationTemplateFile from a dict
sdk_automation_template_file_from_dict = SdkAutomationTemplateFile.from_dict(sdk_automation_template_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


