# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**circuit** | **str** |  | [optional] 
**circuit_name** | **str** |  | [optional] 
**config_updated_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**configured_max_transmission_unit** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**duplex** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**ip_sec** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpSec**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpSec.md) |  | [optional] 
**ipv4** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4.md) |  | [optional] 
**ipv6** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4.md) |  | [optional] 
**ipv6_addresses** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4.md) |  | [optional] 
**lan** | **str** |  | [optional] 
**lldp_enabled** | **bool** |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**oper_updated_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**phy_address** | **str** |  | [optional] 
**security_zone** | **str** |  | [optional] 
**sfp_optical_strength** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSfpOpticalStrengthInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSfpOpticalStrengthInner.md) |  | [optional] 
**speed_mbps** | **int** |  | [optional] 
**subinterfaces** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSubinterfacesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerSubinterfacesInner.md) |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**tcp_mss_v4** | **int** |  | [optional] 
**tcp_mss_v6** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**up** | **bool** |  | [optional] 
**vrf_function_id** | **int** |  | [optional] 
**vrf_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


