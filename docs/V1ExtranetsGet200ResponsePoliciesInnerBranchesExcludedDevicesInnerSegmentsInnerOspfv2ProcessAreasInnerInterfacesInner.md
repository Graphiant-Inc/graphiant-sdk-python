# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessAreasInnerInterfacesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bfd** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfd**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfd.md) |  | [optional] 
**bfd_neighbors** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerBfdNeighbor.md) |  | [optional] 
**cost** | **int** |  | [optional] 
**dead_interval** | **int** |  | [optional] 
**dead_interval_value** | **int** |  | [optional] 
**dr_priority** | **int** |  | [optional] 
**hello_interval** | **int** |  | [optional] 
**hello_interval_value** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**if_index** | **int** |  | [optional] 
**interface** | **str** |  | [optional] 
**max_transmission_unit** | **int** |  | [optional] 
**mtu_ignore** | **bool** |  | [optional] 
**prefix_sid** | **int** |  | [optional] 
**retransmit_interval** | **int** |  | [optional] 
**retransmit_interval_value** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv2_process_areas_inner_interfaces_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessAreasInnerInterfacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessAreasInnerInterfacesInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv2_process_areas_inner_interfaces_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessAreasInnerInterfacesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessAreasInnerInterfacesInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv2_process_areas_inner_interfaces_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv2_process_areas_inner_interfaces_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessAreasInnerInterfacesInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv2_process_areas_inner_interfaces_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessAreasInnerInterfacesInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv2_process_areas_inner_interfaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


