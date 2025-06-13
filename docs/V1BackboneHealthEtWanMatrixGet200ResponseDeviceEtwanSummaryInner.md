# V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**device_name** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_et_wan_matrix_get200_response_device_etwan_summary_inner import V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner from a JSON string
v1_backbone_health_et_wan_matrix_get200_response_device_etwan_summary_inner_instance = V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner.to_json())

# convert the object into a dict
v1_backbone_health_et_wan_matrix_get200_response_device_etwan_summary_inner_dict = v1_backbone_health_et_wan_matrix_get200_response_device_etwan_summary_inner_instance.to_dict()
# create an instance of V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner from a dict
v1_backbone_health_et_wan_matrix_get200_response_device_etwan_summary_inner_from_dict = V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner.from_dict(v1_backbone_health_et_wan_matrix_get200_response_device_etwan_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


