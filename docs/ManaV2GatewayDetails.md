# ManaV2GatewayDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**ManaV2AwsGatewayDetails**](ManaV2AwsGatewayDetails.md) |  | [optional] 
**azure** | [**ManaV2AzureGatewayDetails**](ManaV2AzureGatewayDetails.md) |  | [optional] 
**description** | **str** |  | [optional] 
**gcp** | [**ManaV2GcpGatewayDetails**](ManaV2GcpGatewayDetails.md) |  | [optional] 
**ipsec_gateway** | [**ManaV2IPsecGatewayDetails**](ManaV2IPsecGatewayDetails.md) |  | [optional] 
**ipsec_gateway_peers** | [**ManaV2IPsecGatewayPeersConfig**](ManaV2IPsecGatewayPeersConfig.md) |  | [optional] 
**oci** | [**ManaV2OciGatewayDetails**](ManaV2OciGatewayDetails.md) |  | [optional] 
**region_id** | **int** |  | [optional] 
**speed** | **str** |  | [optional] 
**vrf_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_gateway_details import ManaV2GatewayDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2GatewayDetails from a JSON string
mana_v2_gateway_details_instance = ManaV2GatewayDetails.from_json(json)
# print the JSON string representation of the object
print(ManaV2GatewayDetails.to_json())

# convert the object into a dict
mana_v2_gateway_details_dict = mana_v2_gateway_details_instance.to_dict()
# create an instance of ManaV2GatewayDetails from a dict
mana_v2_gateway_details_from_dict = ManaV2GatewayDetails.from_dict(mana_v2_gateway_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


