# SdkAutomationCatalogModuleSlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_key** | **str** | Owning catalog playbook key (e.g. system_bundle) | [optional] 
**description** | **str** | Short description of the module slot | [optional] 
**file_distinguisher** | **str** | Top-level YAML key from playbook_catalog_module the UI uses to map an uploaded file to this module (e.g. device_system, interfaces, circuits) | [optional] 
**is_required** | **bool** | When true, create/validate must include this module_key | [optional] 
**module_key** | **str** | Stable catalog key from playbook_catalog_module (e.g. system_config_file); used as ModuleFile.module_key | [optional] 
**name** | **str** | Display name for the module slot | [optional] 

## Example

```python
from graphiant_sdk.models.sdk_automation_catalog_module_slot import SdkAutomationCatalogModuleSlot

# TODO update the JSON string below
json = "{}"
# create an instance of SdkAutomationCatalogModuleSlot from a JSON string
sdk_automation_catalog_module_slot_instance = SdkAutomationCatalogModuleSlot.from_json(json)
# print the JSON string representation of the object
print(SdkAutomationCatalogModuleSlot.to_json())

# convert the object into a dict
sdk_automation_catalog_module_slot_dict = sdk_automation_catalog_module_slot_instance.to_dict()
# create an instance of SdkAutomationCatalogModuleSlot from a dict
sdk_automation_catalog_module_slot_from_dict = SdkAutomationCatalogModuleSlot.from_dict(sdk_automation_catalog_module_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


