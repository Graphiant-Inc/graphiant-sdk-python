# V2AssuranceTopologyOverviewPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_applications** | **int** |  | [optional] 
**num_flows** | **int** |  | [optional] 
**topology** | [**V2AssuranceTopologyOverviewPost200ResponseTopology**](V2AssuranceTopologyOverviewPost200ResponseTopology.md) |  | [optional] 
**topology_change_ts** | [**List[V1AlarmHistoryGet200ResponseHistoryInnerTime]**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**traffic_regions** | [**List[V2AssuranceTopologyOverviewPost200ResponseTrafficRegionsInner]**](V2AssuranceTopologyOverviewPost200ResponseTrafficRegionsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_overview_post200_response import V2AssuranceTopologyOverviewPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyOverviewPost200Response from a JSON string
v2_assurance_topology_overview_post200_response_instance = V2AssuranceTopologyOverviewPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyOverviewPost200Response.to_json())

# convert the object into a dict
v2_assurance_topology_overview_post200_response_dict = v2_assurance_topology_overview_post200_response_instance.to_dict()
# create an instance of V2AssuranceTopologyOverviewPost200Response from a dict
v2_assurance_topology_overview_post200_response_from_dict = V2AssuranceTopologyOverviewPost200Response.from_dict(v2_assurance_topology_overview_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


