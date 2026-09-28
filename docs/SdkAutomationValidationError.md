# SdkAutomationValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable validation error detail | [optional] 
**module_key** | **str** | Catalog module key when the error is scoped to a module; unset otherwise | [optional] 
**type** | **str** | Error category (syntax or schema) | [optional] 

## Example

```python
from graphiant_sdk.models.sdk_automation_validation_error import SdkAutomationValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of SdkAutomationValidationError from a JSON string
sdk_automation_validation_error_instance = SdkAutomationValidationError.from_json(json)
# print the JSON string representation of the object
print(SdkAutomationValidationError.to_json())

# convert the object into a dict
sdk_automation_validation_error_dict = sdk_automation_validation_error_instance.to_dict()
# create an instance of SdkAutomationValidationError from a dict
sdk_automation_validation_error_from_dict = SdkAutomationValidationError.from_dict(sdk_automation_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


