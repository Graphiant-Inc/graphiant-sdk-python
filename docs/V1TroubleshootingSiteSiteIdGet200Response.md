# V1TroubleshootingSiteSiteIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_statuses** | [**List[V1TroubleshootingSiteSiteIdGet200ResponseEdgeStatusesInner]**](V1TroubleshootingSiteSiteIdGet200ResponseEdgeStatusesInner.md) |  | [optional] 
**site_name** | **str** |  | [optional] 
**site_status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_troubleshooting_site_site_id_get200_response import V1TroubleshootingSiteSiteIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1TroubleshootingSiteSiteIdGet200Response from a JSON string
v1_troubleshooting_site_site_id_get200_response_instance = V1TroubleshootingSiteSiteIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1TroubleshootingSiteSiteIdGet200Response.to_json())

# convert the object into a dict
v1_troubleshooting_site_site_id_get200_response_dict = v1_troubleshooting_site_site_id_get200_response_instance.to_dict()
# create an instance of V1TroubleshootingSiteSiteIdGet200Response from a dict
v1_troubleshooting_site_site_id_get200_response_from_dict = V1TroubleshootingSiteSiteIdGet200Response.from_dict(v1_troubleshooting_site_site_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


