# V1TroubleshootingDeviceDeviceIdPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maintenance_mode** | **bool** |  | [optional] 
**colr_active** | **bool** |  | [optional] 
**control_plane** | [**V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane**](V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane.md) |  | [optional] 
**data_plane** | [**V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane**](V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane.md) |  | [optional] 
**issues** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner.md) |  | [optional] 
**lifecycle_status** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**sw_version** | **str** |  | [optional] 
**sw_version_v2** | [**V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion**](V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion.md) |  | [optional] 
**system_plane** | [**V1TroubleshootingDeviceDeviceIdPost200ResponseSystemPlane**](V1TroubleshootingDeviceDeviceIdPost200ResponseSystemPlane.md) |  | [optional] 
**up_since_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_troubleshooting_device_device_id_post200_response import V1TroubleshootingDeviceDeviceIdPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1TroubleshootingDeviceDeviceIdPost200Response from a JSON string
v1_troubleshooting_device_device_id_post200_response_instance = V1TroubleshootingDeviceDeviceIdPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1TroubleshootingDeviceDeviceIdPost200Response.to_json())

# convert the object into a dict
v1_troubleshooting_device_device_id_post200_response_dict = v1_troubleshooting_device_device_id_post200_response_instance.to_dict()
# create an instance of V1TroubleshootingDeviceDeviceIdPost200Response from a dict
v1_troubleshooting_device_device_id_post200_response_from_dict = V1TroubleshootingDeviceDeviceIdPost200Response.from_dict(v1_troubleshooting_device_device_id_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


