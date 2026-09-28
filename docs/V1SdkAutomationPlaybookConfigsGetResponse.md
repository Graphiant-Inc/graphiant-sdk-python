# V1SdkAutomationPlaybookConfigsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[SdkAutomationPlaybookConfigSummary]**](SdkAutomationPlaybookConfigSummary.md) |  | [optional] 
**page_info** | [**CommonPageInfo**](CommonPageInfo.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_configs_get_response import V1SdkAutomationPlaybookConfigsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookConfigsGetResponse from a JSON string
v1_sdk_automation_playbook_configs_get_response_instance = V1SdkAutomationPlaybookConfigsGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookConfigsGetResponse.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_configs_get_response_dict = v1_sdk_automation_playbook_configs_get_response_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookConfigsGetResponse from a dict
v1_sdk_automation_playbook_configs_get_response_from_dict = V1SdkAutomationPlaybookConfigsGetResponse.from_dict(v1_sdk_automation_playbook_configs_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


