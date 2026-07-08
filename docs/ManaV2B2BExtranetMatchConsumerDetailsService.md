# ManaV2B2BExtranetMatchConsumerDetailsService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | [optional] 
**contact_email** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**service_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_b2_b_extranet_match_consumer_details_service import ManaV2B2BExtranetMatchConsumerDetailsService

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2B2BExtranetMatchConsumerDetailsService from a JSON string
mana_v2_b2_b_extranet_match_consumer_details_service_instance = ManaV2B2BExtranetMatchConsumerDetailsService.from_json(json)
# print the JSON string representation of the object
print(ManaV2B2BExtranetMatchConsumerDetailsService.to_json())

# convert the object into a dict
mana_v2_b2_b_extranet_match_consumer_details_service_dict = mana_v2_b2_b_extranet_match_consumer_details_service_instance.to_dict()
# create an instance of ManaV2B2BExtranetMatchConsumerDetailsService from a dict
mana_v2_b2_b_extranet_match_consumer_details_service_from_dict = ManaV2B2BExtranetMatchConsumerDetailsService.from_dict(mana_v2_b2_b_extranet_match_consumer_details_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


