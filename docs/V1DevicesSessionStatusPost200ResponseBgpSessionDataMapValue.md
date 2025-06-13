# V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_bgp_neighbors_count** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**odp_bgp_neighbors_count** | **int** |  | [optional] 
**wan_interfaces_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_session_status_post200_response_bgp_session_data_map_value import V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue from a JSON string
v1_devices_session_status_post200_response_bgp_session_data_map_value_instance = V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue.from_json(json)
# print the JSON string representation of the object
print(V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue.to_json())

# convert the object into a dict
v1_devices_session_status_post200_response_bgp_session_data_map_value_dict = v1_devices_session_status_post200_response_bgp_session_data_map_value_instance.to_dict()
# create an instance of V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue from a dict
v1_devices_session_status_post200_response_bgp_session_data_map_value_from_dict = V1DevicesSessionStatusPost200ResponseBgpSessionDataMapValue.from_dict(v1_devices_session_status_post200_response_bgp_session_data_map_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


