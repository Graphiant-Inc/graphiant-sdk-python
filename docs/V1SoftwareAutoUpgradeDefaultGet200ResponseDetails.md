# V1SoftwareAutoUpgradeDefaultGet200ResponseDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**day_of_week** | **str** |  | [optional] 
**hour** | **int** |  | [optional] 
**minute** | **int** |  | [optional] 
**occurrence_in_month** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_software_auto_upgrade_default_get200_response_details import V1SoftwareAutoUpgradeDefaultGet200ResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of V1SoftwareAutoUpgradeDefaultGet200ResponseDetails from a JSON string
v1_software_auto_upgrade_default_get200_response_details_instance = V1SoftwareAutoUpgradeDefaultGet200ResponseDetails.from_json(json)
# print the JSON string representation of the object
print(V1SoftwareAutoUpgradeDefaultGet200ResponseDetails.to_json())

# convert the object into a dict
v1_software_auto_upgrade_default_get200_response_details_dict = v1_software_auto_upgrade_default_get200_response_details_instance.to_dict()
# create an instance of V1SoftwareAutoUpgradeDefaultGet200ResponseDetails from a dict
v1_software_auto_upgrade_default_get200_response_details_from_dict = V1SoftwareAutoUpgradeDefaultGet200ResponseDetails.from_dict(v1_software_auto_upgrade_default_get200_response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


