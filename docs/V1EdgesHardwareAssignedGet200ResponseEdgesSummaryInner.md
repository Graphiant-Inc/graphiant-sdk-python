# V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_on** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**device_id** | **int** |  | [optional] 
**discovered_location** | **str** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**enterprise_name** | **str** |  | [optional] 
**first_appeared_on** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**hostname** | **str** |  | [optional] 
**ip_detected** | **str** |  | [optional] 
**is_hardware** | **bool** |  | [optional] 
**is_new** | **bool** |  | [optional] 
**is_requested** | **bool** |  | [optional] 
**last_booted_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**location** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerLocation**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerLocation.md) |  | [optional] 
**model** | **str** |  | [optional] 
**override_region** | **str** |  | [optional] 
**parent_enterprise_name** | **str** |  | [optional] 
**portal_status** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**serial_num** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**site_id** | **int** |  | [optional] 
**stale** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**sw_name** | **str** |  | [optional] 
**sw_version** | **str** |  | [optional] 
**tt_conn_count** | **int** |  | [optional] 
**upgrade_summary** | [**V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummary**](V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummary.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_edges_hardware_assigned_get200_response_edges_summary_inner import V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInner from a JSON string
v1_edges_hardware_assigned_get200_response_edges_summary_inner_instance = V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInner.from_json(json)
# print the JSON string representation of the object
print(V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInner.to_json())

# convert the object into a dict
v1_edges_hardware_assigned_get200_response_edges_summary_inner_dict = v1_edges_hardware_assigned_get200_response_edges_summary_inner_instance.to_dict()
# create an instance of V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInner from a dict
v1_edges_hardware_assigned_get200_response_edges_summary_inner_from_dict = V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInner.from_dict(v1_edges_hardware_assigned_get200_response_edges_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


