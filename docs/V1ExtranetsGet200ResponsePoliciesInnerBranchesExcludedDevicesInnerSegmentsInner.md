# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_aggregations** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpAggregationsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpAggregationsInner.md) |  | [optional] 
**bgp_multipath** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpMultipath**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpMultipath.md) |  | [optional] 
**bgp_neighbors** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInner.md) |  | [optional] 
**bgp_redistributions** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpRedistributions**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpRedistributions.md) |  | [optional] 
**description** | **str** |  | [optional] 
**dhcp_subnets** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInner.md) |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**function** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**ipfix_exporters** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpfixExportersInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpfixExportersInner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**nat_ruleset** | **str** |  | [optional] 
**networks** | **List[str]** |  | [optional] 
**ospfv2_process** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2Process**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2Process.md) |  | [optional] 
**ospfv3_process** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process.md) |  | [optional] 
**overlay_filters** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOverlayFilters**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOverlayFilters.md) |  | [optional] 
**routable** | **bool** |  | [optional] 
**route_distinguisher** | **str** |  | [optional] 
**static_routes** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner.md) |  | [optional] 
**syslog_targets** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerSyslogTargetsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerSyslogTargetsInner.md) |  | [optional] 
**traffic_ruleset** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


