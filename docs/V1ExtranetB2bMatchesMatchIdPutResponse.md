# V1ExtranetB2bMatchesMatchIdPutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** |  | [optional] 
**match** | [**ManaV2B2bExtranetMatch**](ManaV2B2bExtranetMatch.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_b2b_matches_match_id_put_response import V1ExtranetB2bMatchesMatchIdPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetB2bMatchesMatchIdPutResponse from a JSON string
v1_extranet_b2b_matches_match_id_put_response_instance = V1ExtranetB2bMatchesMatchIdPutResponse.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetB2bMatchesMatchIdPutResponse.to_json())

# convert the object into a dict
v1_extranet_b2b_matches_match_id_put_response_dict = v1_extranet_b2b_matches_match_id_put_response_instance.to_dict()
# create an instance of V1ExtranetB2bMatchesMatchIdPutResponse from a dict
v1_extranet_b2b_matches_match_id_put_response_from_dict = V1ExtranetB2bMatchesMatchIdPutResponse.from_dict(v1_extranet_b2b_matches_match_id_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


