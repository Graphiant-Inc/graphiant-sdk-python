# V1DevicesSessionStatusPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_session_data_map** | [**Dict[str, V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue]**](V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue.md) |  | [optional] 
**bgp_session_map** | [**Dict[str, V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue]**](V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue.md) |  | [optional] 
**bgp_session_states** | [**List[V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue]**](V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_session_status_post200_response import V1DevicesSessionStatusPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesSessionStatusPost200Response from a JSON string
v1_devices_session_status_post200_response_instance = V1DevicesSessionStatusPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1DevicesSessionStatusPost200Response.to_json())

# convert the object into a dict
v1_devices_session_status_post200_response_dict = v1_devices_session_status_post200_response_instance.to_dict()
# create an instance of V1DevicesSessionStatusPost200Response from a dict
v1_devices_session_status_post200_response_from_dict = V1DevicesSessionStatusPost200Response.from_dict(v1_devices_session_status_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


