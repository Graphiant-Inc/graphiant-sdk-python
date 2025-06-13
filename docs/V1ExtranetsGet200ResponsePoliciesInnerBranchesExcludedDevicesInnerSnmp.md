# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communities** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpCommunitiesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpCommunitiesInner.md) |  | [optional] 
**engine_enable_authen_traps** | **bool** |  | [optional] 
**engine_enable_high_memory_traps** | **bool** |  | [optional] 
**engine_enable_high_cpu_traps** | **bool** |  | [optional] 
**engine_enable_local_acess_v4** | **bool** |  | [optional] 
**engine_enable_local_acess_v6** | **bool** |  | [optional] 
**engine_enable_user_hints** | **bool** |  | [optional] 
**engine_enable_user_validation** | **bool** |  | [optional] 
**engine_enabled** | **bool** |  | [optional] 
**engine_endpoints** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpEngineEndpointsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpEngineEndpointsInner.md) |  | [optional] 
**engine_id_admin_octets** | **str** |  | [optional] 
**engine_id_admin_text** | **str** |  | [optional] 
**engine_id_ipv4** | **str** |  | [optional] 
**engine_id_ipv6** | **str** |  | [optional] 
**engine_id_mac** | **str** |  | [optional] 
**engine_id_raw** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**global_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**notify_filter_profiles** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInner.md) |  | [optional] 
**status** | **str** |  | [optional] 
**targets** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpTargetsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpTargetsInner.md) |  | [optional] 
**usm_local_users** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpUsmLocalUsersInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpUsmLocalUsersInner.md) |  | [optional] 
**usm_remote_users** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpUsmRemoteUsersInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpUsmRemoteUsersInner.md) |  | [optional] 
**v2c_enabled** | **bool** |  | [optional] 
**v3_enabled** | **bool** |  | [optional] 
**vacm_groups** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmp

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmp from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmp.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmp.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmp from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmp.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


