# V1GatewaysSummaryGet200ResponseSummariesInnerGatewayDeviceSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**hostname** | **str** |  | [optional] 
**interface_id** | **int** |  | [optional] 
**maintenance_mode** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_summary_get200_response_summaries_inner_gateway_device_summary_inner import V1GatewaysSummaryGet200ResponseSummariesInnerGatewayDeviceSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysSummaryGet200ResponseSummariesInnerGatewayDeviceSummaryInner from a JSON string
v1_gateways_summary_get200_response_summaries_inner_gateway_device_summary_inner_instance = V1GatewaysSummaryGet200ResponseSummariesInnerGatewayDeviceSummaryInner.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysSummaryGet200ResponseSummariesInnerGatewayDeviceSummaryInner.to_json())

# convert the object into a dict
v1_gateways_summary_get200_response_summaries_inner_gateway_device_summary_inner_dict = v1_gateways_summary_get200_response_summaries_inner_gateway_device_summary_inner_instance.to_dict()
# create an instance of V1GatewaysSummaryGet200ResponseSummariesInnerGatewayDeviceSummaryInner from a dict
v1_gateways_summary_get200_response_summaries_inner_gateway_device_summary_inner_from_dict = V1GatewaysSummaryGet200ResponseSummariesInnerGatewayDeviceSummaryInner.from_dict(v1_gateways_summary_get200_response_summaries_inner_gateway_device_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


