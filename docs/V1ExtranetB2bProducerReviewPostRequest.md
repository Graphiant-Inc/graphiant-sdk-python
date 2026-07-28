# V1ExtranetB2bProducerReviewPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**ManaV2ExtranetServiceProducerPolicy**](ManaV2ExtranetServiceProducerPolicy.md) |  | 
**service_name** | **str** |  (required) | 
**service_type** | **str** | Branded extranet service type (peering_service, client_to_server, …) (required) | 

## Example

```python
from graphiant_sdk.models.v1_extranet_b2b_producer_review_post_request import V1ExtranetB2bProducerReviewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetB2bProducerReviewPostRequest from a JSON string
v1_extranet_b2b_producer_review_post_request_instance = V1ExtranetB2bProducerReviewPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetB2bProducerReviewPostRequest.to_json())

# convert the object into a dict
v1_extranet_b2b_producer_review_post_request_dict = v1_extranet_b2b_producer_review_post_request_instance.to_dict()
# create an instance of V1ExtranetB2bProducerReviewPostRequest from a dict
v1_extranet_b2b_producer_review_post_request_from_dict = V1ExtranetB2bProducerReviewPostRequest.from_dict(v1_extranet_b2b_producer_review_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


