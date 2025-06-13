# V2AuditLogsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_ref** | **str** |  | [optional] 
**logs** | [**List[V2AuditLogsPost200ResponseLogsInner]**](V2AuditLogsPost200ResponseLogsInner.md) |  | [optional] 
**total_logs** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_audit_logs_post200_response import V2AuditLogsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AuditLogsPost200Response from a JSON string
v2_audit_logs_post200_response_instance = V2AuditLogsPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2AuditLogsPost200Response.to_json())

# convert the object into a dict
v2_audit_logs_post200_response_dict = v2_audit_logs_post200_response_instance.to_dict()
# create an instance of V2AuditLogsPost200Response from a dict
v2_audit_logs_post200_response_from_dict = V2AuditLogsPost200Response.from_dict(v2_audit_logs_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


