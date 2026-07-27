# ManaV2OspfAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Shared secret for OSPFv2 MD5 authentication on this interface | [optional] 
**key_id** | **int** | Identifier of the OSPFv2 MD5 authentication key configured on this interface | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_ospf_authentication import ManaV2OspfAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2OspfAuthentication from a JSON string
mana_v2_ospf_authentication_instance = ManaV2OspfAuthentication.from_json(json)
# print the JSON string representation of the object
print(ManaV2OspfAuthentication.to_json())

# convert the object into a dict
mana_v2_ospf_authentication_dict = mana_v2_ospf_authentication_instance.to_dict()
# create an instance of ManaV2OspfAuthentication from a dict
mana_v2_ospf_authentication_from_dict = ManaV2OspfAuthentication.from_dict(mana_v2_ospf_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


