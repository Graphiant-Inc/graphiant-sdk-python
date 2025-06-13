# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_aggregations** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpAggregationsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpAggregationsInner.md) |  | [optional] 
**bgp_multipath** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpMultipath**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpMultipath.md) |  | [optional] 
**bgp_neighbors** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner.md) |  | [optional] 
**bgp_redistributions** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpRedistributions**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpRedistributions.md) |  | [optional] 
**carrier** | **str** |  | [optional] 
**circuit_type** | **str** |  | [optional] 
**connection_type** | **str** |  | [optional] 
**core_logical_interfaces_v2** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerCoreLogicalInterfacesV2Inner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerCoreLogicalInterfacesV2Inner.md) |  | [optional] 
**description** | **str** |  | [optional] 
**dia_enabled** | **bool** |  | [optional] 
**dia_snmp_index** | **int** |  | [optional] 
**discovered_public_ip** | **str** |  | [optional] 
**drop_mechanism** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interface_name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**last_resort** | **bool** |  | [optional] 
**link_down_speed_mbps** | **int** |  | [optional] 
**link_up_speed_mbps** | **int** |  | [optional] 
**loopback** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**pat_addresses** | **List[str]** |  | [optional] 
**private_ip** | **str** |  | [optional] 
**profile** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerProfile**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerProfile.md) |  | [optional] 
**qos_profile** | **str** |  | [optional] 
**qos_profile_type** | **str** |  | [optional] 
**snmp_index** | **int** |  | [optional] 
**static_routes** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner.md) |  | [optional] 
**wan_interface_v2** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerCoreLogicalInterfacesV2Inner**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerCoreLogicalInterfacesV2Inner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


