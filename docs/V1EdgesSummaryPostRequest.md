# V1EdgesSummaryPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**V1EdgesSummaryPostRequestFilter**](V1EdgesSummaryPostRequestFilter.md) |  | [optional] 
**show_excluded** | **bool** | Include devices excluded from Graphiant API lists. Ignored for non-Graphiant callers. Default false. | [optional] 

## Example

```python
from graphiant_sdk.models.v1_edges_summary_post_request import V1EdgesSummaryPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1EdgesSummaryPostRequest from a JSON string
v1_edges_summary_post_request_instance = V1EdgesSummaryPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1EdgesSummaryPostRequest.to_json())

# convert the object into a dict
v1_edges_summary_post_request_dict = v1_edges_summary_post_request_instance.to_dict()
# create an instance of V1EdgesSummaryPostRequest from a dict
v1_edges_summary_post_request_from_dict = V1EdgesSummaryPostRequest.from_dict(v1_edges_summary_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


