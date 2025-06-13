# V1GlobalConfigPatchRequestGlobalPrefixSetsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix_set** | [**V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSet**](V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSet.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_global_prefix_sets_value import V1GlobalConfigPatchRequestGlobalPrefixSetsValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestGlobalPrefixSetsValue from a JSON string
v1_global_config_patch_request_global_prefix_sets_value_instance = V1GlobalConfigPatchRequestGlobalPrefixSetsValue.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestGlobalPrefixSetsValue.to_json())

# convert the object into a dict
v1_global_config_patch_request_global_prefix_sets_value_dict = v1_global_config_patch_request_global_prefix_sets_value_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestGlobalPrefixSetsValue from a dict
v1_global_config_patch_request_global_prefix_sets_value_from_dict = V1GlobalConfigPatchRequestGlobalPrefixSetsValue.from_dict(v1_global_config_patch_request_global_prefix_sets_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


