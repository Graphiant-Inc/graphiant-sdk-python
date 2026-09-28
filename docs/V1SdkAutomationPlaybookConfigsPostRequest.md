# V1SdkAutomationPlaybookConfigsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_key** | **str** | Catalog key from playbook_catalog_playbook (e.g. system_bundle) | [optional] 
**files** | [**List[SdkAutomationModuleFile]**](SdkAutomationModuleFile.md) |  | [optional] 
**validate_only** | **bool** | When true, validate without persisting (Validate Bundle); when false, create on success | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_configs_post_request import V1SdkAutomationPlaybookConfigsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookConfigsPostRequest from a JSON string
v1_sdk_automation_playbook_configs_post_request_instance = V1SdkAutomationPlaybookConfigsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookConfigsPostRequest.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_configs_post_request_dict = v1_sdk_automation_playbook_configs_post_request_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookConfigsPostRequest from a dict
v1_sdk_automation_playbook_configs_post_request_from_dict = V1SdkAutomationPlaybookConfigsPostRequest.from_dict(v1_sdk_automation_playbook_configs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


