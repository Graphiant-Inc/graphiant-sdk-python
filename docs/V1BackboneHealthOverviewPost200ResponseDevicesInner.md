# V1BackboneHealthOverviewPost200ResponseDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_status** | **str** |  | [optional] 
**data_status** | **str** |  | [optional] 
**device_id** | **int** |  | [optional] 
**device_name** | **str** |  | [optional] 
**device_role** | **str** |  | [optional] 
**overall_status** | **str** |  | [optional] 
**region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 
**selected_status** | **str** |  | [optional] 
**system_status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_overview_post200_response_devices_inner import V1BackboneHealthOverviewPost200ResponseDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthOverviewPost200ResponseDevicesInner from a JSON string
v1_backbone_health_overview_post200_response_devices_inner_instance = V1BackboneHealthOverviewPost200ResponseDevicesInner.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthOverviewPost200ResponseDevicesInner.to_json())

# convert the object into a dict
v1_backbone_health_overview_post200_response_devices_inner_dict = v1_backbone_health_overview_post200_response_devices_inner_instance.to_dict()
# create an instance of V1BackboneHealthOverviewPost200ResponseDevicesInner from a dict
v1_backbone_health_overview_post200_response_devices_inner_from_dict = V1BackboneHealthOverviewPost200ResponseDevicesInner.from_dict(v1_backbone_health_overview_post200_response_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


