# V2ExtranetSitesConsumptionOverviewPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lan_segments** | [**List[V2ExtranetSitesConsumptionOverviewPost200ResponseLanSegmentsInner]**](V2ExtranetSitesConsumptionOverviewPost200ResponseLanSegmentsInner.md) |  | [optional] 
**regions** | [**List[V2ExtranetSitesConsumptionOverviewPost200ResponseLanSegmentsInner]**](V2ExtranetSitesConsumptionOverviewPost200ResponseLanSegmentsInner.md) |  | [optional] 
**sites** | [**List[V2ExtranetSitesConsumptionOverviewPost200ResponseLanSegmentsInner]**](V2ExtranetSitesConsumptionOverviewPost200ResponseLanSegmentsInner.md) |  | [optional] 
**total_usage** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_extranet_sites_consumption_overview_post200_response import V2ExtranetSitesConsumptionOverviewPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2ExtranetSitesConsumptionOverviewPost200Response from a JSON string
v2_extranet_sites_consumption_overview_post200_response_instance = V2ExtranetSitesConsumptionOverviewPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2ExtranetSitesConsumptionOverviewPost200Response.to_json())

# convert the object into a dict
v2_extranet_sites_consumption_overview_post200_response_dict = v2_extranet_sites_consumption_overview_post200_response_instance.to_dict()
# create an instance of V2ExtranetSitesConsumptionOverviewPost200Response from a dict
v2_extranet_sites_consumption_overview_post200_response_from_dict = V2ExtranetSitesConsumptionOverviewPost200Response.from_dict(v2_extranet_sites_consumption_overview_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


