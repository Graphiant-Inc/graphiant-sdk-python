# UpgradeInventoryKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | Blob storage container this image was indexed from. Same model + version can exist in more than one container Empty for rows indexed before multi-container support. | [optional] 
**model** | **int** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.upgrade_inventory_key import UpgradeInventoryKey

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeInventoryKey from a JSON string
upgrade_inventory_key_instance = UpgradeInventoryKey.from_json(json)
# print the JSON string representation of the object
print(UpgradeInventoryKey.to_json())

# convert the object into a dict
upgrade_inventory_key_dict = upgrade_inventory_key_instance.to_dict()
# create an instance of UpgradeInventoryKey from a dict
upgrade_inventory_key_from_dict = UpgradeInventoryKey.from_dict(upgrade_inventory_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


