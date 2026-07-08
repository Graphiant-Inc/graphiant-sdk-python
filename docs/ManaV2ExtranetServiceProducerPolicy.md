# ManaV2ExtranetServiceProducerPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**global_object_device_summaries** | [**Dict[str, ManaV2GlobalObjectServiceSummaries]**](ManaV2GlobalObjectServiceSummaries.md) |  | [optional] 
**global_object_ops** | [**Dict[str, ManaV2GlobalObjectServiceOps]**](ManaV2GlobalObjectServiceOps.md) |  | [optional] 
**nat_translation_mode** | [**ManaV2ExtranetNatTranslationMode**](ManaV2ExtranetNatTranslationMode.md) |  | [optional] 
**prefix_tags** | [**List[ManaV2B2bExtranetPrefixTag]**](ManaV2B2bExtranetPrefixTag.md) |  | [optional] 
**service_lan_segment** | **int** | LAN segment ID for the service | [optional] 
**sites** | [**List[ManaV2B2bSiteInformation]**](ManaV2B2bSiteInformation.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_service_producer_policy import ManaV2ExtranetServiceProducerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetServiceProducerPolicy from a JSON string
mana_v2_extranet_service_producer_policy_instance = ManaV2ExtranetServiceProducerPolicy.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetServiceProducerPolicy.to_json())

# convert the object into a dict
mana_v2_extranet_service_producer_policy_dict = mana_v2_extranet_service_producer_policy_instance.to_dict()
# create an instance of ManaV2ExtranetServiceProducerPolicy from a dict
mana_v2_extranet_service_producer_policy_from_dict = ManaV2ExtranetServiceProducerPolicy.from_dict(mana_v2_extranet_service_producer_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


