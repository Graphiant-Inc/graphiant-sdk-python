# V1DataAssuranceAssurancesGlobalPostRequestConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner]**](V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner.md) |  | [optional] 
**flex_algo** | **str** |  | [optional] 
**lan_names** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**site_list_id** | **int** |  | [optional] 
**use_all_sites** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_data_assurance_assurances_global_post_request_config import V1DataAssuranceAssurancesGlobalPostRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of V1DataAssuranceAssurancesGlobalPostRequestConfig from a JSON string
v1_data_assurance_assurances_global_post_request_config_instance = V1DataAssuranceAssurancesGlobalPostRequestConfig.from_json(json)
# print the JSON string representation of the object
print(V1DataAssuranceAssurancesGlobalPostRequestConfig.to_json())

# convert the object into a dict
v1_data_assurance_assurances_global_post_request_config_dict = v1_data_assurance_assurances_global_post_request_config_instance.to_dict()
# create an instance of V1DataAssuranceAssurancesGlobalPostRequestConfig from a dict
v1_data_assurance_assurances_global_post_request_config_from_dict = V1DataAssuranceAssurancesGlobalPostRequestConfig.from_dict(v1_data_assurance_assurances_global_post_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


