# V2MonitoringExtranetServiceStatusDetailsGet200ResponseStatusesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**statuses** | [**List[V2MonitoringExtranetServiceStatusDetailsGet200ResponseStatusesInnerStatusesInner]**](V2MonitoringExtranetServiceStatusDetailsGet200ResponseStatusesInnerStatusesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_extranet_service_status_details_get200_response_statuses_inner import V2MonitoringExtranetServiceStatusDetailsGet200ResponseStatusesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringExtranetServiceStatusDetailsGet200ResponseStatusesInner from a JSON string
v2_monitoring_extranet_service_status_details_get200_response_statuses_inner_instance = V2MonitoringExtranetServiceStatusDetailsGet200ResponseStatusesInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringExtranetServiceStatusDetailsGet200ResponseStatusesInner.to_json())

# convert the object into a dict
v2_monitoring_extranet_service_status_details_get200_response_statuses_inner_dict = v2_monitoring_extranet_service_status_details_get200_response_statuses_inner_instance.to_dict()
# create an instance of V2MonitoringExtranetServiceStatusDetailsGet200ResponseStatusesInner from a dict
v2_monitoring_extranet_service_status_details_get200_response_statuses_inner_from_dict = V2MonitoringExtranetServiceStatusDetailsGet200ResponseStatusesInner.from_dict(v2_monitoring_extranet_service_status_details_get200_response_statuses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


