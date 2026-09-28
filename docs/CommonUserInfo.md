# CommonUserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearer_token** | **str** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**exp** | **int** |  | [optional] 
**original_enterprise_id** | **int** |  | [optional] 
**permissions** | [**CommonPermissions**](CommonPermissions.md) |  | [optional] 
**time_zone** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.common_user_info import CommonUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommonUserInfo from a JSON string
common_user_info_instance = CommonUserInfo.from_json(json)
# print the JSON string representation of the object
print(CommonUserInfo.to_json())

# convert the object into a dict
common_user_info_dict = common_user_info_instance.to_dict()
# create an instance of CommonUserInfo from a dict
common_user_info_from_dict = CommonUserInfo.from_dict(common_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


