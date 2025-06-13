# V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInnerBoxInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInnerBoxInner.md) |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 
**peer_device_id** | **int** |  | [optional] 
**peer_device_region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 
**session_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner import V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInner from a JSON string
v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_instance = V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInner.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInner.to_json())

# convert the object into a dict
v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_dict = v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_instance.to_dict()
# create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInner from a dict
v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_from_dict = V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixQoeMatrixInner.from_dict(v1_backbone_health_device_device_id_post200_response_qoe_matrix_qoe_matrix_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


