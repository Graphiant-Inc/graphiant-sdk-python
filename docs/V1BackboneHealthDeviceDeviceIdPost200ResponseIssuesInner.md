# V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** |  | [optional] 
**allow_listed** | **bool** |  | [optional] 
**component** | **str** |  | [optional] 
**end_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**entity** | **str** |  | [optional] 
**issue** | **str** |  | [optional] 
**mute_listed** | **bool** |  | [optional] 
**notification_created** | **bool** |  | [optional] 
**plane** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**start_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_issues_inner import V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner from a JSON string
v1_backbone_health_device_device_id_post200_response_issues_inner_instance = V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_issues_inner_dict = v1_backbone_health_device_device_id_post200_response_issues_inner_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner from a dict
v1_backbone_health_device_device_id_post200_response_issues_inner_from_dict = V1BackboneHealthDeviceDeviceIdPost200ResponseIssuesInner.from_dict(v1_backbone_health_device_device_id_post200_response_issues_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


