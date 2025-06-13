# V1AuditLogsPost200ResponseLogsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **str** |  | [optional] 
**actor** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**end** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**failed_target_results** | [**List[V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner]**](V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner.md) |  | [optional] 
**info** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**start** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**status** | **str** |  | [optional] 
**targets** | [**List[V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner]**](V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_audit_logs_post200_response_logs_inner import V1AuditLogsPost200ResponseLogsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuditLogsPost200ResponseLogsInner from a JSON string
v1_audit_logs_post200_response_logs_inner_instance = V1AuditLogsPost200ResponseLogsInner.from_json(json)
# print the JSON string representation of the object
print(V1AuditLogsPost200ResponseLogsInner.to_json())

# convert the object into a dict
v1_audit_logs_post200_response_logs_inner_dict = v1_audit_logs_post200_response_logs_inner_instance.to_dict()
# create an instance of V1AuditLogsPost200ResponseLogsInner from a dict
v1_audit_logs_post200_response_logs_inner_from_dict = V1AuditLogsPost200ResponseLogsInner.from_dict(v1_audit_logs_post200_response_logs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


