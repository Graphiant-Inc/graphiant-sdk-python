# V1AdaptiveFecPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ManaV2AdaptiveFecConfiguration**](ManaV2AdaptiveFecConfiguration.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_adaptive_fec_put_request import V1AdaptiveFecPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AdaptiveFecPutRequest from a JSON string
v1_adaptive_fec_put_request_instance = V1AdaptiveFecPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1AdaptiveFecPutRequest.to_json())

# convert the object into a dict
v1_adaptive_fec_put_request_dict = v1_adaptive_fec_put_request_instance.to_dict()
# create an instance of V1AdaptiveFecPutRequest from a dict
v1_adaptive_fec_put_request_from_dict = V1AdaptiveFecPutRequest.from_dict(v1_adaptive_fec_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


