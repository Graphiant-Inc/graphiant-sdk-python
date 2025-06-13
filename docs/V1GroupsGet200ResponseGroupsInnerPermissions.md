# V1GroupsGet200ResponseGroupsInnerPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_manager** | **str** |  | [optional] 
**b2b** | **str** |  | [optional] 
**billing_and_invoicing** | **str** |  | [optional] 
**compliance** | **str** |  | [optional] 
**developer_tools** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**global_services** | **str** |  | [optional] 
**insights** | **str** |  | [optional] 
**licensing** | **str** |  | [optional] 
**logs** | **str** |  | [optional] 
**monitoring_and_troubleshooting** | **str** |  | [optional] 
**network_configuration** | **str** |  | [optional] 
**order_status** | **str** |  | [optional] 
**reports** | **str** |  | [optional] 
**safety_and_security** | **str** |  | [optional] 
**service_policies** | **str** |  | [optional] 
**support** | **str** |  | [optional] 
**user_and_tenant_management** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_groups_get200_response_groups_inner_permissions import V1GroupsGet200ResponseGroupsInnerPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of V1GroupsGet200ResponseGroupsInnerPermissions from a JSON string
v1_groups_get200_response_groups_inner_permissions_instance = V1GroupsGet200ResponseGroupsInnerPermissions.from_json(json)
# print the JSON string representation of the object
print(V1GroupsGet200ResponseGroupsInnerPermissions.to_json())

# convert the object into a dict
v1_groups_get200_response_groups_inner_permissions_dict = v1_groups_get200_response_groups_inner_permissions_instance.to_dict()
# create an instance of V1GroupsGet200ResponseGroupsInnerPermissions from a dict
v1_groups_get200_response_groups_inner_permissions_from_dict = V1GroupsGet200ResponseGroupsInnerPermissions.from_dict(v1_groups_get200_response_groups_inner_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


