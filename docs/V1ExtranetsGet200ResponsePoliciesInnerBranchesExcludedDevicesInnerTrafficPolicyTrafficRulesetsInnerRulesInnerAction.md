# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyTrafficRulesetsInnerRulesInnerAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_circuit** | **str** |  | [optional] 
**backup_circuit_label** | **str** |  | [optional] 
**egress** | **str** |  | [optional] 
**logging** | **bool** |  | [optional] 
**primary_circuit** | **str** |  | [optional] 
**primary_circuit_label** | **str** |  | [optional] 
**remark** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDscpMatch**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDscpMatch.md) |  | [optional] 
**sla_class** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_traffic_rulesets_inner_rules_inner_action import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyTrafficRulesetsInnerRulesInnerAction

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyTrafficRulesetsInnerRulesInnerAction from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_traffic_rulesets_inner_rules_inner_action_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyTrafficRulesetsInnerRulesInnerAction.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyTrafficRulesetsInnerRulesInnerAction.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_traffic_rulesets_inner_rules_inner_action_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_traffic_rulesets_inner_rules_inner_action_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyTrafficRulesetsInnerRulesInnerAction from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_traffic_rulesets_inner_rules_inner_action_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyTrafficRulesetsInnerRulesInnerAction.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_traffic_rulesets_inner_rules_inner_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


