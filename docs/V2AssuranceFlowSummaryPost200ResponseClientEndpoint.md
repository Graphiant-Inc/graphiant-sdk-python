# V2AssuranceFlowSummaryPost200ResponseClientEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuits** | **List[str]** |  | [optional] 
**edges** | [**List[V2AssuranceFlowSummaryPost200ResponseClientEndpointEdgesInner]**](V2AssuranceFlowSummaryPost200ResponseClientEndpointEdgesInner.md) |  | [optional] 
**jitter** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter**](V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter.md) |  | [optional] 
**latency** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter**](V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter.md) |  | [optional] 
**loss** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter**](V2AssuranceFlowSummaryPost200ResponseClientEndpointJitter.md) |  | [optional] 
**site** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpointSite**](V2AssuranceFlowSummaryPost200ResponseClientEndpointSite.md) |  | [optional] 
**total_downlink_usage** | **int** |  | [optional] 
**total_uplink_usage** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_flow_summary_post200_response_client_endpoint import V2AssuranceFlowSummaryPost200ResponseClientEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceFlowSummaryPost200ResponseClientEndpoint from a JSON string
v2_assurance_flow_summary_post200_response_client_endpoint_instance = V2AssuranceFlowSummaryPost200ResponseClientEndpoint.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceFlowSummaryPost200ResponseClientEndpoint.to_json())

# convert the object into a dict
v2_assurance_flow_summary_post200_response_client_endpoint_dict = v2_assurance_flow_summary_post200_response_client_endpoint_instance.to_dict()
# create an instance of V2AssuranceFlowSummaryPost200ResponseClientEndpoint from a dict
v2_assurance_flow_summary_post200_response_client_endpoint_from_dict = V2AssuranceFlowSummaryPost200ResponseClientEndpoint.from_dict(v2_assurance_flow_summary_post200_response_client_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


