# V1BackboneHealthOverviewPostRequestFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuit_names** | **List[str]** |  | [optional] 
**device_ids** | **List[int]** |  | [optional] 
**lan_segments** | **List[str]** |  | [optional] 
**region_ids** | **List[int]** |  | [optional] 
**site_ids** | **List[int]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_overview_post_request_filter import V1BackboneHealthOverviewPostRequestFilter

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthOverviewPostRequestFilter from a JSON string
v1_backbone_health_overview_post_request_filter_instance = V1BackboneHealthOverviewPostRequestFilter.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthOverviewPostRequestFilter.to_json())

# convert the object into a dict
v1_backbone_health_overview_post_request_filter_dict = v1_backbone_health_overview_post_request_filter_instance.to_dict()
# create an instance of V1BackboneHealthOverviewPostRequestFilter from a dict
v1_backbone_health_overview_post_request_filter_from_dict = V1BackboneHealthOverviewPostRequestFilter.from_dict(v1_backbone_health_overview_post_request_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


