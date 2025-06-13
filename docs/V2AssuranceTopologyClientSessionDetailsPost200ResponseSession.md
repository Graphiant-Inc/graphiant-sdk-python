# V2AssuranceTopologyClientSessionDetailsPost200ResponseSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**bucket** | **str** |  | [optional] 
**client_endpoint** | [**V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint**](V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint.md) |  | [optional] 
**client_flex_algo** | **str** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**client_links** | [**List[V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner]**](V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner.md) |  | [optional] 
**first_seen_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**lan_segment** | **List[str]** |  | [optional] 
**last_seen_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**local_dia_links** | [**List[V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionLocalDiaLinksInner]**](V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionLocalDiaLinksInner.md) |  | [optional] 
**pop_links** | [**List[V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner]**](V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner.md) |  | [optional] 
**remote_dia_links** | [**List[V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionLocalDiaLinksInner]**](V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionLocalDiaLinksInner.md) |  | [optional] 
**risk_status** | **str** |  | [optional] 
**server_endpoint** | [**V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint**](V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientEndpoint.md) |  | [optional] 
**server_flex_algos** | **List[str]** |  | [optional] 
**server_ip** | **str** |  | [optional] 
**server_links** | [**List[V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner]**](V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionClientLinksInner.md) |  | [optional] 
**server_port** | **int** |  | [optional] 
**session_id** | **str** |  | [optional] 
**sla** | **str** |  | [optional] 
**sla_class** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_client_session_details_post200_response_session import V2AssuranceTopologyClientSessionDetailsPost200ResponseSession

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyClientSessionDetailsPost200ResponseSession from a JSON string
v2_assurance_topology_client_session_details_post200_response_session_instance = V2AssuranceTopologyClientSessionDetailsPost200ResponseSession.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyClientSessionDetailsPost200ResponseSession.to_json())

# convert the object into a dict
v2_assurance_topology_client_session_details_post200_response_session_dict = v2_assurance_topology_client_session_details_post200_response_session_instance.to_dict()
# create an instance of V2AssuranceTopologyClientSessionDetailsPost200ResponseSession from a dict
v2_assurance_topology_client_session_details_post200_response_session_from_dict = V2AssuranceTopologyClientSessionDetailsPost200ResponseSession.from_dict(v2_assurance_topology_client_session_details_post200_response_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


