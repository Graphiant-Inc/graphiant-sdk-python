# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpSec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_replay_window_size** | **int** |  | [optional] 
**dh_group** | **str** |  | [optional] 
**dpd_interval** | **int** |  | [optional] 
**encryption_alg** | **str** |  | [optional] 
**esn** | **bool** |  | [optional] 
**established_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**ike_integrity** | **str** |  | [optional] 
**ipsec_encryption_alg** | **str** |  | [optional] 
**ipsec_integrity** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**local_address** | **str** |  | [optional] 
**local_circuit** | **str** |  | [optional] 
**local_ike_peer_identity** | **str** |  | [optional] 
**local_ikesa_spi** | **int** |  | [optional] 
**local_port** | **int** |  | [optional] 
**negotiated_algo** | **str** |  | [optional] 
**oper_state** | **bool** |  | [optional] 
**perfect_forward_secrecy** | **str** |  | [optional] 
**preshared_key** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**reauth_interval** | **int** |  | [optional] 
**rekey_interval** | **int** |  | [optional] 
**remote_address** | **str** |  | [optional] 
**remote_ike_peer_identity** | **str** |  | [optional] 
**remote_ikesa_spi** | **int** |  | [optional] 
**remote_port** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ip_sec import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpSec

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpSec from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ip_sec_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpSec.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpSec.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ip_sec_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ip_sec_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpSec from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ip_sec_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpSec.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ip_sec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


