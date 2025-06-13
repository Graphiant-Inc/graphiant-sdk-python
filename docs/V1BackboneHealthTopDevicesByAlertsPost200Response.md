# V1BackboneHealthTopDevicesByAlertsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_plane** | [**V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlane**](V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlane.md) |  | [optional] 
**data_plane** | [**V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlane**](V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlane.md) |  | [optional] 
**system_plane** | [**V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlane**](V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlane.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_backbone_health_top_devices_by_alerts_post200_response import V1BackboneHealthTopDevicesByAlertsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1BackboneHealthTopDevicesByAlertsPost200Response from a JSON string
v1_backbone_health_top_devices_by_alerts_post200_response_instance = V1BackboneHealthTopDevicesByAlertsPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1BackboneHealthTopDevicesByAlertsPost200Response.to_json())

# convert the object into a dict
v1_backbone_health_top_devices_by_alerts_post200_response_dict = v1_backbone_health_top_devices_by_alerts_post200_response_instance.to_dict()
# create an instance of V1BackboneHealthTopDevicesByAlertsPost200Response from a dict
v1_backbone_health_top_devices_by_alerts_post200_response_from_dict = V1BackboneHealthTopDevicesByAlertsPost200Response.from_dict(v1_backbone_health_top_devices_by_alerts_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


