# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**lacp_config** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterfaceLacpConfig**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterfaceLacpConfig.md) |  | [optional] 
**members** | **List[int]** |  | [optional] 
**minimum_members** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_lag_interface import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterface

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterface from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_lag_interface_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterface.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterface.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_lag_interface_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_lag_interface_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterface from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_lag_interface_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerLagInterface.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_lag_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


