# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach_point** | **str** |  | [optional] 
**default_action** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**global_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**statements** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInner.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


