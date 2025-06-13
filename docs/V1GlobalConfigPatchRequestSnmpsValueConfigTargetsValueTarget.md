# V1GlobalConfigPatchRequestSnmpsValueConfigTargetsValueTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community** | **str** |  | [optional] 
**lan_segment** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**notify_filter_profile** | **str** |  | [optional] 
**notify_type** | **str** |  | [optional] 
**source_ip** | **str** |  | [optional] 
**target_ip** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 
**usm_security_level** | **str** |  | [optional] 
**usm_user_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_snmps_value_config_targets_value_target import V1GlobalConfigPatchRequestSnmpsValueConfigTargetsValueTarget

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestSnmpsValueConfigTargetsValueTarget from a JSON string
v1_global_config_patch_request_snmps_value_config_targets_value_target_instance = V1GlobalConfigPatchRequestSnmpsValueConfigTargetsValueTarget.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestSnmpsValueConfigTargetsValueTarget.to_json())

# convert the object into a dict
v1_global_config_patch_request_snmps_value_config_targets_value_target_dict = v1_global_config_patch_request_snmps_value_config_targets_value_target_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestSnmpsValueConfigTargetsValueTarget from a dict
v1_global_config_patch_request_snmps_value_config_targets_value_target_from_dict = V1GlobalConfigPatchRequestSnmpsValueConfigTargetsValueTarget.from_dict(v1_global_config_patch_request_snmps_value_config_targets_value_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


