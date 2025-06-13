# V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_distance** | **int** |  | [optional] 
**areas** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessAreasInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessAreasInner.md) |  | [optional] 
**default_originate** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**redistributed_protocols** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessRedistributedProtocolsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv2ProcessRedistributedProtocolsInner.md) |  | [optional] 
**router_id** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv3_process import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process from a JSON string
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv3_process_instance = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process.to_json())

# convert the object into a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv3_process_dict = v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv3_process_instance.to_dict()
# create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process from a dict
v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv3_process_from_dict = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process.from_dict(v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv3_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


