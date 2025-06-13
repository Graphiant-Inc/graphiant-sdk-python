# V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatement**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatement.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_routing_policies_value_policy_statements_value import V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValue from a JSON string
v1_global_config_patch_request_routing_policies_value_policy_statements_value_instance = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValue.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValue.to_json())

# convert the object into a dict
v1_global_config_patch_request_routing_policies_value_policy_statements_value_dict = v1_global_config_patch_request_routing_policies_value_policy_statements_value_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValue from a dict
v1_global_config_patch_request_routing_policies_value_policy_statements_value_from_dict = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValue.from_dict(v1_global_config_patch_request_routing_policies_value_policy_statements_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


