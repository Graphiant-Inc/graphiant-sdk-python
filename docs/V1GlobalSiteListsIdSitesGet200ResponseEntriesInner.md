# V1GlobalSiteListsIdSitesGet200ResponseEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**edge_references** | **int** |  | [optional] 
**site_name** | **str** |  | [optional] 
**tag** | [**List[V1GlobalSiteListsIdSitesGet200ResponseEntriesInnerTagInner]**](V1GlobalSiteListsIdSitesGet200ResponseEntriesInnerTagInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_site_lists_id_sites_get200_response_entries_inner import V1GlobalSiteListsIdSitesGet200ResponseEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalSiteListsIdSitesGet200ResponseEntriesInner from a JSON string
v1_global_site_lists_id_sites_get200_response_entries_inner_instance = V1GlobalSiteListsIdSitesGet200ResponseEntriesInner.from_json(json)
# print the JSON string representation of the object
print(V1GlobalSiteListsIdSitesGet200ResponseEntriesInner.to_json())

# convert the object into a dict
v1_global_site_lists_id_sites_get200_response_entries_inner_dict = v1_global_site_lists_id_sites_get200_response_entries_inner_instance.to_dict()
# create an instance of V1GlobalSiteListsIdSitesGet200ResponseEntriesInner from a dict
v1_global_site_lists_id_sites_get200_response_entries_inner_from_dict = V1GlobalSiteListsIdSitesGet200ResponseEntriesInner.from_dict(v1_global_site_lists_id_sites_get200_response_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


