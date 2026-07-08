# ManaV2ExtranetServiceCustomerMatchSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**lan_segment** | **int** |  | [optional] 
**matched_customers** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_service_customer_match_summary import ManaV2ExtranetServiceCustomerMatchSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetServiceCustomerMatchSummary from a JSON string
mana_v2_extranet_service_customer_match_summary_instance = ManaV2ExtranetServiceCustomerMatchSummary.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetServiceCustomerMatchSummary.to_json())

# convert the object into a dict
mana_v2_extranet_service_customer_match_summary_dict = mana_v2_extranet_service_customer_match_summary_instance.to_dict()
# create an instance of ManaV2ExtranetServiceCustomerMatchSummary from a dict
mana_v2_extranet_service_customer_match_summary_from_dict = ManaV2ExtranetServiceCustomerMatchSummary.from_dict(mana_v2_extranet_service_customer_match_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


