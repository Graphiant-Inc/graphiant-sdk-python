# V2AuditLogsPost200ResponseLogsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**activity_id** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**entity** | [**V1ActivityLogsPostRequestSelectorJobEntity**](V1ActivityLogsPostRequestSelectorJobEntity.md) |  | [optional] 
**job_type** | **str** |  | [optional] 
**target** | [**V1ActivityLogsPostRequestSelectorJobEntity**](V1ActivityLogsPostRequestSelectorJobEntity.md) |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**user** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_audit_logs_post200_response_logs_inner import V2AuditLogsPost200ResponseLogsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AuditLogsPost200ResponseLogsInner from a JSON string
v2_audit_logs_post200_response_logs_inner_instance = V2AuditLogsPost200ResponseLogsInner.from_json(json)
# print the JSON string representation of the object
print(V2AuditLogsPost200ResponseLogsInner.to_json())

# convert the object into a dict
v2_audit_logs_post200_response_logs_inner_dict = v2_audit_logs_post200_response_logs_inner_instance.to_dict()
# create an instance of V2AuditLogsPost200ResponseLogsInner from a dict
v2_audit_logs_post200_response_logs_inner_from_dict = V2AuditLogsPost200ResponseLogsInner.from_dict(v2_audit_logs_post200_response_logs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


