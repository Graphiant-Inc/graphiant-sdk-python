# V2AssuranceEndpointIntelPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_endpoint_intel_post_request import V2AssuranceEndpointIntelPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceEndpointIntelPostRequest from a JSON string
v2_assurance_endpoint_intel_post_request_instance = V2AssuranceEndpointIntelPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceEndpointIntelPostRequest.to_json())

# convert the object into a dict
v2_assurance_endpoint_intel_post_request_dict = v2_assurance_endpoint_intel_post_request_instance.to_dict()
# create an instance of V2AssuranceEndpointIntelPostRequest from a dict
v2_assurance_endpoint_intel_post_request_from_dict = V2AssuranceEndpointIntelPostRequest.from_dict(v2_assurance_endpoint_intel_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


