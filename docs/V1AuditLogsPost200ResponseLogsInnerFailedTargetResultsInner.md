# V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**target** | [**V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInnerTarget**](V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInnerTarget.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_audit_logs_post200_response_logs_inner_failed_target_results_inner import V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner from a JSON string
v1_audit_logs_post200_response_logs_inner_failed_target_results_inner_instance = V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner.from_json(json)
# print the JSON string representation of the object
print(V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner.to_json())

# convert the object into a dict
v1_audit_logs_post200_response_logs_inner_failed_target_results_inner_dict = v1_audit_logs_post200_response_logs_inner_failed_target_results_inner_instance.to_dict()
# create an instance of V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner from a dict
v1_audit_logs_post200_response_logs_inner_failed_target_results_inner_from_dict = V1AuditLogsPost200ResponseLogsInnerFailedTargetResultsInner.from_dict(v1_audit_logs_post200_response_logs_inner_failed_target_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


