# ManaV2ExtranetServiceCustomerInvite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_emails** | **List[str]** |  | [optional] 
**maximum_number_of_sites** | **int** | Maximum number of consumer sites | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_extranet_service_customer_invite import ManaV2ExtranetServiceCustomerInvite

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ExtranetServiceCustomerInvite from a JSON string
mana_v2_extranet_service_customer_invite_instance = ManaV2ExtranetServiceCustomerInvite.from_json(json)
# print the JSON string representation of the object
print(ManaV2ExtranetServiceCustomerInvite.to_json())

# convert the object into a dict
mana_v2_extranet_service_customer_invite_dict = mana_v2_extranet_service_customer_invite_instance.to_dict()
# create an instance of ManaV2ExtranetServiceCustomerInvite from a dict
mana_v2_extranet_service_customer_invite_from_dict = ManaV2ExtranetServiceCustomerInvite.from_dict(mana_v2_extranet_service_customer_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


