# V1BackboneHealthDeviceDeviceIdPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_plane** | [**V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlane**](V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlane.md) |  | [optional] 
**data_plane** | [**V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane**](V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane.md) |  | [optional] 
**issues** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner.md) |  | [optional] 
**qoe_matrix** | [**V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrix**](V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrix.md) |  | [optional] 
**role** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**sw_version** | **str** |  | [optional] 
**sw_version_v2** | [**V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion**](V1EdgesHardwareAssignedGet200ResponseEdgesSummaryInnerUpgradeSummaryRunningVersion.md) |  | [optional] 
**system_plane** | [**V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlane**](V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlane.md) |  | [optional] 
**up_since_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response import V1BackboneHealthDeviceDeviceIdPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200Response from a JSON string
v1_backbone_health_device_device_id_post200_response_instance = V1BackboneHealthDeviceDeviceIdPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200Response.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_dict = v1_backbone_health_device_device_id_post200_response_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200Response from a dict
v1_backbone_health_device_device_id_post200_response_from_dict = V1BackboneHealthDeviceDeviceIdPost200Response.from_dict(v1_backbone_health_device_device_id_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


