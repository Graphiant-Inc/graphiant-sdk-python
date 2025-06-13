# V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchCommunity**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchCommunity.md) |  | [optional] 
**prefix_set** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchPrefixSet**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchPrefixSet.md) |  | [optional] 
**protocol_route_type** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchProtocolRouteType**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchProtocolRouteType.md) |  | [optional] 
**route_tag** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchRouteTag**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchRouteTag.md) |  | [optional] 
**seq** | **int** |  | [optional] 
**source_interface** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchSourceInterface**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchSourceInterface.md) |  | [optional] 
**source_protocol** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchSourceProtocol**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchSourceProtocol.md) |  | [optional] 
**stale** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchStale**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchStale.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_matches_value_match import V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatch

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatch from a JSON string
v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_matches_value_match_instance = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatch.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatch.to_json())

# convert the object into a dict
v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_matches_value_match_dict = v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_matches_value_match_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatch from a dict
v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_matches_value_match_from_dict = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatch.from_dict(v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_matches_value_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


