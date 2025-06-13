# V1LogsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_ref** | **str** |  | [optional] 
**histogram** | [**List[V1AuditLogsPost200ResponseHistogramInner]**](V1AuditLogsPost200ResponseHistogramInner.md) |  | [optional] 
**logs** | [**List[V1LogsPost200ResponseLogsInner]**](V1LogsPost200ResponseLogsInner.md) |  | [optional] 
**total_logs** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_logs_post200_response import V1LogsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1LogsPost200Response from a JSON string
v1_logs_post200_response_instance = V1LogsPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1LogsPost200Response.to_json())

# convert the object into a dict
v1_logs_post200_response_dict = v1_logs_post200_response_instance.to_dict()
# create an instance of V1LogsPost200Response from a dict
v1_logs_post200_response_from_dict = V1LogsPost200Response.from_dict(v1_logs_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


