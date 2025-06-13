# V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**device_name** | **str** |  | [optional] 
**region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_qoe_matrix_devices_inner import V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner from a JSON string
v1_backbone_health_device_device_id_post200_response_qoe_matrix_devices_inner_instance = V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_qoe_matrix_devices_inner_dict = v1_backbone_health_device_device_id_post200_response_qoe_matrix_devices_inner_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner from a dict
v1_backbone_health_device_device_id_post200_response_qoe_matrix_devices_inner_from_dict = V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner.from_dict(v1_backbone_health_device_device_id_post200_response_qoe_matrix_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


