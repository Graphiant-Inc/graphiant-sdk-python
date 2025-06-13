# V1SitesDetailsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sites** | [**List[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite]**](V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSite.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sites_details_get200_response import V1SitesDetailsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1SitesDetailsGet200Response from a JSON string
v1_sites_details_get200_response_instance = V1SitesDetailsGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1SitesDetailsGet200Response.to_json())

# convert the object into a dict
v1_sites_details_get200_response_dict = v1_sites_details_get200_response_instance.to_dict()
# create an instance of V1SitesDetailsGet200Response from a dict
v1_sites_details_get200_response_from_dict = V1SitesDetailsGet200Response.from_dict(v1_sites_details_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


