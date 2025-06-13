# V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_pop_name** | **str** |  | [optional] 
**jitter** | **float** |  | [optional] 
**latency** | **float** |  | [optional] 
**loss** | **float** |  | [optional] 
**second_pop_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_client_session_details_post200_response_session_pop_links_inner import V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner from a JSON string
v2_assurance_topology_client_session_details_post200_response_session_pop_links_inner_instance = V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner.to_json())

# convert the object into a dict
v2_assurance_topology_client_session_details_post200_response_session_pop_links_inner_dict = v2_assurance_topology_client_session_details_post200_response_session_pop_links_inner_instance.to_dict()
# create an instance of V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner from a dict
v2_assurance_topology_client_session_details_post200_response_session_pop_links_inner_from_dict = V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner.from_dict(v2_assurance_topology_client_session_details_post200_response_session_pop_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


