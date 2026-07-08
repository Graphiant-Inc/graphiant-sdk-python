# ManaV2ExtranetNatTranslationPeerToPeerPrefix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outside_nat_prefix** | **str** | Optional outside address presented for prefix on the far side of the attachment; omit for no NAT on that prefix | [optional] 
**prefix** | **str** | At match: customer export prefix. At consumer accept/update (peering): subscribed service prefix | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_nat_translation_peer_to_peer_prefix import ManaV2ExtranetNatTranslationPeerToPeerPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetNatTranslationPeerToPeerPrefix from a JSON string
mana_v2_extranet_nat_translation_peer_to_peer_prefix_instance = ManaV2ExtranetNatTranslationPeerToPeerPrefix.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetNatTranslationPeerToPeerPrefix.to_json())

# convert the object into a dict
mana_v2_extranet_nat_translation_peer_to_peer_prefix_dict = mana_v2_extranet_nat_translation_peer_to_peer_prefix_instance.to_dict()
# create an instance of ManaV2ExtranetNatTranslationPeerToPeerPrefix from a dict
mana_v2_extranet_nat_translation_peer_to_peer_prefix_from_dict = ManaV2ExtranetNatTranslationPeerToPeerPrefix.from_dict(mana_v2_extranet_nat_translation_peer_to_peer_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


