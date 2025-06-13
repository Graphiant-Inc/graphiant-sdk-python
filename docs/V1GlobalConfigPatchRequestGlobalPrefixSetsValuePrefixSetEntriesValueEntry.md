# V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_prefix** | **str** |  | [optional] 
**mask_lower** | **int** |  | [optional] 
**mask_upper** | **int** |  | [optional] 
**seq** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_global_prefix_sets_value_prefix_set_entries_value_entry import V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry from a JSON string
v1_global_config_patch_request_global_prefix_sets_value_prefix_set_entries_value_entry_instance = V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry.to_json())

# convert the object into a dict
v1_global_config_patch_request_global_prefix_sets_value_prefix_set_entries_value_entry_dict = v1_global_config_patch_request_global_prefix_sets_value_prefix_set_entries_value_entry_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry from a dict
v1_global_config_patch_request_global_prefix_sets_value_prefix_set_entries_value_entry_from_dict = V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry.from_dict(v1_global_config_patch_request_global_prefix_sets_value_prefix_set_entries_value_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


