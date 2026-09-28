# V1SdkAutomationPlaybookConfigsConfigIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Optional description / notes update | [optional] 
**files** | [**List[SdkAutomationModuleFile]**](SdkAutomationModuleFile.md) |  | [optional] 
**name** | **str** | Optional display name update | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sdk_automation_playbook_configs_config_id_put_request import V1SdkAutomationPlaybookConfigsConfigIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SdkAutomationPlaybookConfigsConfigIdPutRequest from a JSON string
v1_sdk_automation_playbook_configs_config_id_put_request_instance = V1SdkAutomationPlaybookConfigsConfigIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1SdkAutomationPlaybookConfigsConfigIdPutRequest.to_json())

# convert the object into a dict
v1_sdk_automation_playbook_configs_config_id_put_request_dict = v1_sdk_automation_playbook_configs_config_id_put_request_instance.to_dict()
# create an instance of V1SdkAutomationPlaybookConfigsConfigIdPutRequest from a dict
v1_sdk_automation_playbook_configs_config_id_put_request_from_dict = V1SdkAutomationPlaybookConfigsConfigIdPutRequest.from_dict(v1_sdk_automation_playbook_configs_config_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


