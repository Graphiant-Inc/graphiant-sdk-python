# V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_policy** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCallPolicy**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCallPolicy.md) |  | [optional] 
**import_policy** | [**V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCallPolicy**](V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCallPolicy.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_overlay_filters import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters from a JSON string
v1_devices_device_id_config_put_request_core_core_vrf_overlay_filters_instance = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_core_core_vrf_overlay_filters_dict = v1_devices_device_id_config_put_request_core_core_vrf_overlay_filters_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters from a dict
v1_devices_device_id_config_put_request_core_core_vrf_overlay_filters_from_dict = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfOverlayFilters.from_dict(v1_devices_device_id_config_put_request_core_core_vrf_overlay_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


