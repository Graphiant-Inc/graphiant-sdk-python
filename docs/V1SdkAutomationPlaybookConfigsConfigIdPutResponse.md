# V1SdkAutomationPlaybookConfigsConfigIdPutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[SdkAutomationValidationError]**](SdkAutomationValidationError.md) |  | [optional] 
**is_valid** | **bool** | True when validation succeeded and the update was applied | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_configs_config_id_put_response import V1SdkAutomationPlaybookConfigsConfigIdPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookConfigsConfigIdPutResponse from a JSON string
v1_sdk_automation_playbook_configs_config_id_put_response_instance = V1SdkAutomationPlaybookConfigsConfigIdPutResponse.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookConfigsConfigIdPutResponse.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_configs_config_id_put_response_dict = v1_sdk_automation_playbook_configs_config_id_put_response_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookConfigsConfigIdPutResponse from a dict
v1_sdk_automation_playbook_configs_config_id_put_response_from_dict = V1SdkAutomationPlaybookConfigsConfigIdPutResponse.from_dict(v1_sdk_automation_playbook_configs_config_id_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


