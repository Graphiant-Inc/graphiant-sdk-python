# V1SoftwareRunningDetailsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[V1SoftwareRunningDetailsGet200ResponseDevicesInner]**](V1SoftwareRunningDetailsGet200ResponseDevicesInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_software_running_details_get200_response import V1SoftwareRunningDetailsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1SoftwareRunningDetailsGet200Response from a JSON string
v1_software_running_details_get200_response_instance = V1SoftwareRunningDetailsGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1SoftwareRunningDetailsGet200Response.to_json())

# convert the object into a dict
v1_software_running_details_get200_response_dict = v1_software_running_details_get200_response_instance.to_dict()
# create an instance of V1SoftwareRunningDetailsGet200Response from a dict
v1_software_running_details_get200_response_from_dict = V1SoftwareRunningDetailsGet200Response.from_dict(v1_software_running_details_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


