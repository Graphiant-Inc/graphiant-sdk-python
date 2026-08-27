# ManaV2AdaptiveFecConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adaptive_fec_enabled** | **bool** |  | [optional] 
**sla_classes** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_adaptive_fec_configuration import ManaV2AdaptiveFecConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2AdaptiveFecConfiguration from a JSON string
mana_v2_adaptive_fec_configuration_instance = ManaV2AdaptiveFecConfiguration.from_json(json)
# print the JSON string representation of the object
print(ManaV2AdaptiveFecConfiguration.to_json())

# convert the object into a dict
mana_v2_adaptive_fec_configuration_dict = mana_v2_adaptive_fec_configuration_instance.to_dict()
# create an instance of ManaV2AdaptiveFecConfiguration from a dict
mana_v2_adaptive_fec_configuration_from_dict = ManaV2AdaptiveFecConfiguration.from_dict(mana_v2_adaptive_fec_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


