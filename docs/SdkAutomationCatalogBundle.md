# SdkAutomationCatalogBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Short description of the bundle | [optional] 
**key** | **str** | Stable catalog key (e.g. system_bundle); used as CreatePlaybookConfigRequest.bundle_key | [optional] 
**name** | **str** | Display name for the UI picklist | [optional] 

## Example

```python
from graphiant_sdk.models.sdk_automation_catalog_bundle import SdkAutomationCatalogBundle

# TODO update the JSON string below
json = "{}"
# create an instance of SdkAutomationCatalogBundle from a JSON string
sdk_automation_catalog_bundle_instance = SdkAutomationCatalogBundle.from_json(json)
# print the JSON string representation of the object
print(SdkAutomationCatalogBundle.to_json())

# convert the object into a dict
sdk_automation_catalog_bundle_dict = sdk_automation_catalog_bundle_instance.to_dict()
# create an instance of SdkAutomationCatalogBundle from a dict
sdk_automation_catalog_bundle_from_dict = SdkAutomationCatalogBundle.from_dict(sdk_automation_catalog_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


