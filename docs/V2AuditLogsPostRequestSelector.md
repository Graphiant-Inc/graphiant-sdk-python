# V2AuditLogsPostRequestSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** |  | [optional] 
**entities** | [**List[V1ActivityLogsPostRequestSelectorJobEntity]**](V1ActivityLogsPostRequestSelectorJobEntity.md) |  | [optional] 
**job_types** | **List[str]** |  | [optional] 
**targets** | [**List[V1ActivityLogsPostRequestSelectorJobEntity]**](V1ActivityLogsPostRequestSelectorJobEntity.md) |  | [optional] 
**users** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_audit_logs_post_request_selector import V2AuditLogsPostRequestSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V2AuditLogsPostRequestSelector from a JSON string
v2_audit_logs_post_request_selector_instance = V2AuditLogsPostRequestSelector.from_json(json)
# print the JSON string representation of the object
print(V2AuditLogsPostRequestSelector.to_json())

# convert the object into a dict
v2_audit_logs_post_request_selector_dict = v2_audit_logs_post_request_selector_instance.to_dict()
# create an instance of V2AuditLogsPostRequestSelector from a dict
v2_audit_logs_post_request_selector_from_dict = V2AuditLogsPostRequestSelector.from_dict(v2_audit_logs_post_request_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


