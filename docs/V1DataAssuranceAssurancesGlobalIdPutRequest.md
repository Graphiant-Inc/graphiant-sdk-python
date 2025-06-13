# V1DataAssuranceAssurancesGlobalIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_removal_reason** | **str** |  | [optional] 
**config** | [**V1DataAssuranceAssurancesGlobalPostRequestConfig**](V1DataAssuranceAssurancesGlobalPostRequestConfig.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_data_assurance_assurances_global_id_put_request import V1DataAssuranceAssurancesGlobalIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DataAssuranceAssurancesGlobalIdPutRequest from a JSON string
v1_data_assurance_assurances_global_id_put_request_instance = V1DataAssuranceAssurancesGlobalIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1DataAssuranceAssurancesGlobalIdPutRequest.to_json())

# convert the object into a dict
v1_data_assurance_assurances_global_id_put_request_dict = v1_data_assurance_assurances_global_id_put_request_instance.to_dict()
# create an instance of V1DataAssuranceAssurancesGlobalIdPutRequest from a dict
v1_data_assurance_assurances_global_id_put_request_from_dict = V1DataAssuranceAssurancesGlobalIdPutRequest.from_dict(v1_data_assurance_assurances_global_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


