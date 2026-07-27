# V1ExtranetB2bMatchesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **int** |  | [optional] 
**match** | [**ManaV2B2bExtranetMatch**](ManaV2B2bExtranetMatch.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_b2b_matches_post_request import V1ExtranetB2bMatchesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetB2bMatchesPostRequest from a JSON string
v1_extranet_b2b_matches_post_request_instance = V1ExtranetB2bMatchesPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetB2bMatchesPostRequest.to_json())

# convert the object into a dict
v1_extranet_b2b_matches_post_request_dict = v1_extranet_b2b_matches_post_request_instance.to_dict()
# create an instance of V1ExtranetB2bMatchesPostRequest from a dict
v1_extranet_b2b_matches_post_request_from_dict = V1ExtranetB2bMatchesPostRequest.from_dict(v1_extranet_b2b_matches_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


