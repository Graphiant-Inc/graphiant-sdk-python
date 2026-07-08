# ManaV2ExtranetConsumerLanPrefixes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_prefixes** | **List[str]** |  | [optional] 
**service_prefix_dnat** | **Dict[str, str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_consumer_lan_prefixes import ManaV2ExtranetConsumerLanPrefixes

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetConsumerLanPrefixes from a JSON string
mana_v2_extranet_consumer_lan_prefixes_instance = ManaV2ExtranetConsumerLanPrefixes.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetConsumerLanPrefixes.to_json())

# convert the object into a dict
mana_v2_extranet_consumer_lan_prefixes_dict = mana_v2_extranet_consumer_lan_prefixes_instance.to_dict()
# create an instance of ManaV2ExtranetConsumerLanPrefixes from a dict
mana_v2_extranet_consumer_lan_prefixes_from_dict = ManaV2ExtranetConsumerLanPrefixes.from_dict(mana_v2_extranet_consumer_lan_prefixes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


