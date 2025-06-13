# V2AuditLogsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_ref** | **str** |  | [optional] 
**num_logs** | **int** |  | [optional] 
**old_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**recent_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**selector** | [**V2AuditLogsPostRequestSelector**](V2AuditLogsPostRequestSelector.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_audit_logs_post_request import V2AuditLogsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AuditLogsPostRequest from a JSON string
v2_audit_logs_post_request_instance = V2AuditLogsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AuditLogsPostRequest.to_json())

# convert the object into a dict
v2_audit_logs_post_request_dict = v2_audit_logs_post_request_instance.to_dict()
# create an instance of V2AuditLogsPostRequest from a dict
v2_audit_logs_post_request_from_dict = V2AuditLogsPostRequest.from_dict(v2_audit_logs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


