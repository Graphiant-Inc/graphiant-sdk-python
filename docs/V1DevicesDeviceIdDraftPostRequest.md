# V1DevicesDeviceIdDraftPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_version** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**draft** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInner**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_draft_post_request import V1DevicesDeviceIdDraftPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdDraftPostRequest from a JSON string
v1_devices_device_id_draft_post_request_instance = V1DevicesDeviceIdDraftPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdDraftPostRequest.to_json())

# convert the object into a dict
v1_devices_device_id_draft_post_request_dict = v1_devices_device_id_draft_post_request_instance.to_dict()
# create an instance of V1DevicesDeviceIdDraftPostRequest from a dict
v1_devices_device_id_draft_post_request_from_dict = V1DevicesDeviceIdDraftPostRequest.from_dict(v1_devices_device_id_draft_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


