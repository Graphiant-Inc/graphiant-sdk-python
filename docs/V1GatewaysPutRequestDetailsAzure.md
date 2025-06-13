# V1GatewaysPutRequestDetailsAzure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms_peering_vlan_id** | **int** |  | [optional] 
**routing_policy** | **str** |  | [optional] 
**service_key** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_azure import V1GatewaysPutRequestDetailsAzure

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsAzure from a JSON string
v1_gateways_put_request_details_azure_instance = V1GatewaysPutRequestDetailsAzure.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsAzure.to_json())

# convert the object into a dict
v1_gateways_put_request_details_azure_dict = v1_gateways_put_request_details_azure_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsAzure from a dict
v1_gateways_put_request_details_azure_from_dict = V1GatewaysPutRequestDetailsAzure.from_dict(v1_gateways_put_request_details_azure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


