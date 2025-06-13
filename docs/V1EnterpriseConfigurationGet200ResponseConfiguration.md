# V1EnterpriseConfigurationGet200ResponseConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption** | **str** |  | [optional] 
**use_encryption** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_configuration_get200_response_configuration import V1EnterpriseConfigurationGet200ResponseConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseConfigurationGet200ResponseConfiguration from a JSON string
v1_enterprise_configuration_get200_response_configuration_instance = V1EnterpriseConfigurationGet200ResponseConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseConfigurationGet200ResponseConfiguration.to_json())

# convert the object into a dict
v1_enterprise_configuration_get200_response_configuration_dict = v1_enterprise_configuration_get200_response_configuration_instance.to_dict()
# create an instance of V1EnterpriseConfigurationGet200ResponseConfiguration from a dict
v1_enterprise_configuration_get200_response_configuration_from_dict = V1EnterpriseConfigurationGet200ResponseConfiguration.from_dict(v1_enterprise_configuration_get200_response_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


