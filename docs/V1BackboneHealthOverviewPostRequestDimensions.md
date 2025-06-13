# V1BackboneHealthOverviewPostRequestDimensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_expiry** | **bool** |  | [optional] 
**core_connectivity** | **bool** |  | [optional] 
**core_core_sla_performance** | **bool** |  | [optional] 
**core_wan_performance** | **bool** |  | [optional] 
**cpu** | **bool** |  | [optional] 
**crashes** | **bool** |  | [optional] 
**credit_expiry** | **bool** |  | [optional] 
**disk** | **bool** |  | [optional] 
**fan_speed** | **bool** |  | [optional] 
**license_expiry** | **bool** |  | [optional] 
**memory** | **bool** |  | [optional] 
**odp_connectivity** | **bool** |  | [optional] 
**t2_connectivity** | **bool** |  | [optional] 
**temperature** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_overview_post_request_dimensions import V1BackboneHealthOverviewPostRequestDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthOverviewPostRequestDimensions from a JSON string
v1_backbone_health_overview_post_request_dimensions_instance = V1BackboneHealthOverviewPostRequestDimensions.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthOverviewPostRequestDimensions.to_json())

# convert the object into a dict
v1_backbone_health_overview_post_request_dimensions_dict = v1_backbone_health_overview_post_request_dimensions_instance.to_dict()
# create an instance of V1BackboneHealthOverviewPostRequestDimensions from a dict
v1_backbone_health_overview_post_request_dimensions_from_dict = V1BackboneHealthOverviewPostRequestDimensions.from_dict(v1_backbone_health_overview_post_request_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


