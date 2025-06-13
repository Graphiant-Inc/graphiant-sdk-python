# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpTargetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**notify_filter_profile** | **str** |  | [optional] 
**notify_type** | **str** |  | [optional] 
**source_ip** | **str** |  | [optional] 
**target_ip** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 
**usm_security_level** | **str** |  | [optional] 
**usm_user_name** | **str** |  | [optional] 
**vrf_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_targets_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpTargetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpTargetsInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_targets_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpTargetsInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpTargetsInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_targets_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_targets_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpTargetsInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_targets_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpTargetsInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_targets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


