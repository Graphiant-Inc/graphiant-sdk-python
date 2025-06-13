# V1DevicesOauthRedirectGet200ResponseOnboardingRedirection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_onboarding_gw_addr** | **str** |  | [optional] 
**private_portal_url** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**root_ca** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_oauth_redirect_get200_response_onboarding_redirection import V1DevicesOauthRedirectGet200ResponseOnboardingRedirection

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesOauthRedirectGet200ResponseOnboardingRedirection from a JSON string
v1_devices_oauth_redirect_get200_response_onboarding_redirection_instance = V1DevicesOauthRedirectGet200ResponseOnboardingRedirection.from_json(json)
# print the JSON string representation of the object
print(V1DevicesOauthRedirectGet200ResponseOnboardingRedirection.to_json())

# convert the object into a dict
v1_devices_oauth_redirect_get200_response_onboarding_redirection_dict = v1_devices_oauth_redirect_get200_response_onboarding_redirection_instance.to_dict()
# create an instance of V1DevicesOauthRedirectGet200ResponseOnboardingRedirection from a dict
v1_devices_oauth_redirect_get200_response_onboarding_redirection_from_dict = V1DevicesOauthRedirectGet200ResponseOnboardingRedirection.from_dict(v1_devices_oauth_redirect_get200_response_onboarding_redirection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


