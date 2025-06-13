# V1DevicesRunningVersionPost200ResponseVersionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**version** | [**V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion**](V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_running_version_post200_response_versions_inner import V1DevicesRunningVersionPost200ResponseVersionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesRunningVersionPost200ResponseVersionsInner from a JSON string
v1_devices_running_version_post200_response_versions_inner_instance = V1DevicesRunningVersionPost200ResponseVersionsInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesRunningVersionPost200ResponseVersionsInner.to_json())

# convert the object into a dict
v1_devices_running_version_post200_response_versions_inner_dict = v1_devices_running_version_post200_response_versions_inner_instance.to_dict()
# create an instance of V1DevicesRunningVersionPost200ResponseVersionsInner from a dict
v1_devices_running_version_post200_response_versions_inner_from_dict = V1DevicesRunningVersionPost200ResponseVersionsInner.from_dict(v1_devices_running_version_post200_response_versions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


