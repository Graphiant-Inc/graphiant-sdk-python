# V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_distance** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionAdministrativeDistance**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionAdministrativeDistance.md) |  | [optional] 
**aspath_prepend** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionAspathPrepend**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionAspathPrepend.md) |  | [optional] 
**bgp_set_next_hop** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionBgpSetNextHop**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionBgpSetNextHop.md) |  | [optional] 
**call_policy** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCallPolicy**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCallPolicy.md) |  | [optional] 
**communities** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities.md) |  | [optional] 
**local_pref** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionLocalPref**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionLocalPref.md) |  | [optional] 
**metric** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionMetric**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionMetric.md) |  | [optional] 
**result** | **str** |  | [optional] 
**seq** | **int** |  | [optional] 
**weight** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionWeight**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionWeight.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_actions_value_action import V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueAction

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueAction from a JSON string
v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_actions_value_action_instance = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueAction.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueAction.to_json())

# convert the object into a dict
v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_actions_value_action_dict = v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_actions_value_action_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueAction from a dict
v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_actions_value_action_from_dict = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueAction.from_dict(v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_actions_value_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


