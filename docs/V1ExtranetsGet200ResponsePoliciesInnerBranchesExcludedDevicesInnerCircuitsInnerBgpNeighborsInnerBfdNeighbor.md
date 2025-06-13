# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desired_minimum_tx_interval** | **int** |  | [optional] 
**if_index** | **int** |  | [optional] 
**interface** | **str** |  | [optional] 
**last_updated** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**local_diag** | **str** |  | [optional] 
**peer_address** | **str** |  | [optional] 
**remote_diag** | **str** |  | [optional] 
**required_minimum_rx_interval** | **int** |  | [optional] 
**segment_name** | **str** |  | [optional] 
**source_address** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**time_in_state** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**up** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_bfd_neighbor import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_bfd_neighbor_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_bfd_neighbor_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_bfd_neighbor_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_bfd_neighbor_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_bfd_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


