# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerBgp**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerBgp.md) |  | [optional] 
**destination_address** | **str** |  | [optional] 
**ike_initiator** | **bool** |  | [optional] 
**ipsec_label** | **str** |  | [optional] 
**lan** | **str** |  | [optional] 
**local_address_v4** | **str** |  | [optional] 
**local_address_v6** | **str** |  | [optional] 
**local_circuit** | **str** |  | [optional] 
**local_ike_peer_identity** | **str** |  | [optional] 
**mtu** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**preshared_key** | **str** |  | [optional] 
**remote_address_v4** | **str** |  | [optional] 
**remote_address_v6** | **str** |  | [optional] 
**remote_ike_peer_identity** | **str** |  | [optional] 
**static** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerStatic**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInnerStatic.md) |  | [optional] 
**tcp_mss** | **int** |  | [optional] 
**vpn_profile** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerIpsecTunnelsInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


