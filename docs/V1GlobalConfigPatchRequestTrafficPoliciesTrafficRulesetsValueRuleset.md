# V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRuleset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**global_id** | **int** |  | [optional] 
**is_global_sync** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**rules** | [**Dict[str, V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValue]**](V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset import V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRuleset from a JSON string
v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_instance = V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRuleset.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRuleset.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_dict = v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRuleset from a dict
v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_from_dict = V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRuleset.from_dict(v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


