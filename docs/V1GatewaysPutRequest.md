# V1GatewaysPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**V1GatewaysPutRequestDetails**](V1GatewaysPutRequestDetails.md) |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_gateways_put_request import V1GatewaysPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GatewaysPutRequest from a JSON string
v1_gateways_put_request_instance = V1GatewaysPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1GatewaysPutRequest.to_json())

# convert the object into a dict
v1_gateways_put_request_dict = v1_gateways_put_request_instance.to_dict()
# create an instance of V1GatewaysPutRequest from a dict
v1_gateways_put_request_from_dict = V1GatewaysPutRequest.from_dict(v1_gateways_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


