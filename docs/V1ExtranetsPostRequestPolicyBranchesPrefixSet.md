# V1ExtranetsPostRequestPolicyBranchesPrefixSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entries** | [**Dict[str, V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry]**](V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry.md) |  | [optional] 
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_post_request_policy_branches_prefix_set import V1ExtranetsPostRequestPolicyBranchesPrefixSet

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsPostRequestPolicyBranchesPrefixSet from a JSON string
v1_extranets_post_request_policy_branches_prefix_set_instance = V1ExtranetsPostRequestPolicyBranchesPrefixSet.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsPostRequestPolicyBranchesPrefixSet.to_json())

# convert the object into a dict
v1_extranets_post_request_policy_branches_prefix_set_dict = v1_extranets_post_request_policy_branches_prefix_set_instance.to_dict()
# create an instance of V1ExtranetsPostRequestPolicyBranchesPrefixSet from a dict
v1_extranets_post_request_policy_branches_prefix_set_from_dict = V1ExtranetsPostRequestPolicyBranchesPrefixSet.from_dict(v1_extranets_post_request_policy_branches_prefix_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


