# V2IntegrationIntegrationIdPutRequestIntegrationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**V2IntegrationPostRequestIntegrationBodyDetails**](V2IntegrationPostRequestIntegrationBodyDetails.md) |  | [optional] 
**enterprise** | **int** |  | [optional] 
**integration_type** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_integration_integration_id_put_request_integration_body import V2IntegrationIntegrationIdPutRequestIntegrationBody

# TODO update the JSON string below
json = "{}"
# create an instance of V2IntegrationIntegrationIdPutRequestIntegrationBody from a JSON string
v2_integration_integration_id_put_request_integration_body_instance = V2IntegrationIntegrationIdPutRequestIntegrationBody.from_json(json)
# print the JSON string representation of the object
print(V2IntegrationIntegrationIdPutRequestIntegrationBody.to_json())

# convert the object into a dict
v2_integration_integration_id_put_request_integration_body_dict = v2_integration_integration_id_put_request_integration_body_instance.to_dict()
# create an instance of V2IntegrationIntegrationIdPutRequestIntegrationBody from a dict
v2_integration_integration_id_put_request_integration_body_from_dict = V2IntegrationIntegrationIdPutRequestIntegrationBody.from_dict(v2_integration_integration_id_put_request_integration_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


