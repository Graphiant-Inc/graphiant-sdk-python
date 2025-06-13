# V1VersionPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_metadata** | [**V1VersionPostRequestConfigurationMetadata**](V1VersionPostRequestConfigurationMetadata.md) |  | [optional] 
**device_id** | **int** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_version_post_request import V1VersionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1VersionPostRequest from a JSON string
v1_version_post_request_instance = V1VersionPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1VersionPostRequest.to_json())

# convert the object into a dict
v1_version_post_request_dict = v1_version_post_request_instance.to_dict()
# create an instance of V1VersionPostRequest from a dict
v1_version_post_request_from_dict = V1VersionPostRequest.from_dict(v1_version_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


