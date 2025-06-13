# V2MonitoringQueueInstantPost200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**samples** | [**List[V2MonitoringBfdPost200ResponseDataInnerSamplesInner]**](V2MonitoringBfdPost200ResponseDataInnerSamplesInner.md) |  | [optional] 
**selector** | [**V2MonitoringQueueInstantPostRequestSelectorsInner**](V2MonitoringQueueInstantPostRequestSelectorsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_queue_instant_post200_response_data_inner import V2MonitoringQueueInstantPost200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringQueueInstantPost200ResponseDataInner from a JSON string
v2_monitoring_queue_instant_post200_response_data_inner_instance = V2MonitoringQueueInstantPost200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringQueueInstantPost200ResponseDataInner.to_json())

# convert the object into a dict
v2_monitoring_queue_instant_post200_response_data_inner_dict = v2_monitoring_queue_instant_post200_response_data_inner_instance.to_dict()
# create an instance of V2MonitoringQueueInstantPost200ResponseDataInner from a dict
v2_monitoring_queue_instant_post200_response_data_inner_from_dict = V2MonitoringQueueInstantPost200ResponseDataInner.from_dict(v2_monitoring_queue_instant_post200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


