# V1GlobalConfigPatchRequestRoutingPoliciesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicy**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicy.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_routing_policies_value import V1GlobalConfigPatchRequestRoutingPoliciesValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValue from a JSON string
v1_global_config_patch_request_routing_policies_value_instance = V1GlobalConfigPatchRequestRoutingPoliciesValue.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestRoutingPoliciesValue.to_json())

# convert the object into a dict
v1_global_config_patch_request_routing_policies_value_dict = v1_global_config_patch_request_routing_policies_value_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValue from a dict
v1_global_config_patch_request_routing_policies_value_from_dict = V1GlobalConfigPatchRequestRoutingPoliciesValue.from_dict(v1_global_config_patch_request_routing_policies_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


