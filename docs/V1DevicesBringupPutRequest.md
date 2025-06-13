# V1DevicesBringupPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_ids** | **List[int]** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_devices_bringup_put_request import V1DevicesBringupPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DevicesBringupPutRequest from a JSON string
v1_devices_bringup_put_request_instance = V1DevicesBringupPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1DevicesBringupPutRequest.to_json())

# convert the object into a dict
v1_devices_bringup_put_request_dict = v1_devices_bringup_put_request_instance.to_dict()
# create an instance of V1DevicesBringupPutRequest from a dict
v1_devices_bringup_put_request_from_dict = V1DevicesBringupPutRequest.from_dict(v1_devices_bringup_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


