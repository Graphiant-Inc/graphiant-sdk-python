# V1ExtranetB2bMatchesMatchIdConsumerPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**ManaV2ExtranetServiceConsumerPolicy**](ManaV2ExtranetServiceConsumerPolicy.md) |  | [optional] 
**service_id** | **int** | Producer service id being consumed | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_b2b_matches_match_id_consumer_post_request import V1ExtranetB2bMatchesMatchIdConsumerPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetB2bMatchesMatchIdConsumerPostRequest from a JSON string
v1_extranet_b2b_matches_match_id_consumer_post_request_instance = V1ExtranetB2bMatchesMatchIdConsumerPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetB2bMatchesMatchIdConsumerPostRequest.to_json())

# convert the object into a dict
v1_extranet_b2b_matches_match_id_consumer_post_request_dict = v1_extranet_b2b_matches_match_id_consumer_post_request_instance.to_dict()
# create an instance of V1ExtranetB2bMatchesMatchIdConsumerPostRequest from a dict
v1_extranet_b2b_matches_match_id_consumer_post_request_from_dict = V1ExtranetB2bMatchesMatchIdConsumerPostRequest.from_dict(v1_extranet_b2b_matches_match_id_consumer_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


