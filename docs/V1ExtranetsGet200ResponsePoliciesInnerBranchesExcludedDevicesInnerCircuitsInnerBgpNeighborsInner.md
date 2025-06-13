# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_families** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerAddressFamiliesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerAddressFamiliesInner.md) |  | [optional] 
**allow_as_in** | **int** |  | [optional] 
**as_override** | **bool** |  | [optional] 
**bfd** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfd**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfd.md) |  | [optional] 
**bfd_neighbor** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor.md) |  | [optional] 
**bgp_type** | **str** |  | [optional] 
**default_originate** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**hold_timer** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**keepalive_timer** | **int** |  | [optional] 
**local_address** | **str** |  | [optional] 
**local_interface** | **str** |  | [optional] 
**max_prefix** | **int** |  | [optional] 
**md5_password** | **str** |  | [optional] 
**multi_hop** | **int** |  | [optional] 
**peer_asn** | **int** |  | [optional] 
**remote_address** | **str** |  | [optional] 
**remove_private_as** | **bool** |  | [optional] 
**send_community** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**time_since_last_oper_change** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**up** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


