# V1TroubleshootingEnterprisePost200ResponseSitesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_status** | **str** |  | [optional] 
**data_status** | **str** |  | [optional] 
**overall_status** | **str** |  | [optional] 
**region** | [**V2AssuranceTopologyInventoryPost200ResponseRegionsInner**](V2AssuranceTopologyInventoryPost200ResponseRegionsInner.md) |  | [optional] 
**selected_status** | **str** |  | [optional] 
**site_id** | **int** |  | [optional] 
**site_name** | **str** |  | [optional] 
**system_status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_troubleshooting_enterprise_post200_response_sites_inner import V1TroubleshootingEnterprisePost200ResponseSitesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1TroubleshootingEnterprisePost200ResponseSitesInner from a JSON string
v1_troubleshooting_enterprise_post200_response_sites_inner_instance = V1TroubleshootingEnterprisePost200ResponseSitesInner.from_json(json)
# print the JSON string representation of the object
print(V1TroubleshootingEnterprisePost200ResponseSitesInner.to_json())

# convert the object into a dict
v1_troubleshooting_enterprise_post200_response_sites_inner_dict = v1_troubleshooting_enterprise_post200_response_sites_inner_instance.to_dict()
# create an instance of V1TroubleshootingEnterprisePost200ResponseSitesInner from a dict
v1_troubleshooting_enterprise_post200_response_sites_inner_from_dict = V1TroubleshootingEnterprisePost200ResponseSitesInner.from_dict(v1_troubleshooting_enterprise_post200_response_sites_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


