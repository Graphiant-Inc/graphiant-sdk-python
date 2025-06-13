# V1TroubleshootingTopSitesByAlertsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_plane** | [**V1TroubleshootingTopSitesByAlertsPost200ResponseControlPlane**](V1TroubleshootingTopSitesByAlertsPost200ResponseControlPlane.md) |  | [optional] 
**data_plane** | [**V1TroubleshootingTopSitesByAlertsPost200ResponseControlPlane**](V1TroubleshootingTopSitesByAlertsPost200ResponseControlPlane.md) |  | [optional] 
**system_plane** | [**V1TroubleshootingTopSitesByAlertsPost200ResponseControlPlane**](V1TroubleshootingTopSitesByAlertsPost200ResponseControlPlane.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_troubleshooting_top_sites_by_alerts_post200_response import V1TroubleshootingTopSitesByAlertsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1TroubleshootingTopSitesByAlertsPost200Response from a JSON string
v1_troubleshooting_top_sites_by_alerts_post200_response_instance = V1TroubleshootingTopSitesByAlertsPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1TroubleshootingTopSitesByAlertsPost200Response.to_json())

# convert the object into a dict
v1_troubleshooting_top_sites_by_alerts_post200_response_dict = v1_troubleshooting_top_sites_by_alerts_post200_response_instance.to_dict()
# create an instance of V1TroubleshootingTopSitesByAlertsPost200Response from a dict
v1_troubleshooting_top_sites_by_alerts_post200_response_from_dict = V1TroubleshootingTopSitesByAlertsPost200Response.from_dict(v1_troubleshooting_top_sites_by_alerts_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


