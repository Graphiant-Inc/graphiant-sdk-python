# V1BackboneHealthEtetSlaMatrixGet200ResponseSlaMatrixInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay_status** | **str** |  | [optional] 
**delay_value** | **float** |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_name** | **str** |  | [optional] 
**jitter_status** | **str** |  | [optional] 
**jitter_value** | **float** |  | [optional] 
**loss_status** | **str** |  | [optional] 
**loss_value** | **float** |  | [optional] 
**mos_value** | **float** |  | [optional] 
**peer_device_id** | **int** |  | [optional] 
**peer_device_name** | **str** |  | [optional] 
**peer_region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 
**region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_etet_sla_matrix_get200_response_sla_matrix_inner import V1BackboneHealthEtetSlaMatrixGet200ResponseSlaMatrixInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthEtetSlaMatrixGet200ResponseSlaMatrixInner from a JSON string
v1_backbone_health_etet_sla_matrix_get200_response_sla_matrix_inner_instance = V1BackboneHealthEtetSlaMatrixGet200ResponseSlaMatrixInner.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthEtetSlaMatrixGet200ResponseSlaMatrixInner.to_json())

# convert the object into a dict
v1_backbone_health_etet_sla_matrix_get200_response_sla_matrix_inner_dict = v1_backbone_health_etet_sla_matrix_get200_response_sla_matrix_inner_instance.to_dict()
# create an instance of V1BackboneHealthEtetSlaMatrixGet200ResponseSlaMatrixInner from a dict
v1_backbone_health_etet_sla_matrix_get200_response_sla_matrix_inner_from_dict = V1BackboneHealthEtetSlaMatrixGet200ResponseSlaMatrixInner.from_dict(v1_backbone_health_etet_sla_matrix_get200_response_sla_matrix_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


