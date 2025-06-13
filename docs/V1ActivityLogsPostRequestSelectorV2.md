# V1ActivityLogsPostRequestSelectorV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_ids** | **List[int]** |  | [optional] 
**entities** | [**List[V1ActivityLogsPostRequestSelectorJobEntity]**](V1ActivityLogsPostRequestSelectorJobEntity.md) |  | [optional] 
**site_ids** | **List[int]** |  | [optional] 
**statuses** | **List[str]** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_activity_logs_post_request_selector_v2 import V1ActivityLogsPostRequestSelectorV2

# TODO update the JSON string below
json = "{}"
# create an instance of V1ActivityLogsPostRequestSelectorV2 from a JSON string
v1_activity_logs_post_request_selector_v2_instance = V1ActivityLogsPostRequestSelectorV2.from_json(json)
# print the JSON string representation of the object
print(V1ActivityLogsPostRequestSelectorV2.to_json())

# convert the object into a dict
v1_activity_logs_post_request_selector_v2_dict = v1_activity_logs_post_request_selector_v2_instance.to_dict()
# create an instance of V1ActivityLogsPostRequestSelectorV2 from a dict
v1_activity_logs_post_request_selector_v2_from_dict = V1ActivityLogsPostRequestSelectorV2.from_dict(v1_activity_logs_post_request_selector_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


