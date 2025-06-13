# V1ActivityLogsPostRequestSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_ids** | **List[int]** |  | [optional] 
**id** | **str** |  | [optional] 
**in_progress** | **bool** |  | [optional] 
**job_entity** | [**V1ActivityLogsPostRequestSelectorJobEntity**](V1ActivityLogsPostRequestSelectorJobEntity.md) |  | [optional] 
**target_ids** | [**List[V1ActivityLogsPostRequestSelectorJobEntity]**](V1ActivityLogsPostRequestSelectorJobEntity.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_activity_logs_post_request_selector import V1ActivityLogsPostRequestSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1ActivityLogsPostRequestSelector from a JSON string
v1_activity_logs_post_request_selector_instance = V1ActivityLogsPostRequestSelector.from_json(json)
# print the JSON string representation of the object
print(V1ActivityLogsPostRequestSelector.to_json())

# convert the object into a dict
v1_activity_logs_post_request_selector_dict = v1_activity_logs_post_request_selector_instance.to_dict()
# create an instance of V1ActivityLogsPostRequestSelector from a dict
v1_activity_logs_post_request_selector_from_dict = V1ActivityLogsPostRequestSelector.from_dict(v1_activity_logs_post_request_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


