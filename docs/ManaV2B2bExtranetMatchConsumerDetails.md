# ManaV2B2bExtranetMatchConsumerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_id** | **int** |  | [optional] 
**consumer_prefixes** | **List[str]** |  | [optional] 
**customer** | [**ManaV2B2BExtranetMatchConsumerDetailsCustomer**](ManaV2B2BExtranetMatchConsumerDetailsCustomer.md) |  | [optional] 
**old_consumer_prefixes** | **List[str]** |  | [optional] 
**old_service_prefixes** | [**List[ManaV2B2BExtranetMatchConsumerDetailsProducerPrefix]**](ManaV2B2BExtranetMatchConsumerDetailsProducerPrefix.md) |  | [optional] 
**service** | [**ManaV2B2BExtranetMatchConsumerDetailsService**](ManaV2B2BExtranetMatchConsumerDetailsService.md) |  | [optional] 
**service_prefixes** | [**List[ManaV2B2BExtranetMatchConsumerDetailsProducerPrefix]**](ManaV2B2BExtranetMatchConsumerDetailsProducerPrefix.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_b2b_extranet_match_consumer_details import ManaV2B2bExtranetMatchConsumerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2B2bExtranetMatchConsumerDetails from a JSON string
mana_v2_b2b_extranet_match_consumer_details_instance = ManaV2B2bExtranetMatchConsumerDetails.from_json(json)
# print the JSON string representation of the object
print(ManaV2B2bExtranetMatchConsumerDetails.to_json())

# convert the object into a dict
mana_v2_b2b_extranet_match_consumer_details_dict = mana_v2_b2b_extranet_match_consumer_details_instance.to_dict()
# create an instance of ManaV2B2bExtranetMatchConsumerDetails from a dict
mana_v2_b2b_extranet_match_consumer_details_from_dict = ManaV2B2bExtranetMatchConsumerDetails.from_dict(mana_v2_b2b_extranet_match_consumer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


