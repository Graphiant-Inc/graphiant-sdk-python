# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInnerMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** |  | [optional] 
**destination_network** | **str** |  | [optional] 
**destination_port** | **int** |  | [optional] 
**destination_port_range** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange.md) |  | [optional] 
**domain_category_ids** | **List[int]** |  | [optional] 
**domain_wildcards** | **List[str]** |  | [optional] 
**dscp** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDscpMatch**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDscpMatch.md) |  | [optional] 
**icmp_type** | **int** |  | [optional] 
**ip_protocol** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**source_network** | **str** |  | [optional] 
**source_port** | **int** |  | [optional] 
**source_port_range** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_match import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInnerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInnerMatch from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_match_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInnerMatch.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInnerMatch.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_match_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_match_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInnerMatch from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_match_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInnerMatch.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


