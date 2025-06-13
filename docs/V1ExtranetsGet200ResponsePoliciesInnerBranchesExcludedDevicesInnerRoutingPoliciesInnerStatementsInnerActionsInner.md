# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_distance** | **int** |  | [optional] 
**aspath_prepend** | **int** |  | [optional] 
**bgp_set_next_hop** | **str** |  | [optional] 
**call_policy** | **str** |  | [optional] 
**community** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunitiesCommunity**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunitiesCommunity.md) |  | [optional] 
**id** | **int** |  | [optional] 
**local_pref** | **int** |  | [optional] 
**metric_absolute** | **int** |  | [optional] 
**metric_modifier** | **int** |  | [optional] 
**result** | **str** |  | [optional] 
**seq** | **int** |  | [optional] 
**weight** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_actions_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerActionsInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_actions_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerActionsInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerActionsInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_actions_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_actions_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerActionsInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_actions_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerActionsInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


