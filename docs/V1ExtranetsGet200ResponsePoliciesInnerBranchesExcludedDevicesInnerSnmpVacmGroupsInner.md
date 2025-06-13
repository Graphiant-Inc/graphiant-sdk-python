# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accesses** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInnerAccessesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInnerAccessesInner.md) |  | [optional] 
**group_members** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInnerGroupMembersInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInnerGroupMembersInner.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**views** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInnerViewsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInnerViewsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_vacm_groups_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_vacm_groups_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_vacm_groups_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_vacm_groups_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_vacm_groups_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpVacmGroupsInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_vacm_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


