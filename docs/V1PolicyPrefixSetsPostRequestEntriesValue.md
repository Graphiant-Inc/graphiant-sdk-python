# V1PolicyPrefixSetsPostRequestEntriesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_prefix** | **str** |  | [optional] 
**mask_lower** | **int** |  | [optional] 
**mask_upper** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_policy_prefix_sets_post_request_entries_value import V1PolicyPrefixSetsPostRequestEntriesValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1PolicyPrefixSetsPostRequestEntriesValue from a JSON string
v1_policy_prefix_sets_post_request_entries_value_instance = V1PolicyPrefixSetsPostRequestEntriesValue.from_json(json)
# print the JSON string representation of the object
print(V1PolicyPrefixSetsPostRequestEntriesValue.to_json())

# convert the object into a dict
v1_policy_prefix_sets_post_request_entries_value_dict = v1_policy_prefix_sets_post_request_entries_value_instance.to_dict()
# create an instance of V1PolicyPrefixSetsPostRequestEntriesValue from a dict
v1_policy_prefix_sets_post_request_entries_value_from_dict = V1PolicyPrefixSetsPostRequestEntriesValue.from_dict(v1_policy_prefix_sets_post_request_entries_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


