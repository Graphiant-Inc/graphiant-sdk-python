# V1BackboneHealthOverviewPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**V1BackboneHealthOverviewPostRequestDimensions**](V1BackboneHealthOverviewPostRequestDimensions.md) |  | [optional] 
**filter** | [**V1BackboneHealthOverviewPostRequestFilter**](V1BackboneHealthOverviewPostRequestFilter.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_overview_post_request import V1BackboneHealthOverviewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthOverviewPostRequest from a JSON string
v1_backbone_health_overview_post_request_instance = V1BackboneHealthOverviewPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthOverviewPostRequest.to_json())

# convert the object into a dict
v1_backbone_health_overview_post_request_dict = v1_backbone_health_overview_post_request_instance.to_dict()
# create an instance of V1BackboneHealthOverviewPostRequest from a dict
v1_backbone_health_overview_post_request_from_dict = V1BackboneHealthOverviewPostRequest.from_dict(v1_backbone_health_overview_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


