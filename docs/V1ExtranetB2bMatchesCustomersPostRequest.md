# V1ExtranetB2bMatchesCustomersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customers** | [**List[ManaV2ExtranetServiceProducerCustomer]**](ManaV2ExtranetServiceProducerCustomer.md) |  | [optional] 
**service_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_b2b_matches_customers_post_request import V1ExtranetB2bMatchesCustomersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetB2bMatchesCustomersPostRequest from a JSON string
v1_extranet_b2b_matches_customers_post_request_instance = V1ExtranetB2bMatchesCustomersPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetB2bMatchesCustomersPostRequest.to_json())

# convert the object into a dict
v1_extranet_b2b_matches_customers_post_request_dict = v1_extranet_b2b_matches_customers_post_request_instance.to_dict()
# create an instance of V1ExtranetB2bMatchesCustomersPostRequest from a dict
v1_extranet_b2b_matches_customers_post_request_from_dict = V1ExtranetB2bMatchesCustomersPostRequest.from_dict(v1_extranet_b2b_matches_customers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


