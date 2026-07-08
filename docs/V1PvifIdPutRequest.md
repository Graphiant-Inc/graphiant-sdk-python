# V1PvifIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ManaV2PublicVifGatewayWriteRequest**](ManaV2PublicVifGatewayWriteRequest.md) |  | 

## Example

```python
from graphiant_sdk.models.v1_pvif_id_put_request import V1PvifIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1PvifIdPutRequest from a JSON string
v1_pvif_id_put_request_instance = V1PvifIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1PvifIdPutRequest.to_json())

# convert the object into a dict
v1_pvif_id_put_request_dict = v1_pvif_id_put_request_instance.to_dict()
# create an instance of V1PvifIdPutRequest from a dict
v1_pvif_id_put_request_from_dict = V1PvifIdPutRequest.from_dict(v1_pvif_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


