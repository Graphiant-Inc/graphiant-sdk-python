# V1SiteDetailsSitelistsPost200ResponseSiteListsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**policy_count** | **int** |  | [optional] 
**site_count** | **int** |  | [optional] 
**site_list_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_site_details_sitelists_post200_response_site_lists_inner import V1SiteDetailsSitelistsPost200ResponseSiteListsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1SiteDetailsSitelistsPost200ResponseSiteListsInner from a JSON string
v1_site_details_sitelists_post200_response_site_lists_inner_instance = V1SiteDetailsSitelistsPost200ResponseSiteListsInner.from_json(json)
# print the JSON string representation of the object
print(V1SiteDetailsSitelistsPost200ResponseSiteListsInner.to_json())

# convert the object into a dict
v1_site_details_sitelists_post200_response_site_lists_inner_dict = v1_site_details_sitelists_post200_response_site_lists_inner_instance.to_dict()
# create an instance of V1SiteDetailsSitelistsPost200ResponseSiteListsInner from a dict
v1_site_details_sitelists_post200_response_site_lists_inner_from_dict = V1SiteDetailsSitelistsPost200ResponseSiteListsInner.from_dict(v1_site_details_sitelists_post200_response_site_lists_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


