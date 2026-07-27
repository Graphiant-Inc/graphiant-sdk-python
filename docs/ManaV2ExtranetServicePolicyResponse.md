# ManaV2ExtranetServicePolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**ManaV2ExtranetServiceProducerPolicy**](ManaV2ExtranetServiceProducerPolicy.md) |  | [optional] 
**service_name** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_service_policy_response import ManaV2ExtranetServicePolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetServicePolicyResponse from a JSON string
mana_v2_extranet_service_policy_response_instance = ManaV2ExtranetServicePolicyResponse.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetServicePolicyResponse.to_json())

# convert the object into a dict
mana_v2_extranet_service_policy_response_dict = mana_v2_extranet_service_policy_response_instance.to_dict()
# create an instance of ManaV2ExtranetServicePolicyResponse from a dict
mana_v2_extranet_service_policy_response_from_dict = ManaV2ExtranetServicePolicyResponse.from_dict(mana_v2_extranet_service_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


