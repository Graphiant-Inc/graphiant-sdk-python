# V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneLastCrash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crash_details** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**up_since_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_system_plane_last_crash import V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneLastCrash

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneLastCrash from a JSON string
v1_backbone_health_device_device_id_post200_response_system_plane_last_crash_instance = V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneLastCrash.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneLastCrash.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_system_plane_last_crash_dict = v1_backbone_health_device_device_id_post200_response_system_plane_last_crash_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneLastCrash from a dict
v1_backbone_health_device_device_id_post200_response_system_plane_last_crash_from_dict = V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneLastCrash.from_dict(v1_backbone_health_device_device_id_post200_response_system_plane_last_crash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


