# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrative_distance** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**next_hop** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInnerNextHop**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInnerNextHop.md) |  | [optional] 
**next_hops** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInnerNextHop]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInnerNextHop.md) |  | [optional] 
**prefix** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_static_routes_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_static_routes_inner_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_static_routes_inner_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_static_routes_inner_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_static_routes_inner_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInnerStaticRoutesInner.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_static_routes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


