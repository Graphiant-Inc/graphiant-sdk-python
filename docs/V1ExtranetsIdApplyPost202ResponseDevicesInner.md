# V1ExtranetsIdApplyPost202ResponseDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**device_name** | **str** |  | [optional] 
**site_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_id_apply_post202_response_devices_inner import V1ExtranetsIdApplyPost202ResponseDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsIdApplyPost202ResponseDevicesInner from a JSON string
v1_extranets_id_apply_post202_response_devices_inner_instance = V1ExtranetsIdApplyPost202ResponseDevicesInner.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsIdApplyPost202ResponseDevicesInner.to_json())

# convert the object into a dict
v1_extranets_id_apply_post202_response_devices_inner_dict = v1_extranets_id_apply_post202_response_devices_inner_instance.to_dict()
# create an instance of V1ExtranetsIdApplyPost202ResponseDevicesInner from a dict
v1_extranets_id_apply_post202_response_devices_inner_from_dict = V1ExtranetsIdApplyPost202ResponseDevicesInner.from_dict(v1_extranets_id_apply_post202_response_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


