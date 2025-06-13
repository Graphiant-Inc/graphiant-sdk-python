# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSubinterfacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**circuit** | **str** |  | [optional] 
**config_updated_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**description** | **str** |  | [optional] 
**duplex** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**ipv4** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4.md) |  | [optional] 
**ipv6** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4.md) |  | [optional] 
**ipv6_addresses** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4.md) |  | [optional] 
**lan** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**oper_updated_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**parent_mac_address** | **str** |  | [optional] 
**security_zone** | **str** |  | [optional] 
**speed_mbps** | **int** |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**tcp_mss_v4** | **int** |  | [optional] 
**tcp_mss_v6** | **int** |  | [optional] 
**up** | **bool** |  | [optional] 
**vlan** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_subinterfaces_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSubinterfacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSubinterfacesInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_subinterfaces_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSubinterfacesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSubinterfacesInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_subinterfaces_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_subinterfaces_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSubinterfacesInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_subinterfaces_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSubinterfacesInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_subinterfaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


