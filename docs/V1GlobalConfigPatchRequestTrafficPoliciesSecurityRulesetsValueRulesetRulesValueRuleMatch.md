# V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchApplication**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchApplication.md) |  | [optional] 
**content_filter** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchContentFilter**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchContentFilter.md) |  | [optional] 
**destination_network** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationNetwork**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationNetwork.md) |  | [optional] 
**destination_port** | **int** |  | [optional] 
**destination_port_range** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange.md) |  | [optional] 
**domain_list** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDomainList**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDomainList.md) |  | [optional] 
**dscp** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDscp**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDscp.md) |  | [optional] 
**icmp_type** | **int** |  | [optional] 
**ip_protocol** | **str** |  | [optional] 
**protocol** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchProtocol**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchProtocol.md) |  | [optional] 
**source_network** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchSourceNetwork**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchSourceNetwork.md) |  | [optional] 
**source_port** | **int** |  | [optional] 
**source_port_range** | [**V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_match import V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch from a JSON string
v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_match_instance = V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_match_dict = v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_match_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch from a dict
v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_match_from_dict = V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch.from_dict(v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


