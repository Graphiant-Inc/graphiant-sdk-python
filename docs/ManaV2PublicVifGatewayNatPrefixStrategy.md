# ManaV2PublicVifGatewayNatPrefixStrategy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**centralized** | [**ManaV2PublicVifGatewayCentralizedNat**](ManaV2PublicVifGatewayCentralizedNat.md) |  | [optional] 
**decentralized** | [**ManaV2PublicVifGatewayDecentralizedPrefixes**](ManaV2PublicVifGatewayDecentralizedPrefixes.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_public_vif_gateway_nat_prefix_strategy import ManaV2PublicVifGatewayNatPrefixStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVifGatewayNatPrefixStrategy from a JSON string
mana_v2_public_vif_gateway_nat_prefix_strategy_instance = ManaV2PublicVifGatewayNatPrefixStrategy.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVifGatewayNatPrefixStrategy.to_json())

# convert the object into a dict
mana_v2_public_vif_gateway_nat_prefix_strategy_dict = mana_v2_public_vif_gateway_nat_prefix_strategy_instance.to_dict()
# create an instance of ManaV2PublicVifGatewayNatPrefixStrategy from a dict
mana_v2_public_vif_gateway_nat_prefix_strategy_from_dict = ManaV2PublicVifGatewayNatPrefixStrategy.from_dict(mana_v2_public_vif_gateway_nat_prefix_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


