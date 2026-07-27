# ManaV2ExtranetServiceCustomerSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_emails** | **List[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**matched_services** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_service_customer_summary import ManaV2ExtranetServiceCustomerSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetServiceCustomerSummary from a JSON string
mana_v2_extranet_service_customer_summary_instance = ManaV2ExtranetServiceCustomerSummary.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetServiceCustomerSummary.to_json())

# convert the object into a dict
mana_v2_extranet_service_customer_summary_dict = mana_v2_extranet_service_customer_summary_instance.to_dict()
# create an instance of ManaV2ExtranetServiceCustomerSummary from a dict
mana_v2_extranet_service_customer_summary_from_dict = ManaV2ExtranetServiceCustomerSummary.from_dict(mana_v2_extranet_service_customer_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


