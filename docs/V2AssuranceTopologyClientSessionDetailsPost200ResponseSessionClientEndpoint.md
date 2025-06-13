# V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuits** | **List[str]** |  | [optional] 
**edges** | [**List[V2AssuranceFlowSummaryPost200ResponseClientEndpointEdgesInner]**](V2AssuranceFlowSummaryPost200ResponseClientEndpointEdgesInner.md) |  | [optional] 
**is_gateway** | **bool** |  | [optional] 
**jitter** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter**](V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter.md) |  | [optional] 
**latency** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter**](V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter.md) |  | [optional] 
**loss** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter**](V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter.md) |  | [optional] 
**site** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointSite**](V2AssuranceFlowSummaryPost200ResponseClientEndpointSite.md) |  | [optional] 
**total_downlink_usage** | **int** |  | [optional] 
**total_uplink_usage** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_client_session_details_post200_response_session_client_endpoint import V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint from a JSON string
v2_assurance_topology_client_session_details_post200_response_session_client_endpoint_instance = V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint.to_json())

# convert the object into a dict
v2_assurance_topology_client_session_details_post200_response_session_client_endpoint_dict = v2_assurance_topology_client_session_details_post200_response_session_client_endpoint_instance.to_dict()
# create an instance of V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint from a dict
v2_assurance_topology_client_session_details_post200_response_session_client_endpoint_from_dict = V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint.from_dict(v2_assurance_topology_client_session_details_post200_response_session_client_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


