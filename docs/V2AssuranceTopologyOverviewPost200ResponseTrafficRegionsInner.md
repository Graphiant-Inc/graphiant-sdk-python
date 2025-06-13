# V2AssuranceTopologyOverviewPost200ResponseTrafficRegionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_sites** | **int** |  | [optional] 
**region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_overview_post200_response_traffic_regions_inner import V2AssuranceTopologyOverviewPost200ResponseTrafficRegionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyOverviewPost200ResponseTrafficRegionsInner from a JSON string
v2_assurance_topology_overview_post200_response_traffic_regions_inner_instance = V2AssuranceTopologyOverviewPost200ResponseTrafficRegionsInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyOverviewPost200ResponseTrafficRegionsInner.to_json())

# convert the object into a dict
v2_assurance_topology_overview_post200_response_traffic_regions_inner_dict = v2_assurance_topology_overview_post200_response_traffic_regions_inner_instance.to_dict()
# create an instance of V2AssuranceTopologyOverviewPost200ResponseTrafficRegionsInner from a dict
v2_assurance_topology_overview_post200_response_traffic_regions_inner_from_dict = V2AssuranceTopologyOverviewPost200ResponseTrafficRegionsInner.from_dict(v2_assurance_topology_overview_post200_response_traffic_regions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


