# V1BackboneHealthOverviewPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[V1BackboneHealthOverviewPost200ResponseDevicesInner]**](V1BackboneHealthOverviewPost200ResponseDevicesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_overview_post200_response import V1BackboneHealthOverviewPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthOverviewPost200Response from a JSON string
v1_backbone_health_overview_post200_response_instance = V1BackboneHealthOverviewPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthOverviewPost200Response.to_json())

# convert the object into a dict
v1_backbone_health_overview_post200_response_dict = v1_backbone_health_overview_post200_response_instance.to_dict()
# create an instance of V1BackboneHealthOverviewPost200Response from a dict
v1_backbone_health_overview_post200_response_from_dict = V1BackboneHealthOverviewPost200Response.from_dict(v1_backbone_health_overview_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


