# V2MonitoringQueuePostRequestSelectorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | [optional] 
**interface_name** | **str** |  | [optional] 
**sla_class** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_queue_post_request_selectors_inner import V2MonitoringQueuePostRequestSelectorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringQueuePostRequestSelectorsInner from a JSON string
v2_monitoring_queue_post_request_selectors_inner_instance = V2MonitoringQueuePostRequestSelectorsInner.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringQueuePostRequestSelectorsInner.to_json())

# convert the object into a dict
v2_monitoring_queue_post_request_selectors_inner_dict = v2_monitoring_queue_post_request_selectors_inner_instance.to_dict()
# create an instance of V2MonitoringQueuePostRequestSelectorsInner from a dict
v2_monitoring_queue_post_request_selectors_inner_from_dict = V2MonitoringQueuePostRequestSelectorsInner.from_dict(v2_monitoring_queue_post_request_selectors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


