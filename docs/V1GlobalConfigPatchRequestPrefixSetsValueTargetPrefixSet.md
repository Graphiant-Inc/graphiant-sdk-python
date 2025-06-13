# V1GlobalConfigPatchRequestPrefixSetsValueTargetPrefixSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entries** | [**List[V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry]**](V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry.md) |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_prefix_sets_value_target_prefix_set import V1GlobalConfigPatchRequestPrefixSetsValueTargetPrefixSet

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestPrefixSetsValueTargetPrefixSet from a JSON string
v1_global_config_patch_request_prefix_sets_value_target_prefix_set_instance = V1GlobalConfigPatchRequestPrefixSetsValueTargetPrefixSet.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestPrefixSetsValueTargetPrefixSet.to_json())

# convert the object into a dict
v1_global_config_patch_request_prefix_sets_value_target_prefix_set_dict = v1_global_config_patch_request_prefix_sets_value_target_prefix_set_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestPrefixSetsValueTargetPrefixSet from a dict
v1_global_config_patch_request_prefix_sets_value_target_prefix_set_from_dict = V1GlobalConfigPatchRequestPrefixSetsValueTargetPrefixSet.from_dict(v1_global_config_patch_request_prefix_sets_value_target_prefix_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


