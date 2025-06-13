# V2ExtranetServiceOvertimeConsumptionPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dl_agg_stats** | [**List[V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner]**](V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner.md) |  | [optional] 
**ul_agg_stats** | [**List[V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner]**](V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_extranet_service_overtime_consumption_post200_response import V2ExtranetServiceOvertimeConsumptionPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2ExtranetServiceOvertimeConsumptionPost200Response from a JSON string
v2_extranet_service_overtime_consumption_post200_response_instance = V2ExtranetServiceOvertimeConsumptionPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2ExtranetServiceOvertimeConsumptionPost200Response.to_json())

# convert the object into a dict
v2_extranet_service_overtime_consumption_post200_response_dict = v2_extranet_service_overtime_consumption_post200_response_instance.to_dict()
# create an instance of V2ExtranetServiceOvertimeConsumptionPost200Response from a dict
v2_extranet_service_overtime_consumption_post200_response_from_dict = V2ExtranetServiceOvertimeConsumptionPost200Response.from_dict(v2_extranet_service_overtime_consumption_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


