# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**downlink_burst_rate** | **int** |  | [optional] 
**downlink_policer_rate** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**index** | **int** |  | [optional] 
**logging** | **bool** |  | [optional] 
**match** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInnerMatch**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInnerMatch.md) |  | [optional] 
**name** | **str** |  | [optional] 
**seq** | **int** |  | [optional] 
**uplink_burst_rate** | **int** |  | [optional] 
**uplink_policer_rate** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInnerRulesInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_security_rulesets_inner_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


