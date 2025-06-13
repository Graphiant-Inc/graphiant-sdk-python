# V1TroubleshootingEnterprisePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**V1TroubleshootingEnterprisePostRequestDimensions**](V1TroubleshootingEnterprisePostRequestDimensions.md) |  | [optional] 
**filter** | [**V1BackboneHealthOverviewPostRequestFilter**](V1BackboneHealthOverviewPostRequestFilter.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_troubleshooting_enterprise_post_request import V1TroubleshootingEnterprisePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1TroubleshootingEnterprisePostRequest from a JSON string
v1_troubleshooting_enterprise_post_request_instance = V1TroubleshootingEnterprisePostRequest.from_json(json)
# print the JSON string representation of the object
print(V1TroubleshootingEnterprisePostRequest.to_json())

# convert the object into a dict
v1_troubleshooting_enterprise_post_request_dict = v1_troubleshooting_enterprise_post_request_instance.to_dict()
# create an instance of V1TroubleshootingEnterprisePostRequest from a dict
v1_troubleshooting_enterprise_post_request_from_dict = V1TroubleshootingEnterprisePostRequest.from_dict(v1_troubleshooting_enterprise_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


