# V1DevicesSummaryGet200ResponseSitesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[V1DevicesSummaryGet200ResponseSitesInnerDevicesInner]**](V1DevicesSummaryGet200ResponseSitesInnerDevicesInner.md) |  | [optional] 
**site_id** | **int** |  | [optional] 
**site_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_summary_get200_response_sites_inner import V1DevicesSummaryGet200ResponseSitesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesSummaryGet200ResponseSitesInner from a JSON string
v1_devices_summary_get200_response_sites_inner_instance = V1DevicesSummaryGet200ResponseSitesInner.from_json(json)
# print the JSON string representation of the object
print(V1DevicesSummaryGet200ResponseSitesInner.to_json())

# convert the object into a dict
v1_devices_summary_get200_response_sites_inner_dict = v1_devices_summary_get200_response_sites_inner_instance.to_dict()
# create an instance of V1DevicesSummaryGet200ResponseSitesInner from a dict
v1_devices_summary_get200_response_sites_inner_from_dict = V1DevicesSummaryGet200ResponseSitesInner.from_dict(v1_devices_summary_get200_response_sites_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


