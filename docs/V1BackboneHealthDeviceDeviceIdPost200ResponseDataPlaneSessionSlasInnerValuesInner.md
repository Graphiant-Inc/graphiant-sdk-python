# V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay_value** | **float** |  | [optional] 
**jitter_value** | **float** |  | [optional] 
**loss_value** | **float** |  | [optional] 
**status** | **str** |  | [optional] 
**time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_data_plane_session_slas_inner_values_inner import V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner from a JSON string
v1_backbone_health_device_device_id_post200_response_data_plane_session_slas_inner_values_inner_instance = V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_data_plane_session_slas_inner_values_inner_dict = v1_backbone_health_device_device_id_post200_response_data_plane_session_slas_inner_values_inner_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner from a dict
v1_backbone_health_device_device_id_post200_response_data_plane_session_slas_inner_values_inner_from_dict = V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner.from_dict(v1_backbone_health_device_device_id_post200_response_data_plane_session_slas_inner_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


