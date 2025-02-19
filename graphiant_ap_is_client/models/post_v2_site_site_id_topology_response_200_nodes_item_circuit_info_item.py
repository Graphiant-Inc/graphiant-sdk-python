from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2SiteSiteIdTopologyResponse200NodesItemCircuitInfoItem")


@_attrs_define
class PostV2SiteSiteIdTopologyResponse200NodesItemCircuitInfoItem:
    """
    Attributes:
        average_downlink_utilization (Union[Unset, str]):  Example: TYPE_DOUBLE.
        average_uplink_utilization (Union[Unset, str]):  Example: TYPE_DOUBLE.
        circuit_carrier (Union[Unset, str]):  Example: TYPE_STRING.
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        current_downlink_utilization (Union[Unset, str]):  Example: TYPE_DOUBLE.
        current_uplink_utilization (Union[Unset, str]):  Example: TYPE_DOUBLE.
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        jitter (Union[Unset, str]):  Example: TYPE_UINT64.
        label (Union[Unset, str]):  Example: TYPE_ENUM.
        last_resort (Union[Unset, str]):  Example: TYPE_BOOL.
        latency (Union[Unset, str]):  Example: TYPE_UINT64.
        loss (Union[Unset, str]):  Example: TYPE_FLOAT.
        qoe (Union[Unset, str]):  Example: TYPE_FLOAT.
        quality (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    average_downlink_utilization: Union[Unset, str] = UNSET
    average_uplink_utilization: Union[Unset, str] = UNSET
    circuit_carrier: Union[Unset, str] = UNSET
    circuit_name: Union[Unset, str] = UNSET
    current_downlink_utilization: Union[Unset, str] = UNSET
    current_uplink_utilization: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    jitter: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    last_resort: Union[Unset, str] = UNSET
    latency: Union[Unset, str] = UNSET
    loss: Union[Unset, str] = UNSET
    qoe: Union[Unset, str] = UNSET
    quality: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average_downlink_utilization = self.average_downlink_utilization

        average_uplink_utilization = self.average_uplink_utilization

        circuit_carrier = self.circuit_carrier

        circuit_name = self.circuit_name

        current_downlink_utilization = self.current_downlink_utilization

        current_uplink_utilization = self.current_uplink_utilization

        device_id = self.device_id

        interface_name = self.interface_name

        jitter = self.jitter

        label = self.label

        last_resort = self.last_resort

        latency = self.latency

        loss = self.loss

        qoe = self.qoe

        quality = self.quality

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average_downlink_utilization is not UNSET:
            field_dict["averageDownlinkUtilization"] = average_downlink_utilization
        if average_uplink_utilization is not UNSET:
            field_dict["averageUplinkUtilization"] = average_uplink_utilization
        if circuit_carrier is not UNSET:
            field_dict["circuitCarrier"] = circuit_carrier
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if current_downlink_utilization is not UNSET:
            field_dict["currentDownlinkUtilization"] = current_downlink_utilization
        if current_uplink_utilization is not UNSET:
            field_dict["currentUplinkUtilization"] = current_uplink_utilization
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if jitter is not UNSET:
            field_dict["jitter"] = jitter
        if label is not UNSET:
            field_dict["label"] = label
        if last_resort is not UNSET:
            field_dict["lastResort"] = last_resort
        if latency is not UNSET:
            field_dict["latency"] = latency
        if loss is not UNSET:
            field_dict["loss"] = loss
        if qoe is not UNSET:
            field_dict["qoe"] = qoe
        if quality is not UNSET:
            field_dict["quality"] = quality

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        average_downlink_utilization = d.pop("averageDownlinkUtilization", UNSET)

        average_uplink_utilization = d.pop("averageUplinkUtilization", UNSET)

        circuit_carrier = d.pop("circuitCarrier", UNSET)

        circuit_name = d.pop("circuitName", UNSET)

        current_downlink_utilization = d.pop("currentDownlinkUtilization", UNSET)

        current_uplink_utilization = d.pop("currentUplinkUtilization", UNSET)

        device_id = d.pop("deviceId", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        jitter = d.pop("jitter", UNSET)

        label = d.pop("label", UNSET)

        last_resort = d.pop("lastResort", UNSET)

        latency = d.pop("latency", UNSET)

        loss = d.pop("loss", UNSET)

        qoe = d.pop("qoe", UNSET)

        quality = d.pop("quality", UNSET)

        post_v2_site_site_id_topology_response_200_nodes_item_circuit_info_item = cls(
            average_downlink_utilization=average_downlink_utilization,
            average_uplink_utilization=average_uplink_utilization,
            circuit_carrier=circuit_carrier,
            circuit_name=circuit_name,
            current_downlink_utilization=current_downlink_utilization,
            current_uplink_utilization=current_uplink_utilization,
            device_id=device_id,
            interface_name=interface_name,
            jitter=jitter,
            label=label,
            last_resort=last_resort,
            latency=latency,
            loss=loss,
            qoe=qoe,
            quality=quality,
        )

        post_v2_site_site_id_topology_response_200_nodes_item_circuit_info_item.additional_properties = d
        return post_v2_site_site_id_topology_response_200_nodes_item_circuit_info_item

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
