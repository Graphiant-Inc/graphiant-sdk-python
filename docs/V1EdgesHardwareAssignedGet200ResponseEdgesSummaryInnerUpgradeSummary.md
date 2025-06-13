# V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**last_discovered_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**last_upgrade_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**running_version** | [**V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion**](V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion.md) |  | [optional] 
**schedule** | [**V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummarySchedule**](V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummarySchedule.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary import V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummary from a JSON string
v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_instance = V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummary.from_json(json)
# print the JSON string representation of the object
print(V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummary.to_json())

# convert the object into a dict
v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_dict = v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_instance.to_dict()
# create an instance of V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummary from a dict
v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_from_dict = V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummary.from_dict(v1_edges_hardware_assigned_get200_response_edges_summary_inner_upgrade_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


