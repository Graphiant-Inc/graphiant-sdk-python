# V1BackboneHealthFilterGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuits** | [**List[V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionLocalDiaLinksInner]**](V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionLocalDiaLinksInner.md) |  | [optional] 
**devices** | [**List[V2AssuranceFlowSummaryPost200ResponseClientEndpointEdgesInner]**](V2AssuranceFlowSummaryPost200ResponseClientEndpointEdgesInner.md) |  | [optional] 
**lan_segments** | [**List[V1BackboneHealthFilterGet200ResponseLanSegmentsInner]**](V1BackboneHealthFilterGet200ResponseLanSegmentsInner.md) |  | [optional] 
**regions** | [**List[V1BackboneHealthFilterGet200ResponseRegionsInner]**](V1BackboneHealthFilterGet200ResponseRegionsInner.md) |  | [optional] 
**sites** | [**List[V1BackboneHealthFilterGet200ResponseSitesInner]**](V1BackboneHealthFilterGet200ResponseSitesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_filter_get200_response import V1BackboneHealthFilterGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthFilterGet200Response from a JSON string
v1_backbone_health_filter_get200_response_instance = V1BackboneHealthFilterGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthFilterGet200Response.to_json())

# convert the object into a dict
v1_backbone_health_filter_get200_response_dict = v1_backbone_health_filter_get200_response_instance.to_dict()
# create an instance of V1BackboneHealthFilterGet200Response from a dict
v1_backbone_health_filter_get200_response_from_dict = V1BackboneHealthFilterGet200Response.from_dict(v1_backbone_health_filter_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


