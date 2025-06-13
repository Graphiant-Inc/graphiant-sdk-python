# V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInnerBoxInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay_value** | **float** |  | [optional] 
**end_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**jitter_value** | **float** |  | [optional] 
**loss_value** | **float** |  | [optional] 
**start_time** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**status** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_box_inner import V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInnerBoxInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInnerBoxInner from a JSON string
v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_box_inner_instance = V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInnerBoxInner.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInnerBoxInner.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_box_inner_dict = v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_box_inner_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInnerBoxInner from a dict
v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_box_inner_from_dict = V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInnerBoxInner.from_dict(v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_box_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


