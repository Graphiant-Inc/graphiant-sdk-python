# V2AssuranceTopologyClientSessionsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions** | [**List[V2AssuranceTopologyClientSessionDetailsPost200ResponseSession]**](V2AssuranceTopologyClientSessionDetailsPost200ResponseSession.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_client_sessions_post200_response import V2AssuranceTopologyClientSessionsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyClientSessionsPost200Response from a JSON string
v2_assurance_topology_client_sessions_post200_response_instance = V2AssuranceTopologyClientSessionsPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyClientSessionsPost200Response.to_json())

# convert the object into a dict
v2_assurance_topology_client_sessions_post200_response_dict = v2_assurance_topology_client_sessions_post200_response_instance.to_dict()
# create an instance of V2AssuranceTopologyClientSessionsPost200Response from a dict
v2_assurance_topology_client_sessions_post200_response_from_dict = V2AssuranceTopologyClientSessionsPost200Response.from_dict(v2_assurance_topology_client_sessions_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


