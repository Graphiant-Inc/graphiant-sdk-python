# V1ExtranetSitesUsagePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bw_allocation** | **int** |  | [optional] 
**dl_stats** | [**List[V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner]**](V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner.md) |  | [optional] 
**ul_stats** | [**List[V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner]**](V2ExtranetServiceOvertimeConsumptionPost200ResponseDlAggStatsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_sites_usage_post200_response import V1ExtranetSitesUsagePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetSitesUsagePost200Response from a JSON string
v1_extranet_sites_usage_post200_response_instance = V1ExtranetSitesUsagePost200Response.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetSitesUsagePost200Response.to_json())

# convert the object into a dict
v1_extranet_sites_usage_post200_response_dict = v1_extranet_sites_usage_post200_response_instance.to_dict()
# create an instance of V1ExtranetSitesUsagePost200Response from a dict
v1_extranet_sites_usage_post200_response_from_dict = V1ExtranetSitesUsagePost200Response.from_dict(v1_extranet_sites_usage_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


