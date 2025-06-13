# V1GlobalIpsecProfileGet200ResponseIpsecProfilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**ipsec_profile_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_ipsec_profile_get200_response_ipsec_profiles_inner import V1GlobalIpsecProfileGet200ResponseIpsecProfilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalIpsecProfileGet200ResponseIpsecProfilesInner from a JSON string
v1_global_ipsec_profile_get200_response_ipsec_profiles_inner_instance = V1GlobalIpsecProfileGet200ResponseIpsecProfilesInner.from_json(json)
# print the JSON string representation of the object
print(V1GlobalIpsecProfileGet200ResponseIpsecProfilesInner.to_json())

# convert the object into a dict
v1_global_ipsec_profile_get200_response_ipsec_profiles_inner_dict = v1_global_ipsec_profile_get200_response_ipsec_profiles_inner_instance.to_dict()
# create an instance of V1GlobalIpsecProfileGet200ResponseIpsecProfilesInner from a dict
v1_global_ipsec_profile_get200_response_ipsec_profiles_inner_from_dict = V1GlobalIpsecProfileGet200ResponseIpsecProfilesInner.from_dict(v1_global_ipsec_profile_get200_response_ipsec_profiles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


