# V1SitesSiteIdCircuitsGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuits** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInner]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerCircuitsInner.md) |  | [optional] 
**device_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sites_site_id_circuits_get200_response_data_inner import V1SitesSiteIdCircuitsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1SitesSiteIdCircuitsGet200ResponseDataInner from a JSON string
v1_sites_site_id_circuits_get200_response_data_inner_instance = V1SitesSiteIdCircuitsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(V1SitesSiteIdCircuitsGet200ResponseDataInner.to_json())

# convert the object into a dict
v1_sites_site_id_circuits_get200_response_data_inner_dict = v1_sites_site_id_circuits_get200_response_data_inner_instance.to_dict()
# create an instance of V1SitesSiteIdCircuitsGet200ResponseDataInner from a dict
v1_sites_site_id_circuits_get200_response_data_inner_from_dict = V1SitesSiteIdCircuitsGet200ResponseDataInner.from_dict(v1_sites_site_id_circuits_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


