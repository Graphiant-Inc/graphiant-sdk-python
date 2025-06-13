# V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bwuage_edge_provider** | [**List[V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetailsBwuageEdgeProviderInner]**](V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetailsBwuageEdgeProviderInner.md) |  | [optional] 
**bwuage_provider** | [**List[V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetailsBwuageProviderInner]**](V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetailsBwuageProviderInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_bwtracker_region_site_details_post200_response_bwusage_details import V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetails from a JSON string
v1_bwtracker_region_site_details_post200_response_bwusage_details_instance = V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetails.from_json(json)
# print the JSON string representation of the object
print(V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetails.to_json())

# convert the object into a dict
v1_bwtracker_region_site_details_post200_response_bwusage_details_dict = v1_bwtracker_region_site_details_post200_response_bwusage_details_instance.to_dict()
# create an instance of V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetails from a dict
v1_bwtracker_region_site_details_post200_response_bwusage_details_from_dict = V1BwtrackerRegionSiteDetailsPost200ResponseBwusageDetails.from_dict(v1_bwtracker_region_site_details_post200_response_bwusage_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


