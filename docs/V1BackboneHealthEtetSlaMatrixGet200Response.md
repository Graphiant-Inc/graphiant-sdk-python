# V1BackboneHealthEtetSlaMatrixGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner]**](V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner.md) |  | [optional] 
**region_status** | [**List[V1BackboneHealthEtetSlaMatrixGet200ResponseRegionStatusInner]**](V1BackboneHealthEtetSlaMatrixGet200ResponseRegionStatusInner.md) |  | [optional] 
**sla_matrix** | [**List[V1BackboneHealthEtetSlaMatrixGet200ResponseSlaMatrixInner]**](V1BackboneHealthEtetSlaMatrixGet200ResponseSlaMatrixInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_etet_sla_matrix_get200_response import V1BackboneHealthEtetSlaMatrixGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthEtetSlaMatrixGet200Response from a JSON string
v1_backbone_health_etet_sla_matrix_get200_response_instance = V1BackboneHealthEtetSlaMatrixGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthEtetSlaMatrixGet200Response.to_json())

# convert the object into a dict
v1_backbone_health_etet_sla_matrix_get200_response_dict = v1_backbone_health_etet_sla_matrix_get200_response_instance.to_dict()
# create an instance of V1BackboneHealthEtetSlaMatrixGet200Response from a dict
v1_backbone_health_etet_sla_matrix_get200_response_from_dict = V1BackboneHealthEtetSlaMatrixGet200Response.from_dict(v1_backbone_health_etet_sla_matrix_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


