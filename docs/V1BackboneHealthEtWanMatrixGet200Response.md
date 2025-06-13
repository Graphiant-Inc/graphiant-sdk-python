# V1BackboneHealthEtWanMatrixGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_etwan_summary** | [**List[V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner]**](V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner.md) |  | [optional] 
**region_sla_status** | [**List[V1BackboneHealthEtWanMatrixGet200ResponseRegionSlaStatusInner]**](V1BackboneHealthEtWanMatrixGet200ResponseRegionSlaStatusInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_et_wan_matrix_get200_response import V1BackboneHealthEtWanMatrixGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthEtWanMatrixGet200Response from a JSON string
v1_backbone_health_et_wan_matrix_get200_response_instance = V1BackboneHealthEtWanMatrixGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthEtWanMatrixGet200Response.to_json())

# convert the object into a dict
v1_backbone_health_et_wan_matrix_get200_response_dict = v1_backbone_health_et_wan_matrix_get200_response_instance.to_dict()
# create an instance of V1BackboneHealthEtWanMatrixGet200Response from a dict
v1_backbone_health_et_wan_matrix_get200_response_from_dict = V1BackboneHealthEtWanMatrixGet200Response.from_dict(v1_backbone_health_et_wan_matrix_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


