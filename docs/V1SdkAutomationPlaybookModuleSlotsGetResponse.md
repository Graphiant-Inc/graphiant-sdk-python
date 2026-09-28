# V1SdkAutomationPlaybookModuleSlotsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modules** | [**List[SdkAutomationCatalogModuleSlot]**](SdkAutomationCatalogModuleSlot.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_module_slots_get_response import V1SdkAutomationPlaybookModuleSlotsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookModuleSlotsGetResponse from a JSON string
v1_sdk_automation_playbook_module_slots_get_response_instance = V1SdkAutomationPlaybookModuleSlotsGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookModuleSlotsGetResponse.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_module_slots_get_response_dict = v1_sdk_automation_playbook_module_slots_get_response_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookModuleSlotsGetResponse from a dict
v1_sdk_automation_playbook_module_slots_get_response_from_dict = V1SdkAutomationPlaybookModuleSlotsGetResponse.from_dict(v1_sdk_automation_playbook_module_slots_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


