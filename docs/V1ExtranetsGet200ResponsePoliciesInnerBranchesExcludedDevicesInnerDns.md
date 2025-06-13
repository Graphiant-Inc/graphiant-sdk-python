# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudflare_servers** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner.md) |  | [optional] 
**dynamic_servers** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner.md) |  | [optional] 
**dynamic_servers_v2** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsDynamicServersV2**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsDynamicServersV2.md) |  | [optional] 
**mode** | **str** |  | [optional] 
**static_servers** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner.md) |  | [optional] 
**static_servers_v2** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsStaticServersV2**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsStaticServersV2.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_dns import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDns

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDns from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_dns_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDns.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDns.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_dns_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_dns_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDns from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_dns_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDns.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


