# V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_circuit** | [**V1PortalApikeysPostRequest**](V1PortalApikeysPostRequest.md) |  | [optional] 
**backup_circuit_label** | [**V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleActionBackupCircuitLabel**](V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleActionBackupCircuitLabel.md) |  | [optional] 
**egress** | **str** |  | [optional] 
**logging** | **bool** |  | [optional] 
**primary_circuit** | [**V1PortalApikeysPostRequest**](V1PortalApikeysPostRequest.md) |  | [optional] 
**primary_circuit_label** | [**V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleActionBackupCircuitLabel**](V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleActionBackupCircuitLabel.md) |  | [optional] 
**remark** | [**V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleActionRemark**](V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleActionRemark.md) |  | [optional] 
**set_sla_class** | [**V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleActionSetSlaClass**](V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleActionSetSlaClass.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action import V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction from a JSON string
v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action_instance = V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action_dict = v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction from a dict
v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action_from_dict = V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction.from_dict(v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


