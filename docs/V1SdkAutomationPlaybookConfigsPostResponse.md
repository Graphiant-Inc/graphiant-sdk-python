# V1SdkAutomationPlaybookConfigsPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Created config id when validation succeeds and validate_only is false; empty otherwise | [optional] 
**errors** | [**List[SdkAutomationValidationError]**](SdkAutomationValidationError.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_configs_post_response import V1SdkAutomationPlaybookConfigsPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookConfigsPostResponse from a JSON string
v1_sdk_automation_playbook_configs_post_response_instance = V1SdkAutomationPlaybookConfigsPostResponse.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookConfigsPostResponse.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_configs_post_response_dict = v1_sdk_automation_playbook_configs_post_response_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookConfigsPostResponse from a dict
v1_sdk_automation_playbook_configs_post_response_from_dict = V1SdkAutomationPlaybookConfigsPostResponse.from_dict(v1_sdk_automation_playbook_configs_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


