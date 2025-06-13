# V1GlobalConfigPatchRequestTrafficPolicies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dpi_applications** | [**Dict[str, V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValue]**](V1GlobalConfigPatchRequestTrafficPoliciesDpiApplicationsValue.md) |  | [optional] 
**network_lists** | [**Dict[str, V1GlobalConfigPatchRequestTrafficPoliciesNetworkListsValue]**](V1GlobalConfigPatchRequestTrafficPoliciesNetworkListsValue.md) |  | [optional] 
**port_lists** | [**Dict[str, V1GlobalConfigPatchRequestTrafficPoliciesPortListsValue]**](V1GlobalConfigPatchRequestTrafficPoliciesPortListsValue.md) |  | [optional] 
**security_rulesets** | [**Dict[str, V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValue]**](V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValue.md) |  | [optional] 
**traffic_rulesets** | [**Dict[str, V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValue]**](V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValue.md) |  | [optional] 
**zone_firewalls** | [**Dict[str, V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValue]**](V1GlobalConfigPatchRequestTrafficPoliciesZoneFirewallsValue.md) |  | [optional] 
**zones** | [**Dict[str, V1GlobalConfigPatchRequestTrafficPoliciesZonesValue]**](V1GlobalConfigPatchRequestTrafficPoliciesZonesValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies import V1GlobalConfigPatchRequestTrafficPolicies

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestTrafficPolicies from a JSON string
v1_global_config_patch_request_traffic_policies_instance = V1GlobalConfigPatchRequestTrafficPolicies.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestTrafficPolicies.to_json())

# convert the object into a dict
v1_global_config_patch_request_traffic_policies_dict = v1_global_config_patch_request_traffic_policies_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestTrafficPolicies from a dict
v1_global_config_patch_request_traffic_policies_from_dict = V1GlobalConfigPatchRequestTrafficPolicies.from_dict(v1_global_config_patch_request_traffic_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


