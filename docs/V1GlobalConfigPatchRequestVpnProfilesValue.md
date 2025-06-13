# V1GlobalConfigPatchRequestVpnProfilesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpn_profile** | [**V1GlobalConfigPatchRequestVpnProfilesValueVpnProfile**](V1GlobalConfigPatchRequestVpnProfilesValueVpnProfile.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_vpn_profiles_value import V1GlobalConfigPatchRequestVpnProfilesValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestVpnProfilesValue from a JSON string
v1_global_config_patch_request_vpn_profiles_value_instance = V1GlobalConfigPatchRequestVpnProfilesValue.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestVpnProfilesValue.to_json())

# convert the object into a dict
v1_global_config_patch_request_vpn_profiles_value_dict = v1_global_config_patch_request_vpn_profiles_value_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestVpnProfilesValue from a dict
v1_global_config_patch_request_vpn_profiles_value_from_dict = V1GlobalConfigPatchRequestVpnProfilesValue.from_dict(v1_global_config_patch_request_vpn_profiles_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


