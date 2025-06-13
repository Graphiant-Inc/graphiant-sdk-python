# V1GlobalSummaryPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipfix_exported_type** | **bool** |  | [optional] 
**prefix_set_type** | **bool** |  | [optional] 
**routing_policy_type** | **bool** |  | [optional] 
**snmp_type** | **bool** |  | [optional] 
**syslog_server_type** | **bool** |  | [optional] 
**traffic_policy_type** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_summary_post_request import V1GlobalSummaryPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalSummaryPostRequest from a JSON string
v1_global_summary_post_request_instance = V1GlobalSummaryPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GlobalSummaryPostRequest.to_json())

# convert the object into a dict
v1_global_summary_post_request_dict = v1_global_summary_post_request_instance.to_dict()
# create an instance of V1GlobalSummaryPostRequest from a dict
v1_global_summary_post_request_from_dict = V1GlobalSummaryPostRequest.from_dict(v1_global_summary_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


