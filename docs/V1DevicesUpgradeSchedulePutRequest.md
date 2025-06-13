# V1DevicesUpgradeSchedulePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**device_ids** | **List[int]** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**version** | [**V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion**](V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_upgrade_schedule_put_request import V1DevicesUpgradeSchedulePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesUpgradeSchedulePutRequest from a JSON string
v1_devices_upgrade_schedule_put_request_instance = V1DevicesUpgradeSchedulePutRequest.from_json(json)
# print the JSON string representation of the object
print(V1DevicesUpgradeSchedulePutRequest.to_json())

# convert the object into a dict
v1_devices_upgrade_schedule_put_request_dict = v1_devices_upgrade_schedule_put_request_instance.to_dict()
# create an instance of V1DevicesUpgradeSchedulePutRequest from a dict
v1_devices_upgrade_schedule_put_request_from_dict = V1DevicesUpgradeSchedulePutRequest.from_dict(v1_devices_upgrade_schedule_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


