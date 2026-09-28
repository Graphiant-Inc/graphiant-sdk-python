# IamEnterprise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_eula** | **bool** |  | [optional] 
**account_type** | **str** |  | [optional] 
**admin_email** | **str** |  | [optional] 
**backbone_apis_enabled** | **bool** |  | [optional] 
**cloud_provider** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**counts** | [**IamCounts**](IamCounts.md) |  | [optional] 
**credit_limit** | **int** |  | [optional] 
**customers** | [**Dict[str, IamCustomer]**](IamCustomer.md) |  | [optional] 
**description** | **str** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**eula_agreement_date** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**impersonation_enabled** | **bool** |  | [optional] 
**logo** | **str** |  | [optional] 
**marketplace_id** | **str** |  | [optional] 
**parent_company_name** | **str** |  | [optional] 
**parent_enterprise_id** | **int** |  | [optional] 
**portal_banner** | **str** |  | [optional] 
**proxy_tenant_id** | **int** |  | [optional] 
**small_logo** | **str** |  | [optional] 
**token_expiry** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.iam_enterprise import IamEnterprise

# TODO update the JSON string below
json = "{}"
# create an instance of IamEnterprise from a JSON string
iam_enterprise_instance = IamEnterprise.from_json(json)
# print the JSON string representation of the object
print(IamEnterprise.to_json())

# convert the object into a dict
iam_enterprise_dict = iam_enterprise_instance.to_dict()
# create an instance of IamEnterprise from a dict
iam_enterprise_from_dict = IamEnterprise.from_dict(iam_enterprise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


