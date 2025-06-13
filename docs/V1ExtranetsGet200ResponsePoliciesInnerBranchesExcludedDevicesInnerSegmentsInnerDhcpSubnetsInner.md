# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_lease_time_secs** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interface** | **str** |  | [optional] 
**ip_prefix** | **str** |  | [optional] 
**ip_version** | **int** |  | [optional] 
**leases** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerLeasesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerLeasesInner.md) |  | [optional] 
**max_lease_time_secs** | **int** |  | [optional] 
**min_lease_time_secs** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**nameservers** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerNameservers**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerNameservers.md) |  | [optional] 
**ranges** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerRangesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerRangesInner.md) |  | [optional] 
**static_leases** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerStaticLeasesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInnerStaticLeasesInner.md) |  | [optional] 
**total_addresses** | **int** |  | [optional] 
**utilization** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_dhcp_subnets_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_dhcp_subnets_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_dhcp_subnets_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_dhcp_subnets_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_dhcp_subnets_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerDhcpSubnetsInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_dhcp_subnets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


