# V1ExtranetsSourceSegmentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** |  | [optional] 
**target** | [**V1ExtranetsPostRequestPolicyBranches**](V1ExtranetsPostRequestPolicyBranches.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranets_source_segments_post_request import V1ExtranetsSourceSegmentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetsSourceSegmentsPostRequest from a JSON string
v1_extranets_source_segments_post_request_instance = V1ExtranetsSourceSegmentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetsSourceSegmentsPostRequest.to_json())

# convert the object into a dict
v1_extranets_source_segments_post_request_dict = v1_extranets_source_segments_post_request_instance.to_dict()
# create an instance of V1ExtranetsSourceSegmentsPostRequest from a dict
v1_extranets_source_segments_post_request_from_dict = V1ExtranetsSourceSegmentsPostRequest.from_dict(v1_extranets_source_segments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


