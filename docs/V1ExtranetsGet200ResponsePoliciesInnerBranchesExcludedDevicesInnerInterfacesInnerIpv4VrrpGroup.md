# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_mode** | **bool** |  | [optional] 
**allow_inter_operability** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**effective_priority** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**group_members** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroupGroupMembersInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroupGroupMembersInner.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**preempt** | **bool** |  | [optional] 
**priority** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**tracked_interfaces** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroupTrackedInterfacesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroupTrackedInterfacesInner.md) |  | [optional] 
**virtual_ip_address** | **str** |  | [optional] 
**virtual_mac_address** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


