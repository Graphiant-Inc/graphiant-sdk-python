# ManaV2ExtranetServiceProducerCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_emails** | **List[str]** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**match_id** | **int** |  | [optional] 
**matched_services** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_service_producer_customer import ManaV2ExtranetServiceProducerCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetServiceProducerCustomer from a JSON string
mana_v2_extranet_service_producer_customer_instance = ManaV2ExtranetServiceProducerCustomer.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetServiceProducerCustomer.to_json())

# convert the object into a dict
mana_v2_extranet_service_producer_customer_dict = mana_v2_extranet_service_producer_customer_instance.to_dict()
# create an instance of ManaV2ExtranetServiceProducerCustomer from a dict
mana_v2_extranet_service_producer_customer_from_dict = ManaV2ExtranetServiceProducerCustomer.from_dict(mana_v2_extranet_service_producer_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


