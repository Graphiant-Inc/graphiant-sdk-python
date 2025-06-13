# V1GlobalConfigPatchRequestVpnProfilesValueVpnProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_replay_window_size** | **int** |  | [optional] 
**dpd_interval** | **int** |  | [optional] 
**esn** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**ike_dh_group** | **str** |  | [optional] 
**ike_encryption_alg** | **str** |  | [optional] 
**ike_integrity** | **str** |  | [optional] 
**ipsec_encryption_alg** | **str** |  | [optional] 
**ipsec_integrity** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**perfect_forward_secrecy** | **str** |  | [optional] 
**reauth_interval** | **int** |  | [optional] 
**rekey_interval** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_vpn_profiles_value_vpn_profile import V1GlobalConfigPatchRequestVpnProfilesValueVpnProfile

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestVpnProfilesValueVpnProfile from a JSON string
v1_global_config_patch_request_vpn_profiles_value_vpn_profile_instance = V1GlobalConfigPatchRequestVpnProfilesValueVpnProfile.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestVpnProfilesValueVpnProfile.to_json())

# convert the object into a dict
v1_global_config_patch_request_vpn_profiles_value_vpn_profile_dict = v1_global_config_patch_request_vpn_profiles_value_vpn_profile_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestVpnProfilesValueVpnProfile from a dict
v1_global_config_patch_request_vpn_profiles_value_vpn_profile_from_dict = V1GlobalConfigPatchRequestVpnProfilesValueVpnProfile.from_dict(v1_global_config_patch_request_vpn_profiles_value_vpn_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


