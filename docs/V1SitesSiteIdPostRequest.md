# V1SitesSiteIdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site** | [**V1SitesPostRequestSite**](V1SitesPostRequestSite.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sites_site_id_post_request import V1SitesSiteIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SitesSiteIdPostRequest from a JSON string
v1_sites_site_id_post_request_instance = V1SitesSiteIdPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1SitesSiteIdPostRequest.to_json())

# convert the object into a dict
v1_sites_site_id_post_request_dict = v1_sites_site_id_post_request_instance.to_dict()
# create an instance of V1SitesSiteIdPostRequest from a dict
v1_sites_site_id_post_request_from_dict = V1SitesSiteIdPostRequest.from_dict(v1_sites_site_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


