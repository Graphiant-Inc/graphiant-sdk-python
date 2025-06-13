# V1ExtranetsGet200ResponsePoliciesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto** | [**V1ExtranetsGet200ResponsePoliciesInnerAuto**](V1ExtranetsGet200ResponsePoliciesInnerAuto.md) |  | [optional] 
**branches** | [**V1ExtranetsGet200ResponsePoliciesInnerBranches**](V1ExtranetsGet200ResponsePoliciesInnerBranches.md) |  | [optional] 
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**created_by** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**host_prefix_set** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet**](V1ExtranetsGet200ResponsePoliciesInnerBranchesPrefixSet.md) |  | [optional] 
**id** | **int** |  | [optional] 
**manual** | [**V1ExtranetsGet200ResponsePoliciesInnerManual**](V1ExtranetsGet200ResponsePoliciesInnerManual.md) |  | [optional] 
**name** | **str** |  | [optional] 
**shared_prefixes** | **List[str]** |  | [optional] 
**shared_segment** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner.md) |  | [optional] 
**source** | [**V1ExtranetsGet200ResponsePoliciesInnerBranches**](V1ExtranetsGet200ResponsePoliciesInnerBranches.md) |  | [optional] 
**target_segments** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInner.md) |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner import V1ExtranetsGet200ResponsePoliciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInner from a JSON string
v1_extranets_get200_response_policies_inner_instance = V1ExtranetsGet200ResponsePoliciesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_dict = v1_extranets_get200_response_policies_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInner from a dict
v1_extranets_get200_response_policies_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInner.from_dict(v1_extranets_get200_response_policies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


