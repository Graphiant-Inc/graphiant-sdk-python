# V1AuditLogsPost200ResponseHistogramInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_audit_logs_post200_response_histogram_inner import V1AuditLogsPost200ResponseHistogramInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuditLogsPost200ResponseHistogramInner from a JSON string
v1_audit_logs_post200_response_histogram_inner_instance = V1AuditLogsPost200ResponseHistogramInner.from_json(json)
# print the JSON string representation of the object
print(V1AuditLogsPost200ResponseHistogramInner.to_json())

# convert the object into a dict
v1_audit_logs_post200_response_histogram_inner_dict = v1_audit_logs_post200_response_histogram_inner_instance.to_dict()
# create an instance of V1AuditLogsPost200ResponseHistogramInner from a dict
v1_audit_logs_post200_response_histogram_inner_from_dict = V1AuditLogsPost200ResponseHistogramInner.from_dict(v1_audit_logs_post200_response_histogram_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


