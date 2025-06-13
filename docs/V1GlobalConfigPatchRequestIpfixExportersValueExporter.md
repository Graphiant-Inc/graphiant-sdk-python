# V1GlobalConfigPatchRequestIpfixExportersValueExporter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_address** | **str** |  | [optional] 
**destination_port** | **int** |  | [optional] 
**global_id** | **int** |  | [optional] 
**is_global_sync** | **bool** |  | [optional] 
**monitored_segments** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**sample_mode** | **str** |  | [optional] 
**sample_rate** | **int** |  | [optional] 
**source_interface_name** | **str** |  | [optional] 
**vrf_id** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_config_patch_request_ipfix_exporters_value_exporter import V1GlobalConfigPatchRequestIpfixExportersValueExporter

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalConfigPatchRequestIpfixExportersValueExporter from a JSON string
v1_global_config_patch_request_ipfix_exporters_value_exporter_instance = V1GlobalConfigPatchRequestIpfixExportersValueExporter.from_json(json)
# print the JSON string representation of the object
print(V1GlobalConfigPatchRequestIpfixExportersValueExporter.to_json())

# convert the object into a dict
v1_global_config_patch_request_ipfix_exporters_value_exporter_dict = v1_global_config_patch_request_ipfix_exporters_value_exporter_instance.to_dict()
# create an instance of V1GlobalConfigPatchRequestIpfixExportersValueExporter from a dict
v1_global_config_patch_request_ipfix_exporters_value_exporter_from_dict = V1GlobalConfigPatchRequestIpfixExportersValueExporter.from_dict(v1_global_config_patch_request_ipfix_exporters_value_exporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


