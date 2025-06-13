# V1GlobalConfigPatchRequestSnmpsValueConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communities** | [**Dict[str, V1PortalApikeysPostRequest]**](V1PortalApikeysPostRequest.md) |  | [optional] 
**engine_authen_traps** | **bool** |  | [optional] 
**engine_enabled** | **bool** |  | [optional] 
**engine_endpoints** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValue.md) |  | [optional] 
**engine_high_cpu_traps** | **bool** |  | [optional] 
**engine_high_memory_traps** | **bool** |  | [optional] 
**engine_id_admin_octets** | **str** |  | [optional] 
**engine_id_admin_text** | **str** |  | [optional] 
**engine_id_ipv4** | **str** |  | [optional] 
**engine_id_ipv6** | **str** |  | [optional] 
**engine_id_mac** | **str** |  | [optional] 
**engine_id_raw** | **str** |  | [optional] 
**engine_local_acess_v4** | **bool** |  | [optional] 
**engine_local_acess_v6** | **bool** |  | [optional] 
**engine_user_hints** | **bool** |  | [optional] 
**engine_user_validation** | **bool** |  | [optional] 
**global_id** | **int** |  | [optional] 
**is_global_sync** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**notify_filter_profiles** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValue.md) |  | [optional] 
**targets** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigTargetsValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigTargetsValue.md) |  | [optional] 
**usm_local_users** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigUsmLocalUsersValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigUsmLocalUsersValue.md) |  | [optional] 
**usm_remote_users** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigUsmRemoteUsersValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigUsmRemoteUsersValue.md) |  | [optional] 
**v2c_enabled** | **bool** |  | [optional] 
**v3_enabled** | **bool** |  | [optional] 
**vacm_groups** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValue.md) |  | [optional] 
**vacm_views** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigVacmViewsValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigVacmViewsValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_snmps_value_config import V1GlobalConfigPatchRequestSnmpsValueConfig

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestSnmpsValueConfig from a JSON string
v1_global_config_patch_request_snmps_value_config_instance = V1GlobalConfigPatchRequestSnmpsValueConfig.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestSnmpsValueConfig.to_json())

# convert the object into a dict
v1_global_config_patch_request_snmps_value_config_dict = v1_global_config_patch_request_snmps_value_config_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestSnmpsValueConfig from a dict
v1_global_config_patch_request_snmps_value_config_from_dict = V1GlobalConfigPatchRequestSnmpsValueConfig.from_dict(v1_global_config_patch_request_snmps_value_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


