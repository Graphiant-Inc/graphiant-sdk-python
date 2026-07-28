# ManaV2ExtranetServiceConsumerPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_lan_segments** | [**Dict[str, ManaV2ExtranetConsumerLanPrefixes]**](ManaV2ExtranetConsumerLanPrefixes.md) |  | 
**global_object_ops** | [**Dict[str, ManaV2GlobalObjectServiceOps]**](ManaV2GlobalObjectServiceOps.md) |  | [optional] 
**nat_translation_mode** | [**ManaV2ExtranetNatTranslationMode**](ManaV2ExtranetNatTranslationMode.md) |  | [optional] 
**site_to_site_vpn** | [**ManaV2GuestConsumerSiteToSiteVpnConfig**](ManaV2GuestConsumerSiteToSiteVpnConfig.md) |  | [optional] 
**sites** | [**List[ManaV2B2bSiteInformation]**](ManaV2B2bSiteInformation.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_service_consumer_policy import ManaV2ExtranetServiceConsumerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetServiceConsumerPolicy from a JSON string
mana_v2_extranet_service_consumer_policy_instance = ManaV2ExtranetServiceConsumerPolicy.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetServiceConsumerPolicy.to_json())

# convert the object into a dict
mana_v2_extranet_service_consumer_policy_dict = mana_v2_extranet_service_consumer_policy_instance.to_dict()
# create an instance of ManaV2ExtranetServiceConsumerPolicy from a dict
mana_v2_extranet_service_consumer_policy_from_dict = ManaV2ExtranetServiceConsumerPolicy.from_dict(mana_v2_extranet_service_consumer_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


