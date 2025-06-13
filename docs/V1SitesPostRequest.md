# V1SitesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise_id** | **int** |  | [optional] 
**site** | [**V1SitesPostRequestSite**](V1SitesPostRequestSite.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sites_post_request import V1SitesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SitesPostRequest from a JSON string
v1_sites_post_request_instance = V1SitesPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1SitesPostRequest.to_json())

# convert the object into a dict
v1_sites_post_request_dict = v1_sites_post_request_instance.to_dict()
# create an instance of V1SitesPostRequest from a dict
v1_sites_post_request_from_dict = V1SitesPostRequest.from_dict(v1_sites_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


