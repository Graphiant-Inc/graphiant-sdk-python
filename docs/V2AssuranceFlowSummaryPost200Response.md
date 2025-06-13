# V2AssuranceFlowSummaryPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**bucket** | **str** |  | [optional] 
**client_endpoint** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpoint**](V2AssuranceFlowSummaryPost200ResponseClientEndpoint.md) |  | [optional] 
**client_ip** | **str** |  | [optional] 
**first_seen_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**lan_segment** | **str** |  | [optional] 
**last_seen_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**risk_status** | **str** |  | [optional] 
**server_endpoint** | [**V2AssuranceFlowSummaryPost200ResponseClientEndpoint**](V2AssuranceFlowSummaryPost200ResponseClientEndpoint.md) |  | [optional] 
**server_ip** | **str** |  | [optional] 
**server_port** | **int** |  | [optional] 
**sla_class** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_flow_summary_post200_response import V2AssuranceFlowSummaryPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceFlowSummaryPost200Response from a JSON string
v2_assurance_flow_summary_post200_response_instance = V2AssuranceFlowSummaryPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceFlowSummaryPost200Response.to_json())

# convert the object into a dict
v2_assurance_flow_summary_post200_response_dict = v2_assurance_flow_summary_post200_response_instance.to_dict()
# create an instance of V2AssuranceFlowSummaryPost200Response from a dict
v2_assurance_flow_summary_post200_response_from_dict = V2AssuranceFlowSummaryPost200Response.from_dict(v2_assurance_flow_summary_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


