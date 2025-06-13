# V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInnerMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_port** | **int** |  | [optional] 
**destination_prefix** | **str** |  | [optional] 
**icmp_type** | **int** |  | [optional] 
**protocol** | **int** |  | [optional] 
**source_port** | **int** |  | [optional] 
**source_prefix** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_consumer_post200_response_policy_inner_inbound_security_rules_inner_match import V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInnerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInnerMatch from a JSON string
v1_extranets_b2b_consumer_post200_response_policy_inner_inbound_security_rules_inner_match_instance = V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInnerMatch.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInnerMatch.to_json())

# convert the object into a dict
v1_extranets_b2b_consumer_post200_response_policy_inner_inbound_security_rules_inner_match_dict = v1_extranets_b2b_consumer_post200_response_policy_inner_inbound_security_rules_inner_match_instance.to_dict()
# create an instance of V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInnerMatch from a dict
v1_extranets_b2b_consumer_post200_response_policy_inner_inbound_security_rules_inner_match_from_dict = V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInnerMatch.from_dict(v1_extranets_b2b_consumer_post200_response_policy_inner_inbound_security_rules_inner_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


