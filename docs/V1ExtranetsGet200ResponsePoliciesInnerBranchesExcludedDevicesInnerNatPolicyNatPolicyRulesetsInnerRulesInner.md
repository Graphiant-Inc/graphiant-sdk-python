# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerNatPolicyNatPolicyRulesetsInnerRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertise_pre_nat_prefixes** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**index** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**original_dst_ip_prefix** | **str** |  | [optional] 
**original_src_ip_prefix** | **str** |  | [optional] 
**seq** | **int** |  | [optional] 
**translated_dst_ip_prefix** | **str** |  | [optional] 
**translated_src_ip_prefix** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_nat_policy_nat_policy_rulesets_inner_rules_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerNatPolicyNatPolicyRulesetsInnerRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerNatPolicyNatPolicyRulesetsInnerRulesInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_nat_policy_nat_policy_rulesets_inner_rules_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerNatPolicyNatPolicyRulesetsInnerRulesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerNatPolicyNatPolicyRulesetsInnerRulesInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_nat_policy_nat_policy_rulesets_inner_rules_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_nat_policy_nat_policy_rulesets_inner_rules_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerNatPolicyNatPolicyRulesetsInnerRulesInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_nat_policy_nat_policy_rulesets_inner_rules_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerNatPolicyNatPolicyRulesetsInnerRulesInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_nat_policy_nat_policy_rulesets_inner_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


