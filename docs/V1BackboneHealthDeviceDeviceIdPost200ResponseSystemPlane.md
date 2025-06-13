# V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlane


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInnerTransitionsInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInnerTransitionsInner.md) |  | [optional] 
**crashes** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneCrashesInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneCrashesInner.md) |  | [optional] 
**disk** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInnerTransitionsInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInnerTransitionsInner.md) |  | [optional] 
**last_crash** | [**V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneLastCrash**](V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlaneLastCrash.md) |  | [optional] 
**maintenance_windows** | [**List[V2NotificationlistPostRequest]**](V2NotificationlistPostRequest.md) |  | [optional] 
**memory** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInnerTransitionsInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInnerTransitionsInner.md) |  | [optional] 
**overheating** | [**List[V2NotificationlistPostRequest]**](V2NotificationlistPostRequest.md) |  | [optional] 
**status** | **str** |  | [optional] 
**temperature_series** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInnerTransitionsInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInnerTransitionsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_system_plane import V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlane

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlane from a JSON string
v1_backbone_health_device_device_id_post200_response_system_plane_instance = V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlane.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlane.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_system_plane_dict = v1_backbone_health_device_device_id_post200_response_system_plane_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlane from a dict
v1_backbone_health_device_device_id_post200_response_system_plane_from_dict = V1BackboneHealthDeviceDeviceIdPost200ResponseSystemPlane.from_dict(v1_backbone_health_device_device_id_post200_response_system_plane_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


