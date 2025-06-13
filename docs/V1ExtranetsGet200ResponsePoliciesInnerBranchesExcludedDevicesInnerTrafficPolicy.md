# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dpi_applications** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyDpiApplicationsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyDpiApplicationsInner.md) |  | [optional] 
**network_lists** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyNetworkListsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyNetworkListsInner.md) |  | [optional] 
**port_lists** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyPortListsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyPortListsInner.md) |  | [optional] 
**security_rulesets** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicySecurityRulesetsInner.md) |  | [optional] 
**traffic_rulesets** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyTrafficRulesetsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyTrafficRulesetsInner.md) |  | [optional] 
**zone_firewalls** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyZoneFirewallsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyZoneFirewallsInner.md) |  | [optional] 
**zone_pairs** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyZonePairsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicyZonePairsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicy from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicy.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicy.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicy from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerTrafficPolicy.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_traffic_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


