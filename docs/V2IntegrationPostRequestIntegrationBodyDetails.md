# V2IntegrationPostRequestIntegrationBodyDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opsgenie_key** | **str** |  | [optional] 
**opsramp_details** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_integration_post_request_integration_body_details import V2IntegrationPostRequestIntegrationBodyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of V2IntegrationPostRequestIntegrationBodyDetails from a JSON string
v2_integration_post_request_integration_body_details_instance = V2IntegrationPostRequestIntegrationBodyDetails.from_json(json)
# print the JSON string representation of the object
print(V2IntegrationPostRequestIntegrationBodyDetails.to_json())

# convert the object into a dict
v2_integration_post_request_integration_body_details_dict = v2_integration_post_request_integration_body_details_instance.to_dict()
# create an instance of V2IntegrationPostRequestIntegrationBodyDetails from a dict
v2_integration_post_request_integration_body_details_from_dict = V2IntegrationPostRequestIntegrationBodyDetails.from_dict(v2_integration_post_request_integration_body_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


