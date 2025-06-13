# V2SiteSiteIdDetailPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site** | [**V2SiteSiteIdDetailPost200ResponseSite**](V2SiteSiteIdDetailPost200ResponseSite.md) |  | [optional] 
**snapshots** | [**List[V1AlarmHistoryGet200ResponseHistoryInnerTime]**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_site_site_id_detail_post200_response import V2SiteSiteIdDetailPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2SiteSiteIdDetailPost200Response from a JSON string
v2_site_site_id_detail_post200_response_instance = V2SiteSiteIdDetailPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2SiteSiteIdDetailPost200Response.to_json())

# convert the object into a dict
v2_site_site_id_detail_post200_response_dict = v2_site_site_id_detail_post200_response_instance.to_dict()
# create an instance of V2SiteSiteIdDetailPost200Response from a dict
v2_site_site_id_detail_post200_response_from_dict = V2SiteSiteIdDetailPost200Response.from_dict(v2_site_site_id_detail_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


