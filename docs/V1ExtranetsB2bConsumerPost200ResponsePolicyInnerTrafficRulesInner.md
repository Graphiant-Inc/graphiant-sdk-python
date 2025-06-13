# V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInnerAction**](V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInnerAction.md) |  | [optional] 
**match** | [**V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInnerMatch**](V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInnerMatch.md) |  | [optional] 
**policy_rule_index** | **int** |  | [optional] 
**seq** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_consumer_post200_response_policy_inner_traffic_rules_inner import V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner from a JSON string
v1_extranets_b2b_consumer_post200_response_policy_inner_traffic_rules_inner_instance = V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner.to_json())

# convert the object into a dict
v1_extranets_b2b_consumer_post200_response_policy_inner_traffic_rules_inner_dict = v1_extranets_b2b_consumer_post200_response_policy_inner_traffic_rules_inner_instance.to_dict()
# create an instance of V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner from a dict
v1_extranets_b2b_consumer_post200_response_policy_inner_traffic_rules_inner_from_dict = V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner.from_dict(v1_extranets_b2b_consumer_post200_response_policy_inner_traffic_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


