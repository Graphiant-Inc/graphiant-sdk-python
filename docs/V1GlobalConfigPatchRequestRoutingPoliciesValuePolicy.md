# V1GlobalConfigPatchRequestRoutingPoliciesValuePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach_point** | **str** |  | [optional] 
**default_action** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**global_id** | **int** |  | [optional] 
**is_global_sync** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**statements** | [**Dict[str, V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValue]**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_routing_policies_value_policy import V1GlobalConfigPatchRequestRoutingPoliciesValuePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValuePolicy from a JSON string
v1_global_config_patch_request_routing_policies_value_policy_instance = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicy.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestRoutingPoliciesValuePolicy.to_json())

# convert the object into a dict
v1_global_config_patch_request_routing_policies_value_policy_dict = v1_global_config_patch_request_routing_policies_value_policy_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValuePolicy from a dict
v1_global_config_patch_request_routing_policies_value_policy_from_dict = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicy.from_dict(v1_global_config_patch_request_routing_policies_value_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


