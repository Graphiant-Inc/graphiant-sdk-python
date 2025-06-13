# V2IntegrationPost200ResponseIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**details** | [**V2IntegrationPostRequestIntegrationBodyDetails**](V2IntegrationPostRequestIntegrationBodyDetails.md) |  | [optional] 
**enterprise_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_integration_post200_response_integration import V2IntegrationPost200ResponseIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of V2IntegrationPost200ResponseIntegration from a JSON string
v2_integration_post200_response_integration_instance = V2IntegrationPost200ResponseIntegration.from_json(json)
# print the JSON string representation of the object
print(V2IntegrationPost200ResponseIntegration.to_json())

# convert the object into a dict
v2_integration_post200_response_integration_dict = v2_integration_post200_response_integration_instance.to_dict()
# create an instance of V2IntegrationPost200ResponseIntegration from a dict
v2_integration_post200_response_integration_from_dict = V2IntegrationPost200ResponseIntegration.from_dict(v2_integration_post200_response_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


