# V2MonitoringExtranetEdgeStatusGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_statuses** | [**List[V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner]**](V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_extranet_edge_status_get200_response import V2MonitoringExtranetEdgeStatusGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringExtranetEdgeStatusGet200Response from a JSON string
v2_monitoring_extranet_edge_status_get200_response_instance = V2MonitoringExtranetEdgeStatusGet200Response.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringExtranetEdgeStatusGet200Response.to_json())

# convert the object into a dict
v2_monitoring_extranet_edge_status_get200_response_dict = v2_monitoring_extranet_edge_status_get200_response_instance.to_dict()
# create an instance of V2MonitoringExtranetEdgeStatusGet200Response from a dict
v2_monitoring_extranet_edge_status_get200_response_from_dict = V2MonitoringExtranetEdgeStatusGet200Response.from_dict(v2_monitoring_extranet_edge_status_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


