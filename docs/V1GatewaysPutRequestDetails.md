# V1GatewaysPutRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**V1GatewaysPutRequestDetailsAws**](V1GatewaysPutRequestDetailsAws.md) |  | [optional] 
**azure** | [**V1GatewaysPutRequestDetailsAzure**](V1GatewaysPutRequestDetailsAzure.md) |  | [optional] 
**description** | **str** |  | [optional] 
**gcp** | [**V1GatewaysPutRequestDetailsGcp**](V1GatewaysPutRequestDetailsGcp.md) |  | [optional] 
**ipsec_gateway** | [**V1GatewaysPutRequestDetailsIpsecGateway**](V1GatewaysPutRequestDetailsIpsecGateway.md) |  | [optional] 
**oci** | [**V1GatewaysPutRequestDetailsOci**](V1GatewaysPutRequestDetailsOci.md) |  | [optional] 
**region_id** | **int** |  | [optional] 
**speed** | **str** |  | [optional] 
**vrf_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details import V1GatewaysPutRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetails from a JSON string
v1_gateways_put_request_details_instance = V1GatewaysPutRequestDetails.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetails.to_json())

# convert the object into a dict
v1_gateways_put_request_details_dict = v1_gateways_put_request_details_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetails from a dict
v1_gateways_put_request_details_from_dict = V1GatewaysPutRequestDetails.from_dict(v1_gateways_put_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


