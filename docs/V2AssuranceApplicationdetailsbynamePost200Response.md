# V2AssuranceApplicationdetailsbynamePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id_record** | [**V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord**](V2AssuranceApplicationdetailsbynamePost200ResponseAppIdRecord.md) |  | [optional] 
**app_name_record** | [**V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord**](V2AssuranceApplicationdetailsbynamePost200ResponseAppNameRecord.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_applicationdetailsbyname_post200_response import V2AssuranceApplicationdetailsbynamePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceApplicationdetailsbynamePost200Response from a JSON string
v2_assurance_applicationdetailsbyname_post200_response_instance = V2AssuranceApplicationdetailsbynamePost200Response.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceApplicationdetailsbynamePost200Response.to_json())

# convert the object into a dict
v2_assurance_applicationdetailsbyname_post200_response_dict = v2_assurance_applicationdetailsbyname_post200_response_instance.to_dict()
# create an instance of V2AssuranceApplicationdetailsbynamePost200Response from a dict
v2_assurance_applicationdetailsbyname_post200_response_from_dict = V2AssuranceApplicationdetailsbynamePost200Response.from_dict(v2_assurance_applicationdetailsbyname_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


