# V2ExtranetSitesConsumptionOverviewPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_b2_b** | **bool** |  | [optional] 
**is_provider** | **bool** |  | [optional] 
**site_id** | **int** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 
**vrf_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_extranet_sites_consumption_overview_post_request import V2ExtranetSitesConsumptionOverviewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2ExtranetSitesConsumptionOverviewPostRequest from a JSON string
v2_extranet_sites_consumption_overview_post_request_instance = V2ExtranetSitesConsumptionOverviewPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2ExtranetSitesConsumptionOverviewPostRequest.to_json())

# convert the object into a dict
v2_extranet_sites_consumption_overview_post_request_dict = v2_extranet_sites_consumption_overview_post_request_instance.to_dict()
# create an instance of V2ExtranetSitesConsumptionOverviewPostRequest from a dict
v2_extranet_sites_consumption_overview_post_request_from_dict = V2ExtranetSitesConsumptionOverviewPostRequest.from_dict(v2_extranet_sites_consumption_overview_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


