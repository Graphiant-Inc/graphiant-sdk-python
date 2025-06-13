# V1FlowsFlowTablePost200ResponseFlowTableInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_ip** | **str** |  | [optional] 
**dest_port** | **int** |  | [optional] 
**dl_circuit_name** | **str** |  | [optional] 
**dl_usage** | **float** |  | [optional] 
**egress_local_core_region** | **str** |  | [optional] 
**ingress_local_core_region** | **str** |  | [optional] 
**lan_segment** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**remote_core_region** | **str** |  | [optional] 
**sla_class** | **str** |  | [optional] 
**src_ip** | **str** |  | [optional] 
**src_port** | **int** |  | [optional] 
**ts** | [**V1AlarmHistoryGet200ResponseHistoryInnerTime**](V1AlarmHistoryGet200ResponseHistoryInnerTime.md) |  | [optional] 
**ul_circuit_name** | **str** |  | [optional] 
**ul_usage** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_flows_flow_table_post200_response_flow_table_inner import V1FlowsFlowTablePost200ResponseFlowTableInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowsFlowTablePost200ResponseFlowTableInner from a JSON string
v1_flows_flow_table_post200_response_flow_table_inner_instance = V1FlowsFlowTablePost200ResponseFlowTableInner.from_json(json)
# print the JSON string representation of the object
print(V1FlowsFlowTablePost200ResponseFlowTableInner.to_json())

# convert the object into a dict
v1_flows_flow_table_post200_response_flow_table_inner_dict = v1_flows_flow_table_post200_response_flow_table_inner_instance.to_dict()
# create an instance of V1FlowsFlowTablePost200ResponseFlowTableInner from a dict
v1_flows_flow_table_post200_response_flow_table_inner_from_dict = V1FlowsFlowTablePost200ResponseFlowTableInner.from_dict(v1_flows_flow_table_post200_response_flow_table_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


