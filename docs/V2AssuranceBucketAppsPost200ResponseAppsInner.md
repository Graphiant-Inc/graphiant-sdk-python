# V2AssuranceBucketAppsPost200ResponseAppsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**builtin_app_id** | **int** |  | [optional] 
**custom_app_id** | **int** |  | [optional] 
**flex_algo** | [**V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecordFlexAlgoInner**](V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecordFlexAlgoInner.md) |  | [optional] 
**is_domain** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_bucket_apps_post200_response_apps_inner import V2AssuranceBucketAppsPost200ResponseAppsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceBucketAppsPost200ResponseAppsInner from a JSON string
v2_assurance_bucket_apps_post200_response_apps_inner_instance = V2AssuranceBucketAppsPost200ResponseAppsInner.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceBucketAppsPost200ResponseAppsInner.to_json())

# convert the object into a dict
v2_assurance_bucket_apps_post200_response_apps_inner_dict = v2_assurance_bucket_apps_post200_response_apps_inner_instance.to_dict()
# create an instance of V2AssuranceBucketAppsPost200ResponseAppsInner from a dict
v2_assurance_bucket_apps_post200_response_apps_inner_from_dict = V2AssuranceBucketAppsPost200ResponseAppsInner.from_dict(v2_assurance_bucket_apps_post200_response_apps_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


