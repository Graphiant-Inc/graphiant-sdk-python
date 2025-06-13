# V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction**](V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction.md) |  | [optional] 
**description** | **str** |  | [optional] 
**match** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch.md) |  | [optional] 
**name** | **str** |  | [optional] 
**seq** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule import V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule from a JSON string
v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_instance = V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_dict = v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule from a dict
v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_from_dict = V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule.from_dict(v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


