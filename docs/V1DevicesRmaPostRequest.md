# V1DevicesRmaPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_device_id** | **int** |  | [optional] 
**new_device_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_rma_post_request import V1DevicesRmaPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesRmaPostRequest from a JSON string
v1_devices_rma_post_request_instance = V1DevicesRmaPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1DevicesRmaPostRequest.to_json())

# convert the object into a dict
v1_devices_rma_post_request_dict = v1_devices_rma_post_request_instance.to_dict()
# create an instance of V1DevicesRmaPostRequest from a dict
v1_devices_rma_post_request_from_dict = V1DevicesRmaPostRequest.from_dict(v1_devices_rma_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


