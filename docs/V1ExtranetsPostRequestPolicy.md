# V1ExtranetsPostRequestPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto** | [**V1ExtranetsGet200ResponsePoliciesInnerAuto**](V1ExtranetsGet200ResponsePoliciesInnerAuto.md) |  | [optional] 
**branches** | [**V1ExtranetsPostRequestPolicyBranches**](V1ExtranetsPostRequestPolicyBranches.md) |  | [optional] 
**description** | **str** |  | [optional] 
**host_prefix_set** | [**V1ExtranetsPostRequestPolicyBranchesPrefixSet**](V1ExtranetsPostRequestPolicyBranchesPrefixSet.md) |  | [optional] 
**manual** | [**V1ExtranetsGet200ResponsePoliciesInnerManual**](V1ExtranetsGet200ResponsePoliciesInnerManual.md) |  | [optional] 
**name** | **str** |  | [optional] 
**shared_prefixes** | **List[str]** |  | [optional] 
**shared_segment** | **int** |  | [optional] 
**source** | [**V1ExtranetsPostRequestPolicyBranches**](V1ExtranetsPostRequestPolicyBranches.md) |  | [optional] 
**target_segments** | **List[int]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_post_request_policy import V1ExtranetsPostRequestPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsPostRequestPolicy from a JSON string
v1_extranets_post_request_policy_instance = V1ExtranetsPostRequestPolicy.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsPostRequestPolicy.to_json())

# convert the object into a dict
v1_extranets_post_request_policy_dict = v1_extranets_post_request_policy_instance.to_dict()
# create an instance of V1ExtranetsPostRequestPolicy from a dict
v1_extranets_post_request_policy_from_dict = V1ExtranetsPostRequestPolicy.from_dict(v1_extranets_post_request_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


