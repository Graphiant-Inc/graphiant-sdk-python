# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**devices** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSiteDevicesInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSiteDevicesInner.md) |  | [optional] 
**edge_count** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerLocation**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerLocation.md) |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**policy_reference_count** | **int** |  | [optional] 
**policy_tag** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTag**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTag.md) |  | [optional] 
**segment_count** | **int** |  | [optional] 
**site_list_reference_count** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**updated_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_site import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_site_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_site_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_site_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_site_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


