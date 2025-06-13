# V2AssuranceTopologyRegionSummaryPost200ResponseSitesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_count** | **int** |  | [optional] 
**lan_segments** | **List[str]** |  | [optional] 
**pop_names** | **List[str]** |  | [optional] 
**region_name** | **str** |  | [optional] 
**site_id** | **int** |  | [optional] 
**site_name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_region_summary_post200_response_sites_inner import V2AssuranceTopologyRegionSummaryPost200ResponseSitesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyRegionSummaryPost200ResponseSitesInner from a JSON string
v2_assurance_topology_region_summary_post200_response_sites_inner_instance = V2AssuranceTopologyRegionSummaryPost200ResponseSitesInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyRegionSummaryPost200ResponseSitesInner.to_json())

# convert the object into a dict
v2_assurance_topology_region_summary_post200_response_sites_inner_dict = v2_assurance_topology_region_summary_post200_response_sites_inner_instance.to_dict()
# create an instance of V2AssuranceTopologyRegionSummaryPost200ResponseSitesInner from a dict
v2_assurance_topology_region_summary_post200_response_sites_inner_from_dict = V2AssuranceTopologyRegionSummaryPost200ResponseSitesInner.from_dict(v2_assurance_topology_region_summary_post200_response_sites_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


