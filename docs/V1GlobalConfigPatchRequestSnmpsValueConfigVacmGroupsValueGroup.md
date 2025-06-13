# V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accesses** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupAccessesValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupAccessesValue.md) |  | [optional] 
**members** | [**Dict[str, V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValue]**](V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValue.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_snmps_value_config_vacm_groups_value_group import V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroup from a JSON string
v1_global_config_patch_request_snmps_value_config_vacm_groups_value_group_instance = V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroup.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroup.to_json())

# convert the object into a dict
v1_global_config_patch_request_snmps_value_config_vacm_groups_value_group_dict = v1_global_config_patch_request_snmps_value_config_vacm_groups_value_group_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroup from a dict
v1_global_config_patch_request_snmps_value_config_vacm_groups_value_group_from_dict = V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroup.from_dict(v1_global_config_patch_request_snmps_value_config_vacm_groups_value_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


