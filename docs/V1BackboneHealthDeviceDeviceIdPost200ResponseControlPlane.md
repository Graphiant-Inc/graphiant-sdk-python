# V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlane


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_transitions** | [**V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitions**](V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitions.md) |  | [optional] 
**management_transitions** | [**V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitions**](V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitions.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_control_plane import V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlane

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlane from a JSON string
v1_backbone_health_device_device_id_post200_response_control_plane_instance = V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlane.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlane.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_control_plane_dict = v1_backbone_health_device_device_id_post200_response_control_plane_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlane from a dict
v1_backbone_health_device_device_id_post200_response_control_plane_from_dict = V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlane.from_dict(v1_backbone_health_device_device_id_post200_response_control_plane_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


