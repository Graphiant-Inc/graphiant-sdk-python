# V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRuleset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**global_id** | **int** |  | [optional] 
**is_global_sync** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**rules** | [**Dict[str, V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValue]**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset import V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRuleset from a JSON string
v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_instance = V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRuleset.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRuleset.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_dict = v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRuleset from a dict
v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_from_dict = V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRuleset.from_dict(v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


