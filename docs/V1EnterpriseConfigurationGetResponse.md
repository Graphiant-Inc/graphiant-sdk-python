# V1EnterpriseConfigurationGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adaptive_fec_config** | [**ManaV2AdaptiveFecConfiguration**](ManaV2AdaptiveFecConfiguration.md) |  | [optional] 
**configuration** | [**ManaV2EnterpriseConfiguration**](ManaV2EnterpriseConfiguration.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_configuration_get_response import V1EnterpriseConfigurationGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseConfigurationGetResponse from a JSON string
v1_enterprise_configuration_get_response_instance = V1EnterpriseConfigurationGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseConfigurationGetResponse.to_json())

# convert the object into a dict
v1_enterprise_configuration_get_response_dict = v1_enterprise_configuration_get_response_instance.to_dict()
# create an instance of V1EnterpriseConfigurationGetResponse from a dict
v1_enterprise_configuration_get_response_from_dict = V1EnterpriseConfigurationGetResponse.from_dict(v1_enterprise_configuration_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


