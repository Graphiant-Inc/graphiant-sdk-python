# V1DevicesDeviceIdConfigPutRequestEdgeNatPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nat_rulesets** | [**Dict[str, V1DevicesDeviceIdConfigPutRequestEdgeNatPolicyNatRulesetsValue]**](V1DevicesDeviceIdConfigPutRequestEdgeNatPolicyNatRulesetsValue.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_nat_policy import V1DevicesDeviceIdConfigPutRequestEdgeNatPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeNatPolicy from a JSON string
v1_devices_device_id_config_put_request_edge_nat_policy_instance = V1DevicesDeviceIdConfigPutRequestEdgeNatPolicy.from_json(json)
# print the JSON string representation of the object
print(V1DevicesDeviceIdConfigPutRequestEdgeNatPolicy.to_json())

# convert the object into a dict
v1_devices_device_id_config_put_request_edge_nat_policy_dict = v1_devices_device_id_config_put_request_edge_nat_policy_instance.to_dict()
# create an instance of V1DevicesDeviceIdConfigPutRequestEdgeNatPolicy from a dict
v1_devices_device_id_config_put_request_edge_nat_policy_from_dict = V1DevicesDeviceIdConfigPutRequestEdgeNatPolicy.from_dict(v1_devices_device_id_config_put_request_edge_nat_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


