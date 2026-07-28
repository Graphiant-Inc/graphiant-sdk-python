# V1ExtranetB2bCustomersIdDetailsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_emails** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**num_sites** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_b2b_customers_id_details_get_response import V1ExtranetB2bCustomersIdDetailsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetB2bCustomersIdDetailsGetResponse from a JSON string
v1_extranet_b2b_customers_id_details_get_response_instance = V1ExtranetB2bCustomersIdDetailsGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetB2bCustomersIdDetailsGetResponse.to_json())

# convert the object into a dict
v1_extranet_b2b_customers_id_details_get_response_dict = v1_extranet_b2b_customers_id_details_get_response_instance.to_dict()
# create an instance of V1ExtranetB2bCustomersIdDetailsGetResponse from a dict
v1_extranet_b2b_customers_id_details_get_response_from_dict = V1ExtranetB2bCustomersIdDetailsGetResponse.from_dict(v1_extranet_b2b_customers_id_details_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


