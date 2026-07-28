# V1ExtranetB2bProducerIdCustomersGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customers** | [**List[ManaV2ExtranetServiceProducerCustomer]**](ManaV2ExtranetServiceProducerCustomer.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_b2b_producer_id_customers_get_response import V1ExtranetB2bProducerIdCustomersGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetB2bProducerIdCustomersGetResponse from a JSON string
v1_extranet_b2b_producer_id_customers_get_response_instance = V1ExtranetB2bProducerIdCustomersGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetB2bProducerIdCustomersGetResponse.to_json())

# convert the object into a dict
v1_extranet_b2b_producer_id_customers_get_response_dict = v1_extranet_b2b_producer_id_customers_get_response_instance.to_dict()
# create an instance of V1ExtranetB2bProducerIdCustomersGetResponse from a dict
v1_extranet_b2b_producer_id_customers_get_response_from_dict = V1ExtranetB2bProducerIdCustomersGetResponse.from_dict(v1_extranet_b2b_producer_id_customers_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


