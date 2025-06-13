# V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner.md) |  | [optional] 
**qoe_matrix** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_qoe_matrix import V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrix

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrix from a JSON string
v1_backbone_health_device_device_id_post200_response_qoe_matrix_instance = V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrix.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrix.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_qoe_matrix_dict = v1_backbone_health_device_device_id_post200_response_qoe_matrix_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrix from a dict
v1_backbone_health_device_device_id_post200_response_qoe_matrix_from_dict = V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrix.from_dict(v1_backbone_health_device_device_id_post200_response_qoe_matrix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


