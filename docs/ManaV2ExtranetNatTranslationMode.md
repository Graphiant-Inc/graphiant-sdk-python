# ManaV2ExtranetNatTranslationMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**centralized** | [**ManaV2ExtranetNatTranslationCentralized**](ManaV2ExtranetNatTranslationCentralized.md) |  | [optional] 
**decentralized** | [**ManaV2ExtranetNatTranslationDecentralized**](ManaV2ExtranetNatTranslationDecentralized.md) |  | [optional] 
**peer_to_peer** | [**ManaV2ExtranetNatTranslationPeerToPeer**](ManaV2ExtranetNatTranslationPeerToPeer.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_nat_translation_mode import ManaV2ExtranetNatTranslationMode

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetNatTranslationMode from a JSON string
mana_v2_extranet_nat_translation_mode_instance = ManaV2ExtranetNatTranslationMode.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetNatTranslationMode.to_json())

# convert the object into a dict
mana_v2_extranet_nat_translation_mode_dict = mana_v2_extranet_nat_translation_mode_instance.to_dict()
# create an instance of ManaV2ExtranetNatTranslationMode from a dict
mana_v2_extranet_nat_translation_mode_from_dict = ManaV2ExtranetNatTranslationMode.from_dict(mana_v2_extranet_nat_translation_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


