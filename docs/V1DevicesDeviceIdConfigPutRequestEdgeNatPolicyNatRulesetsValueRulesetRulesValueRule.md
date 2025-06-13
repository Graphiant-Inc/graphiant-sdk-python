# V1DevicesDeviceIdConfigPutRequestEdgeNatPolicyNatRulesetsValueRulesetRulesValueRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertise_pre_nat_prefixes** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**original_dst_ip_prefix** | **str** |  | [optional] 
**original_src_ip_prefix** | **str** |  | [optional] 
**seq** | **int** |  | [optional] 
**translated_dst_ip_prefix** | **str** |  | [optional] 
**translated_src_ip_prefix** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_nat_policy_nat_rulesets_value_ruleset_rules_value_rule import V1DevicesDeviceIdConfigPutRequestEdgeNatPolicyNatRulesetsValueRulesetRulesValueRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeNatPolicyNatRulesetsValueRulesetRulesValueRule from a JSON string
v1_devices_device_id_config_put_request_edge_nat_policy_nat_rulesets_value_ruleset_rules_value_rule_instance = V1DevicesDeviceIdConfigPutRequestEdgeNatPolicyNatRulesetsValueRulesetRulesValueRule.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestEdgeNatPolicyNatRulesetsValueRulesetRulesValueRule.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_edge_nat_policy_nat_rulesets_value_ruleset_rules_value_rule_dict = v1_devices_device_id_config_put_request_edge_nat_policy_nat_rulesets_value_ruleset_rules_value_rule_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeNatPolicyNatRulesetsValueRulesetRulesValueRule from a dict
v1_devices_device_id_config_put_request_edge_nat_policy_nat_rulesets_value_ruleset_rules_value_rule_from_dict = V1DevicesDeviceIdConfigPutRequestEdgeNatPolicyNatRulesetsValueRulesetRulesValueRule.from_dict(v1_devices_device_id_config_put_request_edge_nat_policy_nat_rulesets_value_ruleset_rules_value_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


