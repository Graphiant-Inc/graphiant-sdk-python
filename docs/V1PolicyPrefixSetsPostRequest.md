# V1PolicyPrefixSetsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entries** | [**Dict[str, V1PolicyPrefixSetsPostRequestEntriesValue]**](V1PolicyPrefixSetsPostRequestEntriesValue.md) |  | [optional] 
**mode** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**prefix_set_entries** | [**Dict[str, V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry]**](V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_policy_prefix_sets_post_request import V1PolicyPrefixSetsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1PolicyPrefixSetsPostRequest from a JSON string
v1_policy_prefix_sets_post_request_instance = V1PolicyPrefixSetsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1PolicyPrefixSetsPostRequest.to_json())

# convert the object into a dict
v1_policy_prefix_sets_post_request_dict = v1_policy_prefix_sets_post_request_instance.to_dict()
# create an instance of V1PolicyPrefixSetsPostRequest from a dict
v1_policy_prefix_sets_post_request_from_dict = V1PolicyPrefixSetsPostRequest.from_dict(v1_policy_prefix_sets_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


