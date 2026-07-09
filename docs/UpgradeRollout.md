# UpgradeRollout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[UpgradeRolloutDevice]**](UpgradeRolloutDevice.md) |  | [optional] 
**has_failed** | **bool** | True if any device in the rollout has a failed upgrade state. | [optional] 
**id** | **int** | Server-assigned rollout identifier. | [optional] 
**last_run_ts** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**next_run_ts** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**num_devices** | **int** | Count of devices associated with the rollout. | [optional] 
**rollout_config** | [**UpgradeRolloutConfig**](UpgradeRolloutConfig.md) |  | [optional] 
**status** | **str** | Status of the upgrade rollout group | [optional] 

## Example

```python
from graphiant_sdk.models.upgrade_rollout import UpgradeRollout

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeRollout from a JSON string
upgrade_rollout_instance = UpgradeRollout.from_json(json)
# print the JSON string representation of the object
print(UpgradeRollout.to_json())

# convert the object into a dict
upgrade_rollout_dict = upgrade_rollout_instance.to_dict()
# create an instance of UpgradeRollout from a dict
upgrade_rollout_from_dict = UpgradeRollout.from_dict(upgrade_rollout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


