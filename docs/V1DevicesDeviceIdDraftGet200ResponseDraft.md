# V1DevicesDeviceIdDraftGet200ResponseDraft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mana_device** | [**V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInner**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInner.md) |  | [optional] 
**version_info** | [**V1DevicesDeviceIdDraftGet200ResponseDraftVersionInfo**](V1DevicesDeviceIdDraftGet200ResponseDraftVersionInfo.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_draft_get200_response_draft import V1DevicesDeviceIdDraftGet200ResponseDraft

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdDraftGet200ResponseDraft from a JSON string
v1_devices_device_id_draft_get200_response_draft_instance = V1DevicesDeviceIdDraftGet200ResponseDraft.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdDraftGet200ResponseDraft.to_json())

# convert the object into a dict
v1_devices_device_id_draft_get200_response_draft_dict = v1_devices_device_id_draft_get200_response_draft_instance.to_dict()
# create an instance of V1DevicesDeviceIdDraftGet200ResponseDraft from a dict
v1_devices_device_id_draft_get200_response_draft_from_dict = V1DevicesDeviceIdDraftGet200ResponseDraft.from_dict(v1_devices_device_id_draft_get200_response_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


