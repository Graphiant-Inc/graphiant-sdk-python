from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_flows_flow_table_response_200_flow_table_item_ts import (
        PostV1FlowsFlowTableResponse200FlowTableItemTs,
    )


T = TypeVar("T", bound="PostV1FlowsFlowTableResponse200FlowTableItem")


@_attrs_define
class PostV1FlowsFlowTableResponse200FlowTableItem:
    """
    Attributes:
        dest_ip (Union[Unset, str]):  Example: TYPE_STRING.
        dest_port (Union[Unset, str]):  Example: TYPE_UINT32.
        dl_circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        dl_usage (Union[Unset, str]):  Example: TYPE_DOUBLE.
        egress_local_core_region (Union[Unset, str]):  Example: TYPE_STRING.
        ingress_local_core_region (Union[Unset, str]):  Example: TYPE_STRING.
        lan_segment (Union[Unset, str]):  Example: TYPE_STRING.
        protocol (Union[Unset, str]):  Example: TYPE_STRING.
        remote_core_region (Union[Unset, str]):  Example: TYPE_STRING.
        sla_class (Union[Unset, str]):  Example: TYPE_ENUM.
        src_ip (Union[Unset, str]):  Example: TYPE_STRING.
        src_port (Union[Unset, str]):  Example: TYPE_UINT32.
        ts (Union[Unset, PostV1FlowsFlowTableResponse200FlowTableItemTs]):
        ul_circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        ul_usage (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    dest_ip: Union[Unset, str] = UNSET
    dest_port: Union[Unset, str] = UNSET
    dl_circuit_name: Union[Unset, str] = UNSET
    dl_usage: Union[Unset, str] = UNSET
    egress_local_core_region: Union[Unset, str] = UNSET
    ingress_local_core_region: Union[Unset, str] = UNSET
    lan_segment: Union[Unset, str] = UNSET
    protocol: Union[Unset, str] = UNSET
    remote_core_region: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    src_ip: Union[Unset, str] = UNSET
    src_port: Union[Unset, str] = UNSET
    ts: Union[Unset, "PostV1FlowsFlowTableResponse200FlowTableItemTs"] = UNSET
    ul_circuit_name: Union[Unset, str] = UNSET
    ul_usage: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dest_ip = self.dest_ip

        dest_port = self.dest_port

        dl_circuit_name = self.dl_circuit_name

        dl_usage = self.dl_usage

        egress_local_core_region = self.egress_local_core_region

        ingress_local_core_region = self.ingress_local_core_region

        lan_segment = self.lan_segment

        protocol = self.protocol

        remote_core_region = self.remote_core_region

        sla_class = self.sla_class

        src_ip = self.src_ip

        src_port = self.src_port

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        ul_circuit_name = self.ul_circuit_name

        ul_usage = self.ul_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dest_ip is not UNSET:
            field_dict["destIp"] = dest_ip
        if dest_port is not UNSET:
            field_dict["destPort"] = dest_port
        if dl_circuit_name is not UNSET:
            field_dict["dlCircuitName"] = dl_circuit_name
        if dl_usage is not UNSET:
            field_dict["dlUsage"] = dl_usage
        if egress_local_core_region is not UNSET:
            field_dict["egressLocalCoreRegion"] = egress_local_core_region
        if ingress_local_core_region is not UNSET:
            field_dict["ingressLocalCoreRegion"] = ingress_local_core_region
        if lan_segment is not UNSET:
            field_dict["lanSegment"] = lan_segment
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if remote_core_region is not UNSET:
            field_dict["remoteCoreRegion"] = remote_core_region
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class
        if src_ip is not UNSET:
            field_dict["srcIp"] = src_ip
        if src_port is not UNSET:
            field_dict["srcPort"] = src_port
        if ts is not UNSET:
            field_dict["ts"] = ts
        if ul_circuit_name is not UNSET:
            field_dict["ulCircuitName"] = ul_circuit_name
        if ul_usage is not UNSET:
            field_dict["ulUsage"] = ul_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_flows_flow_table_response_200_flow_table_item_ts import (
            PostV1FlowsFlowTableResponse200FlowTableItemTs,
        )

        d = src_dict.copy()
        dest_ip = d.pop("destIp", UNSET)

        dest_port = d.pop("destPort", UNSET)

        dl_circuit_name = d.pop("dlCircuitName", UNSET)

        dl_usage = d.pop("dlUsage", UNSET)

        egress_local_core_region = d.pop("egressLocalCoreRegion", UNSET)

        ingress_local_core_region = d.pop("ingressLocalCoreRegion", UNSET)

        lan_segment = d.pop("lanSegment", UNSET)

        protocol = d.pop("protocol", UNSET)

        remote_core_region = d.pop("remoteCoreRegion", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        src_ip = d.pop("srcIp", UNSET)

        src_port = d.pop("srcPort", UNSET)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV1FlowsFlowTableResponse200FlowTableItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV1FlowsFlowTableResponse200FlowTableItemTs.from_dict(_ts)

        ul_circuit_name = d.pop("ulCircuitName", UNSET)

        ul_usage = d.pop("ulUsage", UNSET)

        post_v1_flows_flow_table_response_200_flow_table_item = cls(
            dest_ip=dest_ip,
            dest_port=dest_port,
            dl_circuit_name=dl_circuit_name,
            dl_usage=dl_usage,
            egress_local_core_region=egress_local_core_region,
            ingress_local_core_region=ingress_local_core_region,
            lan_segment=lan_segment,
            protocol=protocol,
            remote_core_region=remote_core_region,
            sla_class=sla_class,
            src_ip=src_ip,
            src_port=src_port,
            ts=ts,
            ul_circuit_name=ul_circuit_name,
            ul_usage=ul_usage,
        )

        post_v1_flows_flow_table_response_200_flow_table_item.additional_properties = d
        return post_v1_flows_flow_table_response_200_flow_table_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
