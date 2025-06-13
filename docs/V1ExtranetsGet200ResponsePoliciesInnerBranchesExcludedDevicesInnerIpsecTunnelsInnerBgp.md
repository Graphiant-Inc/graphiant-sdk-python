# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerBgp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_families** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerAddressFamiliesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerBgpNeighborsInnerAddressFamiliesInner.md) |  | [optional] 
**hold_timer** | **int** |  | [optional] 
**keepalive_timer** | **int** |  | [optional] 
**md5_password** | **str** |  | [optional] 
**peer_asn** | **int** |  | [optional] 
**send_community** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_bgp import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerBgp

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerBgp from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_bgp_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerBgp.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerBgp.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_bgp_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_bgp_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerBgp from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_bgp_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerBgp.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_bgp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


