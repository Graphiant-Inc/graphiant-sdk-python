# V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bwusage_region** | [**List[V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetailsBwusageRegionInner]**](V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetailsBwusageRegionInner.md) |  | [optional] 
**bwusage_site** | [**List[V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetailsBwusageSiteInner]**](V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetailsBwusageSiteInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_bwtracker_enterprise_details_post200_response_bwusage_details import V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetails from a JSON string
v1_bwtracker_enterprise_details_post200_response_bwusage_details_instance = V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetails.from_json(json)
# print the JSON string representation of the object
print(V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetails.to_json())

# convert the object into a dict
v1_bwtracker_enterprise_details_post200_response_bwusage_details_dict = v1_bwtracker_enterprise_details_post200_response_bwusage_details_instance.to_dict()
# create an instance of V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetails from a dict
v1_bwtracker_enterprise_details_post200_response_bwusage_details_from_dict = V1BwtrackerEnterpriseDetailsPost200ResponseBwusageDetails.from_dict(v1_bwtracker_enterprise_details_post200_response_bwusage_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


