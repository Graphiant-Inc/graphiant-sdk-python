# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entries** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInnerEntriesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInnerEntriesInner.md) |  | [optional] 
**error_message** | **str** |  | [optional] 
**global_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**policies** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInnerPoliciesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInnerPoliciesInner.md) |  | [optional] 
**policy_count** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_prefix_sets_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_prefix_sets_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_prefix_sets_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_prefix_sets_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_prefix_sets_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerPrefixSetsInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_prefix_sets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


