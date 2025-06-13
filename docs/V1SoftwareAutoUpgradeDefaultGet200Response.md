# V1SoftwareAutoUpgradeDefaultGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**V1SoftwareAutoUpgradeDefaultGet200ResponseDetails**](V1SoftwareAutoUpgradeDefaultGet200ResponseDetails.md) |  | [optional] 
**release** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_software_auto_upgrade_default_get200_response import V1SoftwareAutoUpgradeDefaultGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1SoftwareAutoUpgradeDefaultGet200Response from a JSON string
v1_software_auto_upgrade_default_get200_response_instance = V1SoftwareAutoUpgradeDefaultGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1SoftwareAutoUpgradeDefaultGet200Response.to_json())

# convert the object into a dict
v1_software_auto_upgrade_default_get200_response_dict = v1_software_auto_upgrade_default_get200_response_instance.to_dict()
# create an instance of V1SoftwareAutoUpgradeDefaultGet200Response from a dict
v1_software_auto_upgrade_default_get200_response_from_dict = V1SoftwareAutoUpgradeDefaultGet200Response.from_dict(v1_software_auto_upgrade_default_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


