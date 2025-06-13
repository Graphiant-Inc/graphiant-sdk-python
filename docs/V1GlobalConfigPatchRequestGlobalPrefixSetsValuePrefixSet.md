# V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entries** | [**Dict[str, V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValue]**](V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValue.md) |  | [optional] 
**global_id** | **int** |  | [optional] 
**is_global_sync** | **bool** |  | [optional] 
**mode** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_global_prefix_sets_value_prefix_set import V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSet

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSet from a JSON string
v1_global_config_patch_request_global_prefix_sets_value_prefix_set_instance = V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSet.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSet.to_json())

# convert the object into a dict
v1_global_config_patch_request_global_prefix_sets_value_prefix_set_dict = v1_global_config_patch_request_global_prefix_sets_value_prefix_set_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSet from a dict
v1_global_config_patch_request_global_prefix_sets_value_prefix_set_from_dict = V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSet.from_dict(v1_global_config_patch_request_global_prefix_sets_value_prefix_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


