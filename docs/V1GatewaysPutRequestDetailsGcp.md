# V1GatewaysPutRequestDetailsGcp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**pairing_key** | **str** |  | [optional] 
**routing_policy** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request_details_gcp import V1GatewaysPutRequestDetailsGcp

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequestDetailsGcp from a JSON string
v1_gateways_put_request_details_gcp_instance = V1GatewaysPutRequestDetailsGcp.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequestDetailsGcp.to_json())

# convert the object into a dict
v1_gateways_put_request_details_gcp_dict = v1_gateways_put_request_details_gcp_instance.to_dict()
# create an instance of V1GatewaysPutRequestDetailsGcp from a dict
v1_gateways_put_request_details_gcp_from_dict = V1GatewaysPutRequestDetailsGcp.from_dict(v1_gateways_put_request_details_gcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


