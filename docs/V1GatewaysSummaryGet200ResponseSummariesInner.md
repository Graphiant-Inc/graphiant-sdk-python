# V1GatewaysSummaryGet200ResponseSummariesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**gateway_device_summary** | [**List[V1GatewaysSummaryGet200ResponseSummariesInnerGatewayDeviceSummaryInner]**](V1GatewaysSummaryGet200ResponseSummariesInnerGatewayDeviceSummaryInner.md) |  | [optional] 
**graphiant_region** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**speed** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**support_status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_summary_get200_response_summaries_inner import V1GatewaysSummaryGet200ResponseSummariesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysSummaryGet200ResponseSummariesInner from a JSON string
v1_gateways_summary_get200_response_summaries_inner_instance = V1GatewaysSummaryGet200ResponseSummariesInner.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysSummaryGet200ResponseSummariesInner.to_json())

# convert the object into a dict
v1_gateways_summary_get200_response_summaries_inner_dict = v1_gateways_summary_get200_response_summaries_inner_instance.to_dict()
# create an instance of V1GatewaysSummaryGet200ResponseSummariesInner from a dict
v1_gateways_summary_get200_response_summaries_inner_from_dict = V1GatewaysSummaryGet200ResponseSummariesInner.from_dict(v1_gateways_summary_get200_response_summaries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


