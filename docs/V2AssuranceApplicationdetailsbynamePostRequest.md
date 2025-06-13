# V2AssuranceApplicationdetailsbynamePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id_key** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**bucket_id** | **str** |  | [optional] 
**flex_algo_id** | **int** |  | [optional] 
**time_window** | [**V2NotificationlistPostRequestTimeWindow**](V2NotificationlistPostRequestTimeWindow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_applicationdetailsbyname_post_request import V2AssuranceApplicationdetailsbynamePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceApplicationdetailsbynamePostRequest from a JSON string
v2_assurance_applicationdetailsbyname_post_request_instance = V2AssuranceApplicationdetailsbynamePostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceApplicationdetailsbynamePostRequest.to_json())

# convert the object into a dict
v2_assurance_applicationdetailsbyname_post_request_dict = v2_assurance_applicationdetailsbyname_post_request_instance.to_dict()
# create an instance of V2AssuranceApplicationdetailsbynamePostRequest from a dict
v2_assurance_applicationdetailsbyname_post_request_from_dict = V2AssuranceApplicationdetailsbynamePostRequest.from_dict(v2_assurance_applicationdetailsbyname_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


