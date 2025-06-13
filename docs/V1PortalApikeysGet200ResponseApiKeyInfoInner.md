# V1PortalApikeysGet200ResponseApiKeyInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**gcs_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_portal_apikeys_get200_response_api_key_info_inner import V1PortalApikeysGet200ResponseApiKeyInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1PortalApikeysGet200ResponseApiKeyInfoInner from a JSON string
v1_portal_apikeys_get200_response_api_key_info_inner_instance = V1PortalApikeysGet200ResponseApiKeyInfoInner.from_json(json)
# print the JSON string representation of the object
print(V1PortalApikeysGet200ResponseApiKeyInfoInner.to_json())

# convert the object into a dict
v1_portal_apikeys_get200_response_api_key_info_inner_dict = v1_portal_apikeys_get200_response_api_key_info_inner_instance.to_dict()
# create an instance of V1PortalApikeysGet200ResponseApiKeyInfoInner from a dict
v1_portal_apikeys_get200_response_api_key_info_inner_from_dict = V1PortalApikeysGet200ResponseApiKeyInfoInner.from_dict(v1_portal_apikeys_get200_response_api_key_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


