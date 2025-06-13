# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerMatchesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community** | **List[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**prefix_set** | **str** |  | [optional] 
**protocol_route_type** | **str** |  | [optional] 
**route_tag** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchRouteTagEntry**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementMatchesValueMatchRouteTagEntry.md) |  | [optional] 
**seq** | **int** |  | [optional] 
**source_interface** | **str** |  | [optional] 
**source_protocol** | **str** |  | [optional] 
**stale_purge** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_matches_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerMatchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerMatchesInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_matches_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerMatchesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerMatchesInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_matches_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_matches_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerMatchesInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_matches_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerRoutingPoliciesInnerStatementsInnerMatchesInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_routing_policies_inner_statements_inner_matches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


