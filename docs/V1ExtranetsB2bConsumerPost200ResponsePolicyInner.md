# V1ExtranetsB2bConsumerPost200ResponsePolicyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_lan_segment** | **int** |  | [optional] 
**inbound_security_rules** | [**List[V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInner]**](V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInner.md) |  | [optional] 
**outbound_security_rules** | [**List[V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInner]**](V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInner.md) |  | [optional] 
**restricted_prefixes** | **List[str]** |  | [optional] 
**rules** | [**List[V1ExtranetsB2bConsumerPostRequestPolicyInnerRulesInner]**](V1ExtranetsB2bConsumerPostRequestPolicyInnerRulesInner.md) |  | [optional] 
**traffic_rules** | [**List[V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner]**](V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_consumer_post200_response_policy_inner import V1ExtranetsB2bConsumerPost200ResponsePolicyInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bConsumerPost200ResponsePolicyInner from a JSON string
v1_extranets_b2b_consumer_post200_response_policy_inner_instance = V1ExtranetsB2bConsumerPost200ResponsePolicyInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bConsumerPost200ResponsePolicyInner.to_json())

# convert the object into a dict
v1_extranets_b2b_consumer_post200_response_policy_inner_dict = v1_extranets_b2b_consumer_post200_response_policy_inner_instance.to_dict()
# create an instance of V1ExtranetsB2bConsumerPost200ResponsePolicyInner from a dict
v1_extranets_b2b_consumer_post200_response_policy_inner_from_dict = V1ExtranetsB2bConsumerPost200ResponsePolicyInner.from_dict(v1_extranets_b2b_consumer_post200_response_policy_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


