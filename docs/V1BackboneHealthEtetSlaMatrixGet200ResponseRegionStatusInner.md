# V1BackboneHealthEtetSlaMatrixGet200ResponseRegionStatusInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer_region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 
**region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_etet_sla_matrix_get200_response_region_status_inner import V1BackboneHealthEtetSlaMatrixGet200ResponseRegionStatusInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthEtetSlaMatrixGet200ResponseRegionStatusInner from a JSON string
v1_backbone_health_etet_sla_matrix_get200_response_region_status_inner_instance = V1BackboneHealthEtetSlaMatrixGet200ResponseRegionStatusInner.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthEtetSlaMatrixGet200ResponseRegionStatusInner.to_json())

# convert the object into a dict
v1_backbone_health_etet_sla_matrix_get200_response_region_status_inner_dict = v1_backbone_health_etet_sla_matrix_get200_response_region_status_inner_instance.to_dict()
# create an instance of V1BackboneHealthEtetSlaMatrixGet200ResponseRegionStatusInner from a dict
v1_backbone_health_etet_sla_matrix_get200_response_region_status_inner_from_dict = V1BackboneHealthEtetSlaMatrixGet200ResponseRegionStatusInner.from_dict(v1_backbone_health_etet_sla_matrix_get200_response_region_status_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


