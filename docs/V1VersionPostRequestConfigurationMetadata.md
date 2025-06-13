# V1VersionPostRequestConfigurationMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_confirm** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_version_post_request_configuration_metadata import V1VersionPostRequestConfigurationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of V1VersionPostRequestConfigurationMetadata from a JSON string
v1_version_post_request_configuration_metadata_instance = V1VersionPostRequestConfigurationMetadata.from_json(json)
# print the JSON string representation of the object
print(V1VersionPostRequestConfigurationMetadata.to_json())

# convert the object into a dict
v1_version_post_request_configuration_metadata_dict = v1_version_post_request_configuration_metadata_instance.to_dict()
# create an instance of V1VersionPostRequestConfigurationMetadata from a dict
v1_version_post_request_configuration_metadata_from_dict = V1VersionPostRequestConfigurationMetadata.from_dict(v1_version_post_request_configuration_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


