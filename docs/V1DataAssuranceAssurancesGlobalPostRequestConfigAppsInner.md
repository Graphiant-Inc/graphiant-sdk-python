# V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **int** |  | [optional] 
**builtin_app_id** | **int** |  | [optional] 
**custom_app_id** | **int** |  | [optional] 
**is_domain** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**servers** | [**List[V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInnerServersInner]**](V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInnerServersInner.md) |  | [optional] 
**use_all_servers** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_data_assurance_assurances_global_post_request_config_apps_inner import V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner from a JSON string
v1_data_assurance_assurances_global_post_request_config_apps_inner_instance = V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner.from_json(json)
# print the JSON string representation of the object
print(V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner.to_json())

# convert the object into a dict
v1_data_assurance_assurances_global_post_request_config_apps_inner_dict = v1_data_assurance_assurances_global_post_request_config_apps_inner_instance.to_dict()
# create an instance of V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner from a dict
v1_data_assurance_assurances_global_post_request_config_apps_inner_from_dict = V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner.from_dict(v1_data_assurance_assurances_global_post_request_config_apps_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


