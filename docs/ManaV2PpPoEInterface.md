# ManaV2PpPoEInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | **str** |  | [optional] 
**dns_servers** | **List[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**last_ipcp_close_reason** | **str** |  | [optional] 
**last_ipv6_cp_close_reason** | **str** |  | [optional] 
**last_lcp_close_reason** | **str** |  | [optional] 
**lcp_echo_failure** | **int** |  | [optional] 
**lcp_echo_interval** | **int** |  | [optional] 
**maximum_receive_unit** | **int** |  | [optional] 
**password** | **str** |  | [optional] 
**peer_ipv4_address** | **str** |  | [optional] 
**peer_ipv6_address** | **str** |  | [optional] 
**ppp_connect_timeout** | **int** |  | [optional] 
**server_mac_address** | **str** |  | [optional] 
**server_name** | **str** |  | [optional] 
**session_id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_pp_po_e_interface import ManaV2PpPoEInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PpPoEInterface from a JSON string
mana_v2_pp_po_e_interface_instance = ManaV2PpPoEInterface.from_json(json)
# print the JSON string representation of the object
print(ManaV2PpPoEInterface.to_json())

# convert the object into a dict
mana_v2_pp_po_e_interface_dict = mana_v2_pp_po_e_interface_instance.to_dict()
# create an instance of ManaV2PpPoEInterface from a dict
mana_v2_pp_po_e_interface_from_dict = ManaV2PpPoEInterface.from_dict(mana_v2_pp_po_e_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


