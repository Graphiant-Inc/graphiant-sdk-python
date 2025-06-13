# V1ExtranetsGet200ResponsePoliciesInnerBranches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_devices** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInner.md) |  | [optional] 
**prefix_set** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet**](V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet.md) |  | [optional] 
**sites** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches import V1ExtranetsGet200ResponsePoliciesInnerBranches

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranches from a JSON string
v1_extranets_get200_response_policies_inner_branches_instance = V1ExtranetsGet200ResponsePoliciesInnerBranches.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranches.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_dict = v1_extranets_get200_response_policies_inner_branches_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranches from a dict
v1_extranets_get200_response_policies_inner_branches_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranches.from_dict(v1_extranets_get200_response_policies_inner_branches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


