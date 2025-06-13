# V1ExtranetsB2bPost200ResponsePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_name** | **str** |  | [optional] 
**inbound_security_rules** | [**List[V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInner]**](V1ExtranetsB2bConsumerPost200ResponsePolicyInnerInboundSecurityRulesInner.md) |  | [optional] 
**policy** | [**V1ExtranetsB2bPostRequestPolicy**](V1ExtranetsB2bPostRequestPolicy.md) |  | [optional] 
**service_name** | **str** |  | [optional] 
**traffic_rules** | [**List[V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner]**](V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_b2b_post200_response_policy import V1ExtranetsB2bPost200ResponsePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsB2bPost200ResponsePolicy from a JSON string
v1_extranets_b2b_post200_response_policy_instance = V1ExtranetsB2bPost200ResponsePolicy.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsB2bPost200ResponsePolicy.to_json())

# convert the object into a dict
v1_extranets_b2b_post200_response_policy_dict = v1_extranets_b2b_post200_response_policy_instance.to_dict()
# create an instance of V1ExtranetsB2bPost200ResponsePolicy from a dict
v1_extranets_b2b_post200_response_policy_from_dict = V1ExtranetsB2bPost200ResponsePolicy.from_dict(v1_extranets_b2b_post200_response_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


