# V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**downlink_burst_rate** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleDownlinkBurstRate**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleDownlinkBurstRate.md) |  | [optional] 
**downlink_policer_rate** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleDownlinkBurstRate**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleDownlinkBurstRate.md) |  | [optional] 
**logging** | **bool** |  | [optional] 
**match** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch.md) |  | [optional] 
**name** | **str** |  | [optional] 
**seq** | **int** |  | [optional] 
**uplink_burst_rate** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleDownlinkBurstRate**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleDownlinkBurstRate.md) |  | [optional] 
**uplink_policer_rate** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleDownlinkBurstRate**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleDownlinkBurstRate.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule import V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRule from a JSON string
v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_instance = V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRule.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRule.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_dict = v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRule from a dict
v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_from_dict = V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRule.from_dict(v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


