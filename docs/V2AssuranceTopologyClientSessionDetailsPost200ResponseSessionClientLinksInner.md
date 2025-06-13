# V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuit_name** | **str** |  | [optional] 
**jitter** | **float** |  | [optional] 
**latency** | **float** |  | [optional] 
**loss** | **float** |  | [optional] 
**pop_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_client_session_details_post200_response_session_client_links_inner import V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner from a JSON string
v2_assurance_topology_client_session_details_post200_response_session_client_links_inner_instance = V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner.to_json())

# convert the object into a dict
v2_assurance_topology_client_session_details_post200_response_session_client_links_inner_dict = v2_assurance_topology_client_session_details_post200_response_session_client_links_inner_instance.to_dict()
# create an instance of V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner from a dict
v2_assurance_topology_client_session_details_post200_response_session_client_links_inner_from_dict = V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner.from_dict(v2_assurance_topology_client_session_details_post200_response_session_client_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


