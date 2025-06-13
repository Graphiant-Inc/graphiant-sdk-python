# V1ActivityLogsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_ref** | **str** |  | [optional] 
**details** | [**List[V1ActivityLogsPost200ResponseDetailsInner]**](V1ActivityLogsPost200ResponseDetailsInner.md) |  | [optional] 
**filter_entities** | [**Dict[str, V1ActivityLogsPost200ResponseFilterEntitiesValue]**](V1ActivityLogsPost200ResponseFilterEntitiesValue.md) |  | [optional] 
**filter_job_types** | **List[str]** |  | [optional] 
**total_logs** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_activity_logs_post200_response import V1ActivityLogsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ActivityLogsPost200Response from a JSON string
v1_activity_logs_post200_response_instance = V1ActivityLogsPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1ActivityLogsPost200Response.to_json())

# convert the object into a dict
v1_activity_logs_post200_response_dict = v1_activity_logs_post200_response_instance.to_dict()
# create an instance of V1ActivityLogsPost200Response from a dict
v1_activity_logs_post200_response_from_dict = V1ActivityLogsPost200Response.from_dict(v1_activity_logs_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


