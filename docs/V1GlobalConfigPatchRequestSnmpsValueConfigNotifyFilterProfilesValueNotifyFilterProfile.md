# V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValueNotifyFilterProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_exclude_list** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValueNotifyFilterProfileIncludeExcludeListValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValueNotifyFilterProfileIncludeExcludeListValue.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_snmps_value_config_notify_filter_profiles_value_notify_filter_profile import V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValueNotifyFilterProfile

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValueNotifyFilterProfile from a JSON string
v1_global_config_patch_request_snmps_value_config_notify_filter_profiles_value_notify_filter_profile_instance = V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValueNotifyFilterProfile.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValueNotifyFilterProfile.to_json())

# convert the object into a dict
v1_global_config_patch_request_snmps_value_config_notify_filter_profiles_value_notify_filter_profile_dict = v1_global_config_patch_request_snmps_value_config_notify_filter_profiles_value_notify_filter_profile_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValueNotifyFilterProfile from a dict
v1_global_config_patch_request_snmps_value_config_notify_filter_profiles_value_notify_filter_profile_from_dict = V1GlobalConfigPatchRequestSnmpsValueConfigNotifyFilterProfilesValueNotifyFilterProfile.from_dict(v1_global_config_patch_request_snmps_value_config_notify_filter_profiles_value_notify_filter_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


