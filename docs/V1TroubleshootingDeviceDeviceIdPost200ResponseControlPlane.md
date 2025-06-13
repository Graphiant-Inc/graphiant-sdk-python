# V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_transitions** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner.md) |  | [optional] 
**management_transitions** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_troubleshooting_device_device_id_post200_response_control_plane import V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane

# TODO update the JSON string below
json = "{}"
# create an instance of V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane from a JSON string
v1_troubleshooting_device_device_id_post200_response_control_plane_instance = V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane.from_json(json)
# print the JSON string representation of the object
print(V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane.to_json())

# convert the object into a dict
v1_troubleshooting_device_device_id_post200_response_control_plane_dict = v1_troubleshooting_device_device_id_post200_response_control_plane_instance.to_dict()
# create an instance of V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane from a dict
v1_troubleshooting_device_device_id_post200_response_control_plane_from_dict = V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane.from_dict(v1_troubleshooting_device_device_id_post200_response_control_plane_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


