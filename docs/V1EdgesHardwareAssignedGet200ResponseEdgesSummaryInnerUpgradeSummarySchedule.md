# V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummarySchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**device_id** | **int** |  | [optional] 
**download_progress** | **int** |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**version** | [**V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion**](V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_schedule import V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummarySchedule

# TODO update the JSON string below
json = "{}"
# create an instance of V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummarySchedule from a JSON string
v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_schedule_instance = V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummarySchedule.from_json(json)
# print the JSON string representation of the object
print(V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummarySchedule.to_json())

# convert the object into a dict
v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_schedule_dict = v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_schedule_instance.to_dict()
# create an instance of V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummarySchedule from a dict
v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_schedule_from_dict = V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummarySchedule.from_dict(v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


