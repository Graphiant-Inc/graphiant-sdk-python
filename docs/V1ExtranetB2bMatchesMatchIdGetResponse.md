# V1ExtranetB2bMatchesMatchIdGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | **str** |  | [optional] 
**match** | [**ManaV2B2bExtranetMatch**](ManaV2B2bExtranetMatch.md) |  | [optional] 
**match_id** | **int** |  | [optional] 
**service_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_b2b_matches_match_id_get_response import V1ExtranetB2bMatchesMatchIdGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetB2bMatchesMatchIdGetResponse from a JSON string
v1_extranet_b2b_matches_match_id_get_response_instance = V1ExtranetB2bMatchesMatchIdGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetB2bMatchesMatchIdGetResponse.to_json())

# convert the object into a dict
v1_extranet_b2b_matches_match_id_get_response_dict = v1_extranet_b2b_matches_match_id_get_response_instance.to_dict()
# create an instance of V1ExtranetB2bMatchesMatchIdGetResponse from a dict
v1_extranet_b2b_matches_match_id_get_response_from_dict = V1ExtranetB2bMatchesMatchIdGetResponse.from_dict(v1_extranet_b2b_matches_match_id_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


