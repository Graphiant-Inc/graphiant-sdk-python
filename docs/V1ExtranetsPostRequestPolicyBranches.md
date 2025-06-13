# V1ExtranetsPostRequestPolicyBranches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_devices** | **List[int]** |  | [optional] 
**prefix_set** | [**V1ExtranetsPostRequestPolicyBranchesPrefixSet**](V1ExtranetsPostRequestPolicyBranchesPrefixSet.md) |  | [optional] 
**sites** | **List[int]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_post_request_policy_branches import V1ExtranetsPostRequestPolicyBranches

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsPostRequestPolicyBranches from a JSON string
v1_extranets_post_request_policy_branches_instance = V1ExtranetsPostRequestPolicyBranches.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsPostRequestPolicyBranches.to_json())

# convert the object into a dict
v1_extranets_post_request_policy_branches_dict = v1_extranets_post_request_policy_branches_instance.to_dict()
# create an instance of V1ExtranetsPostRequestPolicyBranches from a dict
v1_extranets_post_request_policy_branches_from_dict = V1ExtranetsPostRequestPolicyBranches.from_dict(v1_extranets_post_request_policy_branches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


