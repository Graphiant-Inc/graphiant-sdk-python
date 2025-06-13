# V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**down_transitions** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner.md) |  | [optional] 
**session_slas** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInner.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_data_plane import V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane from a JSON string
v1_backbone_health_device_device_id_post200_response_data_plane_instance = V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_data_plane_dict = v1_backbone_health_device_device_id_post200_response_data_plane_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane from a dict
v1_backbone_health_device_device_id_post200_response_data_plane_from_dict = V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane.from_dict(v1_backbone_health_device_device_id_post200_response_data_plane_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


