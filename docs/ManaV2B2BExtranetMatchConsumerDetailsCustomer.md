# ManaV2B2BExtranetMatchConsumerDetailsCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_emails** | **List[str]** |  | [optional] 
**company_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**num_sites** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_b2_b_extranet_match_consumer_details_customer import ManaV2B2BExtranetMatchConsumerDetailsCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2B2BExtranetMatchConsumerDetailsCustomer from a JSON string
mana_v2_b2_b_extranet_match_consumer_details_customer_instance = ManaV2B2BExtranetMatchConsumerDetailsCustomer.from_json(json)
# print the JSON string representation of the object
print(ManaV2B2BExtranetMatchConsumerDetailsCustomer.to_json())

# convert the object into a dict
mana_v2_b2_b_extranet_match_consumer_details_customer_dict = mana_v2_b2_b_extranet_match_consumer_details_customer_instance.to_dict()
# create an instance of ManaV2B2BExtranetMatchConsumerDetailsCustomer from a dict
mana_v2_b2_b_extranet_match_consumer_details_customer_from_dict = ManaV2B2BExtranetMatchConsumerDetailsCustomer.from_dict(mana_v2_b2_b_extranet_match_consumer_details_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


