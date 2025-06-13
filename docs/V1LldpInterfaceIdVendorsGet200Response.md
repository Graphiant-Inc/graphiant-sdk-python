# V1LldpInterfaceIdVendorsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendors** | [**List[V1LldpInterfaceIdVendorsGet200ResponseVendorsInner]**](V1LldpInterfaceIdVendorsGet200ResponseVendorsInner.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_lldp_interface_id_vendors_get200_response import V1LldpInterfaceIdVendorsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1LldpInterfaceIdVendorsGet200Response from a JSON string
v1_lldp_interface_id_vendors_get200_response_instance = V1LldpInterfaceIdVendorsGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1LldpInterfaceIdVendorsGet200Response.to_json())

# convert the object into a dict
v1_lldp_interface_id_vendors_get200_response_dict = v1_lldp_interface_id_vendors_get200_response_instance.to_dict()
# create an instance of V1LldpInterfaceIdVendorsGet200Response from a dict
v1_lldp_interface_id_vendors_get200_response_from_dict = V1LldpInterfaceIdVendorsGet200Response.from_dict(v1_lldp_interface_id_vendors_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


