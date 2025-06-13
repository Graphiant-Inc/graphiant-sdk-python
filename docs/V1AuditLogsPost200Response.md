# V1AuditLogsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_ref** | **str** |  | [optional] 
**histogram** | [**List[V1AuditLogsPost200ResponseHistogramInner]**](V1AuditLogsPost200ResponseHistogramInner.md) |  | [optional] 
**logs** | [**List[V1AuditLogsPost200ResponseLogsInner]**](V1AuditLogsPost200ResponseLogsInner.md) |  | [optional] 
**total_logs** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_audit_logs_post200_response import V1AuditLogsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuditLogsPost200Response from a JSON string
v1_audit_logs_post200_response_instance = V1AuditLogsPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1AuditLogsPost200Response.to_json())

# convert the object into a dict
v1_audit_logs_post200_response_dict = v1_audit_logs_post200_response_instance.to_dict()
# create an instance of V1AuditLogsPost200Response from a dict
v1_audit_logs_post200_response_from_dict = V1AuditLogsPost200Response.from_dict(v1_audit_logs_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


