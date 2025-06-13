# V2MonitoringQueuePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[V2MonitoringQueuePost200ResponseDataInner]**](V2MonitoringQueuePost200ResponseDataInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_queue_post200_response import V2MonitoringQueuePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringQueuePost200Response from a JSON string
v2_monitoring_queue_post200_response_instance = V2MonitoringQueuePost200Response.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringQueuePost200Response.to_json())

# convert the object into a dict
v2_monitoring_queue_post200_response_dict = v2_monitoring_queue_post200_response_instance.to_dict()
# create an instance of V2MonitoringQueuePost200Response from a dict
v2_monitoring_queue_post200_response_from_dict = V2MonitoringQueuePost200Response.from_dict(v2_monitoring_queue_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


