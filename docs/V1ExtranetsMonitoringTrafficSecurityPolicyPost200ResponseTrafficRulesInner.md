# V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseTrafficRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSiteDevicesInner**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSiteDevicesInner.md) |  | [optional] 
**traffic_policy_rule** | [**V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner**](V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner.md) |  | [optional] 
**vrf_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_monitoring_traffic_security_policy_post200_response_traffic_rules_inner import V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseTrafficRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseTrafficRulesInner from a JSON string
v1_extranets_monitoring_traffic_security_policy_post200_response_traffic_rules_inner_instance = V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseTrafficRulesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseTrafficRulesInner.to_json())

# convert the object into a dict
v1_extranets_monitoring_traffic_security_policy_post200_response_traffic_rules_inner_dict = v1_extranets_monitoring_traffic_security_policy_post200_response_traffic_rules_inner_instance.to_dict()
# create an instance of V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseTrafficRulesInner from a dict
v1_extranets_monitoring_traffic_security_policy_post200_response_traffic_rules_inner_from_dict = V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseTrafficRulesInner.from_dict(v1_extranets_monitoring_traffic_security_policy_post200_response_traffic_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


