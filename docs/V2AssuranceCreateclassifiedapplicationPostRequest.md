# V2AssuranceCreateclassifiedapplicationPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**ip_prefix_list** | **List[str]** |  | [optional] 
**port_list** | **List[str]** |  | [optional] 
**protocol_list** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_createclassifiedapplication_post_request import V2AssuranceCreateclassifiedapplicationPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceCreateclassifiedapplicationPostRequest from a JSON string
v2_assurance_createclassifiedapplication_post_request_instance = V2AssuranceCreateclassifiedapplicationPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceCreateclassifiedapplicationPostRequest.to_json())

# convert the object into a dict
v2_assurance_createclassifiedapplication_post_request_dict = v2_assurance_createclassifiedapplication_post_request_instance.to_dict()
# create an instance of V2AssuranceCreateclassifiedapplicationPostRequest from a dict
v2_assurance_createclassifiedapplication_post_request_from_dict = V2AssuranceCreateclassifiedapplicationPostRequest.from_dict(v2_assurance_createclassifiedapplication_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


