# V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_rules** | [**List[V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseSecurityRulesInner]**](V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseSecurityRulesInner.md) |  | [optional] 
**traffic_rules** | [**List[V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseTrafficRulesInner]**](V1ExtranetsMonitoringTrafficSecurityPolicyPost200ResponseTrafficRulesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_monitoring_traffic_security_policy_post200_response import V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response from a JSON string
v1_extranets_monitoring_traffic_security_policy_post200_response_instance = V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response.to_json())

# convert the object into a dict
v1_extranets_monitoring_traffic_security_policy_post200_response_dict = v1_extranets_monitoring_traffic_security_policy_post200_response_instance.to_dict()
# create an instance of V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response from a dict
v1_extranets_monitoring_traffic_security_policy_post200_response_from_dict = V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response.from_dict(v1_extranets_monitoring_traffic_security_policy_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


