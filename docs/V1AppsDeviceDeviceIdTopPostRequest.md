# V1AppsDeviceDeviceIdTopPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_apps** | **int** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_apps_device_device_id_top_post_request import V1AppsDeviceDeviceIdTopPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppsDeviceDeviceIdTopPostRequest from a JSON string
v1_apps_device_device_id_top_post_request_instance = V1AppsDeviceDeviceIdTopPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AppsDeviceDeviceIdTopPostRequest.to_json())

# convert the object into a dict
v1_apps_device_device_id_top_post_request_dict = v1_apps_device_device_id_top_post_request_instance.to_dict()
# create an instance of V1AppsDeviceDeviceIdTopPostRequest from a dict
v1_apps_device_device_id_top_post_request_from_dict = V1AppsDeviceDeviceIdTopPostRequest.from_dict(v1_apps_device_device_id_top_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


