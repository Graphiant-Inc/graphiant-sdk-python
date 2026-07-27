# ManaV2B2bExtranetMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_prefixes** | **List[str]** |  | [optional] 
**lan_segment** | **int** |  | [optional] 
**nat_translation_mode** | [**ManaV2ExtranetNatTranslationMode**](ManaV2ExtranetNatTranslationMode.md) |  | [optional] 
**num_customers** | **int** | Number of customers subscribed to the service | [optional] 
**service_id** | **int** | Producer service id | [optional] 
**service_prefixes** | [**List[ManaV2B2bExtranetPrefixTag]**](ManaV2B2bExtranetPrefixTag.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_b2b_extranet_match import ManaV2B2bExtranetMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2B2bExtranetMatch from a JSON string
mana_v2_b2b_extranet_match_instance = ManaV2B2bExtranetMatch.from_json(json)
# print the JSON string representation of the object
print(ManaV2B2bExtranetMatch.to_json())

# convert the object into a dict
mana_v2_b2b_extranet_match_dict = mana_v2_b2b_extranet_match_instance.to_dict()
# create an instance of ManaV2B2bExtranetMatch from a dict
mana_v2_b2b_extranet_match_from_dict = ManaV2B2bExtranetMatch.from_dict(mana_v2_b2b_extranet_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


