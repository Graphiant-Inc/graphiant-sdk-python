# V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**Dict[str, V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValue]**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValue.md) |  | [optional] 
**matches** | [**Dict[str, V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValue]**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValue.md) |  | [optional] 
**seq** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement import V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatement

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatement from a JSON string
v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_instance = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatement.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatement.to_json())

# convert the object into a dict
v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_dict = v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatement from a dict
v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_from_dict = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatement.from_dict(v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


