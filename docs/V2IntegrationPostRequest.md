# V2IntegrationPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_body** | [**V2IntegrationPostRequestIntegrationBody**](V2IntegrationPostRequestIntegrationBody.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_integration_post_request import V2IntegrationPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2IntegrationPostRequest from a JSON string
v2_integration_post_request_instance = V2IntegrationPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2IntegrationPostRequest.to_json())

# convert the object into a dict
v2_integration_post_request_dict = v2_integration_post_request_instance.to_dict()
# create an instance of V2IntegrationPostRequest from a dict
v2_integration_post_request_from_dict = V2IntegrationPostRequest.from_dict(v2_integration_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


