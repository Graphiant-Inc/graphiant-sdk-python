# V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entries** | [**List[V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry]**](V1GlobalConfigPatchRequestGlobalPrefixSetsValuePrefixSetEntriesValueEntry.md) |  | [optional] 
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_prefix_set import V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet from a JSON string
v1_extranets_get200_response_policies_inner_branches_prefix_set_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_prefix_set_dict = v1_extranets_get200_response_policies_inner_branches_prefix_set_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet from a dict
v1_extranets_get200_response_policies_inner_branches_prefix_set_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet.from_dict(v1_extranets_get200_response_policies_inner_branches_prefix_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


